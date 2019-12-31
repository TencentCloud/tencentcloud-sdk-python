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


class CreateSecretRequest(AbstractModel):
    """CreateSecret请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称，同一region内不可重复，最长128字节，使用字母、数字或者 - _ 的组合，第一个字符必须为字母或者数字。
        :type SecretName: str
        :param VersionId: 凭据版本，查询凭据信息时需要根据SecretName 和 VersionId进行查询，最长64 字节，使用字母、数字或者 - _ . 的组合并且以字母或数字开头。
        :type VersionId: str
        :param Description: 描述信息，用于详细描述用途等，最大支持2048字节。
        :type Description: str
        :param KmsKeyId: 指定对凭据进行加密的KMS CMK。如果为空则表示使用Secrets Manager为您默认创建的CMK进行加密。您也可以指定在同region 下自行创建的KMS CMK进行加密。
        :type KmsKeyId: str
        :param SecretBinary: 二进制凭据信息base64编码后的明文。SecretBinary 和 SecretString 必须且只能设置一个，最大支持4096字节。
        :type SecretBinary: str
        :param SecretString: 文本类型凭据信息明文（不需要进行base64编码）。SecretBinary 和 SecretString 必须且只能设置一个，，最大支持4096字节。
        :type SecretString: str
        """
        self.SecretName = None
        self.VersionId = None
        self.Description = None
        self.KmsKeyId = None
        self.SecretBinary = None
        self.SecretString = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")


class CreateSecretResponse(AbstractModel):
    """CreateSecret返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 新创建的凭据名称。
        :type SecretName: str
        :param VersionId: 新创建的凭据版本。
        :type VersionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class DeleteSecretRequest(AbstractModel):
    """DeleteSecret请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定需要删除的凭据名称。
        :type SecretName: str
        :param RecoveryWindowInDays: 指定计划删除日期，单位（天），0（默认）表示立即删除， 1-30 表示预留的天数，超出该日期之后彻底删除。
        :type RecoveryWindowInDays: int
        """
        self.SecretName = None
        self.RecoveryWindowInDays = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RecoveryWindowInDays = params.get("RecoveryWindowInDays")


class DeleteSecretResponse(AbstractModel):
    """DeleteSecret返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定删除的凭据名称。
        :type SecretName: str
        :param DeleteTime: 凭据删除的日期，unix时间戳。
        :type DeleteTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.DeleteTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.DeleteTime = params.get("DeleteTime")
        self.RequestId = params.get("RequestId")


class DeleteSecretVersionRequest(AbstractModel):
    """DeleteSecretVersion请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定凭据名称。
        :type SecretName: str
        :param VersionId: 指定该名称下需要删除的凭据的版本号。
        :type VersionId: str
        """
        self.SecretName = None
        self.VersionId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")


