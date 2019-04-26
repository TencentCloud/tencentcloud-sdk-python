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

from tencentcloud.common.abstract_model import AbstractModel


class CreateKeyRequest(AbstractModel):
    """CreateKey请求参数结构体

    """

    def __init__(self):
        """
        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名， 不可为空，1-60个字符或数字的组合
        :type Alias: str
        :param Description: CMK 的描述，最大1024字节
        :type Description: str
        :param KeyUsage: 指定key的用途。目前，仅支持"ENCRYPT_DECRYPT"，默认为  "ENCRYPT_DECRYPT"，即key用于加密和解密
        :type KeyUsage: str
        :param Type: 指定key类型，1为当前地域默认类型，默认为1，且当前只支持该类型
        :type Type: int
        """
        self.Alias = None
        self.Description = None
        self.KeyUsage = None
        self.Type = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.Description = params.get("Description")
        self.KeyUsage = params.get("KeyUsage")
        self.Type = params.get("Type")


class CreateKeyResponse(AbstractModel):
    """CreateKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识符
        :type KeyId: str
        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名
        :type Alias: str
        :param CreateTime: 密钥创建时间，unix时间戳
        :type CreateTime: int
        :param Description: CMK的描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param KeyState: CMK的状态
        :type KeyState: str
        :param KeyUsage: CMK的用途
        :type KeyUsage: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.Alias = None
        self.CreateTime = None
        self.Description = None
        self.KeyState = None
        self.KeyUsage = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Alias = params.get("Alias")
        self.CreateTime = params.get("CreateTime")
        self.Description = params.get("Description")
        self.KeyState = params.get("KeyState")
        self.KeyUsage = params.get("KeyUsage")
        self.RequestId = params.get("RequestId")


class DecryptRequest(AbstractModel):
    """Decrypt请求参数结构体

    """

    def __init__(self):
        """
        :param CiphertextBlob: 被加密的密文数据
        :type CiphertextBlob: str
        :param EncryptionContext: key/value对的json字符串，如果Encrypt指定了该参数，则在调用Decrypt API时需要提供同样的参数，最大支持1024字符
        :type EncryptionContext: str
        """
        self.CiphertextBlob = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.EncryptionContext = params.get("EncryptionContext")


class DecryptResponse(AbstractModel):
    """Decrypt返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识
        :type KeyId: str
        :param Plaintext: 解密后的明文。该字段是base64编码的，为了得到原始明文，调用方需要进行base64解码
        :type Plaintext: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.RequestId = params.get("RequestId")


class DescribeKeyRequest(AbstractModel):
    """DescribeKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK全局唯一标识符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DescribeKeyResponse(AbstractModel):
    """DescribeKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyMetadata: 密钥属性信息
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyMetadata: :class:`tencentcloud.kms.v20190118.models.KeyMetadata`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param KeyIds: 查询CMK的ID列表，批量查询一次最多支持100个KeyId
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class DescribeKeysResponse(AbstractModel):
    """DescribeKeys返回参数结构体

    """

    def __init__(self):
        """
        :param KeyMetadatas: 返回的属性信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DisableKeyRequest(AbstractModel):
    """DisableKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DisableKeyResponse(AbstractModel):
    """DisableKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeyRotationRequest(AbstractModel):
    """DisableKeyRotation请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class DisableKeyRotationResponse(AbstractModel):
    """DisableKeyRotation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableKeysRequest(AbstractModel):
    """DisableKeys请求参数结构体

    """

    def __init__(self):
        """
        :param KeyIds: 需要批量禁用的CMK Id 列表，CMK数量最大支持100
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class DisableKeysResponse(AbstractModel):
    """DisableKeys返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRequest(AbstractModel):
    """EnableKey请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class EnableKeyResponse(AbstractModel):
    """EnableKey返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeyRotationRequest(AbstractModel):
    """EnableKeyRotation请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class EnableKeyRotationResponse(AbstractModel):
    """EnableKeyRotation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableKeysRequest(AbstractModel):
    """EnableKeys请求参数结构体

    """

    def __init__(self):
        """
        :param KeyIds: 需要批量启用的CMK Id 列表， CMK数量最大支持100
        :type KeyIds: list of str
        """
        self.KeyIds = None


    def _deserialize(self, params):
        self.KeyIds = params.get("KeyIds")


class EnableKeysResponse(AbstractModel):
    """EnableKeys返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EncryptRequest(AbstractModel):
    """Encrypt请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: 调用CreateKey生成的CMK全局唯一标识符
        :type KeyId: str
        :param Plaintext: 被加密的明文数据，该字段必须使用base64编码，原文最大长度支持4K
        :type Plaintext: str
        :param EncryptionContext: key/value对的json字符串，如果指定了该参数，则在调用Decrypt API时需要提供同样的参数，最大支持1024个字符
        :type EncryptionContext: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.EncryptionContext = params.get("EncryptionContext")


class EncryptResponse(AbstractModel):
    """Encrypt返回参数结构体

    """

    def __init__(self):
        """
        :param CiphertextBlob: 加密后的密文
        :type CiphertextBlob: str
        :param KeyId: 加密使用的CMK的全局唯一标识
        :type KeyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param KeyId: CMK全局唯一标识符
        :type KeyId: str
        :param KeySpec: 指定生成Datakey的加密算法以及Datakey大小，AES_128或者AES_256。默认为AES_256
        :type KeySpec: str
        :param NumberOfBytes: 生成的DataKey的长度，同时指定NumberOfBytes和KeySpec时，以NumberOfBytes为准。最小值为1， 最大值为1024
        :type NumberOfBytes: int
        :param EncryptionContext: key/value对的json字符串，如果使用该字段，则返回的DataKey在解密时需要填入相同的字符串
        :type EncryptionContext: str
        """
        self.KeyId = None
        self.KeySpec = None
        self.NumberOfBytes = None
        self.EncryptionContext = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.KeySpec = params.get("KeySpec")
        self.NumberOfBytes = params.get("NumberOfBytes")
        self.EncryptionContext = params.get("EncryptionContext")


class GenerateDataKeyResponse(AbstractModel):
    """GenerateDataKey返回参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识
        :type KeyId: str
        :param Plaintext: 生成的DataKey的明文，该明文使用base64编码，用户需要使用base64解码得到明文
        :type Plaintext: str
        :param CiphertextBlob: DataKey加密后的密文，用户需要自行保存密文
        :type CiphertextBlob: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyId = None
        self.Plaintext = None
        self.CiphertextBlob = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")
        self.Plaintext = params.get("Plaintext")
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.RequestId = params.get("RequestId")


