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
from tencentcloud.kms.v20190118 import models
from typing import Dict


class KmsClient(AbstractClient):
    _apiVersion = '2019-01-18'
    _endpoint = 'kms.tencentcloudapi.com'
    _service = 'kms'

    async def ArchiveKey(
            self,
            request: models.ArchiveKeyRequest,
            opts: Dict = None,
    ) -> models.ArchiveKeyResponse:
        """
        对密钥进行归档，被归档的密钥只能用于解密，不能加密
        """
        
        kwargs = {}
        kwargs["action"] = "ArchiveKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ArchiveKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AsymmetricRsaDecrypt(
            self,
            request: models.AsymmetricRsaDecryptRequest,
            opts: Dict = None,
    ) -> models.AsymmetricRsaDecryptResponse:
        """
        使用指定的RSA非对称密钥的私钥进行数据解密，密文必须是使用对应公钥加密的。处于Enabled 状态的非对称密钥才能进行解密操作。
        """
        
        kwargs = {}
        kwargs["action"] = "AsymmetricRsaDecrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AsymmetricRsaDecryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AsymmetricSm2Decrypt(
            self,
            request: models.AsymmetricSm2DecryptRequest,
            opts: Dict = None,
    ) -> models.AsymmetricSm2DecryptResponse:
        """
        使用指定的SM2非对称密钥的私钥进行数据解密，密文必须是使用对应公钥加密的。处于Enabled 状态的非对称密钥才能进行解密操作。传入的密文的长度不能超过256字节。
        """
        
        kwargs = {}
        kwargs["action"] = "AsymmetricSm2Decrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AsymmetricSm2DecryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindCloudResource(
            self,
            request: models.BindCloudResourceRequest,
            opts: Dict = None,
    ) -> models.BindCloudResourceResponse:
        """
        记录当前key被哪个云产品的那个资源所使用。如果当前key设置了自动过期，则取消该设置，确保当前key不会自动失效。如果当前关联关系已经创建，也返回成功。
        """
        
        kwargs = {}
        kwargs["action"] = "BindCloudResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindCloudResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelDataKeyDeletion(
            self,
            request: models.CancelDataKeyDeletionRequest,
            opts: Dict = None,
    ) -> models.CancelDataKeyDeletionResponse:
        """
        取消计划删除数据密钥
        """
        
        kwargs = {}
        kwargs["action"] = "CancelDataKeyDeletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelDataKeyDeletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelKeyArchive(
            self,
            request: models.CancelKeyArchiveRequest,
            opts: Dict = None,
    ) -> models.CancelKeyArchiveResponse:
        """
        取消密钥归档，取消后密钥的状态变为Enabled。
        """
        
        kwargs = {}
        kwargs["action"] = "CancelKeyArchive"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelKeyArchiveResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelKeyDeletion(
            self,
            request: models.CancelKeyDeletionRequest,
            opts: Dict = None,
    ) -> models.CancelKeyDeletionResponse:
        """
        取消CMK的计划删除操作
        """
        
        kwargs = {}
        kwargs["action"] = "CancelKeyDeletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelKeyDeletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKey(
            self,
            request: models.CreateKeyRequest,
            opts: Dict = None,
    ) -> models.CreateKeyResponse:
        """
        创建用户管理数据密钥的主密钥CMK（Custom Master Key）。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWhiteBoxKey(
            self,
            request: models.CreateWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.CreateWhiteBoxKeyResponse:
        """
        创建白盒密钥。 密钥个数的上限为 50。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Decrypt(
            self,
            request: models.DecryptRequest,
            opts: Dict = None,
    ) -> models.DecryptResponse:
        """
        本接口用于解密密文，得到明文数据。
        """
        
        kwargs = {}
        kwargs["action"] = "Decrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DecryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImportedKeyMaterial(
            self,
            request: models.DeleteImportedKeyMaterialRequest,
            opts: Dict = None,
    ) -> models.DeleteImportedKeyMaterialResponse:
        """
        用于删除导入的密钥材料，仅对EXTERNAL类型的CMK有效，该接口将CMK设置为PendingImport 状态，并不会删除CMK，在重新进行密钥导入后可继续使用。彻底删除CMK请使用 ScheduleKeyDeletion 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImportedKeyMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImportedKeyMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWhiteBoxKey(
            self,
            request: models.DeleteWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.DeleteWhiteBoxKeyResponse:
        """
        删除白盒密钥, 注意：必须先禁用后，才可以删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataKey(
            self,
            request: models.DescribeDataKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeDataKeyResponse:
        """
        获取数据密钥的详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataKeys(
            self,
            request: models.DescribeDataKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeDataKeysResponse:
        """
        返回数据密钥属性信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKey(
            self,
            request: models.DescribeKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeKeyResponse:
        """
        用于获取指定KeyId的主密钥属性详情信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKeys(
            self,
            request: models.DescribeKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeKeysResponse:
        """
        该接口用于批量获取主密钥属性信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxDecryptKey(
            self,
            request: models.DescribeWhiteBoxDecryptKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxDecryptKeyResponse:
        """
        获取白盒解密密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxDecryptKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxDecryptKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxDeviceFingerprints(
            self,
            request: models.DescribeWhiteBoxDeviceFingerprintsRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxDeviceFingerprintsResponse:
        """
        获取指定密钥的设备指纹列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxDeviceFingerprints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxDeviceFingerprintsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxKey(
            self,
            request: models.DescribeWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxKeyResponse:
        """
        展示白盒密钥的信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxKeyDetails(
            self,
            request: models.DescribeWhiteBoxKeyDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxKeyDetailsResponse:
        """
        获取白盒密钥列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxKeyDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxKeyDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWhiteBoxServiceStatus(
            self,
            request: models.DescribeWhiteBoxServiceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeWhiteBoxServiceStatusResponse:
        """
        获取白盒密钥服务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWhiteBoxServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWhiteBoxServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableDataKey(
            self,
            request: models.DisableDataKeyRequest,
            opts: Dict = None,
    ) -> models.DisableDataKeyResponse:
        """
        禁用数据密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DisableDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableDataKeys(
            self,
            request: models.DisableDataKeysRequest,
            opts: Dict = None,
    ) -> models.DisableDataKeysResponse:
        """
        批量禁用数据密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DisableDataKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableDataKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableKey(
            self,
            request: models.DisableKeyRequest,
            opts: Dict = None,
    ) -> models.DisableKeyResponse:
        """
        本接口用于禁用一个主密钥，处于禁用状态的Key无法用于加密、解密操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableKeyRotation(
            self,
            request: models.DisableKeyRotationRequest,
            opts: Dict = None,
    ) -> models.DisableKeyRotationResponse:
        """
        对指定的CMK禁止密钥轮换功能。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableKeyRotation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableKeyRotationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableKeys(
            self,
            request: models.DisableKeysRequest,
            opts: Dict = None,
    ) -> models.DisableKeysResponse:
        """
        该接口用于批量禁止CMK的使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableWhiteBoxKey(
            self,
            request: models.DisableWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.DisableWhiteBoxKeyResponse:
        """
        禁用白盒密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DisableWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableWhiteBoxKeys(
            self,
            request: models.DisableWhiteBoxKeysRequest,
            opts: Dict = None,
    ) -> models.DisableWhiteBoxKeysResponse:
        """
        批量禁用白盒密钥
        """
        
        kwargs = {}
        kwargs["action"] = "DisableWhiteBoxKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableWhiteBoxKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableDataKey(
            self,
            request: models.EnableDataKeyRequest,
            opts: Dict = None,
    ) -> models.EnableDataKeyResponse:
        """
        启用数据密钥
        """
        
        kwargs = {}
        kwargs["action"] = "EnableDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableDataKeys(
            self,
            request: models.EnableDataKeysRequest,
            opts: Dict = None,
    ) -> models.EnableDataKeysResponse:
        """
        批量启用数据密钥
        """
        
        kwargs = {}
        kwargs["action"] = "EnableDataKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableDataKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableKey(
            self,
            request: models.EnableKeyRequest,
            opts: Dict = None,
    ) -> models.EnableKeyResponse:
        """
        用于启用一个指定的CMK。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableKeyRotation(
            self,
            request: models.EnableKeyRotationRequest,
            opts: Dict = None,
    ) -> models.EnableKeyRotationResponse:
        """
        对指定的CMK开启密钥轮换功能。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableKeyRotation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableKeyRotationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableKeys(
            self,
            request: models.EnableKeysRequest,
            opts: Dict = None,
    ) -> models.EnableKeysResponse:
        """
        该接口用于批量启用CMK。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableWhiteBoxKey(
            self,
            request: models.EnableWhiteBoxKeyRequest,
            opts: Dict = None,
    ) -> models.EnableWhiteBoxKeyResponse:
        """
        启用白盒密钥
        """
        
        kwargs = {}
        kwargs["action"] = "EnableWhiteBoxKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableWhiteBoxKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableWhiteBoxKeys(
            self,
            request: models.EnableWhiteBoxKeysRequest,
            opts: Dict = None,
    ) -> models.EnableWhiteBoxKeysResponse:
        """
        批量启用白盒密钥
        """
        
        kwargs = {}
        kwargs["action"] = "EnableWhiteBoxKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableWhiteBoxKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def Encrypt(
            self,
            request: models.EncryptRequest,
            opts: Dict = None,
    ) -> models.EncryptResponse:
        """
        本接口用于加密最多为4KB任意数据，可用于加密数据库密码，RSA Key，或其它较小的敏感信息。对于应用的数据加密，使用GenerateDataKey生成的DataKey进行本地数据的加解密操作
        """
        
        kwargs = {}
        kwargs["action"] = "Encrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EncryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EncryptByWhiteBox(
            self,
            request: models.EncryptByWhiteBoxRequest,
            opts: Dict = None,
    ) -> models.EncryptByWhiteBoxResponse:
        """
        使用白盒密钥进行加密
        """
        
        kwargs = {}
        kwargs["action"] = "EncryptByWhiteBox"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EncryptByWhiteBoxResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateDataKey(
            self,
            request: models.GenerateDataKeyRequest,
            opts: Dict = None,
    ) -> models.GenerateDataKeyResponse:
        """
        本接口生成一个数据密钥，您可以用这个密钥进行本地数据的加密。
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateRandom(
            self,
            request: models.GenerateRandomRequest,
            opts: Dict = None,
    ) -> models.GenerateRandomResponse:
        """
        随机数生成接口。
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateRandom"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateRandomResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataKeyCiphertextBlob(
            self,
            request: models.GetDataKeyCiphertextBlobRequest,
            opts: Dict = None,
    ) -> models.GetDataKeyCiphertextBlobResponse:
        """
        下载数据密钥密文
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataKeyCiphertextBlob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataKeyCiphertextBlobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataKeyPlaintext(
            self,
            request: models.GetDataKeyPlaintextRequest,
            opts: Dict = None,
    ) -> models.GetDataKeyPlaintextResponse:
        """
        获取数据密钥明文
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataKeyPlaintext"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataKeyPlaintextResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetKeyRotationStatus(
            self,
            request: models.GetKeyRotationStatusRequest,
            opts: Dict = None,
    ) -> models.GetKeyRotationStatusResponse:
        """
        查询指定的CMK是否开启了密钥轮换功能。
        """
        
        kwargs = {}
        kwargs["action"] = "GetKeyRotationStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetKeyRotationStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetParametersForImport(
            self,
            request: models.GetParametersForImportRequest,
            opts: Dict = None,
    ) -> models.GetParametersForImportResponse:
        """
        获取导入主密钥（CMK）材料的参数，返回的Token作为执行ImportKeyMaterial的参数之一，返回的PublicKey用于对自主导入密钥材料进行加密。返回的Token和PublicKey 24小时后失效，失效后如需重新导入，需要再次调用该接口获取新的Token和PublicKey。
        """
        
        kwargs = {}
        kwargs["action"] = "GetParametersForImport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetParametersForImportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPublicKey(
            self,
            request: models.GetPublicKeyRequest,
            opts: Dict = None,
    ) -> models.GetPublicKeyResponse:
        """
        该接口用于获取非对称密钥的公钥信息，可用于本地数据加密或验签。只有处于Enabled状态的非对称密钥才可能获取公钥。
        """
        
        kwargs = {}
        kwargs["action"] = "GetPublicKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPublicKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRegions(
            self,
            request: models.GetRegionsRequest,
            opts: Dict = None,
    ) -> models.GetRegionsResponse:
        """
        获取可以提供KMS服务的地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetServiceStatus(
            self,
            request: models.GetServiceStatusRequest,
            opts: Dict = None,
    ) -> models.GetServiceStatusResponse:
        """
        用于查询该用户是否已开通KMS服务
        """
        
        kwargs = {}
        kwargs["action"] = "GetServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportDataKey(
            self,
            request: models.ImportDataKeyRequest,
            opts: Dict = None,
    ) -> models.ImportDataKeyResponse:
        """
        数据密钥导入接口，并托管到KMS
        """
        
        kwargs = {}
        kwargs["action"] = "ImportDataKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportDataKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportKeyMaterial(
            self,
            request: models.ImportKeyMaterialRequest,
            opts: Dict = None,
    ) -> models.ImportKeyMaterialResponse:
        """
        用于导入密钥材料。只有类型为EXTERNAL 的CMK 才可以导入，导入的密钥材料使用 GetParametersForImport 获取的密钥进行加密。可以为指定的 CMK 重新导入密钥材料，并重新指定过期时间，但必须导入相同的密钥材料。CMK 密钥材料导入后不可以更换密钥材料。导入的密钥材料过期或者被删除后，指定的CMK将无法使用，需要再次导入相同的密钥材料才能正常使用。CMK是独立的，同样的密钥材料可导入不同的 CMK 中，但使用其中一个 CMK 加密的数据无法使用另一个 CMK解密。
        只有Enabled 和 PendingImport状态的CMK可以导入密钥材料。
        """
        
        kwargs = {}
        kwargs["action"] = "ImportKeyMaterial"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportKeyMaterialResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAlgorithms(
            self,
            request: models.ListAlgorithmsRequest,
            opts: Dict = None,
    ) -> models.ListAlgorithmsResponse:
        """
        列出当前Region支持的加密方式
        """
        
        kwargs = {}
        kwargs["action"] = "ListAlgorithms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAlgorithmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDataKeyDetail(
            self,
            request: models.ListDataKeyDetailRequest,
            opts: Dict = None,
    ) -> models.ListDataKeyDetailResponse:
        """
        根据指定Offset和Limit获取数据密钥列表详情。
        """
        
        kwargs = {}
        kwargs["action"] = "ListDataKeyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDataKeyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDataKeys(
            self,
            request: models.ListDataKeysRequest,
            opts: Dict = None,
    ) -> models.ListDataKeysResponse:
        """
        用于查询数据密钥的列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListDataKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDataKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListKeyDetail(
            self,
            request: models.ListKeyDetailRequest,
            opts: Dict = None,
    ) -> models.ListKeyDetailResponse:
        """
        根据指定Offset和Limit获取主密钥列表详情。
        """
        
        kwargs = {}
        kwargs["action"] = "ListKeyDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListKeyDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListKeys(
            self,
            request: models.ListKeysRequest,
            opts: Dict = None,
    ) -> models.ListKeysResponse:
        """
        列出账号下面状态为Enabled， Disabled 和 PendingImport 的CMK KeyId 列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OverwriteWhiteBoxDeviceFingerprints(
            self,
            request: models.OverwriteWhiteBoxDeviceFingerprintsRequest,
            opts: Dict = None,
    ) -> models.OverwriteWhiteBoxDeviceFingerprintsResponse:
        """
        覆盖指定密钥的设备指纹信息
        """
        
        kwargs = {}
        kwargs["action"] = "OverwriteWhiteBoxDeviceFingerprints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OverwriteWhiteBoxDeviceFingerprintsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostQuantumCryptoDecrypt(
            self,
            request: models.PostQuantumCryptoDecryptRequest,
            opts: Dict = None,
    ) -> models.PostQuantumCryptoDecryptResponse:
        """
        本接口使用后量子密码算法密钥，解密密文，并得到明文数据。
        """
        
        kwargs = {}
        kwargs["action"] = "PostQuantumCryptoDecrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostQuantumCryptoDecryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostQuantumCryptoEncrypt(
            self,
            request: models.PostQuantumCryptoEncryptRequest,
            opts: Dict = None,
    ) -> models.PostQuantumCryptoEncryptResponse:
        """
        本接口使用后量子密码算法密钥，可加密最多为4KB任意数据，可用于加密数据库密码，RSA Key，或其它较小的敏感信息。对于应用的数据加密，使用GenerateDataKey生成的DataKey进行本地数据的加解密操作。
        """
        
        kwargs = {}
        kwargs["action"] = "PostQuantumCryptoEncrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostQuantumCryptoEncryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostQuantumCryptoSign(
            self,
            request: models.PostQuantumCryptoSignRequest,
            opts: Dict = None,
    ) -> models.PostQuantumCryptoSignResponse:
        """
        使用后量子密码算法签名验签密钥进行签名。
        """
        
        kwargs = {}
        kwargs["action"] = "PostQuantumCryptoSign"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostQuantumCryptoSignResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PostQuantumCryptoVerify(
            self,
            request: models.PostQuantumCryptoVerifyRequest,
            opts: Dict = None,
    ) -> models.PostQuantumCryptoVerifyResponse:
        """
        使用后量子密码算法密钥对签名进行验证。
        """
        
        kwargs = {}
        kwargs["action"] = "PostQuantumCryptoVerify"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PostQuantumCryptoVerifyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReEncrypt(
            self,
            request: models.ReEncryptRequest,
            opts: Dict = None,
    ) -> models.ReEncryptResponse:
        """
        使用指定CMK对密文重新加密。
        """
        
        kwargs = {}
        kwargs["action"] = "ReEncrypt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReEncryptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScheduleDataKeyDeletion(
            self,
            request: models.ScheduleDataKeyDeletionRequest,
            opts: Dict = None,
    ) -> models.ScheduleDataKeyDeletionResponse:
        """
        计划删除数据密钥
        """
        
        kwargs = {}
        kwargs["action"] = "ScheduleDataKeyDeletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScheduleDataKeyDeletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScheduleKeyDeletion(
            self,
            request: models.ScheduleKeyDeletionRequest,
            opts: Dict = None,
    ) -> models.ScheduleKeyDeletionResponse:
        """
        CMK计划删除接口，用于指定CMK删除的时间，可选时间区间为[7,30]天
        """
        
        kwargs = {}
        kwargs["action"] = "ScheduleKeyDeletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScheduleKeyDeletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SignByAsymmetricKey(
            self,
            request: models.SignByAsymmetricKeyRequest,
            opts: Dict = None,
    ) -> models.SignByAsymmetricKeyResponse:
        """
        非对称密钥签名。
        注意：只有 KeyUsage 为 ASYMMETRIC_SIGN_VERIFY_SM2、ASYMMETRIC_SIGN_VERIFY_ECC 或其他支持的 ASYMMETRIC_SIGN_VERIFY_${ALGORITHM} 的密钥才可以使用签名功能。
        """
        
        kwargs = {}
        kwargs["action"] = "SignByAsymmetricKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SignByAsymmetricKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindCloudResource(
            self,
            request: models.UnbindCloudResourceRequest,
            opts: Dict = None,
    ) -> models.UnbindCloudResourceResponse:
        """
        删除指定（key, 资源，云产品）的记录，以表明：指定的云产品的资源已不再使用当前的key。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindCloudResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindCloudResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAlias(
            self,
            request: models.UpdateAliasRequest,
            opts: Dict = None,
    ) -> models.UpdateAliasResponse:
        """
        用于修改CMK的别名。对于处于PendingDelete状态的CMK禁止修改。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataKeyDescription(
            self,
            request: models.UpdateDataKeyDescriptionRequest,
            opts: Dict = None,
    ) -> models.UpdateDataKeyDescriptionResponse:
        """
        修改数据密钥描述
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataKeyDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataKeyDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataKeyName(
            self,
            request: models.UpdateDataKeyNameRequest,
            opts: Dict = None,
    ) -> models.UpdateDataKeyNameResponse:
        """
        修改数据密钥名称
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataKeyName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataKeyNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateKeyDescription(
            self,
            request: models.UpdateKeyDescriptionRequest,
            opts: Dict = None,
    ) -> models.UpdateKeyDescriptionResponse:
        """
        该接口用于对指定的cmk修改描述信息。对于处于PendingDelete状态的CMK禁止修改。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateKeyDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateKeyDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyByAsymmetricKey(
            self,
            request: models.VerifyByAsymmetricKeyRequest,
            opts: Dict = None,
    ) -> models.VerifyByAsymmetricKeyResponse:
        """
        使用非对称密钥验签
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyByAsymmetricKey"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyByAsymmetricKeyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)