class DeleteSecretVersionResponse(AbstractModel):
    """DeleteSecretVersion返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        :param VersionId: 凭据版本号。
        :type VersionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class DescribeSecretRequest(AbstractModel):
    """DescribeSecret请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定需要获取凭据详细信息的凭据名称。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class DescribeSecretResponse(AbstractModel):
    """DescribeSecret返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        :param Description: 凭据描述信息。
        :type Description: str
        :param KmsKeyId: 用于加密的KMS CMK ID。
        :type KmsKeyId: str
        :param CreateUin: 创建者UIN。
        :type CreateUin: int
        :param Status: 凭据状态：Enabled、Disabled、PendingDelete
        :type Status: str
        :param DeleteTime: 删除日期，uinx 时间戳，非计划删除状态的凭据为0。
        :type DeleteTime: int
        :param CreateTime: 创建日期。
        :type CreateTime: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.Description = None
        self.KmsKeyId = None
        self.CreateUin = None
        self.Status = None
        self.DeleteTime = None
        self.CreateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.CreateUin = params.get("CreateUin")
        self.Status = params.get("Status")
        self.DeleteTime = params.get("DeleteTime")
        self.CreateTime = params.get("CreateTime")
        self.RequestId = params.get("RequestId")


class DisableSecretRequest(AbstractModel):
    """DisableSecret请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定停用的凭据名称。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class DisableSecretResponse(AbstractModel):
    """DisableSecret返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 停用的凭据名称。
        :type SecretName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class EnableSecretRequest(AbstractModel):
    """EnableSecret请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定启用凭据的名称。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class EnableSecretResponse(AbstractModel):
    """EnableSecret返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 启用的凭据名称。
        :type SecretName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions请求参数结构体

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions返回参数结构体

    """

    def __init__(self):
        """
        :param Regions: region列表。
        :type Regions: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Regions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Regions = params.get("Regions")
        self.RequestId = params.get("RequestId")


class GetSecretValueRequest(AbstractModel):
    """GetSecretValue请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定凭据的名称。
        :type SecretName: str
        :param VersionId: 指定对应凭据的版本号。
        :type VersionId: str
        """
        self.SecretName = None
        self.VersionId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")


class GetSecretValueResponse(AbstractModel):
    """GetSecretValue返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据的名称。
        :type SecretName: str
        :param VersionId: 该凭据对应的版本号。
        :type VersionId: str
        :param SecretBinary: 在创建凭据(CreateSecret)时，如果指定的是二进制数据，则该字段为返回结果，并且使用base64进行编码，应用方需要进行base64解码后获取原始数据。SecretBinary和SecretString只有一个不为空。
        :type SecretBinary: str
        :param SecretString: 在创建凭据(CreateSecret)时，如果指定的是普通文本数据，则该字段为返回结果。SecretBinary和SecretString只有一个不为空。
        :type SecretString: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")
        self.RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus请求参数结构体

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceEnabled: true表示服务已开通，false 表示服务尚未开通。
        :type ServiceEnabled: bool
        :param InvalidType: 服务不可用类型： 0-未购买，1-正常， 2-欠费停服， 3-资源释放。
        :type InvalidType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceEnabled = None
        self.InvalidType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceEnabled = params.get("ServiceEnabled")
        self.InvalidType = params.get("InvalidType")
        self.RequestId = params.get("RequestId")


class ListSecretVersionIdsRequest(AbstractModel):
    """ListSecretVersionIds请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class ListSecretVersionIdsResponse(AbstractModel):
    """ListSecretVersionIds返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        :param Versions: VersionId列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Versions: list of VersionInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.Versions = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        if params.get("Versions") is not None:
            self.Versions = []
            for item in params.get("Versions"):
                obj = VersionInfo()
                obj._deserialize(item)
                self.Versions.append(obj)
        self.RequestId = params.get("RequestId")


class ListSecretsRequest(AbstractModel):
    """ListSecrets请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 查询列表的起始位置，以0开始，不设置默认为0。
        :type Offset: int
        :param Limit: 单次查询返回的最大数量，0或不设置则使用默认值 20。
        :type Limit: int
        :param OrderType: 根据创建时间的排序方式，0或者不设置则使用降序排序， 1 表示升序排序。
        :type OrderType: int
        :param State: 根据凭据状态进行过滤，默认为0表示查询全部，1 表示查询Enabed 凭据列表，2表示查询Disabled 凭据列表， 3 表示查询PendingDelete 凭据列表。
        :type State: int
        :param SearchSecretName: 根据凭据名称进行过滤，为空表示不过滤。
        :type SearchSecretName: str
        """
        self.Offset = None
        self.Limit = None
        self.OrderType = None
        self.State = None
        self.SearchSecretName = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderType = params.get("OrderType")
        self.State = params.get("State")
        self.SearchSecretName = params.get("SearchSecretName")


class ListSecretsResponse(AbstractModel):
    """ListSecrets返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 根据State和SearchSecretName 筛选的凭据总数。
        :type TotalCount: int
        :param SecretMetadatas: 返回凭据信息列表。
        :type SecretMetadatas: list of SecretMetadata
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SecretMetadatas = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SecretMetadatas") is not None:
            self.SecretMetadatas = []
            for item in params.get("SecretMetadatas"):
                obj = SecretMetadata()
                obj._deserialize(item)
                self.SecretMetadatas.append(obj)
        self.RequestId = params.get("RequestId")


class PutSecretValueRequest(AbstractModel):
    """PutSecretValue请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定需要增加版本的凭据名称。
        :type SecretName: str
        :param VersionId: 指定新增加的版本号，最长64 字节，使用字母、数字或者 - _ . 的组合并且以字母或数字开头。
        :type VersionId: str
        :param SecretBinary: 二进制凭据信息，使用base64编码。SecretBinary 和 SecretString 必须且只能设置一个。
        :type SecretBinary: str
        :param SecretString: 文本类型凭据信息明文（不需要进行base64编码），SecretBinary 和 SecretString 必须且只能设置一个。
        :type SecretString: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")


