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
        r"""
        :param _KeyUsage: 算法的标识
        :type KeyUsage: str
        :param _Algorithm: 算法的名称
        :type Algorithm: str
        """
        self._KeyUsage = None
        self._Algorithm = None

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm


    def _deserialize(self, params):
        self._KeyUsage = params.get("KeyUsage")
        self._Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveKeyRequest(AbstractModel):
    """ArchiveKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ArchiveKeyResponse(AbstractModel):
    """ArchiveKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AsymmetricRsaDecryptRequest(AbstractModel):
    """AsymmetricRsaDecrypt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标识
        :type KeyId: str
        :param _Ciphertext: 使用PublicKey加密的密文，Base64编码
        :type Ciphertext: str
        :param _Algorithm: 在使用公钥加密时对应的算法：当前支持RSAES_PKCS1_V1_5、RSAES_OAEP_SHA_1、RSAES_OAEP_SHA_256
        :type Algorithm: str
        """
        self._KeyId = None
        self._Ciphertext = None
        self._Algorithm = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Ciphertext(self):
        return self._Ciphertext

    @Ciphertext.setter
    def Ciphertext(self, Ciphertext):
        self._Ciphertext = Ciphertext

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Ciphertext = params.get("Ciphertext")
        self._Algorithm = params.get("Algorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsymmetricRsaDecryptResponse(AbstractModel):
    """AsymmetricRsaDecrypt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标识
        :type KeyId: str
        :param _Plaintext: 解密后的明文，base64编码
        :type Plaintext: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._RequestId = params.get("RequestId")


class AsymmetricSm2DecryptRequest(AbstractModel):
    """AsymmetricSm2Decrypt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标识
        :type KeyId: str
        :param _Ciphertext: 使用PublicKey加密的密文，Base64编码。密文长度不能超过256字节。
        :type Ciphertext: str
        """
        self._KeyId = None
        self._Ciphertext = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Ciphertext(self):
        return self._Ciphertext

    @Ciphertext.setter
    def Ciphertext(self, Ciphertext):
        self._Ciphertext = Ciphertext


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Ciphertext = params.get("Ciphertext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AsymmetricSm2DecryptResponse(AbstractModel):
    """AsymmetricSm2Decrypt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标识
        :type KeyId: str
        :param _Plaintext: 解密后的明文，base64编码
        :type Plaintext: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._RequestId = params.get("RequestId")


class BindCloudResourceRequest(AbstractModel):
    """BindCloudResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: cmk的ID
        :type KeyId: str
        :param _ProductId: 云产品的唯一性标识符
        :type ProductId: str
        :param _ResourceId: 资源/实例ID，由调用方根据自己的云产品特征来定义，以字符串形式做存储。
        :type ResourceId: str
        """
        self._KeyId = None
        self._ProductId = None
        self._ResourceId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._ProductId = params.get("ProductId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindCloudResourceResponse(AbstractModel):
    """BindCloudResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CancelKeyArchiveRequest(AbstractModel):
    """CancelKeyArchive请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKeyArchiveResponse(AbstractModel):
    """CancelKeyArchive返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CancelKeyDeletionRequest(AbstractModel):
    """CancelKeyDeletion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 需要被取消删除的CMK的唯一标志
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelKeyDeletionResponse(AbstractModel):
    """CancelKeyDeletion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 唯一标志被取消删除的CMK。
        :type KeyId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class CreateKeyRequest(AbstractModel):
    """CreateKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合，首字符必须为字母或者数字。以 kms- 作为前缀的用于云产品使用，Alias 不可重复。
        :type Alias: str
        :param _Description: CMK 的描述，最大1024字节
        :type Description: str
        :param _KeyUsage: 指定key的用途，默认为  "ENCRYPT_DECRYPT" 表示创建对称加解密密钥，其它支持用途 “ASYMMETRIC_DECRYPT_RSA_2048” 表示创建用于加解密的RSA2048非对称密钥，“ASYMMETRIC_DECRYPT_SM2” 表示创建用于加解密的SM2非对称密钥，“ASYMMETRIC_SIGN_VERIFY_SM2” 表示创建用于签名验签的SM2非对称密钥，“ASYMMETRIC_SIGN_VERIFY_ECC” 表示创建用于签名验签的ECC非对称密钥，“ASYMMETRIC_SIGN_VERIFY_RSA_2048” 表示创建用于签名验签的RSA_2048非对称密钥，“ASYMMETRIC_SIGN_VERIFY_ECDSA384”表示创建用于签名验签的 ECDSA384 非对称秘钥。完整的秘钥用途与算法支持列表可通过 ListAlgorithms 接口获取。
        :type KeyUsage: str
        :param _Type: 指定key类型，默认为1，1表示默认类型，由KMS创建CMK密钥，2 表示EXTERNAL 类型，该类型需要用户导入密钥材料，参考 GetParametersForImport 和 ImportKeyMaterial 接口
        :type Type: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _HsmClusterId: KMS 高级版对应的 HSM 集群 ID（仅对 KMS 独占版/托管版服务实例有效）。
        :type HsmClusterId: str
        """
        self._Alias = None
        self._Description = None
        self._KeyUsage = None
        self._Type = None
        self._Tags = None
        self._HsmClusterId = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._Description = params.get("Description")
        self._KeyUsage = params.get("KeyUsage")
        self._Type = params.get("Type")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._HsmClusterId = params.get("HsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKeyResponse(AbstractModel):
    """CreateKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的全局唯一标识符
        :type KeyId: str
        :param _Alias: 作为密钥更容易辨识，更容易被人看懂的别名
        :type Alias: str
        :param _CreateTime: 密钥创建时间，unix时间戳
        :type CreateTime: int
        :param _Description: CMK的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _KeyState: CMK的状态
        :type KeyState: str
        :param _KeyUsage: CMK的用途
        :type KeyUsage: str
        :param _TagCode: 标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误
注意：此字段可能返回 null，表示取不到有效值。
        :type TagCode: int
        :param _TagMsg: 标签操作的返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagMsg: str
        :param _HsmClusterId: HSM 集群 ID（仅对 KMS 独占版/托管版服务实例有效）
注意：此字段可能返回 null，表示取不到有效值。
        :type HsmClusterId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._Alias = None
        self._CreateTime = None
        self._Description = None
        self._KeyState = None
        self._KeyUsage = None
        self._TagCode = None
        self._TagMsg = None
        self._HsmClusterId = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KeyState(self):
        return self._KeyState

    @KeyState.setter
    def KeyState(self, KeyState):
        self._KeyState = KeyState

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def TagCode(self):
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Alias = params.get("Alias")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._KeyState = params.get("KeyState")
        self._KeyUsage = params.get("KeyUsage")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._HsmClusterId = params.get("HsmClusterId")
        self._RequestId = params.get("RequestId")


class CreateWhiteBoxKeyRequest(AbstractModel):
    """CreateWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合，首字符必须为字母或者数字。Alias不可重复。
        :type Alias: str
        :param _Algorithm: 创建密钥所有的算法类型，支持的取值：AES_256,SM4
        :type Algorithm: str
        :param _Description: 密钥的描述，最大1024字节
        :type Description: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        """
        self._Alias = None
        self._Algorithm = None
        self._Description = None
        self._Tags = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._Algorithm = params.get("Algorithm")
        self._Description = params.get("Description")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWhiteBoxKeyResponse(AbstractModel):
    """CreateWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EncryptKey: 用于加密的密钥，base64编码
        :type EncryptKey: str
        :param _DecryptKey: 用于解密的密钥，base64编码
        :type DecryptKey: str
        :param _KeyId: 白盒密钥的全局唯一标识符
        :type KeyId: str
        :param _TagCode: 标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误
注意：此字段可能返回 null，表示取不到有效值。
        :type TagCode: int
        :param _TagMsg: 标签操作的返回信息
注意：此字段可能返回 null，表示取不到有效值。
        :type TagMsg: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EncryptKey = None
        self._DecryptKey = None
        self._KeyId = None
        self._TagCode = None
        self._TagMsg = None
        self._RequestId = None

    @property
    def EncryptKey(self):
        return self._EncryptKey

    @EncryptKey.setter
    def EncryptKey(self, EncryptKey):
        self._EncryptKey = EncryptKey

    @property
    def DecryptKey(self):
        return self._DecryptKey

    @DecryptKey.setter
    def DecryptKey(self, DecryptKey):
        self._DecryptKey = DecryptKey

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def TagCode(self):
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EncryptKey = params.get("EncryptKey")
        self._DecryptKey = params.get("DecryptKey")
        self._KeyId = params.get("KeyId")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._RequestId = params.get("RequestId")


class DecryptRequest(AbstractModel):
    """Decrypt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: 待解密的密文数据
        :type CiphertextBlob: str
        :param _EncryptionContext: key/value对的json字符串，如果Encrypt指定了该参数，则在调用Decrypt API时需要提供同样的参数，最大支持1024字符
        :type EncryptionContext: str
        :param _EncryptionPublicKey: PEM 格式公钥字符串，支持 RSA2048 和 SM2 公钥，用于对返回数据中的 Plaintext 值进行加密。若为空，则不对 Plaintext 值加密。
        :type EncryptionPublicKey: str
        :param _EncryptionAlgorithm: 非对称加密算法，配合 EncryptionPublicKey 对返回数据进行加密。目前支持：SM2（以 C1C3C2 格式返回密文），SM2_C1C3C2_ASN1 （以 C1C3C2 ASN1 格式返回密文），RSAES_PKCS1_V1_5，RSAES_OAEP_SHA_1，RSAES_OAEP_SHA_256。若为空，则默认为 SM2。
        :type EncryptionAlgorithm: str
        """
        self._CiphertextBlob = None
        self._EncryptionContext = None
        self._EncryptionPublicKey = None
        self._EncryptionAlgorithm = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def EncryptionContext(self):
        return self._EncryptionContext

    @EncryptionContext.setter
    def EncryptionContext(self, EncryptionContext):
        self._EncryptionContext = EncryptionContext

    @property
    def EncryptionPublicKey(self):
        return self._EncryptionPublicKey

    @EncryptionPublicKey.setter
    def EncryptionPublicKey(self, EncryptionPublicKey):
        self._EncryptionPublicKey = EncryptionPublicKey

    @property
    def EncryptionAlgorithm(self):
        return self._EncryptionAlgorithm

    @EncryptionAlgorithm.setter
    def EncryptionAlgorithm(self, EncryptionAlgorithm):
        self._EncryptionAlgorithm = EncryptionAlgorithm


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._EncryptionContext = params.get("EncryptionContext")
        self._EncryptionPublicKey = params.get("EncryptionPublicKey")
        self._EncryptionAlgorithm = params.get("EncryptionAlgorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DecryptResponse(AbstractModel):
    """Decrypt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的全局唯一标识
        :type KeyId: str
        :param _Plaintext: 若调用时未提供 EncryptionPublicKey，该字段值为 Base64 编码的明文，需进行 Base64 解码以获取明文。
若调用时提供了 EncryptionPublicKey，则该字段值为使用 EncryptionPublicKey 公钥进行非对称加密后的 Base64 编码的密文。需在 Base64 解码后，使用用户上传的公钥对应的私钥进行进一步解密，以获取明文。
        :type Plaintext: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._RequestId = params.get("RequestId")


class DeleteImportedKeyMaterialRequest(AbstractModel):
    """DeleteImportedKeyMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 指定需要删除密钥材料的EXTERNAL CMK。
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImportedKeyMaterialResponse(AbstractModel):
    """DeleteImportedKeyMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteWhiteBoxKeyRequest(AbstractModel):
    """DeleteWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥的全局唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWhiteBoxKeyResponse(AbstractModel):
    """DeleteWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeKeyRequest(AbstractModel):
    """DescribeKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK全局唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeyResponse(AbstractModel):
    """DescribeKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyMetadata: 密钥属性信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyMetadata: :class:`tencentcloud.kms.v20190118.models.KeyMetadata`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyMetadata = None
        self._RequestId = None

    @property
    def KeyMetadata(self):
        return self._KeyMetadata

    @KeyMetadata.setter
    def KeyMetadata(self, KeyMetadata):
        self._KeyMetadata = KeyMetadata

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyMetadata") is not None:
            self._KeyMetadata = KeyMetadata()
            self._KeyMetadata._deserialize(params.get("KeyMetadata"))
        self._RequestId = params.get("RequestId")


class DescribeKeysRequest(AbstractModel):
    """DescribeKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 查询CMK的ID列表，批量查询一次最多支持100个KeyId
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyMetadatas: 返回的属性信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyMetadatas: list of KeyMetadata
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyMetadatas = None
        self._RequestId = None

    @property
    def KeyMetadatas(self):
        return self._KeyMetadatas

    @KeyMetadatas.setter
    def KeyMetadatas(self, KeyMetadatas):
        self._KeyMetadatas = KeyMetadatas

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyMetadatas") is not None:
            self._KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self._KeyMetadatas.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxDecryptKeyRequest(AbstractModel):
    """DescribeWhiteBoxDecryptKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥的全局唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxDecryptKeyResponse(AbstractModel):
    """DescribeWhiteBoxDecryptKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DecryptKey: 白盒解密密钥，base64编码
        :type DecryptKey: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DecryptKey = None
        self._RequestId = None

    @property
    def DecryptKey(self):
        return self._DecryptKey

    @DecryptKey.setter
    def DecryptKey(self, DecryptKey):
        self._DecryptKey = DecryptKey

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DecryptKey = params.get("DecryptKey")
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxDeviceFingerprintsResponse(AbstractModel):
    """DescribeWhiteBoxDeviceFingerprints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceFingerprints: 设备指纹列表
        :type DeviceFingerprints: list of DeviceFingerprint
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeviceFingerprints = None
        self._RequestId = None

    @property
    def DeviceFingerprints(self):
        return self._DeviceFingerprints

    @DeviceFingerprints.setter
    def DeviceFingerprints(self, DeviceFingerprints):
        self._DeviceFingerprints = DeviceFingerprints

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeviceFingerprints") is not None:
            self._DeviceFingerprints = []
            for item in params.get("DeviceFingerprints"):
                obj = DeviceFingerprint()
                obj._deserialize(item)
                self._DeviceFingerprints.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyDetailsRequest(AbstractModel):
    """DescribeWhiteBoxKeyDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyStatus: 过滤条件：密钥的状态，0：disabled，1：enabled
        :type KeyStatus: int
        :param _Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0
        :type Offset: int
        :param _Limit: 含义跟 SQL 查询的 Limit 一致，表示本次最多获取 Limit 个元素。缺省值为0, 表示不分页
        :type Limit: int
        :param _TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        """
        self._KeyStatus = None
        self._Offset = None
        self._Limit = None
        self._TagFilters = None

    @property
    def KeyStatus(self):
        return self._KeyStatus

    @KeyStatus.setter
    def KeyStatus(self, KeyStatus):
        self._KeyStatus = KeyStatus

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        self._KeyStatus = params.get("KeyStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxKeyDetailsResponse(AbstractModel):
    """DescribeWhiteBoxKeyDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyInfos: 白盒密钥信息列表。
        :type KeyInfos: list of WhiteboxKeyInfo
        :param _TotalCount: 白盒密钥总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyInfos = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def KeyInfos(self):
        return self._KeyInfos

    @KeyInfos.setter
    def KeyInfos(self, KeyInfos):
        self._KeyInfos = KeyInfos

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyInfos") is not None:
            self._KeyInfos = []
            for item in params.get("KeyInfos"):
                obj = WhiteboxKeyInfo()
                obj._deserialize(item)
                self._KeyInfos.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxKeyRequest(AbstractModel):
    """DescribeWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥的全局唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWhiteBoxKeyResponse(AbstractModel):
    """DescribeWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyInfo: 白盒密钥信息
        :type KeyInfo: :class:`tencentcloud.kms.v20190118.models.WhiteboxKeyInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyInfo = None
        self._RequestId = None

    @property
    def KeyInfo(self):
        return self._KeyInfo

    @KeyInfo.setter
    def KeyInfo(self, KeyInfo):
        self._KeyInfo = KeyInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeyInfo") is not None:
            self._KeyInfo = WhiteboxKeyInfo()
            self._KeyInfo._deserialize(params.get("KeyInfo"))
        self._RequestId = params.get("RequestId")


class DescribeWhiteBoxServiceStatusRequest(AbstractModel):
    """DescribeWhiteBoxServiceStatus请求参数结构体

    """


class DescribeWhiteBoxServiceStatusResponse(AbstractModel):
    """DescribeWhiteBoxServiceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceEnabled: 用户的白盒密钥服务是否可用
        :type ServiceEnabled: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceEnabled = None
        self._RequestId = None

    @property
    def ServiceEnabled(self):
        return self._ServiceEnabled

    @ServiceEnabled.setter
    def ServiceEnabled(self, ServiceEnabled):
        self._ServiceEnabled = ServiceEnabled

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceEnabled = params.get("ServiceEnabled")
        self._RequestId = params.get("RequestId")


class DeviceFingerprint(AbstractModel):
    """设备指纹

    """

    def __init__(self):
        r"""
        :param _Identity: 指纹信息，由设备指纹采集工具采集获得，格式满足正则表达式：^[0-9a-f]{8}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{14}[\-][0-9a-f]{16}$
        :type Identity: str
        :param _Description: 描述信息，如：IP，设备名称等，最大1024字节
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        """
        self._Identity = None
        self._Description = None

    @property
    def Identity(self):
        return self._Identity

    @Identity.setter
    def Identity(self, Identity):
        self._Identity = Identity

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Identity = params.get("Identity")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyRequest(AbstractModel):
    """DisableKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyResponse(AbstractModel):
    """DisableKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableKeyRotationRequest(AbstractModel):
    """DisableKeyRotation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeyRotationResponse(AbstractModel):
    """DisableKeyRotation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableKeysRequest(AbstractModel):
    """DisableKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 需要批量禁用的CMK Id 列表，CMK数量最大支持100
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableKeysResponse(AbstractModel):
    """DisableKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableWhiteBoxKeyRequest(AbstractModel):
    """DisableWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥的全局唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWhiteBoxKeyResponse(AbstractModel):
    """DisableWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DisableWhiteBoxKeysRequest(AbstractModel):
    """DisableWhiteBoxKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 白盒密钥的全局唯一标识符列表。注意：要确保所有提供的KeyId是格式有效的，没有重复，个数不超过50个，并且都是有效存在的。
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableWhiteBoxKeysResponse(AbstractModel):
    """DisableWhiteBoxKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableKeyRequest(AbstractModel):
    """EnableKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeyResponse(AbstractModel):
    """EnableKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableKeyRotationRequest(AbstractModel):
    """EnableKeyRotation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK唯一标识符
        :type KeyId: str
        :param _RotateDays: 密钥轮转周期，单位天，允许范围 7 ~ 365，默认值 365。
        :type RotateDays: int
        """
        self._KeyId = None
        self._RotateDays = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RotateDays(self):
        return self._RotateDays

    @RotateDays.setter
    def RotateDays(self, RotateDays):
        self._RotateDays = RotateDays


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._RotateDays = params.get("RotateDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeyRotationResponse(AbstractModel):
    """EnableKeyRotation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableKeysRequest(AbstractModel):
    """EnableKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 需要批量启用的CMK Id 列表， CMK数量最大支持100
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableKeysResponse(AbstractModel):
    """EnableKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableWhiteBoxKeyRequest(AbstractModel):
    """EnableWhiteBoxKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥的全局唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWhiteBoxKeyResponse(AbstractModel):
    """EnableWhiteBoxKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EnableWhiteBoxKeysRequest(AbstractModel):
    """EnableWhiteBoxKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyIds: 白盒密钥的全局唯一标识符列表。注意：要确保所有提供的KeyId是格式有效的，没有重复，个数不超过50个，并且都是有效存在的。
        :type KeyIds: list of str
        """
        self._KeyIds = None

    @property
    def KeyIds(self):
        return self._KeyIds

    @KeyIds.setter
    def KeyIds(self, KeyIds):
        self._KeyIds = KeyIds


    def _deserialize(self, params):
        self._KeyIds = params.get("KeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableWhiteBoxKeysResponse(AbstractModel):
    """EnableWhiteBoxKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EncryptByWhiteBoxRequest(AbstractModel):
    """EncryptByWhiteBox请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥的全局唯一标识符
        :type KeyId: str
        :param _PlainText: 待加密的文本， base64编码，文本的原始长度最大不超过4KB
        :type PlainText: str
        :param _InitializationVector: 初始化向量，大小为 16 Bytes，加密算法会使用到, base64编码；如果不传，则由后端服务随机生成。用户需要自行保存该值，作为解密的参数。
        :type InitializationVector: str
        """
        self._KeyId = None
        self._PlainText = None
        self._InitializationVector = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PlainText(self):
        return self._PlainText

    @PlainText.setter
    def PlainText(self, PlainText):
        self._PlainText = PlainText

    @property
    def InitializationVector(self):
        return self._InitializationVector

    @InitializationVector.setter
    def InitializationVector(self, InitializationVector):
        self._InitializationVector = InitializationVector


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._PlainText = params.get("PlainText")
        self._InitializationVector = params.get("InitializationVector")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptByWhiteBoxResponse(AbstractModel):
    """EncryptByWhiteBox返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InitializationVector: 初始化向量，加密算法会使用到, base64编码。如果由调用方在入参中传入，则原样返回。如果调用方没有传入，则后端服务随机生成，并返回
        :type InitializationVector: str
        :param _CipherText: 加密后的密文，base64编码
        :type CipherText: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InitializationVector = None
        self._CipherText = None
        self._RequestId = None

    @property
    def InitializationVector(self):
        return self._InitializationVector

    @InitializationVector.setter
    def InitializationVector(self, InitializationVector):
        self._InitializationVector = InitializationVector

    @property
    def CipherText(self):
        return self._CipherText

    @CipherText.setter
    def CipherText(self, CipherText):
        self._CipherText = CipherText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InitializationVector = params.get("InitializationVector")
        self._CipherText = params.get("CipherText")
        self._RequestId = params.get("RequestId")


class EncryptRequest(AbstractModel):
    """Encrypt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 调用CreateKey生成的CMK全局唯一标识符
        :type KeyId: str
        :param _Plaintext: 被加密的明文数据，该字段必须使用base64编码，原文最大长度支持4K
        :type Plaintext: str
        :param _EncryptionContext: key/value对的json字符串，如果指定了该参数，则在调用Decrypt API时需要提供同样的参数，最大支持1024个字符
        :type EncryptionContext: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._EncryptionContext = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def EncryptionContext(self):
        return self._EncryptionContext

    @EncryptionContext.setter
    def EncryptionContext(self, EncryptionContext):
        self._EncryptionContext = EncryptionContext


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._EncryptionContext = params.get("EncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EncryptResponse(AbstractModel):
    """Encrypt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: 加密后的密文，base64编码。注意：本字段中打包了密文和密钥的相关信息，不是对明文的直接加密结果，只有将该字段作为Decrypt接口的输入参数，才可以解密出原文。
        :type CiphertextBlob: str
        :param _KeyId: 加密使用的CMK的全局唯一标识
        :type KeyId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CiphertextBlob = None
        self._KeyId = None
        self._RequestId = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class GenerateDataKeyRequest(AbstractModel):
    """GenerateDataKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK全局唯一标识符
        :type KeyId: str
        :param _KeySpec: 指定生成Datakey的加密算法以及Datakey大小，AES_128或者AES_256。KeySpec 和 NumberOfBytes 必须指定一个
        :type KeySpec: str
        :param _NumberOfBytes: 生成的DataKey的长度，同时指定NumberOfBytes和KeySpec时，以NumberOfBytes为准。最小值为1， 最大值为1024。KeySpec 和 NumberOfBytes 必须指定一个
        :type NumberOfBytes: int
        :param _EncryptionContext: key/value对的json字符串，如果使用该字段，则返回的DataKey在解密时需要填入相同的字符串
        :type EncryptionContext: str
        :param _EncryptionPublicKey: PEM 格式公钥字符串，支持 RSA2048 和 SM2 公钥，用于对返回数据中的 Plaintext 值进行加密。若为空，则不对 Plaintext 值加密。
        :type EncryptionPublicKey: str
        :param _EncryptionAlgorithm: 非对称加密算法，配合 EncryptionPublicKey 对返回数据进行加密。目前支持：SM2（以 C1C3C2 格式返回密文），SM2_C1C3C2_ASN1 （以 C1C3C2 ASN1 格式返回密文），RSAES_PKCS1_V1_5，RSAES_OAEP_SHA_1，RSAES_OAEP_SHA_256。若为空，则默认为 SM2。
        :type EncryptionAlgorithm: str
        """
        self._KeyId = None
        self._KeySpec = None
        self._NumberOfBytes = None
        self._EncryptionContext = None
        self._EncryptionPublicKey = None
        self._EncryptionAlgorithm = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeySpec(self):
        return self._KeySpec

    @KeySpec.setter
    def KeySpec(self, KeySpec):
        self._KeySpec = KeySpec

    @property
    def NumberOfBytes(self):
        return self._NumberOfBytes

    @NumberOfBytes.setter
    def NumberOfBytes(self, NumberOfBytes):
        self._NumberOfBytes = NumberOfBytes

    @property
    def EncryptionContext(self):
        return self._EncryptionContext

    @EncryptionContext.setter
    def EncryptionContext(self, EncryptionContext):
        self._EncryptionContext = EncryptionContext

    @property
    def EncryptionPublicKey(self):
        return self._EncryptionPublicKey

    @EncryptionPublicKey.setter
    def EncryptionPublicKey(self, EncryptionPublicKey):
        self._EncryptionPublicKey = EncryptionPublicKey

    @property
    def EncryptionAlgorithm(self):
        return self._EncryptionAlgorithm

    @EncryptionAlgorithm.setter
    def EncryptionAlgorithm(self, EncryptionAlgorithm):
        self._EncryptionAlgorithm = EncryptionAlgorithm


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._KeySpec = params.get("KeySpec")
        self._NumberOfBytes = params.get("NumberOfBytes")
        self._EncryptionContext = params.get("EncryptionContext")
        self._EncryptionPublicKey = params.get("EncryptionPublicKey")
        self._EncryptionAlgorithm = params.get("EncryptionAlgorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateDataKeyResponse(AbstractModel):
    """GenerateDataKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的全局唯一标识
        :type KeyId: str
        :param _Plaintext: 若调用时未提供 EncryptionPublicKey，该字段值为生成的数据密钥 DataKey 的 Base64 编码的明文，需进行 Base64 解码以获取 DataKey 明文。
若调用时提供了 EncryptionPublicKey，则该字段值为使用 EncryptionPublicKey 公钥进行非对称加密后的 Base64 编码的密文。需在 Base64 解码后，使用用户上传的公钥对应的私钥进行进一步解密，以获取 DataKey 明文。
        :type Plaintext: str
        :param _CiphertextBlob: 数据密钥DataKey加密后的密文，用户需要自行保存该密文，KMS不托管用户的数据密钥。可以通过Decrypt接口从CiphertextBlob中获取数据密钥DataKey明文
        :type CiphertextBlob: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._Plaintext = None
        self._CiphertextBlob = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Plaintext = params.get("Plaintext")
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._RequestId = params.get("RequestId")


class GenerateRandomRequest(AbstractModel):
    """GenerateRandom请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NumberOfBytes: 生成的随机数的长度。最小值为1， 最大值为1024。
        :type NumberOfBytes: int
        """
        self._NumberOfBytes = None

    @property
    def NumberOfBytes(self):
        return self._NumberOfBytes

    @NumberOfBytes.setter
    def NumberOfBytes(self, NumberOfBytes):
        self._NumberOfBytes = NumberOfBytes


    def _deserialize(self, params):
        self._NumberOfBytes = params.get("NumberOfBytes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateRandomResponse(AbstractModel):
    """GenerateRandom返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Plaintext: 生成的随机数的明文，该明文使用base64编码，用户需要使用base64解码得到明文。
        :type Plaintext: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Plaintext = None
        self._RequestId = None

    @property
    def Plaintext(self):
        return self._Plaintext

    @Plaintext.setter
    def Plaintext(self, Plaintext):
        self._Plaintext = Plaintext

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Plaintext = params.get("Plaintext")
        self._RequestId = params.get("RequestId")


class GetKeyRotationStatusRequest(AbstractModel):
    """GetKeyRotationStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetKeyRotationStatusResponse(AbstractModel):
    """GetKeyRotationStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyRotationEnabled: 密钥轮换是否开启
        :type KeyRotationEnabled: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyRotationEnabled = None
        self._RequestId = None

    @property
    def KeyRotationEnabled(self):
        return self._KeyRotationEnabled

    @KeyRotationEnabled.setter
    def KeyRotationEnabled(self, KeyRotationEnabled):
        self._KeyRotationEnabled = KeyRotationEnabled

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyRotationEnabled = params.get("KeyRotationEnabled")
        self._RequestId = params.get("RequestId")


class GetParametersForImportRequest(AbstractModel):
    """GetParametersForImport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标识，获取密钥参数的CMK必须是EXTERNAL类型，即在CreateKey时指定Type=2 类型的CMK。
        :type KeyId: str
        :param _WrappingAlgorithm: 指定加密密钥材料的算法，目前支持RSAES_PKCS1_V1_5、RSAES_OAEP_SHA_1、RSAES_OAEP_SHA_256
        :type WrappingAlgorithm: str
        :param _WrappingKeySpec: 指定加密密钥材料的类型，目前只支持RSA_2048
        :type WrappingKeySpec: str
        """
        self._KeyId = None
        self._WrappingAlgorithm = None
        self._WrappingKeySpec = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def WrappingAlgorithm(self):
        return self._WrappingAlgorithm

    @WrappingAlgorithm.setter
    def WrappingAlgorithm(self, WrappingAlgorithm):
        self._WrappingAlgorithm = WrappingAlgorithm

    @property
    def WrappingKeySpec(self):
        return self._WrappingKeySpec

    @WrappingKeySpec.setter
    def WrappingKeySpec(self, WrappingKeySpec):
        self._WrappingKeySpec = WrappingKeySpec


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._WrappingAlgorithm = params.get("WrappingAlgorithm")
        self._WrappingKeySpec = params.get("WrappingKeySpec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetParametersForImportResponse(AbstractModel):
    """GetParametersForImport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标识，用于指定目标导入密钥材料的CMK。
        :type KeyId: str
        :param _ImportToken: 导入密钥材料需要的token，用于作为 ImportKeyMaterial 的参数。
        :type ImportToken: str
        :param _PublicKey: 用于加密密钥材料的RSA公钥，base64编码。使用PublicKey base64解码后的公钥将导入密钥进行加密后作为 ImportKeyMaterial 的参数。
        :type PublicKey: str
        :param _ParametersValidTo: 该导出token和公钥的有效期，超过该时间后无法导入，需要重新调用GetParametersForImport获取。
        :type ParametersValidTo: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._ImportToken = None
        self._PublicKey = None
        self._ParametersValidTo = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ImportToken(self):
        return self._ImportToken

    @ImportToken.setter
    def ImportToken(self, ImportToken):
        self._ImportToken = ImportToken

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def ParametersValidTo(self):
        return self._ParametersValidTo

    @ParametersValidTo.setter
    def ParametersValidTo(self, ParametersValidTo):
        self._ParametersValidTo = ParametersValidTo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._ImportToken = params.get("ImportToken")
        self._PublicKey = params.get("PublicKey")
        self._ParametersValidTo = params.get("ParametersValidTo")
        self._RequestId = params.get("RequestId")


class GetPublicKeyRequest(AbstractModel):
    """GetPublicKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标识。
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetPublicKeyResponse(AbstractModel):
    """GetPublicKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标识。
        :type KeyId: str
        :param _PublicKey: 经过base64编码的公钥内容。
        :type PublicKey: str
        :param _PublicKeyPem: PEM格式的公钥内容。
        :type PublicKeyPem: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._PublicKey = None
        self._PublicKeyPem = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PublicKeyPem(self):
        return self._PublicKeyPem

    @PublicKeyPem.setter
    def PublicKeyPem(self, PublicKeyPem):
        self._PublicKeyPem = PublicKeyPem

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._PublicKey = params.get("PublicKey")
        self._PublicKeyPem = params.get("PublicKeyPem")
        self._RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions请求参数结构体

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Regions: 可用region列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Regions: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Regions = None
        self._RequestId = None

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Regions = params.get("Regions")
        self._RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus请求参数结构体

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceEnabled: KMS服务是否开通， true 表示已开通
        :type ServiceEnabled: bool
        :param _InvalidType: 服务不可用类型： 0-未购买，1-正常， 2-欠费停服， 3-资源释放
注意：此字段可能返回 null，表示取不到有效值。
        :type InvalidType: int
        :param _UserLevel: 0-普通版，1-旗舰版
        :type UserLevel: int
        :param _ProExpireTime: 旗舰版到期时间（Epoch Unix Timestamp）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProExpireTime: int
        :param _ProRenewFlag: 旗舰版是否自动续费：0-不自动续费，1-自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type ProRenewFlag: int
        :param _ProResourceId: 旗舰版购买记录的唯一性标识。如果为开通旗舰版，则返回值为空
注意：此字段可能返回 null，表示取不到有效值。
        :type ProResourceId: str
        :param _ExclusiveVSMEnabled: 是否开通 KMS 托管版
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusiveVSMEnabled: bool
        :param _ExclusiveHSMEnabled: 是否开通 KMS 独享版
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusiveHSMEnabled: bool
        :param _SubscriptionInfo: KMS 订阅信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubscriptionInfo: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceEnabled = None
        self._InvalidType = None
        self._UserLevel = None
        self._ProExpireTime = None
        self._ProRenewFlag = None
        self._ProResourceId = None
        self._ExclusiveVSMEnabled = None
        self._ExclusiveHSMEnabled = None
        self._SubscriptionInfo = None
        self._RequestId = None

    @property
    def ServiceEnabled(self):
        return self._ServiceEnabled

    @ServiceEnabled.setter
    def ServiceEnabled(self, ServiceEnabled):
        self._ServiceEnabled = ServiceEnabled

    @property
    def InvalidType(self):
        return self._InvalidType

    @InvalidType.setter
    def InvalidType(self, InvalidType):
        self._InvalidType = InvalidType

    @property
    def UserLevel(self):
        return self._UserLevel

    @UserLevel.setter
    def UserLevel(self, UserLevel):
        self._UserLevel = UserLevel

    @property
    def ProExpireTime(self):
        return self._ProExpireTime

    @ProExpireTime.setter
    def ProExpireTime(self, ProExpireTime):
        self._ProExpireTime = ProExpireTime

    @property
    def ProRenewFlag(self):
        return self._ProRenewFlag

    @ProRenewFlag.setter
    def ProRenewFlag(self, ProRenewFlag):
        self._ProRenewFlag = ProRenewFlag

    @property
    def ProResourceId(self):
        return self._ProResourceId

    @ProResourceId.setter
    def ProResourceId(self, ProResourceId):
        self._ProResourceId = ProResourceId

    @property
    def ExclusiveVSMEnabled(self):
        return self._ExclusiveVSMEnabled

    @ExclusiveVSMEnabled.setter
    def ExclusiveVSMEnabled(self, ExclusiveVSMEnabled):
        self._ExclusiveVSMEnabled = ExclusiveVSMEnabled

    @property
    def ExclusiveHSMEnabled(self):
        return self._ExclusiveHSMEnabled

    @ExclusiveHSMEnabled.setter
    def ExclusiveHSMEnabled(self, ExclusiveHSMEnabled):
        self._ExclusiveHSMEnabled = ExclusiveHSMEnabled

    @property
    def SubscriptionInfo(self):
        return self._SubscriptionInfo

    @SubscriptionInfo.setter
    def SubscriptionInfo(self, SubscriptionInfo):
        self._SubscriptionInfo = SubscriptionInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceEnabled = params.get("ServiceEnabled")
        self._InvalidType = params.get("InvalidType")
        self._UserLevel = params.get("UserLevel")
        self._ProExpireTime = params.get("ProExpireTime")
        self._ProRenewFlag = params.get("ProRenewFlag")
        self._ProResourceId = params.get("ProResourceId")
        self._ExclusiveVSMEnabled = params.get("ExclusiveVSMEnabled")
        self._ExclusiveHSMEnabled = params.get("ExclusiveHSMEnabled")
        self._SubscriptionInfo = params.get("SubscriptionInfo")
        self._RequestId = params.get("RequestId")


class ImportKeyMaterialRequest(AbstractModel):
    """ImportKeyMaterial请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EncryptedKeyMaterial: 使用GetParametersForImport 返回的PublicKey加密后的密钥材料base64编码。对于国密版本region的KMS，导入的密钥材料长度要求为 128 bit，FIPS版本region的KMS， 导入的密钥材料长度要求为 256 bit。
        :type EncryptedKeyMaterial: str
        :param _ImportToken: 通过调用GetParametersForImport获得的导入令牌。
        :type ImportToken: str
        :param _KeyId: 指定导入密钥材料的CMK，需要和GetParametersForImport 指定的CMK相同。
        :type KeyId: str
        :param _ValidTo: 密钥材料过期时间 unix 时间戳，不指定或者 0 表示密钥材料不会过期，若指定过期时间，需要大于当前时间点，最大支持 2147443200。
        :type ValidTo: int
        """
        self._EncryptedKeyMaterial = None
        self._ImportToken = None
        self._KeyId = None
        self._ValidTo = None

    @property
    def EncryptedKeyMaterial(self):
        return self._EncryptedKeyMaterial

    @EncryptedKeyMaterial.setter
    def EncryptedKeyMaterial(self, EncryptedKeyMaterial):
        self._EncryptedKeyMaterial = EncryptedKeyMaterial

    @property
    def ImportToken(self):
        return self._ImportToken

    @ImportToken.setter
    def ImportToken(self, ImportToken):
        self._ImportToken = ImportToken

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ValidTo(self):
        return self._ValidTo

    @ValidTo.setter
    def ValidTo(self, ValidTo):
        self._ValidTo = ValidTo


    def _deserialize(self, params):
        self._EncryptedKeyMaterial = params.get("EncryptedKeyMaterial")
        self._ImportToken = params.get("ImportToken")
        self._KeyId = params.get("KeyId")
        self._ValidTo = params.get("ValidTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportKeyMaterialResponse(AbstractModel):
    """ImportKeyMaterial返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Key(AbstractModel):
    """返回CMK列表信息

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的全局唯一标识。
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyMetadata(AbstractModel):
    """CMK属性信息

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的全局唯一标识
        :type KeyId: str
        :param _Alias: 作为密钥更容易辨识，更容易被人看懂的别名
        :type Alias: str
        :param _CreateTime: 密钥创建时间
        :type CreateTime: int
        :param _Description: CMK的描述
        :type Description: str
        :param _KeyState: CMK的状态， 取值为：Enabled | Disabled | PendingDelete | PendingImport | Archived
        :type KeyState: str
        :param _KeyUsage: CMK用途，取值为: ENCRYPT_DECRYPT | ASYMMETRIC_DECRYPT_RSA_2048 | ASYMMETRIC_DECRYPT_SM2 | ASYMMETRIC_SIGN_VERIFY_SM2 | ASYMMETRIC_SIGN_VERIFY_RSA_2048 | ASYMMETRIC_SIGN_VERIFY_ECC
        :type KeyUsage: str
        :param _Type: CMK类型，2 表示符合FIPS标准，4表示符合国密标准
        :type Type: int
        :param _CreatorUin: 创建者
        :type CreatorUin: int
        :param _KeyRotationEnabled: 是否开启了密钥轮换功能
        :type KeyRotationEnabled: bool
        :param _Owner: CMK的创建者，用户创建的为 user，授权各云产品自动创建的为对应的产品名
        :type Owner: str
        :param _NextRotateTime: 在密钥轮换开启状态下，下次轮换的时间
        :type NextRotateTime: int
        :param _DeletionDate: 计划删除的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DeletionDate: int
        :param _Origin: CMK 密钥材料类型，由KMS创建的为： TENCENT_KMS， 由用户导入的类型为：EXTERNAL
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: str
        :param _ValidTo: 在Origin为  EXTERNAL 时有效，表示密钥材料的有效日期， 0 表示不过期
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidTo: int
        :param _ResourceId: 资源ID，格式：creatorUin/$creatorUin/$keyId
        :type ResourceId: str
        :param _HsmClusterId: HSM 集群 ID（仅对 KMS 独占版/托管版服务实例有效）
注意：此字段可能返回 null，表示取不到有效值。
        :type HsmClusterId: str
        """
        self._KeyId = None
        self._Alias = None
        self._CreateTime = None
        self._Description = None
        self._KeyState = None
        self._KeyUsage = None
        self._Type = None
        self._CreatorUin = None
        self._KeyRotationEnabled = None
        self._Owner = None
        self._NextRotateTime = None
        self._DeletionDate = None
        self._Origin = None
        self._ValidTo = None
        self._ResourceId = None
        self._HsmClusterId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KeyState(self):
        return self._KeyState

    @KeyState.setter
    def KeyState(self, KeyState):
        self._KeyState = KeyState

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreatorUin(self):
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def KeyRotationEnabled(self):
        return self._KeyRotationEnabled

    @KeyRotationEnabled.setter
    def KeyRotationEnabled(self, KeyRotationEnabled):
        self._KeyRotationEnabled = KeyRotationEnabled

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def NextRotateTime(self):
        return self._NextRotateTime

    @NextRotateTime.setter
    def NextRotateTime(self, NextRotateTime):
        self._NextRotateTime = NextRotateTime

    @property
    def DeletionDate(self):
        return self._DeletionDate

    @DeletionDate.setter
    def DeletionDate(self, DeletionDate):
        self._DeletionDate = DeletionDate

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def ValidTo(self):
        return self._ValidTo

    @ValidTo.setter
    def ValidTo(self, ValidTo):
        self._ValidTo = ValidTo

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Alias = params.get("Alias")
        self._CreateTime = params.get("CreateTime")
        self._Description = params.get("Description")
        self._KeyState = params.get("KeyState")
        self._KeyUsage = params.get("KeyUsage")
        self._Type = params.get("Type")
        self._CreatorUin = params.get("CreatorUin")
        self._KeyRotationEnabled = params.get("KeyRotationEnabled")
        self._Owner = params.get("Owner")
        self._NextRotateTime = params.get("NextRotateTime")
        self._DeletionDate = params.get("DeletionDate")
        self._Origin = params.get("Origin")
        self._ValidTo = params.get("ValidTo")
        self._ResourceId = params.get("ResourceId")
        self._HsmClusterId = params.get("HsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAlgorithmsRequest(AbstractModel):
    """ListAlgorithms请求参数结构体

    """


class ListAlgorithmsResponse(AbstractModel):
    """ListAlgorithms返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SymmetricAlgorithms: 本地区支持的对称加密算法
        :type SymmetricAlgorithms: list of AlgorithmInfo
        :param _AsymmetricAlgorithms: 本地区支持的非对称加密算法
        :type AsymmetricAlgorithms: list of AlgorithmInfo
        :param _AsymmetricSignVerifyAlgorithms: 本地区支持的非对称签名验签算法
        :type AsymmetricSignVerifyAlgorithms: list of AlgorithmInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SymmetricAlgorithms = None
        self._AsymmetricAlgorithms = None
        self._AsymmetricSignVerifyAlgorithms = None
        self._RequestId = None

    @property
    def SymmetricAlgorithms(self):
        return self._SymmetricAlgorithms

    @SymmetricAlgorithms.setter
    def SymmetricAlgorithms(self, SymmetricAlgorithms):
        self._SymmetricAlgorithms = SymmetricAlgorithms

    @property
    def AsymmetricAlgorithms(self):
        return self._AsymmetricAlgorithms

    @AsymmetricAlgorithms.setter
    def AsymmetricAlgorithms(self, AsymmetricAlgorithms):
        self._AsymmetricAlgorithms = AsymmetricAlgorithms

    @property
    def AsymmetricSignVerifyAlgorithms(self):
        return self._AsymmetricSignVerifyAlgorithms

    @AsymmetricSignVerifyAlgorithms.setter
    def AsymmetricSignVerifyAlgorithms(self, AsymmetricSignVerifyAlgorithms):
        self._AsymmetricSignVerifyAlgorithms = AsymmetricSignVerifyAlgorithms

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SymmetricAlgorithms") is not None:
            self._SymmetricAlgorithms = []
            for item in params.get("SymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self._SymmetricAlgorithms.append(obj)
        if params.get("AsymmetricAlgorithms") is not None:
            self._AsymmetricAlgorithms = []
            for item in params.get("AsymmetricAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self._AsymmetricAlgorithms.append(obj)
        if params.get("AsymmetricSignVerifyAlgorithms") is not None:
            self._AsymmetricSignVerifyAlgorithms = []
            for item in params.get("AsymmetricSignVerifyAlgorithms"):
                obj = AlgorithmInfo()
                obj._deserialize(item)
                self._AsymmetricSignVerifyAlgorithms.append(obj)
        self._RequestId = params.get("RequestId")


class ListKeyDetailRequest(AbstractModel):
    """ListKeyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0
        :type Offset: int
        :param _Limit: 含义跟 SQL 查询的 Limit 一致，表示本次最多获取 Limit 个元素。缺省值为10，最大值为200
        :type Limit: int
        :param _Role: 根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk
        :type Role: int
        :param _OrderType: 根据CMK创建时间排序， 0 表示按照降序排序，1表示按照升序排序
        :type OrderType: int
        :param _KeyState: 根据CMK状态筛选， 0表示全部CMK， 1 表示仅查询Enabled CMK， 2 表示仅查询Disabled CMK，3 表示查询PendingDelete 状态的CMK(处于计划删除状态的Key)，4 表示查询 PendingImport 状态的CMK，5 表示查询 Archived 状态的 CMK
        :type KeyState: int
        :param _SearchKeyAlias: 根据KeyId或者Alias进行模糊匹配查询
        :type SearchKeyAlias: str
        :param _Origin: 根据CMK类型筛选， "TENCENT_KMS" 表示筛选密钥材料由KMS创建的CMK， "EXTERNAL" 表示筛选密钥材料需要用户导入的 EXTERNAL类型CMK，"ALL" 或者不设置表示两种类型都查询，大小写敏感。
        :type Origin: str
        :param _KeyUsage: 根据CMK的KeyUsage筛选，ALL表示筛选全部，可使用的参数为：ALL 或 ENCRYPT_DECRYPT 或 ASYMMETRIC_DECRYPT_RSA_2048 或 ASYMMETRIC_DECRYPT_SM2 或 ASYMMETRIC_SIGN_VERIFY_SM2 或 ASYMMETRIC_SIGN_VERIFY_RSA_2048 或 ASYMMETRIC_SIGN_VERIFY_ECC，为空则默认筛选ENCRYPT_DECRYPT类型
        :type KeyUsage: str
        :param _TagFilters: 标签过滤条件
        :type TagFilters: list of TagFilter
        :param _HsmClusterId: KMS 高级版对应的 HSM 集群 ID（仅对 KMS 独占版/托管版服务实例有效）。
        :type HsmClusterId: str
        """
        self._Offset = None
        self._Limit = None
        self._Role = None
        self._OrderType = None
        self._KeyState = None
        self._SearchKeyAlias = None
        self._Origin = None
        self._KeyUsage = None
        self._TagFilters = None
        self._HsmClusterId = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def OrderType(self):
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def KeyState(self):
        return self._KeyState

    @KeyState.setter
    def KeyState(self, KeyState):
        self._KeyState = KeyState

    @property
    def SearchKeyAlias(self):
        return self._SearchKeyAlias

    @SearchKeyAlias.setter
    def SearchKeyAlias(self, SearchKeyAlias):
        self._SearchKeyAlias = SearchKeyAlias

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def KeyUsage(self):
        return self._KeyUsage

    @KeyUsage.setter
    def KeyUsage(self, KeyUsage):
        self._KeyUsage = KeyUsage

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Role = params.get("Role")
        self._OrderType = params.get("OrderType")
        self._KeyState = params.get("KeyState")
        self._SearchKeyAlias = params.get("SearchKeyAlias")
        self._Origin = params.get("Origin")
        self._KeyUsage = params.get("KeyUsage")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._HsmClusterId = params.get("HsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeyDetailResponse(AbstractModel):
    """ListKeyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: CMK的总数量
        :type TotalCount: int
        :param _KeyMetadatas: 返回的属性信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyMetadatas: list of KeyMetadata
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._KeyMetadatas = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def KeyMetadatas(self):
        return self._KeyMetadatas

    @KeyMetadatas.setter
    def KeyMetadatas(self, KeyMetadatas):
        self._KeyMetadatas = KeyMetadatas

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("KeyMetadatas") is not None:
            self._KeyMetadatas = []
            for item in params.get("KeyMetadatas"):
                obj = KeyMetadata()
                obj._deserialize(item)
                self._KeyMetadatas.append(obj)
        self._RequestId = params.get("RequestId")


class ListKeysRequest(AbstractModel):
    """ListKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0
        :type Offset: int
        :param _Limit: 含义跟 SQL 查询的 Limit 一致，表示本次获最多获取 Limit 个元素。缺省值为10，最大值为200
        :type Limit: int
        :param _Role: 根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk
        :type Role: int
        :param _HsmClusterId: KMS 高级版对应的 HSM 集群 ID（仅对 KMS 独占版/托管版服务实例有效）。
        :type HsmClusterId: str
        """
        self._Offset = None
        self._Limit = None
        self._Role = None
        self._HsmClusterId = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def HsmClusterId(self):
        return self._HsmClusterId

    @HsmClusterId.setter
    def HsmClusterId(self, HsmClusterId):
        self._HsmClusterId = HsmClusterId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Role = params.get("Role")
        self._HsmClusterId = params.get("HsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListKeysResponse(AbstractModel):
    """ListKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Keys: CMK列表数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of Key
        :param _TotalCount: CMK的总数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Keys = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Keys(self):
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = Key()
                obj._deserialize(item)
                self._Keys.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class OverwriteWhiteBoxDeviceFingerprintsRequest(AbstractModel):
    """OverwriteWhiteBoxDeviceFingerprints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥ID
        :type KeyId: str
        :param _DeviceFingerprints: 设备指纹列表，如果列表为空，则表示删除该密钥对应的所有指纹信息。列表最大长度不超过200。
        :type DeviceFingerprints: list of DeviceFingerprint
        """
        self._KeyId = None
        self._DeviceFingerprints = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def DeviceFingerprints(self):
        return self._DeviceFingerprints

    @DeviceFingerprints.setter
    def DeviceFingerprints(self, DeviceFingerprints):
        self._DeviceFingerprints = DeviceFingerprints


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        if params.get("DeviceFingerprints") is not None:
            self._DeviceFingerprints = []
            for item in params.get("DeviceFingerprints"):
                obj = DeviceFingerprint()
                obj._deserialize(item)
                self._DeviceFingerprints.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverwriteWhiteBoxDeviceFingerprintsResponse(AbstractModel):
    """OverwriteWhiteBoxDeviceFingerprints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class PostQuantumCryptoDecryptRequest(AbstractModel):
    """PostQuantumCryptoDecrypt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: 待解密的密文数据
        :type CiphertextBlob: str
        :param _EncryptionPublicKey: PEM 格式公钥字符串，支持 RSA2048 和 SM2 公钥，用于对返回数据中的 Plaintext 值进行加密。若为空，则不对 Plaintext 值加密。
        :type EncryptionPublicKey: str
        :param _EncryptionAlgorithm: 非对称加密算法，配合 EncryptionPublicKey 对返回数据进行加密。目前支持：SM2（以 C1C3C2 格式返回密文），SM2_C1C3C2_ASN1 （以 C1C3C2 ASN1 格式返回密文），RSAES_PKCS1_V1_5，RSAES_OAEP_SHA_1，RSAES_OAEP_SHA_256。若为空，则默认为 SM2。
        :type EncryptionAlgorithm: str
        """
        self._CiphertextBlob = None
        self._EncryptionPublicKey = None
        self._EncryptionAlgorithm = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def EncryptionPublicKey(self):
        return self._EncryptionPublicKey

    @EncryptionPublicKey.setter
    def EncryptionPublicKey(self, EncryptionPublicKey):
        self._EncryptionPublicKey = EncryptionPublicKey

    @property
    def EncryptionAlgorithm(self):
        return self._EncryptionAlgorithm

    @EncryptionAlgorithm.setter
    def EncryptionAlgorithm(self, EncryptionAlgorithm):
        self._EncryptionAlgorithm = EncryptionAlgorithm


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._EncryptionPublicKey = params.get("EncryptionPublicKey")
        self._EncryptionAlgorithm = params.get("EncryptionAlgorithm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostQuantumCryptoDecryptResponse(AbstractModel):
    """PostQuantumCryptoDecrypt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的全局唯一标识
        :type KeyId: str
        :param _PlainText: 若调用时未提供 EncryptionPublicKey，该字段值为 Base64 编码的明文，需进行 Base64 解码以获取明文。
若调用时提供了 EncryptionPublicKey，则该字段值为使用 EncryptionPublicKey 公钥进行非对称加密后的 Base64 编码的密文。需在 Base64 解码后，使用用户上传的公钥对应的私钥进行进一步解密，以获取明文。
        :type PlainText: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeyId = None
        self._PlainText = None
        self._RequestId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PlainText(self):
        return self._PlainText

    @PlainText.setter
    def PlainText(self, PlainText):
        self._PlainText = PlainText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._PlainText = params.get("PlainText")
        self._RequestId = params.get("RequestId")


class PostQuantumCryptoEncryptRequest(AbstractModel):
    """PostQuantumCryptoEncrypt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 调用CreateKey生成的CMK全局唯一标识符
        :type KeyId: str
        :param _PlainText: 被加密的明文数据，该字段必须使用base64编码，原文最大长度支持4K
        :type PlainText: str
        """
        self._KeyId = None
        self._PlainText = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PlainText(self):
        return self._PlainText

    @PlainText.setter
    def PlainText(self, PlainText):
        self._PlainText = PlainText


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._PlainText = params.get("PlainText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostQuantumCryptoEncryptResponse(AbstractModel):
    """PostQuantumCryptoEncrypt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: 加密后的密文，base64编码。注意：本字段中打包了密文和密钥的相关信息，不是对明文的直接加密结果，只有将该字段作为PostQuantumCryptoDecrypt接口的输入参数，才可以解密出原文。
        :type CiphertextBlob: str
        :param _KeyId: 加密使用的CMK的全局唯一标识
        :type KeyId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CiphertextBlob = None
        self._KeyId = None
        self._RequestId = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class PostQuantumCryptoSignRequest(AbstractModel):
    """PostQuantumCryptoSign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Message: Base64 编码的消息原文。消息原文的长度（Base64编码前的长度）不超过4096字节。
        :type Message: str
        :param _KeyId: 密钥的唯一标识
        :type KeyId: str
        """
        self._Message = None
        self._KeyId = None

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostQuantumCryptoSignResponse(AbstractModel):
    """PostQuantumCryptoSign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Signature: 签名值，Base64编码。可使用 PostQuantumCryptoVerify接口对签名值进行验证。
        :type Signature: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Signature = None
        self._RequestId = None

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Signature = params.get("Signature")
        self._RequestId = params.get("RequestId")


class PostQuantumCryptoVerifyRequest(AbstractModel):
    """PostQuantumCryptoVerify请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥的唯一标识
        :type KeyId: str
        :param _SignatureValue: 签名值，通过调用KMS PostQuantumCryptoSign签名接口生成
        :type SignatureValue: str
        :param _Message: Base64 编码的消息原文，消息原文的长度（Base64编码前的长度）不超过4096字节。
        :type Message: str
        """
        self._KeyId = None
        self._SignatureValue = None
        self._Message = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def SignatureValue(self):
        return self._SignatureValue

    @SignatureValue.setter
    def SignatureValue(self, SignatureValue):
        self._SignatureValue = SignatureValue

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._SignatureValue = params.get("SignatureValue")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostQuantumCryptoVerifyResponse(AbstractModel):
    """PostQuantumCryptoVerify返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignatureValid: 签名是否有效。true：签名有效，false：签名无效。
        :type SignatureValid: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignatureValid = None
        self._RequestId = None

    @property
    def SignatureValid(self):
        return self._SignatureValid

    @SignatureValid.setter
    def SignatureValid(self, SignatureValid):
        self._SignatureValid = SignatureValid

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignatureValid = params.get("SignatureValid")
        self._RequestId = params.get("RequestId")


class ReEncryptRequest(AbstractModel):
    """ReEncrypt请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: 需要重新加密的密文
        :type CiphertextBlob: str
        :param _DestinationKeyId: 重新加密使用的CMK，如果为空，则使用密文原有的CMK重新加密（若密钥没有轮换则密文不会刷新）
        :type DestinationKeyId: str
        :param _SourceEncryptionContext: CiphertextBlob 密文加密时使用的key/value对的json字符串。如果加密时未使用，则为空
        :type SourceEncryptionContext: str
        :param _DestinationEncryptionContext: 重新加密使用的key/value对的json字符串，如果使用该字段，则返回的新密文在解密时需要填入相同的字符串
        :type DestinationEncryptionContext: str
        """
        self._CiphertextBlob = None
        self._DestinationKeyId = None
        self._SourceEncryptionContext = None
        self._DestinationEncryptionContext = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def DestinationKeyId(self):
        return self._DestinationKeyId

    @DestinationKeyId.setter
    def DestinationKeyId(self, DestinationKeyId):
        self._DestinationKeyId = DestinationKeyId

    @property
    def SourceEncryptionContext(self):
        return self._SourceEncryptionContext

    @SourceEncryptionContext.setter
    def SourceEncryptionContext(self, SourceEncryptionContext):
        self._SourceEncryptionContext = SourceEncryptionContext

    @property
    def DestinationEncryptionContext(self):
        return self._DestinationEncryptionContext

    @DestinationEncryptionContext.setter
    def DestinationEncryptionContext(self, DestinationEncryptionContext):
        self._DestinationEncryptionContext = DestinationEncryptionContext


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._DestinationKeyId = params.get("DestinationKeyId")
        self._SourceEncryptionContext = params.get("SourceEncryptionContext")
        self._DestinationEncryptionContext = params.get("DestinationEncryptionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReEncryptResponse(AbstractModel):
    """ReEncrypt返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CiphertextBlob: 重新加密后的密文
        :type CiphertextBlob: str
        :param _KeyId: 重新加密使用的CMK
        :type KeyId: str
        :param _SourceKeyId: 重新加密前密文使用的CMK
        :type SourceKeyId: str
        :param _ReEncrypted: true表示密文已经重新加密。同一个CMK进行重加密，在密钥没有发生轮换的情况下不会进行实际重新加密操作，返回原密文
        :type ReEncrypted: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CiphertextBlob = None
        self._KeyId = None
        self._SourceKeyId = None
        self._ReEncrypted = None
        self._RequestId = None

    @property
    def CiphertextBlob(self):
        return self._CiphertextBlob

    @CiphertextBlob.setter
    def CiphertextBlob(self, CiphertextBlob):
        self._CiphertextBlob = CiphertextBlob

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def SourceKeyId(self):
        return self._SourceKeyId

    @SourceKeyId.setter
    def SourceKeyId(self, SourceKeyId):
        self._SourceKeyId = SourceKeyId

    @property
    def ReEncrypted(self):
        return self._ReEncrypted

    @ReEncrypted.setter
    def ReEncrypted(self, ReEncrypted):
        self._ReEncrypted = ReEncrypted

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CiphertextBlob = params.get("CiphertextBlob")
        self._KeyId = params.get("KeyId")
        self._SourceKeyId = params.get("SourceKeyId")
        self._ReEncrypted = params.get("ReEncrypted")
        self._RequestId = params.get("RequestId")


class ScheduleKeyDeletionRequest(AbstractModel):
    """ScheduleKeyDeletion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: CMK的唯一标志
        :type KeyId: str
        :param _PendingWindowInDays: 计划删除时间区间[7,30]
        :type PendingWindowInDays: int
        """
        self._KeyId = None
        self._PendingWindowInDays = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def PendingWindowInDays(self):
        return self._PendingWindowInDays

    @PendingWindowInDays.setter
    def PendingWindowInDays(self, PendingWindowInDays):
        self._PendingWindowInDays = PendingWindowInDays


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._PendingWindowInDays = params.get("PendingWindowInDays")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleKeyDeletionResponse(AbstractModel):
    """ScheduleKeyDeletion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeletionDate: 计划删除执行时间
        :type DeletionDate: int
        :param _KeyId: 唯一标志被计划删除的CMK
        :type KeyId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeletionDate = None
        self._KeyId = None
        self._RequestId = None

    @property
    def DeletionDate(self):
        return self._DeletionDate

    @DeletionDate.setter
    def DeletionDate(self, DeletionDate):
        self._DeletionDate = DeletionDate

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeletionDate = params.get("DeletionDate")
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class SignByAsymmetricKeyRequest(AbstractModel):
    """SignByAsymmetricKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Algorithm: 签名算法，支持的算法：SM2DSA，ECC_P256_R1，RSA_PSS_SHA_256，RSA_PKCS1_SHA_256 等。更多支持的算法可通过 ListAlgorithms 接口进行查询。
        :type Algorithm: str
        :param _Message: 消息原文或消息摘要。如果提供的是消息原文，则消息原文的长度（Base64编码前的长度）不超过4096字节。如果提供的是消息摘要，消息摘要长度（Base64编码前的长度）必须等于32字节
        :type Message: str
        :param _KeyId: 密钥的唯一标识
        :type KeyId: str
        :param _MessageType: 消息类型：RAW，DIGEST，如果不传，默认为RAW，表示消息原文。
        :type MessageType: str
        """
        self._Algorithm = None
        self._Message = None
        self._KeyId = None
        self._MessageType = None

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def MessageType(self):
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType


    def _deserialize(self, params):
        self._Algorithm = params.get("Algorithm")
        self._Message = params.get("Message")
        self._KeyId = params.get("KeyId")
        self._MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SignByAsymmetricKeyResponse(AbstractModel):
    """SignByAsymmetricKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Signature: 签名，Base64编码
        :type Signature: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Signature = None
        self._RequestId = None

    @property
    def Signature(self):
        return self._Signature

    @Signature.setter
    def Signature(self, Signature):
        self._Signature = Signature

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Signature = params.get("Signature")
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    """标签键和标签值

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """标签过滤器

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudResourceRequest(AbstractModel):
    """UnbindCloudResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: cmk的ID
        :type KeyId: str
        :param _ProductId: 云产品的唯一性标识符
        :type ProductId: str
        :param _ResourceId: 资源/实例ID，由调用方根据自己的云产品特征来定义，以字符串形式做存储。
        :type ResourceId: str
        """
        self._KeyId = None
        self._ProductId = None
        self._ResourceId = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._ProductId = params.get("ProductId")
        self._ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindCloudResourceResponse(AbstractModel):
    """UnbindCloudResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Alias: 新的别名，1-60个字符或数字的组合
        :type Alias: str
        :param _KeyId: CMK的全局唯一标识符
        :type KeyId: str
        """
        self._Alias = None
        self._KeyId = None

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._Alias = params.get("Alias")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateKeyDescriptionRequest(AbstractModel):
    """UpdateKeyDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Description: 新的描述信息，最大支持1024字节
        :type Description: str
        :param _KeyId: 需要修改描述信息的CMK ID
        :type KeyId: str
        """
        self._Description = None
        self._KeyId = None

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateKeyDescriptionResponse(AbstractModel):
    """UpdateKeyDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class VerifyByAsymmetricKeyRequest(AbstractModel):
    """VerifyByAsymmetricKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 密钥的唯一标识
        :type KeyId: str
        :param _SignatureValue: 签名值，通过调用KMS签名接口生成
        :type SignatureValue: str
        :param _Message: 消息原文或消息摘要。如果提供的是消息原文，则消息原文的长度（Base64编码前的长度）不超过4096字节。如果提供的是消息摘要，则消息摘要长度（Base64编码前的长度）必须等于32字节
        :type Message: str
        :param _Algorithm: 签名算法，支持的算法：SM2DSA，ECC_P256_R1，RSA_PSS_SHA_256，RSA_PKCS1_SHA_256 等。更多支持的算法可通过 ListAlgorithms 接口进行查询。
        :type Algorithm: str
        :param _MessageType: 消息类型：RAW，DIGEST，如果不传，默认为RAW，表示消息原文。
        :type MessageType: str
        """
        self._KeyId = None
        self._SignatureValue = None
        self._Message = None
        self._Algorithm = None
        self._MessageType = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def SignatureValue(self):
        return self._SignatureValue

    @SignatureValue.setter
    def SignatureValue(self, SignatureValue):
        self._SignatureValue = SignatureValue

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def MessageType(self):
        return self._MessageType

    @MessageType.setter
    def MessageType(self, MessageType):
        self._MessageType = MessageType


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._SignatureValue = params.get("SignatureValue")
        self._Message = params.get("Message")
        self._Algorithm = params.get("Algorithm")
        self._MessageType = params.get("MessageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyByAsymmetricKeyResponse(AbstractModel):
    """VerifyByAsymmetricKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignatureValid: 签名是否有效。true：签名有效，false：签名无效。
        :type SignatureValid: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignatureValid = None
        self._RequestId = None

    @property
    def SignatureValid(self):
        return self._SignatureValid

    @SignatureValid.setter
    def SignatureValid(self, SignatureValid):
        self._SignatureValid = SignatureValid

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignatureValid = params.get("SignatureValid")
        self._RequestId = params.get("RequestId")


class WhiteboxKeyInfo(AbstractModel):
    """白盒密钥信息

    """

    def __init__(self):
        r"""
        :param _KeyId: 白盒密钥的全局唯一标识符
        :type KeyId: str
        :param _Alias: 作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字母数字 - _ 的组合，首字符必须为字母或者数字. 不可重复
        :type Alias: str
        :param _CreatorUin: 创建者
        :type CreatorUin: int
        :param _Description: 密钥的描述信息
        :type Description: str
        :param _CreateTime: 密钥创建时间，Unix时间戳
        :type CreateTime: int
        :param _Status: 白盒密钥的状态， 取值为：Enabled | Disabled
        :type Status: str
        :param _OwnerUin: 创建者
        :type OwnerUin: int
        :param _Algorithm: 密钥所用的算法类型
        :type Algorithm: str
        :param _EncryptKey: 白盒加密密钥，base64编码
        :type EncryptKey: str
        :param _DecryptKey: 白盒解密密钥，base64编码
        :type DecryptKey: str
        :param _ResourceId: 资源ID，格式：creatorUin/$creatorUin/$keyId
        :type ResourceId: str
        :param _DeviceFingerprintBind: 是否有设备指纹与当前密钥绑定
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceFingerprintBind: bool
        """
        self._KeyId = None
        self._Alias = None
        self._CreatorUin = None
        self._Description = None
        self._CreateTime = None
        self._Status = None
        self._OwnerUin = None
        self._Algorithm = None
        self._EncryptKey = None
        self._DecryptKey = None
        self._ResourceId = None
        self._DeviceFingerprintBind = None

    @property
    def KeyId(self):
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def CreatorUin(self):
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def EncryptKey(self):
        return self._EncryptKey

    @EncryptKey.setter
    def EncryptKey(self, EncryptKey):
        self._EncryptKey = EncryptKey

    @property
    def DecryptKey(self):
        return self._DecryptKey

    @DecryptKey.setter
    def DecryptKey(self, DecryptKey):
        self._DecryptKey = DecryptKey

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def DeviceFingerprintBind(self):
        return self._DeviceFingerprintBind

    @DeviceFingerprintBind.setter
    def DeviceFingerprintBind(self, DeviceFingerprintBind):
        self._DeviceFingerprintBind = DeviceFingerprintBind


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        self._Alias = params.get("Alias")
        self._CreatorUin = params.get("CreatorUin")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._Status = params.get("Status")
        self._OwnerUin = params.get("OwnerUin")
        self._Algorithm = params.get("Algorithm")
        self._EncryptKey = params.get("EncryptKey")
        self._DecryptKey = params.get("DecryptKey")
        self._ResourceId = params.get("ResourceId")
        self._DeviceFingerprintBind = params.get("DeviceFingerprintBind")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        