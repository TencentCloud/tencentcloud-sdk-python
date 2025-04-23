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


class CreateProductSecretRequest(AbstractModel):
    """CreateProductSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称，同一region内不可重复，最长128字节，使用字母、数字或者 - _ 的组合，第一个字符必须为字母或者数字。
        :type SecretName: str
        :param _UserNamePrefix: 用户账号名前缀，由用户自行指定，长度限定在8个字符以内，
可选字符集包括：
数字字符：[0, 9]，
小写字符：[a, z]，
大写字符：[A, Z]，
特殊字符(全英文符号)：下划线(_)，
前缀必须以大写或小写字母开头。
        :type UserNamePrefix: str
        :param _ProductName: 凭据所绑定的云产品名称，如Mysql，可以通过DescribeSupportedProducts接口获取所支持的云产品名称。
        :type ProductName: str
        :param _InstanceID: 云产品实例ID。
        :type InstanceID: str
        :param _Domains: 账号的域名，IP形式，支持填入%。
        :type Domains: list of str
        :param _PrivilegesList: 将凭据与云产品实例绑定时，需要授予的权限列表。
        :type PrivilegesList: list of ProductPrivilegeUnit
        :param _Description: 描述信息，用于详细描述用途等，最大支持2048字节。
        :type Description: str
        :param _KmsKeyId: 指定对凭据进行加密的KMS CMK。
如果为空则表示使用Secrets Manager为您默认创建的CMK进行加密。
您也可以指定在同region 下自行创建的KMS CMK进行加密。
        :type KmsKeyId: str
        :param _Tags: 标签列表。
        :type Tags: list of Tag
        :param _RotationBeginTime: 用户自定义的开始轮转时间，格式：2006-01-02 15:04:05。
当EnableRotation为True时，此参数必填。
        :type RotationBeginTime: str
        :param _EnableRotation: 是否开启轮转
True -- 开启
False -- 不开启
如果不指定，默认为False。
        :type EnableRotation: bool
        :param _RotationFrequency: 轮转周期，以天为单位，默认为1天。
        :type RotationFrequency: int
        :param _KmsHsmClusterId: KMS的独享集群的ID。当KmsKeyId为空,并且用户的KMS存在有效的HsmClusterId时有效。
        :type KmsHsmClusterId: str
        """
        self._SecretName = None
        self._UserNamePrefix = None
        self._ProductName = None
        self._InstanceID = None
        self._Domains = None
        self._PrivilegesList = None
        self._Description = None
        self._KmsKeyId = None
        self._Tags = None
        self._RotationBeginTime = None
        self._EnableRotation = None
        self._RotationFrequency = None
        self._KmsHsmClusterId = None

    @property
    def SecretName(self):
        """凭据名称，同一region内不可重复，最长128字节，使用字母、数字或者 - _ 的组合，第一个字符必须为字母或者数字。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def UserNamePrefix(self):
        """用户账号名前缀，由用户自行指定，长度限定在8个字符以内，