class PutSecretValueResponse(AbstractModel):
    """PutSecretValue返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        :param VersionId: 新增加的版本号。
        :type VersionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class RestoreSecretRequest(AbstractModel):
    """RestoreSecret请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定需要恢复的凭据名称。
        :type SecretName: str
        """
        self.SecretName = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")


class RestoreSecretResponse(AbstractModel):
    """RestoreSecret返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class SecretMetadata(AbstractModel):
    """凭据的基础信息

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        :param Description: 凭据的描述信息。
        :type Description: str
        :param KmsKeyId: 用于加密凭据的KMS KeyId。
        :type KmsKeyId: str
        :param CreateUin: 创建者UIN。
        :type CreateUin: int
        :param Status: 凭据状态：Enabled、Disabled、PendingDelete
        :type Status: str
        :param DeleteTime: 凭据删除日期，对于status为PendingDelete 的有效，unix时间戳。
        :type DeleteTime: int
        :param CreateTime: 凭据创建时间，unix时间戳。
        :type CreateTime: int
        :param KmsKeyType: 用于加密凭据的KMS CMK类型，DEFAULT 表示SecretsManager 创建的默认密钥， CUSTOMER 表示用户指定的密钥。
        :type KmsKeyType: str
        """
        self.SecretName = None
        self.Description = None
        self.KmsKeyId = None
        self.CreateUin = None
        self.Status = None
        self.DeleteTime = None
        self.CreateTime = None
        self.KmsKeyType = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")
        self.KmsKeyId = params.get("KmsKeyId")
        self.CreateUin = params.get("CreateUin")
        self.Status = params.get("Status")
        self.DeleteTime = params.get("DeleteTime")
        self.CreateTime = params.get("CreateTime")
        self.KmsKeyType = params.get("KmsKeyType")


class UpdateDescriptionRequest(AbstractModel):
    """UpdateDescription请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定需要更新描述信息的凭据名。
        :type SecretName: str
        :param Description: 新的描述信息，最大长度2048个字节。
        :type Description: str
        """
        self.SecretName = None
        self.Description = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.Description = params.get("Description")


class UpdateDescriptionResponse(AbstractModel):
    """UpdateDescription返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.RequestId = params.get("RequestId")


class UpdateSecretRequest(AbstractModel):
    """UpdateSecret请求参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 指定需要更新凭据内容的名称。
        :type SecretName: str
        :param VersionId: 指定需要更新凭据内容的版本号。
        :type VersionId: str
        :param SecretBinary: 新的凭据内容为二进制的场景使用该字段，并使用base64进行编码。SecretBinary 和 SecretString 只能一个不为空。
        :type SecretBinary: str
        :param SecretString: 新的凭据内容为文本的场景使用该字段，不需要base64编码。SecretBinary 和 SecretString 只能一个不为空。
        :type SecretString: str
        """
        self.SecretName = None
        self.VersionId = None
        self.SecretBinary = None
        self.SecretString = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.SecretBinary = params.get("SecretBinary")
        self.SecretString = params.get("SecretString")


class UpdateSecretResponse(AbstractModel):
    """UpdateSecret返回参数结构体

    """

    def __init__(self):
        """
        :param SecretName: 凭据名称。
        :type SecretName: str
        :param VersionId: 凭据版本号。
        :type VersionId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecretName = None
        self.VersionId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.VersionId = params.get("VersionId")
        self.RequestId = params.get("RequestId")


class VersionInfo(AbstractModel):
    """凭据版本号列表信息

    """

    def __init__(self):
        """
        :param VersionId: 版本号。
        :type VersionId: str
        :param CreateTime: 创建时间，unix时间戳。
        :type CreateTime: int
        """
        self.VersionId = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VersionId = params.get("VersionId")
        self.CreateTime = params.get("CreateTime")