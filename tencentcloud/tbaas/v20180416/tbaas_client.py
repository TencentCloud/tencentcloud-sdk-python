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
from tencentcloud.tbaas.v20180416 import models


class TbaasClient(AbstractClient):
    _apiVersion = '2018-04-16'
    _endpoint = 'tbaas.tencentcloudapi.com'
    _service = 'tbaas'


    def ApplyUserCert(self, request):
        """申请用户证书

        :param request: Request instance for ApplyUserCert.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.ApplyUserCertRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.ApplyUserCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyUserCert", params, headers=headers)
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
        """版本升级

        Bcos根据块高查询区块信息

        :param request: Request instance for BlockByNumberHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.BlockByNumberHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.BlockByNumberHandlerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BlockByNumberHandler", params, headers=headers)
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


    def CreateChaincodeAndInstallForUser(self, request):
        """创建并安装合约

        :param request: Request instance for CreateChaincodeAndInstallForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.CreateChaincodeAndInstallForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.CreateChaincodeAndInstallForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateChaincodeAndInstallForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateChaincodeAndInstallForUserResponse()
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


    def DeployDynamicBcosContract(self, request):
        """动态部署并发布Bcos合约

        :param request: Request instance for DeployDynamicBcosContract.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.DeployDynamicBcosContractRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.DeployDynamicBcosContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployDynamicBcosContract", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployDynamicBcosContractResponse()
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


    def DeployDynamicContractHandler(self, request):
        """版本升级

        动态部署合约

        :param request: Request instance for DeployDynamicContractHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.DeployDynamicContractHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.DeployDynamicContractHandlerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeployDynamicContractHandler", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeployDynamicContractHandlerResponse()
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
            headers = request.headers
            body = self.call("DownloadUserCert", params, headers=headers)
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


    def GetBcosBlockByNumber(self, request):
        """使用块高查询Bcos区块信息

        :param request: Request instance for GetBcosBlockByNumber.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBcosBlockByNumberRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBcosBlockByNumberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBcosBlockByNumber", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBcosBlockByNumberResponse()
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


    def GetBcosBlockList(self, request):
        """Bcos分页查询当前群组下的区块列表

        :param request: Request instance for GetBcosBlockList.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBcosBlockListRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBcosBlockListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBcosBlockList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBcosBlockListResponse()
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


    def GetBcosTransByHash(self, request):
        """Bcos根据交易哈希查看交易详细信息

        :param request: Request instance for GetBcosTransByHash.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBcosTransByHashRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBcosTransByHashResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBcosTransByHash", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBcosTransByHashResponse()
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


    def GetBcosTransList(self, request):
        """Bcos分页查询当前群组的交易信息列表

        :param request: Request instance for GetBcosTransList.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBcosTransListRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBcosTransListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBcosTransList", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBcosTransListResponse()
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
            headers = request.headers
            body = self.call("GetBlockList", params, headers=headers)
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
        """版本升级

        Bcos分页查询当前群组下的区块列表

        :param request: Request instance for GetBlockListHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBlockListHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBlockListHandlerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBlockListHandler", params, headers=headers)
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


    def GetBlockTransactionListForUser(self, request):
        """获取区块内的交易列表

        :param request: Request instance for GetBlockTransactionListForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetBlockTransactionListForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetBlockTransactionListForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetBlockTransactionListForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetBlockTransactionListForUserResponse()
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


    def GetChaincodeCompileLogForUser(self, request):
        """获取合约编译日志

        :param request: Request instance for GetChaincodeCompileLogForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeCompileLogForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeCompileLogForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetChaincodeCompileLogForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetChaincodeCompileLogForUserResponse()
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


    def GetChaincodeInitializeResultForUser(self, request):
        """实例化结果查询

        :param request: Request instance for GetChaincodeInitializeResultForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeInitializeResultForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeInitializeResultForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetChaincodeInitializeResultForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetChaincodeInitializeResultForUserResponse()
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


    def GetChaincodeLogForUser(self, request):
        """获取合约容器日志

        :param request: Request instance for GetChaincodeLogForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeLogForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetChaincodeLogForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetChaincodeLogForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetChaincodeLogForUserResponse()
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


    def GetChannelListForUser(self, request):
        """获取通道列表

        :param request: Request instance for GetChannelListForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetChannelListForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetChannelListForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetChannelListForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetChannelListForUserResponse()
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


    def GetClusterListForUser(self, request):
        """获取该用户的网络列表。网络信息中包含组织信息，但仅包含该用户所在组织的信息。

        :param request: Request instance for GetClusterListForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetClusterListForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetClusterListForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetClusterListForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetClusterListForUserResponse()
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
            headers = request.headers
            body = self.call("GetClusterSummary", params, headers=headers)
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
            headers = request.headers
            body = self.call("GetInvokeTx", params, headers=headers)
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
            headers = request.headers
            body = self.call("GetLatesdTransactionList", params, headers=headers)
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


    def GetPeerLogForUser(self, request):
        """获取节点日志

        :param request: Request instance for GetPeerLogForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetPeerLogForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetPeerLogForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetPeerLogForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetPeerLogForUserResponse()
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
        """版本升级

        Bcos根据交易哈希查看交易详细信息

        :param request: Request instance for GetTransByHashHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetTransByHashHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetTransByHashHandlerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTransByHashHandler", params, headers=headers)
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
        """版本升级

        Bcos分页查询当前群组的交易信息列表

        :param request: Request instance for GetTransListHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.GetTransListHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.GetTransListHandlerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTransListHandler", params, headers=headers)
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
            headers = request.headers
            body = self.call("GetTransactionDetailForUser", params, headers=headers)
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


    def InitializeChaincodeForUser(self, request):
        """实例化合约

        :param request: Request instance for InitializeChaincodeForUser.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InitializeChaincodeForUserRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InitializeChaincodeForUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitializeChaincodeForUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitializeChaincodeForUserResponse()
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
            headers = request.headers
            body = self.call("Invoke", params, headers=headers)
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


    def InvokeBcosTrans(self, request):
        """执行Bcos交易，支持动态部署的合约

        :param request: Request instance for InvokeBcosTrans.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InvokeBcosTransRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InvokeBcosTransResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeBcosTrans", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvokeBcosTransResponse()
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


    def InvokeChainMakerContract(self, request):
        """调用长安链合约执行交易

        :param request: Request instance for InvokeChainMakerContract.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.InvokeChainMakerContractRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.InvokeChainMakerContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InvokeChainMakerContract", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InvokeChainMakerContractResponse()
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
            headers = request.headers
            body = self.call("Query", params, headers=headers)
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


    def QueryChainMakerBlockTransaction(self, request):
        """查询长安链指定高度区块的交易

        :param request: Request instance for QueryChainMakerBlockTransaction.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerBlockTransactionRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerBlockTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerBlockTransaction", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryChainMakerBlockTransactionResponse()
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


    def QueryChainMakerContract(self, request):
        """调用长安链合约查询

        :param request: Request instance for QueryChainMakerContract.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerContractRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerContractResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerContract", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryChainMakerContractResponse()
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


    def QueryChainMakerTransaction(self, request):
        """通过交易ID查询长安链交易

        :param request: Request instance for QueryChainMakerTransaction.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerTransactionRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.QueryChainMakerTransactionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryChainMakerTransaction", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryChainMakerTransactionResponse()
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
        """版本升级

        Bcos发送交易

        :param request: Request instance for SendTransactionHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.SendTransactionHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.SendTransactionHandlerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SendTransactionHandler", params, headers=headers)
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
            headers = request.headers
            body = self.call("SrvInvoke", params, headers=headers)
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


    def TransByDynamicContractHandler(self, request):
        """版本升级

        根据动态部署的合约发送交易

        :param request: Request instance for TransByDynamicContractHandler.
        :type request: :class:`tencentcloud.tbaas.v20180416.models.TransByDynamicContractHandlerRequest`
        :rtype: :class:`tencentcloud.tbaas.v20180416.models.TransByDynamicContractHandlerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransByDynamicContractHandler", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransByDynamicContractHandlerResponse()
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