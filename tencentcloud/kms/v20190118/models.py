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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AlgorithmInfo(AbstractModel):
    """算法的名称 和 标识

    """

    def __init__(self):
        """
        :param KeyUsage: 算法的标识\n        :type KeyUsage: str\n        :param Algorithm: 算法的名称\n        :type Algorithm: str\n        """
        self.KeyUsage = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.KeyUsage = params.get("KeyUsage")
        self.Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveKeyRequest(AbstractModel):
    """ArchiveKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveKeyResponse(AbstractModel):
    """ArchiveKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AsymmetricRsaDecryptRequest(AbstractModel):
    """AsymmetricRsaDecrypt请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标识\n        :type KeyId: str\n        :param Ciphertext: 使用PublicKey加密的密文，Base64编码\n        :type Ciphertext: str\n        :param Algorithm: 在使用公钥加密时对应的算法：当前支持RSAES_PKCS1_V1_5、RSAES_OAEP_SHA_1、RSAES_OAEP_SHA_256\n        :type Algorithm: str\n        """
        self.KeyId = None
        self.Ciphertext = None
        self.Algorithm = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Ciphertext = params.get("Ciphertext")
        self.Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsymmetricRsaDecryptResponse(AbstractModel):
    """AsymmetricRsaDecrypt返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标识\n        :type KeyId: str\n        :param Plaintext: 解密后的明文，base64编码\n        :type Plaintext: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class AsymmetricSm2DecryptRequest(AbstractModel):
    """AsymmetricSm2Decrypt请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标识\n        :type KeyId: str\n        :param Ciphertext: 使用PublicKey加密的密文，Base64编码。密文长度不能超过256字节。\n        :type Ciphertext: str\n        """
        self.KeyId = None
        self.Ciphertext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Ciphertext = params.get("Ciphertext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsymmetricSm2DecryptResponse(AbstractModel):
    """AsymmetricSm2Decrypt返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标识\n        :type KeyId: str\n        :param Plaintext: 解密后的明文，base64编码\n        :type Plaintext: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class BindCloudResourceRequest(AbstractModel):
    """BindCloudResource请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: cmk的ID\n        :type KeyId: str\n        :param ProductId: 云产品的唯一性标识符\n        :type ProductId: str\n        :param ResourceId: 资源/实例ID，由调用方根据自己的云产品特征来定义，以字符串形式做存储。\n        :type ResourceId: str\n        """
        self.KeyId = None
        self.ProductId = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.ProductId = params.get("ProductId")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudResourceResponse(AbstractModel):
    """BindCloudResource返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelKeyArchiveRequest(AbstractModel):
    """CancelKeyArchive请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKeyArchiveResponse(AbstractModel):
    """CancelKeyArchive返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CancelKeyDeletionRequest(AbstractModel):
    """CancelKeyDeletion请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 需要被取消删除的CMK的唯一标志\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKeyDeletionResponse(AbstractModel):
    """CancelKeyDeletion返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 唯一标志被取消删除的CMK。\n        :type KeyId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class CreateKeyRequest(AbstractModel):
    """CreateKey请求参数结构体

    """

    def __init__(self):
        """
        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合，首字符必须为字母或者数字。以 kms- 作为前缀的用于云产品使用，Alias 不可重复。\n        :type Alias: str\n        :param Description: CMK 的描述，最大1024字节\n        :type Description: str\n        :param KeyUsage: 指定key的用途，默认为  "ENCRYPT_DECRYPT" 表示创建对称加解密密钥，其它支持用途 “ASYMMETRIC_DECRYPT_RSA_2048” 表示创建用于加解密的RSA2048非对称密钥，“ASYMMETRIC_DECRYPT_SM2” 表示创建用于加解密的SM2非对称密钥, “ASYMMETRIC_SIGN_VERIFY_SM2” 表示创建用于签名验签的SM2非对称密钥, “ASYMMETRIC_SIGN_VERIFY_ECC” 表示创建用于签名验签的ECC非对称密钥, “ASYMMETRIC_SIGN_VERIFY_RSA_2048” 表示创建用于签名验签的RSA_2048非对称密钥\n        :type KeyUsage: str\n        :param Type: 指定key类型，默认为1，1表示默认类型，由KMS创建CMK密钥，2 表示EXTERNAL 类型，该类型需要用户导入密钥材料，参考 GetParametersForImport 和 ImportKeyMaterial 接口\n        :type Type: int\n        :param Tags: 标签列表\n        :type Tags: list of Tag\n        """
        self.Alias = None
        self.Description = None
        self.KeyUsage = None
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.Description = params.get("Description")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyResponse(AbstractModel):
    """CreateKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识符\n        :type KeyId: str\n        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名\n        :type Alias: str\n        :param CreateTime: 密钥创建时间，unix时间戳\n        :type CreateTime: int\n        :param Description: CMK的描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param KeyState: CMK的状态\n        :type KeyState: str\n        :param KeyUsage: CMK的用途\n        :type KeyUsage: str\n        :param TagCode: 标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagCode: int\n        :param TagMsg: 标签操作的返回信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Alias = None
        self.CreateTime = None
        self.Description = None
        self.KeyState = None
        self.KeyUsage = None
        self.TagCode = None
        self.TagMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.Description = params.get("Description")
        self.KeyState = params.get("KeyState")
        self.KeyUsage = params.get("KeyUsage")
        self.TagCode = params.get("TagCode")
        self.TagMsg = params.get("TagMsg")
        self.RequestId = params.get("RequestId")