可选字符集包括：
数字字符：[0, 9]，
小写字符：[a, z]，
大写字符：[A, Z]，
特殊字符(全英文符号)：下划线(_)，
前缀必须以大写或小写字母开头。
        :rtype: str
        """
        return self._UserNamePrefix

    @UserNamePrefix.setter
    def UserNamePrefix(self, UserNamePrefix):
        self._UserNamePrefix = UserNamePrefix

    @property
    def ProductName(self):
        """凭据所绑定的云产品名称，如Mysql，可以通过DescribeSupportedProducts接口获取所支持的云产品名称。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def InstanceID(self):
        """云产品实例ID。
        :rtype: str
        """
        return self._InstanceID

    @InstanceID.setter
    def InstanceID(self, InstanceID):
        self._InstanceID = InstanceID

    @property
    def Domains(self):
        """账号的域名，IP形式，支持填入%。
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def PrivilegesList(self):
        """将凭据与云产品实例绑定时，需要授予的权限列表。
        :rtype: list of ProductPrivilegeUnit
        """
        return self._PrivilegesList

    @PrivilegesList.setter
    def PrivilegesList(self, PrivilegesList):
        self._PrivilegesList = PrivilegesList

    @property
    def Description(self):
        """描述信息，用于详细描述用途等，最大支持2048字节。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """指定对凭据进行加密的KMS CMK。
如果为空则表示使用Secrets Manager为您默认创建的CMK进行加密。
您也可以指定在同region 下自行创建的KMS CMK进行加密。
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def Tags(self):
        """标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RotationBeginTime(self):
        """用户自定义的开始轮转时间，格式：2006-01-02 15:04:05。
当EnableRotation为True时，此参数必填。
        :rtype: str
        """
        return self._RotationBeginTime

    @RotationBeginTime.setter
    def RotationBeginTime(self, RotationBeginTime):
        self._RotationBeginTime = RotationBeginTime

    @property
    def EnableRotation(self):
        """是否开启轮转
True -- 开启
False -- 不开启
如果不指定，默认为False。
        :rtype: bool
        """
        return self._EnableRotation

    @EnableRotation.setter
    def EnableRotation(self, EnableRotation):
        self._EnableRotation = EnableRotation

    @property
    def RotationFrequency(self):
        """轮转周期，以天为单位，默认为1天。
        :rtype: int
        """
        return self._RotationFrequency

    @RotationFrequency.setter
    def RotationFrequency(self, RotationFrequency):
        self._RotationFrequency = RotationFrequency

    @property
    def KmsHsmClusterId(self):
        """KMS的独享集群的ID。当KmsKeyId为空,并且用户的KMS存在有效的HsmClusterId时有效。
        :rtype: str
        """
        return self._KmsHsmClusterId

    @KmsHsmClusterId.setter
    def KmsHsmClusterId(self, KmsHsmClusterId):
        self._KmsHsmClusterId = KmsHsmClusterId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._UserNamePrefix = params.get("UserNamePrefix")
        self._ProductName = params.get("ProductName")
        self._InstanceID = params.get("InstanceID")
        self._Domains = params.get("Domains")
        if params.get("PrivilegesList") is not None:
            self._PrivilegesList = []
            for item in params.get("PrivilegesList"):
                obj = ProductPrivilegeUnit()
                obj._deserialize(item)
                self._PrivilegesList.append(obj)
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RotationBeginTime = params.get("RotationBeginTime")
        self._EnableRotation = params.get("EnableRotation")
        self._RotationFrequency = params.get("RotationFrequency")
        self._KmsHsmClusterId = params.get("KmsHsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProductSecretResponse(AbstractModel):
    """CreateProductSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 创建的凭据名称。
        :type SecretName: str
        :param _TagCode: 标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误。
        :type TagCode: int
        :param _TagMsg: 标签操作的返回信息。
        :type TagMsg: str
        :param _FlowID: 创建云产品凭据异步任务ID号。
        :type FlowID: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._TagCode = None
        self._TagMsg = None
        self._FlowID = None
        self._RequestId = None

    @property
    def SecretName(self):
        """创建的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def TagCode(self):
        """标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误。
        :rtype: int
        """
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        """标签操作的返回信息。
        :rtype: str
        """
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

    @property
    def FlowID(self):
        """创建云产品凭据异步任务ID号。
        :rtype: int
        """
        return self._FlowID

    @FlowID.setter
    def FlowID(self, FlowID):
        self._FlowID = FlowID

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
        self._SecretName = params.get("SecretName")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._FlowID = params.get("FlowID")
        self._RequestId = params.get("RequestId")


class CreateSSHKeyPairSecretRequest(AbstractModel):
    """CreateSSHKeyPairSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称，同一region内不可重复，最长128字节，使用字母、数字或者 - _ 的组合，第一个字符必须为字母或者数字。
        :type SecretName: str
        :param _ProjectId: 密钥对创建后所属的项目ID。
        :type ProjectId: int
        :param _Description: 描述信息，用于详细描述用途等，最大支持2048字节。
        :type Description: str
        :param _KmsKeyId: 指定对凭据进行加密的KMS CMK。
如果为空则表示使用Secrets Manager为您默认创建的CMK进行加密。
您也可以指定在同region 下自行创建的KMS CMK进行加密。
        :type KmsKeyId: str
        :param _Tags: 标签列表。
        :type Tags: list of Tag
        :param _SSHKeyName: 用户自定义输入的SSH密钥对的名称，可由数字，字母和下划线组成，只能以数字和字母开头，长度不超过25个字符。
        :type SSHKeyName: str
        :param _KmsHsmClusterId: KMS的独享集群的ID。当KmsKeyId为空,并且用户的KMS存在有效的HsmClusterId时有效。
        :type KmsHsmClusterId: str
        """
        self._SecretName = None
        self._ProjectId = None
        self._Description = None
        self._KmsKeyId = None
        self._Tags = None
        self._SSHKeyName = None
        self._KmsHsmClusterId = None

    @property
    def SecretName(self):
        """凭据名称，同一region内不可重复，最长128字节，使用字母、数字或者 - _ 的组合，第一个字符必须为字母或者数字。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def ProjectId(self):
        """密钥对创建后所属的项目ID。
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Description(self):
        """描述信息，用于详细描述用途等，最大支持2048字节。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """指定对凭据进行加密的KMS CMK。
如果为空则表示使用Secrets Manager为您默认创建的CMK进行加密。
您也可以指定在同region 下自行创建的KMS CMK进行加密。
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def Tags(self):
        """标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def SSHKeyName(self):
        """用户自定义输入的SSH密钥对的名称，可由数字，字母和下划线组成，只能以数字和字母开头，长度不超过25个字符。
        :rtype: str
        """
        return self._SSHKeyName

    @SSHKeyName.setter
    def SSHKeyName(self, SSHKeyName):
        self._SSHKeyName = SSHKeyName

    @property
    def KmsHsmClusterId(self):
        """KMS的独享集群的ID。当KmsKeyId为空,并且用户的KMS存在有效的HsmClusterId时有效。
        :rtype: str
        """
        return self._KmsHsmClusterId

    @KmsHsmClusterId.setter
    def KmsHsmClusterId(self, KmsHsmClusterId):
        self._KmsHsmClusterId = KmsHsmClusterId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._ProjectId = params.get("ProjectId")
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._SSHKeyName = params.get("SSHKeyName")
        self._KmsHsmClusterId = params.get("KmsHsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSSHKeyPairSecretResponse(AbstractModel):
    """CreateSSHKeyPairSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 创建的凭据名称。
        :type SecretName: str
        :param _SSHKeyID: 创建的SSH密钥ID。
        :type SSHKeyID: str
        :param _SSHKeyName: 创建的SSH密钥名称。
        :type SSHKeyName: str
        :param _TagCode: 标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误
        :type TagCode: int
        :param _TagMsg: 标签操作的返回信息。
        :type TagMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._SSHKeyID = None
        self._SSHKeyName = None
        self._TagCode = None
        self._TagMsg = None
        self._RequestId = None

    @property
    def SecretName(self):
        """创建的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def SSHKeyID(self):
        """创建的SSH密钥ID。
        :rtype: str
        """
        return self._SSHKeyID

    @SSHKeyID.setter
    def SSHKeyID(self, SSHKeyID):
        self._SSHKeyID = SSHKeyID

    @property
    def SSHKeyName(self):
        """创建的SSH密钥名称。
        :rtype: str
        """
        return self._SSHKeyName

    @SSHKeyName.setter
    def SSHKeyName(self, SSHKeyName):
        self._SSHKeyName = SSHKeyName

    @property
    def TagCode(self):
        """标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误
        :rtype: int
        """
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        """标签操作的返回信息。
        :rtype: str
        """
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

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
        self._SecretName = params.get("SecretName")
        self._SSHKeyID = params.get("SSHKeyID")
        self._SSHKeyName = params.get("SSHKeyName")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._RequestId = params.get("RequestId")


class CreateSecretRequest(AbstractModel):
    """CreateSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称，同一region内不可重复，最长128字节，使用字母、数字或者 - _ 的组合，第一个字符必须为字母或者数字。一旦创建不可修改。
        :type SecretName: str
        :param _VersionId: 凭据版本，查询凭据信息时需要根据SecretName 和 VersionId进行查询，最长64 字节，使用字母、数字或者 - _ . 的组合并且以字母或数字开头。若为空，则使用默认的初始凭据版本号。可选，若为空或该凭据为云产品类凭据，则该版本号默认为 SSM_Current。
        :type VersionId: str
        :param _Description: 描述信息，用于详细描述用途等，最大支持2048字节。
        :type Description: str
        :param _KmsKeyId: 指定对凭据进行加密的KMS CMK。如果为空则表示使用Secrets Manager为您默认创建的CMK进行加密。您也可以指定在同region 下自行创建的KMS CMK进行加密。
        :type KmsKeyId: str
        :param _SecretType: 凭据类型，默认为0自定义凭据。
        :type SecretType: int
        :param _SecretBinary: 二进制凭据信息base64编码后的明文。SecretBinary 和 SecretString 必须且只能设置一个，最大支持32KB字节。
        :type SecretBinary: str
        :param _SecretString: 文本类型凭据信息明文（不需要进行base64编码）。SecretBinary 和 SecretString 必须且只能设置一个，最大支持32KB字节。
        :type SecretString: str
        :param _AdditionalConfig: JSON 格式字符串，用于指定特定凭据类型的额外配置。
        :type AdditionalConfig: str
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _KmsHsmClusterId: KMS的独享集群的ID。当KmsKeyId为空,并且用户的KMS存在有效的HsmClusterId时有效。
        :type KmsHsmClusterId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._Description = None
        self._KmsKeyId = None
        self._SecretType = None
        self._SecretBinary = None
        self._SecretString = None
        self._AdditionalConfig = None
        self._Tags = None
        self._KmsHsmClusterId = None

    @property
    def SecretName(self):
        """凭据名称，同一region内不可重复，最长128字节，使用字母、数字或者 - _ 的组合，第一个字符必须为字母或者数字。一旦创建不可修改。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """凭据版本，查询凭据信息时需要根据SecretName 和 VersionId进行查询，最长64 字节，使用字母、数字或者 - _ . 的组合并且以字母或数字开头。若为空，则使用默认的初始凭据版本号。可选，若为空或该凭据为云产品类凭据，则该版本号默认为 SSM_Current。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Description(self):
        """描述信息，用于详细描述用途等，最大支持2048字节。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """指定对凭据进行加密的KMS CMK。如果为空则表示使用Secrets Manager为您默认创建的CMK进行加密。您也可以指定在同region 下自行创建的KMS CMK进行加密。
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def SecretType(self):
        """凭据类型，默认为0自定义凭据。
        :rtype: int
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def SecretBinary(self):
        """二进制凭据信息base64编码后的明文。SecretBinary 和 SecretString 必须且只能设置一个，最大支持32KB字节。
        :rtype: str
        """
        return self._SecretBinary

    @SecretBinary.setter
    def SecretBinary(self, SecretBinary):
        self._SecretBinary = SecretBinary

    @property
    def SecretString(self):
        """文本类型凭据信息明文（不需要进行base64编码）。SecretBinary 和 SecretString 必须且只能设置一个，最大支持32KB字节。
        :rtype: str
        """
        return self._SecretString

    @SecretString.setter
    def SecretString(self, SecretString):
        self._SecretString = SecretString

    @property
    def AdditionalConfig(self):
        """JSON 格式字符串，用于指定特定凭据类型的额外配置。
        :rtype: str
        """
        return self._AdditionalConfig

    @AdditionalConfig.setter
    def AdditionalConfig(self, AdditionalConfig):
        self._AdditionalConfig = AdditionalConfig

    @property
    def Tags(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def KmsHsmClusterId(self):
        """KMS的独享集群的ID。当KmsKeyId为空,并且用户的KMS存在有效的HsmClusterId时有效。
        :rtype: str
        """
        return self._KmsHsmClusterId

    @KmsHsmClusterId.setter
    def KmsHsmClusterId(self, KmsHsmClusterId):
        self._KmsHsmClusterId = KmsHsmClusterId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        self._SecretType = params.get("SecretType")
        self._SecretBinary = params.get("SecretBinary")
        self._SecretString = params.get("SecretString")
        self._AdditionalConfig = params.get("AdditionalConfig")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._KmsHsmClusterId = params.get("KmsHsmClusterId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecretResponse(AbstractModel):
    """CreateSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 新创建的凭据名称。
        :type SecretName: str
        :param _VersionId: 新创建的凭据版本。
        :type VersionId: str
        :param _TagCode: 标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误
        :type TagCode: int
        :param _TagMsg: 标签操作的返回信息
        :type TagMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._TagCode = None
        self._TagMsg = None
        self._RequestId = None

    @property
    def SecretName(self):
        """新创建的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """新创建的凭据版本。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def TagCode(self):
        """标签操作的返回码. 0: 成功；1: 内部错误；2: 业务处理错误
        :rtype: int
        """
        return self._TagCode

    @TagCode.setter
    def TagCode(self, TagCode):
        self._TagCode = TagCode

    @property
    def TagMsg(self):
        """标签操作的返回信息
        :rtype: str
        """
        return self._TagMsg

    @TagMsg.setter
    def TagMsg(self, TagMsg):
        self._TagMsg = TagMsg

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
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._TagCode = params.get("TagCode")
        self._TagMsg = params.get("TagMsg")
        self._RequestId = params.get("RequestId")


class DeleteSecretRequest(AbstractModel):
    """DeleteSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定需要删除的凭据名称。
        :type SecretName: str
        :param _RecoveryWindowInDays: 指定计划删除日期，单位（天），0（默认）表示立即删除， 1-30 表示预留的天数，超出该日期之后彻底删除。
当凭据类型为SSH密钥对凭据时，此字段只能取值只能为0。
        :type RecoveryWindowInDays: int
        :param _CleanSSHKey: 当凭据类型为SSH密钥对凭据时，此字段有效，取值：
True -- 表示不仅仅清理此凭据中存储的SSH密钥信息，还会将SSH密钥对从CVM侧进行清理。注意，如果SSH密钥此时绑定了CVM实例，那么会清理失败。
False --  表示仅仅清理此凭据中存储的SSH密钥信息，不在CVM进侧进行清理。
        :type CleanSSHKey: bool
        """
        self._SecretName = None
        self._RecoveryWindowInDays = None
        self._CleanSSHKey = None

    @property
    def SecretName(self):
        """指定需要删除的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def RecoveryWindowInDays(self):
        """指定计划删除日期，单位（天），0（默认）表示立即删除， 1-30 表示预留的天数，超出该日期之后彻底删除。
当凭据类型为SSH密钥对凭据时，此字段只能取值只能为0。
        :rtype: int
        """
        return self._RecoveryWindowInDays

    @RecoveryWindowInDays.setter
    def RecoveryWindowInDays(self, RecoveryWindowInDays):
        self._RecoveryWindowInDays = RecoveryWindowInDays

    @property
    def CleanSSHKey(self):
        """当凭据类型为SSH密钥对凭据时，此字段有效，取值：
True -- 表示不仅仅清理此凭据中存储的SSH密钥信息，还会将SSH密钥对从CVM侧进行清理。注意，如果SSH密钥此时绑定了CVM实例，那么会清理失败。
False --  表示仅仅清理此凭据中存储的SSH密钥信息，不在CVM进侧进行清理。
        :rtype: bool
        """
        return self._CleanSSHKey

    @CleanSSHKey.setter
    def CleanSSHKey(self, CleanSSHKey):
        self._CleanSSHKey = CleanSSHKey


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._RecoveryWindowInDays = params.get("RecoveryWindowInDays")
        self._CleanSSHKey = params.get("CleanSSHKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecretResponse(AbstractModel):
    """DeleteSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定删除的凭据名称。
        :type SecretName: str
        :param _DeleteTime: 凭据删除的日期，unix时间戳。
        :type DeleteTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._DeleteTime = None
        self._RequestId = None

    @property
    def SecretName(self):
        """指定删除的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def DeleteTime(self):
        """凭据删除的日期，unix时间戳。
        :rtype: int
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

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
        self._SecretName = params.get("SecretName")
        self._DeleteTime = params.get("DeleteTime")
        self._RequestId = params.get("RequestId")


class DeleteSecretVersionRequest(AbstractModel):
    """DeleteSecretVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定凭据名称。
        :type SecretName: str
        :param _VersionId: 指定该名称下需要删除的凭据的版本号。
        :type VersionId: str
        """
        self._SecretName = None
        self._VersionId = None

    @property
    def SecretName(self):
        """指定凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """指定该名称下需要删除的凭据的版本号。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecretVersionResponse(AbstractModel):
    """DeleteSecretVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称。
        :type SecretName: str
        :param _VersionId: 凭据版本号。
        :type VersionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._RequestId = None

    @property
    def SecretName(self):
        """凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """凭据版本号。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

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
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class DescribeAsyncRequestInfoRequest(AbstractModel):
    """DescribeAsyncRequestInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowID: 异步任务ID号
        :type FlowID: int
        """
        self._FlowID = None

    @property
    def FlowID(self):
        """异步任务ID号
        :rtype: int
        """
        return self._FlowID

    @FlowID.setter
    def FlowID(self, FlowID):
        self._FlowID = FlowID


    def _deserialize(self, params):
        self._FlowID = params.get("FlowID")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncRequestInfoResponse(AbstractModel):
    """DescribeAsyncRequestInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 0:处理中，1:处理成功，2:处理失败
        :type TaskStatus: int
        :param _Description: 任务描述信息。
        :type Description: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatus = None
        self._Description = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        """0:处理中，1:处理成功，2:处理失败
        :rtype: int
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def Description(self):
        """任务描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

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
        self._TaskStatus = params.get("TaskStatus")
        self._Description = params.get("Description")
        self._RequestId = params.get("RequestId")


class DescribeRotationDetailRequest(AbstractModel):
    """DescribeRotationDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定需要获取凭据轮转详细信息的凭据名称。
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """指定需要获取凭据轮转详细信息的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRotationDetailResponse(AbstractModel):
    """DescribeRotationDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnableRotation: 否允许轮转，true表示开启轮转，false表示禁止轮转。
        :type EnableRotation: bool
        :param _Frequency: 轮转的频率，以天为单位，默认为1天。
        :type Frequency: int
        :param _LatestRotateTime: 最近一次轮转的时间，显式可见的时间字符串，格式 2006-01-02 15:04:05。
        :type LatestRotateTime: str
        :param _NextRotateBeginTime: 下一次开始轮转的时间，显式可见的时间字符串，格式 2006-01-02 15:04:05。
        :type NextRotateBeginTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnableRotation = None
        self._Frequency = None
        self._LatestRotateTime = None
        self._NextRotateBeginTime = None
        self._RequestId = None

    @property
    def EnableRotation(self):
        """否允许轮转，true表示开启轮转，false表示禁止轮转。
        :rtype: bool
        """
        return self._EnableRotation

    @EnableRotation.setter
    def EnableRotation(self, EnableRotation):
        self._EnableRotation = EnableRotation

    @property
    def Frequency(self):
        """轮转的频率，以天为单位，默认为1天。
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def LatestRotateTime(self):
        """最近一次轮转的时间，显式可见的时间字符串，格式 2006-01-02 15:04:05。
        :rtype: str
        """
        return self._LatestRotateTime

    @LatestRotateTime.setter
    def LatestRotateTime(self, LatestRotateTime):
        self._LatestRotateTime = LatestRotateTime

    @property
    def NextRotateBeginTime(self):
        """下一次开始轮转的时间，显式可见的时间字符串，格式 2006-01-02 15:04:05。
        :rtype: str
        """
        return self._NextRotateBeginTime

    @NextRotateBeginTime.setter
    def NextRotateBeginTime(self, NextRotateBeginTime):
        self._NextRotateBeginTime = NextRotateBeginTime

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
        self._EnableRotation = params.get("EnableRotation")
        self._Frequency = params.get("Frequency")
        self._LatestRotateTime = params.get("LatestRotateTime")
        self._NextRotateBeginTime = params.get("NextRotateBeginTime")
        self._RequestId = params.get("RequestId")


class DescribeRotationHistoryRequest(AbstractModel):
    """DescribeRotationHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定需要获取凭据轮转历史的凭据名称。
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """指定需要获取凭据轮转历史的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRotationHistoryResponse(AbstractModel):
    """DescribeRotationHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionIDs: 版本号列表
        :type VersionIDs: list of str
        :param _TotalCount: 版本号个数，可以给用户展示的版本号个数上限为10个。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionIDs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def VersionIDs(self):
        """版本号列表
        :rtype: list of str
        """
        return self._VersionIDs

    @VersionIDs.setter
    def VersionIDs(self, VersionIDs):
        self._VersionIDs = VersionIDs

    @property
    def TotalCount(self):
        """版本号个数，可以给用户展示的版本号个数上限为10个。
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
        self._VersionIDs = params.get("VersionIDs")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecretRequest(AbstractModel):
    """DescribeSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定需要获取凭据详细信息的凭据名称。
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """指定需要获取凭据详细信息的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecretResponse(AbstractModel):
    """DescribeSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称。
        :type SecretName: str
        :param _Description: 凭据描述信息。
        :type Description: str
        :param _KmsKeyId: 用于加密的KMS CMK ID。
        :type KmsKeyId: str
        :param _CreateUin: 创建者UIN。
        :type CreateUin: int
        :param _Status: 凭据状态：Enabled、Disabled、PendingDelete, Creating, Failed。
        :type Status: str
        :param _DeleteTime: 删除日期，uinx 时间戳，非计划删除状态的凭据为0。
        :type DeleteTime: int
        :param _CreateTime: 创建日期。
        :type CreateTime: int
        :param _SecretType: 0 --  用户自定义凭据类型；1 -- 数据库凭据类型；2 -- SSH密钥对凭据类型；3 -- 云API密钥（AKSK）凭据类型（使用此功能需要联系云助手单独开启白名单）；4 -- Redis类型凭据。
        :type SecretType: int
        :param _ProductName: 云产品名称。
        :type ProductName: str
        :param _ResourceID: 云产品实例ID。
        :type ResourceID: str
        :param _RotationStatus: 是否开启轮转：True -- 开启轮转；False -- 关闭轮转。
        :type RotationStatus: bool
        :param _RotationFrequency: 轮转周期，默认以天为单位。
        :type RotationFrequency: int
        :param _ResourceName: 当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对凭据的名称。
        :type ResourceName: str
        :param _ProjectID: 当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对所属的项目ID。
        :type ProjectID: int
        :param _AssociatedInstanceIDs: 当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对所关联的CVM实例ID。
        :type AssociatedInstanceIDs: list of str
        :param _TargetUin: 当凭据类型为云API密钥对凭据时，此字段有效，用于表示此云API密钥对所属的用户UIN。
        :type TargetUin: int
        :param _AdditionalConfig: 凭据额外配置
        :type AdditionalConfig: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._Description = None
        self._KmsKeyId = None
        self._CreateUin = None
        self._Status = None
        self._DeleteTime = None
        self._CreateTime = None
        self._SecretType = None
        self._ProductName = None
        self._ResourceID = None
        self._RotationStatus = None
        self._RotationFrequency = None
        self._ResourceName = None
        self._ProjectID = None
        self._AssociatedInstanceIDs = None
        self._TargetUin = None
        self._AdditionalConfig = None
        self._RequestId = None

    @property
    def SecretName(self):
        """凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Description(self):
        """凭据描述信息。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """用于加密的KMS CMK ID。
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def CreateUin(self):
        """创建者UIN。
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Status(self):
        """凭据状态：Enabled、Disabled、PendingDelete, Creating, Failed。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeleteTime(self):
        """删除日期，uinx 时间戳，非计划删除状态的凭据为0。
        :rtype: int
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def CreateTime(self):
        """创建日期。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecretType(self):
        """0 --  用户自定义凭据类型；1 -- 数据库凭据类型；2 -- SSH密钥对凭据类型；3 -- 云API密钥（AKSK）凭据类型（使用此功能需要联系云助手单独开启白名单）；4 -- Redis类型凭据。
        :rtype: int
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def ProductName(self):
        """云产品名称。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ResourceID(self):
        """云产品实例ID。
        :rtype: str
        """
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID

    @property
    def RotationStatus(self):
        """是否开启轮转：True -- 开启轮转；False -- 关闭轮转。
        :rtype: bool
        """
        return self._RotationStatus

    @RotationStatus.setter
    def RotationStatus(self, RotationStatus):
        self._RotationStatus = RotationStatus

    @property
    def RotationFrequency(self):
        """轮转周期，默认以天为单位。
        :rtype: int
        """
        return self._RotationFrequency

    @RotationFrequency.setter
    def RotationFrequency(self, RotationFrequency):
        self._RotationFrequency = RotationFrequency

    @property
    def ResourceName(self):
        """当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对凭据的名称。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ProjectID(self):
        """当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对所属的项目ID。
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def AssociatedInstanceIDs(self):
        """当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对所关联的CVM实例ID。
        :rtype: list of str
        """
        return self._AssociatedInstanceIDs

    @AssociatedInstanceIDs.setter
    def AssociatedInstanceIDs(self, AssociatedInstanceIDs):
        self._AssociatedInstanceIDs = AssociatedInstanceIDs

    @property
    def TargetUin(self):
        """当凭据类型为云API密钥对凭据时，此字段有效，用于表示此云API密钥对所属的用户UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def AdditionalConfig(self):
        """凭据额外配置
        :rtype: str
        """
        return self._AdditionalConfig

    @AdditionalConfig.setter
    def AdditionalConfig(self, AdditionalConfig):
        self._AdditionalConfig = AdditionalConfig

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
        self._SecretName = params.get("SecretName")
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        self._CreateUin = params.get("CreateUin")
        self._Status = params.get("Status")
        self._DeleteTime = params.get("DeleteTime")
        self._CreateTime = params.get("CreateTime")
        self._SecretType = params.get("SecretType")
        self._ProductName = params.get("ProductName")
        self._ResourceID = params.get("ResourceID")
        self._RotationStatus = params.get("RotationStatus")
        self._RotationFrequency = params.get("RotationFrequency")
        self._ResourceName = params.get("ResourceName")
        self._ProjectID = params.get("ProjectID")
        self._AssociatedInstanceIDs = params.get("AssociatedInstanceIDs")
        self._TargetUin = params.get("TargetUin")
        self._AdditionalConfig = params.get("AdditionalConfig")
        self._RequestId = params.get("RequestId")


class DescribeSupportedProductsRequest(AbstractModel):
    """DescribeSupportedProducts请求参数结构体

    """


class DescribeSupportedProductsResponse(AbstractModel):
    """DescribeSupportedProducts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 支持的所有云产品列表。
每种云产品与凭据类型的对应关系如下：
当SecretType为1时，支持的云产品列表包括：Mysql、Tdsql-mysql、Tdsql_C_Mysql；
当SecretType为2时，支持的产品列表为：Cvm；
当SecretType为3时，支持的产品列表为：Cam（此功能的使用需要联系云助手单独开始白名单）；
当SecretType为4时，支持的产品列表为：Redis。
        :type Products: list of str
        :param _TotalCount: 支持的产品个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Products = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Products(self):
        """支持的所有云产品列表。
每种云产品与凭据类型的对应关系如下：
当SecretType为1时，支持的云产品列表包括：Mysql、Tdsql-mysql、Tdsql_C_Mysql；
当SecretType为2时，支持的产品列表为：Cvm；
当SecretType为3时，支持的产品列表为：Cam（此功能的使用需要联系云助手单独开始白名单）；
当SecretType为4时，支持的产品列表为：Redis。
        :rtype: list of str
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def TotalCount(self):
        """支持的产品个数
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
        self._Products = params.get("Products")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DisableSecretRequest(AbstractModel):
    """DisableSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定停用的凭据名称。
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """指定停用的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableSecretResponse(AbstractModel):
    """DisableSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 停用的凭据名称。
        :type SecretName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._RequestId = None

    @property
    def SecretName(self):
        """停用的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

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
        self._SecretName = params.get("SecretName")
        self._RequestId = params.get("RequestId")


class EnableSecretRequest(AbstractModel):
    """EnableSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定启用凭据的名称。
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """指定启用凭据的名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableSecretResponse(AbstractModel):
    """EnableSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 启用的凭据名称。
        :type SecretName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._RequestId = None

    @property
    def SecretName(self):
        """启用的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

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
        self._SecretName = params.get("SecretName")
        self._RequestId = params.get("RequestId")


class GetRegionsRequest(AbstractModel):
    """GetRegions请求参数结构体

    """


class GetRegionsResponse(AbstractModel):
    """GetRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Regions: region列表。
        :type Regions: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Regions = None
        self._RequestId = None

    @property
    def Regions(self):
        """region列表。
        :rtype: list of str
        """
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

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
        self._Regions = params.get("Regions")
        self._RequestId = params.get("RequestId")


class GetSSHKeyPairValueRequest(AbstractModel):
    """GetSSHKeyPairValue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称，此凭据只能为SSH密钥对凭据类型。
        :type SecretName: str
        :param _SSHKeyId: 密钥对ID，是云服务器中密钥对的唯一标识。
        :type SSHKeyId: str
        """
        self._SecretName = None
        self._SSHKeyId = None

    @property
    def SecretName(self):
        """凭据名称，此凭据只能为SSH密钥对凭据类型。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def SSHKeyId(self):
        """密钥对ID，是云服务器中密钥对的唯一标识。
        :rtype: str
        """
        return self._SSHKeyId

    @SSHKeyId.setter
    def SSHKeyId(self, SSHKeyId):
        self._SSHKeyId = SSHKeyId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._SSHKeyId = params.get("SSHKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSSHKeyPairValueResponse(AbstractModel):
    """GetSSHKeyPairValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SSHKeyID: SSH密钥对ID。
        :type SSHKeyID: str
        :param _PublicKey: 公钥明文，使用base64编码。
        :type PublicKey: str
        :param _PrivateKey: 私钥明文，使用base64编码
        :type PrivateKey: str
        :param _ProjectID: 此密钥对所属的项目ID。
        :type ProjectID: int
        :param _SSHKeyDescription: SSH密钥对的描述信息。
用户可以在CVM侧控制台对密钥对的描述信息进行修改。
        :type SSHKeyDescription: str
        :param _SSHKeyName: SSH密钥对的名称。
用户可以在CVM侧控制台对密钥对的名称进行修改。
        :type SSHKeyName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SSHKeyID = None
        self._PublicKey = None
        self._PrivateKey = None
        self._ProjectID = None
        self._SSHKeyDescription = None
        self._SSHKeyName = None
        self._RequestId = None

    @property
    def SSHKeyID(self):
        """SSH密钥对ID。
        :rtype: str
        """
        return self._SSHKeyID

    @SSHKeyID.setter
    def SSHKeyID(self, SSHKeyID):
        self._SSHKeyID = SSHKeyID

    @property
    def PublicKey(self):
        """公钥明文，使用base64编码。
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def PrivateKey(self):
        """私钥明文，使用base64编码
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def ProjectID(self):
        """此密钥对所属的项目ID。
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def SSHKeyDescription(self):
        """SSH密钥对的描述信息。
用户可以在CVM侧控制台对密钥对的描述信息进行修改。
        :rtype: str
        """
        return self._SSHKeyDescription

    @SSHKeyDescription.setter
    def SSHKeyDescription(self, SSHKeyDescription):
        self._SSHKeyDescription = SSHKeyDescription

    @property
    def SSHKeyName(self):
        """SSH密钥对的名称。
用户可以在CVM侧控制台对密钥对的名称进行修改。
        :rtype: str
        """
        return self._SSHKeyName

    @SSHKeyName.setter
    def SSHKeyName(self, SSHKeyName):
        self._SSHKeyName = SSHKeyName

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
        self._SSHKeyID = params.get("SSHKeyID")
        self._PublicKey = params.get("PublicKey")
        self._PrivateKey = params.get("PrivateKey")
        self._ProjectID = params.get("ProjectID")
        self._SSHKeyDescription = params.get("SSHKeyDescription")
        self._SSHKeyName = params.get("SSHKeyName")
        self._RequestId = params.get("RequestId")


class GetSecretValueRequest(AbstractModel):
    """GetSecretValue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定凭据的名称。
        :type SecretName: str
        :param _VersionId: 指定对应凭据的版本号。
对于云产品凭据如Mysql凭据，通过指定凭据名称和历史版本号来获取历史轮转凭据的明文信息，如果要获取当前正在使用的凭据版本的明文，需要将版本号指定为：SSM_Current。
        :type VersionId: str
        """
        self._SecretName = None
        self._VersionId = None

    @property
    def SecretName(self):
        """指定凭据的名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """指定对应凭据的版本号。
对于云产品凭据如Mysql凭据，通过指定凭据名称和历史版本号来获取历史轮转凭据的明文信息，如果要获取当前正在使用的凭据版本的明文，需要将版本号指定为：SSM_Current。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSecretValueResponse(AbstractModel):
    """GetSecretValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据的名称。
        :type SecretName: str
        :param _VersionId: 该凭据对应的版本号。
        :type VersionId: str
        :param _SecretBinary: 在创建凭据(CreateSecret)时，如果指定的是二进制数据，则该字段为返回结果，并且使用base64进行编码，应用方需要进行base64解码后获取原始数据。
SecretBinary和SecretString只有一个不为空。
        :type SecretBinary: str
        :param _SecretString: 在创建凭据(CreateSecret)时，如果指定的是普通文本数据，则该字段为返回结果。
SecretBinary和SecretString只有一个不为空。
        :type SecretString: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._SecretBinary = None
        self._SecretString = None
        self._RequestId = None

    @property
    def SecretName(self):
        """凭据的名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """该凭据对应的版本号。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def SecretBinary(self):
        """在创建凭据(CreateSecret)时，如果指定的是二进制数据，则该字段为返回结果，并且使用base64进行编码，应用方需要进行base64解码后获取原始数据。
SecretBinary和SecretString只有一个不为空。
        :rtype: str
        """
        return self._SecretBinary

    @SecretBinary.setter
    def SecretBinary(self, SecretBinary):
        self._SecretBinary = SecretBinary

    @property
    def SecretString(self):
        """在创建凭据(CreateSecret)时，如果指定的是普通文本数据，则该字段为返回结果。
SecretBinary和SecretString只有一个不为空。
        :rtype: str
        """
        return self._SecretString

    @SecretString.setter
    def SecretString(self, SecretString):
        self._SecretString = SecretString

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
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._SecretBinary = params.get("SecretBinary")
        self._SecretString = params.get("SecretString")
        self._RequestId = params.get("RequestId")


class GetServiceStatusRequest(AbstractModel):
    """GetServiceStatus请求参数结构体

    """


class GetServiceStatusResponse(AbstractModel):
    """GetServiceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceEnabled: true表示服务已开通，false 表示服务尚未开通。
        :type ServiceEnabled: bool
        :param _InvalidType: 服务不可用类型： 0-未购买，1-正常， 2-欠费停服， 3-资源释放。
        :type InvalidType: int
        :param _AccessKeyEscrowEnabled: true表示用户已经可以使用密钥安全托管功能，
false表示用户暂时不能使用密钥安全托管功能。
        :type AccessKeyEscrowEnabled: bool
        :param _ExpireTime: 过期时间
        :type ExpireTime: str
        :param _QPSLimit: 计算性能限制
        :type QPSLimit: int
        :param _SecretLimit: 凭据个数限制
        :type SecretLimit: int
        :param _PayModel: 付费模式
        :type PayModel: str
        :param _RenewFlag: 自动续费标识，0:手动续费 1:自动续费 2:到期不续
        :type RenewFlag: int
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _TotalCount: 已托管凭据个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceEnabled = None
        self._InvalidType = None
        self._AccessKeyEscrowEnabled = None
        self._ExpireTime = None
        self._QPSLimit = None
        self._SecretLimit = None
        self._PayModel = None
        self._RenewFlag = None
        self._ResourceId = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ServiceEnabled(self):
        """true表示服务已开通，false 表示服务尚未开通。
        :rtype: bool
        """
        return self._ServiceEnabled

    @ServiceEnabled.setter
    def ServiceEnabled(self, ServiceEnabled):
        self._ServiceEnabled = ServiceEnabled

    @property
    def InvalidType(self):
        """服务不可用类型： 0-未购买，1-正常， 2-欠费停服， 3-资源释放。
        :rtype: int
        """
        return self._InvalidType

    @InvalidType.setter
    def InvalidType(self, InvalidType):
        self._InvalidType = InvalidType

    @property
    def AccessKeyEscrowEnabled(self):
        """true表示用户已经可以使用密钥安全托管功能，
false表示用户暂时不能使用密钥安全托管功能。
        :rtype: bool
        """
        return self._AccessKeyEscrowEnabled

    @AccessKeyEscrowEnabled.setter
    def AccessKeyEscrowEnabled(self, AccessKeyEscrowEnabled):
        self._AccessKeyEscrowEnabled = AccessKeyEscrowEnabled

    @property
    def ExpireTime(self):
        """过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def QPSLimit(self):
        """计算性能限制
        :rtype: int
        """
        return self._QPSLimit

    @QPSLimit.setter
    def QPSLimit(self, QPSLimit):
        self._QPSLimit = QPSLimit

    @property
    def SecretLimit(self):
        """凭据个数限制
        :rtype: int
        """
        return self._SecretLimit

    @SecretLimit.setter
    def SecretLimit(self, SecretLimit):
        self._SecretLimit = SecretLimit

    @property
    def PayModel(self):
        """付费模式
        :rtype: str
        """
        return self._PayModel

    @PayModel.setter
    def PayModel(self, PayModel):
        self._PayModel = PayModel

    @property
    def RenewFlag(self):
        """自动续费标识，0:手动续费 1:自动续费 2:到期不续
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ResourceId(self):
        """资源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def TotalCount(self):
        """已托管凭据个数
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
        self._ServiceEnabled = params.get("ServiceEnabled")
        self._InvalidType = params.get("InvalidType")
        self._AccessKeyEscrowEnabled = params.get("AccessKeyEscrowEnabled")
        self._ExpireTime = params.get("ExpireTime")
        self._QPSLimit = params.get("QPSLimit")
        self._SecretLimit = params.get("SecretLimit")
        self._PayModel = params.get("PayModel")
        self._RenewFlag = params.get("RenewFlag")
        self._ResourceId = params.get("ResourceId")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListSecretVersionIdsRequest(AbstractModel):
    """ListSecretVersionIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """凭据名称
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSecretVersionIdsResponse(AbstractModel):
    """ListSecretVersionIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称。
        :type SecretName: str
        :param _Versions: VersionId列表。
        :type Versions: list of VersionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._Versions = None
        self._RequestId = None

    @property
    def SecretName(self):
        """凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Versions(self):
        """VersionId列表。
        :rtype: list of VersionInfo
        """
        return self._Versions

    @Versions.setter
    def Versions(self, Versions):
        self._Versions = Versions

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
        self._SecretName = params.get("SecretName")
        if params.get("Versions") is not None:
            self._Versions = []
            for item in params.get("Versions"):
                obj = VersionInfo()
                obj._deserialize(item)
                self._Versions.append(obj)
        self._RequestId = params.get("RequestId")


class ListSecretsRequest(AbstractModel):
    """ListSecrets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 查询列表的起始位置，以0开始，不设置默认为0。
        :type Offset: int
        :param _Limit: 单次查询返回的最大数量，0或不设置则使用默认值 20。
        :type Limit: int
        :param _OrderType: 根据创建时间的排序方式，0或者不设置则使用降序排序， 1 表示升序排序。
        :type OrderType: int
        :param _State: 根据凭据状态进行过滤。
默认为0表示查询全部。
1 --  表示查询Enabled 凭据列表。
2 --  表示查询Disabled 凭据列表。
3 --  表示查询PendingDelete 凭据列表。
4 --  表示PendingCreate。
5 --  表示CreateFailed。
其中状态PendingCreate和CreateFailed只有在SecretType为云产品凭据时生效
        :type State: int
        :param _SearchSecretName: 根据凭据名称进行过滤，为空表示不过滤。
        :type SearchSecretName: str
        :param _TagFilters: 标签过滤条件。
        :type TagFilters: list of TagFilter
        :param _SecretType: 0  -- 表示用户自定义凭据，默认为0。
1  -- 表示用户云产品凭据。
2 -- 表示SSH密钥对凭据。
3 -- 表示云API密钥对凭据。
        :type SecretType: int
        :param _ProductName: 此参数仅在SecretType参数值为1时生效，
当SecretType值为1时：
如果ProductName值为空，则表示查询所有类型的云产品凭据；
如果ProductName值为某个指定的云产品值如Mysql时，则表示查询Mysql数据库凭据；
如果ProductName值为多个云产品值，如：Mysql,Tdsql-mysql,Tdsql_C_Mysql（多个值以英文逗号,分隔开）则表示查询三种云产品类型的凭据；
支持的云产品列表请通过接口：DescribeSupportedProducts进行查询。
        :type ProductName: str
        """
        self._Offset = None
        self._Limit = None
        self._OrderType = None
        self._State = None
        self._SearchSecretName = None
        self._TagFilters = None
        self._SecretType = None
        self._ProductName = None

    @property
    def Offset(self):
        """查询列表的起始位置，以0开始，不设置默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """单次查询返回的最大数量，0或不设置则使用默认值 20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def OrderType(self):
        """根据创建时间的排序方式，0或者不设置则使用降序排序， 1 表示升序排序。
        :rtype: int
        """
        return self._OrderType

    @OrderType.setter
    def OrderType(self, OrderType):
        self._OrderType = OrderType

    @property
    def State(self):
        """根据凭据状态进行过滤。
默认为0表示查询全部。
1 --  表示查询Enabled 凭据列表。
2 --  表示查询Disabled 凭据列表。
3 --  表示查询PendingDelete 凭据列表。
4 --  表示PendingCreate。
5 --  表示CreateFailed。
其中状态PendingCreate和CreateFailed只有在SecretType为云产品凭据时生效
        :rtype: int
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def SearchSecretName(self):
        """根据凭据名称进行过滤，为空表示不过滤。
        :rtype: str
        """
        return self._SearchSecretName

    @SearchSecretName.setter
    def SearchSecretName(self, SearchSecretName):
        self._SearchSecretName = SearchSecretName

    @property
    def TagFilters(self):
        """标签过滤条件。
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def SecretType(self):
        """0  -- 表示用户自定义凭据，默认为0。
1  -- 表示用户云产品凭据。
2 -- 表示SSH密钥对凭据。
3 -- 表示云API密钥对凭据。
        :rtype: int
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def ProductName(self):
        """此参数仅在SecretType参数值为1时生效，
当SecretType值为1时：
如果ProductName值为空，则表示查询所有类型的云产品凭据；
如果ProductName值为某个指定的云产品值如Mysql时，则表示查询Mysql数据库凭据；
如果ProductName值为多个云产品值，如：Mysql,Tdsql-mysql,Tdsql_C_Mysql（多个值以英文逗号,分隔开）则表示查询三种云产品类型的凭据；
支持的云产品列表请通过接口：DescribeSupportedProducts进行查询。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._OrderType = params.get("OrderType")
        self._State = params.get("State")
        self._SearchSecretName = params.get("SearchSecretName")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._SecretType = params.get("SecretType")
        self._ProductName = params.get("ProductName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSecretsResponse(AbstractModel):
    """ListSecrets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 根据State和SearchSecretName 筛选的凭据总数。
        :type TotalCount: int
        :param _SecretMetadatas: 返回凭据信息列表。
        :type SecretMetadatas: list of SecretMetadata
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SecretMetadatas = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """根据State和SearchSecretName 筛选的凭据总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SecretMetadatas(self):
        """返回凭据信息列表。
        :rtype: list of SecretMetadata
        """
        return self._SecretMetadatas

    @SecretMetadatas.setter
    def SecretMetadatas(self, SecretMetadatas):
        self._SecretMetadatas = SecretMetadatas

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
        self._TotalCount = params.get("TotalCount")
        if params.get("SecretMetadatas") is not None:
            self._SecretMetadatas = []
            for item in params.get("SecretMetadatas"):
                obj = SecretMetadata()
                obj._deserialize(item)
                self._SecretMetadatas.append(obj)
        self._RequestId = params.get("RequestId")


class ProductPrivilegeUnit(AbstractModel):
    """凭据关联产品时被赋予的权限

    """

    def __init__(self):
        r"""
        :param _PrivilegeName: 权限名称，当前可选：
GlobalPrivileges
DatabasePrivileges
TablePrivileges
ColumnPrivileges

当权限为DatabasePrivileges时，必须通过参数Database指定数据库名；

当权限为TablePrivileges时，必须通过参数Database和TableName指定数据库名以及数据库中的表名；

当权限为ColumnPrivileges时，必须通过参数Database、TableName和CoulmnName指定数据库、数据库中的表名以及表中的列名。
        :type PrivilegeName: str
        :param _Privileges: 权限列表。
对于Mysql产品来说，可选权限值为：

1. GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示清除该权限。

2. DatabasePrivileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示清除该权限。

3. TablePrivileges 权限的可选值为：权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示清除该权限。

4. ColumnPrivileges 权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
注意，不传该参数表示清除该权限。
        :type Privileges: list of str
        :param _Database: 仅当PrivilegeName为DatabasePrivileges时这个值才有效。
        :type Database: str
        :param _TableName: 仅当PrivilegeName为TablePrivileges时这个值才有效，并且此时需要填充Database显式指明所在的数据库实例。
        :type TableName: str
        :param _ColumnName: 仅当PrivilegeName为ColumnPrivileges时这个值才生效，并且此时必须填充：
Database - 显式指明所在的数据库实例。
TableName - 显式指明所在表
        :type ColumnName: str
        """
        self._PrivilegeName = None
        self._Privileges = None
        self._Database = None
        self._TableName = None
        self._ColumnName = None

    @property
    def PrivilegeName(self):
        """权限名称，当前可选：
GlobalPrivileges
DatabasePrivileges
TablePrivileges
ColumnPrivileges

当权限为DatabasePrivileges时，必须通过参数Database指定数据库名；

当权限为TablePrivileges时，必须通过参数Database和TableName指定数据库名以及数据库中的表名；

当权限为ColumnPrivileges时，必须通过参数Database、TableName和CoulmnName指定数据库、数据库中的表名以及表中的列名。
        :rtype: str
        """
        return self._PrivilegeName

    @PrivilegeName.setter
    def PrivilegeName(self, PrivilegeName):
        self._PrivilegeName = PrivilegeName

    @property
    def Privileges(self):
        """权限列表。
对于Mysql产品来说，可选权限值为：

1. GlobalPrivileges 中权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "PROCESS", "DROP","REFERENCES","INDEX","ALTER","SHOW DATABASES","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示清除该权限。

2. DatabasePrivileges 权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE TEMPORARY TABLES","LOCK TABLES","EXECUTE","CREATE VIEW","SHOW VIEW","CREATE ROUTINE","ALTER ROUTINE","EVENT","TRIGGER"。
注意，不传该参数表示清除该权限。

3. TablePrivileges 权限的可选值为：权限的可选值为："SELECT","INSERT","UPDATE","DELETE","CREATE", "DROP","REFERENCES","INDEX","ALTER","CREATE VIEW","SHOW VIEW", "TRIGGER"。
注意，不传该参数表示清除该权限。

4. ColumnPrivileges 权限的可选值为："SELECT","INSERT","UPDATE","REFERENCES"。
注意，不传该参数表示清除该权限。
        :rtype: list of str
        """
        return self._Privileges

    @Privileges.setter
    def Privileges(self, Privileges):
        self._Privileges = Privileges

    @property
    def Database(self):
        """仅当PrivilegeName为DatabasePrivileges时这个值才有效。
        :rtype: str
        """
        return self._Database

    @Database.setter
    def Database(self, Database):
        self._Database = Database

    @property
    def TableName(self):
        """仅当PrivilegeName为TablePrivileges时这个值才有效，并且此时需要填充Database显式指明所在的数据库实例。
        :rtype: str
        """
        return self._TableName

    @TableName.setter
    def TableName(self, TableName):
        self._TableName = TableName

    @property
    def ColumnName(self):
        """仅当PrivilegeName为ColumnPrivileges时这个值才生效，并且此时必须填充：
Database - 显式指明所在的数据库实例。
TableName - 显式指明所在表
        :rtype: str
        """
        return self._ColumnName

    @ColumnName.setter
    def ColumnName(self, ColumnName):
        self._ColumnName = ColumnName


    def _deserialize(self, params):
        self._PrivilegeName = params.get("PrivilegeName")
        self._Privileges = params.get("Privileges")
        self._Database = params.get("Database")
        self._TableName = params.get("TableName")
        self._ColumnName = params.get("ColumnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutSecretValueRequest(AbstractModel):
    """PutSecretValue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定需要增加版本的凭据名称。
        :type SecretName: str
        :param _VersionId: 指定新增加的版本号，最长64 字节，使用字母、数字或者 - _ . 的组合并且以字母或数字开头。
        :type VersionId: str
        :param _SecretBinary: 二进制凭据信息，使用base64编码。
SecretBinary 和 SecretString 必须且只能设置一个。
        :type SecretBinary: str
        :param _SecretString: 文本类型凭据信息明文（不需要进行base64编码），SecretBinary 和 SecretString 必须且只能设置一个。
        :type SecretString: str
        """
        self._SecretName = None
        self._VersionId = None
        self._SecretBinary = None
        self._SecretString = None

    @property
    def SecretName(self):
        """指定需要增加版本的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """指定新增加的版本号，最长64 字节，使用字母、数字或者 - _ . 的组合并且以字母或数字开头。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def SecretBinary(self):
        """二进制凭据信息，使用base64编码。
SecretBinary 和 SecretString 必须且只能设置一个。
        :rtype: str
        """
        return self._SecretBinary

    @SecretBinary.setter
    def SecretBinary(self, SecretBinary):
        self._SecretBinary = SecretBinary

    @property
    def SecretString(self):
        """文本类型凭据信息明文（不需要进行base64编码），SecretBinary 和 SecretString 必须且只能设置一个。
        :rtype: str
        """
        return self._SecretString

    @SecretString.setter
    def SecretString(self, SecretString):
        self._SecretString = SecretString


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._SecretBinary = params.get("SecretBinary")
        self._SecretString = params.get("SecretString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutSecretValueResponse(AbstractModel):
    """PutSecretValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称。
        :type SecretName: str
        :param _VersionId: 新增加的版本号。
        :type VersionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._RequestId = None

    @property
    def SecretName(self):
        """凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """新增加的版本号。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

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
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class RestoreSecretRequest(AbstractModel):
    """RestoreSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定需要恢复的凭据名称。
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """指定需要恢复的凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RestoreSecretResponse(AbstractModel):
    """RestoreSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称。
        :type SecretName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._RequestId = None

    @property
    def SecretName(self):
        """凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

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
        self._SecretName = params.get("SecretName")
        self._RequestId = params.get("RequestId")


class RotateProductSecretRequest(AbstractModel):
    """RotateProductSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 需要轮转的凭据名。
        :type SecretName: str
        """
        self._SecretName = None

    @property
    def SecretName(self):
        """需要轮转的凭据名。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RotateProductSecretResponse(AbstractModel):
    """RotateProductSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FlowID: 当凭据类型为云产品凭据时（即SecretType为1，如MySQL、Tdsql等托管凭据）此字段有效，返回轮转异步任务ID号。
        :type FlowID: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FlowID = None
        self._RequestId = None

    @property
    def FlowID(self):
        """当凭据类型为云产品凭据时（即SecretType为1，如MySQL、Tdsql等托管凭据）此字段有效，返回轮转异步任务ID号。
        :rtype: int
        """
        return self._FlowID

    @FlowID.setter
    def FlowID(self, FlowID):
        self._FlowID = FlowID

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
        self._FlowID = params.get("FlowID")
        self._RequestId = params.get("RequestId")


class SecretMetadata(AbstractModel):
    """凭据的基础信息

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称
        :type SecretName: str
        :param _Description: 凭据的描述信息
        :type Description: str
        :param _KmsKeyId: 用于加密凭据的KMS KeyId
        :type KmsKeyId: str
        :param _CreateUin: 创建者UIN
        :type CreateUin: int
        :param _Status: 凭据状态：Enabled、Disabled、PendingDelete、Creating、Failed
        :type Status: str
        :param _DeleteTime: 凭据删除日期，对于status为PendingDelete 的有效，unix时间戳
        :type DeleteTime: int
        :param _CreateTime: 凭据创建时间，unix时间戳
        :type CreateTime: int
        :param _KmsKeyType: 用于加密凭据的KMS CMK类型，DEFAULT 表示SecretsManager 创建的默认密钥， CUSTOMER 表示用户指定的密钥
        :type KmsKeyType: str
        :param _RotationStatus: 1:--开启轮转；0--禁止轮转
        :type RotationStatus: int
        :param _NextRotationTime: 下一次轮转开始时间，uinx 时间戳
        :type NextRotationTime: int
        :param _SecretType: 0 -- 用户自定义凭据；
1 -- 云产品凭据；
2 -- SSH密钥对凭据；
3 -- 云API密钥对凭据；
4 -- Redis类型凭据；
        :type SecretType: int
        :param _ProductName: 云产品名称，仅在SecretType为1，即凭据类型为云产品凭据时生效
        :type ProductName: str
        :param _ResourceName: 当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对凭据的名称。
        :type ResourceName: str
        :param _ProjectID: 当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对所属的项目ID。
        :type ProjectID: int
        :param _AssociatedInstanceIDs: 当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对所关联的CVM实例ID。
        :type AssociatedInstanceIDs: list of str
        :param _TargetUin: 当凭据类型为云API密钥对凭据时，此字段有效，用于表示云API密钥对所属的用户UIN。
        :type TargetUin: int
        :param _RotationFrequency: 轮转的频率，以天作为单位，在轮转开启状态下生效。
        :type RotationFrequency: int
        :param _ResourceID: 云产品凭据对应的云产品实例 ID 号。
        :type ResourceID: str
        :param _RotationBeginTime: 用户指定的轮转开始时间。
        :type RotationBeginTime: str
        """
        self._SecretName = None
        self._Description = None
        self._KmsKeyId = None
        self._CreateUin = None
        self._Status = None
        self._DeleteTime = None
        self._CreateTime = None
        self._KmsKeyType = None
        self._RotationStatus = None
        self._NextRotationTime = None
        self._SecretType = None
        self._ProductName = None
        self._ResourceName = None
        self._ProjectID = None
        self._AssociatedInstanceIDs = None
        self._TargetUin = None
        self._RotationFrequency = None
        self._ResourceID = None
        self._RotationBeginTime = None

    @property
    def SecretName(self):
        """凭据名称
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Description(self):
        """凭据的描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def KmsKeyId(self):
        """用于加密凭据的KMS KeyId
        :rtype: str
        """
        return self._KmsKeyId

    @KmsKeyId.setter
    def KmsKeyId(self, KmsKeyId):
        self._KmsKeyId = KmsKeyId

    @property
    def CreateUin(self):
        """创建者UIN
        :rtype: int
        """
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Status(self):
        """凭据状态：Enabled、Disabled、PendingDelete、Creating、Failed
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DeleteTime(self):
        """凭据删除日期，对于status为PendingDelete 的有效，unix时间戳
        :rtype: int
        """
        return self._DeleteTime

    @DeleteTime.setter
    def DeleteTime(self, DeleteTime):
        self._DeleteTime = DeleteTime

    @property
    def CreateTime(self):
        """凭据创建时间，unix时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def KmsKeyType(self):
        """用于加密凭据的KMS CMK类型，DEFAULT 表示SecretsManager 创建的默认密钥， CUSTOMER 表示用户指定的密钥
        :rtype: str
        """
        return self._KmsKeyType

    @KmsKeyType.setter
    def KmsKeyType(self, KmsKeyType):
        self._KmsKeyType = KmsKeyType

    @property
    def RotationStatus(self):
        """1:--开启轮转；0--禁止轮转
        :rtype: int
        """
        return self._RotationStatus

    @RotationStatus.setter
    def RotationStatus(self, RotationStatus):
        self._RotationStatus = RotationStatus

    @property
    def NextRotationTime(self):
        """下一次轮转开始时间，uinx 时间戳
        :rtype: int
        """
        return self._NextRotationTime

    @NextRotationTime.setter
    def NextRotationTime(self, NextRotationTime):
        self._NextRotationTime = NextRotationTime

    @property
    def SecretType(self):
        """0 -- 用户自定义凭据；
1 -- 云产品凭据；
2 -- SSH密钥对凭据；
3 -- 云API密钥对凭据；
4 -- Redis类型凭据；
        :rtype: int
        """
        return self._SecretType

    @SecretType.setter
    def SecretType(self, SecretType):
        self._SecretType = SecretType

    @property
    def ProductName(self):
        """云产品名称，仅在SecretType为1，即凭据类型为云产品凭据时生效
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ResourceName(self):
        """当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对凭据的名称。
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ProjectID(self):
        """当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对所属的项目ID。
        :rtype: int
        """
        return self._ProjectID

    @ProjectID.setter
    def ProjectID(self, ProjectID):
        self._ProjectID = ProjectID

    @property
    def AssociatedInstanceIDs(self):
        """当凭据类型为SSH密钥对凭据时，此字段有效，用于表示SSH密钥对所关联的CVM实例ID。
        :rtype: list of str
        """
        return self._AssociatedInstanceIDs

    @AssociatedInstanceIDs.setter
    def AssociatedInstanceIDs(self, AssociatedInstanceIDs):
        self._AssociatedInstanceIDs = AssociatedInstanceIDs

    @property
    def TargetUin(self):
        """当凭据类型为云API密钥对凭据时，此字段有效，用于表示云API密钥对所属的用户UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def RotationFrequency(self):
        """轮转的频率，以天作为单位，在轮转开启状态下生效。
        :rtype: int
        """
        return self._RotationFrequency

    @RotationFrequency.setter
    def RotationFrequency(self, RotationFrequency):
        self._RotationFrequency = RotationFrequency

    @property
    def ResourceID(self):
        """云产品凭据对应的云产品实例 ID 号。
        :rtype: str
        """
        return self._ResourceID

    @ResourceID.setter
    def ResourceID(self, ResourceID):
        self._ResourceID = ResourceID

    @property
    def RotationBeginTime(self):
        """用户指定的轮转开始时间。
        :rtype: str
        """
        return self._RotationBeginTime

    @RotationBeginTime.setter
    def RotationBeginTime(self, RotationBeginTime):
        self._RotationBeginTime = RotationBeginTime


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._Description = params.get("Description")
        self._KmsKeyId = params.get("KmsKeyId")
        self._CreateUin = params.get("CreateUin")
        self._Status = params.get("Status")
        self._DeleteTime = params.get("DeleteTime")
        self._CreateTime = params.get("CreateTime")
        self._KmsKeyType = params.get("KmsKeyType")
        self._RotationStatus = params.get("RotationStatus")
        self._NextRotationTime = params.get("NextRotationTime")
        self._SecretType = params.get("SecretType")
        self._ProductName = params.get("ProductName")
        self._ResourceName = params.get("ResourceName")
        self._ProjectID = params.get("ProjectID")
        self._AssociatedInstanceIDs = params.get("AssociatedInstanceIDs")
        self._TargetUin = params.get("TargetUin")
        self._RotationFrequency = params.get("RotationFrequency")
        self._ResourceID = params.get("ResourceID")
        self._RotationBeginTime = params.get("RotationBeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
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
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: list of str
        """
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
        


class UpdateDescriptionRequest(AbstractModel):
    """UpdateDescription请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定需要更新描述信息的凭据名。
        :type SecretName: str
        :param _Description: 新的描述信息，最大长度2048个字节。
        :type Description: str
        """
        self._SecretName = None
        self._Description = None

    @property
    def SecretName(self):
        """指定需要更新描述信息的凭据名。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Description(self):
        """新的描述信息，最大长度2048个字节。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDescriptionResponse(AbstractModel):
    """UpdateDescription返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称。
        :type SecretName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._RequestId = None

    @property
    def SecretName(self):
        """凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

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
        self._SecretName = params.get("SecretName")
        self._RequestId = params.get("RequestId")


class UpdateRotationStatusRequest(AbstractModel):
    """UpdateRotationStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 云产品凭据名称。
        :type SecretName: str
        :param _EnableRotation: 是否开启轮转。
true -- 开启轮转；
false -- 禁止轮转。
        :type EnableRotation: bool
        :param _Frequency: 轮转周期，以天为单位，最小为30天，最大为365天。
        :type Frequency: int
        :param _RotationBeginTime: 用户设置的期望开始轮转时间，格式为：2006-01-02 15:04:05。
当EnableRotation为true时，如果不填RotationBeginTime，则默认填充为当前时间。
        :type RotationBeginTime: str
        """
        self._SecretName = None
        self._EnableRotation = None
        self._Frequency = None
        self._RotationBeginTime = None

    @property
    def SecretName(self):
        """云产品凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def EnableRotation(self):
        """是否开启轮转。
true -- 开启轮转；
false -- 禁止轮转。
        :rtype: bool
        """
        return self._EnableRotation

    @EnableRotation.setter
    def EnableRotation(self, EnableRotation):
        self._EnableRotation = EnableRotation

    @property
    def Frequency(self):
        """轮转周期，以天为单位，最小为30天，最大为365天。
        :rtype: int
        """
        return self._Frequency

    @Frequency.setter
    def Frequency(self, Frequency):
        self._Frequency = Frequency

    @property
    def RotationBeginTime(self):
        """用户设置的期望开始轮转时间，格式为：2006-01-02 15:04:05。
当EnableRotation为true时，如果不填RotationBeginTime，则默认填充为当前时间。
        :rtype: str
        """
        return self._RotationBeginTime

    @RotationBeginTime.setter
    def RotationBeginTime(self, RotationBeginTime):
        self._RotationBeginTime = RotationBeginTime


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._EnableRotation = params.get("EnableRotation")
        self._Frequency = params.get("Frequency")
        self._RotationBeginTime = params.get("RotationBeginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRotationStatusResponse(AbstractModel):
    """UpdateRotationStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateSecretRequest(AbstractModel):
    """UpdateSecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 指定需要更新凭据内容的名称。
        :type SecretName: str
        :param _VersionId: 指定需要更新凭据内容的版本号。
        :type VersionId: str
        :param _SecretBinary: 新的凭据内容为二进制的场景使用该字段，并使用base64进行编码。
SecretBinary 和 SecretString 只能一个不为空。
        :type SecretBinary: str
        :param _SecretString: 新的凭据内容为文本的场景使用该字段，不需要base64编码SecretBinary 和 SecretString 只能一个不为空。
        :type SecretString: str
        """
        self._SecretName = None
        self._VersionId = None
        self._SecretBinary = None
        self._SecretString = None

    @property
    def SecretName(self):
        """指定需要更新凭据内容的名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """指定需要更新凭据内容的版本号。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def SecretBinary(self):
        """新的凭据内容为二进制的场景使用该字段，并使用base64进行编码。
SecretBinary 和 SecretString 只能一个不为空。
        :rtype: str
        """
        return self._SecretBinary

    @SecretBinary.setter
    def SecretBinary(self, SecretBinary):
        self._SecretBinary = SecretBinary

    @property
    def SecretString(self):
        """新的凭据内容为文本的场景使用该字段，不需要base64编码SecretBinary 和 SecretString 只能一个不为空。
        :rtype: str
        """
        return self._SecretString

    @SecretString.setter
    def SecretString(self, SecretString):
        self._SecretString = SecretString


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._SecretBinary = params.get("SecretBinary")
        self._SecretString = params.get("SecretString")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSecretResponse(AbstractModel):
    """UpdateSecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 凭据名称。
        :type SecretName: str
        :param _VersionId: 凭据版本号。
        :type VersionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecretName = None
        self._VersionId = None
        self._RequestId = None

    @property
    def SecretName(self):
        """凭据名称。
        :rtype: str
        """
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def VersionId(self):
        """凭据版本号。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

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
        self._SecretName = params.get("SecretName")
        self._VersionId = params.get("VersionId")
        self._RequestId = params.get("RequestId")


class VersionInfo(AbstractModel):
    """凭据版本号列表信息

    """

    def __init__(self):
        r"""
        :param _VersionId: 版本号
        :type VersionId: str
        :param _CreateTime: 创建时间，unix时间戳。
        :type CreateTime: int
        """
        self._VersionId = None
        self._CreateTime = None

    @property
    def VersionId(self):
        """版本号
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def CreateTime(self):
        """创建时间，unix时间戳。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        