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


class CertificateIdentityUser(AbstractModel):
    """证书用户信息和身份鉴别信息。则该字段无需传入，默认为空。对电子签名者身份鉴别类型及措施有特殊展示要求的可使用该字段。

    """

    def __init__(self):
        r"""
        :param _Name: 姓名
        :type Name: str
        :param _IdentityUniqueId: 唯一身份id
        :type IdentityUniqueId: str
        :param _IdCardNumber: 身份证号
        :type IdCardNumber: str
        :param _IdentificationType: 身份鉴别类型
1：授权金融机构身份鉴别
        :type IdentificationType: str
        :param _IdentificationMeasures: 身份鉴别措施
1、身份证鉴别
2、银行卡鉴别
3、支付账户密码验证
4、人脸识别验证
        :type IdentificationMeasures: list of str
        """
        self._Name = None
        self._IdentityUniqueId = None
        self._IdCardNumber = None
        self._IdentificationType = None
        self._IdentificationMeasures = None

    @property
    def Name(self):
        """姓名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def IdentityUniqueId(self):
        """唯一身份id
        :rtype: str
        """
        return self._IdentityUniqueId

    @IdentityUniqueId.setter
    def IdentityUniqueId(self, IdentityUniqueId):
        self._IdentityUniqueId = IdentityUniqueId

    @property
    def IdCardNumber(self):
        """身份证号
        :rtype: str
        """
        return self._IdCardNumber

    @IdCardNumber.setter
    def IdCardNumber(self, IdCardNumber):
        self._IdCardNumber = IdCardNumber

    @property
    def IdentificationType(self):
        """身份鉴别类型
1：授权金融机构身份鉴别
        :rtype: str
        """
        return self._IdentificationType

    @IdentificationType.setter
    def IdentificationType(self, IdentificationType):
        self._IdentificationType = IdentificationType

    @property
    def IdentificationMeasures(self):
        """身份鉴别措施
