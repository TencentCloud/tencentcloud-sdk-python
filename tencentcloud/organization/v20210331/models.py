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


class AcceptJoinShareUnitInvitationRequest(AbstractModel):
    r"""AcceptJoinShareUnitInvitation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        """
        self._UnitId = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptJoinShareUnitInvitationResponse(AbstractModel):
    r"""AcceptJoinShareUnitInvitation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class AddExternalSAMLIdPCertificateRequest(AbstractModel):
    r"""AddExternalSAMLIdPCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _X509Certificate: PEM 格式的 X509 证书。  由 SAML 身份提供商提供。
        :type X509Certificate: str
        """
        self._ZoneId = None
        self._X509Certificate = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def X509Certificate(self):
        r"""PEM 格式的 X509 证书。  由 SAML 身份提供商提供。
        :rtype: str
        """
        return self._X509Certificate

    @X509Certificate.setter
    def X509Certificate(self, X509Certificate):
        self._X509Certificate = X509Certificate


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._X509Certificate = params.get("X509Certificate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddExternalSAMLIdPCertificateResponse(AbstractModel):
    r"""AddExternalSAMLIdPCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: SAML 签名证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        r"""SAML 签名证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class AddOrganizationMemberEmailRequest(AbstractModel):
    r"""AddOrganizationMemberEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _Email: 邮箱地址。
        :type Email: str
        :param _CountryCode: 国际区号。
        :type CountryCode: str
        :param _Phone: 手机号。
        :type Phone: str
        """
        self._MemberUin = None
        self._Email = None
        self._CountryCode = None
        self._Phone = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Email(self):
        r"""邮箱地址。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CountryCode(self):
        r"""国际区号。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Phone(self):
        r"""手机号。
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Email = params.get("Email")
        self._CountryCode = params.get("CountryCode")
        self._Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddOrganizationMemberEmailResponse(AbstractModel):
    r"""AddOrganizationMemberEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindId: 绑定Id
        :type BindId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindId = None
        self._RequestId = None

    @property
    def BindId(self):
        r"""绑定Id
        :rtype: int
        """
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

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
        self._BindId = params.get("BindId")
        self._RequestId = params.get("RequestId")


class AddOrganizationNodeRequest(AbstractModel):
    r"""AddOrganizationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ParentNodeId: 父节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :type ParentNodeId: int
        :param _Name: 节点名称。最大长度为40个字符，支持英文字母、数字、汉字、符号+@、&._[]-
        :type Name: str
        :param _Remark: 备注。
        :type Remark: str
        :param _Tags: 部门标签列表。最大10个
        :type Tags: list of Tag
        """
        self._ParentNodeId = None
        self._Name = None
        self._Remark = None
        self._Tags = None

    @property
    def ParentNodeId(self):
        r"""父节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :rtype: int
        """
        return self._ParentNodeId

    @ParentNodeId.setter
    def ParentNodeId(self, ParentNodeId):
        self._ParentNodeId = ParentNodeId

    @property
    def Name(self):
        r"""节点名称。最大长度为40个字符，支持英文字母、数字、汉字、符号+@、&._[]-
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Tags(self):
        r"""部门标签列表。最大10个
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ParentNodeId = params.get("ParentNodeId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
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
        


class AddOrganizationNodeResponse(AbstractModel):
    r"""AddOrganizationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID。
        :type NodeId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NodeId = None
        self._RequestId = None

    @property
    def NodeId(self):
        r"""节点ID。
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

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
        self._NodeId = params.get("NodeId")
        self._RequestId = params.get("RequestId")


class AddPermissionPolicyToRoleConfigurationRequest(AbstractModel):
    r"""AddPermissionPolicyToRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置 ID
        :type RoleConfigurationId: str
        :param _RolePolicyType: 权限策略类型。取值：  System：系统策略。复用 CAM 的系统策略。 Custom: 自定义策略。按照 CAM 权限策略语法和结构编写的自定义策略。 
        :type RolePolicyType: str
        :param _RolePolicyNames: 权限策略名称，长度最大为 20策略，每个策略长度最大32个字符。如果要添加系统策略，建议使用RolePolicies参数。自定义策略时，数组长度最大为1。
        :type RolePolicyNames: list of str
        :param _RolePolicies: 添加的系统策略详情。
        :type RolePolicies: list of PolicyDetail
        :param _CustomPolicyDocument: 自定义策略内容。长度：最大 4096 个字符。当RolePolicyType为Inline时，该参数必须配置。关于权限策略的语法和结构，请参见权限策略语法和结构。
        :type CustomPolicyDocument: str
        :param _CustomPolicyDocuments: 自定义策略内容列表（跟RolePolicyNames一一对应）
        :type CustomPolicyDocuments: list of str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._RolePolicyType = None
        self._RolePolicyNames = None
        self._RolePolicies = None
        self._CustomPolicyDocument = None
        self._CustomPolicyDocuments = None

    @property
    def ZoneId(self):
        r"""空间 ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置 ID
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def RolePolicyType(self):
        r"""权限策略类型。取值：  System：系统策略。复用 CAM 的系统策略。 Custom: 自定义策略。按照 CAM 权限策略语法和结构编写的自定义策略。 
        :rtype: str
        """
        return self._RolePolicyType

    @RolePolicyType.setter
    def RolePolicyType(self, RolePolicyType):
        self._RolePolicyType = RolePolicyType

    @property
    def RolePolicyNames(self):
        r"""权限策略名称，长度最大为 20策略，每个策略长度最大32个字符。如果要添加系统策略，建议使用RolePolicies参数。自定义策略时，数组长度最大为1。
        :rtype: list of str
        """
        return self._RolePolicyNames

    @RolePolicyNames.setter
    def RolePolicyNames(self, RolePolicyNames):
        self._RolePolicyNames = RolePolicyNames

    @property
    def RolePolicies(self):
        r"""添加的系统策略详情。
        :rtype: list of PolicyDetail
        """
        return self._RolePolicies

    @RolePolicies.setter
    def RolePolicies(self, RolePolicies):
        self._RolePolicies = RolePolicies

    @property
    def CustomPolicyDocument(self):
        r"""自定义策略内容。长度：最大 4096 个字符。当RolePolicyType为Inline时，该参数必须配置。关于权限策略的语法和结构，请参见权限策略语法和结构。
        :rtype: str
        """
        return self._CustomPolicyDocument

    @CustomPolicyDocument.setter
    def CustomPolicyDocument(self, CustomPolicyDocument):
        self._CustomPolicyDocument = CustomPolicyDocument

    @property
    def CustomPolicyDocuments(self):
        r"""自定义策略内容列表（跟RolePolicyNames一一对应）
        :rtype: list of str
        """
        return self._CustomPolicyDocuments

    @CustomPolicyDocuments.setter
    def CustomPolicyDocuments(self, CustomPolicyDocuments):
        self._CustomPolicyDocuments = CustomPolicyDocuments


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._RolePolicyType = params.get("RolePolicyType")
        self._RolePolicyNames = params.get("RolePolicyNames")
        if params.get("RolePolicies") is not None:
            self._RolePolicies = []
            for item in params.get("RolePolicies"):
                obj = PolicyDetail()
                obj._deserialize(item)
                self._RolePolicies.append(obj)
        self._CustomPolicyDocument = params.get("CustomPolicyDocument")
        self._CustomPolicyDocuments = params.get("CustomPolicyDocuments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddPermissionPolicyToRoleConfigurationResponse(AbstractModel):
    r"""AddPermissionPolicyToRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class AddShareUnitMembersRequest(AbstractModel):
    r"""AddShareUnitMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _Area: 共享单元地域。
        :type Area: str
        :param _Members: 共享成员列表。最大10个。
        :type Members: list of ShareMember
        """
        self._UnitId = None
        self._Area = None
        self._Members = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def Area(self):
        r"""共享单元地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Members(self):
        r"""共享成员列表。最大10个。
        :rtype: list of ShareMember
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        self._Area = params.get("Area")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = ShareMember()
                obj._deserialize(item)
                self._Members.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddShareUnitMembersResponse(AbstractModel):
    r"""AddShareUnitMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class AddShareUnitRequest(AbstractModel):
    r"""AddShareUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 共享单元名称。仅支持大小写字母、数字、-、以及_的组合，3-128个字符。
        :type Name: str
        :param _Area: 共享单元地域。可通过接口[DescribeShareAreas](https://cloud.tencent.com/document/product/850/103050)获取支持共享的地域。
        :type Area: str
        :param _Description: 共享单元描述。最大128个字符。
        :type Description: str
        :param _ShareScope: 共享范围。取值：1-仅允许集团组织内共享 2-允许共享给任意账号，默认值：1
        :type ShareScope: int
        """
        self._Name = None
        self._Area = None
        self._Description = None
        self._ShareScope = None

    @property
    def Name(self):
        r"""共享单元名称。仅支持大小写字母、数字、-、以及_的组合，3-128个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Area(self):
        r"""共享单元地域。可通过接口[DescribeShareAreas](https://cloud.tencent.com/document/product/850/103050)获取支持共享的地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Description(self):
        r"""共享单元描述。最大128个字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ShareScope(self):
        r"""共享范围。取值：1-仅允许集团组织内共享 2-允许共享给任意账号，默认值：1
        :rtype: int
        """
        return self._ShareScope

    @ShareScope.setter
    def ShareScope(self, ShareScope):
        self._ShareScope = ShareScope


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Area = params.get("Area")
        self._Description = params.get("Description")
        self._ShareScope = params.get("ShareScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddShareUnitResourcesRequest(AbstractModel):
    r"""AddShareUnitResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _Area: 共享单元地域。
        :type Area: str
        :param _Type: 共享资源类型。支持共享的资源类型,请参见[资源共享概述](https://cloud.tencent.com/document/product/850/59489)
        :type Type: str
        :param _Resources: 共享资源列表。最大10个。
        :type Resources: list of ProductResource
        """
        self._UnitId = None
        self._Area = None
        self._Type = None
        self._Resources = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def Area(self):
        r"""共享单元地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Type(self):
        r"""共享资源类型。支持共享的资源类型,请参见[资源共享概述](https://cloud.tencent.com/document/product/850/59489)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Resources(self):
        r"""共享资源列表。最大10个。
        :rtype: list of ProductResource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        self._Area = params.get("Area")
        self._Type = params.get("Type")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ProductResource()
                obj._deserialize(item)
                self._Resources.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddShareUnitResourcesResponse(AbstractModel):
    r"""AddShareUnitResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class AddShareUnitResponse(AbstractModel):
    r"""AddShareUnit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UnitId = None
        self._RequestId = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

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
        self._UnitId = params.get("UnitId")
        self._RequestId = params.get("RequestId")


class AddUserToGroupRequest(AbstractModel):
    r"""AddUserToGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _GroupId: 用户组 ID。
        :type GroupId: str
        :param _UserId: 用户 ID。
        :type UserId: str
        """
        self._ZoneId = None
        self._GroupId = None
        self._UserId = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        r"""用户组 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UserId(self):
        r"""用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddUserToGroupResponse(AbstractModel):
    r"""AddUserToGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class AttachPolicyRequest(AbstractModel):
    r"""AttachPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetId: 绑定策略目标ID。成员Uin或部门ID
        :type TargetId: int
        :param _TargetType: 目标类型。取值范围：NODE-部门、MEMBER-成员
        :type TargetType: str
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _Type: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type Type: str
        """
        self._TargetId = None
        self._TargetType = None
        self._PolicyId = None
        self._Type = None

    @property
    def TargetId(self):
        r"""绑定策略目标ID。成员Uin或部门ID
        :rtype: int
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        r"""目标类型。取值范围：NODE-部门、MEMBER-成员
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Type(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._PolicyId = params.get("PolicyId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachPolicyResponse(AbstractModel):
    r"""AttachPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class AuthNode(AbstractModel):
    r"""互信主体主要信息

    """

    def __init__(self):
        r"""
        :param _RelationId: 互信主体关系ID
        :type RelationId: int
        :param _AuthName: 互信主体名称
        :type AuthName: str
        :param _Manager: 主体管理员
        :type Manager: :class:`tencentcloud.organization.v20210331.models.MemberMainInfo`
        """
        self._RelationId = None
        self._AuthName = None
        self._Manager = None

    @property
    def RelationId(self):
        r"""互信主体关系ID
        :rtype: int
        """
        return self._RelationId

    @RelationId.setter
    def RelationId(self, RelationId):
        self._RelationId = RelationId

    @property
    def AuthName(self):
        r"""互信主体名称
        :rtype: str
        """
        return self._AuthName

    @AuthName.setter
    def AuthName(self, AuthName):
        self._AuthName = AuthName

    @property
    def Manager(self):
        r"""主体管理员
        :rtype: :class:`tencentcloud.organization.v20210331.models.MemberMainInfo`
        """
        return self._Manager

    @Manager.setter
    def Manager(self, Manager):
        self._Manager = Manager


    def _deserialize(self, params):
        self._RelationId = params.get("RelationId")
        self._AuthName = params.get("AuthName")
        if params.get("Manager") is not None:
            self._Manager = MemberMainInfo()
            self._Manager._deserialize(params.get("Manager"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthRelationFile(AbstractModel):
    r"""野鹤实名互信申请证明文件

    """

    def __init__(self):
        r"""
        :param _Name: 文件名。
        :type Name: str
        :param _Url: 文件路径。
        :type Url: str
        """
        self._Name = None
        self._Url = None

    @property
    def Name(self):
        r"""文件名。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        r"""文件路径。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountRequest(AbstractModel):
    r"""BindOrganizationMemberAuthAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PolicyId: 策略ID。可以调用[DescribeOrganizationMemberPolicies](https://cloud.tencent.com/document/product/850/82935)获取
        :type PolicyId: int
        :param _OrgSubAccountUins: 组织管理员子账号Uin列表。最大5个
        :type OrgSubAccountUins: list of int
        """
        self._MemberUin = None
        self._PolicyId = None
        self._OrgSubAccountUins = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        r"""策略ID。可以调用[DescribeOrganizationMemberPolicies](https://cloud.tencent.com/document/product/850/82935)获取
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OrgSubAccountUins(self):
        r"""组织管理员子账号Uin列表。最大5个
        :rtype: list of int
        """
        return self._OrgSubAccountUins

    @OrgSubAccountUins.setter
    def OrgSubAccountUins(self, OrgSubAccountUins):
        self._OrgSubAccountUins = OrgSubAccountUins


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        self._OrgSubAccountUins = params.get("OrgSubAccountUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationMemberAuthAccountResponse(AbstractModel):
    r"""BindOrganizationMemberAuthAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class BindOrganizationPolicySubAccountRequest(AbstractModel):
    r"""BindOrganizationPolicySubAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _OrgSubAccountUins: 组织管理员子账号Uin列表。最大5个
        :type OrgSubAccountUins: list of int
        """
        self._PolicyId = None
        self._OrgSubAccountUins = None

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OrgSubAccountUins(self):
        r"""组织管理员子账号Uin列表。最大5个
        :rtype: list of int
        """
        return self._OrgSubAccountUins

    @OrgSubAccountUins.setter
    def OrgSubAccountUins(self, OrgSubAccountUins):
        self._OrgSubAccountUins = OrgSubAccountUins


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._OrgSubAccountUins = params.get("OrgSubAccountUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindOrganizationPolicySubAccountResponse(AbstractModel):
    r"""BindOrganizationPolicySubAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CancelOrganizationMemberAuthAccountRequest(AbstractModel):
    r"""CancelOrganizationMemberAuthAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PolicyId: 策略ID。可以通过[DescribeOrganizationMemberPolicies](https://cloud.tencent.com/document/product/850/82935)获取
        :type PolicyId: int
        :param _OrgSubAccountUin: 组织子账号Uin。
        :type OrgSubAccountUin: int
        """
        self._MemberUin = None
        self._PolicyId = None
        self._OrgSubAccountUin = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        r"""策略ID。可以通过[DescribeOrganizationMemberPolicies](https://cloud.tencent.com/document/product/850/82935)获取
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OrgSubAccountUin(self):
        r"""组织子账号Uin。
        :rtype: int
        """
        return self._OrgSubAccountUin

    @OrgSubAccountUin.setter
    def OrgSubAccountUin(self, OrgSubAccountUin):
        self._OrgSubAccountUin = OrgSubAccountUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        self._OrgSubAccountUin = params.get("OrgSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationMemberAuthAccountResponse(AbstractModel):
    r"""CancelOrganizationMemberAuthAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CancelOrganizationPolicySubAccountRequest(AbstractModel):
    r"""CancelOrganizationPolicySubAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _OrgSubAccountUins: 组织管理员子账号Uin列表。最大5个
        :type OrgSubAccountUins: list of int
        """
        self._PolicyId = None
        self._OrgSubAccountUins = None

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def OrgSubAccountUins(self):
        r"""组织管理员子账号Uin列表。最大5个
        :rtype: list of int
        """
        return self._OrgSubAccountUins

    @OrgSubAccountUins.setter
    def OrgSubAccountUins(self, OrgSubAccountUins):
        self._OrgSubAccountUins = OrgSubAccountUins


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._OrgSubAccountUins = params.get("OrgSubAccountUins")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelOrganizationPolicySubAccountResponse(AbstractModel):
    r"""CancelOrganizationPolicySubAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CheckAccountDeleteRequest(AbstractModel):
    r"""CheckAccountDelete请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        """
        self._MemberUin = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAccountDeleteResponse(AbstractModel):
    r"""CheckAccountDelete返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllowDelete: 成员是否允许删除。 true-是、false-否
        :type AllowDelete: bool
        :param _NotAllowReason: 不允许删除原因。
        :type NotAllowReason: :class:`tencentcloud.organization.v20210331.models.NotAllowReason`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllowDelete = None
        self._NotAllowReason = None
        self._RequestId = None

    @property
    def AllowDelete(self):
        r"""成员是否允许删除。 true-是、false-否
        :rtype: bool
        """
        return self._AllowDelete

    @AllowDelete.setter
    def AllowDelete(self, AllowDelete):
        self._AllowDelete = AllowDelete

    @property
    def NotAllowReason(self):
        r"""不允许删除原因。
        :rtype: :class:`tencentcloud.organization.v20210331.models.NotAllowReason`
        """
        return self._NotAllowReason

    @NotAllowReason.setter
    def NotAllowReason(self, NotAllowReason):
        self._NotAllowReason = NotAllowReason

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
        self._AllowDelete = params.get("AllowDelete")
        if params.get("NotAllowReason") is not None:
            self._NotAllowReason = NotAllowReason()
            self._NotAllowReason._deserialize(params.get("NotAllowReason"))
        self._RequestId = params.get("RequestId")


class ClearExternalSAMLIdentityProviderRequest(AbstractModel):
    r"""ClearExternalSAMLIdentityProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClearExternalSAMLIdentityProviderResponse(AbstractModel):
    r"""ClearExternalSAMLIdentityProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateGroupRequest(AbstractModel):
    r"""CreateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _GroupName: 用户组的名称。  格式：允许英文字母、数字和特殊字符-。 长度：最大 128 个字符。
        :type GroupName: str
        :param _Description: 用户组的描述。  长度：最大 1024 个字符。
        :type Description: str
        :param _GroupType: 用户组类型  Manual：手动创建，Synchronized：外部导入
        :type GroupType: str
        """
        self._ZoneId = None
        self._GroupName = None
        self._Description = None
        self._GroupType = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupName(self):
        r"""用户组的名称。  格式：允许英文字母、数字和特殊字符-。 长度：最大 128 个字符。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        r"""用户组的描述。  长度：最大 1024 个字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GroupType(self):
        r"""用户组类型  Manual：手动创建，Synchronized：外部导入
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        self._GroupType = params.get("GroupType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGroupResponse(AbstractModel):
    r"""CreateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupInfo: 用户组信息。
        :type GroupInfo: :class:`tencentcloud.organization.v20210331.models.GroupInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupInfo = None
        self._RequestId = None

    @property
    def GroupInfo(self):
        r"""用户组信息。
        :rtype: :class:`tencentcloud.organization.v20210331.models.GroupInfo`
        """
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

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
        if params.get("GroupInfo") is not None:
            self._GroupInfo = GroupInfo()
            self._GroupInfo._deserialize(params.get("GroupInfo"))
        self._RequestId = params.get("RequestId")


class CreateOrgServiceAssignRequest(AbstractModel):
    r"""CreateOrgServiceAssign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUins: 委派管理员Uin列表。 最大长度20个
        :type MemberUins: list of int
        :param _ServiceId: 集团服务ID。和集团服务产品标识二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :type ServiceId: int
        :param _Product: 集团服务产品标识。和集团服务ID二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :type Product: str
        :param _ManagementScope: 委派管理员管理范围。 取值：1-全部成员 2-部分成员，默认值1
        :type ManagementScope: int
        :param _ManagementScopeUins: 管理的成员Uin列表。ManagementScope为2时该参数有效
        :type ManagementScopeUins: list of int
        :param _ManagementScopeNodeIds: 管理的部门ID列表。ManagementScope为2时该参数有效
        :type ManagementScopeNodeIds: list of int
        """
        self._MemberUins = None
        self._ServiceId = None
        self._Product = None
        self._ManagementScope = None
        self._ManagementScopeUins = None
        self._ManagementScopeNodeIds = None

    @property
    def MemberUins(self):
        r"""委派管理员Uin列表。 最大长度20个
        :rtype: list of int
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def ServiceId(self):
        r"""集团服务ID。和集团服务产品标识二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :rtype: int
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Product(self):
        r"""集团服务产品标识。和集团服务ID二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ManagementScope(self):
        r"""委派管理员管理范围。 取值：1-全部成员 2-部分成员，默认值1
        :rtype: int
        """
        return self._ManagementScope

    @ManagementScope.setter
    def ManagementScope(self, ManagementScope):
        self._ManagementScope = ManagementScope

    @property
    def ManagementScopeUins(self):
        r"""管理的成员Uin列表。ManagementScope为2时该参数有效
        :rtype: list of int
        """
        return self._ManagementScopeUins

    @ManagementScopeUins.setter
    def ManagementScopeUins(self, ManagementScopeUins):
        self._ManagementScopeUins = ManagementScopeUins

    @property
    def ManagementScopeNodeIds(self):
        r"""管理的部门ID列表。ManagementScope为2时该参数有效
        :rtype: list of int
        """
        return self._ManagementScopeNodeIds

    @ManagementScopeNodeIds.setter
    def ManagementScopeNodeIds(self, ManagementScopeNodeIds):
        self._ManagementScopeNodeIds = ManagementScopeNodeIds


    def _deserialize(self, params):
        self._MemberUins = params.get("MemberUins")
        self._ServiceId = params.get("ServiceId")
        self._Product = params.get("Product")
        self._ManagementScope = params.get("ManagementScope")
        self._ManagementScopeUins = params.get("ManagementScopeUins")
        self._ManagementScopeNodeIds = params.get("ManagementScopeNodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrgServiceAssignResponse(AbstractModel):
    r"""CreateOrgServiceAssign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateOrganizationIdentityRequest(AbstractModel):
    r"""CreateOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityAliasName: 身份名称
        :type IdentityAliasName: str
        :param _IdentityPolicy: 身份策略
        :type IdentityPolicy: list of IdentityPolicy
        :param _Description: 身份描述
        :type Description: str
        """
        self._IdentityAliasName = None
        self._IdentityPolicy = None
        self._Description = None

    @property
    def IdentityAliasName(self):
        r"""身份名称
        :rtype: str
        """
        return self._IdentityAliasName

    @IdentityAliasName.setter
    def IdentityAliasName(self, IdentityAliasName):
        self._IdentityAliasName = IdentityAliasName

    @property
    def IdentityPolicy(self):
        r"""身份策略
        :rtype: list of IdentityPolicy
        """
        return self._IdentityPolicy

    @IdentityPolicy.setter
    def IdentityPolicy(self, IdentityPolicy):
        self._IdentityPolicy = IdentityPolicy

    @property
    def Description(self):
        r"""身份描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._IdentityAliasName = params.get("IdentityAliasName")
        if params.get("IdentityPolicy") is not None:
            self._IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self._IdentityPolicy.append(obj)
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationIdentityResponse(AbstractModel):
    r"""CreateOrganizationIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID
        :type IdentityId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IdentityId = None
        self._RequestId = None

    @property
    def IdentityId(self):
        r"""身份ID
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

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
        self._IdentityId = params.get("IdentityId")
        self._RequestId = params.get("RequestId")


class CreateOrganizationMemberAuthIdentityRequest(AbstractModel):
    r"""CreateOrganizationMemberAuthIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUins: 成员Uin列表。最多10个
        :type MemberUins: list of int non-negative
        :param _IdentityIds: 身份Id列表。最多5个，可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :type IdentityIds: list of int non-negative
        """
        self._MemberUins = None
        self._IdentityIds = None

    @property
    def MemberUins(self):
        r"""成员Uin列表。最多10个
        :rtype: list of int non-negative
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def IdentityIds(self):
        r"""身份Id列表。最多5个，可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :rtype: list of int non-negative
        """
        return self._IdentityIds

    @IdentityIds.setter
    def IdentityIds(self, IdentityIds):
        self._IdentityIds = IdentityIds


    def _deserialize(self, params):
        self._MemberUins = params.get("MemberUins")
        self._IdentityIds = params.get("IdentityIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberAuthIdentityResponse(AbstractModel):
    r"""CreateOrganizationMemberAuthIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateOrganizationMemberPolicyRequest(AbstractModel):
    r"""CreateOrganizationMemberPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PolicyName: 策略名。最大长度为128个字符，支持英文字母、数字、符号+=,.@_-
        :type PolicyName: str
        :param _IdentityId: 成员访问身份ID。可以调用[DescribeOrganizationMemberAuthIdentities](https://cloud.tencent.com/document/product/850/82936)获取
        :type IdentityId: int
        :param _Description: 描述。
        :type Description: str
        """
        self._MemberUin = None
        self._PolicyName = None
        self._IdentityId = None
        self._Description = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyName(self):
        r"""策略名。最大长度为128个字符，支持英文字母、数字、符号+=,.@_-
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        r"""成员访问身份ID。可以调用[DescribeOrganizationMemberAuthIdentities](https://cloud.tencent.com/document/product/850/82936)获取
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def Description(self):
        r"""描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMemberPolicyResponse(AbstractModel):
    r"""CreateOrganizationMemberPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateOrganizationMemberRequest(AbstractModel):
    r"""CreateOrganizationMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type Name: str
        :param _PolicyType: 关系策略。取值：Financial
        :type PolicyType: str
        :param _PermissionIds: 成员财务权限ID列表。取值：1-查看账单、2-查看余额、3-资金划拨（若需要开启资金划拨权限，请联系您的商务经理内部开通。）、4-合并出账、5-开票、6-优惠继承、7-代付费、8-成本分析、9-预算管理、10-信用额度设置（若需要开启信用额度设置权限，请联系您的商务经理内部开通。），1、2 默认必须
        :type PermissionIds: list of int non-negative
        :param _NodeId: 成员所属部门的节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :type NodeId: int
        :param _AccountName: 账号名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type AccountName: str
        :param _Remark: 备注。
        :type Remark: str
        :param _RecordId: 成员创建记录ID。创建异常重试时需要
        :type RecordId: int
        :param _PayUin: 代付者Uin。成员代付费时需要
        :type PayUin: str
        :param _IdentityRoleID: 成员访问身份ID列表。可以调用ListOrganizationIdentity获取，1默认支持
        :type IdentityRoleID: list of int non-negative
        :param _AuthRelationId: 认证主体关系ID。给不同主体创建成员时需要，可以调用DescribeOrganizationAuthNode获取
        :type AuthRelationId: int
        :param _Tags: 成员标签列表。最大10个
        :type Tags: list of Tag
        """
        self._Name = None
        self._PolicyType = None
        self._PermissionIds = None
        self._NodeId = None
        self._AccountName = None
        self._Remark = None
        self._RecordId = None
        self._PayUin = None
        self._IdentityRoleID = None
        self._AuthRelationId = None
        self._Tags = None

    @property
    def Name(self):
        r"""成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PolicyType(self):
        r"""关系策略。取值：Financial
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PermissionIds(self):
        r"""成员财务权限ID列表。取值：1-查看账单、2-查看余额、3-资金划拨（若需要开启资金划拨权限，请联系您的商务经理内部开通。）、4-合并出账、5-开票、6-优惠继承、7-代付费、8-成本分析、9-预算管理、10-信用额度设置（若需要开启信用额度设置权限，请联系您的商务经理内部开通。），1、2 默认必须
        :rtype: list of int non-negative
        """
        return self._PermissionIds

    @PermissionIds.setter
    def PermissionIds(self, PermissionIds):
        self._PermissionIds = PermissionIds

    @property
    def NodeId(self):
        r"""成员所属部门的节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def AccountName(self):
        r"""账号名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :rtype: str
        """
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def Remark(self):
        r"""备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RecordId(self):
        r"""成员创建记录ID。创建异常重试时需要
        :rtype: int
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def PayUin(self):
        r"""代付者Uin。成员代付费时需要
        :rtype: str
        """
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def IdentityRoleID(self):
        r"""成员访问身份ID列表。可以调用ListOrganizationIdentity获取，1默认支持
        :rtype: list of int non-negative
        """
        return self._IdentityRoleID

    @IdentityRoleID.setter
    def IdentityRoleID(self, IdentityRoleID):
        self._IdentityRoleID = IdentityRoleID

    @property
    def AuthRelationId(self):
        r"""认证主体关系ID。给不同主体创建成员时需要，可以调用DescribeOrganizationAuthNode获取
        :rtype: int
        """
        return self._AuthRelationId

    @AuthRelationId.setter
    def AuthRelationId(self, AuthRelationId):
        self._AuthRelationId = AuthRelationId

    @property
    def Tags(self):
        r"""成员标签列表。最大10个
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._PolicyType = params.get("PolicyType")
        self._PermissionIds = params.get("PermissionIds")
        self._NodeId = params.get("NodeId")
        self._AccountName = params.get("AccountName")
        self._Remark = params.get("Remark")
        self._RecordId = params.get("RecordId")
        self._PayUin = params.get("PayUin")
        self._IdentityRoleID = params.get("IdentityRoleID")
        self._AuthRelationId = params.get("AuthRelationId")
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
        


class CreateOrganizationMemberResponse(AbstractModel):
    r"""CreateOrganizationMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Uin: 成员Uin。
        :type Uin: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Uin = None
        self._RequestId = None

    @property
    def Uin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

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
        self._Uin = params.get("Uin")
        self._RequestId = params.get("RequestId")


class CreateOrganizationMembersPolicyRequest(AbstractModel):
    r"""CreateOrganizationMembersPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUins: 成员Uin列表。最多10个
        :type MemberUins: list of int
        :param _PolicyName: 策略名。长度1～128个字符，支持英文字母、数字、符号+=,.@_-
        :type PolicyName: str
        :param _IdentityId: 成员访问身份ID。可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :type IdentityId: int
        :param _Description: 策略描述。最大长度为128个字符
        :type Description: str
        """
        self._MemberUins = None
        self._PolicyName = None
        self._IdentityId = None
        self._Description = None

    @property
    def MemberUins(self):
        r"""成员Uin列表。最多10个
        :rtype: list of int
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def PolicyName(self):
        r"""策略名。长度1～128个字符，支持英文字母、数字、符号+=,.@_-
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        r"""成员访问身份ID。可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def Description(self):
        r"""策略描述。最大长度为128个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._MemberUins = params.get("MemberUins")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateOrganizationMembersPolicyResponse(AbstractModel):
    r"""CreateOrganizationMembersPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateOrganizationRequest(AbstractModel):
    r"""CreateOrganization请求参数结构体

    """


class CreateOrganizationResponse(AbstractModel):
    r"""CreateOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgId: 企业组织ID
        :type OrgId: int
        :param _NickName: 创建者昵称
        :type NickName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgId = None
        self._NickName = None
        self._RequestId = None

    @property
    def OrgId(self):
        r"""企业组织ID
        :rtype: int
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def NickName(self):
        r"""创建者昵称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

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
        self._OrgId = params.get("OrgId")
        self._NickName = params.get("NickName")
        self._RequestId = params.get("RequestId")


class CreatePolicyRequest(AbstractModel):
    r"""CreatePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 策略名。
长度为1~128个字符，可以包含汉字、英文字母、数字和下划线（_）
        :type Name: str
        :param _Content: 策略内容。参考CAM策略语法
        :type Content: str
        :param _Type: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type Type: str
        :param _Description: 策略描述。
        :type Description: str
        """
        self._Name = None
        self._Content = None
        self._Type = None
        self._Description = None

    @property
    def Name(self):
        r"""策略名。
长度为1~128个字符，可以包含汉字、英文字母、数字和下划线（_）
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Content(self):
        r"""策略内容。参考CAM策略语法
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Type(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        r"""策略描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Content = params.get("Content")
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePolicyResponse(AbstractModel):
    r"""CreatePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID
        :type PolicyId: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._RequestId = None

    @property
    def PolicyId(self):
        r"""策略ID
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

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
        self._PolicyId = params.get("PolicyId")
        self._RequestId = params.get("RequestId")


class CreateRoleAssignmentRequest(AbstractModel):
    r"""CreateRoleAssignment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _RoleAssignmentInfo: 授权成员账号信息，最多授权50条。
        :type RoleAssignmentInfo: list of RoleAssignmentInfo
        """
        self._ZoneId = None
        self._RoleAssignmentInfo = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleAssignmentInfo(self):
        r"""授权成员账号信息，最多授权50条。
        :rtype: list of RoleAssignmentInfo
        """
        return self._RoleAssignmentInfo

    @RoleAssignmentInfo.setter
    def RoleAssignmentInfo(self, RoleAssignmentInfo):
        self._RoleAssignmentInfo = RoleAssignmentInfo


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("RoleAssignmentInfo") is not None:
            self._RoleAssignmentInfo = []
            for item in params.get("RoleAssignmentInfo"):
                obj = RoleAssignmentInfo()
                obj._deserialize(item)
                self._RoleAssignmentInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleAssignmentResponse(AbstractModel):
    r"""CreateRoleAssignment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务详情。
        :type Tasks: list of TaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        r"""任务详情。
        :rtype: list of TaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class CreateRoleConfigurationRequest(AbstractModel):
    r"""CreateRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _RoleConfigurationName: 权限配置名称。格式：包含英文字母、数字或短划线（-）。 长度：最大 128 个字符。
        :type RoleConfigurationName: str
        :param _Description: 权限配置的描述。 长度：最大 1024 个字符。
        :type Description: str
        :param _SessionDuration: 会话持续时间。 CIC用户使用权限配置访问集团账号目标账号时，会话最多保持的时间。 单位：秒。 取值范围：900 ~ 43200（15 分钟~12 小时）。 默认值：3600（1 小时）。
        :type SessionDuration: int
        :param _RelayState: 初始访问页面。 CIC用户使用权限配置访问集团账号目标账号时，初始访问的页面地址。 该页面必须是腾讯云控制台页面。默认为空，表示跳转到腾讯云控制台首页。
        :type RelayState: str
        """
        self._ZoneId = None
        self._RoleConfigurationName = None
        self._Description = None
        self._SessionDuration = None
        self._RelayState = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationName(self):
        r"""权限配置名称。格式：包含英文字母、数字或短划线（-）。 长度：最大 128 个字符。
        :rtype: str
        """
        return self._RoleConfigurationName

    @RoleConfigurationName.setter
    def RoleConfigurationName(self, RoleConfigurationName):
        self._RoleConfigurationName = RoleConfigurationName

    @property
    def Description(self):
        r"""权限配置的描述。 长度：最大 1024 个字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SessionDuration(self):
        r"""会话持续时间。 CIC用户使用权限配置访问集团账号目标账号时，会话最多保持的时间。 单位：秒。 取值范围：900 ~ 43200（15 分钟~12 小时）。 默认值：3600（1 小时）。
        :rtype: int
        """
        return self._SessionDuration

    @SessionDuration.setter
    def SessionDuration(self, SessionDuration):
        self._SessionDuration = SessionDuration

    @property
    def RelayState(self):
        r"""初始访问页面。 CIC用户使用权限配置访问集团账号目标账号时，初始访问的页面地址。 该页面必须是腾讯云控制台页面。默认为空，表示跳转到腾讯云控制台首页。
        :rtype: str
        """
        return self._RelayState

    @RelayState.setter
    def RelayState(self, RelayState):
        self._RelayState = RelayState


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationName = params.get("RoleConfigurationName")
        self._Description = params.get("Description")
        self._SessionDuration = params.get("SessionDuration")
        self._RelayState = params.get("RelayState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoleConfigurationResponse(AbstractModel):
    r"""CreateRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleConfigurationInfo: 配置访问详情
        :type RoleConfigurationInfo: :class:`tencentcloud.organization.v20210331.models.RoleConfiguration`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleConfigurationInfo = None
        self._RequestId = None

    @property
    def RoleConfigurationInfo(self):
        r"""配置访问详情
        :rtype: :class:`tencentcloud.organization.v20210331.models.RoleConfiguration`
        """
        return self._RoleConfigurationInfo

    @RoleConfigurationInfo.setter
    def RoleConfigurationInfo(self, RoleConfigurationInfo):
        self._RoleConfigurationInfo = RoleConfigurationInfo

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
        if params.get("RoleConfigurationInfo") is not None:
            self._RoleConfigurationInfo = RoleConfiguration()
            self._RoleConfigurationInfo._deserialize(params.get("RoleConfigurationInfo"))
        self._RequestId = params.get("RequestId")


class CreateSCIMCredentialRequest(AbstractModel):
    r"""CreateSCIMCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _ExpireDuration: 过期时间（秒），最小1小时，最大99年。如果不传则默认一年过期
        :type ExpireDuration: int
        """
        self._ZoneId = None
        self._ExpireDuration = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ExpireDuration(self):
        r"""过期时间（秒），最小1小时，最大99年。如果不传则默认一年过期
        :rtype: int
        """
        return self._ExpireDuration

    @ExpireDuration.setter
    def ExpireDuration(self, ExpireDuration):
        self._ExpireDuration = ExpireDuration


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ExpireDuration = params.get("ExpireDuration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSCIMCredentialResponse(AbstractModel):
    r"""CreateSCIMCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母。
        :type ZoneId: str
        :param _CredentialId: SCIM密钥ID。scimcred-前缀开头，后面是12位随机数字/小写字母。
        :type CredentialId: str
        :param _CredentialType: SCIM密钥类型。
        :type CredentialType: str
        :param _CreateTime: SCIM 密钥的创建时间。
        :type CreateTime: str
        :param _ExpireTime: SCIM 密钥的过期时间。
        :type ExpireTime: str
        :param _CredentialStatus: SCIM密钥状态，Enabled已开启，Disabled已关闭。
        :type CredentialStatus: str
        :param _CredentialSecret: SCIM密钥。
        :type CredentialSecret: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._CredentialId = None
        self._CredentialType = None
        self._CreateTime = None
        self._ExpireTime = None
        self._CredentialStatus = None
        self._CredentialSecret = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CredentialId(self):
        r"""SCIM密钥ID。scimcred-前缀开头，后面是12位随机数字/小写字母。
        :rtype: str
        """
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId

    @property
    def CredentialType(self):
        r"""SCIM密钥类型。
        :rtype: str
        """
        return self._CredentialType

    @CredentialType.setter
    def CredentialType(self, CredentialType):
        self._CredentialType = CredentialType

    @property
    def CreateTime(self):
        r"""SCIM 密钥的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""SCIM 密钥的过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CredentialStatus(self):
        r"""SCIM密钥状态，Enabled已开启，Disabled已关闭。
        :rtype: str
        """
        return self._CredentialStatus

    @CredentialStatus.setter
    def CredentialStatus(self, CredentialStatus):
        self._CredentialStatus = CredentialStatus

    @property
    def CredentialSecret(self):
        r"""SCIM密钥。
        :rtype: str
        """
        return self._CredentialSecret

    @CredentialSecret.setter
    def CredentialSecret(self, CredentialSecret):
        self._CredentialSecret = CredentialSecret

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
        self._ZoneId = params.get("ZoneId")
        self._CredentialId = params.get("CredentialId")
        self._CredentialType = params.get("CredentialType")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._CredentialStatus = params.get("CredentialStatus")
        self._CredentialSecret = params.get("CredentialSecret")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    r"""CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _UserName: 用户名称。空间内必须唯一。不支持修改。  格式：包含数字、英文字母和特殊符号+ = , . @ - _ 。  长度：最大 64 个字符
        :type UserName: str
        :param _FirstName: 用户的姓。  长度：最大 64 个字符。
        :type FirstName: str
        :param _LastName: 用户的名。  长度：最大 64 个字符。
        :type LastName: str
        :param _DisplayName: 用户的显示名称。  长度：最大 256 个字符。
        :type DisplayName: str
        :param _Description: 用户的描述。  长度：最大 1024 个字符。
        :type Description: str
        :param _Email: 用户的电子邮箱。目录内必须唯一。  长度：最大 128 个字符。
        :type Email: str
        :param _UserStatus: 用户的状态。取值：  Enabled（默认值）：启用。 Disabled：禁用。
        :type UserStatus: str
        :param _UserType: 用户类型  Manual：手动创建，Synchronized：外部导入
        :type UserType: str
        :param _NeedResetPassword: 是否需要重置密码： true: 需要重置  false: 不需要重置密码。 默认false
        :type NeedResetPassword: bool
        """
        self._ZoneId = None
        self._UserName = None
        self._FirstName = None
        self._LastName = None
        self._DisplayName = None
        self._Description = None
        self._Email = None
        self._UserStatus = None
        self._UserType = None
        self._NeedResetPassword = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserName(self):
        r"""用户名称。空间内必须唯一。不支持修改。  格式：包含数字、英文字母和特殊符号+ = , . @ - _ 。  长度：最大 64 个字符
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def FirstName(self):
        r"""用户的姓。  长度：最大 64 个字符。
        :rtype: str
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        r"""用户的名。  长度：最大 64 个字符。
        :rtype: str
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def DisplayName(self):
        r"""用户的显示名称。  长度：最大 256 个字符。
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        r"""用户的描述。  长度：最大 1024 个字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Email(self):
        r"""用户的电子邮箱。目录内必须唯一。  长度：最大 128 个字符。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def UserStatus(self):
        r"""用户的状态。取值：  Enabled（默认值）：启用。 Disabled：禁用。
        :rtype: str
        """
        return self._UserStatus

    @UserStatus.setter
    def UserStatus(self, UserStatus):
        self._UserStatus = UserStatus

    @property
    def UserType(self):
        r"""用户类型  Manual：手动创建，Synchronized：外部导入
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def NeedResetPassword(self):
        r"""是否需要重置密码： true: 需要重置  false: 不需要重置密码。 默认false
        :rtype: bool
        """
        return self._NeedResetPassword

    @NeedResetPassword.setter
    def NeedResetPassword(self, NeedResetPassword):
        self._NeedResetPassword = NeedResetPassword


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserName = params.get("UserName")
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._Email = params.get("Email")
        self._UserStatus = params.get("UserStatus")
        self._UserType = params.get("UserType")
        self._NeedResetPassword = params.get("NeedResetPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    r"""CreateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户详情
        :type UserInfo: :class:`tencentcloud.organization.v20210331.models.UserInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserInfo = None
        self._RequestId = None

    @property
    def UserInfo(self):
        r"""用户详情
        :rtype: :class:`tencentcloud.organization.v20210331.models.UserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

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
        if params.get("UserInfo") is not None:
            self._UserInfo = UserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._RequestId = params.get("RequestId")


class CreateUserSyncProvisioningRequest(AbstractModel):
    r"""CreateUserSyncProvisioning请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _UserSyncProvisionings: CAM用户同步信息。
        :type UserSyncProvisionings: list of UserSyncProvisioning
        """
        self._ZoneId = None
        self._UserSyncProvisionings = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserSyncProvisionings(self):
        r"""CAM用户同步信息。
        :rtype: list of UserSyncProvisioning
        """
        return self._UserSyncProvisionings

    @UserSyncProvisionings.setter
    def UserSyncProvisionings(self, UserSyncProvisionings):
        self._UserSyncProvisionings = UserSyncProvisionings


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("UserSyncProvisionings") is not None:
            self._UserSyncProvisionings = []
            for item in params.get("UserSyncProvisionings"):
                obj = UserSyncProvisioning()
                obj._deserialize(item)
                self._UserSyncProvisionings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserSyncProvisioningResponse(AbstractModel):
    r"""CreateUserSyncProvisioning返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务详细。
        :type Tasks: list of UserProvisioningsTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        r"""任务详细。
        :rtype: list of UserProvisioningsTask
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = UserProvisioningsTask()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class DeleteAccountRequest(AbstractModel):
    r"""DeleteAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        """
        self._MemberUin = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAccountResponse(AbstractModel):
    r"""DeleteAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteGroupRequest(AbstractModel):
    r"""DeleteGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _GroupId: 用户组的 ID。
        :type GroupId: str
        """
        self._ZoneId = None
        self._GroupId = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        r"""用户组的 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGroupResponse(AbstractModel):
    r"""DeleteGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOrgServiceAssignRequest(AbstractModel):
    r"""DeleteOrgServiceAssign请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 委派管理员Uin。
        :type MemberUin: int
        :param _ServiceId: 集团服务ID。和集团服务产品标识二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :type ServiceId: int
        :param _Product: 集团服务产品标识。和集团服务ID二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :type Product: str
        """
        self._MemberUin = None
        self._ServiceId = None
        self._Product = None

    @property
    def MemberUin(self):
        r"""委派管理员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def ServiceId(self):
        r"""集团服务ID。和集团服务产品标识二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :rtype: int
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Product(self):
        r"""集团服务产品标识。和集团服务ID二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._ServiceId = params.get("ServiceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrgServiceAssignResponse(AbstractModel):
    r"""DeleteOrgServiceAssign返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOrganizationIdentityRequest(AbstractModel):
    r"""DeleteOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID。可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :type IdentityId: int
        """
        self._IdentityId = None

    @property
    def IdentityId(self):
        r"""身份ID。可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationIdentityResponse(AbstractModel):
    r"""DeleteOrganizationIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOrganizationMemberAuthIdentityRequest(AbstractModel):
    r"""DeleteOrganizationMemberAuthIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _IdentityId: 身份ID。可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :type IdentityId: int
        """
        self._MemberUin = None
        self._IdentityId = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def IdentityId(self):
        r"""身份ID。可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._IdentityId = params.get("IdentityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMemberAuthIdentityResponse(AbstractModel):
    r"""DeleteOrganizationMemberAuthIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOrganizationMembersPolicyRequest(AbstractModel):
    r"""DeleteOrganizationMembersPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 访问策略ID。可以通过[DescribeOrganizationMemberPolicies](https://cloud.tencent.com/document/product/850/82935)获取
        :type PolicyId: int
        """
        self._PolicyId = None

    @property
    def PolicyId(self):
        r"""访问策略ID。可以通过[DescribeOrganizationMemberPolicies](https://cloud.tencent.com/document/product/850/82935)获取
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMembersPolicyResponse(AbstractModel):
    r"""DeleteOrganizationMembersPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOrganizationMembersRequest(AbstractModel):
    r"""DeleteOrganizationMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 被删除成员的Uin列表。
        :type MemberUin: list of int
        """
        self._MemberUin = None

    @property
    def MemberUin(self):
        r"""被删除成员的Uin列表。
        :rtype: list of int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationMembersResponse(AbstractModel):
    r"""DeleteOrganizationMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOrganizationNodesRequest(AbstractModel):
    r"""DeleteOrganizationNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID列表。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :type NodeId: list of int
        """
        self._NodeId = None

    @property
    def NodeId(self):
        r"""节点ID列表。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :rtype: list of int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteOrganizationNodesResponse(AbstractModel):
    r"""DeleteOrganizationNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteOrganizationRequest(AbstractModel):
    r"""DeleteOrganization请求参数结构体

    """


class DeleteOrganizationResponse(AbstractModel):
    r"""DeleteOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeletePolicyRequest(AbstractModel):
    r"""DeletePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 需要删除的策略ID。可以调用[ListPolicies](https://cloud.tencent.com/document/product/850/105311)获取

        :type PolicyId: int
        :param _Type: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type Type: str
        """
        self._PolicyId = None
        self._Type = None

    @property
    def PolicyId(self):
        r"""需要删除的策略ID。可以调用[ListPolicies](https://cloud.tencent.com/document/product/850/105311)获取

        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Type(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePolicyResponse(AbstractModel):
    r"""DeletePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteRoleAssignmentRequest(AbstractModel):
    r"""DeleteRoleAssignment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _TargetUin: 集团账号目标账号的UIN
        :type TargetUin: int
        :param _PrincipalType: CAM 用户同步的身份类型。取值： User：表示同步的身份是用户。 Group：表示同步的身份是用户组。
        :type PrincipalType: str
        :param _PrincipalId: 用户同步 ID。取值： 当PrincipalType取值为Group时，该值为用户组 ID（g-********）， 当PrincipalType取值为User时，该值为用户 ID（u-********）。 	
        :type PrincipalId: str
        :param _DeprovisionStrategy: 当您移除一个集团账号目标账号上使用某权限配置的最后一个授权时，是否同时解除权限配置部署。取值： DeprovisionForLastRoleAssignmentOnAccount：解除权限配置部署。 None（默认值）：不解除权限配置部署。
        :type DeprovisionStrategy: str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._TargetType = None
        self._TargetUin = None
        self._PrincipalType = None
        self._PrincipalId = None
        self._DeprovisionStrategy = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetUin(self):
        r"""集团账号目标账号的UIN
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值： User：表示同步的身份是用户。 Group：表示同步的身份是用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def PrincipalId(self):
        r"""用户同步 ID。取值： 当PrincipalType取值为Group时，该值为用户组 ID（g-********）， 当PrincipalType取值为User时，该值为用户 ID（u-********）。 	
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def DeprovisionStrategy(self):
        r"""当您移除一个集团账号目标账号上使用某权限配置的最后一个授权时，是否同时解除权限配置部署。取值： DeprovisionForLastRoleAssignmentOnAccount：解除权限配置部署。 None（默认值）：不解除权限配置部署。
        :rtype: str
        """
        return self._DeprovisionStrategy

    @DeprovisionStrategy.setter
    def DeprovisionStrategy(self, DeprovisionStrategy):
        self._DeprovisionStrategy = DeprovisionStrategy


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._TargetType = params.get("TargetType")
        self._TargetUin = params.get("TargetUin")
        self._PrincipalType = params.get("PrincipalType")
        self._PrincipalId = params.get("PrincipalId")
        self._DeprovisionStrategy = params.get("DeprovisionStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoleAssignmentResponse(AbstractModel):
    r"""DeleteRoleAssignment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Task: 任务详情
        :type Task: :class:`tencentcloud.organization.v20210331.models.TaskInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Task = None
        self._RequestId = None

    @property
    def Task(self):
        r"""任务详情
        :rtype: :class:`tencentcloud.organization.v20210331.models.TaskInfo`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

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
        if params.get("Task") is not None:
            self._Task = TaskInfo()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class DeleteRoleConfigurationRequest(AbstractModel):
    r"""DeleteRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置 ID
        :type RoleConfigurationId: str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None

    @property
    def ZoneId(self):
        r"""空间 ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置 ID
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoleConfigurationResponse(AbstractModel):
    r"""DeleteRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteSCIMCredentialRequest(AbstractModel):
    r"""DeleteSCIMCredential请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _CredentialId: SCIM密钥ID。scimcred-前缀开头，后面是12位随机数字/小写字母。
        :type CredentialId: str
        """
        self._ZoneId = None
        self._CredentialId = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CredentialId(self):
        r"""SCIM密钥ID。scimcred-前缀开头，后面是12位随机数字/小写字母。
        :rtype: str
        """
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._CredentialId = params.get("CredentialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSCIMCredentialResponse(AbstractModel):
    r"""DeleteSCIMCredential返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteShareUnitMembersRequest(AbstractModel):
    r"""DeleteShareUnitMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _Area: 共享单元地域。
        :type Area: str
        :param _Members: 成员列表。
        :type Members: list of ShareMember
        """
        self._UnitId = None
        self._Area = None
        self._Members = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def Area(self):
        r"""共享单元地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Members(self):
        r"""成员列表。
        :rtype: list of ShareMember
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        self._Area = params.get("Area")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = ShareMember()
                obj._deserialize(item)
                self._Members.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShareUnitMembersResponse(AbstractModel):
    r"""DeleteShareUnitMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteShareUnitRequest(AbstractModel):
    r"""DeleteShareUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        """
        self._UnitId = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShareUnitResourcesRequest(AbstractModel):
    r"""DeleteShareUnitResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _Area: 共享单元地域。
        :type Area: str
        :param _Type: 共享资源类型。支持共享的资源类型,请参见[资源共享概述](https://cloud.tencent.com/document/product/850/59489)
        :type Type: str
        :param _Resources: 共享资源列表。最大10个。
        :type Resources: list of ShareResource
        """
        self._UnitId = None
        self._Area = None
        self._Type = None
        self._Resources = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def Area(self):
        r"""共享单元地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Type(self):
        r"""共享资源类型。支持共享的资源类型,请参见[资源共享概述](https://cloud.tencent.com/document/product/850/59489)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Resources(self):
        r"""共享资源列表。最大10个。
        :rtype: list of ShareResource
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        self._Area = params.get("Area")
        self._Type = params.get("Type")
        if params.get("Resources") is not None:
            self._Resources = []
            for item in params.get("Resources"):
                obj = ShareResource()
                obj._deserialize(item)
                self._Resources.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteShareUnitResourcesResponse(AbstractModel):
    r"""DeleteShareUnitResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteShareUnitResponse(AbstractModel):
    r"""DeleteShareUnit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteUserRequest(AbstractModel):
    r"""DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _UserId: 用户 ID。
        :type UserId: str
        """
        self._ZoneId = None
        self._UserId = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserId(self):
        r"""用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    r"""DeleteUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteUserSyncProvisioningRequest(AbstractModel):
    r"""DeleteUserSyncProvisioning请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _UserProvisioningId: 用户同步的ID。
        :type UserProvisioningId: str
        """
        self._ZoneId = None
        self._UserProvisioningId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserProvisioningId(self):
        r"""用户同步的ID。
        :rtype: str
        """
        return self._UserProvisioningId

    @UserProvisioningId.setter
    def UserProvisioningId(self, UserProvisioningId):
        self._UserProvisioningId = UserProvisioningId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserProvisioningId = params.get("UserProvisioningId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserSyncProvisioningResponse(AbstractModel):
    r"""DeleteUserSyncProvisioning返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Tasks: 任务详情。
        :type Tasks: :class:`tencentcloud.organization.v20210331.models.UserProvisioningsTask`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Tasks = None
        self._RequestId = None

    @property
    def Tasks(self):
        r"""任务详情。
        :rtype: :class:`tencentcloud.organization.v20210331.models.UserProvisioningsTask`
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        if params.get("Tasks") is not None:
            self._Tasks = UserProvisioningsTask()
            self._Tasks._deserialize(params.get("Tasks"))
        self._RequestId = params.get("RequestId")


class DescribeEffectivePolicyRequest(AbstractModel):
    r"""DescribeEffectivePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetId: 账号uin或者节点id。
        :type TargetId: int
        """
        self._TargetId = None

    @property
    def TargetId(self):
        r"""账号uin或者节点id。
        :rtype: int
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEffectivePolicyResponse(AbstractModel):
    r"""DescribeEffectivePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EffectivePolicy: 有效策略。
        :type EffectivePolicy: :class:`tencentcloud.organization.v20210331.models.EffectivePolicy`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EffectivePolicy = None
        self._RequestId = None

    @property
    def EffectivePolicy(self):
        r"""有效策略。
        :rtype: :class:`tencentcloud.organization.v20210331.models.EffectivePolicy`
        """
        return self._EffectivePolicy

    @EffectivePolicy.setter
    def EffectivePolicy(self, EffectivePolicy):
        self._EffectivePolicy = EffectivePolicy

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
        if params.get("EffectivePolicy") is not None:
            self._EffectivePolicy = EffectivePolicy()
            self._EffectivePolicy._deserialize(params.get("EffectivePolicy"))
        self._RequestId = params.get("RequestId")


class DescribeIdentityCenterRequest(AbstractModel):
    r"""DescribeIdentityCenter请求参数结构体

    """


class DescribeIdentityCenterResponse(AbstractModel):
    r"""DescribeIdentityCenter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _ZoneName: 空间名，必须全局唯一。包含小写字母、数字和短划线（-）。不能以短划线（-）开头或结尾，且不能有两个连续的短划线（-）。长度：2~64 个字符。
        :type ZoneName: str
        :param _ServiceStatus: 服务开启状态，Disabled代表未开通，Enabled代表已开通
        :type ServiceStatus: str
        :param _ScimSyncStatus: SCIM 同步状态。Enabled：启用。 Disabled：禁用。
        :type ScimSyncStatus: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._ZoneName = None
        self._ServiceStatus = None
        self._ScimSyncStatus = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneName(self):
        r"""空间名，必须全局唯一。包含小写字母、数字和短划线（-）。不能以短划线（-）开头或结尾，且不能有两个连续的短划线（-）。长度：2~64 个字符。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName

    @property
    def ServiceStatus(self):
        r"""服务开启状态，Disabled代表未开通，Enabled代表已开通
        :rtype: str
        """
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def ScimSyncStatus(self):
        r"""SCIM 同步状态。Enabled：启用。 Disabled：禁用。
        :rtype: str
        """
        return self._ScimSyncStatus

    @ScimSyncStatus.setter
    def ScimSyncStatus(self, ScimSyncStatus):
        self._ScimSyncStatus = ScimSyncStatus

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

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
        self._ZoneId = params.get("ZoneId")
        self._ZoneName = params.get("ZoneName")
        self._ServiceStatus = params.get("ServiceStatus")
        self._ScimSyncStatus = params.get("ScimSyncStatus")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationAuthNodeRequest(AbstractModel):
    r"""DescribeOrganizationAuthNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。默认值：10。
        :type Limit: int
        :param _AuthName: 互信主体名称。
        :type AuthName: str
        """
        self._Offset = None
        self._Limit = None
        self._AuthName = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍。默认值 : 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。默认值：10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def AuthName(self):
        r"""互信主体名称。
        :rtype: str
        """
        return self._AuthName

    @AuthName.setter
    def AuthName(self, AuthName):
        self._AuthName = AuthName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AuthName = params.get("AuthName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationAuthNodeResponse(AbstractModel):
    r"""DescribeOrganizationAuthNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数。
        :type Total: int
        :param _Items: 条目详情。
        :type Items: list of AuthNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""条目详情。
        :rtype: list of AuthNode
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = AuthNode()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationFinancialByMemberRequest(AbstractModel):
    r"""DescribeOrganizationFinancialByMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 查询开始月份。格式：yyyy-mm，例如：2021-01。
        :type Month: str
        :param _Limit: 限制数目。取值范围：1~50，默认值：10	
        :type Limit: int
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _EndMonth: 查询结束月份。格式：yyyy-mm，例如：2021-01,默认值为查询开始月份。
        :type EndMonth: str
        :param _MemberUins: 查询成员列表。 最大100个
        :type MemberUins: list of int
        :param _ProductCodes: 查询产品列表。 最大100个
        :type ProductCodes: list of str
        """
        self._Month = None
        self._Limit = None
        self._Offset = None
        self._EndMonth = None
        self._MemberUins = None
        self._ProductCodes = None

    @property
    def Month(self):
        r"""查询开始月份。格式：yyyy-mm，例如：2021-01。
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50，默认值：10	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍，默认值 : 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EndMonth(self):
        r"""查询结束月份。格式：yyyy-mm，例如：2021-01,默认值为查询开始月份。
        :rtype: str
        """
        return self._EndMonth

    @EndMonth.setter
    def EndMonth(self, EndMonth):
        self._EndMonth = EndMonth

    @property
    def MemberUins(self):
        r"""查询成员列表。 最大100个
        :rtype: list of int
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def ProductCodes(self):
        r"""查询产品列表。 最大100个
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EndMonth = params.get("EndMonth")
        self._MemberUins = params.get("MemberUins")
        self._ProductCodes = params.get("ProductCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationFinancialByMemberResponse(AbstractModel):
    r"""DescribeOrganizationFinancialByMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCost: 当月总消耗。
        :type TotalCost: float
        :param _Items: 成员消耗详情。
        :type Items: list of OrgMemberFinancial
        :param _Total: 总数目。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCost = None
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def TotalCost(self):
        r"""当月总消耗。
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Items(self):
        r"""成员消耗详情。
        :rtype: list of OrgMemberFinancial
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        r"""总数目。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._TotalCost = params.get("TotalCost")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberFinancial()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationFinancialByMonthRequest(AbstractModel):
    r"""DescribeOrganizationFinancialByMonth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 查询月数。取值范围：1~6，默认值：6
        :type Limit: int
        :param _EndMonth: 查询结束月份。格式：yyyy-mm，例如：2021-01
        :type EndMonth: str
        :param _MemberUins: 查询成员列表。 最大100个
        :type MemberUins: list of int
        :param _ProductCodes: 查询产品列表。 最大100个
        :type ProductCodes: list of str
        """
        self._Limit = None
        self._EndMonth = None
        self._MemberUins = None
        self._ProductCodes = None

    @property
    def Limit(self):
        r"""查询月数。取值范围：1~6，默认值：6
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def EndMonth(self):
        r"""查询结束月份。格式：yyyy-mm，例如：2021-01
        :rtype: str
        """
        return self._EndMonth

    @EndMonth.setter
    def EndMonth(self, EndMonth):
        self._EndMonth = EndMonth

    @property
    def MemberUins(self):
        r"""查询成员列表。 最大100个
        :rtype: list of int
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def ProductCodes(self):
        r"""查询产品列表。 最大100个
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._EndMonth = params.get("EndMonth")
        self._MemberUins = params.get("MemberUins")
        self._ProductCodes = params.get("ProductCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationFinancialByMonthResponse(AbstractModel):
    r"""DescribeOrganizationFinancialByMonth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 产品消耗详情。
        :type Items: list of OrgFinancialByMonth
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        r"""产品消耗详情。
        :rtype: list of OrgFinancialByMonth
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgFinancialByMonth()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationFinancialByProductRequest(AbstractModel):
    r"""DescribeOrganizationFinancialByProduct请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Month: 查询开始月份。格式：yyyy-mm，例如：2021-01
        :type Month: str
        :param _Limit: 限制数目。取值范围：1~50，默认值：10	
        :type Limit: int
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _EndMonth: 查询结束月份。格式：yyyy-mm，例如：2021-01,默认值为查询开始月份
        :type EndMonth: str
        :param _MemberUins: 查询成员列表。 最大100个
        :type MemberUins: list of int
        :param _ProductCodes: 查询产品列表。 最大100个
        :type ProductCodes: list of str
        """
        self._Month = None
        self._Limit = None
        self._Offset = None
        self._EndMonth = None
        self._MemberUins = None
        self._ProductCodes = None

    @property
    def Month(self):
        r"""查询开始月份。格式：yyyy-mm，例如：2021-01
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50，默认值：10	
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍，默认值 : 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EndMonth(self):
        r"""查询结束月份。格式：yyyy-mm，例如：2021-01,默认值为查询开始月份
        :rtype: str
        """
        return self._EndMonth

    @EndMonth.setter
    def EndMonth(self, EndMonth):
        self._EndMonth = EndMonth

    @property
    def MemberUins(self):
        r"""查询成员列表。 最大100个
        :rtype: list of int
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def ProductCodes(self):
        r"""查询产品列表。 最大100个
        :rtype: list of str
        """
        return self._ProductCodes

    @ProductCodes.setter
    def ProductCodes(self, ProductCodes):
        self._ProductCodes = ProductCodes


    def _deserialize(self, params):
        self._Month = params.get("Month")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EndMonth = params.get("EndMonth")
        self._MemberUins = params.get("MemberUins")
        self._ProductCodes = params.get("ProductCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationFinancialByProductResponse(AbstractModel):
    r"""DescribeOrganizationFinancialByProduct返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCost: 当月总消耗。
        :type TotalCost: float
        :param _Items: 产品消耗详情。
        :type Items: list of OrgProductFinancial
        :param _Total: 总数目。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCost = None
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def TotalCost(self):
        r"""当月总消耗。
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Items(self):
        r"""产品消耗详情。
        :rtype: list of OrgProductFinancial
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        r"""总数目。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._TotalCost = params.get("TotalCost")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgProductFinancial()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthAccountsRequest(AbstractModel):
    r"""DescribeOrganizationMemberAuthAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。默认值：10。
        :type Limit: int
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PolicyId: 策略ID。可以通过[DescribeOrganizationMemberPolicies](https://cloud.tencent.com/document/product/850/82935)获取
        :type PolicyId: int
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._PolicyId = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍。默认值 : 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。默认值：10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PolicyId(self):
        r"""策略ID。可以通过[DescribeOrganizationMemberPolicies](https://cloud.tencent.com/document/product/850/82935)获取
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthAccountsResponse(AbstractModel):
    r"""DescribeOrganizationMemberAuthAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 列表
        :type Items: list of OrgMemberAuthAccount
        :param _Total: 总数目
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        r"""列表
        :rtype: list of OrgMemberAuthAccount
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        r"""总数目
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberAuthAccount()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberAuthIdentitiesRequest(AbstractModel):
    r"""DescribeOrganizationMemberAuthIdentities请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50，默认值：10
        :type Limit: int
        :param _MemberUin: 组织成员Uin。入参MemberUin与IdentityId至少填写一个
        :type MemberUin: int
        :param _IdentityId: 身份ID。入参MemberUin与IdentityId至少填写一个, 可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :type IdentityId: int
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._IdentityId = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍，默认值 : 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50，默认值：10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MemberUin(self):
        r"""组织成员Uin。入参MemberUin与IdentityId至少填写一个
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def IdentityId(self):
        r"""身份ID。入参MemberUin与IdentityId至少填写一个, 可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._IdentityId = params.get("IdentityId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberAuthIdentitiesResponse(AbstractModel):
    r"""DescribeOrganizationMemberAuthIdentities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 授权身份列表。
        :type Items: list of OrgMemberAuthIdentity
        :param _Total: 总数目。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        r"""授权身份列表。
        :rtype: list of OrgMemberAuthIdentity
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        r"""总数目。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberAuthIdentity()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberEmailBindRequest(AbstractModel):
    r"""DescribeOrganizationMemberEmailBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        """
        self._MemberUin = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberEmailBindResponse(AbstractModel):
    r"""DescribeOrganizationMemberEmailBind返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BindId: 绑定ID。
        :type BindId: int
        :param _ApplyTime: 申请时间。
        :type ApplyTime: str
        :param _Email: 邮箱地址。
        :type Email: str
        :param _Phone: 安全手机号。
        :type Phone: str
        :param _BindStatus: 绑定状态。    未绑定：Unbound，待激活：Valid，绑定成功：Success，绑定失败：Failed
        :type BindStatus: str
        :param _BindTime: 绑定时间。
        :type BindTime: str
        :param _Description: 失败说明。
        :type Description: str
        :param _PhoneBind: 安全手机绑定状态 。 未绑定：0，已绑定：1
        :type PhoneBind: int
        :param _CountryCode: 国际区号。
        :type CountryCode: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BindId = None
        self._ApplyTime = None
        self._Email = None
        self._Phone = None
        self._BindStatus = None
        self._BindTime = None
        self._Description = None
        self._PhoneBind = None
        self._CountryCode = None
        self._RequestId = None

    @property
    def BindId(self):
        r"""绑定ID。
        :rtype: int
        """
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def ApplyTime(self):
        r"""申请时间。
        :rtype: str
        """
        return self._ApplyTime

    @ApplyTime.setter
    def ApplyTime(self, ApplyTime):
        self._ApplyTime = ApplyTime

    @property
    def Email(self):
        r"""邮箱地址。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        r"""安全手机号。
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def BindStatus(self):
        r"""绑定状态。    未绑定：Unbound，待激活：Valid，绑定成功：Success，绑定失败：Failed
        :rtype: str
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def BindTime(self):
        r"""绑定时间。
        :rtype: str
        """
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime

    @property
    def Description(self):
        r"""失败说明。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PhoneBind(self):
        r"""安全手机绑定状态 。 未绑定：0，已绑定：1
        :rtype: int
        """
        return self._PhoneBind

    @PhoneBind.setter
    def PhoneBind(self, PhoneBind):
        self._PhoneBind = PhoneBind

    @property
    def CountryCode(self):
        r"""国际区号。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

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
        self._BindId = params.get("BindId")
        self._ApplyTime = params.get("ApplyTime")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._BindStatus = params.get("BindStatus")
        self._BindTime = params.get("BindTime")
        self._Description = params.get("Description")
        self._PhoneBind = params.get("PhoneBind")
        self._CountryCode = params.get("CountryCode")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMemberPoliciesRequest(AbstractModel):
    r"""DescribeOrganizationMemberPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。默认值：10。
        :type Limit: int
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _SearchKey: 搜索关键字。可用于策略名或描述搜索
        :type SearchKey: str
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._SearchKey = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍。默认值 : 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。默认值：10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def SearchKey(self):
        r"""搜索关键字。可用于策略名或描述搜索
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMemberPoliciesResponse(AbstractModel):
    r"""DescribeOrganizationMemberPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 列表。
        :type Items: list of OrgMemberPolicy
        :param _Total: 总数目。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        r"""列表。
        :rtype: list of OrgMemberPolicy
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        r"""总数目。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMemberPolicy()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMembersAuthPolicyRequest(AbstractModel):
    r"""DescribeOrganizationMembersAuthPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。默认值：10。
        :type Limit: int
        :param _MemberUin: 成员uin。
        :type MemberUin: int
        :param _OrgSubAccountUin: 集团管理员子账号uin。
        :type OrgSubAccountUin: int
        :param _PolicyId: 成员访问策略Id。
        :type PolicyId: int
        """
        self._Offset = None
        self._Limit = None
        self._MemberUin = None
        self._OrgSubAccountUin = None
        self._PolicyId = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍。默认值 : 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。默认值：10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def MemberUin(self):
        r"""成员uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def OrgSubAccountUin(self):
        r"""集团管理员子账号uin。
        :rtype: int
        """
        return self._OrgSubAccountUin

    @OrgSubAccountUin.setter
    def OrgSubAccountUin(self, OrgSubAccountUin):
        self._OrgSubAccountUin = OrgSubAccountUin

    @property
    def PolicyId(self):
        r"""成员访问策略Id。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._MemberUin = params.get("MemberUin")
        self._OrgSubAccountUin = params.get("OrgSubAccountUin")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMembersAuthPolicyResponse(AbstractModel):
    r"""DescribeOrganizationMembersAuthPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 访问授权策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of OrgMembersAuthPolicy
        :param _Total: 总数目。
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        r"""访问授权策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OrgMembersAuthPolicy
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        r"""总数目。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMembersAuthPolicy()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationMembersRequest(AbstractModel):
    r"""DescribeOrganizationMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50，默认值：10
        :type Limit: int
        :param _Lang: 国际站：en，国内站：zh
        :type Lang: str
        :param _SearchKey: 成员名称或者成员ID搜索。
        :type SearchKey: str
        :param _AuthName: 主体名称搜索。
        :type AuthName: str
        :param _Product: 可信服务产品简称。可信服务管理员查询时必须指定
        :type Product: str
        :param _Tags: 成员标签搜索列表，最大10个
        :type Tags: list of Tag
        :param _NodeId: 组织单元ID
        :type NodeId: int
        :param _NodeName: 组织单元名称
        :type NodeName: str
        """
        self._Offset = None
        self._Limit = None
        self._Lang = None
        self._SearchKey = None
        self._AuthName = None
        self._Product = None
        self._Tags = None
        self._NodeId = None
        self._NodeName = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍，默认值 : 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50，默认值：10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Lang(self):
        r"""国际站：en，国内站：zh
        :rtype: str
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def SearchKey(self):
        r"""成员名称或者成员ID搜索。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def AuthName(self):
        r"""主体名称搜索。
        :rtype: str
        """
        return self._AuthName

    @AuthName.setter
    def AuthName(self, AuthName):
        self._AuthName = AuthName

    @property
    def Product(self):
        r"""可信服务产品简称。可信服务管理员查询时必须指定
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Tags(self):
        r"""成员标签搜索列表，最大10个
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NodeId(self):
        r"""组织单元ID
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        r"""组织单元名称
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Lang = params.get("Lang")
        self._SearchKey = params.get("SearchKey")
        self._AuthName = params.get("AuthName")
        self._Product = params.get("Product")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationMembersResponse(AbstractModel):
    r"""DescribeOrganizationMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 成员列表。
        :type Items: list of OrgMember
        :param _Total: 总数目。
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._Total = None
        self._RequestId = None

    @property
    def Items(self):
        r"""成员列表。
        :rtype: list of OrgMember
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def Total(self):
        r"""总数目。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgMember()
                obj._deserialize(item)
                self._Items.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOrganizationNodesRequest(AbstractModel):
    r"""DescribeOrganizationNodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 限制数目。最大50
        :type Limit: int
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Tags: 部门标签搜索列表，最大10个
        :type Tags: list of Tag
        """
        self._Limit = None
        self._Offset = None
        self._Tags = None

    @property
    def Limit(self):
        r"""限制数目。最大50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍。默认值 : 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Tags(self):
        r"""部门标签搜索列表，最大10个
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
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
        


class DescribeOrganizationNodesResponse(AbstractModel):
    r"""DescribeOrganizationNodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数。
        :type Total: int
        :param _Items: 列表详情。
        :type Items: list of OrgNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""列表详情。
        :rtype: list of OrgNode
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgNode()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganizationRequest(AbstractModel):
    r"""DescribeOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Lang: 国际站：en，国内站：zh
        :type Lang: str
        :param _Product: 可信服务产品简称。查询是否该可信服务管理员时必须指定
        :type Product: str
        """
        self._Lang = None
        self._Product = None

    @property
    def Lang(self):
        r"""国际站：en，国内站：zh
        :rtype: str
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang

    @property
    def Product(self):
        r"""可信服务产品简称。查询是否该可信服务管理员时必须指定
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Lang = params.get("Lang")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganizationResponse(AbstractModel):
    r"""DescribeOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgId: 企业组织ID。
        :type OrgId: int
        :param _HostUin: 创建者UIN。
        :type HostUin: int
        :param _NickName: 创建者昵称。
        :type NickName: str
        :param _OrgType: 企业组织类型。
        :type OrgType: int
        :param _IsManager: 是否组织管理员。是：true ，否：false
        :type IsManager: bool
        :param _OrgPolicyType: 策略类型。财务管理：Financial
        :type OrgPolicyType: str
        :param _OrgPolicyName: 策略名。
        :type OrgPolicyName: str
        :param _OrgPermission: 成员财务权限列表。
        :type OrgPermission: list of OrgPermission
        :param _RootNodeId: 组织根节点ID。
        :type RootNodeId: int
        :param _CreateTime: 组织创建时间。
        :type CreateTime: str
        :param _JoinTime: 成员加入时间。
        :type JoinTime: str
        :param _IsAllowQuit: 成员是否允许退出。允许：Allow，不允许：Denied
        :type IsAllowQuit: str
        :param _PayUin: 代付者Uin。
        :type PayUin: str
        :param _PayName: 代付者名称。
        :type PayName: str
        :param _IsAssignManager: 是否可信服务管理员。是：true，否：false
        :type IsAssignManager: bool
        :param _IsAuthManager: 是否实名主体管理员。是：true，否：false
        :type IsAuthManager: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrgId = None
        self._HostUin = None
        self._NickName = None
        self._OrgType = None
        self._IsManager = None
        self._OrgPolicyType = None
        self._OrgPolicyName = None
        self._OrgPermission = None
        self._RootNodeId = None
        self._CreateTime = None
        self._JoinTime = None
        self._IsAllowQuit = None
        self._PayUin = None
        self._PayName = None
        self._IsAssignManager = None
        self._IsAuthManager = None
        self._RequestId = None

    @property
    def OrgId(self):
        r"""企业组织ID。
        :rtype: int
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def HostUin(self):
        r"""创建者UIN。
        :rtype: int
        """
        return self._HostUin

    @HostUin.setter
    def HostUin(self, HostUin):
        self._HostUin = HostUin

    @property
    def NickName(self):
        r"""创建者昵称。
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def OrgType(self):
        r"""企业组织类型。
        :rtype: int
        """
        return self._OrgType

    @OrgType.setter
    def OrgType(self, OrgType):
        self._OrgType = OrgType

    @property
    def IsManager(self):
        r"""是否组织管理员。是：true ，否：false
        :rtype: bool
        """
        return self._IsManager

    @IsManager.setter
    def IsManager(self, IsManager):
        self._IsManager = IsManager

    @property
    def OrgPolicyType(self):
        r"""策略类型。财务管理：Financial
        :rtype: str
        """
        return self._OrgPolicyType

    @OrgPolicyType.setter
    def OrgPolicyType(self, OrgPolicyType):
        self._OrgPolicyType = OrgPolicyType

    @property
    def OrgPolicyName(self):
        r"""策略名。
        :rtype: str
        """
        return self._OrgPolicyName

    @OrgPolicyName.setter
    def OrgPolicyName(self, OrgPolicyName):
        self._OrgPolicyName = OrgPolicyName

    @property
    def OrgPermission(self):
        r"""成员财务权限列表。
        :rtype: list of OrgPermission
        """
        return self._OrgPermission

    @OrgPermission.setter
    def OrgPermission(self, OrgPermission):
        self._OrgPermission = OrgPermission

    @property
    def RootNodeId(self):
        r"""组织根节点ID。
        :rtype: int
        """
        return self._RootNodeId

    @RootNodeId.setter
    def RootNodeId(self, RootNodeId):
        self._RootNodeId = RootNodeId

    @property
    def CreateTime(self):
        r"""组织创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def JoinTime(self):
        r"""成员加入时间。
        :rtype: str
        """
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime

    @property
    def IsAllowQuit(self):
        r"""成员是否允许退出。允许：Allow，不允许：Denied
        :rtype: str
        """
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        r"""代付者Uin。
        :rtype: str
        """
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def PayName(self):
        r"""代付者名称。
        :rtype: str
        """
        return self._PayName

    @PayName.setter
    def PayName(self, PayName):
        self._PayName = PayName

    @property
    def IsAssignManager(self):
        r"""是否可信服务管理员。是：true，否：false
        :rtype: bool
        """
        return self._IsAssignManager

    @IsAssignManager.setter
    def IsAssignManager(self, IsAssignManager):
        self._IsAssignManager = IsAssignManager

    @property
    def IsAuthManager(self):
        r"""是否实名主体管理员。是：true，否：false
        :rtype: bool
        """
        return self._IsAuthManager

    @IsAuthManager.setter
    def IsAuthManager(self, IsAuthManager):
        self._IsAuthManager = IsAuthManager

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
        self._OrgId = params.get("OrgId")
        self._HostUin = params.get("HostUin")
        self._NickName = params.get("NickName")
        self._OrgType = params.get("OrgType")
        self._IsManager = params.get("IsManager")
        self._OrgPolicyType = params.get("OrgPolicyType")
        self._OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self._OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self._OrgPermission.append(obj)
        self._RootNodeId = params.get("RootNodeId")
        self._CreateTime = params.get("CreateTime")
        self._JoinTime = params.get("JoinTime")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        self._PayName = params.get("PayName")
        self._IsAssignManager = params.get("IsAssignManager")
        self._IsAuthManager = params.get("IsAuthManager")
        self._RequestId = params.get("RequestId")


class DescribePolicyConfigRequest(AbstractModel):
    r"""DescribePolicyConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 企业组织Id。可以调用[DescribeOrganization](https://cloud.tencent.com/document/product/850/67059)获取
        :type OrganizationId: int
        :param _Type: 策略类型。默认值0，取值范围：0-服务控制策略、1-标签策略
        :type Type: int
        """
        self._OrganizationId = None
        self._Type = None

    @property
    def OrganizationId(self):
        r"""企业组织Id。可以调用[DescribeOrganization](https://cloud.tencent.com/document/product/850/67059)获取
        :rtype: int
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def Type(self):
        r"""策略类型。默认值0，取值范围：0-服务控制策略、1-标签策略
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyConfigResponse(AbstractModel):
    r"""DescribePolicyConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 开启状态。0-未开启、1-开启
        :type Status: int
        :param _Type: 策略类型。SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type Type: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._Type = None
        self._RequestId = None

    @property
    def Status(self):
        r"""开启状态。0-未开启、1-开启
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Type(self):
        r"""策略类型。SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

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
        self._Status = params.get("Status")
        self._Type = params.get("Type")
        self._RequestId = params.get("RequestId")


class DescribePolicyRequest(AbstractModel):
    r"""DescribePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略Id。可以调用[ListPolicies](https://cloud.tencent.com/document/product/850/105311)获取
        :type PolicyId: int
        :param _PolicyType: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type PolicyType: str
        """
        self._PolicyId = None
        self._PolicyType = None

    @property
    def PolicyId(self):
        r"""策略Id。可以调用[ListPolicies](https://cloud.tencent.com/document/product/850/105311)获取
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyType(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyType = params.get("PolicyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyResponse(AbstractModel):
    r"""DescribePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略Id。
        :type PolicyId: int
        :param _PolicyName: 策略名称。
        :type PolicyName: str
        :param _Type: 策略类型。1-自定义 2-预设策略
        :type Type: int
        :param _Description: 策略描述。
        :type Description: str
        :param _PolicyDocument: 策略文档。
        :type PolicyDocument: str
        :param _UpdateTime: 策略更新时间。
        :type UpdateTime: str
        :param _AddTime: 策略创建时间。
        :type AddTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._Type = None
        self._Description = None
        self._PolicyDocument = None
        self._UpdateTime = None
        self._AddTime = None
        self._RequestId = None

    @property
    def PolicyId(self):
        r"""策略Id。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        r"""策略名称。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Type(self):
        r"""策略类型。1-自定义 2-预设策略
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        r"""策略描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PolicyDocument(self):
        r"""策略文档。
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument

    @property
    def UpdateTime(self):
        r"""策略更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AddTime(self):
        r"""策略创建时间。
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

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
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        self._PolicyDocument = params.get("PolicyDocument")
        self._UpdateTime = params.get("UpdateTime")
        self._AddTime = params.get("AddTime")
        self._RequestId = params.get("RequestId")


class DescribeResourceToShareMemberRequest(AbstractModel):
    r"""DescribeResourceToShareMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Area: 共享地域。可通过接口[DescribeShareAreas](https://cloud.tencent.com/document/product/850/103050)获取支持共享的地域。
        :type Area: str
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。
        :type Limit: int
        :param _SearchKey: 搜索关键字，支持业务资源ID搜索。
        :type SearchKey: str
        :param _Type: 共享资源类型。支持共享的资源类型,请参见[资源共享概述](https://cloud.tencent.com/document/product/850/59489)
        :type Type: str
        :param _ProductResourceIds: 业务资源ID。最大50个
        :type ProductResourceIds: list of str
        """
        self._Area = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._Type = None
        self._ProductResourceIds = None

    @property
    def Area(self):
        r"""共享地域。可通过接口[DescribeShareAreas](https://cloud.tencent.com/document/product/850/103050)获取支持共享的地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍。默认值 : 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        r"""搜索关键字，支持业务资源ID搜索。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Type(self):
        r"""共享资源类型。支持共享的资源类型,请参见[资源共享概述](https://cloud.tencent.com/document/product/850/59489)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ProductResourceIds(self):
        r"""业务资源ID。最大50个
        :rtype: list of str
        """
        return self._ProductResourceIds

    @ProductResourceIds.setter
    def ProductResourceIds(self, ProductResourceIds):
        self._ProductResourceIds = ProductResourceIds


    def _deserialize(self, params):
        self._Area = params.get("Area")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._Type = params.get("Type")
        self._ProductResourceIds = params.get("ProductResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceToShareMemberResponse(AbstractModel):
    r"""DescribeResourceToShareMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        :param _Items: 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of ShareResourceToMember
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ShareResourceToMember
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ShareResourceToMember()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShareAreasRequest(AbstractModel):
    r"""DescribeShareAreas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Lang: 国际站：en，国内站：zh
        :type Lang: str
        """
        self._Lang = None

    @property
    def Lang(self):
        r"""国际站：en，国内站：zh
        :rtype: str
        """
        return self._Lang

    @Lang.setter
    def Lang(self, Lang):
        self._Lang = Lang


    def _deserialize(self, params):
        self._Lang = params.get("Lang")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShareAreasResponse(AbstractModel):
    r"""DescribeShareAreas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 详情
        :type Items: list of ShareArea
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._RequestId = None

    @property
    def Items(self):
        r"""详情
        :rtype: list of ShareArea
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ShareArea()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShareUnitMembersRequest(AbstractModel):
    r"""DescribeShareUnitMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _Area: 共享单元地域。
        :type Area: str
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。
        :type Limit: int
        :param _SearchKey: 搜索关键字。支持成员Uin搜索。
        :type SearchKey: str
        """
        self._UnitId = None
        self._Area = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def Area(self):
        r"""共享单元地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍，默认值 : 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        r"""搜索关键字。支持成员Uin搜索。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        self._Area = params.get("Area")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShareUnitMembersResponse(AbstractModel):
    r"""DescribeShareUnitMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数目。
        :type Total: int
        :param _Items: 共享单元成员列表。
        :type Items: list of ShareUnitMember
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数目。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""共享单元成员列表。
        :rtype: list of ShareUnitMember
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ShareUnitMember()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShareUnitResourcesRequest(AbstractModel):
    r"""DescribeShareUnitResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _Area: 共享单元地域。
        :type Area: str
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。
        :type Limit: int
        :param _SearchKey: 搜索关键字。支持产品资源ID搜索。
        :type SearchKey: str
        :param _Type: 共享资源类型。支持共享的资源类型,请参见[资源共享概述](https://cloud.tencent.com/document/product/850/59489)
        :type Type: str
        """
        self._UnitId = None
        self._Area = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._Type = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def Area(self):
        r"""共享单元地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍，默认值 : 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        r"""搜索关键字。支持产品资源ID搜索。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def Type(self):
        r"""共享资源类型。支持共享的资源类型,请参见[资源共享概述](https://cloud.tencent.com/document/product/850/59489)
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        self._Area = params.get("Area")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShareUnitResourcesResponse(AbstractModel):
    r"""DescribeShareUnitResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数目。
        :type Total: int
        :param _Items: 共享单元资源列表。
        :type Items: list of ShareUnitResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数目。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""共享单元资源列表。
        :rtype: list of ShareUnitResource
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ShareUnitResource()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeShareUnitsRequest(AbstractModel):
    r"""DescribeShareUnits请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Area: 共享单元地域。可通过接口[DescribeShareAreas](https://cloud.tencent.com/document/product/850/103050)获取支持共享的地域。
        :type Area: str
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。
        :type Limit: int
        :param _SearchKey: 搜索关键字。支持UnitId和Name搜索。
        :type SearchKey: str
        """
        self._Area = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None

    @property
    def Area(self):
        r"""共享单元地域。可通过接口[DescribeShareAreas](https://cloud.tencent.com/document/product/850/103050)获取支持共享的地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍。默认值 : 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        r"""搜索关键字。支持UnitId和Name搜索。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Area = params.get("Area")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeShareUnitsResponse(AbstractModel):
    r"""DescribeShareUnits返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数目。
        :type Total: int
        :param _Items: 共享单元列表。
        :type Items: list of ManagerShareUnit
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数目。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""共享单元列表。
        :rtype: list of ManagerShareUnit
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ManagerShareUnit()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class DetachPolicyRequest(AbstractModel):
    r"""DetachPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetId: 解绑策略目标ID。成员Uin或部门ID
        :type TargetId: int
        :param _TargetType: 目标类型。取值范围：NODE-部门、MEMBER-成员
        :type TargetType: str
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _Type: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type Type: str
        """
        self._TargetId = None
        self._TargetType = None
        self._PolicyId = None
        self._Type = None

    @property
    def TargetId(self):
        r"""解绑策略目标ID。成员Uin或部门ID
        :rtype: int
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        r"""目标类型。取值范围：NODE-部门、MEMBER-成员
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Type(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._PolicyId = params.get("PolicyId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachPolicyResponse(AbstractModel):
    r"""DetachPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DisablePolicyTypeRequest(AbstractModel):
    r"""DisablePolicyType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 企业组织Id。可以调用[DescribeOrganization](https://cloud.tencent.com/document/product/850/67059)获取
        :type OrganizationId: int
        :param _PolicyType: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type PolicyType: str
        """
        self._OrganizationId = None
        self._PolicyType = None

    @property
    def OrganizationId(self):
        r"""企业组织Id。可以调用[DescribeOrganization](https://cloud.tencent.com/document/product/850/67059)获取
        :rtype: int
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def PolicyType(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._PolicyType = params.get("PolicyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisablePolicyTypeResponse(AbstractModel):
    r"""DisablePolicyType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DismantleRoleConfigurationRequest(AbstractModel):
    r"""DismantleRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号。
        :type TargetType: str
        :param _TargetUin: 同步的集团账号目标账号的UIN。
        :type TargetUin: int
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._TargetType = None
        self._TargetUin = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号。
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetUin(self):
        r"""同步的集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._TargetType = params.get("TargetType")
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DismantleRoleConfigurationResponse(AbstractModel):
    r"""DismantleRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Task: 任务详情。
        :type Task: :class:`tencentcloud.organization.v20210331.models.RoleProvisioningsTask`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Task = None
        self._RequestId = None

    @property
    def Task(self):
        r"""任务详情。
        :rtype: :class:`tencentcloud.organization.v20210331.models.RoleProvisioningsTask`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

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
        if params.get("Task") is not None:
            self._Task = RoleProvisioningsTask()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class EffectivePolicy(AbstractModel):
    r"""有效策略。

    """

    def __init__(self):
        r"""
        :param _TargetId: 目标ID。
        :type TargetId: int
        :param _PolicyContent: 有效策略内容。
        :type PolicyContent: str
        :param _LastUpdatedTimestamp: 有效策略更新时间。
        :type LastUpdatedTimestamp: int
        """
        self._TargetId = None
        self._PolicyContent = None
        self._LastUpdatedTimestamp = None

    @property
    def TargetId(self):
        r"""目标ID。
        :rtype: int
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def PolicyContent(self):
        r"""有效策略内容。
        :rtype: str
        """
        return self._PolicyContent

    @PolicyContent.setter
    def PolicyContent(self, PolicyContent):
        self._PolicyContent = PolicyContent

    @property
    def LastUpdatedTimestamp(self):
        r"""有效策略更新时间。
        :rtype: int
        """
        return self._LastUpdatedTimestamp

    @LastUpdatedTimestamp.setter
    def LastUpdatedTimestamp(self, LastUpdatedTimestamp):
        self._LastUpdatedTimestamp = LastUpdatedTimestamp


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._PolicyContent = params.get("PolicyContent")
        self._LastUpdatedTimestamp = params.get("LastUpdatedTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnablePolicyTypeRequest(AbstractModel):
    r"""EnablePolicyType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrganizationId: 企业组织Id。可以调用[DescribeOrganization](https://cloud.tencent.com/document/product/850/67059)获取
        :type OrganizationId: int
        :param _PolicyType: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type PolicyType: str
        """
        self._OrganizationId = None
        self._PolicyType = None

    @property
    def OrganizationId(self):
        r"""企业组织Id。可以调用[DescribeOrganization](https://cloud.tencent.com/document/product/850/67059)获取
        :rtype: int
        """
        return self._OrganizationId

    @OrganizationId.setter
    def OrganizationId(self, OrganizationId):
        self._OrganizationId = OrganizationId

    @property
    def PolicyType(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType


    def _deserialize(self, params):
        self._OrganizationId = params.get("OrganizationId")
        self._PolicyType = params.get("PolicyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnablePolicyTypeResponse(AbstractModel):
    r"""EnablePolicyType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class GetExternalSAMLIdentityProviderRequest(AbstractModel):
    r"""GetExternalSAMLIdentityProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetExternalSAMLIdentityProviderResponse(AbstractModel):
    r"""GetExternalSAMLIdentityProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SAMLIdentityProviderConfiguration: saml 身份提供商配置信息。
        :type SAMLIdentityProviderConfiguration: :class:`tencentcloud.organization.v20210331.models.SAMLIdentityProviderConfiguration`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SAMLIdentityProviderConfiguration = None
        self._RequestId = None

    @property
    def SAMLIdentityProviderConfiguration(self):
        r"""saml 身份提供商配置信息。
        :rtype: :class:`tencentcloud.organization.v20210331.models.SAMLIdentityProviderConfiguration`
        """
        return self._SAMLIdentityProviderConfiguration

    @SAMLIdentityProviderConfiguration.setter
    def SAMLIdentityProviderConfiguration(self, SAMLIdentityProviderConfiguration):
        self._SAMLIdentityProviderConfiguration = SAMLIdentityProviderConfiguration

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
        if params.get("SAMLIdentityProviderConfiguration") is not None:
            self._SAMLIdentityProviderConfiguration = SAMLIdentityProviderConfiguration()
            self._SAMLIdentityProviderConfiguration._deserialize(params.get("SAMLIdentityProviderConfiguration"))
        self._RequestId = params.get("RequestId")


class GetGroupRequest(AbstractModel):
    r"""GetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _GroupId: 用户组的 ID。
        :type GroupId: str
        """
        self._ZoneId = None
        self._GroupId = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        r"""用户组的 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetGroupResponse(AbstractModel):
    r"""GetGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupInfo: 用户组信息
        :type GroupInfo: :class:`tencentcloud.organization.v20210331.models.GroupInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupInfo = None
        self._RequestId = None

    @property
    def GroupInfo(self):
        r"""用户组信息
        :rtype: :class:`tencentcloud.organization.v20210331.models.GroupInfo`
        """
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

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
        if params.get("GroupInfo") is not None:
            self._GroupInfo = GroupInfo()
            self._GroupInfo._deserialize(params.get("GroupInfo"))
        self._RequestId = params.get("RequestId")


class GetProvisioningTaskStatusRequest(AbstractModel):
    r"""GetProvisioningTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _TaskId: 任务ID。
        :type TaskId: str
        """
        self._ZoneId = None
        self._TaskId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetProvisioningTaskStatusResponse(AbstractModel):
    r"""GetProvisioningTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 任务状态信息。
        :type TaskStatus: :class:`tencentcloud.organization.v20210331.models.TaskStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatus = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        r"""任务状态信息。
        :rtype: :class:`tencentcloud.organization.v20210331.models.TaskStatus`
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

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
        if params.get("TaskStatus") is not None:
            self._TaskStatus = TaskStatus()
            self._TaskStatus._deserialize(params.get("TaskStatus"))
        self._RequestId = params.get("RequestId")


class GetRoleConfigurationRequest(AbstractModel):
    r"""GetRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置ID
        :type RoleConfigurationId: str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None

    @property
    def ZoneId(self):
        r"""空间 ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetRoleConfigurationResponse(AbstractModel):
    r"""GetRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleConfigurationInfo: 权限配置详情
        :type RoleConfigurationInfo: :class:`tencentcloud.organization.v20210331.models.RoleConfiguration`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleConfigurationInfo = None
        self._RequestId = None

    @property
    def RoleConfigurationInfo(self):
        r"""权限配置详情
        :rtype: :class:`tencentcloud.organization.v20210331.models.RoleConfiguration`
        """
        return self._RoleConfigurationInfo

    @RoleConfigurationInfo.setter
    def RoleConfigurationInfo(self, RoleConfigurationInfo):
        self._RoleConfigurationInfo = RoleConfigurationInfo

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
        if params.get("RoleConfigurationInfo") is not None:
            self._RoleConfigurationInfo = RoleConfiguration()
            self._RoleConfigurationInfo._deserialize(params.get("RoleConfigurationInfo"))
        self._RequestId = params.get("RequestId")


class GetSCIMSynchronizationStatusRequest(AbstractModel):
    r"""GetSCIMSynchronizationStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSCIMSynchronizationStatusResponse(AbstractModel):
    r"""GetSCIMSynchronizationStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SCIMSynchronizationStatus: SCIM 同步状态。Enabled：启用。 Disabled：禁用。
        :type SCIMSynchronizationStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SCIMSynchronizationStatus = None
        self._RequestId = None

    @property
    def SCIMSynchronizationStatus(self):
        r"""SCIM 同步状态。Enabled：启用。 Disabled：禁用。
        :rtype: str
        """
        return self._SCIMSynchronizationStatus

    @SCIMSynchronizationStatus.setter
    def SCIMSynchronizationStatus(self, SCIMSynchronizationStatus):
        self._SCIMSynchronizationStatus = SCIMSynchronizationStatus

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
        self._SCIMSynchronizationStatus = params.get("SCIMSynchronizationStatus")
        self._RequestId = params.get("RequestId")


class GetTaskStatusRequest(AbstractModel):
    r"""GetTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _TaskId: 任务ID。
        :type TaskId: str
        """
        self._ZoneId = None
        self._TaskId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTaskStatusResponse(AbstractModel):
    r"""GetTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskStatus: 任务状态信息。
        :type TaskStatus: :class:`tencentcloud.organization.v20210331.models.TaskStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskStatus = None
        self._RequestId = None

    @property
    def TaskStatus(self):
        r"""任务状态信息。
        :rtype: :class:`tencentcloud.organization.v20210331.models.TaskStatus`
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

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
        if params.get("TaskStatus") is not None:
            self._TaskStatus = TaskStatus()
            self._TaskStatus._deserialize(params.get("TaskStatus"))
        self._RequestId = params.get("RequestId")


class GetUserRequest(AbstractModel):
    r"""GetUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UserId: 用户 ID。
        :type UserId: str
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        """
        self._UserId = None
        self._ZoneId = None

    @property
    def UserId(self):
        r"""用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._UserId = params.get("UserId")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserResponse(AbstractModel):
    r"""GetUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户信息。
        :type UserInfo: :class:`tencentcloud.organization.v20210331.models.UserInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserInfo = None
        self._RequestId = None

    @property
    def UserInfo(self):
        r"""用户信息。
        :rtype: :class:`tencentcloud.organization.v20210331.models.UserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

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
        if params.get("UserInfo") is not None:
            self._UserInfo = UserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._RequestId = params.get("RequestId")


class GetUserSyncProvisioningRequest(AbstractModel):
    r"""GetUserSyncProvisioning请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _UserProvisioningId: CAM 用户同步的 ID。
        :type UserProvisioningId: str
        """
        self._ZoneId = None
        self._UserProvisioningId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserProvisioningId(self):
        r"""CAM 用户同步的 ID。
        :rtype: str
        """
        return self._UserProvisioningId

    @UserProvisioningId.setter
    def UserProvisioningId(self, UserProvisioningId):
        self._UserProvisioningId = UserProvisioningId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserProvisioningId = params.get("UserProvisioningId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetUserSyncProvisioningResponse(AbstractModel):
    r"""GetUserSyncProvisioning返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserProvisioning: CAM 用户同步信息。
        :type UserProvisioning: :class:`tencentcloud.organization.v20210331.models.UserProvisioning`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserProvisioning = None
        self._RequestId = None

    @property
    def UserProvisioning(self):
        r"""CAM 用户同步信息。
        :rtype: :class:`tencentcloud.organization.v20210331.models.UserProvisioning`
        """
        return self._UserProvisioning

    @UserProvisioning.setter
    def UserProvisioning(self, UserProvisioning):
        self._UserProvisioning = UserProvisioning

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
        if params.get("UserProvisioning") is not None:
            self._UserProvisioning = UserProvisioning()
            self._UserProvisioning._deserialize(params.get("UserProvisioning"))
        self._RequestId = params.get("RequestId")


class GetZoneSAMLServiceProviderInfoRequest(AbstractModel):
    r"""GetZoneSAMLServiceProviderInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetZoneSAMLServiceProviderInfoResponse(AbstractModel):
    r"""GetZoneSAMLServiceProviderInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SAMLServiceProvider: saml服务提供商配置信息
        :type SAMLServiceProvider: :class:`tencentcloud.organization.v20210331.models.SAMLServiceProvider`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SAMLServiceProvider = None
        self._RequestId = None

    @property
    def SAMLServiceProvider(self):
        r"""saml服务提供商配置信息
        :rtype: :class:`tencentcloud.organization.v20210331.models.SAMLServiceProvider`
        """
        return self._SAMLServiceProvider

    @SAMLServiceProvider.setter
    def SAMLServiceProvider(self, SAMLServiceProvider):
        self._SAMLServiceProvider = SAMLServiceProvider

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
        if params.get("SAMLServiceProvider") is not None:
            self._SAMLServiceProvider = SAMLServiceProvider()
            self._SAMLServiceProvider._deserialize(params.get("SAMLServiceProvider"))
        self._RequestId = params.get("RequestId")


class GetZoneStatisticsRequest(AbstractModel):
    r"""GetZoneStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        r"""空间ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetZoneStatisticsResponse(AbstractModel):
    r"""GetZoneStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneStatistics: 空间的统计信息。
        :type ZoneStatistics: :class:`tencentcloud.organization.v20210331.models.ZoneStatistics`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneStatistics = None
        self._RequestId = None

    @property
    def ZoneStatistics(self):
        r"""空间的统计信息。
        :rtype: :class:`tencentcloud.organization.v20210331.models.ZoneStatistics`
        """
        return self._ZoneStatistics

    @ZoneStatistics.setter
    def ZoneStatistics(self, ZoneStatistics):
        self._ZoneStatistics = ZoneStatistics

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
        if params.get("ZoneStatistics") is not None:
            self._ZoneStatistics = ZoneStatistics()
            self._ZoneStatistics._deserialize(params.get("ZoneStatistics"))
        self._RequestId = params.get("RequestId")


class GroupInfo(AbstractModel):
    r"""用户组信息。

    """

    def __init__(self):
        r"""
        :param _GroupName: 用户组的名称。
        :type GroupName: str
        :param _Description: 用户组的描述。
        :type Description: str
        :param _CreateTime: 用户组的创建时间。
        :type CreateTime: str
        :param _GroupType: 用户组的类型  Manual：手动创建，Synchronized：外部导入。
        :type GroupType: str
        :param _UpdateTime: 用户组的修改时间。
        :type UpdateTime: str
        :param _GroupId: 用户组的 ID。
        :type GroupId: str
        :param _MemberCount: 组员数量。
        :type MemberCount: int
        :param _IsSelected: 如果有入参FilterUsers，用户在用户组返回true，否则返回false
        :type IsSelected: bool
        """
        self._GroupName = None
        self._Description = None
        self._CreateTime = None
        self._GroupType = None
        self._UpdateTime = None
        self._GroupId = None
        self._MemberCount = None
        self._IsSelected = None

    @property
    def GroupName(self):
        r"""用户组的名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        r"""用户组的描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""用户组的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GroupType(self):
        r"""用户组的类型  Manual：手动创建，Synchronized：外部导入。
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def UpdateTime(self):
        r"""用户组的修改时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def GroupId(self):
        r"""用户组的 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def MemberCount(self):
        r"""组员数量。
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def IsSelected(self):
        r"""如果有入参FilterUsers，用户在用户组返回true，否则返回false
        :rtype: bool
        """
        return self._IsSelected

    @IsSelected.setter
    def IsSelected(self, IsSelected):
        self._IsSelected = IsSelected


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._GroupType = params.get("GroupType")
        self._UpdateTime = params.get("UpdateTime")
        self._GroupId = params.get("GroupId")
        self._MemberCount = params.get("MemberCount")
        self._IsSelected = params.get("IsSelected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupMembers(AbstractModel):
    r"""用户信息

    """

    def __init__(self):
        r"""
        :param _UserName: 查询username。
        :type UserName: str
        :param _DisplayName: 用户的显示名称。
        :type DisplayName: str
        :param _Description: 用户的描述。
        :type Description: str
        :param _Email: 用户的电子邮箱。目录内必须唯一。
        :type Email: str
        :param _UserStatus: 用户状态 Enabled：启用， Disabled：禁用。
        :type UserStatus: str
        :param _UserType: 用户类型  Manual：手动创建，Synchronized：外部导入。
        :type UserType: str
        :param _UserId: 用户 ID
        :type UserId: str
        :param _JoinTime: 用户加入用户组的时间
        :type JoinTime: str
        """
        self._UserName = None
        self._DisplayName = None
        self._Description = None
        self._Email = None
        self._UserStatus = None
        self._UserType = None
        self._UserId = None
        self._JoinTime = None

    @property
    def UserName(self):
        r"""查询username。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def DisplayName(self):
        r"""用户的显示名称。
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        r"""用户的描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Email(self):
        r"""用户的电子邮箱。目录内必须唯一。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def UserStatus(self):
        r"""用户状态 Enabled：启用， Disabled：禁用。
        :rtype: str
        """
        return self._UserStatus

    @UserStatus.setter
    def UserStatus(self, UserStatus):
        self._UserStatus = UserStatus

    @property
    def UserType(self):
        r"""用户类型  Manual：手动创建，Synchronized：外部导入。
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserId(self):
        r"""用户 ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def JoinTime(self):
        r"""用户加入用户组的时间
        :rtype: str
        """
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._Email = params.get("Email")
        self._UserStatus = params.get("UserStatus")
        self._UserType = params.get("UserType")
        self._UserId = params.get("UserId")
        self._JoinTime = params.get("JoinTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IdentityPolicy(AbstractModel):
    r"""组织身份策略

    """

    def __init__(self):
        r"""
        :param _PolicyId: CAM预设策略ID。PolicyType 为预设策略时有效且必选
        :type PolicyId: int
        :param _PolicyName: CAM预设策略名称。PolicyType 为预设策略时有效且必选
        :type PolicyName: str
        :param _PolicyType: 策略类型。取值 1-自定义策略  2-预设策略；默认值2
        :type PolicyType: int
        :param _PolicyDocument: 自定义策略内容，遵循CAM策略语法。PolicyType 为自定义策略时有效且必选
        :type PolicyDocument: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._PolicyType = None
        self._PolicyDocument = None

    @property
    def PolicyId(self):
        r"""CAM预设策略ID。PolicyType 为预设策略时有效且必选
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        r"""CAM预设策略名称。PolicyType 为预设策略时有效且必选
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyType(self):
        r"""策略类型。取值 1-自定义策略  2-预设策略；默认值2
        :rtype: int
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PolicyDocument(self):
        r"""自定义策略内容，遵循CAM策略语法。PolicyType 为自定义策略时有效且必选
        :rtype: str
        """
        return self._PolicyDocument

    @PolicyDocument.setter
    def PolicyDocument(self, PolicyDocument):
        self._PolicyDocument = PolicyDocument


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._PolicyType = params.get("PolicyType")
        self._PolicyDocument = params.get("PolicyDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InviteOrganizationMemberRequest(AbstractModel):
    r"""InviteOrganizationMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 被邀请账号Uin。
        :type MemberUin: int
        :param _Name: 成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type Name: str
        :param _PolicyType: 关系策略。取值：Financial
        :type PolicyType: str
        :param _PermissionIds: 成员财务权限ID列表。取值：1-查看账单、2-查看余额、3-资金划拨（若需要开启资金划拨权限，请联系您的商务经理内部开通。）、4-合并出账、5-开票、6-优惠继承、7-代付费、8-成本分析、9-预算管理、10-信用额度设置（若需要开启信用额度设置权限，请联系您的商务经理内部开通。），1、2 默认必须
        :type PermissionIds: list of int non-negative
        :param _NodeId: 成员所属部门的节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :type NodeId: int
        :param _Remark: 备注。
        :type Remark: str
        :param _IsAllowQuit: 是否允许成员退出。允许：Allow，不允许：Denied。
        :type IsAllowQuit: str
        :param _PayUin: 代付者Uin。成员代付费时需要
        :type PayUin: str
        :param _RelationAuthName: 互信实名主体名称。
        :type RelationAuthName: str
        :param _AuthFile: 互信主体证明文件列表。
        :type AuthFile: list of AuthRelationFile
        :param _Tags: 成员标签列表。最大10个
        :type Tags: list of Tag
        """
        self._MemberUin = None
        self._Name = None
        self._PolicyType = None
        self._PermissionIds = None
        self._NodeId = None
        self._Remark = None
        self._IsAllowQuit = None
        self._PayUin = None
        self._RelationAuthName = None
        self._AuthFile = None
        self._Tags = None

    @property
    def MemberUin(self):
        r"""被邀请账号Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Name(self):
        r"""成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PolicyType(self):
        r"""关系策略。取值：Financial
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PermissionIds(self):
        r"""成员财务权限ID列表。取值：1-查看账单、2-查看余额、3-资金划拨（若需要开启资金划拨权限，请联系您的商务经理内部开通。）、4-合并出账、5-开票、6-优惠继承、7-代付费、8-成本分析、9-预算管理、10-信用额度设置（若需要开启信用额度设置权限，请联系您的商务经理内部开通。），1、2 默认必须
        :rtype: list of int non-negative
        """
        return self._PermissionIds

    @PermissionIds.setter
    def PermissionIds(self, PermissionIds):
        self._PermissionIds = PermissionIds

    @property
    def NodeId(self):
        r"""成员所属部门的节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Remark(self):
        r"""备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def IsAllowQuit(self):
        r"""是否允许成员退出。允许：Allow，不允许：Denied。
        :rtype: str
        """
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        r"""代付者Uin。成员代付费时需要
        :rtype: str
        """
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def RelationAuthName(self):
        r"""互信实名主体名称。
        :rtype: str
        """
        return self._RelationAuthName

    @RelationAuthName.setter
    def RelationAuthName(self, RelationAuthName):
        self._RelationAuthName = RelationAuthName

    @property
    def AuthFile(self):
        r"""互信主体证明文件列表。
        :rtype: list of AuthRelationFile
        """
        return self._AuthFile

    @AuthFile.setter
    def AuthFile(self, AuthFile):
        self._AuthFile = AuthFile

    @property
    def Tags(self):
        r"""成员标签列表。最大10个
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Name = params.get("Name")
        self._PolicyType = params.get("PolicyType")
        self._PermissionIds = params.get("PermissionIds")
        self._NodeId = params.get("NodeId")
        self._Remark = params.get("Remark")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        self._RelationAuthName = params.get("RelationAuthName")
        if params.get("AuthFile") is not None:
            self._AuthFile = []
            for item in params.get("AuthFile"):
                obj = AuthRelationFile()
                obj._deserialize(item)
                self._AuthFile.append(obj)
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
        


class InviteOrganizationMemberResponse(AbstractModel):
    r"""InviteOrganizationMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class JoinedGroups(AbstractModel):
    r"""用户加入的用户组

    """

    def __init__(self):
        r"""
        :param _GroupName: 用户组的名称。
        :type GroupName: str
        :param _Description: 用户组的描述。
        :type Description: str
        :param _GroupId: 用户组 ID。
        :type GroupId: str
        :param _GroupType: 用户组的类型。取值：

Manual：手动创建。
Synchronized：外部同步。
        :type GroupType: str
        :param _JoinTime: 加入用户组的时间
        :type JoinTime: str
        """
        self._GroupName = None
        self._Description = None
        self._GroupId = None
        self._GroupType = None
        self._JoinTime = None

    @property
    def GroupName(self):
        r"""用户组的名称。
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Description(self):
        r"""用户组的描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def GroupId(self):
        r"""用户组 ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupType(self):
        r"""用户组的类型。取值：

Manual：手动创建。
Synchronized：外部同步。
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def JoinTime(self):
        r"""加入用户组的时间
        :rtype: str
        """
        return self._JoinTime

    @JoinTime.setter
    def JoinTime(self, JoinTime):
        self._JoinTime = JoinTime


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Description = params.get("Description")
        self._GroupId = params.get("GroupId")
        self._GroupType = params.get("GroupType")
        self._JoinTime = params.get("JoinTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListExternalSAMLIdPCertificatesRequest(AbstractModel):
    r"""ListExternalSAMLIdPCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListExternalSAMLIdPCertificatesResponse(AbstractModel):
    r"""ListExternalSAMLIdPCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _SAMLIdPCertificates: SAML 签名证书列表
        :type SAMLIdPCertificates: list of SAMLIdPCertificate
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCounts = None
        self._SAMLIdPCertificates = None
        self._RequestId = None

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def SAMLIdPCertificates(self):
        r"""SAML 签名证书列表
        :rtype: list of SAMLIdPCertificate
        """
        return self._SAMLIdPCertificates

    @SAMLIdPCertificates.setter
    def SAMLIdPCertificates(self, SAMLIdPCertificates):
        self._SAMLIdPCertificates = SAMLIdPCertificates

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
        self._TotalCounts = params.get("TotalCounts")
        if params.get("SAMLIdPCertificates") is not None:
            self._SAMLIdPCertificates = []
            for item in params.get("SAMLIdPCertificates"):
                obj = SAMLIdPCertificate()
                obj._deserialize(item)
                self._SAMLIdPCertificates.append(obj)
        self._RequestId = params.get("RequestId")


class ListGroupMembersRequest(AbstractModel):
    r"""ListGroupMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _GroupId: 用户组ID。
        :type GroupId: str
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :type NextToken: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        :param _UserType: 用户类型  Manual：手动创建，Synchronized：外部导入。
        :type UserType: str
        """
        self._ZoneId = None
        self._GroupId = None
        self._NextToken = None
        self._MaxResults = None
        self._UserType = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        r"""用户组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def UserType(self):
        r"""用户类型  Manual：手动创建，Synchronized：外部导入。
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        self._UserType = params.get("UserType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupMembersResponse(AbstractModel):
    r"""ListGroupMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _GroupMembers: 用户组的用户列表
        :type GroupMembers: list of GroupMembers
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._TotalCounts = None
        self._MaxResults = None
        self._IsTruncated = None
        self._GroupMembers = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

    @property
    def GroupMembers(self):
        r"""用户组的用户列表
        :rtype: list of GroupMembers
        """
        return self._GroupMembers

    @GroupMembers.setter
    def GroupMembers(self, GroupMembers):
        self._GroupMembers = GroupMembers

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
        self._NextToken = params.get("NextToken")
        self._TotalCounts = params.get("TotalCounts")
        self._MaxResults = params.get("MaxResults")
        self._IsTruncated = params.get("IsTruncated")
        if params.get("GroupMembers") is not None:
            self._GroupMembers = []
            for item in params.get("GroupMembers"):
                obj = GroupMembers()
                obj._deserialize(item)
                self._GroupMembers.append(obj)
        self._RequestId = params.get("RequestId")


class ListGroupsRequest(AbstractModel):
    r"""ListGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :type NextToken: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        :param _Filter: 过滤条件。  格式：<Attribute> <Operator> <Value>，不区分大小写。目前，<Attribute>只支持GroupName，<Operator>只支持eq（Equals）和sw（Start With）。  示例：Filter = "GroupName sw test"，表示查询名称以 test 开头的全部用户组。Filter = "GroupName eq testgroup"，表示查询名称为 testgroup 的用户组。
        :type Filter: str
        :param _GroupType: 用户组的类型  Manual：手动创建，Synchronized：外部导入。
        :type GroupType: str
        :param _FilterUsers: 筛选的用户，该用户关联的用户组会返回IsSelected=1
        :type FilterUsers: list of str
        :param _SortField: 排序的字段，目前只支持CreateTime，默认是CreateTime字段
        :type SortField: str
        :param _SortType: 排序类型：Desc 倒序 Asc  正序，需要您和SortField一起设置
        :type SortType: str
        :param _Offset: 翻页offset. 不要与NextToken同时使用，优先使用NextToken
        :type Offset: int
        """
        self._ZoneId = None
        self._NextToken = None
        self._MaxResults = None
        self._Filter = None
        self._GroupType = None
        self._FilterUsers = None
        self._SortField = None
        self._SortType = None
        self._Offset = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Filter(self):
        r"""过滤条件。  格式：<Attribute> <Operator> <Value>，不区分大小写。目前，<Attribute>只支持GroupName，<Operator>只支持eq（Equals）和sw（Start With）。  示例：Filter = "GroupName sw test"，表示查询名称以 test 开头的全部用户组。Filter = "GroupName eq testgroup"，表示查询名称为 testgroup 的用户组。
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def GroupType(self):
        r"""用户组的类型  Manual：手动创建，Synchronized：外部导入。
        :rtype: str
        """
        return self._GroupType

    @GroupType.setter
    def GroupType(self, GroupType):
        self._GroupType = GroupType

    @property
    def FilterUsers(self):
        r"""筛选的用户，该用户关联的用户组会返回IsSelected=1
        :rtype: list of str
        """
        return self._FilterUsers

    @FilterUsers.setter
    def FilterUsers(self, FilterUsers):
        self._FilterUsers = FilterUsers

    @property
    def SortField(self):
        r"""排序的字段，目前只支持CreateTime，默认是CreateTime字段
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""排序类型：Desc 倒序 Asc  正序，需要您和SortField一起设置
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Offset(self):
        r"""翻页offset. 不要与NextToken同时使用，优先使用NextToken
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        self._Filter = params.get("Filter")
        self._GroupType = params.get("GroupType")
        self._FilterUsers = params.get("FilterUsers")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListGroupsResponse(AbstractModel):
    r"""ListGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _Groups: 用户组列表。
        :type Groups: list of GroupInfo
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._Groups = None
        self._MaxResults = None
        self._TotalCounts = None
        self._IsTruncated = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Groups(self):
        r"""用户组列表。
        :rtype: list of GroupInfo
        """
        return self._Groups

    @Groups.setter
    def Groups(self, Groups):
        self._Groups = Groups

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

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
        self._NextToken = params.get("NextToken")
        if params.get("Groups") is not None:
            self._Groups = []
            for item in params.get("Groups"):
                obj = GroupInfo()
                obj._deserialize(item)
                self._Groups.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._TotalCounts = params.get("TotalCounts")
        self._IsTruncated = params.get("IsTruncated")
        self._RequestId = params.get("RequestId")


class ListJoinedGroupsForUserRequest(AbstractModel):
    r"""ListJoinedGroupsForUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _UserId: 用户ID
        :type UserId: str
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :type NextToken: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        """
        self._ZoneId = None
        self._UserId = None
        self._NextToken = None
        self._MaxResults = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserId(self):
        r"""用户ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserId = params.get("UserId")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListJoinedGroupsForUserResponse(AbstractModel):
    r"""ListJoinedGroupsForUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _JoinedGroups: 用户加入的用户组列表
        :type JoinedGroups: list of JoinedGroups
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._TotalCounts = None
        self._MaxResults = None
        self._IsTruncated = None
        self._JoinedGroups = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

    @property
    def JoinedGroups(self):
        r"""用户加入的用户组列表
        :rtype: list of JoinedGroups
        """
        return self._JoinedGroups

    @JoinedGroups.setter
    def JoinedGroups(self, JoinedGroups):
        self._JoinedGroups = JoinedGroups

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
        self._NextToken = params.get("NextToken")
        self._TotalCounts = params.get("TotalCounts")
        self._MaxResults = params.get("MaxResults")
        self._IsTruncated = params.get("IsTruncated")
        if params.get("JoinedGroups") is not None:
            self._JoinedGroups = []
            for item in params.get("JoinedGroups"):
                obj = JoinedGroups()
                obj._deserialize(item)
                self._JoinedGroups.append(obj)
        self._RequestId = params.get("RequestId")


class ListNonCompliantResourceRequest(AbstractModel):
    r"""ListNonCompliantResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxResults: 限制数目。取值范围：1~50。
        :type MaxResults: int
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param _TagKey: 标签键。
        :type TagKey: str
        """
        self._MaxResults = None
        self._MemberUin = None
        self._PaginationToken = None
        self._TagKey = None

    @property
    def MaxResults(self):
        r"""限制数目。取值范围：1~50。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def PaginationToken(self):
        r"""从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :rtype: str
        """
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def TagKey(self):
        r"""标签键。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._MaxResults = params.get("MaxResults")
        self._MemberUin = params.get("MemberUin")
        self._PaginationToken = params.get("PaginationToken")
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListNonCompliantResourceResponse(AbstractModel):
    r"""ListNonCompliantResource返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 资源及标签合规信息。
        :type Items: list of ResourceTagMapping
        :param _PaginationToken: 获取的下一页的Token值。
        :type PaginationToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._PaginationToken = None
        self._RequestId = None

    @property
    def Items(self):
        r"""资源及标签合规信息。
        :rtype: list of ResourceTagMapping
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def PaginationToken(self):
        r"""获取的下一页的Token值。
        :rtype: str
        """
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = ResourceTagMapping()
                obj._deserialize(item)
                self._Items.append(obj)
        self._PaginationToken = params.get("PaginationToken")
        self._RequestId = params.get("RequestId")


class ListOrgServiceAssignMemberRequest(AbstractModel):
    r"""ListOrgServiceAssignMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50，默认值：10
        :type Limit: int
        :param _ServiceId: 集团服务ID。和集团服务产品标识二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :type ServiceId: int
        :param _Product: 集团服务产品标识。和集团服务ID二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :type Product: str
        """
        self._Offset = None
        self._Limit = None
        self._ServiceId = None
        self._Product = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍，默认值 : 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50，默认值：10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ServiceId(self):
        r"""集团服务ID。和集团服务产品标识二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :rtype: int
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Product(self):
        r"""集团服务产品标识。和集团服务ID二选一必填，可以通过[ListOrganizationService](https://cloud.tencent.com/document/product/850/109561)获取
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ServiceId = params.get("ServiceId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrgServiceAssignMemberResponse(AbstractModel):
    r"""ListOrgServiceAssignMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数。
        :type Total: int
        :param _Items: 委派管理员列表。
        :type Items: list of OrganizationServiceAssignMember
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""委派管理员列表。
        :rtype: list of OrganizationServiceAssignMember
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrganizationServiceAssignMember()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListOrganizationIdentityRequest(AbstractModel):
    r"""ListOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍。默认值 : 0。
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50。默认值：10。
        :type Limit: int
        :param _SearchKey: 名称搜索关键字。
        :type SearchKey: str
        :param _IdentityId: 身份ID。可以通过身份ID搜索
        :type IdentityId: int
        :param _IdentityType: 身份类型。取值范围 1-预设, 2-自定义
        :type IdentityType: int
        """
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._IdentityId = None
        self._IdentityType = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍。默认值 : 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50。默认值：10。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        r"""名称搜索关键字。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def IdentityId(self):
        r"""身份ID。可以通过身份ID搜索
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityType(self):
        r"""身份类型。取值范围 1-预设, 2-自定义
        :rtype: int
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._IdentityId = params.get("IdentityId")
        self._IdentityType = params.get("IdentityType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationIdentityResponse(AbstractModel):
    r"""ListOrganizationIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数。
        :type Total: int
        :param _Items: 条目详情。
        :type Items: list of OrgIdentity
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""条目详情。
        :rtype: list of OrgIdentity
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrgIdentity()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListOrganizationServiceRequest(AbstractModel):
    r"""ListOrganizationService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量。取值是limit的整数倍，默认值 : 0
        :type Offset: int
        :param _Limit: 限制数目。取值范围：1~50，默认值：10
        :type Limit: int
        :param _SearchKey: 名称搜索关键字。
        :type SearchKey: str
        """
        self._Offset = None
        self._Limit = None
        self._SearchKey = None

    @property
    def Offset(self):
        r"""偏移量。取值是limit的整数倍，默认值 : 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""限制数目。取值范围：1~50，默认值：10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        r"""名称搜索关键字。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListOrganizationServiceResponse(AbstractModel):
    r"""ListOrganizationService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数。
        :type Total: int
        :param _Items: 集团服务列表。
        :type Items: list of OrganizationServiceAssign
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Items = None
        self._RequestId = None

    @property
    def Total(self):
        r"""总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Items(self):
        r"""集团服务列表。
        :rtype: list of OrganizationServiceAssign
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

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
        self._Total = params.get("Total")
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = OrganizationServiceAssign()
                obj._deserialize(item)
                self._Items.append(obj)
        self._RequestId = params.get("RequestId")


class ListPermissionPoliciesInRoleConfigurationRequest(AbstractModel):
    r"""ListPermissionPoliciesInRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置 ID
        :type RoleConfigurationId: str
        :param _RolePolicyType: 权限策略类型。取值：  System：系统策略。复用 CAM 的系统策略。 Custom: 自定义策略。按照 CAM 权限策略语法和结构编写的自定义策略。
        :type RolePolicyType: str
        :param _Filter: 按策略名称搜索
        :type Filter: str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._RolePolicyType = None
        self._Filter = None

    @property
    def ZoneId(self):
        r"""空间 ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置 ID
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def RolePolicyType(self):
        r"""权限策略类型。取值：  System：系统策略。复用 CAM 的系统策略。 Custom: 自定义策略。按照 CAM 权限策略语法和结构编写的自定义策略。
        :rtype: str
        """
        return self._RolePolicyType

    @RolePolicyType.setter
    def RolePolicyType(self, RolePolicyType):
        self._RolePolicyType = RolePolicyType

    @property
    def Filter(self):
        r"""按策略名称搜索
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._RolePolicyType = params.get("RolePolicyType")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPermissionPoliciesInRoleConfigurationResponse(AbstractModel):
    r"""ListPermissionPoliciesInRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCounts: 权限策略总个数。
        :type TotalCounts: int
        :param _RolePolicies: 权限策略列表。
        :type RolePolicies: list of RolePolicie
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCounts = None
        self._RolePolicies = None
        self._RequestId = None

    @property
    def TotalCounts(self):
        r"""权限策略总个数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def RolePolicies(self):
        r"""权限策略列表。
        :rtype: list of RolePolicie
        """
        return self._RolePolicies

    @RolePolicies.setter
    def RolePolicies(self, RolePolicies):
        self._RolePolicies = RolePolicies

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
        self._TotalCounts = params.get("TotalCounts")
        if params.get("RolePolicies") is not None:
            self._RolePolicies = []
            for item in params.get("RolePolicies"):
                obj = RolePolicie()
                obj._deserialize(item)
                self._RolePolicies.append(obj)
        self._RequestId = params.get("RequestId")


class ListPoliciesForTarget(AbstractModel):
    r"""查询目标关联的SCP策略列表

    """

    def __init__(self):
        r"""
        :param _StrategyId: 策略Id
        :type StrategyId: int
        :param _StrategyName: 策略名称
        :type StrategyName: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _Uin: 关联的账号或节点
        :type Uin: int
        :param _Type: 关联类型 1-节点 2-用户
        :type Type: int
        :param _AddTime: 策略创建时间
        :type AddTime: str
        :param _UpdateTime: 策略更新时间
        :type UpdateTime: str
        :param _Name: 部门名称
        :type Name: str
        :param _AttachTime: 策略绑定时间
        :type AttachTime: str
        """
        self._StrategyId = None
        self._StrategyName = None
        self._Remark = None
        self._Uin = None
        self._Type = None
        self._AddTime = None
        self._UpdateTime = None
        self._Name = None
        self._AttachTime = None

    @property
    def StrategyId(self):
        r"""策略Id
        :rtype: int
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        r"""策略名称
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def Remark(self):
        r"""备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Uin(self):
        r"""关联的账号或节点
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Type(self):
        r"""关联类型 1-节点 2-用户
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def AddTime(self):
        r"""策略创建时间
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def UpdateTime(self):
        r"""策略更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Name(self):
        r"""部门名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AttachTime(self):
        r"""策略绑定时间
        :rtype: str
        """
        return self._AttachTime

    @AttachTime.setter
    def AttachTime(self, AttachTime):
        self._AttachTime = AttachTime


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._Remark = params.get("Remark")
        self._Uin = params.get("Uin")
        self._Type = params.get("Type")
        self._AddTime = params.get("AddTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Name = params.get("Name")
        self._AttachTime = params.get("AttachTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesForTargetRequest(AbstractModel):
    r"""ListPoliciesForTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetId: 账号uin或者节点id。
        :type TargetId: int
        :param _Rp: 每页数量。默认值是 20，必须大于 0 且小于或等于 200
        :type Rp: int
        :param _Page: 页码。默认值是 1，从 1开始，不能大于 200
        :type Page: int
        :param _PolicyType: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type PolicyType: str
        :param _Keyword: 搜索关键字。按照策略名称搜索
        :type Keyword: str
        """
        self._TargetId = None
        self._Rp = None
        self._Page = None
        self._PolicyType = None
        self._Keyword = None

    @property
    def TargetId(self):
        r"""账号uin或者节点id。
        :rtype: int
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def Rp(self):
        r"""每页数量。默认值是 20，必须大于 0 且小于或等于 200
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        r"""页码。默认值是 1，从 1开始，不能大于 200
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PolicyType(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Keyword(self):
        r"""搜索关键字。按照策略名称搜索
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._PolicyType = params.get("PolicyType")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesForTargetResponse(AbstractModel):
    r"""ListPoliciesForTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 总数。
        :type TotalNum: int
        :param _List: 目标关联的策略列表。
        :type List: list of ListPoliciesForTarget
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        r"""总数。
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        r"""目标关联的策略列表。
        :rtype: list of ListPoliciesForTarget
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListPoliciesForTarget()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListPoliciesRequest(AbstractModel):
    r"""ListPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rp: 每页数量。默认值是 20，必须大于 0 且小于或等于 200
        :type Rp: int
        :param _Page: 页码。默认值是 1，从 1开始，不能大于 200
        :type Page: int
        :param _Scope: 查询范围。取值范围： All-获取所有策略、QCS-只获取预设策略、Local-只获取自定义策略，默认值：All
        :type Scope: str
        :param _Keyword: 搜索关键字。按照策略名搜索
        :type Keyword: str
        :param _PolicyType: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type PolicyType: str
        """
        self._Rp = None
        self._Page = None
        self._Scope = None
        self._Keyword = None
        self._PolicyType = None

    @property
    def Rp(self):
        r"""每页数量。默认值是 20，必须大于 0 且小于或等于 200
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        r"""页码。默认值是 1，从 1开始，不能大于 200
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def Scope(self):
        r"""查询范围。取值范围： All-获取所有策略、QCS-只获取预设策略、Local-只获取自定义策略，默认值：All
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Keyword(self):
        r"""搜索关键字。按照策略名搜索
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def PolicyType(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType


    def _deserialize(self, params):
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._Scope = params.get("Scope")
        self._Keyword = params.get("Keyword")
        self._PolicyType = params.get("PolicyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListPoliciesResponse(AbstractModel):
    r"""ListPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 策略总数
        :type TotalNum: int
        :param _List: 策略列表数据
        :type List: list of ListPolicyNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        r"""策略总数
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        r"""策略列表数据
        :rtype: list of ListPolicyNode
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListPolicyNode()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListPolicyNode(AbstractModel):
    r"""企业组织策略列表

    """

    def __init__(self):
        r"""
        :param _AddTime: 策略创建时间
        :type AddTime: str
        :param _AttachedTimes: 策略绑定次数
        :type AttachedTimes: int
        :param _Description: 策略描述信息
        :type Description: str
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _PolicyId: 策略Id
        :type PolicyId: int
        :param _UpdateTime: 策略更新时间
        :type UpdateTime: str
        :param _Type: 策略类型 1-自定义 2-预设
        :type Type: int
        """
        self._AddTime = None
        self._AttachedTimes = None
        self._Description = None
        self._PolicyName = None
        self._PolicyId = None
        self._UpdateTime = None
        self._Type = None

    @property
    def AddTime(self):
        r"""策略创建时间
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime

    @property
    def AttachedTimes(self):
        r"""策略绑定次数
        :rtype: int
        """
        return self._AttachedTimes

    @AttachedTimes.setter
    def AttachedTimes(self, AttachedTimes):
        self._AttachedTimes = AttachedTimes

    @property
    def Description(self):
        r"""策略描述信息
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PolicyName(self):
        r"""策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyId(self):
        r"""策略Id
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def UpdateTime(self):
        r"""策略更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Type(self):
        r"""策略类型 1-自定义 2-预设
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._AddTime = params.get("AddTime")
        self._AttachedTimes = params.get("AttachedTimes")
        self._Description = params.get("Description")
        self._PolicyName = params.get("PolicyName")
        self._PolicyId = params.get("PolicyId")
        self._UpdateTime = params.get("UpdateTime")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRoleAssignmentsRequest(AbstractModel):
    r"""ListRoleAssignments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :type NextToken: str
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _TargetUin: 同步的集团账号目标账号的UIN。
        :type TargetUin: int
        :param _PrincipalType: CAM 用户同步的身份类型。取值： User：表示同步的身份是用户。 Group：表示同步的身份是用户组。
        :type PrincipalType: str
        :param _PrincipalId: 用户同步 ID。取值： 当PrincipalType取值为Group时，该值为用户组 ID（g-****)，当PrincipalType取值为User时，该值为用户 ID （u-****）。
        :type PrincipalId: str
        :param _Filter: 查询条件，目前只支持权限配置名称查询。
        :type Filter: str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._MaxResults = None
        self._NextToken = None
        self._TargetType = None
        self._TargetUin = None
        self._PrincipalType = None
        self._PrincipalId = None
        self._Filter = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetUin(self):
        r"""同步的集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值： User：表示同步的身份是用户。 Group：表示同步的身份是用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def PrincipalId(self):
        r"""用户同步 ID。取值： 当PrincipalType取值为Group时，该值为用户组 ID（g-****)，当PrincipalType取值为User时，该值为用户 ID （u-****）。
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def Filter(self):
        r"""查询条件，目前只支持权限配置名称查询。
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TargetType = params.get("TargetType")
        self._TargetUin = params.get("TargetUin")
        self._PrincipalType = params.get("PrincipalType")
        self._PrincipalId = params.get("PrincipalId")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRoleAssignmentsResponse(AbstractModel):
    r"""ListRoleAssignments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _RoleAssignments: 集团账号目标账号的授权列表。
        :type RoleAssignments: list of RoleAssignments
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._TotalCounts = None
        self._MaxResults = None
        self._IsTruncated = None
        self._RoleAssignments = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

    @property
    def RoleAssignments(self):
        r"""集团账号目标账号的授权列表。
        :rtype: list of RoleAssignments
        """
        return self._RoleAssignments

    @RoleAssignments.setter
    def RoleAssignments(self, RoleAssignments):
        self._RoleAssignments = RoleAssignments

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
        self._NextToken = params.get("NextToken")
        self._TotalCounts = params.get("TotalCounts")
        self._MaxResults = params.get("MaxResults")
        self._IsTruncated = params.get("IsTruncated")
        if params.get("RoleAssignments") is not None:
            self._RoleAssignments = []
            for item in params.get("RoleAssignments"):
                obj = RoleAssignments()
                obj._deserialize(item)
                self._RoleAssignments.append(obj)
        self._RequestId = params.get("RequestId")


class ListRoleConfigurationProvisioningsRequest(AbstractModel):
    r"""ListRoleConfigurationProvisionings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :type NextToken: str
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _TargetUin: 同步的集团账号目标账号的UIN。
        :type TargetUin: int
        :param _DeploymentStatus: Deployed: 部署成功 DeployedRequired：需要重新部署 DeployFailed：部署失败
        :type DeploymentStatus: str
        :param _Filter: 支持配置名称搜索。
        :type Filter: str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._MaxResults = None
        self._NextToken = None
        self._TargetType = None
        self._TargetUin = None
        self._DeploymentStatus = None
        self._Filter = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetUin(self):
        r"""同步的集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def DeploymentStatus(self):
        r"""Deployed: 部署成功 DeployedRequired：需要重新部署 DeployFailed：部署失败
        :rtype: str
        """
        return self._DeploymentStatus

    @DeploymentStatus.setter
    def DeploymentStatus(self, DeploymentStatus):
        self._DeploymentStatus = DeploymentStatus

    @property
    def Filter(self):
        r"""支持配置名称搜索。
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TargetType = params.get("TargetType")
        self._TargetUin = params.get("TargetUin")
        self._DeploymentStatus = params.get("DeploymentStatus")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRoleConfigurationProvisioningsResponse(AbstractModel):
    r"""ListRoleConfigurationProvisionings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _RoleConfigurationProvisionings: 部成员账号列表。
        :type RoleConfigurationProvisionings: list of RoleConfigurationProvisionings
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._TotalCounts = None
        self._MaxResults = None
        self._IsTruncated = None
        self._RoleConfigurationProvisionings = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

    @property
    def RoleConfigurationProvisionings(self):
        r"""部成员账号列表。
        :rtype: list of RoleConfigurationProvisionings
        """
        return self._RoleConfigurationProvisionings

    @RoleConfigurationProvisionings.setter
    def RoleConfigurationProvisionings(self, RoleConfigurationProvisionings):
        self._RoleConfigurationProvisionings = RoleConfigurationProvisionings

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
        self._NextToken = params.get("NextToken")
        self._TotalCounts = params.get("TotalCounts")
        self._MaxResults = params.get("MaxResults")
        self._IsTruncated = params.get("IsTruncated")
        if params.get("RoleConfigurationProvisionings") is not None:
            self._RoleConfigurationProvisionings = []
            for item in params.get("RoleConfigurationProvisionings"):
                obj = RoleConfigurationProvisionings()
                obj._deserialize(item)
                self._RoleConfigurationProvisionings.append(obj)
        self._RequestId = params.get("RequestId")


class ListRoleConfigurationsRequest(AbstractModel):
    r"""ListRoleConfigurations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :type NextToken: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        :param _Filter: 过滤文本。不区分大小写。目前，支持 RoleConfigurationName和Description. 示例：Filter = "test"，表示查询名称或描述里包含 test 的权限配置。
        :type Filter: str
        :param _FilterTargets: 检索成员账号是否配置过权限，如果配置过返回IsSelected: true, 否则返回false。
        :type FilterTargets: list of int
        :param _PrincipalId: 授权的用户UserId或者用户组的GroupId，必须和入参数FilterTargets一起设置
        :type PrincipalId: str
        """
        self._ZoneId = None
        self._NextToken = None
        self._MaxResults = None
        self._Filter = None
        self._FilterTargets = None
        self._PrincipalId = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Filter(self):
        r"""过滤文本。不区分大小写。目前，支持 RoleConfigurationName和Description. 示例：Filter = "test"，表示查询名称或描述里包含 test 的权限配置。
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def FilterTargets(self):
        r"""检索成员账号是否配置过权限，如果配置过返回IsSelected: true, 否则返回false。
        :rtype: list of int
        """
        return self._FilterTargets

    @FilterTargets.setter
    def FilterTargets(self, FilterTargets):
        self._FilterTargets = FilterTargets

    @property
    def PrincipalId(self):
        r"""授权的用户UserId或者用户组的GroupId，必须和入参数FilterTargets一起设置
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        self._Filter = params.get("Filter")
        self._FilterTargets = params.get("FilterTargets")
        self._PrincipalId = params.get("PrincipalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListRoleConfigurationsResponse(AbstractModel):
    r"""ListRoleConfigurations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _NextToken: 查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _RoleConfigurations: 权限配置列表。
        :type RoleConfigurations: list of RoleConfiguration
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCounts = None
        self._MaxResults = None
        self._IsTruncated = None
        self._NextToken = None
        self._RoleConfigurations = None
        self._RequestId = None

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RoleConfigurations(self):
        r"""权限配置列表。
        :rtype: list of RoleConfiguration
        """
        return self._RoleConfigurations

    @RoleConfigurations.setter
    def RoleConfigurations(self, RoleConfigurations):
        self._RoleConfigurations = RoleConfigurations

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
        self._TotalCounts = params.get("TotalCounts")
        self._MaxResults = params.get("MaxResults")
        self._IsTruncated = params.get("IsTruncated")
        self._NextToken = params.get("NextToken")
        if params.get("RoleConfigurations") is not None:
            self._RoleConfigurations = []
            for item in params.get("RoleConfigurations"):
                obj = RoleConfiguration()
                obj._deserialize(item)
                self._RoleConfigurations.append(obj)
        self._RequestId = params.get("RequestId")


class ListSCIMCredentialsRequest(AbstractModel):
    r"""ListSCIMCredentials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _CredentialId: SCIM密钥ID
        :type CredentialId: str
        """
        self._ZoneId = None
        self._CredentialId = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CredentialId(self):
        r"""SCIM密钥ID
        :rtype: str
        """
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._CredentialId = params.get("CredentialId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListSCIMCredentialsResponse(AbstractModel):
    r"""ListSCIMCredentials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCounts: SCIM密钥数量。
        :type TotalCounts: int
        :param _SCIMCredentials: SCIM 密钥信息。
        :type SCIMCredentials: list of SCIMCredential
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCounts = None
        self._SCIMCredentials = None
        self._RequestId = None

    @property
    def TotalCounts(self):
        r"""SCIM密钥数量。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def SCIMCredentials(self):
        r"""SCIM 密钥信息。
        :rtype: list of SCIMCredential
        """
        return self._SCIMCredentials

    @SCIMCredentials.setter
    def SCIMCredentials(self, SCIMCredentials):
        self._SCIMCredentials = SCIMCredentials

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
        self._TotalCounts = params.get("TotalCounts")
        if params.get("SCIMCredentials") is not None:
            self._SCIMCredentials = []
            for item in params.get("SCIMCredentials"):
                obj = SCIMCredential()
                obj._deserialize(item)
                self._SCIMCredentials.append(obj)
        self._RequestId = params.get("RequestId")


class ListTargetsForPolicyNode(AbstractModel):
    r"""查询某个指定SCP策略关联的目标列表

    """

    def __init__(self):
        r"""
        :param _Uin: scp账号uin或节点Id
        :type Uin: int
        :param _RelatedType: 关联类型 1-节点关联 2-用户关联
        :type RelatedType: int
        :param _Name: 账号或者节点名称
        :type Name: str
        :param _AddTime: 绑定时间
        :type AddTime: str
        """
        self._Uin = None
        self._RelatedType = None
        self._Name = None
        self._AddTime = None

    @property
    def Uin(self):
        r"""scp账号uin或节点Id
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RelatedType(self):
        r"""关联类型 1-节点关联 2-用户关联
        :rtype: int
        """
        return self._RelatedType

    @RelatedType.setter
    def RelatedType(self, RelatedType):
        self._RelatedType = RelatedType

    @property
    def Name(self):
        r"""账号或者节点名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AddTime(self):
        r"""绑定时间
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._RelatedType = params.get("RelatedType")
        self._Name = params.get("Name")
        self._AddTime = params.get("AddTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTargetsForPolicyRequest(AbstractModel):
    r"""ListTargetsForPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略Id。
        :type PolicyId: int
        :param _Rp: 每页数量。默认值是 20，必须大于 0 且小于或等于 200
        :type Rp: int
        :param _Page: 页码。默认值是 1，从 1开始，不能大于 200
        :type Page: int
        :param _TargetType: 策略类型。取值范围：All-全部、User-用户、Node-节点
        :type TargetType: str
        :param _PolicyType: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type PolicyType: str
        :param _Keyword: 按照多个策略id搜索，空格隔开。
        :type Keyword: str
        """
        self._PolicyId = None
        self._Rp = None
        self._Page = None
        self._TargetType = None
        self._PolicyType = None
        self._Keyword = None

    @property
    def PolicyId(self):
        r"""策略Id。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Rp(self):
        r"""每页数量。默认值是 20，必须大于 0 且小于或等于 200
        :rtype: int
        """
        return self._Rp

    @Rp.setter
    def Rp(self, Rp):
        self._Rp = Rp

    @property
    def Page(self):
        r"""页码。默认值是 1，从 1开始，不能大于 200
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def TargetType(self):
        r"""策略类型。取值范围：All-全部、User-用户、Node-节点
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def PolicyType(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def Keyword(self):
        r"""按照多个策略id搜索，空格隔开。
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._Rp = params.get("Rp")
        self._Page = params.get("Page")
        self._TargetType = params.get("TargetType")
        self._PolicyType = params.get("PolicyType")
        self._Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTargetsForPolicyResponse(AbstractModel):
    r"""ListTargetsForPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalNum: 总数。
        :type TotalNum: int
        :param _List: 指定SCP策略关联目标列表。
        :type List: list of ListTargetsForPolicyNode
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalNum = None
        self._List = None
        self._RequestId = None

    @property
    def TotalNum(self):
        r"""总数。
        :rtype: int
        """
        return self._TotalNum

    @TotalNum.setter
    def TotalNum(self, TotalNum):
        self._TotalNum = TotalNum

    @property
    def List(self):
        r"""指定SCP策略关联目标列表。
        :rtype: list of ListTargetsForPolicyNode
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalNum = params.get("TotalNum")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = ListTargetsForPolicyNode()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListTasksRequest(AbstractModel):
    r"""ListTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _PrincipalId: 用户同步 ID。取值： 当PrincipalType取值为Group时，该值为用户组 ID（g-****）， 当PrincipalType取值为User时，该值为用户 ID（u-****）。
        :type PrincipalId: str
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :type NextToken: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        :param _PrincipalType: CAM 用户同步的身份类型。取值： User：表示同步的身份是用户。 Group：表示同步的身份是用户组。
        :type PrincipalType: str
        :param _TargetUin: 同步的集团账号目标账号的UIN。
        :type TargetUin: int
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _Status: InProgress：任务执行中。 Success：任务执行成功。 Failed：任务执行失败。
        :type Status: str
        :param _TaskType: 任务类型。
        :type TaskType: str
        """
        self._ZoneId = None
        self._PrincipalId = None
        self._NextToken = None
        self._MaxResults = None
        self._PrincipalType = None
        self._TargetUin = None
        self._TargetType = None
        self._RoleConfigurationId = None
        self._Status = None
        self._TaskType = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PrincipalId(self):
        r"""用户同步 ID。取值： 当PrincipalType取值为Group时，该值为用户组 ID（g-****）， 当PrincipalType取值为User时，该值为用户 ID（u-****）。
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值： User：表示同步的身份是用户。 Group：表示同步的身份是用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def TargetUin(self):
        r"""同步的集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def Status(self):
        r"""InProgress：任务执行中。 Success：任务执行成功。 Failed：任务执行失败。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskType(self):
        r"""任务类型。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._PrincipalId = params.get("PrincipalId")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        self._PrincipalType = params.get("PrincipalType")
        self._TargetUin = params.get("TargetUin")
        self._TargetType = params.get("TargetType")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._Status = params.get("Status")
        self._TaskType = params.get("TaskType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTasksResponse(AbstractModel):
    r"""ListTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _Tasks: 任务详情
        :type Tasks: list of TaskInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._TotalCounts = None
        self._MaxResults = None
        self._IsTruncated = None
        self._Tasks = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

    @property
    def Tasks(self):
        r"""任务详情
        :rtype: list of TaskInfo
        """
        return self._Tasks

    @Tasks.setter
    def Tasks(self, Tasks):
        self._Tasks = Tasks

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
        self._NextToken = params.get("NextToken")
        self._TotalCounts = params.get("TotalCounts")
        self._MaxResults = params.get("MaxResults")
        self._IsTruncated = params.get("IsTruncated")
        if params.get("Tasks") is not None:
            self._Tasks = []
            for item in params.get("Tasks"):
                obj = TaskInfo()
                obj._deserialize(item)
                self._Tasks.append(obj)
        self._RequestId = params.get("RequestId")


class ListUserSyncProvisioningsRequest(AbstractModel):
    r"""ListUserSyncProvisionings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _PrincipalId: 用户同步 ID。取值：  当PrincipalType取值为Group时，该值为用户组 ID（g-********）。 当PrincipalType取值为User时，该值为用户 ID（u-********）。
        :type PrincipalId: str
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :type NextToken: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        :param _PrincipalType: CAM 用户同步的身份类型。取值： User：表示同步的身份是用户。 Group：表示同步的身份是用户组。
        :type PrincipalType: str
        :param _TargetUin: 集团账号目标账号的UIN。
        :type TargetUin: int
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _Filter: 检测条件。
        :type Filter: str
        """
        self._ZoneId = None
        self._PrincipalId = None
        self._NextToken = None
        self._MaxResults = None
        self._PrincipalType = None
        self._TargetUin = None
        self._TargetType = None
        self._Filter = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def PrincipalId(self):
        r"""用户同步 ID。取值：  当PrincipalType取值为Group时，该值为用户组 ID（g-********）。 当PrincipalType取值为User时，该值为用户 ID（u-********）。
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法多次查询，直到IsTruncated为false，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值： User：表示同步的身份是用户。 Group：表示同步的身份是用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def TargetUin(self):
        r"""集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Filter(self):
        r"""检测条件。
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._PrincipalId = params.get("PrincipalId")
        self._NextToken = params.get("NextToken")
        self._MaxResults = params.get("MaxResults")
        self._PrincipalType = params.get("PrincipalType")
        self._TargetUin = params.get("TargetUin")
        self._TargetType = params.get("TargetType")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUserSyncProvisioningsResponse(AbstractModel):
    r"""ListUserSyncProvisionings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _UserProvisionings: CAM同步的用户列表。
        :type UserProvisionings: list of UserProvisioning
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._TotalCounts = None
        self._MaxResults = None
        self._IsTruncated = None
        self._UserProvisionings = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。  说明 只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

    @property
    def UserProvisionings(self):
        r"""CAM同步的用户列表。
        :rtype: list of UserProvisioning
        """
        return self._UserProvisionings

    @UserProvisionings.setter
    def UserProvisionings(self, UserProvisionings):
        self._UserProvisionings = UserProvisionings

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
        self._NextToken = params.get("NextToken")
        self._TotalCounts = params.get("TotalCounts")
        self._MaxResults = params.get("MaxResults")
        self._IsTruncated = params.get("IsTruncated")
        if params.get("UserProvisionings") is not None:
            self._UserProvisionings = []
            for item in params.get("UserProvisionings"):
                obj = UserProvisioning()
                obj._deserialize(item)
                self._UserProvisionings.append(obj)
        self._RequestId = params.get("RequestId")


class ListUsersRequest(AbstractModel):
    r"""ListUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _UserStatus: 用户状态 Enabled：启用， Disabled：禁用。
        :type UserStatus: str
        :param _UserType: 用户类型  Manual：手动创建，Synchronized：外部导入。
        :type UserType: str
        :param _Filter: 过滤条件。  目前仅支持用户名，邮箱，用户userId，描述
        :type Filter: str
        :param _MaxResults: 每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :type MaxResults: int
        :param _NextToken: 查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法经过多次查询，直到IsTruncated为false时，表示全部数据查询完毕。
        :type NextToken: str
        :param _FilterGroups: 筛选的用户组，该用户组关联的子用户会返回IsSelected=1
        :type FilterGroups: list of str
        :param _SortField: 排序的字段，目前只支持CreateTime，默认是CreateTime字段
        :type SortField: str
        :param _SortType: 排序类型：Desc 倒序 Asc  正序，需要您和SortField一起设置
        :type SortType: str
        :param _Offset: 翻页offset. 不要与NextToken同时使用，优先使用NextToken
        :type Offset: int
        """
        self._ZoneId = None
        self._UserStatus = None
        self._UserType = None
        self._Filter = None
        self._MaxResults = None
        self._NextToken = None
        self._FilterGroups = None
        self._SortField = None
        self._SortType = None
        self._Offset = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserStatus(self):
        r"""用户状态 Enabled：启用， Disabled：禁用。
        :rtype: str
        """
        return self._UserStatus

    @UserStatus.setter
    def UserStatus(self, UserStatus):
        self._UserStatus = UserStatus

    @property
    def UserType(self):
        r"""用户类型  Manual：手动创建，Synchronized：外部导入。
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def Filter(self):
        r"""过滤条件。  目前仅支持用户名，邮箱，用户userId，描述
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。  取值范围：1~100。  默认值：10。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。首次调用 API 不需要NextToken。  当您首次调用 API 时，如果返回数据总条数超过MaxResults限制，数据会被截断，只返回MaxResults条数据，同时，返回参数IsTruncated为true，返回一个NextToken。您可以使用上一次返回的NextToken继续调用 API，其他请求参数保持不变，查询被截断的数据。您可以按此方法经过多次查询，直到IsTruncated为false时，表示全部数据查询完毕。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def FilterGroups(self):
        r"""筛选的用户组，该用户组关联的子用户会返回IsSelected=1
        :rtype: list of str
        """
        return self._FilterGroups

    @FilterGroups.setter
    def FilterGroups(self, FilterGroups):
        self._FilterGroups = FilterGroups

    @property
    def SortField(self):
        r"""排序的字段，目前只支持CreateTime，默认是CreateTime字段
        :rtype: str
        """
        return self._SortField

    @SortField.setter
    def SortField(self, SortField):
        self._SortField = SortField

    @property
    def SortType(self):
        r"""排序类型：Desc 倒序 Asc  正序，需要您和SortField一起设置
        :rtype: str
        """
        return self._SortType

    @SortType.setter
    def SortType(self, SortType):
        self._SortType = SortType

    @property
    def Offset(self):
        r"""翻页offset. 不要与NextToken同时使用，优先使用NextToken
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserStatus = params.get("UserStatus")
        self._UserType = params.get("UserType")
        self._Filter = params.get("Filter")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._FilterGroups = params.get("FilterGroups")
        self._SortField = params.get("SortField")
        self._SortType = params.get("SortType")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListUsersResponse(AbstractModel):
    r"""ListUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCounts: 符合请求参数条件的数据总条数。
        :type TotalCounts: int
        :param _MaxResults: 每页的最大数据条数。
        :type MaxResults: int
        :param _Users: 用户列表。
        :type Users: list of UserInfo
        :param _NextToken: 查询返回结果下一页的令牌。只有IsTruncated为true时，才显示该参数。
        :type NextToken: str
        :param _IsTruncated: 返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :type IsTruncated: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCounts = None
        self._MaxResults = None
        self._Users = None
        self._NextToken = None
        self._IsTruncated = None
        self._RequestId = None

    @property
    def TotalCounts(self):
        r"""符合请求参数条件的数据总条数。
        :rtype: int
        """
        return self._TotalCounts

    @TotalCounts.setter
    def TotalCounts(self, TotalCounts):
        self._TotalCounts = TotalCounts

    @property
    def MaxResults(self):
        r"""每页的最大数据条数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Users(self):
        r"""用户列表。
        :rtype: list of UserInfo
        """
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users

    @property
    def NextToken(self):
        r"""查询返回结果下一页的令牌。只有IsTruncated为true时，才显示该参数。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def IsTruncated(self):
        r"""返回结果是否被截断。取值：  true：已截断。 false：未截断。
        :rtype: bool
        """
        return self._IsTruncated

    @IsTruncated.setter
    def IsTruncated(self, IsTruncated):
        self._IsTruncated = IsTruncated

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
        self._TotalCounts = params.get("TotalCounts")
        self._MaxResults = params.get("MaxResults")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfo()
                obj._deserialize(item)
                self._Users.append(obj)
        self._NextToken = params.get("NextToken")
        self._IsTruncated = params.get("IsTruncated")
        self._RequestId = params.get("RequestId")


class ManagerShareUnit(AbstractModel):
    r"""我的共享单元列表详情

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _Name: 共享单元名称。
        :type Name: str
        :param _Uin: 共享单元管理员Uin。
        :type Uin: int
        :param _OwnerUin: 共享单元管理员OwnerUin。
        :type OwnerUin: int
        :param _Area: 共享单元地域。
        :type Area: str
        :param _Description: 描述。
        :type Description: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _ShareResourceNum: 共享单元资源数。
        :type ShareResourceNum: int
        :param _ShareMemberNum: 共享单元成员数。
        :type ShareMemberNum: int
        :param _ShareScope: 共享范围。取值：1-仅允许集团组织内共享 2-允许共享给任意账号
        :type ShareScope: int
        """
        self._UnitId = None
        self._Name = None
        self._Uin = None
        self._OwnerUin = None
        self._Area = None
        self._Description = None
        self._CreateTime = None
        self._ShareResourceNum = None
        self._ShareMemberNum = None
        self._ShareScope = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def Name(self):
        r"""共享单元名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Uin(self):
        r"""共享单元管理员Uin。
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def OwnerUin(self):
        r"""共享单元管理员OwnerUin。
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Area(self):
        r"""共享单元地域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Description(self):
        r"""描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ShareResourceNum(self):
        r"""共享单元资源数。
        :rtype: int
        """
        return self._ShareResourceNum

    @ShareResourceNum.setter
    def ShareResourceNum(self, ShareResourceNum):
        self._ShareResourceNum = ShareResourceNum

    @property
    def ShareMemberNum(self):
        r"""共享单元成员数。
        :rtype: int
        """
        return self._ShareMemberNum

    @ShareMemberNum.setter
    def ShareMemberNum(self, ShareMemberNum):
        self._ShareMemberNum = ShareMemberNum

    @property
    def ShareScope(self):
        r"""共享范围。取值：1-仅允许集团组织内共享 2-允许共享给任意账号
        :rtype: int
        """
        return self._ShareScope

    @ShareScope.setter
    def ShareScope(self, ShareScope):
        self._ShareScope = ShareScope


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        self._Name = params.get("Name")
        self._Uin = params.get("Uin")
        self._OwnerUin = params.get("OwnerUin")
        self._Area = params.get("Area")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._ShareResourceNum = params.get("ShareResourceNum")
        self._ShareMemberNum = params.get("ShareMemberNum")
        self._ShareScope = params.get("ShareScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MemberIdentity(AbstractModel):
    r"""成员管理身份

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID。
        :type IdentityId: int
        :param _IdentityAliasName: 身份名称。
        :type IdentityAliasName: str
        """
        self._IdentityId = None
        self._IdentityAliasName = None

    @property
    def IdentityId(self):
        r"""身份ID。
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityAliasName(self):
        r"""身份名称。
        :rtype: str
        """
        return self._IdentityAliasName

    @IdentityAliasName.setter
    def IdentityAliasName(self, IdentityAliasName):
        self._IdentityAliasName = IdentityAliasName


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityAliasName = params.get("IdentityAliasName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MemberMainInfo(AbstractModel):
    r"""成员主要信息

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员uin
        :type MemberUin: int
        :param _MemberName: 成员名称
        :type MemberName: str
        """
        self._MemberUin = None
        self._MemberName = None

    @property
    def MemberUin(self):
        r"""成员uin
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        r"""成员名称
        :rtype: str
        """
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersRequest(AbstractModel):
    r"""MoveOrganizationNodeMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 组织节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :type NodeId: int
        :param _MemberUin: 成员Uin列表。
        :type MemberUin: list of int
        """
        self._NodeId = None
        self._MemberUin = None

    @property
    def NodeId(self):
        r"""组织节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def MemberUin(self):
        r"""成员Uin列表。
        :rtype: list of int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._MemberUin = params.get("MemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MoveOrganizationNodeMembersResponse(AbstractModel):
    r"""MoveOrganizationNodeMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class NodeMainInfo(AbstractModel):
    r"""部门主要信息

    """

    def __init__(self):
        r"""
        :param _NodeId: 部门ID
        :type NodeId: int
        :param _NodeName: 部门名称
        :type NodeName: str
        """
        self._NodeId = None
        self._NodeName = None

    @property
    def NodeId(self):
        r"""部门ID
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        r"""部门名称
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotAllowReason(AbstractModel):
    r"""不允许删除的原因。

    """

    def __init__(self):
        r"""
        :param _IsCreateMember: 是否创建的成员。true-是、false-否；成员不是创建的成员不允许删除
        :type IsCreateMember: bool
        :param _DeletionPermission: 成员删除许可。true-开启、false-关闭；成员删除许可关闭时不允许删除
        :type DeletionPermission: bool
        :param _IsAssignManager: 是否可信服务委派管理员。true-是、false-否；成员是可信服务委派管理员不允许删除
        :type IsAssignManager: bool
        :param _IsAuthManager: 是否主体管理员。true-是、false-否；成员是主体管理员不允许删除
        :type IsAuthManager: bool
        :param _IsShareManager: 是否共享资源管理员。true-是、false-否；成员是共享资源管理员不允许删除
        :type IsShareManager: bool
        :param _OperateProcess: 成员是否设置了操作审批。true-是、false-否；成员设置了操作审批时不允许删除
        :type OperateProcess: bool
        :param _BillingPermission: 是否允许解除成员财务权限。true-是、false-否；成员不能解除财务权限时不允许删除
        :type BillingPermission: bool
        :param _ExistResources: 存在的资源列表。账号存在资源时不允许删除
        :type ExistResources: list of str
        :param _DetectFailedResources: 检测失败的资源列表。账号有资源检测失败时不允许删除。
        :type DetectFailedResources: list of str
        """
        self._IsCreateMember = None
        self._DeletionPermission = None
        self._IsAssignManager = None
        self._IsAuthManager = None
        self._IsShareManager = None
        self._OperateProcess = None
        self._BillingPermission = None
        self._ExistResources = None
        self._DetectFailedResources = None

    @property
    def IsCreateMember(self):
        r"""是否创建的成员。true-是、false-否；成员不是创建的成员不允许删除
        :rtype: bool
        """
        return self._IsCreateMember

    @IsCreateMember.setter
    def IsCreateMember(self, IsCreateMember):
        self._IsCreateMember = IsCreateMember

    @property
    def DeletionPermission(self):
        r"""成员删除许可。true-开启、false-关闭；成员删除许可关闭时不允许删除
        :rtype: bool
        """
        return self._DeletionPermission

    @DeletionPermission.setter
    def DeletionPermission(self, DeletionPermission):
        self._DeletionPermission = DeletionPermission

    @property
    def IsAssignManager(self):
        r"""是否可信服务委派管理员。true-是、false-否；成员是可信服务委派管理员不允许删除
        :rtype: bool
        """
        return self._IsAssignManager

    @IsAssignManager.setter
    def IsAssignManager(self, IsAssignManager):
        self._IsAssignManager = IsAssignManager

    @property
    def IsAuthManager(self):
        r"""是否主体管理员。true-是、false-否；成员是主体管理员不允许删除
        :rtype: bool
        """
        return self._IsAuthManager

    @IsAuthManager.setter
    def IsAuthManager(self, IsAuthManager):
        self._IsAuthManager = IsAuthManager

    @property
    def IsShareManager(self):
        r"""是否共享资源管理员。true-是、false-否；成员是共享资源管理员不允许删除
        :rtype: bool
        """
        return self._IsShareManager

    @IsShareManager.setter
    def IsShareManager(self, IsShareManager):
        self._IsShareManager = IsShareManager

    @property
    def OperateProcess(self):
        r"""成员是否设置了操作审批。true-是、false-否；成员设置了操作审批时不允许删除
        :rtype: bool
        """
        return self._OperateProcess

    @OperateProcess.setter
    def OperateProcess(self, OperateProcess):
        self._OperateProcess = OperateProcess

    @property
    def BillingPermission(self):
        r"""是否允许解除成员财务权限。true-是、false-否；成员不能解除财务权限时不允许删除
        :rtype: bool
        """
        return self._BillingPermission

    @BillingPermission.setter
    def BillingPermission(self, BillingPermission):
        self._BillingPermission = BillingPermission

    @property
    def ExistResources(self):
        r"""存在的资源列表。账号存在资源时不允许删除
        :rtype: list of str
        """
        return self._ExistResources

    @ExistResources.setter
    def ExistResources(self, ExistResources):
        self._ExistResources = ExistResources

    @property
    def DetectFailedResources(self):
        r"""检测失败的资源列表。账号有资源检测失败时不允许删除。
        :rtype: list of str
        """
        return self._DetectFailedResources

    @DetectFailedResources.setter
    def DetectFailedResources(self, DetectFailedResources):
        self._DetectFailedResources = DetectFailedResources


    def _deserialize(self, params):
        self._IsCreateMember = params.get("IsCreateMember")
        self._DeletionPermission = params.get("DeletionPermission")
        self._IsAssignManager = params.get("IsAssignManager")
        self._IsAuthManager = params.get("IsAuthManager")
        self._IsShareManager = params.get("IsShareManager")
        self._OperateProcess = params.get("OperateProcess")
        self._BillingPermission = params.get("BillingPermission")
        self._ExistResources = params.get("ExistResources")
        self._DetectFailedResources = params.get("DetectFailedResources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenIdentityCenterRequest(AbstractModel):
    r"""OpenIdentityCenter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneName: 空间名，必须全局唯一。包含小写字母、数字和短划线（-）。不能以短划线（-）开头或结尾，且不能有两个连续的短划线（-）。长度：2~64 个字符。
        :type ZoneName: str
        """
        self._ZoneName = None

    @property
    def ZoneName(self):
        r"""空间名，必须全局唯一。包含小写字母、数字和短划线（-）。不能以短划线（-）开头或结尾，且不能有两个连续的短划线（-）。长度：2~64 个字符。
        :rtype: str
        """
        return self._ZoneName

    @ZoneName.setter
    def ZoneName(self, ZoneName):
        self._ZoneName = ZoneName


    def _deserialize(self, params):
        self._ZoneName = params.get("ZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenIdentityCenterResponse(AbstractModel):
    r"""OpenIdentityCenter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._RequestId = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

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
        self._ZoneId = params.get("ZoneId")
        self._RequestId = params.get("RequestId")


class OrgFinancialByMonth(AbstractModel):
    r"""按月获取组织财务信息

    """

    def __init__(self):
        r"""
        :param _Id: 记录ID。
        :type Id: int
        :param _Month: 月份，格式：yyyy-mm，示例：2021-01。
        :type Month: str
        :param _TotalCost: 消耗金额，单元：元。
        :type TotalCost: float
        :param _GrowthRate: 比上月增长率%。正数增长，负数下降，空值无法统计。
        :type GrowthRate: str
        """
        self._Id = None
        self._Month = None
        self._TotalCost = None
        self._GrowthRate = None

    @property
    def Id(self):
        r"""记录ID。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Month(self):
        r"""月份，格式：yyyy-mm，示例：2021-01。
        :rtype: str
        """
        return self._Month

    @Month.setter
    def Month(self, Month):
        self._Month = Month

    @property
    def TotalCost(self):
        r"""消耗金额，单元：元。
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def GrowthRate(self):
        r"""比上月增长率%。正数增长，负数下降，空值无法统计。
        :rtype: str
        """
        return self._GrowthRate

    @GrowthRate.setter
    def GrowthRate(self, GrowthRate):
        self._GrowthRate = GrowthRate


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Month = params.get("Month")
        self._TotalCost = params.get("TotalCost")
        self._GrowthRate = params.get("GrowthRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgIdentity(AbstractModel):
    r"""组织身份

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID。
        :type IdentityId: int
        :param _IdentityAliasName: 身份名称。
        :type IdentityAliasName: str
        :param _Description: 描述。
        :type Description: str
        :param _IdentityPolicy: 身份策略。
        :type IdentityPolicy: list of IdentityPolicy
        :param _IdentityType: 身份类型。 1-预设、 2-自定义
        :type IdentityType: int
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self._IdentityId = None
        self._IdentityAliasName = None
        self._Description = None
        self._IdentityPolicy = None
        self._IdentityType = None
        self._UpdateTime = None

    @property
    def IdentityId(self):
        r"""身份ID。
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityAliasName(self):
        r"""身份名称。
        :rtype: str
        """
        return self._IdentityAliasName

    @IdentityAliasName.setter
    def IdentityAliasName(self, IdentityAliasName):
        self._IdentityAliasName = IdentityAliasName

    @property
    def Description(self):
        r"""描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IdentityPolicy(self):
        r"""身份策略。
        :rtype: list of IdentityPolicy
        """
        return self._IdentityPolicy

    @IdentityPolicy.setter
    def IdentityPolicy(self, IdentityPolicy):
        self._IdentityPolicy = IdentityPolicy

    @property
    def IdentityType(self):
        r"""身份类型。 1-预设、 2-自定义
        :rtype: int
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def UpdateTime(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityAliasName = params.get("IdentityAliasName")
        self._Description = params.get("Description")
        if params.get("IdentityPolicy") is not None:
            self._IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self._IdentityPolicy.append(obj)
        self._IdentityType = params.get("IdentityType")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMember(AbstractModel):
    r"""企业组织成员

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin
        :type MemberUin: int
        :param _Name: 成员名
        :type Name: str
        :param _MemberType: 成员类型，邀请：Invite， 创建：Create
        :type MemberType: str
        :param _OrgPolicyType: 关系策略类型
        :type OrgPolicyType: str
        :param _OrgPolicyName: 关系策略名
        :type OrgPolicyName: str
        :param _OrgPermission: 关系策略权限
        :type OrgPermission: list of OrgPermission
        :param _NodeId: 所属节点ID
        :type NodeId: int
        :param _NodeName: 所属节点名
        :type NodeName: str
        :param _Remark: 备注
        :type Remark: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _IsAllowQuit: 是否允许成员退出。允许：Allow，不允许：Denied。
        :type IsAllowQuit: str
        :param _PayUin: 代付者Uin
        :type PayUin: str
        :param _PayName: 代付者名称
        :type PayName: str
        :param _OrgIdentity: 管理身份
        :type OrgIdentity: list of MemberIdentity
        :param _BindStatus: 安全信息绑定状态  未绑定：Unbound，待激活：Valid，绑定成功：Success，绑定失败：Failed
        :type BindStatus: str
        :param _PermissionStatus: 成员权限状态 已确认：Confirmed ，待确认：UnConfirmed
        :type PermissionStatus: str
        :param _Tags: 成员标签列表
        :type Tags: list of Tag
        :param _NickName: 腾讯云昵称
        :type NickName: str
        """
        self._MemberUin = None
        self._Name = None
        self._MemberType = None
        self._OrgPolicyType = None
        self._OrgPolicyName = None
        self._OrgPermission = None
        self._NodeId = None
        self._NodeName = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IsAllowQuit = None
        self._PayUin = None
        self._PayName = None
        self._OrgIdentity = None
        self._BindStatus = None
        self._PermissionStatus = None
        self._Tags = None
        self._NickName = None

    @property
    def MemberUin(self):
        r"""成员Uin
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Name(self):
        r"""成员名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MemberType(self):
        r"""成员类型，邀请：Invite， 创建：Create
        :rtype: str
        """
        return self._MemberType

    @MemberType.setter
    def MemberType(self, MemberType):
        self._MemberType = MemberType

    @property
    def OrgPolicyType(self):
        r"""关系策略类型
        :rtype: str
        """
        return self._OrgPolicyType

    @OrgPolicyType.setter
    def OrgPolicyType(self, OrgPolicyType):
        self._OrgPolicyType = OrgPolicyType

    @property
    def OrgPolicyName(self):
        r"""关系策略名
        :rtype: str
        """
        return self._OrgPolicyName

    @OrgPolicyName.setter
    def OrgPolicyName(self, OrgPolicyName):
        self._OrgPolicyName = OrgPolicyName

    @property
    def OrgPermission(self):
        r"""关系策略权限
        :rtype: list of OrgPermission
        """
        return self._OrgPermission

    @OrgPermission.setter
    def OrgPermission(self, OrgPermission):
        self._OrgPermission = OrgPermission

    @property
    def NodeId(self):
        r"""所属节点ID
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def NodeName(self):
        r"""所属节点名
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsAllowQuit(self):
        r"""是否允许成员退出。允许：Allow，不允许：Denied。
        :rtype: str
        """
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        r"""代付者Uin
        :rtype: str
        """
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def PayName(self):
        r"""代付者名称
        :rtype: str
        """
        return self._PayName

    @PayName.setter
    def PayName(self, PayName):
        self._PayName = PayName

    @property
    def OrgIdentity(self):
        r"""管理身份
        :rtype: list of MemberIdentity
        """
        return self._OrgIdentity

    @OrgIdentity.setter
    def OrgIdentity(self, OrgIdentity):
        self._OrgIdentity = OrgIdentity

    @property
    def BindStatus(self):
        r"""安全信息绑定状态  未绑定：Unbound，待激活：Valid，绑定成功：Success，绑定失败：Failed
        :rtype: str
        """
        return self._BindStatus

    @BindStatus.setter
    def BindStatus(self, BindStatus):
        self._BindStatus = BindStatus

    @property
    def PermissionStatus(self):
        r"""成员权限状态 已确认：Confirmed ，待确认：UnConfirmed
        :rtype: str
        """
        return self._PermissionStatus

    @PermissionStatus.setter
    def PermissionStatus(self, PermissionStatus):
        self._PermissionStatus = PermissionStatus

    @property
    def Tags(self):
        r"""成员标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def NickName(self):
        r"""腾讯云昵称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Name = params.get("Name")
        self._MemberType = params.get("MemberType")
        self._OrgPolicyType = params.get("OrgPolicyType")
        self._OrgPolicyName = params.get("OrgPolicyName")
        if params.get("OrgPermission") is not None:
            self._OrgPermission = []
            for item in params.get("OrgPermission"):
                obj = OrgPermission()
                obj._deserialize(item)
                self._OrgPermission.append(obj)
        self._NodeId = params.get("NodeId")
        self._NodeName = params.get("NodeName")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        self._PayName = params.get("PayName")
        if params.get("OrgIdentity") is not None:
            self._OrgIdentity = []
            for item in params.get("OrgIdentity"):
                obj = MemberIdentity()
                obj._deserialize(item)
                self._OrgIdentity.append(obj)
        self._BindStatus = params.get("BindStatus")
        self._PermissionStatus = params.get("PermissionStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._NickName = params.get("NickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthAccount(AbstractModel):
    r"""成员和子账号的授权关系

    """

    def __init__(self):
        r"""
        :param _OrgSubAccountUin: 组织子账号Uin。
        :type OrgSubAccountUin: int
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _PolicyName: 策略名。
        :type PolicyName: str
        :param _IdentityId: 身份ID。
        :type IdentityId: int
        :param _IdentityRoleName: 身份角色名。
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: 身份角色别名。
        :type IdentityRoleAliasName: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _OrgSubAccountName: 子账号名称
        :type OrgSubAccountName: str
        """
        self._OrgSubAccountUin = None
        self._PolicyId = None
        self._PolicyName = None
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._OrgSubAccountName = None

    @property
    def OrgSubAccountUin(self):
        r"""组织子账号Uin。
        :rtype: int
        """
        return self._OrgSubAccountUin

    @OrgSubAccountUin.setter
    def OrgSubAccountUin(self, OrgSubAccountUin):
        self._OrgSubAccountUin = OrgSubAccountUin

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        r"""策略名。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        r"""身份ID。
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        r"""身份角色名。
        :rtype: str
        """
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        r"""身份角色别名。
        :rtype: str
        """
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def OrgSubAccountName(self):
        r"""子账号名称
        :rtype: str
        """
        return self._OrgSubAccountName

    @OrgSubAccountName.setter
    def OrgSubAccountName(self, OrgSubAccountName):
        self._OrgSubAccountName = OrgSubAccountName


    def _deserialize(self, params):
        self._OrgSubAccountUin = params.get("OrgSubAccountUin")
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._OrgSubAccountName = params.get("OrgSubAccountName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberAuthIdentity(AbstractModel):
    r"""组织成员可授权的身份

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID。
        :type IdentityId: int
        :param _IdentityRoleName: 身份的角色名。
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: 身份的角色别名。
        :type IdentityRoleAliasName: str
        :param _Description: 身份描述。
        :type Description: str
        :param _CreateTime: 首次配置成功的时间。
        :type CreateTime: str
        :param _UpdateTime: 最后一次配置成功的时间。
        :type UpdateTime: str
        :param _IdentityType: 身份类型。取值： 1-预设身份  2-自定义身份
        :type IdentityType: int
        :param _Status: 配置状态。取值：1-配置完成 2-需重新配置
        :type Status: int
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _MemberName: 成员名称。
        :type MemberName: str
        """
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IdentityType = None
        self._Status = None
        self._MemberUin = None
        self._MemberName = None

    @property
    def IdentityId(self):
        r"""身份ID。
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        r"""身份的角色名。
        :rtype: str
        """
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        r"""身份的角色别名。
        :rtype: str
        """
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def Description(self):
        r"""身份描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""首次配置成功的时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""最后一次配置成功的时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IdentityType(self):
        r"""身份类型。取值： 1-预设身份  2-自定义身份
        :rtype: int
        """
        return self._IdentityType

    @IdentityType.setter
    def IdentityType(self, IdentityType):
        self._IdentityType = IdentityType

    @property
    def Status(self):
        r"""配置状态。取值：1-配置完成 2-需重新配置
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        r"""成员名称。
        :rtype: str
        """
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IdentityType = params.get("IdentityType")
        self._Status = params.get("Status")
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberFinancial(AbstractModel):
    r"""组织成员财务信息。

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _MemberName: 成员名称。
        :type MemberName: str
        :param _TotalCost: 消耗金额，单位：元。
        :type TotalCost: float
        :param _Ratio: 占比%。
        :type Ratio: str
        """
        self._MemberUin = None
        self._MemberName = None
        self._TotalCost = None
        self._Ratio = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        r"""成员名称。
        :rtype: str
        """
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName

    @property
    def TotalCost(self):
        r"""消耗金额，单位：元。
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Ratio(self):
        r"""占比%。
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        self._TotalCost = params.get("TotalCost")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMemberPolicy(AbstractModel):
    r"""组织成员被授权的策略

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _PolicyName: 策略名。
        :type PolicyName: str
        :param _IdentityId: 身份ID。
        :type IdentityId: int
        :param _IdentityRoleName: 身份角色名。
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: 身份角色别名。
        :type IdentityRoleAliasName: str
        :param _Description: 描述。
        :type Description: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self._PolicyId = None
        self._PolicyName = None
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._Description = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        r"""策略名。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def IdentityId(self):
        r"""身份ID。
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        r"""身份角色名。
        :rtype: str
        """
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        r"""身份角色别名。
        :rtype: str
        """
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def Description(self):
        r"""描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._Description = params.get("Description")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgMembersAuthPolicy(AbstractModel):
    r"""组织成员访问授权策略

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityId: int
        :param _IdentityRoleName: 身份的角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleName: str
        :param _IdentityRoleAliasName: 身份的角色别名。
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityRoleAliasName: str
        :param _CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _PolicyId: 成员访问策略Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: int
        :param _PolicyName: 成员访问策略名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _MemberUin: 成员uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberUin: int
        :param _MemberName: 成员名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberName: str
        :param _OrgSubAccountUin: 子账号uin或者用户组Id。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgSubAccountUin: int
        :param _OrgSubAccountName: 子账号名称或者用户组名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrgSubAccountName: str
        :param _BindType: 绑定类型。1-子账号、2-用户组
注意：此字段可能返回 null，表示取不到有效值。
        :type BindType: int
        :param _Members: 成员信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Members: list of MemberMainInfo
        """
        self._IdentityId = None
        self._IdentityRoleName = None
        self._IdentityRoleAliasName = None
        self._CreateTime = None
        self._PolicyId = None
        self._PolicyName = None
        self._MemberUin = None
        self._MemberName = None
        self._OrgSubAccountUin = None
        self._OrgSubAccountName = None
        self._BindType = None
        self._Members = None

    @property
    def IdentityId(self):
        r"""身份Id。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def IdentityRoleName(self):
        r"""身份的角色名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IdentityRoleName

    @IdentityRoleName.setter
    def IdentityRoleName(self, IdentityRoleName):
        self._IdentityRoleName = IdentityRoleName

    @property
    def IdentityRoleAliasName(self):
        r"""身份的角色别名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IdentityRoleAliasName

    @IdentityRoleAliasName.setter
    def IdentityRoleAliasName(self, IdentityRoleAliasName):
        self._IdentityRoleAliasName = IdentityRoleAliasName

    @property
    def CreateTime(self):
        r"""创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def PolicyId(self):
        r"""成员访问策略Id。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        r"""成员访问策略名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def MemberUin(self):
        r"""成员uin。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        r"""成员名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName

    @property
    def OrgSubAccountUin(self):
        r"""子账号uin或者用户组Id。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OrgSubAccountUin

    @OrgSubAccountUin.setter
    def OrgSubAccountUin(self, OrgSubAccountUin):
        self._OrgSubAccountUin = OrgSubAccountUin

    @property
    def OrgSubAccountName(self):
        r"""子账号名称或者用户组名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OrgSubAccountName

    @OrgSubAccountName.setter
    def OrgSubAccountName(self, OrgSubAccountName):
        self._OrgSubAccountName = OrgSubAccountName

    @property
    def BindType(self):
        r"""绑定类型。1-子账号、2-用户组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def Members(self):
        r"""成员信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MemberMainInfo
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._IdentityRoleName = params.get("IdentityRoleName")
        self._IdentityRoleAliasName = params.get("IdentityRoleAliasName")
        self._CreateTime = params.get("CreateTime")
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        self._OrgSubAccountUin = params.get("OrgSubAccountUin")
        self._OrgSubAccountName = params.get("OrgSubAccountName")
        self._BindType = params.get("BindType")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = MemberMainInfo()
                obj._deserialize(item)
                self._Members.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgNode(AbstractModel):
    r"""企业组织单元

    """

    def __init__(self):
        r"""
        :param _NodeId: 组织节点ID
        :type NodeId: int
        :param _Name: 名称
        :type Name: str
        :param _ParentNodeId: 父节点ID
        :type ParentNodeId: int
        :param _Remark: 备注
        :type Remark: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Tags: 成员标签列表
        :type Tags: list of Tag
        """
        self._NodeId = None
        self._Name = None
        self._ParentNodeId = None
        self._Remark = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Tags = None

    @property
    def NodeId(self):
        r"""组织节点ID
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Name(self):
        r"""名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ParentNodeId(self):
        r"""父节点ID
        :rtype: int
        """
        return self._ParentNodeId

    @ParentNodeId.setter
    def ParentNodeId(self, ParentNodeId):
        self._ParentNodeId = ParentNodeId

    @property
    def Remark(self):
        r"""备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Tags(self):
        r"""成员标签列表
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Name = params.get("Name")
        self._ParentNodeId = params.get("ParentNodeId")
        self._Remark = params.get("Remark")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
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
        


class OrgPermission(AbstractModel):
    r"""关系策略权限

    """

    def __init__(self):
        r"""
        :param _Id: 权限Id
        :type Id: int
        :param _Name: 权限名
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        r"""权限Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""权限名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgProductFinancial(AbstractModel):
    r"""组织产品财务信息

    """

    def __init__(self):
        r"""
        :param _ProductName: 产品Code。
        :type ProductName: str
        :param _ProductCode: 产品名。
        :type ProductCode: str
        :param _TotalCost: 产品消耗，单位：元。
        :type TotalCost: float
        :param _Ratio: 占比%。
        :type Ratio: str
        """
        self._ProductName = None
        self._ProductCode = None
        self._TotalCost = None
        self._Ratio = None

    @property
    def ProductName(self):
        r"""产品Code。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def ProductCode(self):
        r"""产品名。
        :rtype: str
        """
        return self._ProductCode

    @ProductCode.setter
    def ProductCode(self, ProductCode):
        self._ProductCode = ProductCode

    @property
    def TotalCost(self):
        r"""产品消耗，单位：元。
        :rtype: float
        """
        return self._TotalCost

    @TotalCost.setter
    def TotalCost(self, TotalCost):
        self._TotalCost = TotalCost

    @property
    def Ratio(self):
        r"""占比%。
        :rtype: str
        """
        return self._Ratio

    @Ratio.setter
    def Ratio(self, Ratio):
        self._Ratio = Ratio


    def _deserialize(self, params):
        self._ProductName = params.get("ProductName")
        self._ProductCode = params.get("ProductCode")
        self._TotalCost = params.get("TotalCost")
        self._Ratio = params.get("Ratio")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationServiceAssign(AbstractModel):
    r"""集团服务设置

    """

    def __init__(self):
        r"""
        :param _ServiceId: 集团服务ID。
        :type ServiceId: int
        :param _ProductName: 集团服务产品名称。
        :type ProductName: str
        :param _IsAssign: 是否支持委派。取值: 1-是  2-否
        :type IsAssign: int
        :param _Description: 集团服务描述。
        :type Description: str
        :param _MemberNum: 当前委派管理员数。
        :type MemberNum: str
        :param _Document: 帮助文档。
        :type Document: str
        :param _ConsoleUrl: 集团服务产品控制台路径。
        :type ConsoleUrl: str
        :param _IsUsageStatus: 是否接入使用状态。取值: 1-是 
 2-否
        :type IsUsageStatus: int
        :param _CanAssignCount: 委派管理员数量限制。
        :type CanAssignCount: int
        :param _Product: 集团服务产品标识。
        :type Product: str
        :param _ServiceGrant: 是否支持集团服务授权。取值 1-是、2-否
        :type ServiceGrant: int
        :param _GrantStatus: 集团服务授权启用状态。ServiceGrant值为1时该字段有效 ，取值：Enabled-开启  Disabled-关闭 
        :type GrantStatus: str
        :param _IsSetManagementScope: 是否支持设置委派管理范围。取值: 1-是  2-否
        :type IsSetManagementScope: int
        """
        self._ServiceId = None
        self._ProductName = None
        self._IsAssign = None
        self._Description = None
        self._MemberNum = None
        self._Document = None
        self._ConsoleUrl = None
        self._IsUsageStatus = None
        self._CanAssignCount = None
        self._Product = None
        self._ServiceGrant = None
        self._GrantStatus = None
        self._IsSetManagementScope = None

    @property
    def ServiceId(self):
        r"""集团服务ID。
        :rtype: int
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ProductName(self):
        r"""集团服务产品名称。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def IsAssign(self):
        r"""是否支持委派。取值: 1-是  2-否
        :rtype: int
        """
        return self._IsAssign

    @IsAssign.setter
    def IsAssign(self, IsAssign):
        self._IsAssign = IsAssign

    @property
    def Description(self):
        r"""集团服务描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def MemberNum(self):
        r"""当前委派管理员数。
        :rtype: str
        """
        return self._MemberNum

    @MemberNum.setter
    def MemberNum(self, MemberNum):
        self._MemberNum = MemberNum

    @property
    def Document(self):
        r"""帮助文档。
        :rtype: str
        """
        return self._Document

    @Document.setter
    def Document(self, Document):
        self._Document = Document

    @property
    def ConsoleUrl(self):
        r"""集团服务产品控制台路径。
        :rtype: str
        """
        return self._ConsoleUrl

    @ConsoleUrl.setter
    def ConsoleUrl(self, ConsoleUrl):
        self._ConsoleUrl = ConsoleUrl

    @property
    def IsUsageStatus(self):
        r"""是否接入使用状态。取值: 1-是 
 2-否
        :rtype: int
        """
        return self._IsUsageStatus

    @IsUsageStatus.setter
    def IsUsageStatus(self, IsUsageStatus):
        self._IsUsageStatus = IsUsageStatus

    @property
    def CanAssignCount(self):
        r"""委派管理员数量限制。
        :rtype: int
        """
        return self._CanAssignCount

    @CanAssignCount.setter
    def CanAssignCount(self, CanAssignCount):
        self._CanAssignCount = CanAssignCount

    @property
    def Product(self):
        r"""集团服务产品标识。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ServiceGrant(self):
        r"""是否支持集团服务授权。取值 1-是、2-否
        :rtype: int
        """
        return self._ServiceGrant

    @ServiceGrant.setter
    def ServiceGrant(self, ServiceGrant):
        self._ServiceGrant = ServiceGrant

    @property
    def GrantStatus(self):
        r"""集团服务授权启用状态。ServiceGrant值为1时该字段有效 ，取值：Enabled-开启  Disabled-关闭 
        :rtype: str
        """
        return self._GrantStatus

    @GrantStatus.setter
    def GrantStatus(self, GrantStatus):
        self._GrantStatus = GrantStatus

    @property
    def IsSetManagementScope(self):
        r"""是否支持设置委派管理范围。取值: 1-是  2-否
        :rtype: int
        """
        return self._IsSetManagementScope

    @IsSetManagementScope.setter
    def IsSetManagementScope(self, IsSetManagementScope):
        self._IsSetManagementScope = IsSetManagementScope


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ProductName = params.get("ProductName")
        self._IsAssign = params.get("IsAssign")
        self._Description = params.get("Description")
        self._MemberNum = params.get("MemberNum")
        self._Document = params.get("Document")
        self._ConsoleUrl = params.get("ConsoleUrl")
        self._IsUsageStatus = params.get("IsUsageStatus")
        self._CanAssignCount = params.get("CanAssignCount")
        self._Product = params.get("Product")
        self._ServiceGrant = params.get("ServiceGrant")
        self._GrantStatus = params.get("GrantStatus")
        self._IsSetManagementScope = params.get("IsSetManagementScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganizationServiceAssignMember(AbstractModel):
    r"""集团服务委派成员信息

    """

    def __init__(self):
        r"""
        :param _ServiceId: 集团服务ID。
        :type ServiceId: int
        :param _ProductName: 集团服务产品名称。
        :type ProductName: str
        :param _MemberUin: 委派管理员Uin。
        :type MemberUin: int
        :param _MemberName: 委派管理员名称。
        :type MemberName: str
        :param _UsageStatus: 启用状态 。取值：0-服务无启用状态  1-已启用  2-未启用
        :type UsageStatus: int
        :param _CreateTime: 委派时间。
        :type CreateTime: str
        :param _ManagementScope: 委派管理员管理范围。取值: 1-全部成员  2-部分成员
        :type ManagementScope: int
        :param _ManagementScopeMembers: 管理的成员Uin列表。ManagementScope值为2时该参数有效
        :type ManagementScopeMembers: list of MemberMainInfo
        :param _ManagementScopeNodes: 管理的部门ID列表。ManagementScope值为2时该参数有效
        :type ManagementScopeNodes: list of NodeMainInfo
        """
        self._ServiceId = None
        self._ProductName = None
        self._MemberUin = None
        self._MemberName = None
        self._UsageStatus = None
        self._CreateTime = None
        self._ManagementScope = None
        self._ManagementScopeMembers = None
        self._ManagementScopeNodes = None

    @property
    def ServiceId(self):
        r"""集团服务ID。
        :rtype: int
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ProductName(self):
        r"""集团服务产品名称。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def MemberUin(self):
        r"""委派管理员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def MemberName(self):
        r"""委派管理员名称。
        :rtype: str
        """
        return self._MemberName

    @MemberName.setter
    def MemberName(self, MemberName):
        self._MemberName = MemberName

    @property
    def UsageStatus(self):
        r"""启用状态 。取值：0-服务无启用状态  1-已启用  2-未启用
        :rtype: int
        """
        return self._UsageStatus

    @UsageStatus.setter
    def UsageStatus(self, UsageStatus):
        self._UsageStatus = UsageStatus

    @property
    def CreateTime(self):
        r"""委派时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ManagementScope(self):
        r"""委派管理员管理范围。取值: 1-全部成员  2-部分成员
        :rtype: int
        """
        return self._ManagementScope

    @ManagementScope.setter
    def ManagementScope(self, ManagementScope):
        self._ManagementScope = ManagementScope

    @property
    def ManagementScopeMembers(self):
        r"""管理的成员Uin列表。ManagementScope值为2时该参数有效
        :rtype: list of MemberMainInfo
        """
        return self._ManagementScopeMembers

    @ManagementScopeMembers.setter
    def ManagementScopeMembers(self, ManagementScopeMembers):
        self._ManagementScopeMembers = ManagementScopeMembers

    @property
    def ManagementScopeNodes(self):
        r"""管理的部门ID列表。ManagementScope值为2时该参数有效
        :rtype: list of NodeMainInfo
        """
        return self._ManagementScopeNodes

    @ManagementScopeNodes.setter
    def ManagementScopeNodes(self, ManagementScopeNodes):
        self._ManagementScopeNodes = ManagementScopeNodes


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ProductName = params.get("ProductName")
        self._MemberUin = params.get("MemberUin")
        self._MemberName = params.get("MemberName")
        self._UsageStatus = params.get("UsageStatus")
        self._CreateTime = params.get("CreateTime")
        self._ManagementScope = params.get("ManagementScope")
        if params.get("ManagementScopeMembers") is not None:
            self._ManagementScopeMembers = []
            for item in params.get("ManagementScopeMembers"):
                obj = MemberMainInfo()
                obj._deserialize(item)
                self._ManagementScopeMembers.append(obj)
        if params.get("ManagementScopeNodes") is not None:
            self._ManagementScopeNodes = []
            for item in params.get("ManagementScopeNodes"):
                obj = NodeMainInfo()
                obj._deserialize(item)
                self._ManagementScopeNodes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyDetail(AbstractModel):
    r"""策略详情

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略ID。
        :type PolicyId: int
        :param _PolicyName: 策略名称。
        :type PolicyName: str
        """
        self._PolicyId = None
        self._PolicyName = None

    @property
    def PolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyName(self):
        r"""策略名称。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._PolicyName = params.get("PolicyName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductResource(AbstractModel):
    r"""产品资源

    """

    def __init__(self):
        r"""
        :param _ProductResourceId: 产品资源ID。
        :type ProductResourceId: str
        :param _ResourceGrantLast: 资源六段式最后一节
        :type ResourceGrantLast: str
        """
        self._ProductResourceId = None
        self._ResourceGrantLast = None

    @property
    def ProductResourceId(self):
        r"""产品资源ID。
        :rtype: str
        """
        return self._ProductResourceId

    @ProductResourceId.setter
    def ProductResourceId(self, ProductResourceId):
        self._ProductResourceId = ProductResourceId

    @property
    def ResourceGrantLast(self):
        warnings.warn("parameter `ResourceGrantLast` is deprecated", DeprecationWarning) 

        r"""资源六段式最后一节
        :rtype: str
        """
        return self._ResourceGrantLast

    @ResourceGrantLast.setter
    def ResourceGrantLast(self, ResourceGrantLast):
        warnings.warn("parameter `ResourceGrantLast` is deprecated", DeprecationWarning) 

        self._ResourceGrantLast = ResourceGrantLast


    def _deserialize(self, params):
        self._ProductResourceId = params.get("ProductResourceId")
        self._ResourceGrantLast = params.get("ResourceGrantLast")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProvisionRoleConfigurationRequest(AbstractModel):
    r"""ProvisionRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号。
        :type TargetType: str
        :param _TargetUin: 集团账号目标账号的UIN。
        :type TargetUin: int
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._TargetType = None
        self._TargetUin = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号。
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetUin(self):
        r"""集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._TargetType = params.get("TargetType")
        self._TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProvisionRoleConfigurationResponse(AbstractModel):
    r"""ProvisionRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Task: 任务详情。
        :type Task: :class:`tencentcloud.organization.v20210331.models.RoleProvisioningsTask`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Task = None
        self._RequestId = None

    @property
    def Task(self):
        r"""任务详情。
        :rtype: :class:`tencentcloud.organization.v20210331.models.RoleProvisioningsTask`
        """
        return self._Task

    @Task.setter
    def Task(self, Task):
        self._Task = Task

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
        if params.get("Task") is not None:
            self._Task = RoleProvisioningsTask()
            self._Task._deserialize(params.get("Task"))
        self._RequestId = params.get("RequestId")


class QuitOrganizationRequest(AbstractModel):
    r"""QuitOrganization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _OrgId: 企业组织ID
        :type OrgId: int
        """
        self._OrgId = None

    @property
    def OrgId(self):
        r"""企业组织ID
        :rtype: int
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuitOrganizationResponse(AbstractModel):
    r"""QuitOrganization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RejectJoinShareUnitInvitationRequest(AbstractModel):
    r"""RejectJoinShareUnitInvitation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        """
        self._UnitId = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectJoinShareUnitInvitationResponse(AbstractModel):
    r"""RejectJoinShareUnitInvitation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RemoveExternalSAMLIdPCertificateRequest(AbstractModel):
    r"""RemoveExternalSAMLIdPCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _CertificateId: PEM 格式的 X509 证书。  由 SAML 身份提供商提供。
        :type CertificateId: str
        """
        self._ZoneId = None
        self._CertificateId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CertificateId(self):
        r"""PEM 格式的 X509 证书。  由 SAML 身份提供商提供。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveExternalSAMLIdPCertificateResponse(AbstractModel):
    r"""RemoveExternalSAMLIdPCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RemovePermissionPolicyFromRoleConfigurationRequest(AbstractModel):
    r"""RemovePermissionPolicyFromRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置 ID
        :type RoleConfigurationId: str
        :param _RolePolicyType: 权限策略类型。取值：  System：系统策略。复用 CAM 的系统策略。 Custom: 自定义策略。按照 CAM 权限策略语法和结构编写的自定义策略。
        :type RolePolicyType: str
        :param _RolePolicyName: 权限策略名称，长度最大为 32 个字符。
        :type RolePolicyName: str
        :param _RolePolicyId: 策略ID。
        :type RolePolicyId: int
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._RolePolicyType = None
        self._RolePolicyName = None
        self._RolePolicyId = None

    @property
    def ZoneId(self):
        r"""空间 ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置 ID
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def RolePolicyType(self):
        r"""权限策略类型。取值：  System：系统策略。复用 CAM 的系统策略。 Custom: 自定义策略。按照 CAM 权限策略语法和结构编写的自定义策略。
        :rtype: str
        """
        return self._RolePolicyType

    @RolePolicyType.setter
    def RolePolicyType(self, RolePolicyType):
        self._RolePolicyType = RolePolicyType

    @property
    def RolePolicyName(self):
        r"""权限策略名称，长度最大为 32 个字符。
        :rtype: str
        """
        return self._RolePolicyName

    @RolePolicyName.setter
    def RolePolicyName(self, RolePolicyName):
        self._RolePolicyName = RolePolicyName

    @property
    def RolePolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._RolePolicyId

    @RolePolicyId.setter
    def RolePolicyId(self, RolePolicyId):
        self._RolePolicyId = RolePolicyId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._RolePolicyType = params.get("RolePolicyType")
        self._RolePolicyName = params.get("RolePolicyName")
        self._RolePolicyId = params.get("RolePolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePermissionPolicyFromRoleConfigurationResponse(AbstractModel):
    r"""RemovePermissionPolicyFromRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class RemoveUserFromGroupRequest(AbstractModel):
    r"""RemoveUserFromGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _GroupId: 用户组ID。
        :type GroupId: str
        :param _UserId: 用户ID。
        :type UserId: str
        """
        self._ZoneId = None
        self._GroupId = None
        self._UserId = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        r"""用户组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def UserId(self):
        r"""用户ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        self._UserId = params.get("UserId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveUserFromGroupResponse(AbstractModel):
    r"""RemoveUserFromGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ResourceTagMapping(AbstractModel):
    r"""资源及关联的标签

    """

    def __init__(self):
        r"""
        :param _Resource: 资源六段式。腾讯云使用资源六段式描述一个资源。
例如：qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}。
        :type Resource: str
        :param _ComplianceDetails: 合规详情。
        :type ComplianceDetails: :class:`tencentcloud.organization.v20210331.models.TagComplianceDetails`
        :param _Tags: 资源标签。
        :type Tags: list of Tags
        """
        self._Resource = None
        self._ComplianceDetails = None
        self._Tags = None

    @property
    def Resource(self):
        r"""资源六段式。腾讯云使用资源六段式描述一个资源。
例如：qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}。
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ComplianceDetails(self):
        r"""合规详情。
        :rtype: :class:`tencentcloud.organization.v20210331.models.TagComplianceDetails`
        """
        return self._ComplianceDetails

    @ComplianceDetails.setter
    def ComplianceDetails(self, ComplianceDetails):
        self._ComplianceDetails = ComplianceDetails

    @property
    def Tags(self):
        r"""资源标签。
        :rtype: list of Tags
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("ComplianceDetails") is not None:
            self._ComplianceDetails = TagComplianceDetails()
            self._ComplianceDetails._deserialize(params.get("ComplianceDetails"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleAssignmentInfo(AbstractModel):
    r"""授权成员账号信息

    """

    def __init__(self):
        r"""
        :param _PrincipalId: CAM 用户同步的身份 ID。取值：
当PrincipalType取值为Group时，该值为CIC用户组 ID（g-********）。
当PrincipalType取值为User时，该值为CIC用户 ID（u-********）。
        :type PrincipalId: str
        :param _PrincipalType: CAM 用户同步的身份类型。取值：

User：表示该 CAM 用户同步的身份是CIC用户。
Group：表示该 CAM 用户同步的身份是CIC用户组。
        :type PrincipalType: str
        :param _TargetUin: 同步集团账号目标账号的UIN。
        :type TargetUin: int
        :param _TargetType: 同步集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        """
        self._PrincipalId = None
        self._PrincipalType = None
        self._TargetUin = None
        self._TargetType = None
        self._RoleConfigurationId = None

    @property
    def PrincipalId(self):
        r"""CAM 用户同步的身份 ID。取值：
当PrincipalType取值为Group时，该值为CIC用户组 ID（g-********）。
当PrincipalType取值为User时，该值为CIC用户 ID（u-********）。
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值：

User：表示该 CAM 用户同步的身份是CIC用户。
Group：表示该 CAM 用户同步的身份是CIC用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def TargetUin(self):
        r"""同步集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetType(self):
        r"""同步集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId


    def _deserialize(self, params):
        self._PrincipalId = params.get("PrincipalId")
        self._PrincipalType = params.get("PrincipalType")
        self._TargetUin = params.get("TargetUin")
        self._TargetType = params.get("TargetType")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleAssignments(AbstractModel):
    r"""成员账号的授权详情

    """

    def __init__(self):
        r"""
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _RoleConfigurationName: 权限配置名称。
        :type RoleConfigurationName: str
        :param _TargetUin: 集团账号目标账号的UIN。
        :type TargetUin: int
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号。
        :type TargetType: str
        :param _PrincipalId: CAM 用户同步的身份 ID。取值： 当PrincipalType取值为Group时，该值为CIC 用户组 ID（g-********）。 当PrincipalType取值为User时，该值为CIC 用户 ID（u-********）。
        :type PrincipalId: str
        :param _PrincipalType: CAM 用户同步的身份类型。取值： User：表示该 CAM 用户同步的身份是CIC用户。 Group：表示该 CAM 用户同步的身份是CIC用户组。
        :type PrincipalType: str
        :param _PrincipalName: 用户名称或者用户组名称
        :type PrincipalName: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _TargetName: 集团账号目标账号的名称。
        :type TargetName: str
        """
        self._RoleConfigurationId = None
        self._RoleConfigurationName = None
        self._TargetUin = None
        self._TargetType = None
        self._PrincipalId = None
        self._PrincipalType = None
        self._PrincipalName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._TargetName = None

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def RoleConfigurationName(self):
        r"""权限配置名称。
        :rtype: str
        """
        return self._RoleConfigurationName

    @RoleConfigurationName.setter
    def RoleConfigurationName(self, RoleConfigurationName):
        self._RoleConfigurationName = RoleConfigurationName

    @property
    def TargetUin(self):
        r"""集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号。
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def PrincipalId(self):
        r"""CAM 用户同步的身份 ID。取值： 当PrincipalType取值为Group时，该值为CIC 用户组 ID（g-********）。 当PrincipalType取值为User时，该值为CIC 用户 ID（u-********）。
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值： User：表示该 CAM 用户同步的身份是CIC用户。 Group：表示该 CAM 用户同步的身份是CIC用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def PrincipalName(self):
        r"""用户名称或者用户组名称
        :rtype: str
        """
        return self._PrincipalName

    @PrincipalName.setter
    def PrincipalName(self, PrincipalName):
        self._PrincipalName = PrincipalName

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TargetName(self):
        r"""集团账号目标账号的名称。
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName


    def _deserialize(self, params):
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._RoleConfigurationName = params.get("RoleConfigurationName")
        self._TargetUin = params.get("TargetUin")
        self._TargetType = params.get("TargetType")
        self._PrincipalId = params.get("PrincipalId")
        self._PrincipalType = params.get("PrincipalType")
        self._PrincipalName = params.get("PrincipalName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TargetName = params.get("TargetName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleConfiguration(AbstractModel):
    r"""CIC权限配置

    """

    def __init__(self):
        r"""
        :param _RoleConfigurationId: 权限配置配置ID。
        :type RoleConfigurationId: str
        :param _RoleConfigurationName: 权限配置配名称。
        :type RoleConfigurationName: str
        :param _Description: 权限配置的描述。
        :type Description: str
        :param _SessionDuration: 会话持续时间。CIC 用户使用访问配置访问成员账号时，会话最多保持的时间。
单位：秒。
        :type SessionDuration: int
        :param _RelayState: 初始访问页面。CIC 用户使用访问配置访问成员账号时，初始访问的页面地址。
        :type RelayState: str
        :param _CreateTime: 权限配置的创建时间。
        :type CreateTime: str
        :param _UpdateTime: 权限配置的更新时间。
        :type UpdateTime: str
        :param _IsSelected: 如果有入参FilterTargets查询成员账号是否配置过权限，配置了返回true，否则返回false。
        :type IsSelected: bool
        """
        self._RoleConfigurationId = None
        self._RoleConfigurationName = None
        self._Description = None
        self._SessionDuration = None
        self._RelayState = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IsSelected = None

    @property
    def RoleConfigurationId(self):
        r"""权限配置配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def RoleConfigurationName(self):
        r"""权限配置配名称。
        :rtype: str
        """
        return self._RoleConfigurationName

    @RoleConfigurationName.setter
    def RoleConfigurationName(self, RoleConfigurationName):
        self._RoleConfigurationName = RoleConfigurationName

    @property
    def Description(self):
        r"""权限配置的描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def SessionDuration(self):
        r"""会话持续时间。CIC 用户使用访问配置访问成员账号时，会话最多保持的时间。
单位：秒。
        :rtype: int
        """
        return self._SessionDuration

    @SessionDuration.setter
    def SessionDuration(self, SessionDuration):
        self._SessionDuration = SessionDuration

    @property
    def RelayState(self):
        r"""初始访问页面。CIC 用户使用访问配置访问成员账号时，初始访问的页面地址。
        :rtype: str
        """
        return self._RelayState

    @RelayState.setter
    def RelayState(self, RelayState):
        self._RelayState = RelayState

    @property
    def CreateTime(self):
        r"""权限配置的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""权限配置的更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsSelected(self):
        r"""如果有入参FilterTargets查询成员账号是否配置过权限，配置了返回true，否则返回false。
        :rtype: bool
        """
        return self._IsSelected

    @IsSelected.setter
    def IsSelected(self, IsSelected):
        self._IsSelected = IsSelected


    def _deserialize(self, params):
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._RoleConfigurationName = params.get("RoleConfigurationName")
        self._Description = params.get("Description")
        self._SessionDuration = params.get("SessionDuration")
        self._RelayState = params.get("RelayState")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IsSelected = params.get("IsSelected")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleConfigurationProvisionings(AbstractModel):
    r"""权限配置同步

    """

    def __init__(self):
        r"""
        :param _DeploymentStatus: Deployed: 部署成功 DeployedRequired：需要重新部署 DeployFailed：部署失败
        :type DeploymentStatus: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _RoleConfigurationName: 权限配置名称。
        :type RoleConfigurationName: str
        :param _TargetUin: 集团账号目标账号的UIN
        :type TargetUin: int
        :param _TargetName: 集团账号目标账号的名称。
        :type TargetName: str
        :param _CreateTime: 创建时间，
        :type CreateTime: str
        :param _UpdateTime: 修改时间，
        :type UpdateTime: str
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        """
        self._DeploymentStatus = None
        self._RoleConfigurationId = None
        self._RoleConfigurationName = None
        self._TargetUin = None
        self._TargetName = None
        self._CreateTime = None
        self._UpdateTime = None
        self._TargetType = None

    @property
    def DeploymentStatus(self):
        r"""Deployed: 部署成功 DeployedRequired：需要重新部署 DeployFailed：部署失败
        :rtype: str
        """
        return self._DeploymentStatus

    @DeploymentStatus.setter
    def DeploymentStatus(self, DeploymentStatus):
        self._DeploymentStatus = DeploymentStatus

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def RoleConfigurationName(self):
        r"""权限配置名称。
        :rtype: str
        """
        return self._RoleConfigurationName

    @RoleConfigurationName.setter
    def RoleConfigurationName(self, RoleConfigurationName):
        self._RoleConfigurationName = RoleConfigurationName

    @property
    def TargetUin(self):
        r"""集团账号目标账号的UIN
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetName(self):
        r"""集团账号目标账号的名称。
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def CreateTime(self):
        r"""创建时间，
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""修改时间，
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType


    def _deserialize(self, params):
        self._DeploymentStatus = params.get("DeploymentStatus")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._RoleConfigurationName = params.get("RoleConfigurationName")
        self._TargetUin = params.get("TargetUin")
        self._TargetName = params.get("TargetName")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TargetType = params.get("TargetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RolePolicie(AbstractModel):
    r"""CIC的权限策略

    """

    def __init__(self):
        r"""
        :param _RolePolicyId: 策略ID。
        :type RolePolicyId: int
        :param _RolePolicyName: 权限策略名称
        :type RolePolicyName: str
        :param _RolePolicyType: 权限策略类型
        :type RolePolicyType: str
        :param _RolePolicyDocument: 自定义策略内容。仅自定义策略返回该参数。
        :type RolePolicyDocument: str
        :param _AddTime: 权限策略被添加到权限配置的时间。
        :type AddTime: str
        """
        self._RolePolicyId = None
        self._RolePolicyName = None
        self._RolePolicyType = None
        self._RolePolicyDocument = None
        self._AddTime = None

    @property
    def RolePolicyId(self):
        r"""策略ID。
        :rtype: int
        """
        return self._RolePolicyId

    @RolePolicyId.setter
    def RolePolicyId(self, RolePolicyId):
        self._RolePolicyId = RolePolicyId

    @property
    def RolePolicyName(self):
        r"""权限策略名称
        :rtype: str
        """
        return self._RolePolicyName

    @RolePolicyName.setter
    def RolePolicyName(self, RolePolicyName):
        self._RolePolicyName = RolePolicyName

    @property
    def RolePolicyType(self):
        r"""权限策略类型
        :rtype: str
        """
        return self._RolePolicyType

    @RolePolicyType.setter
    def RolePolicyType(self, RolePolicyType):
        self._RolePolicyType = RolePolicyType

    @property
    def RolePolicyDocument(self):
        r"""自定义策略内容。仅自定义策略返回该参数。
        :rtype: str
        """
        return self._RolePolicyDocument

    @RolePolicyDocument.setter
    def RolePolicyDocument(self, RolePolicyDocument):
        self._RolePolicyDocument = RolePolicyDocument

    @property
    def AddTime(self):
        r"""权限策略被添加到权限配置的时间。
        :rtype: str
        """
        return self._AddTime

    @AddTime.setter
    def AddTime(self, AddTime):
        self._AddTime = AddTime


    def _deserialize(self, params):
        self._RolePolicyId = params.get("RolePolicyId")
        self._RolePolicyName = params.get("RolePolicyName")
        self._RolePolicyType = params.get("RolePolicyType")
        self._RolePolicyDocument = params.get("RolePolicyDocument")
        self._AddTime = params.get("AddTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleProvisioningsTask(AbstractModel):
    r"""同步部署角色任务状态信息。

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _RoleConfigurationName: 权限配置名称。
        :type RoleConfigurationName: str
        :param _TargetUin: 授权的集团账号目标账号的UIN
        :type TargetUin: int
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _TaskType: 任务类型。
        :type TaskType: str
        :param _TaskStatus: 任务状态：InProgress: 进行中，Failed: 失败 3:Success: 成功
        :type TaskStatus: str
        """
        self._TaskId = None
        self._RoleConfigurationId = None
        self._RoleConfigurationName = None
        self._TargetUin = None
        self._TargetType = None
        self._TaskType = None
        self._TaskStatus = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def RoleConfigurationName(self):
        r"""权限配置名称。
        :rtype: str
        """
        return self._RoleConfigurationName

    @RoleConfigurationName.setter
    def RoleConfigurationName(self, RoleConfigurationName):
        self._RoleConfigurationName = RoleConfigurationName

    @property
    def TargetUin(self):
        r"""授权的集团账号目标账号的UIN
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TaskType(self):
        r"""任务类型。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskStatus(self):
        r"""任务状态：InProgress: 进行中，Failed: 失败 3:Success: 成功
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._RoleConfigurationName = params.get("RoleConfigurationName")
        self._TargetUin = params.get("TargetUin")
        self._TargetType = params.get("TargetType")
        self._TaskType = params.get("TaskType")
        self._TaskStatus = params.get("TaskStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SAMLIdPCertificate(AbstractModel):
    r"""SAML 签名证书信息

    """

    def __init__(self):
        r"""
        :param _SerialNumber: 证书序列号。
        :type SerialNumber: str
        :param _Issuer: 证书颁发者。
        :type Issuer: str
        :param _Version: 证书版本。
        :type Version: int
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        :param _PublicKey: PEM 格式的公钥证书（Base64 编码）。
        :type PublicKey: str
        :param _SignatureAlgorithm: 证书的签名算法。
        :type SignatureAlgorithm: str
        :param _NotAfter: 证书的过期时间。
        :type NotAfter: str
        :param _NotBefore: 证书的创建时间。
        :type NotBefore: str
        :param _Subject: 证书的主体。
        :type Subject: str
        :param _X509Certificate: PEM 格式的 X509 证书。
        :type X509Certificate: str
        """
        self._SerialNumber = None
        self._Issuer = None
        self._Version = None
        self._CertificateId = None
        self._PublicKey = None
        self._SignatureAlgorithm = None
        self._NotAfter = None
        self._NotBefore = None
        self._Subject = None
        self._X509Certificate = None

    @property
    def SerialNumber(self):
        r"""证书序列号。
        :rtype: str
        """
        return self._SerialNumber

    @SerialNumber.setter
    def SerialNumber(self, SerialNumber):
        self._SerialNumber = SerialNumber

    @property
    def Issuer(self):
        r"""证书颁发者。
        :rtype: str
        """
        return self._Issuer

    @Issuer.setter
    def Issuer(self, Issuer):
        self._Issuer = Issuer

    @property
    def Version(self):
        r"""证书版本。
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def CertificateId(self):
        r"""证书ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def PublicKey(self):
        r"""PEM 格式的公钥证书（Base64 编码）。
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def SignatureAlgorithm(self):
        r"""证书的签名算法。
        :rtype: str
        """
        return self._SignatureAlgorithm

    @SignatureAlgorithm.setter
    def SignatureAlgorithm(self, SignatureAlgorithm):
        self._SignatureAlgorithm = SignatureAlgorithm

    @property
    def NotAfter(self):
        r"""证书的过期时间。
        :rtype: str
        """
        return self._NotAfter

    @NotAfter.setter
    def NotAfter(self, NotAfter):
        self._NotAfter = NotAfter

    @property
    def NotBefore(self):
        r"""证书的创建时间。
        :rtype: str
        """
        return self._NotBefore

    @NotBefore.setter
    def NotBefore(self, NotBefore):
        self._NotBefore = NotBefore

    @property
    def Subject(self):
        r"""证书的主体。
        :rtype: str
        """
        return self._Subject

    @Subject.setter
    def Subject(self, Subject):
        self._Subject = Subject

    @property
    def X509Certificate(self):
        r"""PEM 格式的 X509 证书。
        :rtype: str
        """
        return self._X509Certificate

    @X509Certificate.setter
    def X509Certificate(self, X509Certificate):
        self._X509Certificate = X509Certificate


    def _deserialize(self, params):
        self._SerialNumber = params.get("SerialNumber")
        self._Issuer = params.get("Issuer")
        self._Version = params.get("Version")
        self._CertificateId = params.get("CertificateId")
        self._PublicKey = params.get("PublicKey")
        self._SignatureAlgorithm = params.get("SignatureAlgorithm")
        self._NotAfter = params.get("NotAfter")
        self._NotBefore = params.get("NotBefore")
        self._Subject = params.get("Subject")
        self._X509Certificate = params.get("X509Certificate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SAMLIdentityProviderConfiguration(AbstractModel):
    r"""saml 身份提供商配置信息。

    """

    def __init__(self):
        r"""
        :param _EntityId: IdP 标识。
        :type EntityId: str
        :param _SSOStatus: SSO 登录的启用状态。取值：  Enabled：启用。 Disabled（默认值）：禁用。
        :type SSOStatus: str
        :param _EncodedMetadataDocument: IdP 元数据文档（Base64 编码）。
        :type EncodedMetadataDocument: str
        :param _CertificateIds: X509证书ID。
        :type CertificateIds: list of str
        :param _LoginUrl: IdP 的登录地址。
        :type LoginUrl: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        """
        self._EntityId = None
        self._SSOStatus = None
        self._EncodedMetadataDocument = None
        self._CertificateIds = None
        self._LoginUrl = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def EntityId(self):
        r"""IdP 标识。
        :rtype: str
        """
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def SSOStatus(self):
        r"""SSO 登录的启用状态。取值：  Enabled：启用。 Disabled（默认值）：禁用。
        :rtype: str
        """
        return self._SSOStatus

    @SSOStatus.setter
    def SSOStatus(self, SSOStatus):
        self._SSOStatus = SSOStatus

    @property
    def EncodedMetadataDocument(self):
        r"""IdP 元数据文档（Base64 编码）。
        :rtype: str
        """
        return self._EncodedMetadataDocument

    @EncodedMetadataDocument.setter
    def EncodedMetadataDocument(self, EncodedMetadataDocument):
        self._EncodedMetadataDocument = EncodedMetadataDocument

    @property
    def CertificateIds(self):
        r"""X509证书ID。
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def LoginUrl(self):
        r"""IdP 的登录地址。
        :rtype: str
        """
        return self._LoginUrl

    @LoginUrl.setter
    def LoginUrl(self, LoginUrl):
        self._LoginUrl = LoginUrl

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._EntityId = params.get("EntityId")
        self._SSOStatus = params.get("SSOStatus")
        self._EncodedMetadataDocument = params.get("EncodedMetadataDocument")
        self._CertificateIds = params.get("CertificateIds")
        self._LoginUrl = params.get("LoginUrl")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SAMLServiceProvider(AbstractModel):
    r"""SAML服务提供商信息

    """

    def __init__(self):
        r"""
        :param _EntityId: https://tencentcloudsso.com/saml/sp/z-sjw8ensa**
        :type EntityId: str
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _EncodedMetadataDocument: SP 元数据文档（Base64 编码）。
        :type EncodedMetadataDocument: str
        :param _AcsUrl: SP 的 ACS URL。
        :type AcsUrl: str
        """
        self._EntityId = None
        self._ZoneId = None
        self._EncodedMetadataDocument = None
        self._AcsUrl = None

    @property
    def EntityId(self):
        r"""https://tencentcloudsso.com/saml/sp/z-sjw8ensa**
        :rtype: str
        """
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EncodedMetadataDocument(self):
        r"""SP 元数据文档（Base64 编码）。
        :rtype: str
        """
        return self._EncodedMetadataDocument

    @EncodedMetadataDocument.setter
    def EncodedMetadataDocument(self, EncodedMetadataDocument):
        self._EncodedMetadataDocument = EncodedMetadataDocument

    @property
    def AcsUrl(self):
        r"""SP 的 ACS URL。
        :rtype: str
        """
        return self._AcsUrl

    @AcsUrl.setter
    def AcsUrl(self, AcsUrl):
        self._AcsUrl = AcsUrl


    def _deserialize(self, params):
        self._EntityId = params.get("EntityId")
        self._ZoneId = params.get("ZoneId")
        self._EncodedMetadataDocument = params.get("EncodedMetadataDocument")
        self._AcsUrl = params.get("AcsUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SCIMCredential(AbstractModel):
    r"""SCIM密钥

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _Status: SCIM密钥状态，Enabled已开启，Disabled已关闭。
        :type Status: str
        :param _CredentialId: SCIM密钥ID。scimcred-前缀开头，后面是12位随机数字/小写字母。
        :type CredentialId: str
        :param _CredentialType: SCIM密钥类型。
        :type CredentialType: str
        :param _CreateTime: SCIM 密钥的创建时间。
        :type CreateTime: str
        :param _ExpireTime: SCIM 密钥的过期时间。
        :type ExpireTime: str
        """
        self._ZoneId = None
        self._Status = None
        self._CredentialId = None
        self._CredentialType = None
        self._CreateTime = None
        self._ExpireTime = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        r"""SCIM密钥状态，Enabled已开启，Disabled已关闭。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CredentialId(self):
        r"""SCIM密钥ID。scimcred-前缀开头，后面是12位随机数字/小写字母。
        :rtype: str
        """
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId

    @property
    def CredentialType(self):
        r"""SCIM密钥类型。
        :rtype: str
        """
        return self._CredentialType

    @CredentialType.setter
    def CredentialType(self, CredentialType):
        self._CredentialType = CredentialType

    @property
    def CreateTime(self):
        r"""SCIM 密钥的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        r"""SCIM 密钥的过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Status = params.get("Status")
        self._CredentialId = params.get("CredentialId")
        self._CredentialType = params.get("CredentialType")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendOrgMemberAccountBindEmailRequest(AbstractModel):
    r"""SendOrgMemberAccountBindEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _BindId: 绑定ID。可以通过[DescribeOrganizationMemberEmailBind](https://cloud.tencent.com/document/product/850/93332)获取
        :type BindId: int
        """
        self._MemberUin = None
        self._BindId = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def BindId(self):
        r"""绑定ID。可以通过[DescribeOrganizationMemberEmailBind](https://cloud.tencent.com/document/product/850/93332)获取
        :rtype: int
        """
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._BindId = params.get("BindId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendOrgMemberAccountBindEmailResponse(AbstractModel):
    r"""SendOrgMemberAccountBindEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class SetExternalSAMLIdentityProviderRequest(AbstractModel):
    r"""SetExternalSAMLIdentityProvider请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _EncodedMetadataDocument: IdP 元数据文档（Base64 编码）。  由支持 SAML 2.0 协议的 IdP 提供。
        :type EncodedMetadataDocument: str
        :param _SSOStatus: SSO 登录的启用状态。取值：  Enabled：启用。 Disabled（默认值）：禁用。
        :type SSOStatus: str
        :param _EntityId: IdP 标识。
        :type EntityId: str
        :param _LoginUrl: IdP 的登录地址。
        :type LoginUrl: str
        :param _X509Certificate: PEM 格式的 X509 证书。指定该参数会替换所有已经存在的证书。
        :type X509Certificate: str
        """
        self._ZoneId = None
        self._EncodedMetadataDocument = None
        self._SSOStatus = None
        self._EntityId = None
        self._LoginUrl = None
        self._X509Certificate = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def EncodedMetadataDocument(self):
        r"""IdP 元数据文档（Base64 编码）。  由支持 SAML 2.0 协议的 IdP 提供。
        :rtype: str
        """
        return self._EncodedMetadataDocument

    @EncodedMetadataDocument.setter
    def EncodedMetadataDocument(self, EncodedMetadataDocument):
        self._EncodedMetadataDocument = EncodedMetadataDocument

    @property
    def SSOStatus(self):
        r"""SSO 登录的启用状态。取值：  Enabled：启用。 Disabled（默认值）：禁用。
        :rtype: str
        """
        return self._SSOStatus

    @SSOStatus.setter
    def SSOStatus(self, SSOStatus):
        self._SSOStatus = SSOStatus

    @property
    def EntityId(self):
        r"""IdP 标识。
        :rtype: str
        """
        return self._EntityId

    @EntityId.setter
    def EntityId(self, EntityId):
        self._EntityId = EntityId

    @property
    def LoginUrl(self):
        r"""IdP 的登录地址。
        :rtype: str
        """
        return self._LoginUrl

    @LoginUrl.setter
    def LoginUrl(self, LoginUrl):
        self._LoginUrl = LoginUrl

    @property
    def X509Certificate(self):
        r"""PEM 格式的 X509 证书。指定该参数会替换所有已经存在的证书。
        :rtype: str
        """
        return self._X509Certificate

    @X509Certificate.setter
    def X509Certificate(self, X509Certificate):
        self._X509Certificate = X509Certificate


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._EncodedMetadataDocument = params.get("EncodedMetadataDocument")
        self._SSOStatus = params.get("SSOStatus")
        self._EntityId = params.get("EntityId")
        self._LoginUrl = params.get("LoginUrl")
        self._X509Certificate = params.get("X509Certificate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetExternalSAMLIdentityProviderResponse(AbstractModel):
    r"""SetExternalSAMLIdentityProvider返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID。
        :type CertificateIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateIds = None
        self._RequestId = None

    @property
    def CertificateIds(self):
        r"""证书ID。
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

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
        self._CertificateIds = params.get("CertificateIds")
        self._RequestId = params.get("RequestId")


class ShareArea(AbstractModel):
    r"""共享地域

    """

    def __init__(self):
        r"""
        :param _Name: 地域名称。
        :type Name: str
        :param _Area: 地域标识。
        :type Area: str
        :param _AreaId: 地域ID。
        :type AreaId: int
        """
        self._Name = None
        self._Area = None
        self._AreaId = None

    @property
    def Name(self):
        r"""地域名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Area(self):
        r"""地域标识。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AreaId(self):
        r"""地域ID。
        :rtype: int
        """
        return self._AreaId

    @AreaId.setter
    def AreaId(self, AreaId):
        self._AreaId = AreaId


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Area = params.get("Area")
        self._AreaId = params.get("AreaId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareMember(AbstractModel):
    r"""共享成员信息

    """

    def __init__(self):
        r"""
        :param _ShareMemberUin: 共享成员Uin。
        :type ShareMemberUin: int
        """
        self._ShareMemberUin = None

    @property
    def ShareMemberUin(self):
        r"""共享成员Uin。
        :rtype: int
        """
        return self._ShareMemberUin

    @ShareMemberUin.setter
    def ShareMemberUin(self, ShareMemberUin):
        self._ShareMemberUin = ShareMemberUin


    def _deserialize(self, params):
        self._ShareMemberUin = params.get("ShareMemberUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareResource(AbstractModel):
    r"""共享资源

    """

    def __init__(self):
        r"""
        :param _ResourceId: 共享资源ID。
        :type ResourceId: str
        :param _ProductResourceId: 产品资源ID。
        :type ProductResourceId: str
        """
        self._ResourceId = None
        self._ProductResourceId = None

    @property
    def ResourceId(self):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        r"""共享资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        warnings.warn("parameter `ResourceId` is deprecated", DeprecationWarning) 

        self._ResourceId = ResourceId

    @property
    def ProductResourceId(self):
        r"""产品资源ID。
        :rtype: str
        """
        return self._ProductResourceId

    @ProductResourceId.setter
    def ProductResourceId(self, ProductResourceId):
        self._ProductResourceId = ProductResourceId


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ProductResourceId = params.get("ProductResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareResourceToMember(AbstractModel):
    r"""与我共享的资源

    """

    def __init__(self):
        r"""
        :param _ResourceId: 共享单元资源ID。
        :type ResourceId: str
        :param _Type: 资源类型。
        :type Type: str
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _UnitName: 共享单元名称。
        :type UnitName: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _ProductResourceId: 业务资源ID。
        :type ProductResourceId: str
        :param _ShareManagerUin: 共享账号Uin。
        :type ShareManagerUin: int
        """
        self._ResourceId = None
        self._Type = None
        self._UnitId = None
        self._UnitName = None
        self._CreateTime = None
        self._ProductResourceId = None
        self._ShareManagerUin = None

    @property
    def ResourceId(self):
        r"""共享单元资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Type(self):
        r"""资源类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def UnitName(self):
        r"""共享单元名称。
        :rtype: str
        """
        return self._UnitName

    @UnitName.setter
    def UnitName(self, UnitName):
        self._UnitName = UnitName

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductResourceId(self):
        r"""业务资源ID。
        :rtype: str
        """
        return self._ProductResourceId

    @ProductResourceId.setter
    def ProductResourceId(self, ProductResourceId):
        self._ProductResourceId = ProductResourceId

    @property
    def ShareManagerUin(self):
        r"""共享账号Uin。
        :rtype: int
        """
        return self._ShareManagerUin

    @ShareManagerUin.setter
    def ShareManagerUin(self, ShareManagerUin):
        self._ShareManagerUin = ShareManagerUin


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Type = params.get("Type")
        self._UnitId = params.get("UnitId")
        self._UnitName = params.get("UnitName")
        self._CreateTime = params.get("CreateTime")
        self._ProductResourceId = params.get("ProductResourceId")
        self._ShareManagerUin = params.get("ShareManagerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareUnitMember(AbstractModel):
    r"""共享单元成员

    """

    def __init__(self):
        r"""
        :param _ShareMemberUin: 共享成员Uin。
        :type ShareMemberUin: int
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        """
        self._ShareMemberUin = None
        self._CreateTime = None

    @property
    def ShareMemberUin(self):
        r"""共享成员Uin。
        :rtype: int
        """
        return self._ShareMemberUin

    @ShareMemberUin.setter
    def ShareMemberUin(self, ShareMemberUin):
        self._ShareMemberUin = ShareMemberUin

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ShareMemberUin = params.get("ShareMemberUin")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareUnitResource(AbstractModel):
    r"""共享单元资源

    """

    def __init__(self):
        r"""
        :param _ResourceId: 共享资源ID。
        :type ResourceId: str
        :param _Type: 共享资源类型。
        :type Type: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _ProductResourceId: 产品资源ID。
        :type ProductResourceId: str
        :param _SharedMemberNum: 共享单元成员数。
        :type SharedMemberNum: int
        :param _SharedMemberUseNum: 使用中共享单元成员数。
        :type SharedMemberUseNum: int
        :param _ShareManagerUin: 共享管理员OwnerUin。
        :type ShareManagerUin: int
        """
        self._ResourceId = None
        self._Type = None
        self._CreateTime = None
        self._ProductResourceId = None
        self._SharedMemberNum = None
        self._SharedMemberUseNum = None
        self._ShareManagerUin = None

    @property
    def ResourceId(self):
        r"""共享资源ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Type(self):
        r"""共享资源类型。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ProductResourceId(self):
        r"""产品资源ID。
        :rtype: str
        """
        return self._ProductResourceId

    @ProductResourceId.setter
    def ProductResourceId(self, ProductResourceId):
        self._ProductResourceId = ProductResourceId

    @property
    def SharedMemberNum(self):
        r"""共享单元成员数。
        :rtype: int
        """
        return self._SharedMemberNum

    @SharedMemberNum.setter
    def SharedMemberNum(self, SharedMemberNum):
        self._SharedMemberNum = SharedMemberNum

    @property
    def SharedMemberUseNum(self):
        r"""使用中共享单元成员数。
        :rtype: int
        """
        return self._SharedMemberUseNum

    @SharedMemberUseNum.setter
    def SharedMemberUseNum(self, SharedMemberUseNum):
        self._SharedMemberUseNum = SharedMemberUseNum

    @property
    def ShareManagerUin(self):
        r"""共享管理员OwnerUin。
        :rtype: int
        """
        return self._ShareManagerUin

    @ShareManagerUin.setter
    def ShareManagerUin(self, ShareManagerUin):
        self._ShareManagerUin = ShareManagerUin


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Type = params.get("Type")
        self._CreateTime = params.get("CreateTime")
        self._ProductResourceId = params.get("ProductResourceId")
        self._SharedMemberNum = params.get("SharedMemberNum")
        self._SharedMemberUseNum = params.get("SharedMemberUseNum")
        self._ShareManagerUin = params.get("ShareManagerUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    r"""标签键值对

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
        r"""标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值
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
        


class TagComplianceDetails(AbstractModel):
    r"""标签合规信息

    """

    def __init__(self):
        r"""
        :param _ComplianceStatus: 合规状态。true-合规，false-不合规
        :type ComplianceStatus: bool
        :param _KeysWithNonCompliantValues: 值不合规的标签键列表。
        :type KeysWithNonCompliantValues: list of str
        :param _NonCompliantKeys: 键不合规的标签键列表。
        :type NonCompliantKeys: list of str
        """
        self._ComplianceStatus = None
        self._KeysWithNonCompliantValues = None
        self._NonCompliantKeys = None

    @property
    def ComplianceStatus(self):
        r"""合规状态。true-合规，false-不合规
        :rtype: bool
        """
        return self._ComplianceStatus

    @ComplianceStatus.setter
    def ComplianceStatus(self, ComplianceStatus):
        self._ComplianceStatus = ComplianceStatus

    @property
    def KeysWithNonCompliantValues(self):
        r"""值不合规的标签键列表。
        :rtype: list of str
        """
        return self._KeysWithNonCompliantValues

    @KeysWithNonCompliantValues.setter
    def KeysWithNonCompliantValues(self, KeysWithNonCompliantValues):
        self._KeysWithNonCompliantValues = KeysWithNonCompliantValues

    @property
    def NonCompliantKeys(self):
        r"""键不合规的标签键列表。
        :rtype: list of str
        """
        return self._NonCompliantKeys

    @NonCompliantKeys.setter
    def NonCompliantKeys(self, NonCompliantKeys):
        self._NonCompliantKeys = NonCompliantKeys


    def _deserialize(self, params):
        self._ComplianceStatus = params.get("ComplianceStatus")
        self._KeysWithNonCompliantValues = params.get("KeysWithNonCompliantValues")
        self._NonCompliantKeys = params.get("NonCompliantKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
    r"""标签键值对

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键。
        :type TagKey: str
        :param _TagValue: 标签值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签键。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签值。
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
        


class TaskInfo(AbstractModel):
    r"""任务状态信息。

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _RoleConfigurationId: 权限配置ID。
        :type RoleConfigurationId: str
        :param _RoleConfigurationName: 权限配置名称。
        :type RoleConfigurationName: str
        :param _TargetUin: 授权的目标成员账号的UIN
        :type TargetUin: int
        :param _TargetType: 同步的目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _PrincipalId: 用户授权的身份ID,如果是身份类型是CIC用户,则为用户ID; 如果是用户组，则为用户组ID;
        :type PrincipalId: str
        :param _PrincipalType: 用户授权的身份类型, User代表CIC用户, Group代表CIC用户组
        :type PrincipalType: str
        :param _TaskType: 任务类型。
        :type TaskType: str
        :param _Status: InProgress：任务执行中。 Success：任务执行成功。 Failed：任务执行失败。
        :type Status: str
        :param _FailureReason: 失败原因
        :type FailureReason: str
        """
        self._TaskId = None
        self._RoleConfigurationId = None
        self._RoleConfigurationName = None
        self._TargetUin = None
        self._TargetType = None
        self._PrincipalId = None
        self._PrincipalType = None
        self._TaskType = None
        self._Status = None
        self._FailureReason = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RoleConfigurationId(self):
        r"""权限配置ID。
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def RoleConfigurationName(self):
        r"""权限配置名称。
        :rtype: str
        """
        return self._RoleConfigurationName

    @RoleConfigurationName.setter
    def RoleConfigurationName(self, RoleConfigurationName):
        self._RoleConfigurationName = RoleConfigurationName

    @property
    def TargetUin(self):
        r"""授权的目标成员账号的UIN
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetType(self):
        r"""同步的目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def PrincipalId(self):
        r"""用户授权的身份ID,如果是身份类型是CIC用户,则为用户ID; 如果是用户组，则为用户组ID;
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def PrincipalType(self):
        r"""用户授权的身份类型, User代表CIC用户, Group代表CIC用户组
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def TaskType(self):
        r"""任务类型。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def Status(self):
        r"""InProgress：任务执行中。 Success：任务执行成功。 Failed：任务执行失败。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FailureReason(self):
        r"""失败原因
        :rtype: str
        """
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._RoleConfigurationName = params.get("RoleConfigurationName")
        self._TargetUin = params.get("TargetUin")
        self._TargetType = params.get("TargetType")
        self._PrincipalId = params.get("PrincipalId")
        self._PrincipalType = params.get("PrincipalType")
        self._TaskType = params.get("TaskType")
        self._Status = params.get("Status")
        self._FailureReason = params.get("FailureReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskStatus(AbstractModel):
    r"""任务状态信息。

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。取值：  InProgress：任务执行中。 Success：任务执行成功。 Failed：任务执行失败。
        :type Status: str
        :param _TaskId: 任务 ID。
        :type TaskId: str
        :param _TaskType: 任务类型。取值：
ProvisionRoleConfiguration：部署权限配置。
DeprovisionRoleConfiguration：解除权限配置部署。
CreateRoleAssignment：在成员 账号上授权。
DeleteRoleAssignment：移除 成员 账号上的授权。
        :type TaskType: str
        :param _FailureReason: 任务失败原因。
说明
只有Status为Failed，才会显示该参数。
        :type FailureReason: str
        """
        self._Status = None
        self._TaskId = None
        self._TaskType = None
        self._FailureReason = None

    @property
    def Status(self):
        r"""任务状态。取值：  InProgress：任务执行中。 Success：任务执行成功。 Failed：任务执行失败。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskId(self):
        r"""任务 ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TaskType(self):
        r"""任务类型。取值：
ProvisionRoleConfiguration：部署权限配置。
DeprovisionRoleConfiguration：解除权限配置部署。
CreateRoleAssignment：在成员 账号上授权。
DeleteRoleAssignment：移除 成员 账号上的授权。
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def FailureReason(self):
        r"""任务失败原因。
说明
只有Status为Failed，才会显示该参数。
        :rtype: str
        """
        return self._FailureReason

    @FailureReason.setter
    def FailureReason(self, FailureReason):
        self._FailureReason = FailureReason


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._TaskId = params.get("TaskId")
        self._TaskType = params.get("TaskType")
        self._FailureReason = params.get("FailureReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomPolicyForRoleConfigurationRequest(AbstractModel):
    r"""UpdateCustomPolicyForRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置 ID
        :type RoleConfigurationId: str
        :param _CustomPolicyName: 权限策略名称，长度最大为 32 个字符。
        :type CustomPolicyName: str
        :param _NewCustomPolicyDocument: 自定义策略内容。长度：最大 4096 个字符。当RolePolicyType为Inline时，该参数必须配置。关于权限策略的语法和结构，请参见权限策略语法和结构。
        :type NewCustomPolicyDocument: str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._CustomPolicyName = None
        self._NewCustomPolicyDocument = None

    @property
    def ZoneId(self):
        r"""空间 ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置 ID
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def CustomPolicyName(self):
        r"""权限策略名称，长度最大为 32 个字符。
        :rtype: str
        """
        return self._CustomPolicyName

    @CustomPolicyName.setter
    def CustomPolicyName(self, CustomPolicyName):
        self._CustomPolicyName = CustomPolicyName

    @property
    def NewCustomPolicyDocument(self):
        r"""自定义策略内容。长度：最大 4096 个字符。当RolePolicyType为Inline时，该参数必须配置。关于权限策略的语法和结构，请参见权限策略语法和结构。
        :rtype: str
        """
        return self._NewCustomPolicyDocument

    @NewCustomPolicyDocument.setter
    def NewCustomPolicyDocument(self, NewCustomPolicyDocument):
        self._NewCustomPolicyDocument = NewCustomPolicyDocument


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._CustomPolicyName = params.get("CustomPolicyName")
        self._NewCustomPolicyDocument = params.get("NewCustomPolicyDocument")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCustomPolicyForRoleConfigurationResponse(AbstractModel):
    r"""UpdateCustomPolicyForRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateGroupRequest(AbstractModel):
    r"""UpdateGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _GroupId: 用户组ID。
        :type GroupId: str
        :param _NewGroupName: 新的用户组名称。
        :type NewGroupName: str
        :param _NewDescription: 新的用户组描述。
        :type NewDescription: str
        """
        self._ZoneId = None
        self._GroupId = None
        self._NewGroupName = None
        self._NewDescription = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def GroupId(self):
        r"""用户组ID。
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def NewGroupName(self):
        r"""新的用户组名称。
        :rtype: str
        """
        return self._NewGroupName

    @NewGroupName.setter
    def NewGroupName(self, NewGroupName):
        self._NewGroupName = NewGroupName

    @property
    def NewDescription(self):
        r"""新的用户组描述。
        :rtype: str
        """
        return self._NewDescription

    @NewDescription.setter
    def NewDescription(self, NewDescription):
        self._NewDescription = NewDescription


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._GroupId = params.get("GroupId")
        self._NewGroupName = params.get("NewGroupName")
        self._NewDescription = params.get("NewDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateGroupResponse(AbstractModel):
    r"""UpdateGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupInfo: 用户组信息。
        :type GroupInfo: :class:`tencentcloud.organization.v20210331.models.GroupInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupInfo = None
        self._RequestId = None

    @property
    def GroupInfo(self):
        r"""用户组信息。
        :rtype: :class:`tencentcloud.organization.v20210331.models.GroupInfo`
        """
        return self._GroupInfo

    @GroupInfo.setter
    def GroupInfo(self, GroupInfo):
        self._GroupInfo = GroupInfo

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
        if params.get("GroupInfo") is not None:
            self._GroupInfo = GroupInfo()
            self._GroupInfo._deserialize(params.get("GroupInfo"))
        self._RequestId = params.get("RequestId")


class UpdateOrganizationIdentityRequest(AbstractModel):
    r"""UpdateOrganizationIdentity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IdentityId: 身份ID。可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :type IdentityId: int
        :param _Description: 身份描述。
        :type Description: str
        :param _IdentityPolicy: 身份策略。
        :type IdentityPolicy: list of IdentityPolicy
        """
        self._IdentityId = None
        self._Description = None
        self._IdentityPolicy = None

    @property
    def IdentityId(self):
        r"""身份ID。可以通过[ListOrganizationIdentity](https://cloud.tencent.com/document/product/850/82934)获取
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def Description(self):
        r"""身份描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def IdentityPolicy(self):
        r"""身份策略。
        :rtype: list of IdentityPolicy
        """
        return self._IdentityPolicy

    @IdentityPolicy.setter
    def IdentityPolicy(self, IdentityPolicy):
        self._IdentityPolicy = IdentityPolicy


    def _deserialize(self, params):
        self._IdentityId = params.get("IdentityId")
        self._Description = params.get("Description")
        if params.get("IdentityPolicy") is not None:
            self._IdentityPolicy = []
            for item in params.get("IdentityPolicy"):
                obj = IdentityPolicy()
                obj._deserialize(item)
                self._IdentityPolicy.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationIdentityResponse(AbstractModel):
    r"""UpdateOrganizationIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateOrganizationMemberEmailBindRequest(AbstractModel):
    r"""UpdateOrganizationMemberEmailBind请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _BindId: 绑定ID。可以通过[DescribeOrganizationMemberEmailBind](https://cloud.tencent.com/document/product/850/93332)获取
        :type BindId: int
        :param _Email: 邮箱地址。
        :type Email: str
        :param _CountryCode: 国际区号。
        :type CountryCode: str
        :param _Phone: 手机号。
        :type Phone: str
        """
        self._MemberUin = None
        self._BindId = None
        self._Email = None
        self._CountryCode = None
        self._Phone = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def BindId(self):
        r"""绑定ID。可以通过[DescribeOrganizationMemberEmailBind](https://cloud.tencent.com/document/product/850/93332)获取
        :rtype: int
        """
        return self._BindId

    @BindId.setter
    def BindId(self, BindId):
        self._BindId = BindId

    @property
    def Email(self):
        r"""邮箱地址。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def CountryCode(self):
        r"""国际区号。
        :rtype: str
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def Phone(self):
        r"""手机号。
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._BindId = params.get("BindId")
        self._Email = params.get("Email")
        self._CountryCode = params.get("CountryCode")
        self._Phone = params.get("Phone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationMemberEmailBindResponse(AbstractModel):
    r"""UpdateOrganizationMemberEmailBind返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateOrganizationMemberRequest(AbstractModel):
    r"""UpdateOrganizationMember请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUin: 成员Uin。
        :type MemberUin: int
        :param _Name: 成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :type Name: str
        :param _Remark: 备注。最大长度为40个字符
        :type Remark: str
        :param _PolicyType: 关系策略类型。PolicyType不为空，PermissionIds不能为空。取值：Financial
        :type PolicyType: str
        :param _PermissionIds: 成员财务权限ID列表。PermissionIds不为空，PolicyType不能为空。
取值：1-查看账单、2-查看余额、3-资金划拨（若需要开启资金划拨权限，请联系您的商务经理内部开通。）、4-合并出账、5-开票、6-优惠继承、7-代付费、8-成本分析、9-预算管理、10-信用额度设置（若需要开启信用额度设置权限，请联系您的商务经理内部开通。），1、2 默认必须
        :type PermissionIds: list of int non-negative
        :param _IsAllowQuit: 是否允许成员退出组织。取值：Allow-允许、Denied-不允许
        :type IsAllowQuit: str
        :param _PayUin: 代付者Uin。成员财务权限有代付费时需要，取值为成员对应主体的主体管理员Uin
        :type PayUin: str
        :param _IsModifyNickName: 是否同步组织成员名称到成员账号昵称。取值： 1-同步 0-不同步
        :type IsModifyNickName: int
        """
        self._MemberUin = None
        self._Name = None
        self._Remark = None
        self._PolicyType = None
        self._PermissionIds = None
        self._IsAllowQuit = None
        self._PayUin = None
        self._IsModifyNickName = None

    @property
    def MemberUin(self):
        r"""成员Uin。
        :rtype: int
        """
        return self._MemberUin

    @MemberUin.setter
    def MemberUin(self, MemberUin):
        self._MemberUin = MemberUin

    @property
    def Name(self):
        r"""成员名称。最大长度为25个字符，支持英文字母、数字、汉字、符号+@、&._[]-:,
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""备注。最大长度为40个字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def PolicyType(self):
        r"""关系策略类型。PolicyType不为空，PermissionIds不能为空。取值：Financial
        :rtype: str
        """
        return self._PolicyType

    @PolicyType.setter
    def PolicyType(self, PolicyType):
        self._PolicyType = PolicyType

    @property
    def PermissionIds(self):
        r"""成员财务权限ID列表。PermissionIds不为空，PolicyType不能为空。
取值：1-查看账单、2-查看余额、3-资金划拨（若需要开启资金划拨权限，请联系您的商务经理内部开通。）、4-合并出账、5-开票、6-优惠继承、7-代付费、8-成本分析、9-预算管理、10-信用额度设置（若需要开启信用额度设置权限，请联系您的商务经理内部开通。），1、2 默认必须
        :rtype: list of int non-negative
        """
        return self._PermissionIds

    @PermissionIds.setter
    def PermissionIds(self, PermissionIds):
        self._PermissionIds = PermissionIds

    @property
    def IsAllowQuit(self):
        r"""是否允许成员退出组织。取值：Allow-允许、Denied-不允许
        :rtype: str
        """
        return self._IsAllowQuit

    @IsAllowQuit.setter
    def IsAllowQuit(self, IsAllowQuit):
        self._IsAllowQuit = IsAllowQuit

    @property
    def PayUin(self):
        r"""代付者Uin。成员财务权限有代付费时需要，取值为成员对应主体的主体管理员Uin
        :rtype: str
        """
        return self._PayUin

    @PayUin.setter
    def PayUin(self, PayUin):
        self._PayUin = PayUin

    @property
    def IsModifyNickName(self):
        r"""是否同步组织成员名称到成员账号昵称。取值： 1-同步 0-不同步
        :rtype: int
        """
        return self._IsModifyNickName

    @IsModifyNickName.setter
    def IsModifyNickName(self, IsModifyNickName):
        self._IsModifyNickName = IsModifyNickName


    def _deserialize(self, params):
        self._MemberUin = params.get("MemberUin")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._PolicyType = params.get("PolicyType")
        self._PermissionIds = params.get("PermissionIds")
        self._IsAllowQuit = params.get("IsAllowQuit")
        self._PayUin = params.get("PayUin")
        self._IsModifyNickName = params.get("IsModifyNickName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationMemberResponse(AbstractModel):
    r"""UpdateOrganizationMember返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateOrganizationMembersPolicyRequest(AbstractModel):
    r"""UpdateOrganizationMembersPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MemberUins: 成员Uin列表。最多10个
        :type MemberUins: list of int
        :param _PolicyId: 成员访问策略Id。可通过DescribeOrganizationMemberPolicies获取
        :type PolicyId: int
        :param _IdentityId: 成员访问身份ID。可通过ListOrganizationIdentity获取
        :type IdentityId: int
        :param _Description: 策略描述。最大长度为128个字符
        :type Description: str
        """
        self._MemberUins = None
        self._PolicyId = None
        self._IdentityId = None
        self._Description = None

    @property
    def MemberUins(self):
        r"""成员Uin列表。最多10个
        :rtype: list of int
        """
        return self._MemberUins

    @MemberUins.setter
    def MemberUins(self, MemberUins):
        self._MemberUins = MemberUins

    @property
    def PolicyId(self):
        r"""成员访问策略Id。可通过DescribeOrganizationMemberPolicies获取
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def IdentityId(self):
        r"""成员访问身份ID。可通过ListOrganizationIdentity获取
        :rtype: int
        """
        return self._IdentityId

    @IdentityId.setter
    def IdentityId(self, IdentityId):
        self._IdentityId = IdentityId

    @property
    def Description(self):
        r"""策略描述。最大长度为128个字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._MemberUins = params.get("MemberUins")
        self._PolicyId = params.get("PolicyId")
        self._IdentityId = params.get("IdentityId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationMembersPolicyResponse(AbstractModel):
    r"""UpdateOrganizationMembersPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateOrganizationNodeRequest(AbstractModel):
    r"""UpdateOrganizationNode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NodeId: 节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :type NodeId: int
        :param _Name: 节点名称。最大长度为40个字符，支持英文字母、数字、汉字、符号+@、&._[]-
        :type Name: str
        :param _Remark: 备注。
        :type Remark: str
        """
        self._NodeId = None
        self._Name = None
        self._Remark = None

    @property
    def NodeId(self):
        r"""节点ID。可以通过[DescribeOrganizationNodes](https://cloud.tencent.com/document/product/850/82926)获取
        :rtype: int
        """
        return self._NodeId

    @NodeId.setter
    def NodeId(self, NodeId):
        self._NodeId = NodeId

    @property
    def Name(self):
        r"""节点名称。最大长度为40个字符，支持英文字母、数字、汉字、符号+@、&._[]-
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        r"""备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._NodeId = params.get("NodeId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateOrganizationNodeResponse(AbstractModel):
    r"""UpdateOrganizationNode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdatePolicyRequest(AbstractModel):
    r"""UpdatePolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyId: 需要编辑的策略ID。可以调用[ListPolicies](https://cloud.tencent.com/document/product/850/105311)获取
        :type PolicyId: int
        :param _Description: 策略描述。
        :type Description: str
        :param _Content: 策略内容。参考CAM策略语法
        :type Content: str
        :param _Name: 策略名。长度为1~128个字符，可以包含汉字、英文字母、数字和下划线（_）
        :type Name: str
        :param _Type: 策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :type Type: str
        """
        self._PolicyId = None
        self._Description = None
        self._Content = None
        self._Name = None
        self._Type = None

    @property
    def PolicyId(self):
        r"""需要编辑的策略ID。可以调用[ListPolicies](https://cloud.tencent.com/document/product/850/105311)获取
        :rtype: int
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Description(self):
        r"""策略描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        r"""策略内容。参考CAM策略语法
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Name(self):
        r"""策略名。长度为1~128个字符，可以包含汉字、英文字母、数字和下划线（_）
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""策略类型。默认值SERVICE_CONTROL_POLICY，取值范围：SERVICE_CONTROL_POLICY-服务控制策略、TAG_POLICY-标签策略
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._Description = params.get("Description")
        self._Content = params.get("Content")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePolicyResponse(AbstractModel):
    r"""UpdatePolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateRoleConfigurationRequest(AbstractModel):
    r"""UpdateRoleConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID
        :type ZoneId: str
        :param _RoleConfigurationId: 权限配置 ID
        :type RoleConfigurationId: str
        :param _NewDescription: 新的权限配置描述。  长度：最大 1024 个字符。
        :type NewDescription: str
        :param _NewSessionDuration: 新的会话持续时间。  CIC 用户使用权限配置访问集团账号目标账号时，会话最多保持的时间。  单位：秒。  取值范围：900-43200（15 分钟-12 小时）。
        :type NewSessionDuration: int
        :param _NewRelayState: 新的初始访问页面。  CIC 用户使用权限配置访问集团账号目标账号时，初始访问的页面地址。  该页面必须是腾讯云控制台页面。
        :type NewRelayState: str
        """
        self._ZoneId = None
        self._RoleConfigurationId = None
        self._NewDescription = None
        self._NewSessionDuration = None
        self._NewRelayState = None

    @property
    def ZoneId(self):
        r"""空间 ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RoleConfigurationId(self):
        r"""权限配置 ID
        :rtype: str
        """
        return self._RoleConfigurationId

    @RoleConfigurationId.setter
    def RoleConfigurationId(self, RoleConfigurationId):
        self._RoleConfigurationId = RoleConfigurationId

    @property
    def NewDescription(self):
        r"""新的权限配置描述。  长度：最大 1024 个字符。
        :rtype: str
        """
        return self._NewDescription

    @NewDescription.setter
    def NewDescription(self, NewDescription):
        self._NewDescription = NewDescription

    @property
    def NewSessionDuration(self):
        r"""新的会话持续时间。  CIC 用户使用权限配置访问集团账号目标账号时，会话最多保持的时间。  单位：秒。  取值范围：900-43200（15 分钟-12 小时）。
        :rtype: int
        """
        return self._NewSessionDuration

    @NewSessionDuration.setter
    def NewSessionDuration(self, NewSessionDuration):
        self._NewSessionDuration = NewSessionDuration

    @property
    def NewRelayState(self):
        r"""新的初始访问页面。  CIC 用户使用权限配置访问集团账号目标账号时，初始访问的页面地址。  该页面必须是腾讯云控制台页面。
        :rtype: str
        """
        return self._NewRelayState

    @NewRelayState.setter
    def NewRelayState(self, NewRelayState):
        self._NewRelayState = NewRelayState


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RoleConfigurationId = params.get("RoleConfigurationId")
        self._NewDescription = params.get("NewDescription")
        self._NewSessionDuration = params.get("NewSessionDuration")
        self._NewRelayState = params.get("NewRelayState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRoleConfigurationResponse(AbstractModel):
    r"""UpdateRoleConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleConfigurationInfo: 权限配置详情
        :type RoleConfigurationInfo: :class:`tencentcloud.organization.v20210331.models.RoleConfiguration`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RoleConfigurationInfo = None
        self._RequestId = None

    @property
    def RoleConfigurationInfo(self):
        r"""权限配置详情
        :rtype: :class:`tencentcloud.organization.v20210331.models.RoleConfiguration`
        """
        return self._RoleConfigurationInfo

    @RoleConfigurationInfo.setter
    def RoleConfigurationInfo(self, RoleConfigurationInfo):
        self._RoleConfigurationInfo = RoleConfigurationInfo

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
        if params.get("RoleConfigurationInfo") is not None:
            self._RoleConfigurationInfo = RoleConfiguration()
            self._RoleConfigurationInfo._deserialize(params.get("RoleConfigurationInfo"))
        self._RequestId = params.get("RequestId")


class UpdateSCIMCredentialStatusRequest(AbstractModel):
    r"""UpdateSCIMCredentialStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _CredentialId: SCIM密钥ID。scimcred-前缀开头，后面是12位随机数字/小写字母。
        :type CredentialId: str
        :param _NewStatus: SCIM密钥状态。Enabled：启用。 Disabled：禁用。
        :type NewStatus: str
        """
        self._ZoneId = None
        self._CredentialId = None
        self._NewStatus = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def CredentialId(self):
        r"""SCIM密钥ID。scimcred-前缀开头，后面是12位随机数字/小写字母。
        :rtype: str
        """
        return self._CredentialId

    @CredentialId.setter
    def CredentialId(self, CredentialId):
        self._CredentialId = CredentialId

    @property
    def NewStatus(self):
        r"""SCIM密钥状态。Enabled：启用。 Disabled：禁用。
        :rtype: str
        """
        return self._NewStatus

    @NewStatus.setter
    def NewStatus(self, NewStatus):
        self._NewStatus = NewStatus


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._CredentialId = params.get("CredentialId")
        self._NewStatus = params.get("NewStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSCIMCredentialStatusResponse(AbstractModel):
    r"""UpdateSCIMCredentialStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateSCIMSynchronizationStatusRequest(AbstractModel):
    r"""UpdateSCIMSynchronizationStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _SCIMSynchronizationStatus: SCIM 同步状态。Enabled：启用。Disabled：禁用。
        :type SCIMSynchronizationStatus: str
        """
        self._ZoneId = None
        self._SCIMSynchronizationStatus = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SCIMSynchronizationStatus(self):
        r"""SCIM 同步状态。Enabled：启用。Disabled：禁用。
        :rtype: str
        """
        return self._SCIMSynchronizationStatus

    @SCIMSynchronizationStatus.setter
    def SCIMSynchronizationStatus(self, SCIMSynchronizationStatus):
        self._SCIMSynchronizationStatus = SCIMSynchronizationStatus


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._SCIMSynchronizationStatus = params.get("SCIMSynchronizationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSCIMSynchronizationStatusResponse(AbstractModel):
    r"""UpdateSCIMSynchronizationStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateShareUnitRequest(AbstractModel):
    r"""UpdateShareUnit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UnitId: 共享单元ID。
        :type UnitId: str
        :param _Name: 共享单元名称。仅支持大小写字母、数字、-、以及_的组合，3-128个字符。
        :type Name: str
        :param _Description: 共享单元描述。最大128个字符。
        :type Description: str
        :param _ShareScope: 共享范围。取值：1-仅允许集团组织内共享 2-允许共享给任意账号，默认值：1
        :type ShareScope: int
        """
        self._UnitId = None
        self._Name = None
        self._Description = None
        self._ShareScope = None

    @property
    def UnitId(self):
        r"""共享单元ID。
        :rtype: str
        """
        return self._UnitId

    @UnitId.setter
    def UnitId(self, UnitId):
        self._UnitId = UnitId

    @property
    def Name(self):
        r"""共享单元名称。仅支持大小写字母、数字、-、以及_的组合，3-128个字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""共享单元描述。最大128个字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ShareScope(self):
        r"""共享范围。取值：1-仅允许集团组织内共享 2-允许共享给任意账号，默认值：1
        :rtype: int
        """
        return self._ShareScope

    @ShareScope.setter
    def ShareScope(self, ShareScope):
        self._ShareScope = ShareScope


    def _deserialize(self, params):
        self._UnitId = params.get("UnitId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ShareScope = params.get("ShareScope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateShareUnitResponse(AbstractModel):
    r"""UpdateShareUnit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateUserRequest(AbstractModel):
    r"""UpdateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _UserId: 用户 ID。
        :type UserId: str
        :param _NewFirstName: 用户的名。
        :type NewFirstName: str
        :param _NewLastName: 用户的姓。
        :type NewLastName: str
        :param _NewDisplayName: 用户的显示名称。
        :type NewDisplayName: str
        :param _NewDescription: 用户的描述。
        :type NewDescription: str
        :param _NewEmail: 用户的电子邮箱。
        :type NewEmail: str
        :param _NeedResetPassword: 是否需要重置密码
        :type NeedResetPassword: bool
        """
        self._ZoneId = None
        self._UserId = None
        self._NewFirstName = None
        self._NewLastName = None
        self._NewDisplayName = None
        self._NewDescription = None
        self._NewEmail = None
        self._NeedResetPassword = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserId(self):
        r"""用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def NewFirstName(self):
        r"""用户的名。
        :rtype: str
        """
        return self._NewFirstName

    @NewFirstName.setter
    def NewFirstName(self, NewFirstName):
        self._NewFirstName = NewFirstName

    @property
    def NewLastName(self):
        r"""用户的姓。
        :rtype: str
        """
        return self._NewLastName

    @NewLastName.setter
    def NewLastName(self, NewLastName):
        self._NewLastName = NewLastName

    @property
    def NewDisplayName(self):
        r"""用户的显示名称。
        :rtype: str
        """
        return self._NewDisplayName

    @NewDisplayName.setter
    def NewDisplayName(self, NewDisplayName):
        self._NewDisplayName = NewDisplayName

    @property
    def NewDescription(self):
        r"""用户的描述。
        :rtype: str
        """
        return self._NewDescription

    @NewDescription.setter
    def NewDescription(self, NewDescription):
        self._NewDescription = NewDescription

    @property
    def NewEmail(self):
        r"""用户的电子邮箱。
        :rtype: str
        """
        return self._NewEmail

    @NewEmail.setter
    def NewEmail(self, NewEmail):
        self._NewEmail = NewEmail

    @property
    def NeedResetPassword(self):
        r"""是否需要重置密码
        :rtype: bool
        """
        return self._NeedResetPassword

    @NeedResetPassword.setter
    def NeedResetPassword(self, NeedResetPassword):
        self._NeedResetPassword = NeedResetPassword


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserId = params.get("UserId")
        self._NewFirstName = params.get("NewFirstName")
        self._NewLastName = params.get("NewLastName")
        self._NewDisplayName = params.get("NewDisplayName")
        self._NewDescription = params.get("NewDescription")
        self._NewEmail = params.get("NewEmail")
        self._NeedResetPassword = params.get("NeedResetPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserResponse(AbstractModel):
    r"""UpdateUser返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UserInfo: 用户信息
        :type UserInfo: :class:`tencentcloud.organization.v20210331.models.UserInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UserInfo = None
        self._RequestId = None

    @property
    def UserInfo(self):
        r"""用户信息
        :rtype: :class:`tencentcloud.organization.v20210331.models.UserInfo`
        """
        return self._UserInfo

    @UserInfo.setter
    def UserInfo(self, UserInfo):
        self._UserInfo = UserInfo

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
        if params.get("UserInfo") is not None:
            self._UserInfo = UserInfo()
            self._UserInfo._deserialize(params.get("UserInfo"))
        self._RequestId = params.get("RequestId")


class UpdateUserStatusRequest(AbstractModel):
    r"""UpdateUserStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间 ID。
        :type ZoneId: str
        :param _UserId: 用户 ID。
        :type UserId: str
        :param _NewUserStatus: 用户的状态。取值：  Enabled：启用。 Disabled：禁用。
        :type NewUserStatus: str
        """
        self._ZoneId = None
        self._UserId = None
        self._NewUserStatus = None

    @property
    def ZoneId(self):
        r"""空间 ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserId(self):
        r"""用户 ID。
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def NewUserStatus(self):
        r"""用户的状态。取值：  Enabled：启用。 Disabled：禁用。
        :rtype: str
        """
        return self._NewUserStatus

    @NewUserStatus.setter
    def NewUserStatus(self, NewUserStatus):
        self._NewUserStatus = NewUserStatus


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserId = params.get("UserId")
        self._NewUserStatus = params.get("NewUserStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserStatusResponse(AbstractModel):
    r"""UpdateUserStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateUserSyncProvisioningRequest(AbstractModel):
    r"""UpdateUserSyncProvisioning请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。
        :type ZoneId: str
        :param _UserProvisioningId: 用户同步的iD
        :type UserProvisioningId: str
        :param _NewDescription: 用户同步描述。
        :type NewDescription: str
        :param _NewDuplicationStateful: 冲突策略。当CIC 用户同步到 CAM 时，如果 CAM 中存在同名用户时的处理策略。取值： KeepBoth：两者都保留。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则对CIC 用户的用户名添加后缀_cic后尝试创建该用户名的 CAM 用户。 TakeOver：替换。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则直接将已经存在的 CAM 用户替换为CIC 同步用户。 
        :type NewDuplicationStateful: str
        :param _NewDeletionStrategy: 删除策略。删除 CAM 用户同步时，对已同步的 CAM 用户的处理策略。取值： Delete：删除。删除 CAM 用户同步时，会删除从CIC 已经同步到 CAM 中的 CAM 用户。 Keep：保留。删除 RAM 用户同步时，会保留从CIC 已经同步到 CAM 中的 CAM 用户。 
        :type NewDeletionStrategy: str
        """
        self._ZoneId = None
        self._UserProvisioningId = None
        self._NewDescription = None
        self._NewDuplicationStateful = None
        self._NewDeletionStrategy = None

    @property
    def ZoneId(self):
        r"""空间ID。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def UserProvisioningId(self):
        r"""用户同步的iD
        :rtype: str
        """
        return self._UserProvisioningId

    @UserProvisioningId.setter
    def UserProvisioningId(self, UserProvisioningId):
        self._UserProvisioningId = UserProvisioningId

    @property
    def NewDescription(self):
        r"""用户同步描述。
        :rtype: str
        """
        return self._NewDescription

    @NewDescription.setter
    def NewDescription(self, NewDescription):
        self._NewDescription = NewDescription

    @property
    def NewDuplicationStateful(self):
        r"""冲突策略。当CIC 用户同步到 CAM 时，如果 CAM 中存在同名用户时的处理策略。取值： KeepBoth：两者都保留。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则对CIC 用户的用户名添加后缀_cic后尝试创建该用户名的 CAM 用户。 TakeOver：替换。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则直接将已经存在的 CAM 用户替换为CIC 同步用户。 
        :rtype: str
        """
        return self._NewDuplicationStateful

    @NewDuplicationStateful.setter
    def NewDuplicationStateful(self, NewDuplicationStateful):
        self._NewDuplicationStateful = NewDuplicationStateful

    @property
    def NewDeletionStrategy(self):
        r"""删除策略。删除 CAM 用户同步时，对已同步的 CAM 用户的处理策略。取值： Delete：删除。删除 CAM 用户同步时，会删除从CIC 已经同步到 CAM 中的 CAM 用户。 Keep：保留。删除 RAM 用户同步时，会保留从CIC 已经同步到 CAM 中的 CAM 用户。 
        :rtype: str
        """
        return self._NewDeletionStrategy

    @NewDeletionStrategy.setter
    def NewDeletionStrategy(self, NewDeletionStrategy):
        self._NewDeletionStrategy = NewDeletionStrategy


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._UserProvisioningId = params.get("UserProvisioningId")
        self._NewDescription = params.get("NewDescription")
        self._NewDuplicationStateful = params.get("NewDuplicationStateful")
        self._NewDeletionStrategy = params.get("NewDeletionStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateUserSyncProvisioningResponse(AbstractModel):
    r"""UpdateUserSyncProvisioning返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UpdateZoneRequest(AbstractModel):
    r"""UpdateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :type ZoneId: str
        :param _NewZoneName: 空间名，必须全局唯一。包含小写字母、数字和短划线（-）。不能以短划线（-）开头或结尾，且不能有两个连续的短划线（-）。长度：2~64 个字符。
        :type NewZoneName: str
        """
        self._ZoneId = None
        self._NewZoneName = None

    @property
    def ZoneId(self):
        r"""空间ID。z-前缀开头，后面是12位随机数字/小写字母
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def NewZoneName(self):
        r"""空间名，必须全局唯一。包含小写字母、数字和短划线（-）。不能以短划线（-）开头或结尾，且不能有两个连续的短划线（-）。长度：2~64 个字符。
        :rtype: str
        """
        return self._NewZoneName

    @NewZoneName.setter
    def NewZoneName(self, NewZoneName):
        self._NewZoneName = NewZoneName


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._NewZoneName = params.get("NewZoneName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateZoneResponse(AbstractModel):
    r"""UpdateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class UserInfo(AbstractModel):
    r"""用户信息

    """

    def __init__(self):
        r"""
        :param _UserName: 查询username。
        :type UserName: str
        :param _FirstName: 用户的名。
        :type FirstName: str
        :param _LastName: 用户的姓。
        :type LastName: str
        :param _DisplayName: 用户的显示名称。
        :type DisplayName: str
        :param _Description: 用户的描述。
        :type Description: str
        :param _Email: 用户的电子邮箱。目录内必须唯一。
        :type Email: str
        :param _UserStatus: 用户状态 Enabled：启用， Disabled：禁用。
        :type UserStatus: str
        :param _UserType: 用户类型  Manual：手动创建，Synchronized：外部导入。
        :type UserType: str
        :param _UserId: 用户 ID
        :type UserId: str
        :param _CreateTime: 用户的创建时间
        :type CreateTime: str
        :param _UpdateTime: 用户的修改时间
        :type UpdateTime: str
        :param _IsSelected: 是否选中
        :type IsSelected: bool
        :param _Password: 用户密码
        :type Password: str
        :param _NeedResetPassword: 下次登录是否需要重置密码， true: 需要重置密码， false：不需要重置密码
        :type NeedResetPassword: bool
        """
        self._UserName = None
        self._FirstName = None
        self._LastName = None
        self._DisplayName = None
        self._Description = None
        self._Email = None
        self._UserStatus = None
        self._UserType = None
        self._UserId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._IsSelected = None
        self._Password = None
        self._NeedResetPassword = None

    @property
    def UserName(self):
        r"""查询username。
        :rtype: str
        """
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def FirstName(self):
        r"""用户的名。
        :rtype: str
        """
        return self._FirstName

    @FirstName.setter
    def FirstName(self, FirstName):
        self._FirstName = FirstName

    @property
    def LastName(self):
        r"""用户的姓。
        :rtype: str
        """
        return self._LastName

    @LastName.setter
    def LastName(self, LastName):
        self._LastName = LastName

    @property
    def DisplayName(self):
        r"""用户的显示名称。
        :rtype: str
        """
        return self._DisplayName

    @DisplayName.setter
    def DisplayName(self, DisplayName):
        self._DisplayName = DisplayName

    @property
    def Description(self):
        r"""用户的描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Email(self):
        r"""用户的电子邮箱。目录内必须唯一。
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def UserStatus(self):
        r"""用户状态 Enabled：启用， Disabled：禁用。
        :rtype: str
        """
        return self._UserStatus

    @UserStatus.setter
    def UserStatus(self, UserStatus):
        self._UserStatus = UserStatus

    @property
    def UserType(self):
        r"""用户类型  Manual：手动创建，Synchronized：外部导入。
        :rtype: str
        """
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def UserId(self):
        r"""用户 ID
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def CreateTime(self):
        r"""用户的创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""用户的修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def IsSelected(self):
        r"""是否选中
        :rtype: bool
        """
        return self._IsSelected

    @IsSelected.setter
    def IsSelected(self, IsSelected):
        self._IsSelected = IsSelected

    @property
    def Password(self):
        r"""用户密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def NeedResetPassword(self):
        r"""下次登录是否需要重置密码， true: 需要重置密码， false：不需要重置密码
        :rtype: bool
        """
        return self._NeedResetPassword

    @NeedResetPassword.setter
    def NeedResetPassword(self, NeedResetPassword):
        self._NeedResetPassword = NeedResetPassword


    def _deserialize(self, params):
        self._UserName = params.get("UserName")
        self._FirstName = params.get("FirstName")
        self._LastName = params.get("LastName")
        self._DisplayName = params.get("DisplayName")
        self._Description = params.get("Description")
        self._Email = params.get("Email")
        self._UserStatus = params.get("UserStatus")
        self._UserType = params.get("UserType")
        self._UserId = params.get("UserId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._IsSelected = params.get("IsSelected")
        self._Password = params.get("Password")
        self._NeedResetPassword = params.get("NeedResetPassword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserProvisioning(AbstractModel):
    r"""用户同步信息

    """

    def __init__(self):
        r"""
        :param _UserProvisioningId: CAM 用户同步的状态。取值：

Enabled：CAM 用户同步已启用。
Disabled：CAM 用户同步未启用。
        :type UserProvisioningId: str
        :param _Description: 描述。
        :type Description: str
        :param _Status: CAM 用户同步的状态。取值：
Enabled：CAM 用户同步已启用。
Disabled：CAM 用户同步未启用。
        :type Status: str
        :param _PrincipalId: CAM 用户同步的身份 ID。取值：
当PrincipalType取值为Group时，该值为CIC用户组 ID（g-********）。
当PrincipalType取值为User时，该值为CIC用户 ID（u-********）。
        :type PrincipalId: str
        :param _PrincipalName: CAM 用户同步的身份名称。取值：
当PrincipalType取值为Group时，该值为CIC用户组名称。
当PrincipalType取值为User时，该值为CIC用户名称。
        :type PrincipalName: str
        :param _PrincipalType: CAM 用户同步的身份类型。取值：

User：表示该 CAM 用户同步的身份是CIC用户。
Group：表示该 CAM 用户同步的身份是CIC用户组。
        :type PrincipalType: str
        :param _TargetUin: 集团账号目标账号的UIN。
        :type TargetUin: int
        :param _TargetName: 集团账号目标账号的名称。
        :type TargetName: str
        :param _DuplicationStrategy: 冲突策略。当CIC 用户同步到 CAM 时，如果 CAM 中存在同名用户时的处理策略。取值： KeepBoth：两者都保留。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则对CIC 用户的用户名添加后缀_cic后尝试创建该用户名的 CAM 用户。 TakeOver：替换。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则直接将已经存在的 CAM 用户替换为CIC 同步用户。
        :type DuplicationStrategy: str
        :param _DeletionStrategy: 删除策略。删除 CAM 用户同步时，对已同步的 CAM 用户的处理策略。取值： Delete：删除。删除 CAM 用户同步时，会删除从CIC 已经同步到 CAM 中的 CAM 用户。 Keep：保留。删除 RAM 用户同步时，会保留从CIC 已经同步到 CAM 中的 CAM 用户。
        :type DeletionStrategy: str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        """
        self._UserProvisioningId = None
        self._Description = None
        self._Status = None
        self._PrincipalId = None
        self._PrincipalName = None
        self._PrincipalType = None
        self._TargetUin = None
        self._TargetName = None
        self._DuplicationStrategy = None
        self._DeletionStrategy = None
        self._CreateTime = None
        self._UpdateTime = None
        self._TargetType = None

    @property
    def UserProvisioningId(self):
        r"""CAM 用户同步的状态。取值：

Enabled：CAM 用户同步已启用。
Disabled：CAM 用户同步未启用。
        :rtype: str
        """
        return self._UserProvisioningId

    @UserProvisioningId.setter
    def UserProvisioningId(self, UserProvisioningId):
        self._UserProvisioningId = UserProvisioningId

    @property
    def Description(self):
        r"""描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""CAM 用户同步的状态。取值：
Enabled：CAM 用户同步已启用。
Disabled：CAM 用户同步未启用。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PrincipalId(self):
        r"""CAM 用户同步的身份 ID。取值：
当PrincipalType取值为Group时，该值为CIC用户组 ID（g-********）。
当PrincipalType取值为User时，该值为CIC用户 ID（u-********）。
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def PrincipalName(self):
        r"""CAM 用户同步的身份名称。取值：
当PrincipalType取值为Group时，该值为CIC用户组名称。
当PrincipalType取值为User时，该值为CIC用户名称。
        :rtype: str
        """
        return self._PrincipalName

    @PrincipalName.setter
    def PrincipalName(self, PrincipalName):
        self._PrincipalName = PrincipalName

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值：

User：表示该 CAM 用户同步的身份是CIC用户。
Group：表示该 CAM 用户同步的身份是CIC用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def TargetUin(self):
        r"""集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetName(self):
        r"""集团账号目标账号的名称。
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def DuplicationStrategy(self):
        r"""冲突策略。当CIC 用户同步到 CAM 时，如果 CAM 中存在同名用户时的处理策略。取值： KeepBoth：两者都保留。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则对CIC 用户的用户名添加后缀_cic后尝试创建该用户名的 CAM 用户。 TakeOver：替换。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则直接将已经存在的 CAM 用户替换为CIC 同步用户。
        :rtype: str
        """
        return self._DuplicationStrategy

    @DuplicationStrategy.setter
    def DuplicationStrategy(self, DuplicationStrategy):
        self._DuplicationStrategy = DuplicationStrategy

    @property
    def DeletionStrategy(self):
        r"""删除策略。删除 CAM 用户同步时，对已同步的 CAM 用户的处理策略。取值： Delete：删除。删除 CAM 用户同步时，会删除从CIC 已经同步到 CAM 中的 CAM 用户。 Keep：保留。删除 RAM 用户同步时，会保留从CIC 已经同步到 CAM 中的 CAM 用户。
        :rtype: str
        """
        return self._DeletionStrategy

    @DeletionStrategy.setter
    def DeletionStrategy(self, DeletionStrategy):
        self._DeletionStrategy = DeletionStrategy

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType


    def _deserialize(self, params):
        self._UserProvisioningId = params.get("UserProvisioningId")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._PrincipalId = params.get("PrincipalId")
        self._PrincipalName = params.get("PrincipalName")
        self._PrincipalType = params.get("PrincipalType")
        self._TargetUin = params.get("TargetUin")
        self._TargetName = params.get("TargetName")
        self._DuplicationStrategy = params.get("DuplicationStrategy")
        self._DeletionStrategy = params.get("DeletionStrategy")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TargetType = params.get("TargetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserProvisioningsTask(AbstractModel):
    r"""用户同步任务状态信息。

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。
        :type TaskId: str
        :param _TargetUin: 授权的集团账号目标账号的UIN
        :type TargetUin: int
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        :param _TaskType: 任务类型。StartProvisioning：用户同步，DeleteProvisioning：删除用户同步
        :type TaskType: str
        :param _TaskStatus: 任务状态：InProgress: 进行中，Failed: 失败 3:Success: 成功
        :type TaskStatus: str
        :param _UserProvisioningId: 用户同步ID。
        :type UserProvisioningId: str
        :param _PrincipalId:  CAM 用户同步的身份 ID。取值： 当PrincipalType取值为Group时，该值为CIC 用户组 ID（g-********）。 当PrincipalType取值为User时，该值为CIC 用户 ID（u-********）。
        :type PrincipalId: str
        :param _PrincipalType: CAM 用户同步的身份类型。取值： User：表示该 CAM 用户同步的身份是CIC 用户。 Group：表示该 CAM 用户同步的身份是CIC 用户组。
        :type PrincipalType: str
        :param _PrincipalName: 用户或者用户组名称。
        :type PrincipalName: str
        :param _DuplicationStrategy: 冲突策略。KeepBoth:两者都保留;TakeOver:替换
        :type DuplicationStrategy: str
        :param _DeletionStrategy: 删除策略。Delete:删除;Keep:保留
        :type DeletionStrategy: str
        """
        self._TaskId = None
        self._TargetUin = None
        self._TargetType = None
        self._TaskType = None
        self._TaskStatus = None
        self._UserProvisioningId = None
        self._PrincipalId = None
        self._PrincipalType = None
        self._PrincipalName = None
        self._DuplicationStrategy = None
        self._DeletionStrategy = None

    @property
    def TaskId(self):
        r"""任务ID。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def TargetUin(self):
        r"""授权的集团账号目标账号的UIN
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TaskType(self):
        r"""任务类型。StartProvisioning：用户同步，DeleteProvisioning：删除用户同步
        :rtype: str
        """
        return self._TaskType

    @TaskType.setter
    def TaskType(self, TaskType):
        self._TaskType = TaskType

    @property
    def TaskStatus(self):
        r"""任务状态：InProgress: 进行中，Failed: 失败 3:Success: 成功
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def UserProvisioningId(self):
        r"""用户同步ID。
        :rtype: str
        """
        return self._UserProvisioningId

    @UserProvisioningId.setter
    def UserProvisioningId(self, UserProvisioningId):
        self._UserProvisioningId = UserProvisioningId

    @property
    def PrincipalId(self):
        r""" CAM 用户同步的身份 ID。取值： 当PrincipalType取值为Group时，该值为CIC 用户组 ID（g-********）。 当PrincipalType取值为User时，该值为CIC 用户 ID（u-********）。
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值： User：表示该 CAM 用户同步的身份是CIC 用户。 Group：表示该 CAM 用户同步的身份是CIC 用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def PrincipalName(self):
        r"""用户或者用户组名称。
        :rtype: str
        """
        return self._PrincipalName

    @PrincipalName.setter
    def PrincipalName(self, PrincipalName):
        self._PrincipalName = PrincipalName

    @property
    def DuplicationStrategy(self):
        r"""冲突策略。KeepBoth:两者都保留;TakeOver:替换
        :rtype: str
        """
        return self._DuplicationStrategy

    @DuplicationStrategy.setter
    def DuplicationStrategy(self, DuplicationStrategy):
        self._DuplicationStrategy = DuplicationStrategy

    @property
    def DeletionStrategy(self):
        r"""删除策略。Delete:删除;Keep:保留
        :rtype: str
        """
        return self._DeletionStrategy

    @DeletionStrategy.setter
    def DeletionStrategy(self, DeletionStrategy):
        self._DeletionStrategy = DeletionStrategy


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._TargetUin = params.get("TargetUin")
        self._TargetType = params.get("TargetType")
        self._TaskType = params.get("TaskType")
        self._TaskStatus = params.get("TaskStatus")
        self._UserProvisioningId = params.get("UserProvisioningId")
        self._PrincipalId = params.get("PrincipalId")
        self._PrincipalType = params.get("PrincipalType")
        self._PrincipalName = params.get("PrincipalName")
        self._DuplicationStrategy = params.get("DuplicationStrategy")
        self._DeletionStrategy = params.get("DeletionStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserSyncProvisioning(AbstractModel):
    r"""CAM用户同步信息

    """

    def __init__(self):
        r"""
        :param _Description: 描述。
        :type Description: str
        :param _PrincipalId: CAM 用户同步的身份 ID。取值：
当PrincipalType取值为Group时，该值为CIC用户组 ID（g-********）。
当PrincipalType取值为User时，该值为CIC用户 ID（u-********）。
        :type PrincipalId: str
        :param _PrincipalType: CAM 用户同步的身份类型。取值：

User：表示该 CAM 用户同步的身份是CIC用户。
Group：表示该 CAM 用户同步的身份是CIC用户组。
        :type PrincipalType: str
        :param _TargetUin: 同步的集团账号目标账号的UIN。
        :type TargetUin: int
        :param _DuplicationStrategy: 冲突策略。当CIC 用户同步到 CAM 时，如果 CAM 中存在同名用户时的处理策略。取值： KeepBoth：两者都保留。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则对CIC 用户的用户名添加后缀_cic后尝试创建该用户名的 CAM 用户。 TakeOver：替换。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则直接将已经存在的 CAM 用户替换为CIC 同步用户。
        :type DuplicationStrategy: str
        :param _DeletionStrategy: 删除策略。删除 CAM 用户同步时，对已同步的 CAM 用户的处理策略。取值： Delete：删除。删除 CAM 用户同步时，会删除从CIC 已经同步到 CAM 中的 CAM 用户。 Keep：保留。删除 RAM 用户同步时，会保留从CIC 已经同步到 CAM 中的 CAM 用户。
        :type DeletionStrategy: str
        :param _TargetType: 同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :type TargetType: str
        """
        self._Description = None
        self._PrincipalId = None
        self._PrincipalType = None
        self._TargetUin = None
        self._DuplicationStrategy = None
        self._DeletionStrategy = None
        self._TargetType = None

    @property
    def Description(self):
        r"""描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PrincipalId(self):
        r"""CAM 用户同步的身份 ID。取值：
当PrincipalType取值为Group时，该值为CIC用户组 ID（g-********）。
当PrincipalType取值为User时，该值为CIC用户 ID（u-********）。
        :rtype: str
        """
        return self._PrincipalId

    @PrincipalId.setter
    def PrincipalId(self, PrincipalId):
        self._PrincipalId = PrincipalId

    @property
    def PrincipalType(self):
        r"""CAM 用户同步的身份类型。取值：

User：表示该 CAM 用户同步的身份是CIC用户。
Group：表示该 CAM 用户同步的身份是CIC用户组。
        :rtype: str
        """
        return self._PrincipalType

    @PrincipalType.setter
    def PrincipalType(self, PrincipalType):
        self._PrincipalType = PrincipalType

    @property
    def TargetUin(self):
        r"""同步的集团账号目标账号的UIN。
        :rtype: int
        """
        return self._TargetUin

    @TargetUin.setter
    def TargetUin(self, TargetUin):
        self._TargetUin = TargetUin

    @property
    def DuplicationStrategy(self):
        r"""冲突策略。当CIC 用户同步到 CAM 时，如果 CAM 中存在同名用户时的处理策略。取值： KeepBoth：两者都保留。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则对CIC 用户的用户名添加后缀_cic后尝试创建该用户名的 CAM 用户。 TakeOver：替换。当CIC 用户被同步到 CAM 时，如果 CAM 已经存在同名用户，则直接将已经存在的 CAM 用户替换为CIC 同步用户。
        :rtype: str
        """
        return self._DuplicationStrategy

    @DuplicationStrategy.setter
    def DuplicationStrategy(self, DuplicationStrategy):
        self._DuplicationStrategy = DuplicationStrategy

    @property
    def DeletionStrategy(self):
        r"""删除策略。删除 CAM 用户同步时，对已同步的 CAM 用户的处理策略。取值： Delete：删除。删除 CAM 用户同步时，会删除从CIC 已经同步到 CAM 中的 CAM 用户。 Keep：保留。删除 RAM 用户同步时，会保留从CIC 已经同步到 CAM 中的 CAM 用户。
        :rtype: str
        """
        return self._DeletionStrategy

    @DeletionStrategy.setter
    def DeletionStrategy(self, DeletionStrategy):
        self._DeletionStrategy = DeletionStrategy

    @property
    def TargetType(self):
        r"""同步的集团账号目标账号的类型，ManagerUin管理账号;MemberUin成员账号
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._PrincipalId = params.get("PrincipalId")
        self._PrincipalType = params.get("PrincipalType")
        self._TargetUin = params.get("TargetUin")
        self._DuplicationStrategy = params.get("DuplicationStrategy")
        self._DeletionStrategy = params.get("DeletionStrategy")
        self._TargetType = params.get("TargetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneStatistics(AbstractModel):
    r"""CIC的空间统计

    """

    def __init__(self):
        r"""
        :param _UserQuota: 用户配额。
        :type UserQuota: int
        :param _GroupQuota: 用户组配额。
        :type GroupQuota: int
        :param _RoleConfigurationQuota: 权限配置配额。
        :type RoleConfigurationQuota: int
        :param _SystemPolicyPerRoleConfigurationQuota: 权限配置绑定的系统策略配额。
        :type SystemPolicyPerRoleConfigurationQuota: int
        :param _UserCount: 用户数。
        :type UserCount: int
        :param _GroupCount: 用户组数。
        :type GroupCount: int
        :param _RoleConfigurationCount: 权限配置数
        :type RoleConfigurationCount: int
        :param _UserProvisioningCount: 同步用户数。
        :type UserProvisioningCount: int
        :param _RoleConfigurationSyncCount: 同步角色数。
        :type RoleConfigurationSyncCount: int
        """
        self._UserQuota = None
        self._GroupQuota = None
        self._RoleConfigurationQuota = None
        self._SystemPolicyPerRoleConfigurationQuota = None
        self._UserCount = None
        self._GroupCount = None
        self._RoleConfigurationCount = None
        self._UserProvisioningCount = None
        self._RoleConfigurationSyncCount = None

    @property
    def UserQuota(self):
        r"""用户配额。
        :rtype: int
        """
        return self._UserQuota

    @UserQuota.setter
    def UserQuota(self, UserQuota):
        self._UserQuota = UserQuota

    @property
    def GroupQuota(self):
        r"""用户组配额。
        :rtype: int
        """
        return self._GroupQuota

    @GroupQuota.setter
    def GroupQuota(self, GroupQuota):
        self._GroupQuota = GroupQuota

    @property
    def RoleConfigurationQuota(self):
        r"""权限配置配额。
        :rtype: int
        """
        return self._RoleConfigurationQuota

    @RoleConfigurationQuota.setter
    def RoleConfigurationQuota(self, RoleConfigurationQuota):
        self._RoleConfigurationQuota = RoleConfigurationQuota

    @property
    def SystemPolicyPerRoleConfigurationQuota(self):
        r"""权限配置绑定的系统策略配额。
        :rtype: int
        """
        return self._SystemPolicyPerRoleConfigurationQuota

    @SystemPolicyPerRoleConfigurationQuota.setter
    def SystemPolicyPerRoleConfigurationQuota(self, SystemPolicyPerRoleConfigurationQuota):
        self._SystemPolicyPerRoleConfigurationQuota = SystemPolicyPerRoleConfigurationQuota

    @property
    def UserCount(self):
        r"""用户数。
        :rtype: int
        """
        return self._UserCount

    @UserCount.setter
    def UserCount(self, UserCount):
        self._UserCount = UserCount

    @property
    def GroupCount(self):
        r"""用户组数。
        :rtype: int
        """
        return self._GroupCount

    @GroupCount.setter
    def GroupCount(self, GroupCount):
        self._GroupCount = GroupCount

    @property
    def RoleConfigurationCount(self):
        r"""权限配置数
        :rtype: int
        """
        return self._RoleConfigurationCount

    @RoleConfigurationCount.setter
    def RoleConfigurationCount(self, RoleConfigurationCount):
        self._RoleConfigurationCount = RoleConfigurationCount

    @property
    def UserProvisioningCount(self):
        r"""同步用户数。
        :rtype: int
        """
        return self._UserProvisioningCount

    @UserProvisioningCount.setter
    def UserProvisioningCount(self, UserProvisioningCount):
        self._UserProvisioningCount = UserProvisioningCount

    @property
    def RoleConfigurationSyncCount(self):
        r"""同步角色数。
        :rtype: int
        """
        return self._RoleConfigurationSyncCount

    @RoleConfigurationSyncCount.setter
    def RoleConfigurationSyncCount(self, RoleConfigurationSyncCount):
        self._RoleConfigurationSyncCount = RoleConfigurationSyncCount


    def _deserialize(self, params):
        self._UserQuota = params.get("UserQuota")
        self._GroupQuota = params.get("GroupQuota")
        self._RoleConfigurationQuota = params.get("RoleConfigurationQuota")
        self._SystemPolicyPerRoleConfigurationQuota = params.get("SystemPolicyPerRoleConfigurationQuota")
        self._UserCount = params.get("UserCount")
        self._GroupCount = params.get("GroupCount")
        self._RoleConfigurationCount = params.get("RoleConfigurationCount")
        self._UserProvisioningCount = params.get("UserProvisioningCount")
        self._RoleConfigurationSyncCount = params.get("RoleConfigurationSyncCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        