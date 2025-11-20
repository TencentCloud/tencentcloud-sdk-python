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
from tencentcloud.btoe.v20210514 import models
from typing import Dict


class BtoeClient(AbstractClient):
    _apiVersion = '2021-05-14'
    _endpoint = 'btoe.tencentcloudapi.com'
    _service = 'btoe'

    async def CreateAudioDeposit(
            self,
            request: models.CreateAudioDepositRequest,
            opts: Dict = None,
    ) -> models.CreateAudioDepositResponse:
        """
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品云API接口下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

        用户通过本接口向BTOE写入待存证的视频的原文件或下载URL，BTOE对视频原文件存储后，将其Hash值存证上链，并生成含有电子签章的区块链存证电子凭证。视频文件支持格式：mp4、avi、mkv、mov、flv,wmv,rmvb,3gp；文件大小限制：直接上传原文件不大于5MB。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVideoDeposit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVideoDepositResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDepositCert(
            self,
            request: models.GetDepositCertRequest,
            opts: Dict = None,
    ) -> models.GetDepositCertResponse:
        """
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品api接口下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

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
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

        用户通过存证编码向BTOE查询存证基本信息。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDepositInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDepositInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyEvidenceBlockChainTxHash(
            self,
            request: models.VerifyEvidenceBlockChainTxHashRequest,
            opts: Dict = None,
    ) -> models.VerifyEvidenceBlockChainTxHashResponse:
        """
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

        用户向BTOE核验存证结果中的区块链交易hash的真实性
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyEvidenceBlockChainTxHash"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyEvidenceBlockChainTxHashResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyEvidenceHash(
            self,
            request: models.VerifyEvidenceHashRequest,
            opts: Dict = None,
    ) -> models.VerifyEvidenceHashResponse:
        """
        腾讯云可信取证产品BTOE已经正常退市，发起退市时间为：2023-12-31，全面停止支持时间是：2024-12-31。安全团队已经做好服务侧告知，根据子类退市规定，需要将该产品控制台下线。

        用户存证内容hash向BTOE核验存证记录的真实性。
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyEvidenceHash"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyEvidenceHashResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)