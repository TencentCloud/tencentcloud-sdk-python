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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class CreateAudioDepositRequest(AbstractModel):
    r"""CreateAudioDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param _FileName: 带后缀的文件名称，如music.mp3
        :type FileName: str
        :param _EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._FileContent = None
        self._FileName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        r"""存证名称(长度最大30)
        :rtype: str
        """
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def FileContent(self):
        r"""数据Base64编码，大小不超过5M
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileName(self):
        r"""带后缀的文件名称，如music.mp3
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def EvidenceHash(self):
        r"""文件hash
        :rtype: str
        """
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        r"""算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :rtype: int
        """
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        r"""存证描述
        :rtype: str
        """
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._FileContent = params.get("FileContent")
        self._FileName = params.get("FileName")
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
        


class CreateAudioDepositResponse(AbstractModel):
    r"""CreateAudioDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        r"""请求成功，返回存证编码,用于查询存证后续业务数据
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateDataDepositRequest(AbstractModel):
    r"""CreateDataDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceInfo: 业务数据明文(json格式字符串)，最大256kb
        :type EvidenceInfo: str
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceInfo = None
        self._EvidenceName = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceInfo(self):
        r"""业务数据明文(json格式字符串)，最大256kb
        :rtype: str
        """
        return self._EvidenceInfo

    @EvidenceInfo.setter
    def EvidenceInfo(self, EvidenceInfo):
        self._EvidenceInfo = EvidenceInfo

    @property
    def EvidenceName(self):
        r"""存证名称(长度最大30)
        :rtype: str
        """
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        r"""算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :rtype: int
        """
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        r"""存证描述
        :rtype: str
        """
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceInfo = params.get("EvidenceInfo")
        self._EvidenceName = params.get("EvidenceName")
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
    r"""CreateDataDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        r"""请求成功，返回存证编码,用于查询存证后续业务数据
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateDocDepositRequest(AbstractModel):
    r"""CreateDocDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param _FileName: 带后缀的文件名称，如 test.doc
        :type FileName: str
        :param _EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._FileContent = None
        self._FileName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        r"""存证名称(长度最大30)
        :rtype: str
        """
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def FileContent(self):
        r"""数据Base64编码，大小不超过5M
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileName(self):
        r"""带后缀的文件名称，如 test.doc
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def EvidenceHash(self):
        r"""文件hash
        :rtype: str
        """
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        r"""算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :rtype: int
        """
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        r"""存证描述
        :rtype: str
        """
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._FileContent = params.get("FileContent")
        self._FileName = params.get("FileName")
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
        


class CreateDocDepositResponse(AbstractModel):
    r"""CreateDocDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        r"""请求成功，返回存证编码,用于查询存证后续业务数据
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateHashDepositNoCertRequest(AbstractModel):
    r"""CreateHashDepositNoCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param _BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param _EvidenceInfo: 业务扩展信息
        :type EvidenceInfo: str
        """
        self._EvidenceHash = None
        self._BusinessId = None
        self._EvidenceInfo = None

    @property
    def EvidenceHash(self):
        r"""数据hash
        :rtype: str
        """
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        r"""该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceInfo(self):
        r"""业务扩展信息
        :rtype: str
        """
        return self._EvidenceInfo

    @EvidenceInfo.setter
    def EvidenceInfo(self, EvidenceInfo):
        self._EvidenceInfo = EvidenceInfo


    def _deserialize(self, params):
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._EvidenceInfo = params.get("EvidenceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositNoCertResponse(AbstractModel):
    r"""CreateHashDepositNoCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        r"""透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        r"""存证编码
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateHashDepositNoSealRequest(AbstractModel):
    r"""CreateHashDepositNoSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param _BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param _EvidenceInfo: 业务扩展信息
        :type EvidenceInfo: str
        """
        self._EvidenceHash = None
        self._BusinessId = None
        self._EvidenceInfo = None

    @property
    def EvidenceHash(self):
        r"""数据hash
        :rtype: str
        """
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        r"""该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceInfo(self):
        r"""业务扩展信息
        :rtype: str
        """
        return self._EvidenceInfo

    @EvidenceInfo.setter
    def EvidenceInfo(self, EvidenceInfo):
        self._EvidenceInfo = EvidenceInfo


    def _deserialize(self, params):
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._EvidenceInfo = params.get("EvidenceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositNoSealResponse(AbstractModel):
    r"""CreateHashDepositNoSeal返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        r"""透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        r"""存证编码
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateHashDepositRequest(AbstractModel):
    r"""CreateHashDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param _BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        r"""存证名称(长度最大30)
        :rtype: str
        """
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def EvidenceHash(self):
        r"""数据hash
        :rtype: str
        """
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        r"""该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceDescription(self):
        r"""存证描述
        :rtype: str
        """
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._EvidenceHash = params.get("EvidenceHash")
        self._BusinessId = params.get("BusinessId")
        self._EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositResponse(AbstractModel):
    r"""CreateHashDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        r"""透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        r"""存证编码
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateImageDepositRequest(AbstractModel):
    r"""CreateImageDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param _FileName: 带后缀的文件名称，如 test.png
        :type FileName: str
        :param _EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._FileContent = None
        self._FileName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        r"""存证名称(长度最大30)
        :rtype: str
        """
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def FileContent(self):
        r"""数据Base64编码，大小不超过5M
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileName(self):
        r"""带后缀的文件名称，如 test.png
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def EvidenceHash(self):
        r"""文件hash
        :rtype: str
        """
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        r"""算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :rtype: int
        """
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        r"""存证描述
        :rtype: str
        """
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._FileContent = params.get("FileContent")
        self._FileName = params.get("FileName")
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
        


class CreateImageDepositResponse(AbstractModel):
    r"""CreateImageDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        r"""请求成功，返回存证编码,用于查询存证后续业务数据
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class CreateVideoDepositRequest(AbstractModel):
    r"""CreateVideoDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param _FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param _FileName: 带后缀的文件名称，如music.mkv
        :type FileName: str
        :param _EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param _BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param _HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param _EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self._EvidenceName = None
        self._FileContent = None
        self._FileName = None
        self._EvidenceHash = None
        self._BusinessId = None
        self._HashType = None
        self._EvidenceDescription = None

    @property
    def EvidenceName(self):
        r"""存证名称(长度最大30)
        :rtype: str
        """
        return self._EvidenceName

    @EvidenceName.setter
    def EvidenceName(self, EvidenceName):
        self._EvidenceName = EvidenceName

    @property
    def FileContent(self):
        r"""数据Base64编码，大小不超过5M
        :rtype: str
        """
        return self._FileContent

    @FileContent.setter
    def FileContent(self, FileContent):
        self._FileContent = FileContent

    @property
    def FileName(self):
        r"""带后缀的文件名称，如music.mkv
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def EvidenceHash(self):
        r"""文件hash
        :rtype: str
        """
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def HashType(self):
        r"""算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :rtype: int
        """
        return self._HashType

    @HashType.setter
    def HashType(self, HashType):
        self._HashType = HashType

    @property
    def EvidenceDescription(self):
        r"""存证描述
        :rtype: str
        """
        return self._EvidenceDescription

    @EvidenceDescription.setter
    def EvidenceDescription(self, EvidenceDescription):
        self._EvidenceDescription = EvidenceDescription


    def _deserialize(self, params):
        self._EvidenceName = params.get("EvidenceName")
        self._FileContent = params.get("FileContent")
        self._FileName = params.get("FileName")
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
        


class CreateVideoDepositResponse(AbstractModel):
    r"""CreateVideoDeposit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BusinessId: 业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :type BusinessId: str
        :param _EvidenceId: 请求成功，返回存证编码,用于查询存证后续业务数据
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BusinessId = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def BusinessId(self):
        r"""业务ID 透传 长度最大不超过64
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BusinessId

    @BusinessId.setter
    def BusinessId(self, BusinessId):
        self._BusinessId = BusinessId

    @property
    def EvidenceId(self):
        r"""请求成功，返回存证编码,用于查询存证后续业务数据
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._BusinessId = params.get("BusinessId")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class GetDepositCertRequest(AbstractModel):
    r"""GetDepositCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self._EvidenceId = None

    @property
    def EvidenceId(self):
        r"""存证编码
        :rtype: str
        """
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
    r"""GetDepositCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        :param _EvidenceCert: 存证证书文件临时链接
        :type EvidenceCert: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EvidenceId = None
        self._EvidenceCert = None
        self._RequestId = None

    @property
    def EvidenceId(self):
        r"""存证编码
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def EvidenceCert(self):
        r"""存证证书文件临时链接
        :rtype: str
        """
        return self._EvidenceCert

    @EvidenceCert.setter
    def EvidenceCert(self, EvidenceCert):
        self._EvidenceCert = EvidenceCert

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        self._EvidenceCert = params.get("EvidenceCert")
        self._RequestId = params.get("RequestId")


class GetDepositFileRequest(AbstractModel):
    r"""GetDepositFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self._EvidenceId = None

    @property
    def EvidenceId(self):
        r"""存证编码
        :rtype: str
        """
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
    r"""GetDepositFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编号
        :type EvidenceId: str
        :param _EvidenceFile: 存证文件临时链接
        :type EvidenceFile: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EvidenceId = None
        self._EvidenceFile = None
        self._RequestId = None

    @property
    def EvidenceId(self):
        r"""存证编号
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def EvidenceFile(self):
        r"""存证文件临时链接
        :rtype: str
        """
        return self._EvidenceFile

    @EvidenceFile.setter
    def EvidenceFile(self, EvidenceFile):
        self._EvidenceFile = EvidenceFile

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        self._EvidenceFile = params.get("EvidenceFile")
        self._RequestId = params.get("RequestId")


class GetDepositInfoRequest(AbstractModel):
    r"""GetDepositInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编码
        :type EvidenceId: str
        """
        self._EvidenceId = None

    @property
    def EvidenceId(self):
        r"""存证编码
        :rtype: str
        """
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
    r"""GetDepositInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceId: 存证编号
        :type EvidenceId: str
        :param _EvidenceTime: 上链时间
        :type EvidenceTime: str
        :param _EvidenceTxHash: 区块链交易哈希
        :type EvidenceTxHash: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EvidenceId = None
        self._EvidenceTime = None
        self._EvidenceTxHash = None
        self._RequestId = None

    @property
    def EvidenceId(self):
        r"""存证编号
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def EvidenceTime(self):
        r"""上链时间
        :rtype: str
        """
        return self._EvidenceTime

    @EvidenceTime.setter
    def EvidenceTime(self, EvidenceTime):
        self._EvidenceTime = EvidenceTime

    @property
    def EvidenceTxHash(self):
        r"""区块链交易哈希
        :rtype: str
        """
        return self._EvidenceTxHash

    @EvidenceTxHash.setter
    def EvidenceTxHash(self, EvidenceTxHash):
        self._EvidenceTxHash = EvidenceTxHash

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._EvidenceId = params.get("EvidenceId")
        self._EvidenceTime = params.get("EvidenceTime")
        self._EvidenceTxHash = params.get("EvidenceTxHash")
        self._RequestId = params.get("RequestId")


class VerifyEvidenceBlockChainTxHashRequest(AbstractModel):
    r"""VerifyEvidenceBlockChainTxHash请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceTxHash: 区块链交易 hash，在“存证基本信息查询（GetDepositInfo）”接口中可以获取。
        :type EvidenceTxHash: str
        """
        self._EvidenceTxHash = None

    @property
    def EvidenceTxHash(self):
        r"""区块链交易 hash，在“存证基本信息查询（GetDepositInfo）”接口中可以获取。
        :rtype: str
        """
        return self._EvidenceTxHash

    @EvidenceTxHash.setter
    def EvidenceTxHash(self, EvidenceTxHash):
        self._EvidenceTxHash = EvidenceTxHash


    def _deserialize(self, params):
        self._EvidenceTxHash = params.get("EvidenceTxHash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyEvidenceBlockChainTxHashResponse(AbstractModel):
    r"""VerifyEvidenceBlockChainTxHash返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 核验结果，true为核验成功，fals为核验失败
        :type Result: bool
        :param _EvidenceTime: 存证时间，仅当核验结果为true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type EvidenceTime: str
        :param _EvidenceId: 存证编码，仅当核验结果为true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type EvidenceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._EvidenceTime = None
        self._EvidenceId = None
        self._RequestId = None

    @property
    def Result(self):
        r"""核验结果，true为核验成功，fals为核验失败
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def EvidenceTime(self):
        r"""存证时间，仅当核验结果为true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EvidenceTime

    @EvidenceTime.setter
    def EvidenceTime(self, EvidenceTime):
        self._EvidenceTime = EvidenceTime

    @property
    def EvidenceId(self):
        r"""存证编码，仅当核验结果为true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EvidenceId

    @EvidenceId.setter
    def EvidenceId(self, EvidenceId):
        self._EvidenceId = EvidenceId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._EvidenceTime = params.get("EvidenceTime")
        self._EvidenceId = params.get("EvidenceId")
        self._RequestId = params.get("RequestId")


class VerifyEvidenceHashRequest(AbstractModel):
    r"""VerifyEvidenceHash请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EvidenceHash: 存证内容hash，hash类型即为用户在存证时所用或所选的hash类型
        :type EvidenceHash: str
        """
        self._EvidenceHash = None

    @property
    def EvidenceHash(self):
        r"""存证内容hash，hash类型即为用户在存证时所用或所选的hash类型
        :rtype: str
        """
        return self._EvidenceHash

    @EvidenceHash.setter
    def EvidenceHash(self, EvidenceHash):
        self._EvidenceHash = EvidenceHash


    def _deserialize(self, params):
        self._EvidenceHash = params.get("EvidenceHash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyEvidenceHashResponse(AbstractModel):
    r"""VerifyEvidenceHash返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 核验结果，true为核验成功，false为核验失败
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        r"""核验结果，true为核验成功，false为核验失败
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")