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
from tencentcloud.ds.v20180523 import models


class DsClient(AbstractClient):
    _apiVersion = '2018-05-23'
    _endpoint = 'ds.tencentcloudapi.com'
    _service = 'ds'


    def CheckVcode(self, request):
        """检测验证码接口。此接口用于企业电子合同平台通过给用户发送短信验证码，以短信授权方式签署合同。此接口配合发送验证码接口使用。

        用户在企业电子合同平台输入收到的验证码后，由企业电子合同平台调用该接口向腾讯云提交确认受托签署合同验证码命令。验证码验证正确时，本次合同签署的授权成功。

        :param request: Request instance for CheckVcode.
        :type request: :class:`tencentcloud.ds.v20180523.models.CheckVcodeRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.CheckVcodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckVcode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckVcodeResponse()
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


    def CreateContractByUpload(self, request):
        """此接口适用于：客户平台通过上传PDF文件作为合同，以备未来进行签署。接口返回任务号，可调用DescribeTaskStatus接口查看任务执行结果。

        :param request: Request instance for CreateContractByUpload.
        :type request: :class:`tencentcloud.ds.v20180523.models.CreateContractByUploadRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.CreateContractByUploadResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateContractByUpload", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContractByUploadResponse()
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


    def CreateEnterpriseAccount(self, request):
        """为企业电子合同平台的最终企业用户进行开户。在企业电子合同平台进行操作的企业用户，企业电子合同平台向腾讯云发送企业用户的信息，提交开户命令。腾讯云接到请求后，自动为企业电子合同平台的企业用户生成一张数字证书。

        :param request: Request instance for CreateEnterpriseAccount.
        :type request: :class:`tencentcloud.ds.v20180523.models.CreateEnterpriseAccountRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.CreateEnterpriseAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateEnterpriseAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateEnterpriseAccountResponse()
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


    def CreatePersonalAccount(self, request):
        """为企业电子合同平台的最终个人用户进行开户。在企业电子合同平台进行操作的个人用户，企业电子合同平台向腾讯云发送个人用户的信息，提交开户命令。腾讯云接到请求后，自动为企业电子合同平台的个人用户生成一张数字证书。

        :param request: Request instance for CreatePersonalAccount.
        :type request: :class:`tencentcloud.ds.v20180523.models.CreatePersonalAccountRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.CreatePersonalAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePersonalAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePersonalAccountResponse()
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


    def CreateSeal(self, request):
        """此接口用于客户电子合同平台增加某用户的印章图片。客户平台可以调用此接口增加某用户的印章图片。

        :param request: Request instance for CreateSeal.
        :type request: :class:`tencentcloud.ds.v20180523.models.CreateSealRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.CreateSealResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSeal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSealResponse()
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


    def DeleteAccount(self, request):
        """删除企业电子合同平台的最终用户。调用该接口后，腾讯云将删除该用户账号。删除账号后，已经签名的合同不受影响。

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.ds.v20180523.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountResponse()
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


    def DeleteSeal(self, request):
        """删除印章接口，删除指定账号的某个印章

        :param request: Request instance for DeleteSeal.
        :type request: :class:`tencentcloud.ds.v20180523.models.DeleteSealRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.DeleteSealResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSeal", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSealResponse()
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


    def DescribeTaskStatus(self, request):
        """接口使用于：客户平台可使用该接口查询任务执行状态或者执行结果

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.ds.v20180523.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskStatusResponse()
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


    def DownloadContract(self, request):
        """下载合同接口。调用该接口可以下载签署中和签署完成的合同。接口返回任务号，可调用DescribeTaskStatus接口查看任务执行结果。

        :param request: Request instance for DownloadContract.
        :type request: :class:`tencentcloud.ds.v20180523.models.DownloadContractRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.DownloadContractResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadContract", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadContractResponse()
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


    def SendVcode(self, request):
        """发送验证码接口。此接口用于：企业电子合同平台需要腾讯云发送验证码对其用户进行验证时调用，腾讯云将向其用户联系手机(企业电子合同平台为用户开户时通过接口传入)发送验证码，以验证码授权方式签署合同。用户验证工作由企业电子合同平台自身完成。

        :param request: Request instance for SendVcode.
        :type request: :class:`tencentcloud.ds.v20180523.models.SendVcodeRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.SendVcodeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SendVcode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SendVcodeResponse()
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


    def SignContractByCoordinate(self, request):
        """此接口适用于：客户平台在创建好合同后，由合同签署方对创建的合同内容进行确认，无误后再进行签署。客户平台使用该接口提供详细的PDF文档签名坐标进行签署。

        :param request: Request instance for SignContractByCoordinate.
        :type request: :class:`tencentcloud.ds.v20180523.models.SignContractByCoordinateRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.SignContractByCoordinateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SignContractByCoordinate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SignContractByCoordinateResponse()
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


    def SignContractByKeyword(self, request):
        """此接口适用于：客户平台在创建好合同后，由合同签署方对创建的合同内容进行确认，无误后再进行签署。客户平台使用该接口对PDF合同文档按照关键字和坐标进行签署。

        :param request: Request instance for SignContractByKeyword.
        :type request: :class:`tencentcloud.ds.v20180523.models.SignContractByKeywordRequest`
        :rtype: :class:`tencentcloud.ds.v20180523.models.SignContractByKeywordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SignContractByKeyword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SignContractByKeywordResponse()
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