class CreateWhiteBoxKeyRequest(AbstractModel):
    """CreateWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        """
        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合，首字符必须为字母或者数字。Alias不可重复。\n        :type Alias: str\n        :param Algorithm: 创建密钥所有的算法类型，支持的取值：AES_256,SM4\n        :type Algorithm: str\n        :param Description: 密钥的描述，最大1024字节\n        :type Description: str\n        :param Tags: 标签列表\n        :type Tags: list of Tag\n        """
        self.Alias = None
        self.Algorithm = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.Algorithm = params.get("Algorithm")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhiteBoxKeyResponse(AbstractModel):
    """CreateWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        """
        :param EncryptKey: 用于加密的密钥，base64编码\n        :type EncryptKey: str\n        :param DecryptKey: 用于解密的密钥，base64编码\n        :type DecryptKey: str\n        :param KeyId: 白盒密钥的全局唯一标识符\n        :type KeyId: str\n        :param TagCode: 标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagCode: int\n        :param TagMsg: 标签操作的返回信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagMsg: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EncryptKey = None
        self.DecryptKey = None
        self.KeyId = None
        self.TagCode = None
        self.TagMsg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EncryptKey = params.get("EncryptKey")
        self.DecryptKey = params.get("DecryptKey")
        self.KeyId = params.get("KeyId")
        self.TagCode = params.get("TagCode")
        self.TagMsg = params.get("TagMsg")
        self.RequestId = params.get("RequestId")


class DecryptRequest(AbstractModel):
    """Decrypt请求参数结构体

    """

    def __init__(self):
        """
        :param CiphertextBlob: 待解密的密文数据\n        :type CiphertextBlob: str\n        :param EncryptionContext: key/value对的json字符串，如果Encrypt指定了该参数，则在调用Decrypt API时需要提供同样的参数，最大支持1024字符\n        :type EncryptionContext: str\n        """
        self.CiphertextBlob = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.EncryptionContext = params.get("EncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DecryptResponse(AbstractModel):
    """Decrypt返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识\n        :type KeyId: str\n        :param Plaintext: 解密后的明文。该字段是base64编码的，为了得到原始明文，调用方需要进行base64解码\n        :type Plaintext: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class DeleteImportedKeyMaterialRequest(AbstractModel):
    """DeleteImportedKeyMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 指定需要删除密钥材料的EXTERNAL CMK。\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImportedKeyMaterialResponse(AbstractModel):
    """DeleteImportedKeyMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWhiteBoxKeyRequest(AbstractModel):
    """DeleteWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥的全局唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhiteBoxKeyResponse(AbstractModel):
    """DeleteWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeKeyRequest(AbstractModel):
    """DescribeKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK全局唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeyResponse(AbstractModel):
    """DescribeKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyMetadata: 密钥属性信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyMetadata: :class:`tencentcloud.kms.v20190118.models.KeyMetadata`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyMetadata = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyMetadata") is not None:
            self.KeyMetadata = KeyMetadata()
            self.KeyMetadata._deserialize(params.get("KeyMetadata"))
        self.RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys请求参数结构体

    """

    def __init__(self):
        """
        :param KeyIds: 查询CMK的ID列表，批量查询一次最多支持100个KeyId\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys返回参数结构体

    """

    def __init__(self):
        """
        :param KeyMetadatas: 返回的属性信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyMetadatas: list of KeyMetadata\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxDecryptKeyRequest(AbstractModel):
    """DescribeWhiteBoxDecryptKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥的全局唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxDecryptKeyResponse(AbstractModel):
    """DescribeWhiteBoxDecryptKey返回参数结构体

    """

    def __init__(self):
        """
        :param DecryptKey: 白盒解密密钥，base64编码\n        :type DecryptKey: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DecryptKey = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DecryptKey = params.get("DecryptKey")
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥ID\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxDeviceFingerprintsResponse(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints返回参数结构体

    """

    def __init__(self):
        """
        :param DeviceFingerprints: 设备指纹列表\n        :type DeviceFingerprints: list of DeviceFingerprint\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeviceFingerprints = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeviceFingerprints") is not None:
            self.DeviceFingerprints = []
            for item in params.get("DeviceFingerprints"):
                obj = DeviceFingerprint()
                obj._deserialize(item)
                self.DeviceFingerprints.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyDetailsRequest(AbstractModel):
    """DescribeWhiteBoxKeyDetails请求参数结构体

    """

    def __init__(self):
        """
        :param KeyStatus: 过滤条件：密钥的状态，0：disabled，1：enabled\n        :type KeyStatus: int\n        :param Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0\n        :type Offset: int\n        :param Limit: 含义跟 SQL 查询的 Limit 一致，表示本次最多获取 Limit 个元素。缺省值为0, 表示不分页\n        :type Limit: int\n        :param TagFilters: 标签过滤条件\n        :type TagFilters: list of TagFilter\n        """
        self.KeyStatus = None
        self.Offset = None
        self.Limit = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.KeyStatus = params.get("KeyStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxKeyDetailsResponse(AbstractModel):
    """DescribeWhiteBoxKeyDetails返回参数结构体

    """

    def __init__(self):
        """
        :param KeyInfos: 白盒密钥信息列表\n        :type KeyInfos: list of WhiteboxKeyInfo\n        :param TotalCount: key总数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyInfos = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyInfos") is not None:
            self.KeyInfos = []
            for item in params.get("KeyInfos"):
                obj = WhiteboxKeyInfo()
                obj._deserialize(item)
                self.KeyInfos.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyRequest(AbstractModel):
    """DescribeWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥的全局唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxKeyResponse(AbstractModel):
    """DescribeWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyInfo: 白盒密钥信息\n        :type KeyInfo: :class:`tencentcloud.kms.v20190118.models.WhiteboxKeyInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeyInfo") is not None:
            self.KeyInfo = WhiteboxKeyInfo()
            self.KeyInfo._deserialize(params.get("KeyInfo"))
        self.RequestId = params.get("RequestId")


class DescribeWhiteBoxServiceStatusRequest(AbstractModel):
    """DescribeWhiteBoxServiceStatus请求参数结构体

    """


class DescribeWhiteBoxServiceStatusResponse(AbstractModel):
    """DescribeWhiteBoxServiceStatus返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceEnabled: 用户的白盒密钥服务是否可用\n        :type ServiceEnabled: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ServiceEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.RequestId = params.get("RequestId")


class DeviceFingerprint(AbstractModel):
    """设备指纹

    """

    def __init__(self):
        """
        :param Identity: 指纹信息，由设备指纹采集工具采集获得，格式满足正则表达式：^[0-9a-f]{8}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{16}$\n        :type Identity: str\n        :param Description: 描述信息，如：IP，设备名称等，最大1024字节
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        """
        self.Identity = None
        self.Description = None


    def _deserialize(self, params):
        self.Identity = params.get("Identity")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyRequest(AbstractModel):
    """DisableKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyResponse(AbstractModel):
    """DisableKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeyRotationRequest(AbstractModel):
    """DisableKeyRotation请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyRotationResponse(AbstractModel):
    """DisableKeyRotation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeysRequest(AbstractModel):
    """DisableKeys请求参数结构体

    """

    def __init__(self):
        """
        :param KeyIds: 需要批量禁用的CMK Id 列表，CMK数量最大支持100\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeysResponse(AbstractModel):
    """DisableKeys返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableWhiteBoxKeyRequest(AbstractModel):
    """DisableWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥的全局唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWhiteBoxKeyResponse(AbstractModel):
    """DisableWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableWhiteBoxKeysRequest(AbstractModel):
    """DisableWhiteBoxKeys请求参数结构体

    """

    def __init__(self):
        """
        :param KeyIds: 白盒密钥的全局唯一标识符列表。注意：要确保所有提供的KeyId是格式有效的，没有重复，个数不超过50个，并且都是有效存在的。\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWhiteBoxKeysResponse(AbstractModel):
    """DisableWhiteBoxKeys返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRequest(AbstractModel):
    """EnableKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeyResponse(AbstractModel):
    """EnableKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRotationRequest(AbstractModel):
    """EnableKeyRotation请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeyRotationResponse(AbstractModel):
    """EnableKeyRotation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeysRequest(AbstractModel):
    """EnableKeys请求参数结构体

    """

    def __init__(self):
        """
        :param KeyIds: 需要批量启用的CMK Id 列表， CMK数量最大支持100\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeysResponse(AbstractModel):
    """EnableKeys返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWhiteBoxKeyRequest(AbstractModel):
    """EnableWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥的全局唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWhiteBoxKeyResponse(AbstractModel):
    """EnableWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableWhiteBoxKeysRequest(AbstractModel):
    """EnableWhiteBoxKeys请求参数结构体

    """

    def __init__(self):
        """
        :param KeyIds: 白盒密钥的全局唯一标识符列表。注意：要确保所有提供的KeyId是格式有效的，没有重复，个数不超过50个，并且都是有效存在的。\n        :type KeyIds: list of str\n        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWhiteBoxKeysResponse(AbstractModel):
    """EnableWhiteBoxKeys返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncryptByWhiteBoxRequest(AbstractModel):
    """EncryptByWhiteBox请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥的全局唯一标识符\n        :type KeyId: str\n        :param PlainText: 待加密的文本， base64编码，文本的原始长度最大不超过4KB\n        :type PlainText: str\n        :param InitializationVector: 初始化向量，大小为 16 Bytes，加密算法会使用到, base64编码；如果不传，则由后端服务随机生成。用户需要自行保存该值，作为解密的参数。\n        :type InitializationVector: str\n        """
        self.KeyId = None
        self.PlainText = None
        self.InitializationVector = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PlainText = params.get("PlainText")
        self.InitializationVector = params.get("InitializationVector")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptByWhiteBoxResponse(AbstractModel):
    """EncryptByWhiteBox返回参数结构体

    """

    def __init__(self):
        """
        :param InitializationVector: 初始化向量，加密算法会使用到, base64编码。如果由调用方在入参中传入，则原样返回。如果调用方没有传入，则后端服务随机生成，并返回\n        :type InitializationVector: str\n        :param CipherText: 加密后的密文，base64编码\n        :type CipherText: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InitializationVector = None
        self.CipherText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InitializationVector = params.get("InitializationVector")
        self.CipherText = params.get("CipherText")
        self.RequestId = params.get("RequestId")


class EncryptRequest(AbstractModel):
    """Encrypt请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 调用CreateKey生成的CMK全局唯一标识符\n        :type KeyId: str\n        :param Plaintext: 被加密的明文数据，该字段必须使用base64编码，原文最大长度支持4K\n        :type Plaintext: str\n        :param EncryptionContext: key/value对的json字符串，如果指定了该参数，则在调用Decrypt API时需要提供同样的参数，最大支持1024个字符\n        :type EncryptionContext: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.EncryptionContext = params.get("EncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptResponse(AbstractModel):
    """Encrypt返回参数结构体

    """

    def __init__(self):
        """
        :param CiphertextBlob: 加密后的密文，base64编码。注意：本字段中打包了密文和密钥的相关信息，不是对明文的直接加密结果，只有将该字段作为Decrypt接口的输入参数，才可以解密出原文。\n        :type CiphertextBlob: str\n        :param KeyId: 加密使用的CMK的全局唯一标识\n        :type KeyId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CiphertextBlob = None
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class GenerateDataKeyRequest(AbstractModel):
    """GenerateDataKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK全局唯一标识符\n        :type KeyId: str\n        :param KeySpec: 指定生成Datakey的加密算法以及Datakey大小，AES_128或者AES_256。KeySpec 和 NumberOfBytes 必须指定一个\n        :type KeySpec: str\n        :param NumberOfBytes: 生成的DataKey的长度，同时指定NumberOfBytes和KeySpec时，以NumberOfBytes为准。最小值为1， 最大值为1024。KeySpec 和 NumberOfBytes 必须指定一个\n        :type NumberOfBytes: int\n        :param EncryptionContext: key/value对的json字符串，如果使用该字段，则返回的DataKey在解密时需要填入相同的字符串\n        :type EncryptionContext: str\n        """
        self.KeyId = None
        self.KeySpec = None
        self.NumberOfBytes = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeySpec = params.get("KeySpec")
        self.NumberOfBytes = params.get("NumberOfBytes")
        self.EncryptionContext = params.get("EncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDataKeyResponse(AbstractModel):
    """GenerateDataKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识\n        :type KeyId: str\n        :param Plaintext: 生成的数据密钥DataKey的明文，该明文使用base64进行了编码，需base64解码后作为数据密钥本地使用\n        :type Plaintext: str\n        :param CiphertextBlob: 数据密钥DataKey加密后的密文，用户需要自行保存该密文，KMS不托管用户的数据密钥。可以通过Decrypt接口从CiphertextBlob中获取数据密钥DataKey明文\n        :type CiphertextBlob: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyId = None
        self.Plaintext = None
        self.CiphertextBlob = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.RequestId = params.get("RequestId")


class GenerateRandomRequest(AbstractModel):
    """GenerateRandom请求参数结构体

    """

    def __init__(self):
        """
        :param NumberOfBytes: 生成的随机数的长度。最小值为1， 最大值为1024。\n        :type NumberOfBytes: int\n        """
        self.NumberOfBytes = None


    def _deserialize(self, params):
        self.NumberOfBytes = params.get("NumberOfBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateRandomResponse(AbstractModel):
    """GenerateRandom返回参数结构体

    """

    def __init__(self):
        """
        :param Plaintext: 生成的随机数的明文，该明文使用base64编码，用户需要使用base64解码得到明文。\n        :type Plaintext: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class GetKeyRotationStatusRequest(AbstractModel):
    """GetKeyRotationStatus请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetKeyRotationStatusResponse(AbstractModel):
    """GetKeyRotationStatus返回参数结构体

    """

    def __init__(self):
        """
        :param KeyRotationEnabled: 密钥轮换是否开启\n        :type KeyRotationEnabled: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyRotationEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.RequestId = params.get("RequestId")


class GetParametersForImportRequest(AbstractModel):
    """GetParametersForImport请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标识，获取密钥参数的CMK必须是EXTERNAL类型，即在CreateKey时指定Type=2 类型的CMK。\n        :type KeyId: str\n        :param WrappingAlgorithm: 指定加密密钥材料的算法，目前支持RSAES_PKCS1_V1_5、RSAES_OAEP_SHA_1、RSAES_OAEP_SHA_256\n        :type WrappingAlgorithm: str\n        :param WrappingKeySpec: 指定加密密钥材料的类型，目前只支持RSA_2048\n        :type WrappingKeySpec: str\n        """
        self.KeyId = None
        self.WrappingAlgorithm = None
        self.WrappingKeySpec = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.WrappingAlgorithm = params.get("WrappingAlgorithm")
        self.WrappingKeySpec = params.get("WrappingKeySpec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetParametersForImportResponse(AbstractModel):
    """GetParametersForImport返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标识，用于指定目标导入密钥材料的CMK。\n        :type KeyId: str\n        :param ImportToken: 导入密钥材料需要的token，用于作为 ImportKeyMaterial 的参数。\n        :type ImportToken: str\n        :param PublicKey: 用于加密密钥材料的RSA公钥，base64编码。使用PublicKey base64解码后的公钥将导入密钥进行加密后作为 ImportKeyMaterial 的参数。\n        :type PublicKey: str\n        :param ParametersValidTo: 该导出token和公钥的有效期，超过该时间后无法导入，需要重新调用GetParametersForImport获取。\n        :type ParametersValidTo: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyId = None
        self.ImportToken = None
        self.PublicKey = None
        self.ParametersValidTo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.ImportToken = params.get("ImportToken")
        self.PublicKey = params.get("PublicKey")
        self.ParametersValidTo = params.get("ParametersValidTo")
        self.RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标识。\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标识。\n        :type KeyId: str\n        :param PublicKey: 经过base64编码的公钥内容。\n        :type PublicKey: str\n        :param PublicKeyPem: PEM格式的公钥内容。\n        :type PublicKeyPem: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.KeyId = None
        self.PublicKey = None
        self.PublicKeyPem = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PublicKey = params.get("PublicKey")
        self.PublicKeyPem = params.get("PublicKeyPem")
        self.RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions请求参数结构体

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions返回参数结构体

    """

    def __init__(self):
        """
        :param Regions: 可用region列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Regions: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Regions = params.get("Regions")
        self.RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus请求参数结构体

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceEnabled: KMS服务是否开通， true 表示已开通\n        :type ServiceEnabled: bool\n        :param InvalidType: 服务不可用类型： 0-未购买，1-正常， 2-欠费停服， 3-资源释放
注意：此字段可能返回 null，表示取不到有效值。\n        :type InvalidType: int\n        :param UserLevel: 0-普通版，1-旗舰版\n        :type UserLevel: int\n        :param ProExpireTime: 旗舰版到期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProExpireTime: int\n        :param ProRenewFlag: 旗舰版是否自动续费：0-不自动续费，1-自动续费
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProRenewFlag: int\n        :param ProResourceId: 旗舰版购买记录的唯一性标识。如果为开通旗舰版，则返回值为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProResourceId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ServiceEnabled = None
        self.InvalidType = None
        self.UserLevel = None
        self.ProExpireTime = None
        self.ProRenewFlag = None
        self.ProResourceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.InvalidType = params.get("InvalidType")
        self.UserLevel = params.get("UserLevel")
        self.ProExpireTime = params.get("ProExpireTime")
        self.ProRenewFlag = params.get("ProRenewFlag")
        self.ProResourceId = params.get("ProResourceId")
        self.RequestId = params.get("RequestId")


class ImportKeyMaterialRequest(AbstractModel):
    """ImportKeyMaterial请求参数结构体

    """

    def __init__(self):
        """
        :param EncryptedKeyMaterial: 使用GetParametersForImport 返回的PublicKey加密后的密钥材料base64编码。对于国密版本region的KMS，导入的密钥材料长度要求为 128 bit，FIPS版本region的KMS， 导入的密钥材料长度要求为 256 bit。\n        :type EncryptedKeyMaterial: str\n        :param ImportToken: 通过调用GetParametersForImport获得的导入令牌。\n        :type ImportToken: str\n        :param KeyId: 指定导入密钥材料的CMK，需要和GetParametersForImport 指定的CMK相同。\n        :type KeyId: str\n        :param ValidTo: 密钥材料过期时间 unix 时间戳，不指定或者 0 表示密钥材料不会过期，若指定过期时间，需要大于当前时间点，最大支持 2147443200。\n        :type ValidTo: int\n        """
        self.EncryptedKeyMaterial = None
        self.ImportToken = None
        self.KeyId = None
        self.ValidTo = None


    def _deserialize(self, params):
        self.EncryptedKeyMaterial = params.get("EncryptedKeyMaterial")
        self.ImportToken = params.get("ImportToken")
        self.KeyId = params.get("KeyId")
        self.ValidTo = params.get("ValidTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyMaterialResponse(AbstractModel):
    """ImportKeyMaterial返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Key(AbstractModel):
    """返回CMK列表信息

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识。\n        :type KeyId: str\n        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyMetadata(AbstractModel):
    """CMK属性信息

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识\n        :type KeyId: str\n        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名\n        :type Alias: str\n        :param CreateTime: 密钥创建时间\n        :type CreateTime: int\n        :param Description: CMK的描述\n        :type Description: str\n        :param KeyState: CMK的状态， 取值为：Enabled | Disabled | PendingDelete | PendingImport | Archived\n        :type KeyState: str\n        :param KeyUsage: CMK用途，取值为: ENCRYPT_DECRYPT | ASYMMETRIC_DECRYPT_RSA_2048 | ASYMMETRIC_DECRYPT_SM2 | ASYMMETRIC_SIGN_VERIFY_SM2 | ASYMMETRIC_SIGN_VERIFY_RSA_2048 | ASYMMETRIC_SIGN_VERIFY_ECC\n        :type KeyUsage: str\n        :param Type: CMK类型，2 表示符合FIPS标准，4表示符合国密标准\n        :type Type: int\n        :param CreatorUin: 创建者\n        :type CreatorUin: int\n        :param KeyRotationEnabled: 是否开启了密钥轮换功能\n        :type KeyRotationEnabled: bool\n        :param Owner: CMK的创建者，用户创建的为 user，授权各云产品自动创建的为对应的产品名\n        :type Owner: str\n        :param NextRotateTime: 在密钥轮换开启状态下，下次轮换的时间\n        :type NextRotateTime: int\n        :param DeletionDate: 计划删除的时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeletionDate: int\n        :param Origin: CMK 密钥材料类型，由KMS创建的为： TENCENT_KMS， 由用户导入的类型为：EXTERNAL
注意：此字段可能返回 null，表示取不到有效值。\n        :type Origin: str\n        :param ValidTo: 在Origin为  EXTERNAL 时有效，表示密钥材料的有效日期， 0 表示不过期
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValidTo: int\n        :param ResourceId: 资源ID，格式：creatorUin/$creatorUin/$keyId\n        :type ResourceId: str\n        """
        self.KeyId = None
        self.Alias = None
        self.CreateTime = None
        self.Description = None
        self.KeyState = None
        self.KeyUsage = None
        self.Type = None
        self.CreatorUin = None
        self.KeyRotationEnabled = None
        self.Owner = None
        self.NextRotateTime = None
        self.DeletionDate = None
        self.Origin = None
        self.ValidTo = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.Description = params.get("Description")
        self.KeyState = params.get("KeyState")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")
        self.CreatorUin = params.get("CreatorUin")
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.Owner = params.get("Owner")
        self.NextRotateTime = params.get("NextRotateTime")
        self.DeletionDate = params.get("DeletionDate")
        self.Origin = params.get("Origin")
        self.ValidTo = params.get("ValidTo")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAlgorithmsRequest(AbstractModel):
    """ListAlgorithms请求参数结构体

    """


class ListAlgorithmsResponse(AbstractModel):
    """ListAlgorithms返回参数结构体

    """

    def __init__(self):
        """
        :param SymmetricAlgorithms: 本地区支持的对称加密算法\n        :type SymmetricAlgorithms: list of AlgorithmInfo\n        :param AsymmetricAlgorithms: 本地区支持的非对称加密算法\n        :type AsymmetricAlgorithms: list of AlgorithmInfo\n        :param AsymmetricSignVerifyAlgorithms: 本地区支持的非对称签名验签算法\n        :type AsymmetricSignVerifyAlgorithms: list of AlgorithmInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SymmetricAlgorithms = None
        self.AsymmetricAlgorithms = None
        self.AsymmetricSignVerifyAlgorithms = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SymmetricAlgorithms") is not None:
            self.SymmetricAlgorithms = []
            for item in params.get("SymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.SymmetricAlgorithms.append(obj)
        if params.get("AsymmetricAlgorithms") is not None:
            self.AsymmetricAlgorithms = []
            for item in params.get("AsymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.AsymmetricAlgorithms.append(obj)
        if params.get("AsymmetricSignVerifyAlgorithms") is not None:
            self.AsymmetricSignVerifyAlgorithms = []
            for item in params.get("AsymmetricSignVerifyAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self.AsymmetricSignVerifyAlgorithms.append(obj)
        self.RequestId = params.get("RequestId")


class ListKeyDetailRequest(AbstractModel):
    """ListKeyDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0\n        :type Offset: int\n        :param Limit: 含义跟 SQL 查询的 Limit 一致，表示本次最多获取 Limit 个元素。缺省值为10，最大值为200\n        :type Limit: int\n        :param Role: 根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk\n        :type Role: int\n        :param OrderType: 根据CMK创建时间排序， 0 表示按照降序排序，1表示按照升序排序\n        :type OrderType: int\n        :param KeyState: 根据CMK状态筛选， 0表示全部CMK， 1 表示仅查询Enabled CMK， 2 表示仅查询Disabled CMK，3 表示查询PendingDelete 状态的CMK(处于计划删除状态的Key)，4 表示查询 PendingImport 状态的CMK，5 表示查询 Archived 状态的 CMK\n        :type KeyState: int\n        :param SearchKeyAlias: 根据KeyId或者Alias进行模糊匹配查询\n        :type SearchKeyAlias: str\n        :param Origin: 根据CMK类型筛选， "TENCENT_KMS" 表示筛选密钥材料由KMS创建的CMK， "EXTERNAL" 表示筛选密钥材料需要用户导入的 EXTERNAL类型CMK，"ALL" 或者不设置表示两种类型都查询，大小写敏感。\n        :type Origin: str\n        :param KeyUsage: 根据CMK的KeyUsage筛选，ALL表示筛选全部，可使用的参数为：ALL 或 ENCRYPT_DECRYPT 或 ASYMMETRIC_DECRYPT_RSA_2048 或 ASYMMETRIC_DECRYPT_SM2 或 ASYMMETRIC_SIGN_VERIFY_SM2 或 ASYMMETRIC_SIGN_VERIFY_RSA_2048 或 ASYMMETRIC_SIGN_VERIFY_ECC，为空则默认筛选ENCRYPT_DECRYPT类型\n        :type KeyUsage: str\n        :param TagFilters: 标签过滤条件\n        :type TagFilters: list of TagFilter\n        """
        self.Offset = None
        self.Limit = None
        self.Role = None
        self.OrderType = None
        self.KeyState = None
        self.SearchKeyAlias = None
        self.Origin = None
        self.KeyUsage = None
        self.TagFilters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")
        self.OrderType = params.get("OrderType")
        self.KeyState = params.get("KeyState")
        self.SearchKeyAlias = params.get("SearchKeyAlias")
        self.Origin = params.get("Origin")
        self.KeyUsage = params.get("KeyUsage")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeyDetailResponse(AbstractModel):
    """ListKeyDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: CMK的总数量\n        :type TotalCount: int\n        :param KeyMetadatas: 返回的属性信息列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyMetadatas: list of KeyMetadata\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.KeyMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("KeyMetadatas") is not None:
            self.KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self.KeyMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class ListKeysRequest(AbstractModel):
    """ListKeys请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0\n        :type Offset: int\n        :param Limit: 含义跟 SQL 查询的 Limit 一致，表示本次获最多获取 Limit 个元素。缺省值为10，最大值为200\n        :type Limit: int\n        :param Role: 根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk\n        :type Role: int\n        """
        self.Offset = None
        self.Limit = None
        self.Role = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeysResponse(AbstractModel):
    """ListKeys返回参数结构体

    """

    def __init__(self):
        """
        :param Keys: CMK列表数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type Keys: list of Key\n        :param TotalCount: CMK的总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Keys = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class OverwriteWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """OverwriteWhiteBoxDeviceFingerprints请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥ID\n        :type KeyId: str\n        :param DeviceFingerprints: 设备指纹列表，如果列表为空，则表示删除该密钥对应的所有指纹信息。列表最大长度不超过200。\n        :type DeviceFingerprints: list of DeviceFingerprint\n        """
        self.KeyId = None
        self.DeviceFingerprints = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        if params.get("DeviceFingerprints") is not None:
            self.DeviceFingerprints = []
            for item in params.get("DeviceFingerprints"):
                obj = DeviceFingerprint()
                obj._deserialize(item)
                self.DeviceFingerprints.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverwriteWhiteBoxDeviceFingerprintsResponse(AbstractModel):
    """OverwriteWhiteBoxDeviceFingerprints返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReEncryptRequest(AbstractModel):
    """ReEncrypt请求参数结构体

    """

    def __init__(self):
        """
        :param CiphertextBlob: 需要重新加密的密文\n        :type CiphertextBlob: str\n        :param DestinationKeyId: 重新加密使用的CMK，如果为空，则使用密文原有的CMK重新加密（若密钥没有轮换则密文不会刷新）\n        :type DestinationKeyId: str\n        :param SourceEncryptionContext: CiphertextBlob 密文加密时使用的key/value对的json字符串。如果加密时未使用，则为空\n        :type SourceEncryptionContext: str\n        :param DestinationEncryptionContext: 重新加密使用的key/value对的json字符串，如果使用该字段，则返回的新密文在解密时需要填入相同的字符串\n        :type DestinationEncryptionContext: str\n        """
        self.CiphertextBlob = None
        self.DestinationKeyId = None
        self.SourceEncryptionContext = None
        self.DestinationEncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.DestinationKeyId = params.get("DestinationKeyId")
        self.SourceEncryptionContext = params.get("SourceEncryptionContext")
        self.DestinationEncryptionContext = params.get("DestinationEncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReEncryptResponse(AbstractModel):
    """ReEncrypt返回参数结构体

    """

    def __init__(self):
        """
        :param CiphertextBlob: 重新加密后的密文\n        :type CiphertextBlob: str\n        :param KeyId: 重新加密使用的CMK\n        :type KeyId: str\n        :param SourceKeyId: 重新加密前密文使用的CMK\n        :type SourceKeyId: str\n        :param ReEncrypted: true表示密文已经重新加密。同一个CMK进行重加密，在密钥没有发生轮换的情况下不会进行实际重新加密操作，返回原密文\n        :type ReEncrypted: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CiphertextBlob = None
        self.KeyId = None
        self.SourceKeyId = None
        self.ReEncrypted = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.KeyId = params.get("KeyId")
        self.SourceKeyId = params.get("SourceKeyId")
        self.ReEncrypted = params.get("ReEncrypted")
        self.RequestId = params.get("RequestId")


class ScheduleKeyDeletionRequest(AbstractModel):
    """ScheduleKeyDeletion请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的唯一标志\n        :type KeyId: str\n        :param PendingWindowInDays: 计划删除时间区间[7,30]\n        :type PendingWindowInDays: int\n        """
        self.KeyId = None
        self.PendingWindowInDays = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.PendingWindowInDays = params.get("PendingWindowInDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleKeyDeletionResponse(AbstractModel):
    """ScheduleKeyDeletion返回参数结构体

    """

    def __init__(self):
        """
        :param DeletionDate: 计划删除执行时间\n        :type DeletionDate: int\n        :param KeyId: 唯一标志被计划删除的CMK\n        :type KeyId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeletionDate = None
        self.KeyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeletionDate = params.get("DeletionDate")
        self.KeyId = params.get("KeyId")
        self.RequestId = params.get("RequestId")


class SignByAsymmetricKeyRequest(AbstractModel):
    """SignByAsymmetricKey请求参数结构体

    """

    def __init__(self):
        """
        :param Algorithm: 签名算法，支持的算法：SM2DSA，ECC_P256_R1，RSA_PSS_SHA_256，RSA_PKCS1_SHA_256\n        :type Algorithm: str\n        :param Message: 消息原文或消息摘要。如果提供的是消息原文，则消息原文的长度（Base64编码前的长度）不超过4096字节。如果提供的是消息摘要，消息摘要长度（Base64编码前的长度）必须等于32字节\n        :type Message: str\n        :param KeyId: 密钥的唯一标识\n        :type KeyId: str\n        :param MessageType: 消息类型：RAW，DIGEST，如果不传，默认为RAW，表示消息原文。\n        :type MessageType: str\n        """
        self.Algorithm = None
        self.Message = None
        self.KeyId = None
        self.MessageType = None


    def _deserialize(self, params):
        self.Algorithm = params.get("Algorithm")
        self.Message = params.get("Message")
        self.KeyId = params.get("KeyId")
        self.MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignByAsymmetricKeyResponse(AbstractModel):
    """SignByAsymmetricKey返回参数结构体

    """

    def __init__(self):
        """
        :param Signature: 签名，Base64编码\n        :type Signature: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Signature = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Signature = params.get("Signature")
        self.RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签键和标签值

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """标签过滤器

    """

    def __init__(self):
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: list of str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudResourceRequest(AbstractModel):
    """UnbindCloudResource请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: cmk的ID\n        :type KeyId: str\n        :param ProductId: 云产品的唯一性标识符\n        :type ProductId: str\n        :param ResourceId: 资源/实例ID，由调用方根据自己的云产品特征来定义，以字符串形式做存储。\n        :type ResourceId: str\n        """
        self.KeyId = None
        self.ProductId = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.ProductId = params.get("ProductId")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudResourceResponse(AbstractModel):
    """UnbindCloudResource返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias请求参数结构体

    """

    def __init__(self):
        """
        :param Alias: 新的别名，1-60个字符或数字的组合\n        :type Alias: str\n        :param KeyId: CMK的全局唯一标识符\n        :type KeyId: str\n        """
        self.Alias = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateKeyDescriptionRequest(AbstractModel):
    """UpdateKeyDescription请求参数结构体

    """

    def __init__(self):
        """
        :param Description: 新的描述信息，最大支持1024字节\n        :type Description: str\n        :param KeyId: 需要修改描述信息的CMK ID\n        :type KeyId: str\n        """
        self.Description = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateKeyDescriptionResponse(AbstractModel):
    """UpdateKeyDescription返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VerifyByAsymmetricKeyRequest(AbstractModel):
    """VerifyByAsymmetricKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 密钥的唯一标识\n        :type KeyId: str\n        :param SignatureValue: 签名值，通过调用KMS签名接口生成\n        :type SignatureValue: str\n        :param Message: 消息原文或消息摘要。如果提供的是消息原文，则消息原文的长度（Base64编码前的长度）不超过4096字节。如果提供的是消息摘要，则消息摘要长度（Base64编码前的长度）必须等于32字节\n        :type Message: str\n        :param Algorithm: 签名算法，支持的算法：SM2DSA，ECC_P256_R1，RSA_PSS_SHA_256，RSA_PKCS1_SHA_256\n        :type Algorithm: str\n        :param MessageType: 消息类型：RAW，DIGEST，如果不传，默认为RAW，表示消息原文。\n        :type MessageType: str\n        """
        self.KeyId = None
        self.SignatureValue = None
        self.Message = None
        self.Algorithm = None
        self.MessageType = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.SignatureValue = params.get("SignatureValue")
        self.Message = params.get("Message")
        self.Algorithm = params.get("Algorithm")
        self.MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyByAsymmetricKeyResponse(AbstractModel):
    """VerifyByAsymmetricKey返回参数结构体

    """

    def __init__(self):
        """
        :param SignatureValid: 签名是否有效。true：签名有效，false：签名无效。\n        :type SignatureValid: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SignatureValid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SignatureValid = params.get("SignatureValid")
        self.RequestId = params.get("RequestId")


class WhiteboxKeyInfo(AbstractModel):
    """白盒密钥信息

    """

    def __init__(self):
        """
        :param KeyId: 白盒密钥的全局唯一标识符\n        :type KeyId: str\n        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合，首字符必须为字母或者数字. 不可重复\n        :type Alias: str\n        :param CreatorUin: 创建者\n        :type CreatorUin: int\n        :param Description: 密钥的描述信息\n        :type Description: str\n        :param CreateTime: 密钥创建时间，Unix时间戳\n        :type CreateTime: int\n        :param Status: 白盒密钥的状态， 取值为：Enabled | Disabled\n        :type Status: str\n        :param OwnerUin: 创建者\n        :type OwnerUin: int\n        :param Algorithm: 密钥所用的算法类型\n        :type Algorithm: str\n        :param EncryptKey: 白盒加密密钥，base64编码\n        :type EncryptKey: str\n        :param DecryptKey: 白盒解密密钥，base64编码\n        :type DecryptKey: str\n        :param ResourceId: 资源ID，格式：creatorUin/$creatorUin/$keyId\n        :type ResourceId: str\n        :param DeviceFingerprintBind: 是否有设备指纹与当前密钥绑定
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeviceFingerprintBind: bool\n        """
        self.KeyId = None
        self.Alias = None
        self.CreatorUin = None
        self.Description = None
        self.CreateTime = None
        self.Status = None
        self.OwnerUin = None
        self.Algorithm = None
        self.EncryptKey = None
        self.DecryptKey = None
        self.ResourceId = None
        self.DeviceFingerprintBind = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreatorUin = params.get("CreatorUin")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        self.OwnerUin = params.get("OwnerUin")
        self.Algorithm = params.get("Algorithm")
        self.EncryptKey = params.get("EncryptKey")
        self.DecryptKey = params.get("DecryptKey")
        self.ResourceId = params.get("ResourceId")
        self.DeviceFingerprintBind = params.get("DeviceFingerprintBind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        