class GetKeyRotationStatusRequest(AbstractModel):
    """GetKeyRotationStatus请求参数结构体

    """

    def __init__(self):
        """
        :param KeyId: CMK唯一标识符
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class GetKeyRotationStatusResponse(AbstractModel):
    """GetKeyRotationStatus返回参数结构体

    """

    def __init__(self):
        """
        :param KeyRotationEnabled: 密钥轮换是否开启
        :type KeyRotationEnabled: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeyRotationEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.KeyRotationEnabled = params.get("KeyRotationEnabled")
        self.RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus请求参数结构体

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceEnabled: KMS服务是否开通， true 表示已开通
        :type ServiceEnabled: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceEnabled = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.RequestId = params.get("RequestId")


class Key(AbstractModel):
    """返回CMK列表信息

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识。
        :type KeyId: str
        """
        self.KeyId = None


    def _deserialize(self, params):
        self.KeyId = params.get("KeyId")


class KeyMetadata(AbstractModel):
    """CMK属性信息

    """

    def __init__(self):
        """
        :param KeyId: CMK的全局唯一标识
        :type KeyId: str
        :param Alias: 作为密钥更容易辨识，更容易被人看懂的别名
        :type Alias: str
        :param CreateTime: 密钥创建时间
        :type CreateTime: int
        :param Description: CMK的描述
        :type Description: str
        :param KeyState: CMK的状态， Enabled 或者 Disabled 或者 Deleted
        :type KeyState: str
        :param KeyUsage: CMK用途，当前是 ENCRYPT_DECRYPT
        :type KeyUsage: str
        :param Type: CMK类型，当前为 1 普通类型
        :type Type: int
        :param CreatorUin: 创建者
        :type CreatorUin: int
        :param KeyRotationEnabled: 是否开启了密钥轮换功能
        :type KeyRotationEnabled: bool
        :param Owner: CMK的创建者，用户创建的为 user，授权各云产品自动创建的为对应的产品名
        :type Owner: str
        :param NextRotateTime: 在密钥轮换开启状态下，下次轮换的时间
        :type NextRotateTime: int
        """
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


