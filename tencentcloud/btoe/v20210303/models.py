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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CreateAudioDepositRequest(AbstractModel):
    """CreateAudioDeposit请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param FileName: 对应数据Base64文件名称
        :type FileName: str
        :param EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param FileUrl: 资源访问链接 与fileContent必须二选一
        :type FileUrl: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.FileName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.FileContent = None
        self.FileUrl = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.FileName = params.get("FileName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateAudioDepositResponse(AbstractModel):
    """CreateAudioDeposit返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDataDepositRequest(AbstractModel):
    """CreateDataDeposit请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceInfo: 业务数据明文(json格式字符串)，最大256kb
        :type EvidenceInfo: str
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceInfo = None
        self.EvidenceName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceInfo = params.get("EvidenceInfo")
        self.EvidenceName = params.get("EvidenceName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDataDepositResponse(AbstractModel):
    """CreateDataDeposit返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDocDepositRequest(AbstractModel):
    """CreateDocDeposit请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param FileName: 对应数据Base64文件名称
        :type FileName: str
        :param EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param FileUrl: 资源访问链接 与fileContent必须二选一
        :type FileUrl: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.FileName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.FileContent = None
        self.FileUrl = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.FileName = params.get("FileName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDocDepositResponse(AbstractModel):
    """CreateDocDeposit返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateHashDepositNoCertRequest(AbstractModel):
    """CreateHashDepositNoCert请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceInfo: 业务扩展信息
        :type EvidenceInfo: str
        """
        self.EvidenceHash = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceInfo = None


    def _deserialize(self, params):
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceInfo = params.get("EvidenceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateHashDepositNoCertResponse(AbstractModel):
    """CreateHashDepositNoCert返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 存证编码
        :type EvidenceId: str
        :param EvidenceTime: 上链时间
        :type EvidenceTime: str
        :param EvidenceTxHash: 区块链交易哈希
        :type EvidenceTxHash: str
        :param BlockchainHeight: 区块高度
        :type BlockchainHeight: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.EvidenceTime = None
        self.EvidenceTxHash = None
        self.BlockchainHeight = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.EvidenceTime = params.get("EvidenceTime")
        self.EvidenceTxHash = params.get("EvidenceTxHash")
        self.BlockchainHeight = params.get("BlockchainHeight")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateHashDepositNoSealRequest(AbstractModel):
    """CreateHashDepositNoSeal请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceInfo: 业务扩展信息
        :type EvidenceInfo: str
        """
        self.EvidenceHash = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceInfo = None


    def _deserialize(self, params):
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceInfo = params.get("EvidenceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateHashDepositNoSealResponse(AbstractModel):
    """CreateHashDepositNoSeal返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 存证编码
        :type EvidenceId: str
        :param EvidenceTime: 上链时间
        :type EvidenceTime: str
        :param EvidenceTxHash: 区块链交易哈希
        :type EvidenceTxHash: str
        :param BlockchainHeight: 区块高度
        :type BlockchainHeight: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.EvidenceTime = None
        self.EvidenceTxHash = None
        self.BlockchainHeight = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.EvidenceTime = params.get("EvidenceTime")
        self.EvidenceTxHash = params.get("EvidenceTxHash")
        self.BlockchainHeight = params.get("BlockchainHeight")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateHashDepositRequest(AbstractModel):
    """CreateHashDeposit请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateHashDepositResponse(AbstractModel):
    """CreateHashDeposit返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 存证编码
        :type EvidenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateImageDepositRequest(AbstractModel):
    """CreateImageDeposit请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param FileName: 对应数据Base64文件名称 test.png
        :type FileName: str
        :param EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param FileUrl: 资源访问链接 与fileContent必须二选一
        :type FileUrl: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.FileName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.FileContent = None
        self.FileUrl = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.FileName = params.get("FileName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateImageDepositResponse(AbstractModel):
    """CreateImageDeposit返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateVideoDepositRequest(AbstractModel):
    """CreateVideoDeposit请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param FileName: 对应数据Base64文件名称
        :type FileName: str
        :param EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param FileUrl: 资源访问链接 与fileContent必须二选一
        :type FileUrl: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.FileName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.FileContent = None
        self.FileUrl = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.FileName = params.get("FileName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.FileContent = params.get("FileContent")
        self.FileUrl = params.get("FileUrl")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateVideoDepositResponse(AbstractModel):
    """CreateVideoDeposit返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateWebpageDepositRequest(AbstractModel):
    """CreateWebpageDeposit请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param EvidenceUrl: 网页链接
        :type EvidenceUrl: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.EvidenceUrl = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.EvidenceUrl = params.get("EvidenceUrl")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateWebpageDepositResponse(AbstractModel):
    """CreateWebpageDeposit返回参数结构体

    """

    def __init__(self):
        """
        :param BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BusinessId = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BusinessId = params.get("BusinessId")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetDepositCertRequest(AbstractModel):
    """GetDepositCert请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self.EvidenceId = None


    def _deserialize(self, params):
        self.EvidenceId = params.get("EvidenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetDepositCertResponse(AbstractModel):
    """GetDepositCert返回参数结构体

    """

    def __init__(self):
        """
        :param EvidenceId: 存证编码
        :type EvidenceId: str
        :param EvidenceCert: 存证证书文件临时链接
        :type EvidenceCert: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EvidenceId = None
        self.EvidenceCert = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EvidenceId = params.get("EvidenceId")
        self.EvidenceCert = params.get("EvidenceCert")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetDepositFileRequest(AbstractModel):
    """GetDepositFile请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self.EvidenceId = None


    def _deserialize(self, params):
        self.EvidenceId = params.get("EvidenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetDepositFileResponse(AbstractModel):
    """GetDepositFile返回参数结构体

    """

    def __init__(self):
        """
        :param EvidenceId: 存证编号
        :type EvidenceId: str
        :param EvidenceFile: 存证文件临时链接
        :type EvidenceFile: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EvidenceId = None
        self.EvidenceFile = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EvidenceId = params.get("EvidenceId")
        self.EvidenceFile = params.get("EvidenceFile")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetDepositInfoRequest(AbstractModel):
    """GetDepositInfo请求参数结构体

    """

    def __init__(self):
        """
        :param EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self.EvidenceId = None


    def _deserialize(self, params):
        self.EvidenceId = params.get("EvidenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetDepositInfoResponse(AbstractModel):
    """GetDepositInfo返回参数结构体

    """

    def __init__(self):
        """
        :param EvidenceId: 存证编号
        :type EvidenceId: str
        :param EvidenceTime: 上链时间
        :type EvidenceTime: str
        :param EvidenceTxHash: 区块链交易哈希
        :type EvidenceTxHash: str
        :param BlockchainHeight: 区块高度
        :type BlockchainHeight: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EvidenceId = None
        self.EvidenceTime = None
        self.EvidenceTxHash = None
        self.BlockchainHeight = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EvidenceId = params.get("EvidenceId")
        self.EvidenceTime = params.get("EvidenceTime")
        self.EvidenceTxHash = params.get("EvidenceTxHash")
        self.BlockchainHeight = params.get("BlockchainHeight")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        