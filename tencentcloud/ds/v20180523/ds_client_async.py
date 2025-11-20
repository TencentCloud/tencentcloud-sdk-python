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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.ds.v20180523 import models
from typing import Dict


class DsClient(AbstractClient):
    _apiVersion = '2018-05-23'
    _endpoint = 'ds.tencentcloudapi.com'
    _service = 'ds'

    async def CheckVcode(
            self,
            request: models.CheckVcodeRequest,
            opts: Dict = None,
    ) -> models.CheckVcodeResponse:
        """
        检测验证码接口。此接口用于企业电子合同平台通过给用户发送短信验证码，以短信授权方式签署合同。此接口配合发送验证码接口使用。

        用户在企业电子合同平台输入收到的验证码后，由企业电子合同平台调用该接口向腾讯云提交确认受托签署合同验证码命令。验证码验证正确时，本次合同签署的授权成功。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckVcode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckVcodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateContractByUpload(
            self,
            request: models.CreateContractByUploadRequest,
            opts: Dict = None,
    ) -> models.CreateContractByUploadResponse:
        """
        此接口适用于：客户平台通过上传PDF文件作为合同，以备未来进行签署。接口返回任务号，可调用DescribeTaskStatus接口查看任务执行结果。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateContractByUpload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateContractByUploadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEnterpriseAccount(
            self,
            request: models.CreateEnterpriseAccountRequest,
            opts: Dict = None,
    ) -> models.CreateEnterpriseAccountResponse:
        """
        为企业电子合同平台的最终企业用户进行开户。在企业电子合同平台进行操作的企业用户，企业电子合同平台向腾讯云发送企业用户的信息，提交开户命令。腾讯云接到请求后，自动为企业电子合同平台的企业用户生成一张数字证书。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEnterpriseAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEnterpriseAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePersonalAccount(
            self,
            request: models.CreatePersonalAccountRequest,
            opts: Dict = None,
    ) -> models.CreatePersonalAccountResponse:
        """
        为企业电子合同平台的最终个人用户进行开户。在企业电子合同平台进行操作的个人用户，企业电子合同平台向腾讯云发送个人用户的信息，提交开户命令。腾讯云接到请求后，自动为企业电子合同平台的个人用户生成一张数字证书。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePersonalAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePersonalAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSeal(
            self,
            request: models.CreateSealRequest,
            opts: Dict = None,
    ) -> models.CreateSealResponse:
        """
        此接口用于客户电子合同平台增加某用户的印章图片。客户平台可以调用此接口增加某用户的印章图片。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAccount(
            self,
            request: models.DeleteAccountRequest,
            opts: Dict = None,
    ) -> models.DeleteAccountResponse:
        """
        删除企业电子合同平台的最终用户。调用该接口后，腾讯云将删除该用户账号。删除账号后，已经签名的合同不受影响。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAccount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAccountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSeal(
            self,
            request: models.DeleteSealRequest,
            opts: Dict = None,
    ) -> models.DeleteSealResponse:
        """
        删除印章接口，删除指定账号的某个印章
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        接口使用于：客户平台可使用该接口查询任务执行状态或者执行结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadContract(
            self,
            request: models.DownloadContractRequest,
            opts: Dict = None,
    ) -> models.DownloadContractResponse:
        """
        下载合同接口。调用该接口可以下载签署中和签署完成的合同。接口返回任务号，可调用DescribeTaskStatus接口查看任务执行结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadContract"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadContractResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SendVcode(
            self,
            request: models.SendVcodeRequest,
            opts: Dict = None,
    ) -> models.SendVcodeResponse:
        """
        发送验证码接口。此接口用于：企业电子合同平台需要腾讯云发送验证码对其用户进行验证时调用，腾讯云将向其用户联系手机(企业电子合同平台为用户开户时通过接口传入)发送验证码，以验证码授权方式签署合同。用户验证工作由企业电子合同平台自身完成。
        """
        
        kwargs = {}
        kwargs["action"] = "SendVcode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SendVcodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SignContractByCoordinate(
            self,
            request: models.SignContractByCoordinateRequest,
            opts: Dict = None,
    ) -> models.SignContractByCoordinateResponse:
        """
        此接口适用于：客户平台在创建好合同后，由合同签署方对创建的合同内容进行确认，无误后再进行签署。客户平台使用该接口提供详细的PDF文档签名坐标进行签署。
        """
        
        kwargs = {}
        kwargs["action"] = "SignContractByCoordinate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SignContractByCoordinateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SignContractByKeyword(
            self,
            request: models.SignContractByKeywordRequest,
            opts: Dict = None,
    ) -> models.SignContractByKeywordResponse:
        """
        此接口适用于：客户平台在创建好合同后，由合同签署方对创建的合同内容进行确认，无误后再进行签署。客户平台使用该接口对PDF合同文档按照关键字和坐标进行签署。
        """
        
        kwargs = {}
        kwargs["action"] = "SignContractByKeyword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SignContractByKeywordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)