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
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param FileName: 带后缀的文件名称，如music.mp3
        :type FileName: str
        :param EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.FileContent = None
        self.FileName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.FileContent = params.get("FileContent")
        self.FileName = params.get("FileName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAudioDepositResponse(AbstractModel):
    """CreateAudioDeposit返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateDataDepositRequest(AbstractModel):
    """CreateDataDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceInfo: 业务数据明文(json格式字符串)，最大256kb
        :type EvidenceInfo: str
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceInfo = None
        self.EvidenceName = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceInfo = params.get("EvidenceInfo")
        self.EvidenceName = params.get("EvidenceName")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDataDepositResponse(AbstractModel):
    """CreateDataDeposit返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateDocDepositRequest(AbstractModel):
    """CreateDocDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param FileName: 带后缀的文件名称，如 test.doc
        :type FileName: str
        :param EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.FileContent = None
        self.FileName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.FileContent = params.get("FileContent")
        self.FileName = params.get("FileName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDocDepositResponse(AbstractModel):
    """CreateDocDeposit返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateHashDepositNoCertRequest(AbstractModel):
    """CreateHashDepositNoCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param EvidenceInfo: 业务扩展信息
        :type EvidenceInfo: str
        """
        self.EvidenceHash = None
        self.BusinessId = None
        self.EvidenceInfo = None


    def _deserialize(self, params):
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.EvidenceInfo = params.get("EvidenceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositNoCertResponse(AbstractModel):
    """CreateHashDepositNoCert返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateHashDepositNoSealRequest(AbstractModel):
    """CreateHashDepositNoSeal请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param EvidenceInfo: 业务扩展信息
        :type EvidenceInfo: str
        """
        self.EvidenceHash = None
        self.BusinessId = None
        self.EvidenceInfo = None


    def _deserialize(self, params):
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.EvidenceInfo = params.get("EvidenceInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositNoSealResponse(AbstractModel):
    """CreateHashDepositNoSeal返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateHashDepositRequest(AbstractModel):
    """CreateHashDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param EvidenceHash: 数据hash
        :type EvidenceHash: str
        :param BusinessId: 该字段为透传字段，方便调用方做业务处理， 长度最大不超过64
        :type BusinessId: str
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHashDepositResponse(AbstractModel):
    """CreateHashDeposit返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateImageDepositRequest(AbstractModel):
    """CreateImageDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param FileName: 带后缀的文件名称，如 test.png
        :type FileName: str
        :param EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.FileContent = None
        self.FileName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.FileContent = params.get("FileContent")
        self.FileName = params.get("FileName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageDepositResponse(AbstractModel):
    """CreateImageDeposit返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreateVideoDepositRequest(AbstractModel):
    """CreateVideoDeposit请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceName: 存证名称(长度最大30)
        :type EvidenceName: str
        :param FileContent: 数据Base64编码，大小不超过5M
        :type FileContent: str
        :param FileName: 带后缀的文件名称，如music.mkv
        :type FileName: str
        :param EvidenceHash: 文件hash
        :type EvidenceHash: str
        :param BusinessId: 业务ID 透传 长度最大不超过64
        :type BusinessId: str
        :param HashType: 算法类型 0 SM3, 1 SHA256, 2 SHA384 默认0
        :type HashType: int
        :param EvidenceDescription: 存证描述
        :type EvidenceDescription: str
        """
        self.EvidenceName = None
        self.FileContent = None
        self.FileName = None
        self.EvidenceHash = None
        self.BusinessId = None
        self.HashType = None
        self.EvidenceDescription = None


    def _deserialize(self, params):
        self.EvidenceName = params.get("EvidenceName")
        self.FileContent = params.get("FileContent")
        self.FileName = params.get("FileName")
        self.EvidenceHash = params.get("EvidenceHash")
        self.BusinessId = params.get("BusinessId")
        self.HashType = params.get("HashType")
        self.EvidenceDescription = params.get("EvidenceDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVideoDepositResponse(AbstractModel):
    """CreateVideoDeposit返回参数结构体

    """

    def __init__(self):
        r"""
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


class GetDepositCertRequest(AbstractModel):
    """GetDepositCert请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDepositCertResponse(AbstractModel):
    """GetDepositCert返回参数结构体

    """

    def __init__(self):
        r"""
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


class GetDepositFileRequest(AbstractModel):
    """GetDepositFile请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDepositFileResponse(AbstractModel):
    """GetDepositFile返回参数结构体

    """

    def __init__(self):
        r"""
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


class GetDepositInfoRequest(AbstractModel):
    """GetDepositInfo请求参数结构体

    """

    def __init__(self):
        r"""
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDepositInfoResponse(AbstractModel):
    """GetDepositInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceId: 存证编号
        :type EvidenceId: str
        :param EvidenceTime: 上链时间
        :type EvidenceTime: str
        :param EvidenceTxHash: 区块链交易哈希
        :type EvidenceTxHash: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EvidenceId = None
        self.EvidenceTime = None
        self.EvidenceTxHash = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EvidenceId = params.get("EvidenceId")
        self.EvidenceTime = params.get("EvidenceTime")
        self.EvidenceTxHash = params.get("EvidenceTxHash")
        self.RequestId = params.get("RequestId")


class VerifyEvidenceBlockChainTxHashRequest(AbstractModel):
    """VerifyEvidenceBlockChainTxHash请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceTxHash: 区块链交易 hash，在“存证基本信息查询（GetDepositInfo）”接口中可以获取。
        :type EvidenceTxHash: str
        """
        self.EvidenceTxHash = None


    def _deserialize(self, params):
        self.EvidenceTxHash = params.get("EvidenceTxHash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyEvidenceBlockChainTxHashResponse(AbstractModel):
    """VerifyEvidenceBlockChainTxHash返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 核验结果，true为核验成功，fals为核验失败
        :type Result: bool
        :param EvidenceTime: 存证时间，仅当核验结果为true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type EvidenceTime: str
        :param EvidenceId: 存证编码，仅当核验结果为true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type EvidenceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.EvidenceTime = None
        self.EvidenceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.EvidenceTime = params.get("EvidenceTime")
        self.EvidenceId = params.get("EvidenceId")
        self.RequestId = params.get("RequestId")


class VerifyEvidenceHashRequest(AbstractModel):
    """VerifyEvidenceHash请求参数结构体

    """

    def __init__(self):
        r"""
        :param EvidenceHash: 存证内容hash，hash类型即为用户在存证时所用或所选的hash类型
        :type EvidenceHash: str
        """
        self.EvidenceHash = None


    def _deserialize(self, params):
        self.EvidenceHash = params.get("EvidenceHash")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyEvidenceHashResponse(AbstractModel):
    """VerifyEvidenceHash返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 核验结果，true为核验成功，false为核验失败
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")