1、身份证鉴别
2、银行卡鉴别
3、支付账户密码验证
4、人脸识别验证
        :rtype: list of str
        """
        return self._IdentificationMeasures

    @IdentificationMeasures.setter
    def IdentificationMeasures(self, IdentificationMeasures):
        self._IdentificationMeasures = IdentificationMeasures


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._IdentityUniqueId = params.get("IdentityUniqueId")
        self._IdCardNumber = params.get("IdCardNumber")
        self._IdentificationType = params.get("IdentificationType")
        self._IdentificationMeasures = params.get("IdentificationMeasures")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVerifyReportRequest(AbstractModel):
    """CreateVerifyReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApplyCustomerType: 申请者类型 1:个人，2:企业
        :type ApplyCustomerType: str
        :param _ApplyCustomerName: 申请企业 or 自然人名称
        :type ApplyCustomerName: str
        :param _ApplyName: 验签申请经办人姓名
        :type ApplyName: str
        :param _ApplyMobile: 验签申请经办人电话
        :type ApplyMobile: str
        :param _FileId: 验签文件id
        :type FileId: str
        :param _ApplyEmail: 验签申请经办人邮箱
        :type ApplyEmail: str
        :param _CertificateIdentityUsers: 证书用户身份及身份鉴别信息
        :type CertificateIdentityUsers: list of CertificateIdentityUser
        """
        self._ApplyCustomerType = None
        self._ApplyCustomerName = None
        self._ApplyName = None
        self._ApplyMobile = None
        self._FileId = None
        self._ApplyEmail = None
        self._CertificateIdentityUsers = None

    @property
    def ApplyCustomerType(self):
        """申请者类型 1:个人，2:企业
        :rtype: str
        """
        return self._ApplyCustomerType

    @ApplyCustomerType.setter
    def ApplyCustomerType(self, ApplyCustomerType):
        self._ApplyCustomerType = ApplyCustomerType

    @property
    def ApplyCustomerName(self):
        """申请企业 or 自然人名称
        :rtype: str
        """
        return self._ApplyCustomerName

    @ApplyCustomerName.setter
    def ApplyCustomerName(self, ApplyCustomerName):
        self._ApplyCustomerName = ApplyCustomerName

    @property
    def ApplyName(self):
        """验签申请经办人姓名
        :rtype: str
        """
        return self._ApplyName

    @ApplyName.setter
    def ApplyName(self, ApplyName):
        self._ApplyName = ApplyName

    @property
    def ApplyMobile(self):
        """验签申请经办人电话
        :rtype: str
        """
        return self._ApplyMobile

    @ApplyMobile.setter
    def ApplyMobile(self, ApplyMobile):
        self._ApplyMobile = ApplyMobile

    @property
    def FileId(self):
        """验签文件id
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId

    @property
    def ApplyEmail(self):
        """验签申请经办人邮箱
        :rtype: str
        """
        return self._ApplyEmail

    @ApplyEmail.setter
    def ApplyEmail(self, ApplyEmail):
        self._ApplyEmail = ApplyEmail

    @property
    def CertificateIdentityUsers(self):
        """证书用户身份及身份鉴别信息
        :rtype: list of CertificateIdentityUser
        """
        return self._CertificateIdentityUsers

    @CertificateIdentityUsers.setter
    def CertificateIdentityUsers(self, CertificateIdentityUsers):
        self._CertificateIdentityUsers = CertificateIdentityUsers


    def _deserialize(self, params):
        self._ApplyCustomerType = params.get("ApplyCustomerType")
        self._ApplyCustomerName = params.get("ApplyCustomerName")
        self._ApplyName = params.get("ApplyName")
        self._ApplyMobile = params.get("ApplyMobile")
        self._FileId = params.get("FileId")
        self._ApplyEmail = params.get("ApplyEmail")
        if params.get("CertificateIdentityUsers") is not None:
            self._CertificateIdentityUsers = []
            for item in params.get("CertificateIdentityUsers"):
                obj = CertificateIdentityUser()
                obj._deserialize(item)
                self._CertificateIdentityUsers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVerifyReportResponse(AbstractModel):
    """CreateVerifyReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SignatureId: 签名id
        :type SignatureId: str
        :param _Code: code
        :type Code: str
        :param _Message: message
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SignatureId = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def SignatureId(self):
        """签名id
        :rtype: str
        """
        return self._SignatureId

    @SignatureId.setter
    def SignatureId(self, SignatureId):
        self._SignatureId = SignatureId

    @property
    def Code(self):
        """code
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SignatureId = params.get("SignatureId")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeVerifyReportRequest(AbstractModel):
    """DescribeVerifyReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SignatureId: 签名id
        :type SignatureId: str
        """
        self._SignatureId = None

    @property
    def SignatureId(self):
        """签名id
        :rtype: str
        """
        return self._SignatureId

    @SignatureId.setter
    def SignatureId(self, SignatureId):
        self._SignatureId = SignatureId


    def _deserialize(self, params):
        self._SignatureId = params.get("SignatureId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVerifyReportResponse(AbstractModel):
    """DescribeVerifyReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportUrl: 下载url
        :type ReportUrl: str
        :param _Code: code
        :type Code: str
        :param _Message: message
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportUrl = None
        self._Code = None
        self._Message = None
        self._RequestId = None

    @property
    def ReportUrl(self):
        """下载url
        :rtype: str
        """
        return self._ReportUrl

    @ReportUrl.setter
    def ReportUrl(self, ReportUrl):
        self._ReportUrl = ReportUrl

    @property
    def Code(self):
        """code
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        """message
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReportUrl = params.get("ReportUrl")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class FileInfo(AbstractModel):
    """文件列表信息

    """

    def __init__(self):
        r"""
        :param _FileBody: BASE64编码后的文件内容
        :type FileBody: str
        :param _FileName: 文件名及类型，最大长度不超过200字符
        :type FileName: str
        """
        self._FileBody = None
        self._FileName = None

    @property
    def FileBody(self):
        """BASE64编码后的文件内容
        :rtype: str
        """
        return self._FileBody

    @FileBody.setter
    def FileBody(self, FileBody):
        self._FileBody = FileBody

    @property
    def FileName(self):
        """文件名及类型，最大长度不超过200字符
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName


    def _deserialize(self, params):
        self._FileBody = params.get("FileBody")
        self._FileName = params.get("FileName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFileRequest(AbstractModel):
    """UploadFile请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileInfos: 验签源文件信息列表
        :type FileInfos: list of FileInfo
        """
        self._FileInfos = None

    @property
    def FileInfos(self):
        """验签源文件信息列表
        :rtype: list of FileInfo
        """
        return self._FileInfos

    @FileInfos.setter
    def FileInfos(self, FileInfos):
        self._FileInfos = FileInfos


    def _deserialize(self, params):
        if params.get("FileInfos") is not None:
            self._FileInfos = []
            for item in params.get("FileInfos"):
                obj = FileInfo()
                obj._deserialize(item)
                self._FileInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadFileResponse(AbstractModel):
    """UploadFile返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FileIds: 文件id列表
        :type FileIds: list of str
        :param _TotalCount: 文件id总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FileIds = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def FileIds(self):
        """文件id列表
        :rtype: list of str
        """
        return self._FileIds

    @FileIds.setter
    def FileIds(self, FileIds):
        self._FileIds = FileIds

    @property
    def TotalCount(self):
        """文件id总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._FileIds = params.get("FileIds")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")