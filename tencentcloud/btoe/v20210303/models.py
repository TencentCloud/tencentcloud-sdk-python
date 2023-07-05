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


class CreateAudioDepositRequest(AbstractModel):
    """CreateAudioDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _FileName: 对应数据Base64文件名称
        :type FileName: str
        :param _EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param _FileUrl: 资源访问链接 与fileContent必须二选一
        :type FileUrl: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._FileName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._FileContent = None
        self._FileUrl = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def EvidenceHash(self):
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._FileName = params.get("FileName")
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._FileContent = params.get("FileContent")
        self._FileUrl = params.get("FileUrl")
        self._HashType = params.get("HashType")
        self._EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAudioDepositResponse(AbstractModel):
    """CreateAudioDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateDataDepositRequest(AbstractModel):
    """CreateDataDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceInfo: 业务数据明文(json格式字符串)，最大256kb
        :type EvidenceInfo: str
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceInfo = None
        self._EvidenceName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceInfo(self):
        return self._EvidenceInfo

    @EvidenceInfo.setter
    def EvidenceInfo(self, EvidenceInfo):
        self._EvidenceInfo = EvidenceInfo

    @property
    def EvidenceName(self):
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def EvidenceHash(self):
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceInfo = params.get("EvidenceInfo")
        self._EvidenceName = params.get("EvidenceName")
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._HashType = params.get("HashType")
        self._EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataDepositResponse(AbstractModel):
    """CreateDataDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateDocDepositRequest(AbstractModel):
    """CreateDocDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _FileName: 对应数据Base64文件名称
        :type FileName: str
        :param _EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param _FileUrl: 资源访问链接 与fileContent必须二选一
        :type FileUrl: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._FileName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._FileContent = None
        self._FileUrl = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def EvidenceHash(self):
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._FileName = params.get("FileName")
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._FileContent = params.get("FileContent")
        self._FileUrl = params.get("FileUrl")
        self._HashType = params.get("HashType")
        self._EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocDepositResponse(AbstractModel):
    """CreateDocDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateHashDepositNoCertRequest(AbstractModel):
    """CreateHashDepositNoCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param _BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceInfo: 业务扩展信息
        :type EvidenceInfo: str
        """
        self._EvidenceHash = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceInfo = None

    @property
    def EvidenceHash(self):
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceInfo(self):
        return self._EvidenceInfo

    @EvidenceInfo.setter
    def EvidenceInfo(self, EvidenceInfo):
        self._EvidenceInfo = EvidenceInfo


    def _deserialize(self, params):
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._HashType = params.get("HashType")
        self._EvidenceInfo = params.get("EvidenceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositNoCertResponse(AbstractModel):
    """CreateHashDepositNoCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        :param _EvidenceTime: 上链时间
        :type EvidenceTime: str
        :param _EvidenceTxHash: 区块链交易哈希
        :type EvidenceTxHash: str
        :param _BlockchainHeight: 区块高度
        :type BlockchainHeight: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._EvidenceTime = None
        self._EvidenceTxHash = None
        self._BlockchainHeight = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def EvidenceTime(self):
        return self._EvidenceTime

    @EvidenceTime.setter
    def EvidenceTime(self, EvidenceTime):
        self._EvidenceTime = EvidenceTime

    @property
    def EvidenceTxHash(self):
        return self._EvidenceTxHash

    @EvidenceTxHash.setter
    def EvidenceTxHash(self, EvidenceTxHash):
        self._EvidenceTxHash = EvidenceTxHash

    @property
    def BlockchainHeight(self):
        return self._BlockchainHeight

    @BlockchainHeight.setter
    def BlockchainHeight(self, BlockchainHeight):
        self._BlockchainHeight = BlockchainHeight

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._EvidenceTime = params.get("EvidenceTime")
        self._EvidenceTxHash = params.get("EvidenceTxHash")
        self._BlockchainHeight = params.get("BlockchainHeight")
        self._RequestId = params.get("RequestId")


class CreateHashDepositNoSealRequest(AbstractModel):
    """CreateHashDepositNoSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param _BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceInfo: 业务扩展信息
        :type EvidenceInfo: str
        """
        self._EvidenceHash = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceInfo = None

    @property
    def EvidenceHash(self):
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceInfo(self):
        return self._EvidenceInfo

    @EvidenceInfo.setter
    def EvidenceInfo(self, EvidenceInfo):
        self._EvidenceInfo = EvidenceInfo


    def _deserialize(self, params):
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._HashType = params.get("HashType")
        self._EvidenceInfo = params.get("EvidenceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositNoSealResponse(AbstractModel):
    """CreateHashDepositNoSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        :param _EvidenceTime: 上链时间
        :type EvidenceTime: str
        :param _EvidenceTxHash: 区块链交易哈希
        :type EvidenceTxHash: str
        :param _BlockchainHeight: 区块高度
        :type BlockchainHeight: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._EvidenceTime = None
        self._EvidenceTxHash = None
        self._BlockchainHeight = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def EvidenceTime(self):
        return self._EvidenceTime

    @EvidenceTime.setter
    def EvidenceTime(self, EvidenceTime):
        self._EvidenceTime = EvidenceTime

    @property
    def EvidenceTxHash(self):
        return self._EvidenceTxHash

    @EvidenceTxHash.setter
    def EvidenceTxHash(self, EvidenceTxHash):
        self._EvidenceTxHash = EvidenceTxHash

    @property
    def BlockchainHeight(self):
        return self._BlockchainHeight

    @BlockchainHeight.setter
    def BlockchainHeight(self, BlockchainHeight):
        self._BlockchainHeight = BlockchainHeight

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._EvidenceTime = params.get("EvidenceTime")
        self._EvidenceTxHash = params.get("EvidenceTxHash")
        self._BlockchainHeight = params.get("BlockchainHeight")
        self._RequestId = params.get("RequestId")


class CreateHashDepositRequest(AbstractModel):
    """CreateHashDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param _BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def EvidenceHash(self):
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._HashType = params.get("HashType")
        self._EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositResponse(AbstractModel):
    """CreateHashDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateImageDepositRequest(AbstractModel):
    """CreateImageDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _FileName: 对应数据Base64文件名称 test.png
        :type FileName: str
        :param _EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param _FileUrl: 资源访问链接 与fileContent必须二选一
        :type FileUrl: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._FileName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._FileContent = None
        self._FileUrl = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def EvidenceHash(self):
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._FileName = params.get("FileName")
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._FileContent = params.get("FileContent")
        self._FileUrl = params.get("FileUrl")
        self._HashType = params.get("HashType")
        self._EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageDepositResponse(AbstractModel):
    """CreateImageDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateVideoDepositRequest(AbstractModel):
    """CreateVideoDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _FileName: 对应数据Base64文件名称
        :type FileName: str
        :param _EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param _FileUrl: 资源访问链接 与fileContent必须二选一
        :type FileUrl: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._FileName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._FileContent = None
        self._FileUrl = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def FileName(self):
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def EvidenceHash(self):
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def FileContent(self):
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileUrl(self):
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._FileName = params.get("FileName")
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._FileContent = params.get("FileContent")
        self._FileUrl = params.get("FileUrl")
        self._HashType = params.get("HashType")
        self._EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoDepositResponse(AbstractModel):
    """CreateVideoDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateWebpageDepositRequest(AbstractModel):
    """CreateWebpageDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _EvidenceUrl: 网页链接
        :type EvidenceUrl: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._EvidenceUrl = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def EvidenceUrl(self):
        return self._EvidenceUrl

    @EvidenceUrl.setter
    def EvidenceUrl(self, EvidenceUrl):
        self._EvidenceUrl = EvidenceUrl

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._EvidenceUrl = params.get("EvidenceUrl")
        self._BusinessId = params.get("BusinessId")
        self._HashType = params.get("HashType")
        self._EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWebpageDepositResponse(AbstractModel):
    """CreateWebpageDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class GetDepositCertRequest(AbstractModel):
    """GetDepositCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self._EvidenceId = None

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDepositCertResponse(AbstractModel):
    """GetDepositCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        :param _EvidenceCert: 存证证书文件临时链接
        :type EvidenceCert: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EvidenceId = None
        self._EvidenceCert = None
        self._RequestId = None

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def EvidenceCert(self):
        return self._EvidenceCert

    @EvidenceCert.setter
    def EvidenceCert(self, EvidenceCert):
        self._EvidenceCert = EvidenceCert

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        self._EvidenceCert = params.get("EvidenceCert")
        self._RequestId = params.get("RequestId")


class GetDepositFileRequest(AbstractModel):
    """GetDepositFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self._EvidenceId = None

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDepositFileResponse(AbstractModel):
    """GetDepositFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编号
        :type EvidenceId: str
        :param _EvidenceFile: 存证文件临时链接
        :type EvidenceFile: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EvidenceId = None
        self._EvidenceFile = None
        self._RequestId = None

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def EvidenceFile(self):
        return self._EvidenceFile

    @EvidenceFile.setter
    def EvidenceFile(self, EvidenceFile):
        self._EvidenceFile = EvidenceFile

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        self._EvidenceFile = params.get("EvidenceFile")
        self._RequestId = params.get("RequestId")


class GetDepositInfoRequest(AbstractModel):
    """GetDepositInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self._EvidenceId = None

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDepositInfoResponse(AbstractModel):
    """GetDepositInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编号
        :type EvidenceId: str
        :param _EvidenceTime: 上链时间
        :type EvidenceTime: str
        :param _EvidenceTxHash: 区块链交易哈希
        :type EvidenceTxHash: str
        :param _BlockchainHeight: 区块高度
        :type BlockchainHeight: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EvidenceId = None
        self._EvidenceTime = None
        self._EvidenceTxHash = None
        self._BlockchainHeight = None
        self._RequestId = None

    @property
    def EvidenceId(self):
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def EvidenceTime(self):
        return self._EvidenceTime

    @EvidenceTime.setter
    def EvidenceTime(self, EvidenceTime):
        self._EvidenceTime = EvidenceTime

    @property
    def EvidenceTxHash(self):
        return self._EvidenceTxHash

    @EvidenceTxHash.setter
    def EvidenceTxHash(self, EvidenceTxHash):
        self._EvidenceTxHash = EvidenceTxHash

    @property
    def BlockchainHeight(self):
        return self._BlockchainHeight

    @BlockchainHeight.setter
    def BlockchainHeight(self, BlockchainHeight):
        self._BlockchainHeight = BlockchainHeight

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        self._EvidenceTime = params.get("EvidenceTime")
        self._EvidenceTxHash = params.get("EvidenceTxHash")
        self._BlockchainHeight = params.get("BlockchainHeight")
        self._RequestId = params.get("RequestId")