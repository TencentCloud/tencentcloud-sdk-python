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


class AgentSpaceDTO(AbstractModel):
    """云服务器创建工作空间 DTO

    """

    def __init__(self):
        r"""
        :param _Name: 工作空间名称
        :type Name: str
        :param _ImageId: 镜像id
        :type ImageId: int
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _RemoteUser: 云服务器登录名称
        :type RemoteUser: str
        :param _RemoteHost: 云服务器登录地址
        :type RemoteHost: str
        :param _RemotePort: 云服务器登录端口
        :type RemotePort: str
        :param _WorkspaceType: 工作空间类型
        :type WorkspaceType: str
        :param _WorkspaceVersion: 工作空间版本
        :type WorkspaceVersion: int
        :param _WorkspaceResourceDTO: 工作空间资源结构
        :type WorkspaceResourceDTO: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceResourceDTO`
        :param _Description: 描述
        :type Description: str
        """
        self._Name = None
        self._ImageId = None
        self._ImageName = None
        self._RemoteUser = None
        self._RemoteHost = None
        self._RemotePort = None
        self._WorkspaceType = None
        self._WorkspaceVersion = None
        self._WorkspaceResourceDTO = None
        self._Description = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def RemoteUser(self):
        return self._RemoteUser

    @RemoteUser.setter
    def RemoteUser(self, RemoteUser):
        self._RemoteUser = RemoteUser

    @property
    def RemoteHost(self):
        return self._RemoteHost

    @RemoteHost.setter
    def RemoteHost(self, RemoteHost):
        self._RemoteHost = RemoteHost

    @property
    def RemotePort(self):
        return self._RemotePort

    @RemotePort.setter
    def RemotePort(self, RemotePort):
        self._RemotePort = RemotePort

    @property
    def WorkspaceType(self):
        return self._WorkspaceType

    @WorkspaceType.setter
    def WorkspaceType(self, WorkspaceType):
        self._WorkspaceType = WorkspaceType

    @property
    def WorkspaceVersion(self):
        return self._WorkspaceVersion

    @WorkspaceVersion.setter
    def WorkspaceVersion(self, WorkspaceVersion):
        self._WorkspaceVersion = WorkspaceVersion

    @property
    def WorkspaceResourceDTO(self):
        return self._WorkspaceResourceDTO

    @WorkspaceResourceDTO.setter
    def WorkspaceResourceDTO(self, WorkspaceResourceDTO):
        self._WorkspaceResourceDTO = WorkspaceResourceDTO

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._RemoteUser = params.get("RemoteUser")
        self._RemoteHost = params.get("RemoteHost")
        self._RemotePort = params.get("RemotePort")
        self._WorkspaceType = params.get("WorkspaceType")
        self._WorkspaceVersion = params.get("WorkspaceVersion")
        if params.get("WorkspaceResourceDTO") is not None:
            self._WorkspaceResourceDTO = WorkspaceResourceDTO()
            self._WorkspaceResourceDTO._deserialize(params.get("WorkspaceResourceDTO"))
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomizeTemplatesRequest(AbstractModel):
    """CreateCustomizeTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _UserDefinedTemplateParams: 无
        :type UserDefinedTemplateParams: :class:`tencentcloud.cloudstudio.v20210524.models.UserDefinedTemplateParams`
        """
        self._CloudStudioSessionTeam = None
        self._UserDefinedTemplateParams = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def UserDefinedTemplateParams(self):
        return self._UserDefinedTemplateParams

    @UserDefinedTemplateParams.setter
    def UserDefinedTemplateParams(self, UserDefinedTemplateParams):
        self._UserDefinedTemplateParams = UserDefinedTemplateParams


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        if params.get("UserDefinedTemplateParams") is not None:
            self._UserDefinedTemplateParams = UserDefinedTemplateParams()
            self._UserDefinedTemplateParams._deserialize(params.get("UserDefinedTemplateParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomizeTemplatesResponse(AbstractModel):
    """CreateCustomizeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkspaceByAgentRequest(AbstractModel):
    """CreateWorkspaceByAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 无
        :type CloudStudioSessionTeam: str
        :param _AgentSpaceDTO: 无
        :type AgentSpaceDTO: :class:`tencentcloud.cloudstudio.v20210524.models.AgentSpaceDTO`
        """
        self._CloudStudioSessionTeam = None
        self._AgentSpaceDTO = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def AgentSpaceDTO(self):
        return self._AgentSpaceDTO

    @AgentSpaceDTO.setter
    def AgentSpaceDTO(self, AgentSpaceDTO):
        self._AgentSpaceDTO = AgentSpaceDTO


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        if params.get("AgentSpaceDTO") is not None:
            self._AgentSpaceDTO = AgentSpaceDTO()
            self._AgentSpaceDTO._deserialize(params.get("AgentSpaceDTO"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceByAgentResponse(AbstractModel):
    """CreateWorkspaceByAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceInfoDTO`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceInfoDTO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkspaceByTemplateRequest(AbstractModel):
    """CreateWorkspaceByTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _TemplateId: 模板ID
        :type TemplateId: int
        :param _Name: 工作空间名称
        :type Name: str
        """
        self._CloudStudioSessionTeam = None
        self._TemplateId = None
        self._Name = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._TemplateId = params.get("TemplateId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceByTemplateResponse(AbstractModel):
    """CreateWorkspaceByTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 创建工作空间返回的信息
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkspaceByVersionControlRequest(AbstractModel):
    """CreateWorkspaceByVersionControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceDTO: 工作空间结构
        :type WorkspaceDTO: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceDTO`
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        """
        self._WorkspaceDTO = None
        self._CloudStudioSessionTeam = None

    @property
    def WorkspaceDTO(self):
        return self._WorkspaceDTO

    @WorkspaceDTO.setter
    def WorkspaceDTO(self, WorkspaceDTO):
        self._WorkspaceDTO = WorkspaceDTO

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam


    def _deserialize(self, params):
        if params.get("WorkspaceDTO") is not None:
            self._WorkspaceDTO = WorkspaceDTO()
            self._WorkspaceDTO._deserialize(params.get("WorkspaceDTO"))
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceByVersionControlResponse(AbstractModel):
    """CreateWorkspaceByVersionControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceInfoDTO`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceInfoDTO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CreateWorkspaceTemporaryTokenRequest(AbstractModel):
    """CreateWorkspaceTemporaryToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceTokenDTO: 创建工作空间凭证 DTO
        :type WorkspaceTokenDTO: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTokenDTO`
        """
        self._WorkspaceTokenDTO = None

    @property
    def WorkspaceTokenDTO(self):
        return self._WorkspaceTokenDTO

    @WorkspaceTokenDTO.setter
    def WorkspaceTokenDTO(self, WorkspaceTokenDTO):
        self._WorkspaceTokenDTO = WorkspaceTokenDTO


    def _deserialize(self, params):
        if params.get("WorkspaceTokenDTO") is not None:
            self._WorkspaceTokenDTO = WorkspaceTokenDTO()
            self._WorkspaceTokenDTO._deserialize(params.get("WorkspaceTokenDTO"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceTemporaryTokenResponse(AbstractModel):
    """CreateWorkspaceTemporaryToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 工作空间临时访问 token 信息
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTokenInfoV0`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceTokenInfoV0()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class CustomizeTemplatesPresetsInfo(AbstractModel):
    """模板的预置参数

    """

    def __init__(self):
        r"""
        :param _Tags: 模板tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _Icons: 模板图标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Icons: list of str
        :param _Templates: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Templates: :class:`tencentcloud.cloudstudio.v20210524.models.UserDefinedTemplateParams`
        """
        self._Tags = None
        self._Icons = None
        self._Templates = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Icons(self):
        return self._Icons

    @Icons.setter
    def Icons(self, Icons):
        self._Icons = Icons

    @property
    def Templates(self):
        return self._Templates

    @Templates.setter
    def Templates(self, Templates):
        self._Templates = Templates


    def _deserialize(self, params):
        self._Tags = params.get("Tags")
        self._Icons = params.get("Icons")
        if params.get("Templates") is not None:
            self._Templates = UserDefinedTemplateParams()
            self._Templates._deserialize(params.get("Templates"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizeTemplatesByIdRequest(AbstractModel):
    """DeleteCustomizeTemplatesById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _Id: 模板ID
        :type Id: int
        """
        self._CloudStudioSessionTeam = None
        self._Id = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizeTemplatesByIdResponse(AbstractModel):
    """DeleteCustomizeTemplatesById返回参数结构体

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


class DescribeCustomizeTemplatesByIdRequest(AbstractModel):
    """DescribeCustomizeTemplatesById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _Id: 模板ID
        :type Id: int
        """
        self._CloudStudioSessionTeam = None
        self._Id = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizeTemplatesByIdResponse(AbstractModel):
    """DescribeCustomizeTemplatesById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCustomizeTemplatesPresetsRequest(AbstractModel):
    """DescribeCustomizeTemplatesPresets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _SpaceKey: 空间标识
        :type SpaceKey: str
        """
        self._CloudStudioSessionTeam = None
        self._SpaceKey = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizeTemplatesPresetsResponse(AbstractModel):
    """DescribeCustomizeTemplatesPresets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.CustomizeTemplatesPresetsInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = CustomizeTemplatesPresetsInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeCustomizeTemplatesRequest(AbstractModel):
    """DescribeCustomizeTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        """
        self._CloudStudioSessionTeam = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizeTemplatesResponse(AbstractModel):
    """DescribeCustomizeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of WorkspaceTemplateInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WorkspaceTemplateInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceEnvListRequest(AbstractModel):
    """DescribeWorkspaceEnvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        """
        self._CloudStudioSessionTeam = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceEnvListResponse(AbstractModel):
    """DescribeWorkspaceEnvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ImageUserDTO
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ImageUserDTO()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceIsReadyRequest(AbstractModel):
    """DescribeWorkspaceIsReady请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 工作空间 spaceKey
        :type SpaceKey: str
        """
        self._SpaceKey = None

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceIsReadyResponse(AbstractModel):
    """DescribeWorkspaceIsReady返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 工作空间是否就绪
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceNameExistRequest(AbstractModel):
    """DescribeWorkspaceNameExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _Name: 工作空间名称
        :type Name: str
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        """
        self._CloudStudioSessionTeam = None
        self._Name = None
        self._WorkspaceId = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def WorkspaceId(self):
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._Name = params.get("Name")
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceNameExistResponse(AbstractModel):
    """DescribeWorkspaceNameExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 工作空间信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceInfoDTO`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceInfoDTO()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceStatusListRequest(AbstractModel):
    """DescribeWorkspaceStatusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: xxx
        :type CloudStudioSessionTeam: str
        """
        self._CloudStudioSessionTeam = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceStatusListResponse(AbstractModel):
    """DescribeWorkspaceStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of WorkspaceStatusInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WorkspaceStatusInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWorkspaceStatusRequest(AbstractModel):
    """DescribeWorkspaceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _SpaceKey: 空间标识
        :type SpaceKey: str
        """
        self._CloudStudioSessionTeam = None
        self._SpaceKey = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceStatusResponse(AbstractModel):
    """DescribeWorkspaceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceStatusInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceStatusInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ImageUserDTO(AbstractModel):
    """可用镜像模板列表

    """

    def __init__(self):
        r"""
        :param _Id: 镜像模板ID
        :type Id: str
        :param _Name: 镜像模板名称
        :type Name: str
        :param _Tag: Tag时间
        :type Tag: str
        :param _Description: 描述
        :type Description: str
        :param _DescriptionCN: 中文描述
        :type DescriptionCN: str
        :param _IconUrl: 图标地址
        :type IconUrl: str
        :param _Author: 创建人
        :type Author: str
        :param _Visible: 访问状态
        :type Visible: str
        :param _WorkspaceVersion: 版本
        :type WorkspaceVersion: int
        :param _Sort: 分类
        :type Sort: int
        """
        self._Id = None
        self._Name = None
        self._Tag = None
        self._Description = None
        self._DescriptionCN = None
        self._IconUrl = None
        self._Author = None
        self._Visible = None
        self._WorkspaceVersion = None
        self._Sort = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DescriptionCN(self):
        return self._DescriptionCN

    @DescriptionCN.setter
    def DescriptionCN(self, DescriptionCN):
        self._DescriptionCN = DescriptionCN

    @property
    def IconUrl(self):
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def Visible(self):
        return self._Visible

    @Visible.setter
    def Visible(self, Visible):
        self._Visible = Visible

    @property
    def WorkspaceVersion(self):
        return self._WorkspaceVersion

    @WorkspaceVersion.setter
    def WorkspaceVersion(self, WorkspaceVersion):
        self._WorkspaceVersion = WorkspaceVersion

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._Tag = params.get("Tag")
        self._Description = params.get("Description")
        self._DescriptionCN = params.get("DescriptionCN")
        self._IconUrl = params.get("IconUrl")
        self._Author = params.get("Author")
        self._Visible = params.get("Visible")
        self._WorkspaceVersion = params.get("WorkspaceVersion")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizeTemplateVersionControlRequest(AbstractModel):
    """ModifyCustomizeTemplateVersionControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _TemplateId: 模板ID
        :type TemplateId: int
        :param _Url: 仓库地址
        :type Url: str
        :param _Ref: 代码仓库分支/标签
        :type Ref: str
        :param _RefType: 代码仓库 ref 类型
        :type RefType: str
        """
        self._CloudStudioSessionTeam = None
        self._TemplateId = None
        self._Url = None
        self._Ref = None
        self._RefType = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Ref(self):
        return self._Ref

    @Ref.setter
    def Ref(self, Ref):
        self._Ref = Ref

    @property
    def RefType(self):
        return self._RefType

    @RefType.setter
    def RefType(self, RefType):
        self._RefType = RefType


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._TemplateId = params.get("TemplateId")
        self._Url = params.get("Url")
        self._Ref = params.get("Ref")
        self._RefType = params.get("RefType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizeTemplateVersionControlResponse(AbstractModel):
    """ModifyCustomizeTemplateVersionControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyCustomizeTemplatesFullByIdRequest(AbstractModel):
    """ModifyCustomizeTemplatesFullById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _Id: 模板ID
        :type Id: int
        :param _UserDefinedTemplateParams: 自定义模板参数
        :type UserDefinedTemplateParams: :class:`tencentcloud.cloudstudio.v20210524.models.UserDefinedTemplateParams`
        """
        self._CloudStudioSessionTeam = None
        self._Id = None
        self._UserDefinedTemplateParams = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UserDefinedTemplateParams(self):
        return self._UserDefinedTemplateParams

    @UserDefinedTemplateParams.setter
    def UserDefinedTemplateParams(self, UserDefinedTemplateParams):
        self._UserDefinedTemplateParams = UserDefinedTemplateParams


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._Id = params.get("Id")
        if params.get("UserDefinedTemplateParams") is not None:
            self._UserDefinedTemplateParams = UserDefinedTemplateParams()
            self._UserDefinedTemplateParams._deserialize(params.get("UserDefinedTemplateParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizeTemplatesFullByIdResponse(AbstractModel):
    """ModifyCustomizeTemplatesFullById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 自定义模板返回值
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyCustomizeTemplatesPartByIdRequest(AbstractModel):
    """ModifyCustomizeTemplatesPartById请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _Id: 模板ID
        :type Id: int
        :param _UserDefinedTemplatePatchedParams: 自定义模板Patched参数
        :type UserDefinedTemplatePatchedParams: :class:`tencentcloud.cloudstudio.v20210524.models.UserDefinedTemplatePatchedParams`
        """
        self._CloudStudioSessionTeam = None
        self._Id = None
        self._UserDefinedTemplatePatchedParams = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def UserDefinedTemplatePatchedParams(self):
        return self._UserDefinedTemplatePatchedParams

    @UserDefinedTemplatePatchedParams.setter
    def UserDefinedTemplatePatchedParams(self, UserDefinedTemplatePatchedParams):
        self._UserDefinedTemplatePatchedParams = UserDefinedTemplatePatchedParams


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._Id = params.get("Id")
        if params.get("UserDefinedTemplatePatchedParams") is not None:
            self._UserDefinedTemplatePatchedParams = UserDefinedTemplatePatchedParams()
            self._UserDefinedTemplatePatchedParams._deserialize(params.get("UserDefinedTemplatePatchedParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizeTemplatesPartByIdResponse(AbstractModel):
    """ModifyCustomizeTemplatesPartById返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 自定义模板返回值
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = WorkspaceTemplateInfo()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class ModifyWorkspaceAttributesRequest(AbstractModel):
    """ModifyWorkspaceAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _WorkspaceId: 工作空间ID
        :type WorkspaceId: int
        :param _Name: 工作空间名称
        :type Name: str
        :param _Description: 工作空间描述
        :type Description: str
        :param _PriceId: xxx
        :type PriceId: int
        """
        self._CloudStudioSessionTeam = None
        self._WorkspaceId = None
        self._Name = None
        self._Description = None
        self._PriceId = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def WorkspaceId(self):
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PriceId(self):
        return self._PriceId

    @PriceId.setter
    def PriceId(self, PriceId):
        self._PriceId = PriceId


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._WorkspaceId = params.get("WorkspaceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._PriceId = params.get("PriceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkspaceAttributesResponse(AbstractModel):
    """ModifyWorkspaceAttributes返回参数结构体

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


class RecoverWorkspaceRequest(AbstractModel):
    """RecoverWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 无
        :type CloudStudioSessionTeam: str
        :param _SpaceKey: 无
        :type SpaceKey: str
        """
        self._CloudStudioSessionTeam = None
        self._SpaceKey = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverWorkspaceResponse(AbstractModel):
    """RecoverWorkspace返回参数结构体

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


class RemoveWorkspaceRequest(AbstractModel):
    """RemoveWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CloudStudioSessionTeam: 无
        :type CloudStudioSessionTeam: str
        :param _SpaceKey: 无
        :type SpaceKey: str
        :param _Force: 是否强制，true或者false
        :type Force: bool
        """
        self._CloudStudioSessionTeam = None
        self._SpaceKey = None
        self._Force = None

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._SpaceKey = params.get("SpaceKey")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveWorkspaceResponse(AbstractModel):
    """RemoveWorkspace返回参数结构体

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


class RunWorkspaceRequest(AbstractModel):
    """RunWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 空间标识
        :type SpaceKey: str
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        """
        self._SpaceKey = None
        self._CloudStudioSessionTeam = None

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkspaceResponse(AbstractModel):
    """RunWorkspace返回参数结构体

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


class StopWorkspaceRequest(AbstractModel):
    """StopWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 空间标识
        :type SpaceKey: str
        :param _CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param _Force: 是否强制终止，true或者false
        :type Force: str
        """
        self._SpaceKey = None
        self._CloudStudioSessionTeam = None
        self._Force = None

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def CloudStudioSessionTeam(self):
        return self._CloudStudioSessionTeam

    @CloudStudioSessionTeam.setter
    def CloudStudioSessionTeam(self, CloudStudioSessionTeam):
        self._CloudStudioSessionTeam = CloudStudioSessionTeam

    @property
    def Force(self):
        return self._Force

    @Force.setter
    def Force(self, Force):
        self._Force = Force


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        self._CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self._Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWorkspaceResponse(AbstractModel):
    """StopWorkspace返回参数结构体

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


class UserDefinedTemplateParams(AbstractModel):
    """用户自定义模板参数

    """

    def __init__(self):
        r"""
        :param _Name: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Icon: 模板图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param _Tags: 模板标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _Source: 模板来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _Description: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _VersionControlType: 模板仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlType: str
        :param _VersionControlUrl: 模板地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlUrl: str
        """
        self._Name = None
        self._Icon = None
        self._Tags = None
        self._Source = None
        self._Description = None
        self._VersionControlType = None
        self._VersionControlUrl = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VersionControlType(self):
        return self._VersionControlType

    @VersionControlType.setter
    def VersionControlType(self, VersionControlType):
        self._VersionControlType = VersionControlType

    @property
    def VersionControlUrl(self):
        return self._VersionControlUrl

    @VersionControlUrl.setter
    def VersionControlUrl(self, VersionControlUrl):
        self._VersionControlUrl = VersionControlUrl


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Icon = params.get("Icon")
        self._Tags = params.get("Tags")
        self._Source = params.get("Source")
        self._Description = params.get("Description")
        self._VersionControlType = params.get("VersionControlType")
        self._VersionControlUrl = params.get("VersionControlUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefinedTemplatePatchedParams(AbstractModel):
    """用户自定义模板Patched参数

    """

    def __init__(self):
        r"""
        :param _Source: 模板来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _Name: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Icon: 模板图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param _Description: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Tags: 模板标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        """
        self._Source = None
        self._Name = None
        self._Icon = None
        self._Description = None
        self._Tags = None

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

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
        self._Source = params.get("Source")
        self._Name = params.get("Name")
        self._Icon = params.get("Icon")
        self._Description = params.get("Description")
        self._Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfoRsp(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param _Id: 用户ID
        :type Id: int
        :param _AuthenticationUserInfo: 用户验证信息
        :type AuthenticationUserInfo: :class:`tencentcloud.cloudstudio.v20210524.models.UserSubInfo`
        :param _Avatar: 头像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param _Features: 介绍
注意：此字段可能返回 null，表示取不到有效值。
        :type Features: str
        :param _PreviewStatus: 状况
        :type PreviewStatus: int
        """
        self._Id = None
        self._AuthenticationUserInfo = None
        self._Avatar = None
        self._Features = None
        self._PreviewStatus = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AuthenticationUserInfo(self):
        return self._AuthenticationUserInfo

    @AuthenticationUserInfo.setter
    def AuthenticationUserInfo(self, AuthenticationUserInfo):
        self._AuthenticationUserInfo = AuthenticationUserInfo

    @property
    def Avatar(self):
        return self._Avatar

    @Avatar.setter
    def Avatar(self, Avatar):
        self._Avatar = Avatar

    @property
    def Features(self):
        return self._Features

    @Features.setter
    def Features(self, Features):
        self._Features = Features

    @property
    def PreviewStatus(self):
        return self._PreviewStatus

    @PreviewStatus.setter
    def PreviewStatus(self, PreviewStatus):
        self._PreviewStatus = PreviewStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        if params.get("AuthenticationUserInfo") is not None:
            self._AuthenticationUserInfo = UserSubInfo()
            self._AuthenticationUserInfo._deserialize(params.get("AuthenticationUserInfo"))
        self._Avatar = params.get("Avatar")
        self._Features = params.get("Features")
        self._PreviewStatus = params.get("PreviewStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserSubInfo(AbstractModel):
    """用户验证信息

    """

    def __init__(self):
        r"""
        :param _Team: 团队名称
        :type Team: str
        :param _UserName: 用户名
        :type UserName: str
        :param _NickName: 昵称
        :type NickName: str
        :param _IsAdmin: 是否为管理员
        :type IsAdmin: bool
        :param _IsTrial: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTrial: bool
        """
        self._Team = None
        self._UserName = None
        self._NickName = None
        self._IsAdmin = None
        self._IsTrial = None

    @property
    def Team(self):
        return self._Team

    @Team.setter
    def Team(self, Team):
        self._Team = Team

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def NickName(self):
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def IsAdmin(self):
        return self._IsAdmin

    @IsAdmin.setter
    def IsAdmin(self, IsAdmin):
        self._IsAdmin = IsAdmin

    @property
    def IsTrial(self):
        return self._IsTrial

    @IsTrial.setter
    def IsTrial(self, IsTrial):
        self._IsTrial = IsTrial


    def _deserialize(self, params):
        self._Team = params.get("Team")
        self._UserName = params.get("UserName")
        self._NickName = params.get("NickName")
        self._IsAdmin = params.get("IsAdmin")
        self._IsTrial = params.get("IsTrial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceDTO(AbstractModel):
    """工作空间结构

    """

    def __init__(self):
        r"""
        :param _Name: 工作空间名称
        :type Name: str
        :param _VersionControlType: 代码来源类型
        :type VersionControlType: str
        :param _ImageId: 镜像id
        :type ImageId: int
        :param _ImageName: 镜像名称
        :type ImageName: str
        :param _Description: 描述
        :type Description: str
        :param _WorkspaceVersion: 工作空间版本
        :type WorkspaceVersion: int
        :param _WorkspaceResourceDTO: 工作空间资源结构
        :type WorkspaceResourceDTO: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceResourceDTO`
        :param _VersionControlUrl: 代码仓库地址
        :type VersionControlUrl: str
        :param _VersionControlRef: 代码Ref是分支还是标签
        :type VersionControlRef: str
        :param _VersionControlRefType: 代码Ref地址
        :type VersionControlRefType: str
        :param _SnapshotUid: 快照Uid
        :type SnapshotUid: str
        :param _TemplateId: 模板id
        :type TemplateId: int
        :param _PriceId: 价格id
        :type PriceId: int
        :param _InitializeStatus: 初始化状态
        :type InitializeStatus: int
        :param _VersionControlDesc: 描述
        :type VersionControlDesc: str
        """
        self._Name = None
        self._VersionControlType = None
        self._ImageId = None
        self._ImageName = None
        self._Description = None
        self._WorkspaceVersion = None
        self._WorkspaceResourceDTO = None
        self._VersionControlUrl = None
        self._VersionControlRef = None
        self._VersionControlRefType = None
        self._SnapshotUid = None
        self._TemplateId = None
        self._PriceId = None
        self._InitializeStatus = None
        self._VersionControlDesc = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VersionControlType(self):
        return self._VersionControlType

    @VersionControlType.setter
    def VersionControlType(self, VersionControlType):
        self._VersionControlType = VersionControlType

    @property
    def ImageId(self):
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId

    @property
    def ImageName(self):
        return self._ImageName

    @ImageName.setter
    def ImageName(self, ImageName):
        self._ImageName = ImageName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def WorkspaceVersion(self):
        return self._WorkspaceVersion

    @WorkspaceVersion.setter
    def WorkspaceVersion(self, WorkspaceVersion):
        self._WorkspaceVersion = WorkspaceVersion

    @property
    def WorkspaceResourceDTO(self):
        return self._WorkspaceResourceDTO

    @WorkspaceResourceDTO.setter
    def WorkspaceResourceDTO(self, WorkspaceResourceDTO):
        self._WorkspaceResourceDTO = WorkspaceResourceDTO

    @property
    def VersionControlUrl(self):
        return self._VersionControlUrl

    @VersionControlUrl.setter
    def VersionControlUrl(self, VersionControlUrl):
        self._VersionControlUrl = VersionControlUrl

    @property
    def VersionControlRef(self):
        return self._VersionControlRef

    @VersionControlRef.setter
    def VersionControlRef(self, VersionControlRef):
        self._VersionControlRef = VersionControlRef

    @property
    def VersionControlRefType(self):
        return self._VersionControlRefType

    @VersionControlRefType.setter
    def VersionControlRefType(self, VersionControlRefType):
        self._VersionControlRefType = VersionControlRefType

    @property
    def SnapshotUid(self):
        return self._SnapshotUid

    @SnapshotUid.setter
    def SnapshotUid(self, SnapshotUid):
        self._SnapshotUid = SnapshotUid

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def PriceId(self):
        return self._PriceId

    @PriceId.setter
    def PriceId(self, PriceId):
        self._PriceId = PriceId

    @property
    def InitializeStatus(self):
        return self._InitializeStatus

    @InitializeStatus.setter
    def InitializeStatus(self, InitializeStatus):
        self._InitializeStatus = InitializeStatus

    @property
    def VersionControlDesc(self):
        return self._VersionControlDesc

    @VersionControlDesc.setter
    def VersionControlDesc(self, VersionControlDesc):
        self._VersionControlDesc = VersionControlDesc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._VersionControlType = params.get("VersionControlType")
        self._ImageId = params.get("ImageId")
        self._ImageName = params.get("ImageName")
        self._Description = params.get("Description")
        self._WorkspaceVersion = params.get("WorkspaceVersion")
        if params.get("WorkspaceResourceDTO") is not None:
            self._WorkspaceResourceDTO = WorkspaceResourceDTO()
            self._WorkspaceResourceDTO._deserialize(params.get("WorkspaceResourceDTO"))
        self._VersionControlUrl = params.get("VersionControlUrl")
        self._VersionControlRef = params.get("VersionControlRef")
        self._VersionControlRefType = params.get("VersionControlRefType")
        self._SnapshotUid = params.get("SnapshotUid")
        self._TemplateId = params.get("TemplateId")
        self._PriceId = params.get("PriceId")
        self._InitializeStatus = params.get("InitializeStatus")
        self._VersionControlDesc = params.get("VersionControlDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceInfo(AbstractModel):
    """工作空间信息

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 工作空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: int
        :param _SpaceKey: 工作空间标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SpaceKey: str
        :param _Name: 工作空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        """
        self._WorkspaceId = None
        self._SpaceKey = None
        self._Name = None

    @property
    def WorkspaceId(self):
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._SpaceKey = params.get("SpaceKey")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceInfoDTO(AbstractModel):
    """工作空间基本信息描述

    """

    def __init__(self):
        r"""
        :param _CreateDate: 工作空间创建时间
        :type CreateDate: str
        :param _SpaceKey: 空间key
        :type SpaceKey: str
        :param _WorkspaceId: 工作空间id
        :type WorkspaceId: int
        """
        self._CreateDate = None
        self._SpaceKey = None
        self._WorkspaceId = None

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def WorkspaceId(self):
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId


    def _deserialize(self, params):
        self._CreateDate = params.get("CreateDate")
        self._SpaceKey = params.get("SpaceKey")
        self._WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceResourceDTO(AbstractModel):
    """工作空间资源结构

    """

    def __init__(self):
        r"""
        :param _CpuCoreNumber: CPU核心数
        :type CpuCoreNumber: int
        :param _NormalMemory: 一般内存
        :type NormalMemory: int
        :param _SystemStorage: 系统存储
        :type SystemStorage: int
        :param _UserStorage: 用户存储
        :type UserStorage: int
        :param _GpuNumber: GPU数
        :type GpuNumber: int
        :param _GpuMemory: GPU内存
        :type GpuMemory: int
        """
        self._CpuCoreNumber = None
        self._NormalMemory = None
        self._SystemStorage = None
        self._UserStorage = None
        self._GpuNumber = None
        self._GpuMemory = None

    @property
    def CpuCoreNumber(self):
        return self._CpuCoreNumber

    @CpuCoreNumber.setter
    def CpuCoreNumber(self, CpuCoreNumber):
        self._CpuCoreNumber = CpuCoreNumber

    @property
    def NormalMemory(self):
        return self._NormalMemory

    @NormalMemory.setter
    def NormalMemory(self, NormalMemory):
        self._NormalMemory = NormalMemory

    @property
    def SystemStorage(self):
        return self._SystemStorage

    @SystemStorage.setter
    def SystemStorage(self, SystemStorage):
        self._SystemStorage = SystemStorage

    @property
    def UserStorage(self):
        return self._UserStorage

    @UserStorage.setter
    def UserStorage(self, UserStorage):
        self._UserStorage = UserStorage

    @property
    def GpuNumber(self):
        return self._GpuNumber

    @GpuNumber.setter
    def GpuNumber(self, GpuNumber):
        self._GpuNumber = GpuNumber

    @property
    def GpuMemory(self):
        return self._GpuMemory

    @GpuMemory.setter
    def GpuMemory(self, GpuMemory):
        self._GpuMemory = GpuMemory


    def _deserialize(self, params):
        self._CpuCoreNumber = params.get("CpuCoreNumber")
        self._NormalMemory = params.get("NormalMemory")
        self._SystemStorage = params.get("SystemStorage")
        self._UserStorage = params.get("UserStorage")
        self._GpuNumber = params.get("GpuNumber")
        self._GpuMemory = params.get("GpuMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceShareInfo(AbstractModel):
    """用户空间共享信息

    """

    def __init__(self):
        r"""
        :param _Status: 共享或不共享状态
        :type Status: bool
        :param _WithMe: 是否与我共享
注意：此字段可能返回 null，表示取不到有效值。
        :type WithMe: bool
        :param _BeginDate: 开始共享的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginDate: str
        :param _EndDate: 停止共享的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndDate: str
        :param _Users: 停止共享的时间
        :type Users: list of UserInfoRsp
        """
        self._Status = None
        self._WithMe = None
        self._BeginDate = None
        self._EndDate = None
        self._Users = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def WithMe(self):
        return self._WithMe

    @WithMe.setter
    def WithMe(self, WithMe):
        self._WithMe = WithMe

    @property
    def BeginDate(self):
        return self._BeginDate

    @BeginDate.setter
    def BeginDate(self, BeginDate):
        self._BeginDate = BeginDate

    @property
    def EndDate(self):
        return self._EndDate

    @EndDate.setter
    def EndDate(self, EndDate):
        self._EndDate = EndDate

    @property
    def Users(self):
        return self._Users

    @Users.setter
    def Users(self, Users):
        self._Users = Users


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._WithMe = params.get("WithMe")
        self._BeginDate = params.get("BeginDate")
        self._EndDate = params.get("EndDate")
        if params.get("Users") is not None:
            self._Users = []
            for item in params.get("Users"):
                obj = UserInfoRsp()
                obj._deserialize(item)
                self._Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceStatusInfo(AbstractModel):
    """获取用户工作空间返回信息

    """

    def __init__(self):
        r"""
        :param _Id: 空间ID
        :type Id: int
        :param _Name: 空间名称
        :type Name: str
        :param _Owner: 所属人
        :type Owner: :class:`tencentcloud.cloudstudio.v20210524.models.UserInfoRsp`
        :param _SpaceKey: 空间标识
        :type SpaceKey: str
        :param _Status: 状态
        :type Status: str
        :param _LastOpsDate: 最后操作时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOpsDate: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Share: 共享状态
        :type Share: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceShareInfo`
        :param _WorkspaceType: 空间类型
        :type WorkspaceType: str
        :param _Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _WorkspaceVersion: 空间版本
        :type WorkspaceVersion: int
        :param _ImageIcon: 图标地址
        :type ImageIcon: str
        :param _CreateDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param _VersionControlUrl: 版本控制地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlUrl: str
        :param _VersionControlDesc: 版本控制描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlDesc: str
        :param _VersionControlRef: 版本控制引用
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRef: str
        :param _VersionControlRefType: 版本控制引用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRefType: str
        :param _VersionControlType: 版本控制类型
        :type VersionControlType: str
        :param _TemplateId: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: int
        :param _SnapshotUid: 快照ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotUid: str
        :param _SpecDesc: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecDesc: str
        :param _Cpu: CPU数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param _Memory: 内存
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        """
        self._Id = None
        self._Name = None
        self._Owner = None
        self._SpaceKey = None
        self._Status = None
        self._LastOpsDate = None
        self._Description = None
        self._Share = None
        self._WorkspaceType = None
        self._Label = None
        self._WorkspaceVersion = None
        self._ImageIcon = None
        self._CreateDate = None
        self._VersionControlUrl = None
        self._VersionControlDesc = None
        self._VersionControlRef = None
        self._VersionControlRefType = None
        self._VersionControlType = None
        self._TemplateId = None
        self._SnapshotUid = None
        self._SpecDesc = None
        self._Cpu = None
        self._Memory = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LastOpsDate(self):
        return self._LastOpsDate

    @LastOpsDate.setter
    def LastOpsDate(self, LastOpsDate):
        self._LastOpsDate = LastOpsDate

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Share(self):
        return self._Share

    @Share.setter
    def Share(self, Share):
        self._Share = Share

    @property
    def WorkspaceType(self):
        return self._WorkspaceType

    @WorkspaceType.setter
    def WorkspaceType(self, WorkspaceType):
        self._WorkspaceType = WorkspaceType

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def WorkspaceVersion(self):
        return self._WorkspaceVersion

    @WorkspaceVersion.setter
    def WorkspaceVersion(self, WorkspaceVersion):
        self._WorkspaceVersion = WorkspaceVersion

    @property
    def ImageIcon(self):
        return self._ImageIcon

    @ImageIcon.setter
    def ImageIcon(self, ImageIcon):
        self._ImageIcon = ImageIcon

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def VersionControlUrl(self):
        return self._VersionControlUrl

    @VersionControlUrl.setter
    def VersionControlUrl(self, VersionControlUrl):
        self._VersionControlUrl = VersionControlUrl

    @property
    def VersionControlDesc(self):
        return self._VersionControlDesc

    @VersionControlDesc.setter
    def VersionControlDesc(self, VersionControlDesc):
        self._VersionControlDesc = VersionControlDesc

    @property
    def VersionControlRef(self):
        return self._VersionControlRef

    @VersionControlRef.setter
    def VersionControlRef(self, VersionControlRef):
        self._VersionControlRef = VersionControlRef

    @property
    def VersionControlRefType(self):
        return self._VersionControlRefType

    @VersionControlRefType.setter
    def VersionControlRefType(self, VersionControlRefType):
        self._VersionControlRefType = VersionControlRefType

    @property
    def VersionControlType(self):
        return self._VersionControlType

    @VersionControlType.setter
    def VersionControlType(self, VersionControlType):
        self._VersionControlType = VersionControlType

    @property
    def TemplateId(self):
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def SnapshotUid(self):
        return self._SnapshotUid

    @SnapshotUid.setter
    def SnapshotUid(self, SnapshotUid):
        self._SnapshotUid = SnapshotUid

    @property
    def SpecDesc(self):
        return self._SpecDesc

    @SpecDesc.setter
    def SpecDesc(self, SpecDesc):
        self._SpecDesc = SpecDesc

    @property
    def Cpu(self):
        return self._Cpu

    @Cpu.setter
    def Cpu(self, Cpu):
        self._Cpu = Cpu

    @property
    def Memory(self):
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        if params.get("Owner") is not None:
            self._Owner = UserInfoRsp()
            self._Owner._deserialize(params.get("Owner"))
        self._SpaceKey = params.get("SpaceKey")
        self._Status = params.get("Status")
        self._LastOpsDate = params.get("LastOpsDate")
        self._Description = params.get("Description")
        if params.get("Share") is not None:
            self._Share = WorkspaceShareInfo()
            self._Share._deserialize(params.get("Share"))
        self._WorkspaceType = params.get("WorkspaceType")
        self._Label = params.get("Label")
        self._WorkspaceVersion = params.get("WorkspaceVersion")
        self._ImageIcon = params.get("ImageIcon")
        self._CreateDate = params.get("CreateDate")
        self._VersionControlUrl = params.get("VersionControlUrl")
        self._VersionControlDesc = params.get("VersionControlDesc")
        self._VersionControlRef = params.get("VersionControlRef")
        self._VersionControlRefType = params.get("VersionControlRefType")
        self._VersionControlType = params.get("VersionControlType")
        self._TemplateId = params.get("TemplateId")
        self._SnapshotUid = params.get("SnapshotUid")
        self._SpecDesc = params.get("SpecDesc")
        self._Cpu = params.get("Cpu")
        self._Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceTemplateInfo(AbstractModel):
    """工作空间模板信息

    """

    def __init__(self):
        r"""
        :param _Id: 模板ID
        :type Id: int
        :param _Category: 模板分类
        :type Category: str
        :param _Name: 模板名称
        :type Name: str
        :param _Description: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _DescriptionEN: 中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionEN: str
        :param _Tags: 模板标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: str
        :param _Icon: 模板图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param _VersionControlType: 默认仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlType: str
        :param _VersionControlUrl: 默认仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlUrl: str
        :param _VersionControlDesc: 默认仓库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlDesc: str
        :param _VersionControlOwner: 默认仓库所属人
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlOwner: str
        :param _VersionControlRef: 默认仓库引用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRef: str
        :param _VersionControlRefType: 默认仓库引用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRefType: str
        :param _UserVersionControlUrl: 用户自定义仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVersionControlUrl: str
        :param _UserVersionControlType: 用户自定义仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVersionControlType: str
        :param _UserVersionControlRef: 用户自定义仓库引用
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVersionControlRef: str
        :param _UserVersionControlRefType: 用户自定义仓库引用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVersionControlRefType: str
        :param _DevFile: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type DevFile: str
        :param _PluginFile: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginFile: str
        :param _Marked: 是否标记
        :type Marked: bool
        :param _MarkAt: 标记状态
        :type MarkAt: int
        :param _CreateDate: 创建时间
        :type CreateDate: str
        :param _LastModified: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModified: str
        :param _Sort: 编号
        :type Sort: int
        :param _SnapshotUid: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotUid: str
        :param _UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: int
        :param _Author: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Author: str
        :param _Me: 是否属于当前用户
        :type Me: bool
        :param _AuthorAvatar: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorAvatar: str
        """
        self._Id = None
        self._Category = None
        self._Name = None
        self._Description = None
        self._DescriptionEN = None
        self._Tags = None
        self._Icon = None
        self._VersionControlType = None
        self._VersionControlUrl = None
        self._VersionControlDesc = None
        self._VersionControlOwner = None
        self._VersionControlRef = None
        self._VersionControlRefType = None
        self._UserVersionControlUrl = None
        self._UserVersionControlType = None
        self._UserVersionControlRef = None
        self._UserVersionControlRefType = None
        self._DevFile = None
        self._PluginFile = None
        self._Marked = None
        self._MarkAt = None
        self._CreateDate = None
        self._LastModified = None
        self._Sort = None
        self._SnapshotUid = None
        self._UserId = None
        self._Author = None
        self._Me = None
        self._AuthorAvatar = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DescriptionEN(self):
        return self._DescriptionEN

    @DescriptionEN.setter
    def DescriptionEN(self, DescriptionEN):
        self._DescriptionEN = DescriptionEN

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Icon(self):
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def VersionControlType(self):
        return self._VersionControlType

    @VersionControlType.setter
    def VersionControlType(self, VersionControlType):
        self._VersionControlType = VersionControlType

    @property
    def VersionControlUrl(self):
        return self._VersionControlUrl

    @VersionControlUrl.setter
    def VersionControlUrl(self, VersionControlUrl):
        self._VersionControlUrl = VersionControlUrl

    @property
    def VersionControlDesc(self):
        return self._VersionControlDesc

    @VersionControlDesc.setter
    def VersionControlDesc(self, VersionControlDesc):
        self._VersionControlDesc = VersionControlDesc

    @property
    def VersionControlOwner(self):
        return self._VersionControlOwner

    @VersionControlOwner.setter
    def VersionControlOwner(self, VersionControlOwner):
        self._VersionControlOwner = VersionControlOwner

    @property
    def VersionControlRef(self):
        return self._VersionControlRef

    @VersionControlRef.setter
    def VersionControlRef(self, VersionControlRef):
        self._VersionControlRef = VersionControlRef

    @property
    def VersionControlRefType(self):
        return self._VersionControlRefType

    @VersionControlRefType.setter
    def VersionControlRefType(self, VersionControlRefType):
        self._VersionControlRefType = VersionControlRefType

    @property
    def UserVersionControlUrl(self):
        return self._UserVersionControlUrl

    @UserVersionControlUrl.setter
    def UserVersionControlUrl(self, UserVersionControlUrl):
        self._UserVersionControlUrl = UserVersionControlUrl

    @property
    def UserVersionControlType(self):
        return self._UserVersionControlType

    @UserVersionControlType.setter
    def UserVersionControlType(self, UserVersionControlType):
        self._UserVersionControlType = UserVersionControlType

    @property
    def UserVersionControlRef(self):
        return self._UserVersionControlRef

    @UserVersionControlRef.setter
    def UserVersionControlRef(self, UserVersionControlRef):
        self._UserVersionControlRef = UserVersionControlRef

    @property
    def UserVersionControlRefType(self):
        return self._UserVersionControlRefType

    @UserVersionControlRefType.setter
    def UserVersionControlRefType(self, UserVersionControlRefType):
        self._UserVersionControlRefType = UserVersionControlRefType

    @property
    def DevFile(self):
        return self._DevFile

    @DevFile.setter
    def DevFile(self, DevFile):
        self._DevFile = DevFile

    @property
    def PluginFile(self):
        return self._PluginFile

    @PluginFile.setter
    def PluginFile(self, PluginFile):
        self._PluginFile = PluginFile

    @property
    def Marked(self):
        return self._Marked

    @Marked.setter
    def Marked(self, Marked):
        self._Marked = Marked

    @property
    def MarkAt(self):
        return self._MarkAt

    @MarkAt.setter
    def MarkAt(self, MarkAt):
        self._MarkAt = MarkAt

    @property
    def CreateDate(self):
        return self._CreateDate

    @CreateDate.setter
    def CreateDate(self, CreateDate):
        self._CreateDate = CreateDate

    @property
    def LastModified(self):
        return self._LastModified

    @LastModified.setter
    def LastModified(self, LastModified):
        self._LastModified = LastModified

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def SnapshotUid(self):
        return self._SnapshotUid

    @SnapshotUid.setter
    def SnapshotUid(self, SnapshotUid):
        self._SnapshotUid = SnapshotUid

    @property
    def UserId(self):
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Author(self):
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def Me(self):
        return self._Me

    @Me.setter
    def Me(self, Me):
        self._Me = Me

    @property
    def AuthorAvatar(self):
        return self._AuthorAvatar

    @AuthorAvatar.setter
    def AuthorAvatar(self, AuthorAvatar):
        self._AuthorAvatar = AuthorAvatar


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Category = params.get("Category")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._DescriptionEN = params.get("DescriptionEN")
        self._Tags = params.get("Tags")
        self._Icon = params.get("Icon")
        self._VersionControlType = params.get("VersionControlType")
        self._VersionControlUrl = params.get("VersionControlUrl")
        self._VersionControlDesc = params.get("VersionControlDesc")
        self._VersionControlOwner = params.get("VersionControlOwner")
        self._VersionControlRef = params.get("VersionControlRef")
        self._VersionControlRefType = params.get("VersionControlRefType")
        self._UserVersionControlUrl = params.get("UserVersionControlUrl")
        self._UserVersionControlType = params.get("UserVersionControlType")
        self._UserVersionControlRef = params.get("UserVersionControlRef")
        self._UserVersionControlRefType = params.get("UserVersionControlRefType")
        self._DevFile = params.get("DevFile")
        self._PluginFile = params.get("PluginFile")
        self._Marked = params.get("Marked")
        self._MarkAt = params.get("MarkAt")
        self._CreateDate = params.get("CreateDate")
        self._LastModified = params.get("LastModified")
        self._Sort = params.get("Sort")
        self._SnapshotUid = params.get("SnapshotUid")
        self._UserId = params.get("UserId")
        self._Author = params.get("Author")
        self._Me = params.get("Me")
        self._AuthorAvatar = params.get("AuthorAvatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceTokenDTO(AbstractModel):
    """创建临时工作空间凭证 DTO

    """

    def __init__(self):
        r"""
        :param _SpaceKey: 工作空间 SpaceKey
        :type SpaceKey: str
        :param _TokenExpiredLimitSec: token过期时间，单位是秒，默认 3600
        :type TokenExpiredLimitSec: int
        """
        self._SpaceKey = None
        self._TokenExpiredLimitSec = None

    @property
    def SpaceKey(self):
        return self._SpaceKey

    @SpaceKey.setter
    def SpaceKey(self, SpaceKey):
        self._SpaceKey = SpaceKey

    @property
    def TokenExpiredLimitSec(self):
        return self._TokenExpiredLimitSec

    @TokenExpiredLimitSec.setter
    def TokenExpiredLimitSec(self, TokenExpiredLimitSec):
        self._TokenExpiredLimitSec = TokenExpiredLimitSec


    def _deserialize(self, params):
        self._SpaceKey = params.get("SpaceKey")
        self._TokenExpiredLimitSec = params.get("TokenExpiredLimitSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceTokenInfoV0(AbstractModel):
    """获取工作空间临时访问 token 出参

    """

    def __init__(self):
        r"""
        :param _Token: 访问工作空间临时凭证
        :type Token: str
        :param _ExpiredTime: token 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        """
        self._Token = None
        self._ExpiredTime = None

    @property
    def Token(self):
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime


    def _deserialize(self, params):
        self._Token = params.get("Token")
        self._ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        