class ListKeyDetailRequest(AbstractModel):
    """ListKeyDetail请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0
        :type Offset: int
        :param Limit: 含义跟 SQL 查询的 Limit 一致，表示本次获最多获取 Limit 个元素。缺省值为10，最大值为200
        :type Limit: int
        :param Role: 根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk
        :type Role: int
        :param OrderType: 根据CMK创建时间排序， 0 表示按照降序排序，1表示按照升序排序
        :type OrderType: int
        :param KeyState: 根据CMK状态筛选， 0表示全部CMK， 1 表示仅查询Enabled CMK， 2 表示仅查询Disabled CMK
        :type KeyState: int
        :param SearchKeyAlias: 根据KeyId或者Alias进行模糊匹配查询
        :type SearchKeyAlias: str
        """
        self.Offset = None
        self.Limit = None
        self.Role = None
        self.OrderType = None
        self.KeyState = None
        self.SearchKeyAlias = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")
        self.OrderType = params.get("OrderType")
        self.KeyState = params.get("KeyState")
        self.SearchKeyAlias = params.get("SearchKeyAlias")


class ListKeyDetailResponse(AbstractModel):
    """ListKeyDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: CMK的总数量
        :type TotalCount: int
        :param KeyMetadatas: 返回的属性信息列表，此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyMetadatas: list of KeyMetadata
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param Offset: 含义跟 SQL 查询的 Offset 一致，表示本次获取从按一定顺序排列数组的第 Offset 个元素开始，缺省为0
        :type Offset: int
        :param Limit: 含义跟 SQL 查询的 Limit 一致，表示本次获最多获取 Limit 个元素。缺省值为10，最大值为200
        :type Limit: int
        :param Role: 根据创建者角色筛选，默认 0 表示用户自己创建的cmk， 1 表示授权其它云产品自动创建的cmk
        :type Role: int
        """
        self.Offset = None
        self.Limit = None
        self.Role = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Role = params.get("Role")


class ListKeysResponse(AbstractModel):
    """ListKeys返回参数结构体

    """

    def __init__(self):
        """
        :param Keys: CMK列表数组
注意：此字段可能返回 null，表示取不到有效值。
        :type Keys: list of Key
        :param TotalCount: CMK的总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class ReEncryptRequest(AbstractModel):
    """ReEncrypt请求参数结构体

    """

    def __init__(self):
        """
        :param CiphertextBlob: 需要重新加密的密文
        :type CiphertextBlob: str
        :param DestinationKeyId: 重新加密使用的CMK，如果为空，则使用密文原有的CMK重新加密（若密钥没有轮换则密文不会刷新）
        :type DestinationKeyId: str
        :param SourceEncryptionContext: CiphertextBlob 密文加密时使用的key/value对的json字符串。如果加密时未使用，则为空
        :type SourceEncryptionContext: str
        :param DestinationEncryptionContext: 重新加密使用的key/value对的json字符串，如果使用该字段，则返回的新密文在解密时需要填入相同的字符串
        :type DestinationEncryptionContext: str
        """
        self.CiphertextBlob = None
        self.DestinationKeyId = None
        self.SourceEncryptionContext = None
        self.DestinationEncryptionContext = None


    def _deserialize(self, params):
        self.CiphertextBlob = params.get("CiphertextBlob")
        self.DestinationKeyId = params.get("DestinationKeyId")
        self.SourceEncryptionContext = params.get("SourceEncryptionContext")
        self.DestinationEncryptionContext = params.get("DestinationEncryptionContext")


class ReEncryptResponse(AbstractModel):
    """ReEncrypt返回参数结构体

    """

    def __init__(self):
        """
        :param CiphertextBlob: 重新加密后的密文
        :type CiphertextBlob: str
        :param KeyId: 重新加密使用的CMK
        :type KeyId: str
        :param SourceKeyId: 重新加密前密文使用的CMK
        :type SourceKeyId: str
        :param ReEncrypted: true表示密文已经重新加密。同一个CMK进行重加密，在密钥没有发生轮换的情况下不会进行实际重新加密操作，返回原密文
        :type ReEncrypted: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class UpdateAliasRequest(AbstractModel):
    """UpdateAlias请求参数结构体

    """

    def __init__(self):
        """
        :param Alias: 新的别名，1-64个字符或数字的组合
        :type Alias: str
        :param KeyId: CMK的全局唯一标识符
        :type KeyId: str
        """
        self.Alias = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Alias = params.get("Alias")
        self.KeyId = params.get("KeyId")


class UpdateAliasResponse(AbstractModel):
    """UpdateAlias返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateKeyDescriptionRequest(AbstractModel):
    """UpdateKeyDescription请求参数结构体

    """

    def __init__(self):
        """
        :param Description: 新的描述信息，最大支持1024字节
        :type Description: str
        :param KeyId: 需要修改描述信息的的CMK ID
        :type KeyId: str
        """
        self.Description = None
        self.KeyId = None


    def _deserialize(self, params):
        self.Description = params.get("Description")
        self.KeyId = params.get("KeyId")


class UpdateKeyDescriptionResponse(AbstractModel):
    """UpdateKeyDescription返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")