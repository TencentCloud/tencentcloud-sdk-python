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
from tencentcloud.drm.v20181115 import models
from typing import Dict


class DrmClient(AbstractClient):
    _apiVersion = '2018-11-15'
    _endpoint = 'drm.tencentcloudapi.com'
    _service = 'drm'

    async def AddFairPlayPem(
            self,
            request: models.AddFairPlayPemRequest,
            opts: Dict = None,
    ) -> models.AddFairPlayPemResponse:
        """
        本接口用来设置fairplay方案所需的私钥、私钥密钥、ask等信息。
        如需使用fairplay方案，请务必先设置私钥。
        """
        
        kwargs = {}
        kwargs["action"] = "AddFairPlayPem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddFairPlayPemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateEncryptKeys(
            self,
            request: models.CreateEncryptKeysRequest,
            opts: Dict = None,
    ) -> models.CreateEncryptKeysResponse:
        """
        该接口用来设置加密的密钥。注意，同一个content id，只能设置一次！
        """
        
        kwargs = {}
        kwargs["action"] = "CreateEncryptKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateEncryptKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLicense(
            self,
            request: models.CreateLicenseRequest,
            opts: Dict = None,
    ) -> models.CreateLicenseResponse:
        """
        本接口用来生成DRM方案对应的播放许可证，开发者需提供DRM方案类型、内容类型参数，后台将生成许可证后返回许可证数据
        开发者需要转发终端设备发出的许可证请求信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFairPlayPem(
            self,
            request: models.DeleteFairPlayPemRequest,
            opts: Dict = None,
    ) -> models.DeleteFairPlayPemResponse:
        """
        本接口用来删除fairplay方案的私钥、ask等信息
        注：高风险操作，删除后，您将无法使用腾讯云DRM提供的fairplay服务。
        由于缓存，删除操作需要约半小时生效
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFairPlayPem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFairPlayPemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllKeys(
            self,
            request: models.DescribeAllKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeAllKeysResponse:
        """
        本接口用来查询指定DRM类型、ContentType的所有加密密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDRMLicense(
            self,
            request: models.DescribeDRMLicenseRequest,
            opts: Dict = None,
    ) -> models.DescribeDRMLicenseResponse:
        """
        开发者需要指定使用的DRM类型取值 NORMALAES、和需要加密的Track类型取值 SD,ContentType取值 LiveVideo
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDRMLicense"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDRMLicenseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFairPlayPem(
            self,
            request: models.DescribeFairPlayPemRequest,
            opts: Dict = None,
    ) -> models.DescribeFairPlayPemResponse:
        """
        该接口用来查询设置的FairPlay私钥校验信息。可用该接口校验设置的私钥与本身的私钥是否一致。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFairPlayPem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFairPlayPemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeys(
            self,
            request: models.DescribeKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeKeysResponse:
        """
        开发者需要指定使用的DRM类型、和需要加密的Track类型，后台返回加密使用的密钥
        如果加密使用的ContentID没有关联的密钥信息，后台会自动生成新的密钥返回
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateTDRMKey(
            self,
            request: models.GenerateTDRMKeyRequest,
            opts: Dict = None,
    ) -> models.GenerateTDRMKeyResponse:
        """
        开发者需要指定使用的DRM类型取值 NORMALAES、和需要加密的Track类型取值 SD,ContentType取值 LiveVideo
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateTDRMKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateTDRMKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFairPlayPem(
            self,
            request: models.ModifyFairPlayPemRequest,
            opts: Dict = None,
    ) -> models.ModifyFairPlayPemResponse:
        """
        本接口用来设置fairplay方案所需的私钥、私钥密钥、ask等信息。
        如需使用fairplay方案，请务必先设置私钥。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFairPlayPem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFairPlayPemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartEncryption(
            self,
            request: models.StartEncryptionRequest,
            opts: Dict = None,
    ) -> models.StartEncryptionResponse:
        """
        开发者调用该接口，启动一次内容文件的DRM加密工作流。
        注意：该接口已下线。
        """
        
        kwargs = {}
        kwargs["action"] = "StartEncryption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartEncryptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)