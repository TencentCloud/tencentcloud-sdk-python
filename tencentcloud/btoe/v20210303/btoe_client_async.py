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
from tencentcloud.btoe.v20210303 import models
from typing import Dict


class BtoeClient(AbstractClient):
    _apiVersion = '2021-03-03'
    _endpoint = 'btoe.tencentcloudapi.com'
    _service = 'btoe'

    async def CreateAudioDeposit(
            self,
            request: models.CreateAudioDepositRequest,
            opts: Dict = None,
    ) -> models.CreateAudioDepositResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的音频原文件或下载URL，BTOE对音频原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。音频类型支持格式：mp3、wav、wma、midi、flac；原文件上传大小不超过5 MB，下载URL文件大小不超过25 MB。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAudioDeposit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAudioDepositResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataDeposit(
            self,
            request: models.CreateDataDepositRequest,
            opts: Dict = None,
    ) -> models.CreateDataDepositResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的业务数据明文，业务数据明文存证写入后不可修改，BTOE对业务数据明文存证生成含有电子签章的区块链存证电子凭证。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataDeposit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataDepositResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDocDeposit(
            self,
            request: models.CreateDocDepositRequest,
            opts: Dict = None,
    ) -> models.CreateDocDepositResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的文档原文件或下载URL，BTOE对文档原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。文档类型支持格式：doc、docx、xls、xlsx、ppt、pptx、 pdf、html、txt、md、csv；原文件上传大小不超过5 MB，下载URL文件大小不超过10 MB。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDocDeposit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDocDepositResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHashDeposit(
            self,
            request: models.CreateHashDepositRequest,
            opts: Dict = None,
    ) -> models.CreateHashDepositResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHashDeposit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHashDepositResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHashDepositNoCert(
            self,
            request: models.CreateHashDepositNoCertRequest,
            opts: Dict = None,
    ) -> models.CreateHashDepositNoCertResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链，本接口不生成区块链存证电子凭证。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHashDepositNoCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHashDepositNoCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHashDepositNoSeal(
            self,
            request: models.CreateHashDepositNoSealRequest,
            opts: Dict = None,
    ) -> models.CreateHashDepositNoSealResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的原文数据Hash值，BTOE对业务数据Hash值存证上链，并生成无电子签章的区块链存证电子凭证。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHashDepositNoSeal"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHashDepositNoSealResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImageDeposit(
            self,
            request: models.CreateImageDepositRequest,
            opts: Dict = None,
    ) -> models.CreateImageDepositResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的图片原文件或下载URL，BTOE对图片原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。图片类型支持格式：png、jpg、jpeg、bmp、gif、svg；原文件上传大小不超过5 MB，下载URL文件大小不超过10 MB。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImageDeposit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageDepositResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVideoDeposit(
            self,
            request: models.CreateVideoDepositRequest,
            opts: Dict = None,
    ) -> models.CreateVideoDepositResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE写入待存证的视频的原文件或下载URL，BTOE对视频原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。视频文件支持格式：mp4、avi、mkv、mov、flv,wmv,rmvb,3gp；文件大小限制：直接上传原文件不大于5MB，下载URL文件大小不大于200 MB。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoDeposit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoDepositResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWebpageDeposit(
            self,
            request: models.CreateWebpageDepositRequest,
            opts: Dict = None,
    ) -> models.CreateWebpageDepositResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过本接口向BTOE提交待存证网页的URL，BTOE对URL进行网页快照，并将快照图片存储，将网页快照Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。URL格式必须以http、https开头。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWebpageDeposit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWebpageDepositResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDepositCert(
            self,
            request: models.GetDepositCertRequest,
            opts: Dict = None,
    ) -> models.GetDepositCertResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过存证编码向BTOE查询存证电子凭证信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDepositCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDepositCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDepositFile(
            self,
            request: models.GetDepositFileRequest,
            opts: Dict = None,
    ) -> models.GetDepositFileResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过存证编码向BTOE获取存证文件的下载URL。
        -注：Hash类存证、业务数据明文存证不产生存证文件。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDepositFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDepositFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDepositInfo(
            self,
            request: models.GetDepositInfoRequest,
            opts: Dict = None,
    ) -> models.GetDepositInfoResponse:
        """
        功能迭代，已上线更高版本的接口2021-05-14

        用户通过存证编码向BTOE查询存证基本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDepositInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDepositInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)