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
        :param Name: 工作空间名称
        :type Name: str
        :param ImageId: 镜像id
        :type ImageId: int
        :param ImageName: 镜像名称
        :type ImageName: str
        :param RemoteUser: 云服务器登录名称
        :type RemoteUser: str
        :param RemoteHost: 云服务器登录地址
        :type RemoteHost: str
        :param RemotePort: 云服务器登录端口
        :type RemotePort: str
        :param WorkspaceType: 工作空间类型
        :type WorkspaceType: str
        :param WorkspaceVersion: 工作空间版本
        :type WorkspaceVersion: int
        :param WorkspaceResourceDTO: 工作空间资源结构
        :type WorkspaceResourceDTO: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceResourceDTO`
        :param Description: 描述
        :type Description: str
        """
        self.Name = None
        self.ImageId = None
        self.ImageName = None
        self.RemoteUser = None
        self.RemoteHost = None
        self.RemotePort = None
        self.WorkspaceType = None
        self.WorkspaceVersion = None
        self.WorkspaceResourceDTO = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.RemoteUser = params.get("RemoteUser")
        self.RemoteHost = params.get("RemoteHost")
        self.RemotePort = params.get("RemotePort")
        self.WorkspaceType = params.get("WorkspaceType")
        self.WorkspaceVersion = params.get("WorkspaceVersion")
        if params.get("WorkspaceResourceDTO") is not None:
            self.WorkspaceResourceDTO = WorkspaceResourceDTO()
            self.WorkspaceResourceDTO._deserialize(params.get("WorkspaceResourceDTO"))
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomizeTemplatesRequest(AbstractModel):
    """CreateCustomizeTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param UserDefinedTemplateParams: 无
        :type UserDefinedTemplateParams: :class:`tencentcloud.cloudstudio.v20210524.models.UserDefinedTemplateParams`
        """
        self.CloudStudioSessionTeam = None
        self.UserDefinedTemplateParams = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        if params.get("UserDefinedTemplateParams") is not None:
            self.UserDefinedTemplateParams = UserDefinedTemplateParams()
            self.UserDefinedTemplateParams._deserialize(params.get("UserDefinedTemplateParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomizeTemplatesResponse(AbstractModel):
    """CreateCustomizeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceTemplateInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateWorkspaceByAgentRequest(AbstractModel):
    """CreateWorkspaceByAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 无
        :type CloudStudioSessionTeam: str
        :param AgentSpaceDTO: 无
        :type AgentSpaceDTO: :class:`tencentcloud.cloudstudio.v20210524.models.AgentSpaceDTO`
        """
        self.CloudStudioSessionTeam = None
        self.AgentSpaceDTO = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        if params.get("AgentSpaceDTO") is not None:
            self.AgentSpaceDTO = AgentSpaceDTO()
            self.AgentSpaceDTO._deserialize(params.get("AgentSpaceDTO"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceByAgentResponse(AbstractModel):
    """CreateWorkspaceByAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceInfoDTO`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceInfoDTO()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateWorkspaceByTemplateRequest(AbstractModel):
    """CreateWorkspaceByTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param TemplateId: 模板ID
        :type TemplateId: int
        """
        self.CloudStudioSessionTeam = None
        self.TemplateId = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceByTemplateResponse(AbstractModel):
    """CreateWorkspaceByTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 创建工作空间返回的信息
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CreateWorkspaceByVersionControlRequest(AbstractModel):
    """CreateWorkspaceByVersionControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param WorkspaceDTO: 工作空间结构
        :type WorkspaceDTO: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceDTO`
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        """
        self.WorkspaceDTO = None
        self.CloudStudioSessionTeam = None


    def _deserialize(self, params):
        if params.get("WorkspaceDTO") is not None:
            self.WorkspaceDTO = WorkspaceDTO()
            self.WorkspaceDTO._deserialize(params.get("WorkspaceDTO"))
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWorkspaceByVersionControlResponse(AbstractModel):
    """CreateWorkspaceByVersionControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceInfoDTO`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceInfoDTO()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class CustomizeTemplatesPresetsInfo(AbstractModel):
    """模板的预置参数

    """

    def __init__(self):
        r"""
        :param Tags: 模板tag列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param Icons: 模板图标列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Icons: list of str
        :param Templates: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Templates: :class:`tencentcloud.cloudstudio.v20210524.models.UserDefinedTemplateParams`
        """
        self.Tags = None
        self.Icons = None
        self.Templates = None


    def _deserialize(self, params):
        self.Tags = params.get("Tags")
        self.Icons = params.get("Icons")
        if params.get("Templates") is not None:
            self.Templates = UserDefinedTemplateParams()
            self.Templates._deserialize(params.get("Templates"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizeTemplatesByIdRequest(AbstractModel):
    """DeleteCustomizeTemplatesById请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param Id: 模板ID
        :type Id: int
        """
        self.CloudStudioSessionTeam = None
        self.Id = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomizeTemplatesByIdResponse(AbstractModel):
    """DeleteCustomizeTemplatesById返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomizeTemplatesByIdRequest(AbstractModel):
    """DescribeCustomizeTemplatesById请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param Id: 模板ID
        :type Id: int
        """
        self.CloudStudioSessionTeam = None
        self.Id = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizeTemplatesByIdResponse(AbstractModel):
    """DescribeCustomizeTemplatesById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceTemplateInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCustomizeTemplatesPresetsRequest(AbstractModel):
    """DescribeCustomizeTemplatesPresets请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param SpaceKey: 空间标识
        :type SpaceKey: str
        """
        self.CloudStudioSessionTeam = None
        self.SpaceKey = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizeTemplatesPresetsResponse(AbstractModel):
    """DescribeCustomizeTemplatesPresets返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.CustomizeTemplatesPresetsInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = CustomizeTemplatesPresetsInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeCustomizeTemplatesRequest(AbstractModel):
    """DescribeCustomizeTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        """
        self.CloudStudioSessionTeam = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomizeTemplatesResponse(AbstractModel):
    """DescribeCustomizeTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of WorkspaceTemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = WorkspaceTemplateInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkspaceEnvListRequest(AbstractModel):
    """DescribeWorkspaceEnvList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        """
        self.CloudStudioSessionTeam = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceEnvListResponse(AbstractModel):
    """DescribeWorkspaceEnvList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of ImageUserDTO
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ImageUserDTO()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkspaceNameExistRequest(AbstractModel):
    """DescribeWorkspaceNameExist请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param Name: 工作空间名称
        :type Name: str
        :param WorkspaceId: 工作空间ID
        :type WorkspaceId: str
        """
        self.CloudStudioSessionTeam = None
        self.Name = None
        self.WorkspaceId = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.Name = params.get("Name")
        self.WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceNameExistResponse(AbstractModel):
    """DescribeWorkspaceNameExist返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeWorkspaceStatusListRequest(AbstractModel):
    """DescribeWorkspaceStatusList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: xxx
        :type CloudStudioSessionTeam: str
        """
        self.CloudStudioSessionTeam = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceStatusListResponse(AbstractModel):
    """DescribeWorkspaceStatusList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of WorkspaceStatusInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = WorkspaceStatusInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWorkspaceStatusRequest(AbstractModel):
    """DescribeWorkspaceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param SpaceKey: 空间标识
        :type SpaceKey: str
        """
        self.CloudStudioSessionTeam = None
        self.SpaceKey = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWorkspaceStatusResponse(AbstractModel):
    """DescribeWorkspaceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceStatusInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceStatusInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ImageUserDTO(AbstractModel):
    """可用镜像模板列表

    """

    def __init__(self):
        r"""
        :param Id: 镜像模板ID
        :type Id: str
        :param Name: 镜像模板名称
        :type Name: str
        :param Tag: Tag时间
        :type Tag: str
        :param Description: 描述
        :type Description: str
        :param DescriptionCN: 中文描述
        :type DescriptionCN: str
        :param IconUrl: 图标地址
        :type IconUrl: str
        :param Author: 创建人
        :type Author: str
        :param Visible: 访问状态
        :type Visible: str
        :param WorkspaceVersion: 版本
        :type WorkspaceVersion: int
        :param Sort: 分类
        :type Sort: int
        """
        self.Id = None
        self.Name = None
        self.Tag = None
        self.Description = None
        self.DescriptionCN = None
        self.IconUrl = None
        self.Author = None
        self.Visible = None
        self.WorkspaceVersion = None
        self.Sort = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Tag = params.get("Tag")
        self.Description = params.get("Description")
        self.DescriptionCN = params.get("DescriptionCN")
        self.IconUrl = params.get("IconUrl")
        self.Author = params.get("Author")
        self.Visible = params.get("Visible")
        self.WorkspaceVersion = params.get("WorkspaceVersion")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizeTemplateVersionControlRequest(AbstractModel):
    """ModifyCustomizeTemplateVersionControl请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param TemplateId: 模板ID
        :type TemplateId: int
        :param Url: 仓库地址
        :type Url: str
        :param Ref: 代码仓库分支/标签
        :type Ref: str
        :param RefType: 代码仓库 ref 类型
        :type RefType: str
        """
        self.CloudStudioSessionTeam = None
        self.TemplateId = None
        self.Url = None
        self.Ref = None
        self.RefType = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.TemplateId = params.get("TemplateId")
        self.Url = params.get("Url")
        self.Ref = params.get("Ref")
        self.RefType = params.get("RefType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizeTemplateVersionControlResponse(AbstractModel):
    """ModifyCustomizeTemplateVersionControl返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 无
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceTemplateInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ModifyCustomizeTemplatesFullByIdRequest(AbstractModel):
    """ModifyCustomizeTemplatesFullById请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param Id: 模板ID
        :type Id: int
        :param UserDefinedTemplateParams: 自定义模板参数
        :type UserDefinedTemplateParams: :class:`tencentcloud.cloudstudio.v20210524.models.UserDefinedTemplateParams`
        """
        self.CloudStudioSessionTeam = None
        self.Id = None
        self.UserDefinedTemplateParams = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.Id = params.get("Id")
        if params.get("UserDefinedTemplateParams") is not None:
            self.UserDefinedTemplateParams = UserDefinedTemplateParams()
            self.UserDefinedTemplateParams._deserialize(params.get("UserDefinedTemplateParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizeTemplatesFullByIdResponse(AbstractModel):
    """ModifyCustomizeTemplatesFullById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 自定义模板返回值
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceTemplateInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ModifyCustomizeTemplatesPartByIdRequest(AbstractModel):
    """ModifyCustomizeTemplatesPartById请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param Id: 模板ID
        :type Id: int
        :param UserDefinedTemplatePatchedParams: 自定义模板Patched参数
        :type UserDefinedTemplatePatchedParams: :class:`tencentcloud.cloudstudio.v20210524.models.UserDefinedTemplatePatchedParams`
        """
        self.CloudStudioSessionTeam = None
        self.Id = None
        self.UserDefinedTemplatePatchedParams = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.Id = params.get("Id")
        if params.get("UserDefinedTemplatePatchedParams") is not None:
            self.UserDefinedTemplatePatchedParams = UserDefinedTemplatePatchedParams()
            self.UserDefinedTemplatePatchedParams._deserialize(params.get("UserDefinedTemplatePatchedParams"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomizeTemplatesPartByIdResponse(AbstractModel):
    """ModifyCustomizeTemplatesPartById返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 自定义模板返回值
        :type Data: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceTemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = WorkspaceTemplateInfo()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class ModifyWorkspaceAttributesRequest(AbstractModel):
    """ModifyWorkspaceAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param WorkspaceId: 工作空间ID
        :type WorkspaceId: int
        :param Name: 工作空间名称
        :type Name: str
        :param Description: 工作空间描述
        :type Description: str
        :param PriceId: xxx
        :type PriceId: int
        """
        self.CloudStudioSessionTeam = None
        self.WorkspaceId = None
        self.Name = None
        self.Description = None
        self.PriceId = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.WorkspaceId = params.get("WorkspaceId")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.PriceId = params.get("PriceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyWorkspaceAttributesResponse(AbstractModel):
    """ModifyWorkspaceAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RecoverWorkspaceRequest(AbstractModel):
    """RecoverWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 无
        :type CloudStudioSessionTeam: str
        :param SpaceKey: 无
        :type SpaceKey: str
        """
        self.CloudStudioSessionTeam = None
        self.SpaceKey = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RecoverWorkspaceResponse(AbstractModel):
    """RecoverWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveWorkspaceRequest(AbstractModel):
    """RemoveWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param CloudStudioSessionTeam: 无
        :type CloudStudioSessionTeam: str
        :param SpaceKey: 无
        :type SpaceKey: str
        :param Force: 是否强制，true或者false
        :type Force: bool
        """
        self.CloudStudioSessionTeam = None
        self.SpaceKey = None
        self.Force = None


    def _deserialize(self, params):
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.SpaceKey = params.get("SpaceKey")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveWorkspaceResponse(AbstractModel):
    """RemoveWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RunWorkspaceRequest(AbstractModel):
    """RunWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceKey: 空间标识
        :type SpaceKey: str
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        """
        self.SpaceKey = None
        self.CloudStudioSessionTeam = None


    def _deserialize(self, params):
        self.SpaceKey = params.get("SpaceKey")
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunWorkspaceResponse(AbstractModel):
    """RunWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopWorkspaceRequest(AbstractModel):
    """StopWorkspace请求参数结构体

    """

    def __init__(self):
        r"""
        :param SpaceKey: 空间标识
        :type SpaceKey: str
        :param CloudStudioSessionTeam: 用户所属组
        :type CloudStudioSessionTeam: str
        :param Force: 是否强制终止，true或者false
        :type Force: str
        """
        self.SpaceKey = None
        self.CloudStudioSessionTeam = None
        self.Force = None


    def _deserialize(self, params):
        self.SpaceKey = params.get("SpaceKey")
        self.CloudStudioSessionTeam = params.get("CloudStudioSessionTeam")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopWorkspaceResponse(AbstractModel):
    """StopWorkspace返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UserDefinedTemplateParams(AbstractModel):
    """用户自定义模板参数

    """

    def __init__(self):
        r"""
        :param Name: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Icon: 模板图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param Tags: 模板标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param Source: 模板来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param Description: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param VersionControlType: 模板仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlType: str
        :param VersionControlUrl: 模板地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlUrl: str
        """
        self.Name = None
        self.Icon = None
        self.Tags = None
        self.Source = None
        self.Description = None
        self.VersionControlType = None
        self.VersionControlUrl = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Icon = params.get("Icon")
        self.Tags = params.get("Tags")
        self.Source = params.get("Source")
        self.Description = params.get("Description")
        self.VersionControlType = params.get("VersionControlType")
        self.VersionControlUrl = params.get("VersionControlUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserDefinedTemplatePatchedParams(AbstractModel):
    """用户自定义模板Patched参数

    """

    def __init__(self):
        r"""
        :param Source: 模板来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param Name: 模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Icon: 模板图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param Description: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Tags: 模板标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        """
        self.Source = None
        self.Name = None
        self.Icon = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Name = params.get("Name")
        self.Icon = params.get("Icon")
        self.Description = params.get("Description")
        self.Tags = params.get("Tags")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserInfoRsp(AbstractModel):
    """用户信息

    """

    def __init__(self):
        r"""
        :param Id: 用户ID
        :type Id: int
        :param AuthenticationUserInfo: 用户验证信息
        :type AuthenticationUserInfo: :class:`tencentcloud.cloudstudio.v20210524.models.UserSubInfo`
        :param Avatar: 头像地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Avatar: str
        :param Features: 介绍
注意：此字段可能返回 null，表示取不到有效值。
        :type Features: str
        :param PreviewStatus: 状况
        :type PreviewStatus: int
        """
        self.Id = None
        self.AuthenticationUserInfo = None
        self.Avatar = None
        self.Features = None
        self.PreviewStatus = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        if params.get("AuthenticationUserInfo") is not None:
            self.AuthenticationUserInfo = UserSubInfo()
            self.AuthenticationUserInfo._deserialize(params.get("AuthenticationUserInfo"))
        self.Avatar = params.get("Avatar")
        self.Features = params.get("Features")
        self.PreviewStatus = params.get("PreviewStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserSubInfo(AbstractModel):
    """用户验证信息

    """

    def __init__(self):
        r"""
        :param Team: 团队名称
        :type Team: str
        :param UserName: 用户名
        :type UserName: str
        :param NickName: 昵称
        :type NickName: str
        :param IsAdmin: 是否为管理员
        :type IsAdmin: bool
        :param IsTrial: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type IsTrial: bool
        """
        self.Team = None
        self.UserName = None
        self.NickName = None
        self.IsAdmin = None
        self.IsTrial = None


    def _deserialize(self, params):
        self.Team = params.get("Team")
        self.UserName = params.get("UserName")
        self.NickName = params.get("NickName")
        self.IsAdmin = params.get("IsAdmin")
        self.IsTrial = params.get("IsTrial")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceDTO(AbstractModel):
    """工作空间结构

    """

    def __init__(self):
        r"""
        :param Name: 工作空间名称
        :type Name: str
        :param VersionControlType: 代码来源类型
        :type VersionControlType: str
        :param ImageId: 镜像id
        :type ImageId: int
        :param ImageName: 镜像名称
        :type ImageName: str
        :param Description: 描述
        :type Description: str
        :param WorkspaceVersion: 工作空间版本
        :type WorkspaceVersion: int
        :param WorkspaceResourceDTO: 工作空间资源结构
        :type WorkspaceResourceDTO: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceResourceDTO`
        :param VersionControlUrl: 代码仓库地址
        :type VersionControlUrl: str
        :param VersionControlRef: 代码Ref是分支还是标签
        :type VersionControlRef: str
        :param VersionControlRefType: 代码Ref地址
        :type VersionControlRefType: str
        :param SnapshotUid: 快照Uid
        :type SnapshotUid: str
        :param TemplateId: 模板id
        :type TemplateId: int
        :param PriceId: 价格id
        :type PriceId: int
        :param InitializeStatus: 初始化状态
        :type InitializeStatus: int
        :param VersionControlDesc: 描述
        :type VersionControlDesc: str
        """
        self.Name = None
        self.VersionControlType = None
        self.ImageId = None
        self.ImageName = None
        self.Description = None
        self.WorkspaceVersion = None
        self.WorkspaceResourceDTO = None
        self.VersionControlUrl = None
        self.VersionControlRef = None
        self.VersionControlRefType = None
        self.SnapshotUid = None
        self.TemplateId = None
        self.PriceId = None
        self.InitializeStatus = None
        self.VersionControlDesc = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.VersionControlType = params.get("VersionControlType")
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.Description = params.get("Description")
        self.WorkspaceVersion = params.get("WorkspaceVersion")
        if params.get("WorkspaceResourceDTO") is not None:
            self.WorkspaceResourceDTO = WorkspaceResourceDTO()
            self.WorkspaceResourceDTO._deserialize(params.get("WorkspaceResourceDTO"))
        self.VersionControlUrl = params.get("VersionControlUrl")
        self.VersionControlRef = params.get("VersionControlRef")
        self.VersionControlRefType = params.get("VersionControlRefType")
        self.SnapshotUid = params.get("SnapshotUid")
        self.TemplateId = params.get("TemplateId")
        self.PriceId = params.get("PriceId")
        self.InitializeStatus = params.get("InitializeStatus")
        self.VersionControlDesc = params.get("VersionControlDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceInfo(AbstractModel):
    """工作空间信息

    """

    def __init__(self):
        r"""
        :param WorkspaceId: 工作空间ID
注意：此字段可能返回 null，表示取不到有效值。
        :type WorkspaceId: int
        :param SpaceKey: 工作空间标识
注意：此字段可能返回 null，表示取不到有效值。
        :type SpaceKey: str
        """
        self.WorkspaceId = None
        self.SpaceKey = None


    def _deserialize(self, params):
        self.WorkspaceId = params.get("WorkspaceId")
        self.SpaceKey = params.get("SpaceKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceInfoDTO(AbstractModel):
    """工作空间基本信息描述

    """

    def __init__(self):
        r"""
        :param CreateDate: 工作空间创建时间
        :type CreateDate: str
        :param SpaceKey: 空间key
        :type SpaceKey: str
        :param WorkspaceId: 工作空间id
        :type WorkspaceId: int
        """
        self.CreateDate = None
        self.SpaceKey = None
        self.WorkspaceId = None


    def _deserialize(self, params):
        self.CreateDate = params.get("CreateDate")
        self.SpaceKey = params.get("SpaceKey")
        self.WorkspaceId = params.get("WorkspaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceResourceDTO(AbstractModel):
    """工作空间资源结构

    """

    def __init__(self):
        r"""
        :param CpuCoreNumber: CPU核心数
        :type CpuCoreNumber: int
        :param NormalMemory: 一般内存
        :type NormalMemory: int
        :param SystemStorage: 系统存储
        :type SystemStorage: int
        :param UserStorage: 用户存储
        :type UserStorage: int
        :param GpuNumber: GPU数
        :type GpuNumber: int
        :param GpuMemory: GPU内存
        :type GpuMemory: int
        """
        self.CpuCoreNumber = None
        self.NormalMemory = None
        self.SystemStorage = None
        self.UserStorage = None
        self.GpuNumber = None
        self.GpuMemory = None


    def _deserialize(self, params):
        self.CpuCoreNumber = params.get("CpuCoreNumber")
        self.NormalMemory = params.get("NormalMemory")
        self.SystemStorage = params.get("SystemStorage")
        self.UserStorage = params.get("UserStorage")
        self.GpuNumber = params.get("GpuNumber")
        self.GpuMemory = params.get("GpuMemory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceShareInfo(AbstractModel):
    """用户空间共享信息

    """

    def __init__(self):
        r"""
        :param Status: 共享或不共享状态
        :type Status: bool
        :param WithMe: 是否与我共享
注意：此字段可能返回 null，表示取不到有效值。
        :type WithMe: bool
        :param BeginDate: 开始共享的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginDate: str
        :param EndDate: 停止共享的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type EndDate: str
        :param Users: 停止共享的时间
        :type Users: list of UserInfoRsp
        """
        self.Status = None
        self.WithMe = None
        self.BeginDate = None
        self.EndDate = None
        self.Users = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.WithMe = params.get("WithMe")
        self.BeginDate = params.get("BeginDate")
        self.EndDate = params.get("EndDate")
        if params.get("Users") is not None:
            self.Users = []
            for item in params.get("Users"):
                obj = UserInfoRsp()
                obj._deserialize(item)
                self.Users.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceStatusInfo(AbstractModel):
    """获取用户工作空间返回信息

    """

    def __init__(self):
        r"""
        :param Id: 空间ID
        :type Id: int
        :param Name: 空间名称
        :type Name: str
        :param Owner: 所属人
        :type Owner: :class:`tencentcloud.cloudstudio.v20210524.models.UserInfoRsp`
        :param SpaceKey: 空间标识
        :type SpaceKey: str
        :param Status: 状态
        :type Status: str
        :param LastOpsDate: 最后操作时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastOpsDate: str
        :param Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param Share: 共享状态
        :type Share: :class:`tencentcloud.cloudstudio.v20210524.models.WorkspaceShareInfo`
        :param WorkspaceType: 空间类型
        :type WorkspaceType: str
        :param Label: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param WorkspaceVersion: 空间版本
        :type WorkspaceVersion: int
        :param ImageIcon: 图标地址
        :type ImageIcon: str
        :param CreateDate: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateDate: str
        :param VersionControlUrl: 版本控制地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlUrl: str
        :param VersionControlDesc: 版本控制描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlDesc: str
        :param VersionControlRef: 版本控制引用
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRef: str
        :param VersionControlRefType: 版本控制引用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRefType: str
        :param VersionControlType: 版本控制类型
        :type VersionControlType: str
        :param TemplateId: 模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: int
        :param SnapshotUid: 快照ID
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotUid: str
        :param SpecDesc: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecDesc: str
        :param Cpu: CPU数量
注意：此字段可能返回 null，表示取不到有效值。
        :type Cpu: int
        :param Memory: 内存
注意：此字段可能返回 null，表示取不到有效值。
        :type Memory: int
        """
        self.Id = None
        self.Name = None
        self.Owner = None
        self.SpaceKey = None
        self.Status = None
        self.LastOpsDate = None
        self.Description = None
        self.Share = None
        self.WorkspaceType = None
        self.Label = None
        self.WorkspaceVersion = None
        self.ImageIcon = None
        self.CreateDate = None
        self.VersionControlUrl = None
        self.VersionControlDesc = None
        self.VersionControlRef = None
        self.VersionControlRefType = None
        self.VersionControlType = None
        self.TemplateId = None
        self.SnapshotUid = None
        self.SpecDesc = None
        self.Cpu = None
        self.Memory = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        if params.get("Owner") is not None:
            self.Owner = UserInfoRsp()
            self.Owner._deserialize(params.get("Owner"))
        self.SpaceKey = params.get("SpaceKey")
        self.Status = params.get("Status")
        self.LastOpsDate = params.get("LastOpsDate")
        self.Description = params.get("Description")
        if params.get("Share") is not None:
            self.Share = WorkspaceShareInfo()
            self.Share._deserialize(params.get("Share"))
        self.WorkspaceType = params.get("WorkspaceType")
        self.Label = params.get("Label")
        self.WorkspaceVersion = params.get("WorkspaceVersion")
        self.ImageIcon = params.get("ImageIcon")
        self.CreateDate = params.get("CreateDate")
        self.VersionControlUrl = params.get("VersionControlUrl")
        self.VersionControlDesc = params.get("VersionControlDesc")
        self.VersionControlRef = params.get("VersionControlRef")
        self.VersionControlRefType = params.get("VersionControlRefType")
        self.VersionControlType = params.get("VersionControlType")
        self.TemplateId = params.get("TemplateId")
        self.SnapshotUid = params.get("SnapshotUid")
        self.SpecDesc = params.get("SpecDesc")
        self.Cpu = params.get("Cpu")
        self.Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WorkspaceTemplateInfo(AbstractModel):
    """工作空间模板信息

    """

    def __init__(self):
        r"""
        :param Id: 模板ID
        :type Id: int
        :param Category: 模板分类
        :type Category: str
        :param Name: 模板名称
        :type Name: str
        :param Description: 模板描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param DescriptionEN: 中文描述
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionEN: str
        :param Tags: 模板标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: str
        :param Icon: 模板图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Icon: str
        :param VersionControlType: 默认仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlType: str
        :param VersionControlUrl: 默认仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlUrl: str
        :param VersionControlDesc: 默认仓库描述
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlDesc: str
        :param VersionControlOwner: 默认仓库所属人
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlOwner: str
        :param VersionControlRef: 默认仓库引用地址
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRef: str
        :param VersionControlRefType: 默认仓库引用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionControlRefType: str
        :param UserVersionControlUrl: 用户自定义仓库地址
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVersionControlUrl: str
        :param UserVersionControlType: 用户自定义仓库类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVersionControlType: str
        :param UserVersionControlRef: 用户自定义仓库引用
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVersionControlRef: str
        :param UserVersionControlRefType: 用户自定义仓库引用类型
注意：此字段可能返回 null，表示取不到有效值。
        :type UserVersionControlRefType: str
        :param DevFile: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type DevFile: str
        :param PluginFile: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type PluginFile: str
        :param PrebuildFile: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type PrebuildFile: str
        :param Marked: 是否标记
        :type Marked: bool
        :param MarkAt: 标记状态
        :type MarkAt: int
        :param CreateDate: 创建时间
        :type CreateDate: str
        :param LastModified: 最后修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastModified: str
        :param Sort: 编号
        :type Sort: int
        :param SnapshotUid: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type SnapshotUid: str
        :param UserId: 用户ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UserId: int
        :param Author: 用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type Author: str
        :param Me: 是否属于当前用户
        :type Me: bool
        :param AuthorAvatar: xxx
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorAvatar: str
        """
        self.Id = None
        self.Category = None
        self.Name = None
        self.Description = None
        self.DescriptionEN = None
        self.Tags = None
        self.Icon = None
        self.VersionControlType = None
        self.VersionControlUrl = None
        self.VersionControlDesc = None
        self.VersionControlOwner = None
        self.VersionControlRef = None
        self.VersionControlRefType = None
        self.UserVersionControlUrl = None
        self.UserVersionControlType = None
        self.UserVersionControlRef = None
        self.UserVersionControlRefType = None
        self.DevFile = None
        self.PluginFile = None
        self.PrebuildFile = None
        self.Marked = None
        self.MarkAt = None
        self.CreateDate = None
        self.LastModified = None
        self.Sort = None
        self.SnapshotUid = None
        self.UserId = None
        self.Author = None
        self.Me = None
        self.AuthorAvatar = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Category = params.get("Category")
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        self.DescriptionEN = params.get("DescriptionEN")
        self.Tags = params.get("Tags")
        self.Icon = params.get("Icon")
        self.VersionControlType = params.get("VersionControlType")
        self.VersionControlUrl = params.get("VersionControlUrl")
        self.VersionControlDesc = params.get("VersionControlDesc")
        self.VersionControlOwner = params.get("VersionControlOwner")
        self.VersionControlRef = params.get("VersionControlRef")
        self.VersionControlRefType = params.get("VersionControlRefType")
        self.UserVersionControlUrl = params.get("UserVersionControlUrl")
        self.UserVersionControlType = params.get("UserVersionControlType")
        self.UserVersionControlRef = params.get("UserVersionControlRef")
        self.UserVersionControlRefType = params.get("UserVersionControlRefType")
        self.DevFile = params.get("DevFile")
        self.PluginFile = params.get("PluginFile")
        self.PrebuildFile = params.get("PrebuildFile")
        self.Marked = params.get("Marked")
        self.MarkAt = params.get("MarkAt")
        self.CreateDate = params.get("CreateDate")
        self.LastModified = params.get("LastModified")
        self.Sort = params.get("Sort")
        self.SnapshotUid = params.get("SnapshotUid")
        self.UserId = params.get("UserId")
        self.Author = params.get("Author")
        self.Me = params.get("Me")
        self.AuthorAvatar = params.get("AuthorAvatar")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        