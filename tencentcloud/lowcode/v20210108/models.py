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


class AppJobInfo(AbstractModel):
    r"""安装应用，任务详情

    """

    def __init__(self):
        r"""
        :param _Status: 状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _Step: 当前步骤
注意：此字段可能返回 null，表示取不到有效值。
        :type Step: int
        :param _Id: 任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _TotalStep: 任务总共步骤数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalStep: int
        :param _StepDesc: 当前步骤详情
        :type StepDesc: str
        :param _ErrMsg: 错误信息
        :type ErrMsg: str
        """
        self._Status = None
        self._Step = None
        self._Id = None
        self._TotalStep = None
        self._StepDesc = None
        self._ErrMsg = None

    @property
    def Status(self):
        r"""状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Step(self):
        r"""当前步骤
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step

    @property
    def Id(self):
        r"""任务id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def TotalStep(self):
        r"""任务总共步骤数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalStep

    @TotalStep.setter
    def TotalStep(self, TotalStep):
        self._TotalStep = TotalStep

    @property
    def StepDesc(self):
        r"""当前步骤详情
        :rtype: str
        """
        return self._StepDesc

    @StepDesc.setter
    def StepDesc(self, StepDesc):
        self._StepDesc = StepDesc

    @property
    def ErrMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Step = params.get("Step")
        self._Id = params.get("Id")
        self._TotalStep = params.get("TotalStep")
        self._StepDesc = params.get("StepDesc")
        self._ErrMsg = params.get("ErrMsg")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDeployAppRequest(AbstractModel):
    r"""CheckDeployApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Id: 应用id
        :type Id: str
        :param _BuildId: 构建 Id
        :type BuildId: str
        """
        self._EnvId = None
        self._Id = None
        self._BuildId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Id(self):
        r"""应用id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BuildId(self):
        r"""构建 Id
        :rtype: str
        """
        return self._BuildId

    @BuildId.setter
    def BuildId(self, BuildId):
        self._BuildId = BuildId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Id = params.get("Id")
        self._BuildId = params.get("BuildId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDeployAppResponse(AbstractModel):
    r"""CheckDeployApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态：success、building、reviewFail、releaseSuccess、underReview
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""状态：success、building、reviewFail、releaseSuccess、underReview
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        self._RequestId = params.get("RequestId")


class CreateKnowledgeSetRequest(AbstractModel):
    r"""CreateKnowledgeSet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Name: 知识库标识
        :type Name: str
        :param _Title: 知识库名称
        :type Title: str
        :param _Desc: 描述
        :type Desc: str
        :param _Meta: 知识库的meta信息
        :type Meta: str
        """
        self._EnvId = None
        self._Name = None
        self._Title = None
        self._Desc = None
        self._Meta = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        r"""知识库标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        r"""知识库名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Desc(self):
        r"""描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Meta(self):
        r"""知识库的meta信息
        :rtype: str
        """
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Desc = params.get("Desc")
        self._Meta = params.get("Meta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateKnowledgeSetResponse(AbstractModel):
    r"""CreateKnowledgeSet返回参数结构体

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


class DataSourceDetail(AbstractModel):
    r"""数据源详情列表

    """

    def __init__(self):
        r"""
        :param _Id: 数据源 ID
        :type Id: str
        :param _Title: 数据源名称
        :type Title: str
        :param _Name: 数据源标识
        :type Name: str
        :param _Type: 数据源类型
        :type Type: str
        :param _Description: 数据源描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Schema: 数据源配置
        :type Schema: str
        :param _CmsProject: cms 项目状态, 0: 重新获取详情信息，1： 不需要重新获取详情信息
        :type CmsProject: str
        :param _PkgId: 当前为环境 id
        :type PkgId: str
        :param _SchemaVersion: schema 版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaVersion: str
        :param _CreatorId: 创建者用户 ID
        :type CreatorId: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _EnvId: 环境 id
        :type EnvId: str
        :param _DataSourceVersion: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceVersion: str
        :param _AppUsageList: 所属应用数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUsageList: list of DataSourceLinkApp
        :param _PublishedAt: 发布时间
        :type PublishedAt: str
        :param _ChildDataSourceIds: 子数据源ids
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildDataSourceIds: list of str
        :param _Fun: 数据源发布信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Fun: str
        :param _ScfStatus: 云函数状态 1 Active 2 Creating 3 Updating 4 Deleting  9 Deleted 11 CreatFailed  12 UpdateFailed 13 DeleteFailed 21 UpdateTimeOut
        :type ScfStatus: int
        :param _Methods: 自定义方法
        :type Methods: str
        :param _ChildDataSourceNames: 子数据源名数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildDataSourceNames: list of str
        :param _IsNewDataSource: 是否旧数据源 1 新 0 旧
        :type IsNewDataSource: int
        :param _ViewId: 数据源视图id
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewId: str
        :param _Configuration: 数据源属性配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Configuration: str
        :param _TemplateCode: 外部数据源模板code
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateCode: str
        :param _Source: 外部数据源模板来源 0 空模板 1 腾讯文档 2 腾讯会议 3 企业微信 4 微信电商
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param _PublishVersion: 发布版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishVersion: str
        :param _PublishViewId: 发布视图id
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishViewId: str
        :param _SubType: 数据源子类型   "database" 标准模型 "custom-database" 自定义模型 "system" 系统模型 "connector" 连接器 "custom-connector" 自定义连接器 "hidden" 隐藏数据源
        :type SubType: str
        :param _AuthStatus: 授权状态  0 授权无效 1 授权有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthStatus: int
        :param _AuthInfo: 数据源授权信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthInfo: :class:`tencentcloud.lowcode.v20210108.models.TicketAuthInfo`
        :param _PublishStatus: 1发布0未发布
        :type PublishStatus: int
        :param _UpdateVersion: 更新版本
        :type UpdateVersion: int
        :param _RelationFieldList: 模型关联关系字段列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationFieldList: list of RelationField
        :param _DbInstanceType: db实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DbInstanceType: str
        :param _PreviewTableName: 体验环境db表名
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewTableName: str
        :param _PublishedTableName: 正式环境db表名
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishedTableName: str
        :param _DbSourceType: DB来源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DbSourceType: str
        """
        self._Id = None
        self._Title = None
        self._Name = None
        self._Type = None
        self._Description = None
        self._Schema = None
        self._CmsProject = None
        self._PkgId = None
        self._SchemaVersion = None
        self._CreatorId = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._EnvId = None
        self._DataSourceVersion = None
        self._AppUsageList = None
        self._PublishedAt = None
        self._ChildDataSourceIds = None
        self._Fun = None
        self._ScfStatus = None
        self._Methods = None
        self._ChildDataSourceNames = None
        self._IsNewDataSource = None
        self._ViewId = None
        self._Configuration = None
        self._TemplateCode = None
        self._Source = None
        self._PublishVersion = None
        self._PublishViewId = None
        self._SubType = None
        self._AuthStatus = None
        self._AuthInfo = None
        self._PublishStatus = None
        self._UpdateVersion = None
        self._RelationFieldList = None
        self._DbInstanceType = None
        self._PreviewTableName = None
        self._PublishedTableName = None
        self._DbSourceType = None

    @property
    def Id(self):
        r"""数据源 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Title(self):
        r"""数据源名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Name(self):
        r"""数据源标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        r"""数据源类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        r"""数据源描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Schema(self):
        r"""数据源配置
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def CmsProject(self):
        r"""cms 项目状态, 0: 重新获取详情信息，1： 不需要重新获取详情信息
        :rtype: str
        """
        return self._CmsProject

    @CmsProject.setter
    def CmsProject(self, CmsProject):
        self._CmsProject = CmsProject

    @property
    def PkgId(self):
        r"""当前为环境 id
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def SchemaVersion(self):
        r"""schema 版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SchemaVersion

    @SchemaVersion.setter
    def SchemaVersion(self, SchemaVersion):
        self._SchemaVersion = SchemaVersion

    @property
    def CreatorId(self):
        r"""创建者用户 ID
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def CreatedAt(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def EnvId(self):
        r"""环境 id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DataSourceVersion(self):
        r"""版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataSourceVersion

    @DataSourceVersion.setter
    def DataSourceVersion(self, DataSourceVersion):
        self._DataSourceVersion = DataSourceVersion

    @property
    def AppUsageList(self):
        r"""所属应用数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DataSourceLinkApp
        """
        return self._AppUsageList

    @AppUsageList.setter
    def AppUsageList(self, AppUsageList):
        self._AppUsageList = AppUsageList

    @property
    def PublishedAt(self):
        r"""发布时间
        :rtype: str
        """
        return self._PublishedAt

    @PublishedAt.setter
    def PublishedAt(self, PublishedAt):
        self._PublishedAt = PublishedAt

    @property
    def ChildDataSourceIds(self):
        r"""子数据源ids
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ChildDataSourceIds

    @ChildDataSourceIds.setter
    def ChildDataSourceIds(self, ChildDataSourceIds):
        self._ChildDataSourceIds = ChildDataSourceIds

    @property
    def Fun(self):
        r"""数据源发布信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Fun

    @Fun.setter
    def Fun(self, Fun):
        self._Fun = Fun

    @property
    def ScfStatus(self):
        r"""云函数状态 1 Active 2 Creating 3 Updating 4 Deleting  9 Deleted 11 CreatFailed  12 UpdateFailed 13 DeleteFailed 21 UpdateTimeOut
        :rtype: int
        """
        return self._ScfStatus

    @ScfStatus.setter
    def ScfStatus(self, ScfStatus):
        self._ScfStatus = ScfStatus

    @property
    def Methods(self):
        r"""自定义方法
        :rtype: str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def ChildDataSourceNames(self):
        r"""子数据源名数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ChildDataSourceNames

    @ChildDataSourceNames.setter
    def ChildDataSourceNames(self, ChildDataSourceNames):
        self._ChildDataSourceNames = ChildDataSourceNames

    @property
    def IsNewDataSource(self):
        r"""是否旧数据源 1 新 0 旧
        :rtype: int
        """
        return self._IsNewDataSource

    @IsNewDataSource.setter
    def IsNewDataSource(self, IsNewDataSource):
        self._IsNewDataSource = IsNewDataSource

    @property
    def ViewId(self):
        r"""数据源视图id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ViewId

    @ViewId.setter
    def ViewId(self, ViewId):
        self._ViewId = ViewId

    @property
    def Configuration(self):
        r"""数据源属性配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def TemplateCode(self):
        r"""外部数据源模板code
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TemplateCode

    @TemplateCode.setter
    def TemplateCode(self, TemplateCode):
        self._TemplateCode = TemplateCode

    @property
    def Source(self):
        r"""外部数据源模板来源 0 空模板 1 腾讯文档 2 腾讯会议 3 企业微信 4 微信电商
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def PublishVersion(self):
        warnings.warn("parameter `PublishVersion` is deprecated", DeprecationWarning) 

        r"""发布版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublishVersion

    @PublishVersion.setter
    def PublishVersion(self, PublishVersion):
        warnings.warn("parameter `PublishVersion` is deprecated", DeprecationWarning) 

        self._PublishVersion = PublishVersion

    @property
    def PublishViewId(self):
        r"""发布视图id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublishViewId

    @PublishViewId.setter
    def PublishViewId(self, PublishViewId):
        self._PublishViewId = PublishViewId

    @property
    def SubType(self):
        r"""数据源子类型   "database" 标准模型 "custom-database" 自定义模型 "system" 系统模型 "connector" 连接器 "custom-connector" 自定义连接器 "hidden" 隐藏数据源
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def AuthStatus(self):
        r"""授权状态  0 授权无效 1 授权有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def AuthInfo(self):
        r"""数据源授权信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.TicketAuthInfo`
        """
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

    @property
    def PublishStatus(self):
        r"""1发布0未发布
        :rtype: int
        """
        return self._PublishStatus

    @PublishStatus.setter
    def PublishStatus(self, PublishStatus):
        self._PublishStatus = PublishStatus

    @property
    def UpdateVersion(self):
        r"""更新版本
        :rtype: int
        """
        return self._UpdateVersion

    @UpdateVersion.setter
    def UpdateVersion(self, UpdateVersion):
        self._UpdateVersion = UpdateVersion

    @property
    def RelationFieldList(self):
        r"""模型关联关系字段列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RelationField
        """
        return self._RelationFieldList

    @RelationFieldList.setter
    def RelationFieldList(self, RelationFieldList):
        self._RelationFieldList = RelationFieldList

    @property
    def DbInstanceType(self):
        r"""db实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DbInstanceType

    @DbInstanceType.setter
    def DbInstanceType(self, DbInstanceType):
        self._DbInstanceType = DbInstanceType

    @property
    def PreviewTableName(self):
        r"""体验环境db表名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PreviewTableName

    @PreviewTableName.setter
    def PreviewTableName(self, PreviewTableName):
        self._PreviewTableName = PreviewTableName

    @property
    def PublishedTableName(self):
        r"""正式环境db表名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublishedTableName

    @PublishedTableName.setter
    def PublishedTableName(self, PublishedTableName):
        self._PublishedTableName = PublishedTableName

    @property
    def DbSourceType(self):
        r"""DB来源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DbSourceType

    @DbSourceType.setter
    def DbSourceType(self, DbSourceType):
        self._DbSourceType = DbSourceType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Title = params.get("Title")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._Description = params.get("Description")
        self._Schema = params.get("Schema")
        self._CmsProject = params.get("CmsProject")
        self._PkgId = params.get("PkgId")
        self._SchemaVersion = params.get("SchemaVersion")
        self._CreatorId = params.get("CreatorId")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._EnvId = params.get("EnvId")
        self._DataSourceVersion = params.get("DataSourceVersion")
        if params.get("AppUsageList") is not None:
            self._AppUsageList = []
            for item in params.get("AppUsageList"):
                obj = DataSourceLinkApp()
                obj._deserialize(item)
                self._AppUsageList.append(obj)
        self._PublishedAt = params.get("PublishedAt")
        self._ChildDataSourceIds = params.get("ChildDataSourceIds")
        self._Fun = params.get("Fun")
        self._ScfStatus = params.get("ScfStatus")
        self._Methods = params.get("Methods")
        self._ChildDataSourceNames = params.get("ChildDataSourceNames")
        self._IsNewDataSource = params.get("IsNewDataSource")
        self._ViewId = params.get("ViewId")
        self._Configuration = params.get("Configuration")
        self._TemplateCode = params.get("TemplateCode")
        self._Source = params.get("Source")
        self._PublishVersion = params.get("PublishVersion")
        self._PublishViewId = params.get("PublishViewId")
        self._SubType = params.get("SubType")
        self._AuthStatus = params.get("AuthStatus")
        if params.get("AuthInfo") is not None:
            self._AuthInfo = TicketAuthInfo()
            self._AuthInfo._deserialize(params.get("AuthInfo"))
        self._PublishStatus = params.get("PublishStatus")
        self._UpdateVersion = params.get("UpdateVersion")
        if params.get("RelationFieldList") is not None:
            self._RelationFieldList = []
            for item in params.get("RelationFieldList"):
                obj = RelationField()
                obj._deserialize(item)
                self._RelationFieldList.append(obj)
        self._DbInstanceType = params.get("DbInstanceType")
        self._PreviewTableName = params.get("PreviewTableName")
        self._PublishedTableName = params.get("PublishedTableName")
        self._DbSourceType = params.get("DbSourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceDetailItems(AbstractModel):
    r"""数据详情列表

    """

    def __init__(self):
        r"""
        :param _Rows: 数据详情列表
        :type Rows: list of DataSourceDetail
        :param _Count: 数据源列表总个数
        :type Count: int
        """
        self._Rows = None
        self._Count = None

    @property
    def Rows(self):
        r"""数据详情列表
        :rtype: list of DataSourceDetail
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Count(self):
        r"""数据源列表总个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = DataSourceDetail()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceLinkApp(AbstractModel):
    r"""数据源关联App信息

    """

    def __init__(self):
        r"""
        :param _Id: 应用Id
        :type Id: str
        :param _Title: 应用名称
        :type Title: str
        :param _EditStatusUse: 是否编辑状态使用
        :type EditStatusUse: int
        :param _PreviewStatusUse: 是否预览状态使用
        :type PreviewStatusUse: int
        :param _OnlineStatusUse: 是否正式状态使用
        :type OnlineStatusUse: int
        :param _DataSourceId: 数据源ID
        :type DataSourceId: str
        """
        self._Id = None
        self._Title = None
        self._EditStatusUse = None
        self._PreviewStatusUse = None
        self._OnlineStatusUse = None
        self._DataSourceId = None

    @property
    def Id(self):
        r"""应用Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Title(self):
        r"""应用名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def EditStatusUse(self):
        r"""是否编辑状态使用
        :rtype: int
        """
        return self._EditStatusUse

    @EditStatusUse.setter
    def EditStatusUse(self, EditStatusUse):
        self._EditStatusUse = EditStatusUse

    @property
    def PreviewStatusUse(self):
        r"""是否预览状态使用
        :rtype: int
        """
        return self._PreviewStatusUse

    @PreviewStatusUse.setter
    def PreviewStatusUse(self, PreviewStatusUse):
        self._PreviewStatusUse = PreviewStatusUse

    @property
    def OnlineStatusUse(self):
        r"""是否正式状态使用
        :rtype: int
        """
        return self._OnlineStatusUse

    @OnlineStatusUse.setter
    def OnlineStatusUse(self, OnlineStatusUse):
        self._OnlineStatusUse = OnlineStatusUse

    @property
    def DataSourceId(self):
        r"""数据源ID
        :rtype: str
        """
        return self._DataSourceId

    @DataSourceId.setter
    def DataSourceId(self, DataSourceId):
        self._DataSourceId = DataSourceId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Title = params.get("Title")
        self._EditStatusUse = params.get("EditStatusUse")
        self._PreviewStatusUse = params.get("PreviewStatusUse")
        self._OnlineStatusUse = params.get("OnlineStatusUse")
        self._DataSourceId = params.get("DataSourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceQueryOption(AbstractModel):
    r"""数据源模糊查询参数

    """

    def __init__(self):
        r"""
        :param _LikeName: 数据源标识模糊匹配
        :type LikeName: str
        :param _LikeTitle: 数据源名称模糊匹配
        :type LikeTitle: str
        """
        self._LikeName = None
        self._LikeTitle = None

    @property
    def LikeName(self):
        r"""数据源标识模糊匹配
        :rtype: str
        """
        return self._LikeName

    @LikeName.setter
    def LikeName(self, LikeName):
        self._LikeName = LikeName

    @property
    def LikeTitle(self):
        r"""数据源名称模糊匹配
        :rtype: str
        """
        return self._LikeTitle

    @LikeTitle.setter
    def LikeTitle(self, LikeTitle):
        self._LikeTitle = LikeTitle


    def _deserialize(self, params):
        self._LikeName = params.get("LikeName")
        self._LikeTitle = params.get("LikeTitle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppBindWxAppRequest(AbstractModel):
    r"""DeleteAppBindWxApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WeappId: 应用id
        :type WeappId: str
        """
        self._WeappId = None

    @property
    def WeappId(self):
        r"""应用id
        :rtype: str
        """
        return self._WeappId

    @WeappId.setter
    def WeappId(self, WeappId):
        self._WeappId = WeappId


    def _deserialize(self, params):
        self._WeappId = params.get("WeappId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAppBindWxAppResponse(AbstractModel):
    r"""DeleteAppBindWxApp返回参数结构体

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


class DeleteKnowledgeDocumentSetRequest(AbstractModel):
    r"""DeleteKnowledgeDocumentSet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CollectionView: 知识库标识
        :type CollectionView: str
        :param _Query: 删除时制定的条件
        :type Query: :class:`tencentcloud.lowcode.v20210108.models.DocumentQuery`
        """
        self._EnvId = None
        self._CollectionView = None
        self._Query = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        r"""知识库标识
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def Query(self):
        r"""删除时制定的条件
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DocumentQuery`
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionView = params.get("CollectionView")
        if params.get("Query") is not None:
            self._Query = DocumentQuery()
            self._Query._deserialize(params.get("Query"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKnowledgeDocumentSetResponse(AbstractModel):
    r"""DeleteKnowledgeDocumentSet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 新增文件返回信息
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.DeleteKnowledgeDocumentSetRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""新增文件返回信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DeleteKnowledgeDocumentSetRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteKnowledgeDocumentSetRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteKnowledgeDocumentSetRsp(AbstractModel):
    r"""删除文档出参

    """

    def __init__(self):
        r"""
        :param _AffectedCount: 删除文档数量。
        :type AffectedCount: int
        """
        self._AffectedCount = None

    @property
    def AffectedCount(self):
        r"""删除文档数量。
        :rtype: int
        """
        return self._AffectedCount

    @AffectedCount.setter
    def AffectedCount(self, AffectedCount):
        self._AffectedCount = AffectedCount


    def _deserialize(self, params):
        self._AffectedCount = params.get("AffectedCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKnowledgeSetRequest(AbstractModel):
    r"""DeleteKnowledgeSet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Name: 知识库标识
        :type Name: str
        """
        self._EnvId = None
        self._Name = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        r"""知识库标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKnowledgeSetResponse(AbstractModel):
    r"""DeleteKnowledgeSet返回参数结构体

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


class DeployAppRequest(AbstractModel):
    r"""DeployApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Id: 应用id
        :type Id: str
        :param _Mode: 发布体验preview/正式upload
        :type Mode: str
        :param _BuildType: 构建类型：mp、pc、web、adminPortal
        :type BuildType: str
        :param _SubAppIds: 子包数组
        :type SubAppIds: list of str
        """
        self._EnvId = None
        self._Id = None
        self._Mode = None
        self._BuildType = None
        self._SubAppIds = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Id(self):
        r"""应用id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Mode(self):
        r"""发布体验preview/正式upload
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def BuildType(self):
        r"""构建类型：mp、pc、web、adminPortal
        :rtype: str
        """
        return self._BuildType

    @BuildType.setter
    def BuildType(self, BuildType):
        self._BuildType = BuildType

    @property
    def SubAppIds(self):
        r"""子包数组
        :rtype: list of str
        """
        return self._SubAppIds

    @SubAppIds.setter
    def SubAppIds(self, SubAppIds):
        self._SubAppIds = SubAppIds


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Id = params.get("Id")
        self._Mode = params.get("Mode")
        self._BuildType = params.get("BuildType")
        self._SubAppIds = params.get("SubAppIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployAppResponse(AbstractModel):
    r"""DeployApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BuildId: 构建id
        :type BuildId: str
        :param _DeployErrCode: 发布错误code
        :type DeployErrCode: int
        :param _DeployErrMsg: 发布错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployErrMsg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BuildId = None
        self._DeployErrCode = None
        self._DeployErrMsg = None
        self._RequestId = None

    @property
    def BuildId(self):
        r"""构建id
        :rtype: str
        """
        return self._BuildId

    @BuildId.setter
    def BuildId(self, BuildId):
        self._BuildId = BuildId

    @property
    def DeployErrCode(self):
        r"""发布错误code
        :rtype: int
        """
        return self._DeployErrCode

    @DeployErrCode.setter
    def DeployErrCode(self, DeployErrCode):
        self._DeployErrCode = DeployErrCode

    @property
    def DeployErrMsg(self):
        r"""发布错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeployErrMsg

    @DeployErrMsg.setter
    def DeployErrMsg(self, DeployErrMsg):
        self._DeployErrMsg = DeployErrMsg

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
        self._BuildId = params.get("BuildId")
        self._DeployErrCode = params.get("DeployErrCode")
        self._DeployErrMsg = params.get("DeployErrMsg")
        self._RequestId = params.get("RequestId")


class DescribeAppsRequest(AbstractModel):
    r"""DescribeApps请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页每页个数
        :type Limit: int
        :param _Offset: 分页Offset
        :type Offset: int
        :param _EnvId: 环境id
        :type EnvId: str
        :param _Keyword: 搜索关键词
        :type Keyword: str
        :param _AppIds: 应用id
        :type AppIds: list of str
        :param _Channel: 来源类型
        :type Channel: str
        :param _Type: 1-自定义应用；2-模型应用
        :type Type: int
        :param _Favorite: 应用是否收藏
        :type Favorite: bool
        """
        self._Limit = None
        self._Offset = None
        self._EnvId = None
        self._Keyword = None
        self._AppIds = None
        self._Channel = None
        self._Type = None
        self._Favorite = None

    @property
    def Limit(self):
        r"""分页每页个数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页Offset
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Keyword(self):
        r"""搜索关键词
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def AppIds(self):
        r"""应用id
        :rtype: list of str
        """
        return self._AppIds

    @AppIds.setter
    def AppIds(self, AppIds):
        self._AppIds = AppIds

    @property
    def Channel(self):
        r"""来源类型
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Type(self):
        r"""1-自定义应用；2-模型应用
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Favorite(self):
        r"""应用是否收藏
        :rtype: bool
        """
        return self._Favorite

    @Favorite.setter
    def Favorite(self, Favorite):
        self._Favorite = Favorite


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._EnvId = params.get("EnvId")
        self._Keyword = params.get("Keyword")
        self._AppIds = params.get("AppIds")
        self._Channel = params.get("Channel")
        self._Type = params.get("Type")
        self._Favorite = params.get("Favorite")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAppsResponse(AbstractModel):
    r"""DescribeApps返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Weapps: 应用列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Weapps: list of Weapp
        :param _Count: 应用个数
注意：此字段可能返回 null，表示取不到有效值。
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Weapps = None
        self._Count = None
        self._RequestId = None

    @property
    def Weapps(self):
        r"""应用列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Weapp
        """
        return self._Weapps

    @Weapps.setter
    def Weapps(self, Weapps):
        self._Weapps = Weapps

    @property
    def Count(self):
        r"""应用个数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

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
        if params.get("Weapps") is not None:
            self._Weapps = []
            for item in params.get("Weapps"):
                obj = Weapp()
                obj._deserialize(item)
                self._Weapps.append(obj)
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeDataSourceListRequest(AbstractModel):
    r"""DescribeDataSourceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页条数
        :type PageSize: int
        :param _PageIndex: 页码
        :type PageIndex: int
        :param _EnvId: 环境 id
        :type EnvId: str
        :param _Appids: 应用id数组
        :type Appids: list of str
        :param _DataSourceIds: 数据源id数组
        :type DataSourceIds: list of str
        :param _DataSourceNames: 数据源名称数组
        :type DataSourceNames: list of str
        :param _DataSourceType: 数据源类型 database-自建数据源；cloud-integration-自定义数据源
        :type DataSourceType: str
        :param _QueryOption: 数据源模糊查询参数
        :type QueryOption: :class:`tencentcloud.lowcode.v20210108.models.DataSourceQueryOption`
        :param _ViewIds: 数据源视图Id数组
        :type ViewIds: list of str
        :param _AppLinkStatus: 查询未关联应用的数据源，0:未关联，该参数配合 AppIds 参数一块使用
        :type AppLinkStatus: int
        :param _QueryBindToApp: 查询应用绑定数据源: 0: 否,1: 是
        :type QueryBindToApp: int
        :param _QueryConnector: 查询连接器 0 数据模型 1 连接器 2 自定义连接器
        :type QueryConnector: int
        :param _NotQuerySubTypeList: 废弃中
        :type NotQuerySubTypeList: list of str
        :param _ChannelList: 查询channelList
        :type ChannelList: list of str
        :param _QueryDataSourceRelationList: 是否查询数据源关联关系
        :type QueryDataSourceRelationList: bool
        :param _DbInstanceType: db实例类型
        :type DbInstanceType: str
        :param _DatabaseTableNames: 数据库表名列表
        :type DatabaseTableNames: list of str
        :param _QuerySystemModel: 是否查询系统模型，默认为true，需要显示设置为False才能过滤系统模型
        :type QuerySystemModel: bool
        """
        self._PageSize = None
        self._PageIndex = None
        self._EnvId = None
        self._Appids = None
        self._DataSourceIds = None
        self._DataSourceNames = None
        self._DataSourceType = None
        self._QueryOption = None
        self._ViewIds = None
        self._AppLinkStatus = None
        self._QueryBindToApp = None
        self._QueryConnector = None
        self._NotQuerySubTypeList = None
        self._ChannelList = None
        self._QueryDataSourceRelationList = None
        self._DbInstanceType = None
        self._DatabaseTableNames = None
        self._QuerySystemModel = None

    @property
    def PageSize(self):
        r"""每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageIndex(self):
        r"""页码
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def EnvId(self):
        r"""环境 id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Appids(self):
        r"""应用id数组
        :rtype: list of str
        """
        return self._Appids

    @Appids.setter
    def Appids(self, Appids):
        self._Appids = Appids

    @property
    def DataSourceIds(self):
        r"""数据源id数组
        :rtype: list of str
        """
        return self._DataSourceIds

    @DataSourceIds.setter
    def DataSourceIds(self, DataSourceIds):
        self._DataSourceIds = DataSourceIds

    @property
    def DataSourceNames(self):
        r"""数据源名称数组
        :rtype: list of str
        """
        return self._DataSourceNames

    @DataSourceNames.setter
    def DataSourceNames(self, DataSourceNames):
        self._DataSourceNames = DataSourceNames

    @property
    def DataSourceType(self):
        r"""数据源类型 database-自建数据源；cloud-integration-自定义数据源
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def QueryOption(self):
        r"""数据源模糊查询参数
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DataSourceQueryOption`
        """
        return self._QueryOption

    @QueryOption.setter
    def QueryOption(self, QueryOption):
        self._QueryOption = QueryOption

    @property
    def ViewIds(self):
        r"""数据源视图Id数组
        :rtype: list of str
        """
        return self._ViewIds

    @ViewIds.setter
    def ViewIds(self, ViewIds):
        self._ViewIds = ViewIds

    @property
    def AppLinkStatus(self):
        r"""查询未关联应用的数据源，0:未关联，该参数配合 AppIds 参数一块使用
        :rtype: int
        """
        return self._AppLinkStatus

    @AppLinkStatus.setter
    def AppLinkStatus(self, AppLinkStatus):
        self._AppLinkStatus = AppLinkStatus

    @property
    def QueryBindToApp(self):
        r"""查询应用绑定数据源: 0: 否,1: 是
        :rtype: int
        """
        return self._QueryBindToApp

    @QueryBindToApp.setter
    def QueryBindToApp(self, QueryBindToApp):
        self._QueryBindToApp = QueryBindToApp

    @property
    def QueryConnector(self):
        r"""查询连接器 0 数据模型 1 连接器 2 自定义连接器
        :rtype: int
        """
        return self._QueryConnector

    @QueryConnector.setter
    def QueryConnector(self, QueryConnector):
        self._QueryConnector = QueryConnector

    @property
    def NotQuerySubTypeList(self):
        r"""废弃中
        :rtype: list of str
        """
        return self._NotQuerySubTypeList

    @NotQuerySubTypeList.setter
    def NotQuerySubTypeList(self, NotQuerySubTypeList):
        self._NotQuerySubTypeList = NotQuerySubTypeList

    @property
    def ChannelList(self):
        r"""查询channelList
        :rtype: list of str
        """
        return self._ChannelList

    @ChannelList.setter
    def ChannelList(self, ChannelList):
        self._ChannelList = ChannelList

    @property
    def QueryDataSourceRelationList(self):
        r"""是否查询数据源关联关系
        :rtype: bool
        """
        return self._QueryDataSourceRelationList

    @QueryDataSourceRelationList.setter
    def QueryDataSourceRelationList(self, QueryDataSourceRelationList):
        self._QueryDataSourceRelationList = QueryDataSourceRelationList

    @property
    def DbInstanceType(self):
        r"""db实例类型
        :rtype: str
        """
        return self._DbInstanceType

    @DbInstanceType.setter
    def DbInstanceType(self, DbInstanceType):
        self._DbInstanceType = DbInstanceType

    @property
    def DatabaseTableNames(self):
        r"""数据库表名列表
        :rtype: list of str
        """
        return self._DatabaseTableNames

    @DatabaseTableNames.setter
    def DatabaseTableNames(self, DatabaseTableNames):
        self._DatabaseTableNames = DatabaseTableNames

    @property
    def QuerySystemModel(self):
        r"""是否查询系统模型，默认为true，需要显示设置为False才能过滤系统模型
        :rtype: bool
        """
        return self._QuerySystemModel

    @QuerySystemModel.setter
    def QuerySystemModel(self, QuerySystemModel):
        self._QuerySystemModel = QuerySystemModel


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageIndex = params.get("PageIndex")
        self._EnvId = params.get("EnvId")
        self._Appids = params.get("Appids")
        self._DataSourceIds = params.get("DataSourceIds")
        self._DataSourceNames = params.get("DataSourceNames")
        self._DataSourceType = params.get("DataSourceType")
        if params.get("QueryOption") is not None:
            self._QueryOption = DataSourceQueryOption()
            self._QueryOption._deserialize(params.get("QueryOption"))
        self._ViewIds = params.get("ViewIds")
        self._AppLinkStatus = params.get("AppLinkStatus")
        self._QueryBindToApp = params.get("QueryBindToApp")
        self._QueryConnector = params.get("QueryConnector")
        self._NotQuerySubTypeList = params.get("NotQuerySubTypeList")
        self._ChannelList = params.get("ChannelList")
        self._QueryDataSourceRelationList = params.get("QueryDataSourceRelationList")
        self._DbInstanceType = params.get("DbInstanceType")
        self._DatabaseTableNames = params.get("DatabaseTableNames")
        self._QuerySystemModel = params.get("QuerySystemModel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSourceListResponse(AbstractModel):
    r"""DescribeDataSourceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: data 数据
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.DataSourceDetailItems`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""data 数据
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DataSourceDetailItems`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DataSourceDetailItems()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeDocumentSetDetailRequest(AbstractModel):
    r"""DescribeKnowledgeDocumentSetDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CollectionView: 知识库标识
        :type CollectionView: str
        :param _DocumentSetName: 文件名
        :type DocumentSetName: str
        :param _DocumentSetId: 文件id
        :type DocumentSetId: str
        """
        self._EnvId = None
        self._CollectionView = None
        self._DocumentSetName = None
        self._DocumentSetId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        r"""知识库标识
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def DocumentSetName(self):
        r"""文件名
        :rtype: str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def DocumentSetId(self):
        r"""文件id
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionView = params.get("CollectionView")
        self._DocumentSetName = params.get("DocumentSetName")
        self._DocumentSetId = params.get("DocumentSetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKnowledgeDocumentSetDetailResponse(AbstractModel):
    r"""DescribeKnowledgeDocumentSetDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 新增文件返回信息
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetDetailRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""新增文件返回信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetDetailRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeKnowledgeDocumentSetDetailRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeDocumentSetDetailRsp(AbstractModel):
    r"""上传知识库文档返回结果

    """

    def __init__(self):
        r"""
        :param _Count: 获取的数量。
        :type Count: int
        :param _DocumentSet: 文档信息
        :type DocumentSet: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeDocumentSet`
        """
        self._Count = None
        self._DocumentSet = None

    @property
    def Count(self):
        r"""获取的数量。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DocumentSet(self):
        r"""文档信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeDocumentSet`
        """
        return self._DocumentSet

    @DocumentSet.setter
    def DocumentSet(self, DocumentSet):
        self._DocumentSet = DocumentSet


    def _deserialize(self, params):
        self._Count = params.get("Count")
        if params.get("DocumentSet") is not None:
            self._DocumentSet = KnowledgeDocumentSet()
            self._DocumentSet._deserialize(params.get("DocumentSet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKnowledgeDocumentSetListRequest(AbstractModel):
    r"""DescribeKnowledgeDocumentSetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CollectionView: 知识库标识
        :type CollectionView: str
        :param _Query: 查询条件
        :type Query: :class:`tencentcloud.lowcode.v20210108.models.PageQuery`
        """
        self._EnvId = None
        self._CollectionView = None
        self._Query = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        r"""知识库标识
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def Query(self):
        r"""查询条件
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.PageQuery`
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionView = params.get("CollectionView")
        if params.get("Query") is not None:
            self._Query = PageQuery()
            self._Query._deserialize(params.get("Query"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKnowledgeDocumentSetListResponse(AbstractModel):
    r"""DescribeKnowledgeDocumentSetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 新增文件返回信息
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetListRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""新增文件返回信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetListRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeKnowledgeDocumentSetListRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeDocumentSetListRsp(AbstractModel):
    r"""删除文档出参

    """

    def __init__(self):
        r"""
        :param _DocumentSets: 文件集
        :type DocumentSets: list of QureyKnowledgeDocumentSet
        :param _Count: 条数
        :type Count: int
        """
        self._DocumentSets = None
        self._Count = None

    @property
    def DocumentSets(self):
        r"""文件集
        :rtype: list of QureyKnowledgeDocumentSet
        """
        return self._DocumentSets

    @DocumentSets.setter
    def DocumentSets(self, DocumentSets):
        self._DocumentSets = DocumentSets

    @property
    def Count(self):
        r"""条数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count


    def _deserialize(self, params):
        if params.get("DocumentSets") is not None:
            self._DocumentSets = []
            for item in params.get("DocumentSets"):
                obj = QureyKnowledgeDocumentSet()
                obj._deserialize(item)
                self._DocumentSets.append(obj)
        self._Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKnowledgeSetListRequest(AbstractModel):
    r"""DescribeKnowledgeSetList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Name: 知识库标识，精准查询
        :type Name: str
        :param _Title: 知识库名称，精准查询
        :type Title: str
        :param _Offset: 分页起始位
        :type Offset: int
        :param _Limit: 查询条数
        :type Limit: int
        :param _QueryMode: NoPage标识不分页
        :type QueryMode: str
        """
        self._EnvId = None
        self._Name = None
        self._Title = None
        self._Offset = None
        self._Limit = None
        self._QueryMode = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        r"""知识库标识，精准查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        r"""知识库名称，精准查询
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Offset(self):
        r"""分页起始位
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""查询条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QueryMode(self):
        r"""NoPage标识不分页
        :rtype: str
        """
        return self._QueryMode

    @QueryMode.setter
    def QueryMode(self, QueryMode):
        self._QueryMode = QueryMode


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._QueryMode = params.get("QueryMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeKnowledgeSetListResponse(AbstractModel):
    r"""DescribeKnowledgeSetList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 知识库列表
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSetRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""知识库列表
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSetRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = KnowledgeSetRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeRelatedUsersRequest(AbstractModel):
    r"""DescribeRelatedUsers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RoleId: 角色id
        :type RoleId: int
        :param _EnvId: 环境id
        :type EnvId: str
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 页面含量
        :type PageSize: int
        :param _EnvType: 环境类型
        :type EnvType: str
        """
        self._RoleId = None
        self._EnvId = None
        self._PageNo = None
        self._PageSize = None
        self._EnvType = None

    @property
    def RoleId(self):
        r"""角色id
        :rtype: int
        """
        return self._RoleId

    @RoleId.setter
    def RoleId(self, RoleId):
        self._RoleId = RoleId

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def PageNo(self):
        r"""页码
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        r"""页面含量
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def EnvType(self):
        r"""环境类型
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType


    def _deserialize(self, params):
        self._RoleId = params.get("RoleId")
        self._EnvId = params.get("EnvId")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        self._EnvType = params.get("EnvType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelatedUsersResponse(AbstractModel):
    r"""DescribeRelatedUsers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 关联的用户列表
        :type Data: list of WedaUser
        :param _Total: 总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Total = None
        self._RequestId = None

    @property
    def Data(self):
        r"""关联的用户列表
        :rtype: list of WedaUser
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Total(self):
        r"""总数
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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = WedaUser()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeResourceRoleListRequest(AbstractModel):
    r"""DescribeResourceRoleList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源id
        :type ResourceId: str
        :param _ResourceType: 资源类型
        :type ResourceType: str
        :param _EnvType: 预览：pre；非预览：prod
        :type EnvType: str
        :param _EnvId: 环境id
        :type EnvId: str
        :param _SubType: 子资源类型
        :type SubType: str
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 分页大小
        :type PageSize: int
        """
        self._ResourceId = None
        self._ResourceType = None
        self._EnvType = None
        self._EnvId = None
        self._SubType = None
        self._PageNo = None
        self._PageSize = None

    @property
    def ResourceId(self):
        r"""资源id
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def EnvType(self):
        r"""预览：pre；非预览：prod
        :rtype: str
        """
        return self._EnvType

    @EnvType.setter
    def EnvType(self, EnvType):
        self._EnvType = EnvType

    @property
    def EnvId(self):
        r"""环境id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def SubType(self):
        r"""子资源类型
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def PageNo(self):
        r"""页码
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        r"""分页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._EnvType = params.get("EnvType")
        self._EnvId = params.get("EnvId")
        self._SubType = params.get("SubType")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceRoleListResponse(AbstractModel):
    r"""DescribeResourceRoleList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 角色列表
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.RoleListPage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""角色列表
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.RoleListPage`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = RoleListPage()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DocumentQuery(AbstractModel):
    r"""删除文档时查询入参

    """

    def __init__(self):
        r"""
        :param _DocumentSetId: 文件ids
        :type DocumentSetId: list of str
        :param _DocumentSetName: 文件名集合
        :type DocumentSetName: list of str
        :param _Filter: 使用创建 CollectionView 指定的 Filter 索引的字段设置查询过滤表达式
        :type Filter: str
        """
        self._DocumentSetId = None
        self._DocumentSetName = None
        self._Filter = None

    @property
    def DocumentSetId(self):
        r"""文件ids
        :rtype: list of str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        r"""文件名集合
        :rtype: list of str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def Filter(self):
        r"""使用创建 CollectionView 指定的 Filter 索引的字段设置查询过滤表达式
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._DocumentSetId = params.get("DocumentSetId")
        self._DocumentSetName = params.get("DocumentSetName")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeDocumentSet(AbstractModel):
    r"""文档信息

    """

    def __init__(self):
        r"""
        :param _DocumentSetId: 文档id
        :type DocumentSetId: str
        :param _DocumentSetName: 文档名
        :type DocumentSetName: str
        :param _Text: 文件完整内容。
        :type Text: str
        :param _TextPrefix: 文件内容前 200个字符。
        :type TextPrefix: str
        :param _DocumentSetInfo: 文件详情
        :type DocumentSetInfo: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeDocumentSetInfo`
        :param _SplitterPreprocess: 文件拆分信息
        :type SplitterPreprocess: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSplitterPreprocess`
        :param _Name: 未使用
        :type Name: str
        :param _FileTitle: 文档标题
        :type FileTitle: str
        :param _FileMetaData: 文档元信息，必须为jsonstring
        :type FileMetaData: str
        :param _Author: 作者
        :type Author: str
        :param _DocStatus: 上传文件状态
        :type DocStatus: str
        :param _ErrMsg: 文件上传失败的具体原因
        :type ErrMsg: str
        :param _FileId: Cos存储文件ID
        :type FileId: str
        """
        self._DocumentSetId = None
        self._DocumentSetName = None
        self._Text = None
        self._TextPrefix = None
        self._DocumentSetInfo = None
        self._SplitterPreprocess = None
        self._Name = None
        self._FileTitle = None
        self._FileMetaData = None
        self._Author = None
        self._DocStatus = None
        self._ErrMsg = None
        self._FileId = None

    @property
    def DocumentSetId(self):
        r"""文档id
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        r"""文档名
        :rtype: str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def Text(self):
        r"""文件完整内容。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TextPrefix(self):
        r"""文件内容前 200个字符。
        :rtype: str
        """
        return self._TextPrefix

    @TextPrefix.setter
    def TextPrefix(self, TextPrefix):
        self._TextPrefix = TextPrefix

    @property
    def DocumentSetInfo(self):
        r"""文件详情
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeDocumentSetInfo`
        """
        return self._DocumentSetInfo

    @DocumentSetInfo.setter
    def DocumentSetInfo(self, DocumentSetInfo):
        self._DocumentSetInfo = DocumentSetInfo

    @property
    def SplitterPreprocess(self):
        r"""文件拆分信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSplitterPreprocess`
        """
        return self._SplitterPreprocess

    @SplitterPreprocess.setter
    def SplitterPreprocess(self, SplitterPreprocess):
        self._SplitterPreprocess = SplitterPreprocess

    @property
    def Name(self):
        r"""未使用
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FileTitle(self):
        r"""文档标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        r"""文档元信息，必须为jsonstring
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def Author(self):
        r"""作者
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def DocStatus(self):
        r"""上传文件状态
        :rtype: str
        """
        return self._DocStatus

    @DocStatus.setter
    def DocStatus(self, DocStatus):
        self._DocStatus = DocStatus

    @property
    def ErrMsg(self):
        r"""文件上传失败的具体原因
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def FileId(self):
        r"""Cos存储文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._DocumentSetId = params.get("DocumentSetId")
        self._DocumentSetName = params.get("DocumentSetName")
        self._Text = params.get("Text")
        self._TextPrefix = params.get("TextPrefix")
        if params.get("DocumentSetInfo") is not None:
            self._DocumentSetInfo = KnowledgeDocumentSetInfo()
            self._DocumentSetInfo._deserialize(params.get("DocumentSetInfo"))
        if params.get("SplitterPreprocess") is not None:
            self._SplitterPreprocess = KnowledgeSplitterPreprocess()
            self._SplitterPreprocess._deserialize(params.get("SplitterPreprocess"))
        self._Name = params.get("Name")
        self._FileTitle = params.get("FileTitle")
        self._FileMetaData = params.get("FileMetaData")
        self._Author = params.get("Author")
        self._DocStatus = params.get("DocStatus")
        self._ErrMsg = params.get("ErrMsg")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeDocumentSetInfo(AbstractModel):
    r"""文档信息

    """

    def __init__(self):
        r"""
        :param _TextLength: 文件的字符数。
        :type TextLength: int
        :param _ByteLength: 文件的字节数。
        :type ByteLength: int
        :param _IndexedProgress: 文件被预处理、Embedding 向量化的进度。
        :type IndexedProgress: int
        :param _IndexedStatus: 文件预处理、Embedding 向量化的状态。
New：等待解析。
Loading：文件解析中。
Failure：文件解析、写入出错。
Ready：文件解析、写入完成。

        :type IndexedStatus: str
        :param _CreateTime: 文件创建时间。
        :type CreateTime: str
        :param _LastUpdateTime: 文件最后更新时间。
        :type LastUpdateTime: str
        :param _Keywords: 文件关键字。
        :type Keywords: str
        """
        self._TextLength = None
        self._ByteLength = None
        self._IndexedProgress = None
        self._IndexedStatus = None
        self._CreateTime = None
        self._LastUpdateTime = None
        self._Keywords = None

    @property
    def TextLength(self):
        r"""文件的字符数。
        :rtype: int
        """
        return self._TextLength

    @TextLength.setter
    def TextLength(self, TextLength):
        self._TextLength = TextLength

    @property
    def ByteLength(self):
        r"""文件的字节数。
        :rtype: int
        """
        return self._ByteLength

    @ByteLength.setter
    def ByteLength(self, ByteLength):
        self._ByteLength = ByteLength

    @property
    def IndexedProgress(self):
        r"""文件被预处理、Embedding 向量化的进度。
        :rtype: int
        """
        return self._IndexedProgress

    @IndexedProgress.setter
    def IndexedProgress(self, IndexedProgress):
        self._IndexedProgress = IndexedProgress

    @property
    def IndexedStatus(self):
        r"""文件预处理、Embedding 向量化的状态。
New：等待解析。
Loading：文件解析中。
Failure：文件解析、写入出错。
Ready：文件解析、写入完成。

        :rtype: str
        """
        return self._IndexedStatus

    @IndexedStatus.setter
    def IndexedStatus(self, IndexedStatus):
        self._IndexedStatus = IndexedStatus

    @property
    def CreateTime(self):
        r"""文件创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""文件最后更新时间。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Keywords(self):
        r"""文件关键字。
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords


    def _deserialize(self, params):
        self._TextLength = params.get("TextLength")
        self._ByteLength = params.get("ByteLength")
        self._IndexedProgress = params.get("IndexedProgress")
        self._IndexedStatus = params.get("IndexedStatus")
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeSet(AbstractModel):
    r"""知识库信息

    """

    def __init__(self):
        r"""
        :param _Name: 知识库标识
        :type Name: str
        :param _Title: 知识库名称
        :type Title: str
        :param _Desc: 描述
        :type Desc: str
        :param _Active: 状态，
NOT_ENABLED未启用
ENABLED 已启用
        :type Active: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Meta: 知识库的meta信息
        :type Meta: str
        :param _TotalSize: 知识库容量,单位字节
        :type TotalSize: str
        """
        self._Name = None
        self._Title = None
        self._Desc = None
        self._Active = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Meta = None
        self._TotalSize = None

    @property
    def Name(self):
        r"""知识库标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        r"""知识库名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Desc(self):
        r"""描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Active(self):
        r"""状态，
NOT_ENABLED未启用
ENABLED 已启用
        :rtype: str
        """
        return self._Active

    @Active.setter
    def Active(self, Active):
        self._Active = Active

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
    def Meta(self):
        r"""知识库的meta信息
        :rtype: str
        """
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta

    @property
    def TotalSize(self):
        r"""知识库容量,单位字节
        :rtype: str
        """
        return self._TotalSize

    @TotalSize.setter
    def TotalSize(self, TotalSize):
        self._TotalSize = TotalSize


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Desc = params.get("Desc")
        self._Active = params.get("Active")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Meta = params.get("Meta")
        self._TotalSize = params.get("TotalSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeSetRsp(AbstractModel):
    r"""查询知识库列表返回

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _KnowledgeSets: 知识库列表
        :type KnowledgeSets: list of KnowledgeSet
        """
        self._Total = None
        self._KnowledgeSets = None

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def KnowledgeSets(self):
        r"""知识库列表
        :rtype: list of KnowledgeSet
        """
        return self._KnowledgeSets

    @KnowledgeSets.setter
    def KnowledgeSets(self, KnowledgeSets):
        self._KnowledgeSets = KnowledgeSets


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("KnowledgeSets") is not None:
            self._KnowledgeSets = []
            for item in params.get("KnowledgeSets"):
                obj = KnowledgeSet()
                obj._deserialize(item)
                self._KnowledgeSets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KnowledgeSplitterPreprocess(AbstractModel):
    r"""文件拆分信息

    """

    def __init__(self):
        r"""
        :param _AppendTitleToChunk: 在对文件拆分时，配置是否将 Title 追加到切分后的段落后面一并 Embedding。取值如下所示：
false：不追加。
true：将段落 Title 追加到切分后的段落。

        :type AppendTitleToChunk: bool
        :param _AppendKeywordsToChunk: 在对文件拆分时，配置是否将关键字 keywords 追加到切分后的段落一并 Embedding。取值如下所示：
false：不追加。
true：将全文的 keywords 追加到切分后的段落。

        :type AppendKeywordsToChunk: bool
        """
        self._AppendTitleToChunk = None
        self._AppendKeywordsToChunk = None

    @property
    def AppendTitleToChunk(self):
        r"""在对文件拆分时，配置是否将 Title 追加到切分后的段落后面一并 Embedding。取值如下所示：
false：不追加。
true：将段落 Title 追加到切分后的段落。

        :rtype: bool
        """
        return self._AppendTitleToChunk

    @AppendTitleToChunk.setter
    def AppendTitleToChunk(self, AppendTitleToChunk):
        self._AppendTitleToChunk = AppendTitleToChunk

    @property
    def AppendKeywordsToChunk(self):
        r"""在对文件拆分时，配置是否将关键字 keywords 追加到切分后的段落一并 Embedding。取值如下所示：
false：不追加。
true：将全文的 keywords 追加到切分后的段落。

        :rtype: bool
        """
        return self._AppendKeywordsToChunk

    @AppendKeywordsToChunk.setter
    def AppendKeywordsToChunk(self, AppendKeywordsToChunk):
        self._AppendKeywordsToChunk = AppendKeywordsToChunk


    def _deserialize(self, params):
        self._AppendTitleToChunk = params.get("AppendTitleToChunk")
        self._AppendKeywordsToChunk = params.get("AppendKeywordsToChunk")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrgResp(AbstractModel):
    r"""组织架构返回参数

    """

    def __init__(self):
        r"""
        :param _OrgId: 部门id
        :type OrgId: str
        :param _OrgName: 部门名称
        :type OrgName: str
        :param _OrgIdentity: 部门标识
        :type OrgIdentity: str
        :param _Level: 部门层级
        :type Level: str
        :param _PrimaryColumn: 主键字段
        :type PrimaryColumn: str
        """
        self._OrgId = None
        self._OrgName = None
        self._OrgIdentity = None
        self._Level = None
        self._PrimaryColumn = None

    @property
    def OrgId(self):
        r"""部门id
        :rtype: str
        """
        return self._OrgId

    @OrgId.setter
    def OrgId(self, OrgId):
        self._OrgId = OrgId

    @property
    def OrgName(self):
        r"""部门名称
        :rtype: str
        """
        return self._OrgName

    @OrgName.setter
    def OrgName(self, OrgName):
        self._OrgName = OrgName

    @property
    def OrgIdentity(self):
        r"""部门标识
        :rtype: str
        """
        return self._OrgIdentity

    @OrgIdentity.setter
    def OrgIdentity(self, OrgIdentity):
        self._OrgIdentity = OrgIdentity

    @property
    def Level(self):
        r"""部门层级
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def PrimaryColumn(self):
        r"""主键字段
        :rtype: str
        """
        return self._PrimaryColumn

    @PrimaryColumn.setter
    def PrimaryColumn(self, PrimaryColumn):
        self._PrimaryColumn = PrimaryColumn


    def _deserialize(self, params):
        self._OrgId = params.get("OrgId")
        self._OrgName = params.get("OrgName")
        self._OrgIdentity = params.get("OrgIdentity")
        self._Level = params.get("Level")
        self._PrimaryColumn = params.get("PrimaryColumn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PageQuery(AbstractModel):
    r"""查询条件

    """

    def __init__(self):
        r"""
        :param _DocumentSetId: 文件id数组，表示要查询的文件的所有 ID，支持批量查询，数组元素范围[1,20]。
        :type DocumentSetId: list of str
        :param _DocumentSetName: 表示要查询的文档名称，支持批量查询，数组元素范围[1,20]。
        :type DocumentSetName: list of str
        :param _Limit: 取值范围：[1,16384]
        :type Limit: int
        :param _Offset: 设置分页偏移量，用于控制分页查询返回结果的起始位置，方便用户对数据进行分页展示和浏览。
取值：为 limit 整数倍。
计算公式：offset=limit*(page-1)。
例如：当 limit = 10，page = 2 时，分页偏移量 offset = 10 * (2 - 1) = 10，表示从查询结果的第 11 条记录开始返回数据。

        :type Offset: int
        :param _OutputFields: 设置后，其他字段为空值
        :type OutputFields: list of str
        :param _Filter: 使用创建 CollectionView 指定的 Filter 索引的字段设置查询过滤表达式。
        :type Filter: str
        """
        self._DocumentSetId = None
        self._DocumentSetName = None
        self._Limit = None
        self._Offset = None
        self._OutputFields = None
        self._Filter = None

    @property
    def DocumentSetId(self):
        r"""文件id数组，表示要查询的文件的所有 ID，支持批量查询，数组元素范围[1,20]。
        :rtype: list of str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        r"""表示要查询的文档名称，支持批量查询，数组元素范围[1,20]。
        :rtype: list of str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def Limit(self):
        r"""取值范围：[1,16384]
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""设置分页偏移量，用于控制分页查询返回结果的起始位置，方便用户对数据进行分页展示和浏览。
取值：为 limit 整数倍。
计算公式：offset=limit*(page-1)。
例如：当 limit = 10，page = 2 时，分页偏移量 offset = 10 * (2 - 1) = 10，表示从查询结果的第 11 条记录开始返回数据。

        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OutputFields(self):
        r"""设置后，其他字段为空值
        :rtype: list of str
        """
        return self._OutputFields

    @OutputFields.setter
    def OutputFields(self, OutputFields):
        self._OutputFields = OutputFields

    @property
    def Filter(self):
        r"""使用创建 CollectionView 指定的 Filter 索引的字段设置查询过滤表达式。
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter


    def _deserialize(self, params):
        self._DocumentSetId = params.get("DocumentSetId")
        self._DocumentSetName = params.get("DocumentSetName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OutputFields = params.get("OutputFields")
        self._Filter = params.get("Filter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutWxAppIdToWeAppRequest(AbstractModel):
    r"""PutWxAppIdToWeApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WeAppId: 应用ID
        :type WeAppId: str
        :param _WxAppId: 微信AppId
        :type WxAppId: str
        """
        self._WeAppId = None
        self._WxAppId = None

    @property
    def WeAppId(self):
        r"""应用ID
        :rtype: str
        """
        return self._WeAppId

    @WeAppId.setter
    def WeAppId(self, WeAppId):
        self._WeAppId = WeAppId

    @property
    def WxAppId(self):
        r"""微信AppId
        :rtype: str
        """
        return self._WxAppId

    @WxAppId.setter
    def WxAppId(self, WxAppId):
        self._WxAppId = WxAppId


    def _deserialize(self, params):
        self._WeAppId = params.get("WeAppId")
        self._WxAppId = params.get("WxAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PutWxAppIdToWeAppResponse(AbstractModel):
    r"""PutWxAppIdToWeApp返回参数结构体

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


class QureyKnowledgeDocumentSet(AbstractModel):
    r"""搜索数据的集合

    """

    def __init__(self):
        r"""
        :param _DocumentSetId: 文件id
        :type DocumentSetId: str
        :param _DocumentSetName: 文件名
        :type DocumentSetName: str
        :param _TextPrefix: 文件内容前 200个字符。
        :type TextPrefix: str
        :param _SplitterPreprocess: 文件拆分信息
        :type SplitterPreprocess: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSplitterPreprocess`
        :param _DocumentSetInfo: 文件详情
        :type DocumentSetInfo: :class:`tencentcloud.lowcode.v20210108.models.QureyKnowledgeDocumentSetInfo`
        :param _FileTitle: 文件标题
        :type FileTitle: str
        :param _FileMetaData: 文件元信息，必须为jsonstring
        :type FileMetaData: str
        :param _Name: name
        :type Name: str
        :param _Author: 作者
        :type Author: str
        :param _DocStatus: 文档上传状态
        :type DocStatus: str
        :param _ErrMsg: 上传文件失败时具体的错误消息
        :type ErrMsg: str
        :param _FileId: Cos存储文件ID
        :type FileId: str
        """
        self._DocumentSetId = None
        self._DocumentSetName = None
        self._TextPrefix = None
        self._SplitterPreprocess = None
        self._DocumentSetInfo = None
        self._FileTitle = None
        self._FileMetaData = None
        self._Name = None
        self._Author = None
        self._DocStatus = None
        self._ErrMsg = None
        self._FileId = None

    @property
    def DocumentSetId(self):
        r"""文件id
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        r"""文件名
        :rtype: str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def TextPrefix(self):
        r"""文件内容前 200个字符。
        :rtype: str
        """
        return self._TextPrefix

    @TextPrefix.setter
    def TextPrefix(self, TextPrefix):
        self._TextPrefix = TextPrefix

    @property
    def SplitterPreprocess(self):
        r"""文件拆分信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSplitterPreprocess`
        """
        return self._SplitterPreprocess

    @SplitterPreprocess.setter
    def SplitterPreprocess(self, SplitterPreprocess):
        self._SplitterPreprocess = SplitterPreprocess

    @property
    def DocumentSetInfo(self):
        r"""文件详情
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.QureyKnowledgeDocumentSetInfo`
        """
        return self._DocumentSetInfo

    @DocumentSetInfo.setter
    def DocumentSetInfo(self, DocumentSetInfo):
        self._DocumentSetInfo = DocumentSetInfo

    @property
    def FileTitle(self):
        r"""文件标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        r"""文件元信息，必须为jsonstring
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def Name(self):
        r"""name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Author(self):
        r"""作者
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def DocStatus(self):
        r"""文档上传状态
        :rtype: str
        """
        return self._DocStatus

    @DocStatus.setter
    def DocStatus(self, DocStatus):
        self._DocStatus = DocStatus

    @property
    def ErrMsg(self):
        r"""上传文件失败时具体的错误消息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def FileId(self):
        r"""Cos存储文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._DocumentSetId = params.get("DocumentSetId")
        self._DocumentSetName = params.get("DocumentSetName")
        self._TextPrefix = params.get("TextPrefix")
        if params.get("SplitterPreprocess") is not None:
            self._SplitterPreprocess = KnowledgeSplitterPreprocess()
            self._SplitterPreprocess._deserialize(params.get("SplitterPreprocess"))
        if params.get("DocumentSetInfo") is not None:
            self._DocumentSetInfo = QureyKnowledgeDocumentSetInfo()
            self._DocumentSetInfo._deserialize(params.get("DocumentSetInfo"))
        self._FileTitle = params.get("FileTitle")
        self._FileMetaData = params.get("FileMetaData")
        self._Name = params.get("Name")
        self._Author = params.get("Author")
        self._DocStatus = params.get("DocStatus")
        self._ErrMsg = params.get("ErrMsg")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QureyKnowledgeDocumentSetInfo(AbstractModel):
    r"""查询文件集合信息详情

    """

    def __init__(self):
        r"""
        :param _TextLength: 文件的字符数。
        :type TextLength: int
        :param _ByteLength: 文件的字节数。
        :type ByteLength: int
        :param _IndexedProgress: 文件被预处理、Embedding 向量化的进度。
        :type IndexedProgress: int
        :param _IndexedStatus: 文件预处理、Embedding 向量化的状态。
New：等待解析。
Loading：文件解析中。
Failure：文件解析、写入出错。
Ready：文件解析、写入完成。

        :type IndexedStatus: str
        :param _IndexedErrorMsg: 错误信息
        :type IndexedErrorMsg: str
        :param _CreateTime: 文件创建时间。
        :type CreateTime: str
        :param _LastUpdateTime: 文件最后更新时间。
        :type LastUpdateTime: str
        :param _Keywords: 文件关键字。
        :type Keywords: str
        """
        self._TextLength = None
        self._ByteLength = None
        self._IndexedProgress = None
        self._IndexedStatus = None
        self._IndexedErrorMsg = None
        self._CreateTime = None
        self._LastUpdateTime = None
        self._Keywords = None

    @property
    def TextLength(self):
        r"""文件的字符数。
        :rtype: int
        """
        return self._TextLength

    @TextLength.setter
    def TextLength(self, TextLength):
        self._TextLength = TextLength

    @property
    def ByteLength(self):
        r"""文件的字节数。
        :rtype: int
        """
        return self._ByteLength

    @ByteLength.setter
    def ByteLength(self, ByteLength):
        self._ByteLength = ByteLength

    @property
    def IndexedProgress(self):
        r"""文件被预处理、Embedding 向量化的进度。
        :rtype: int
        """
        return self._IndexedProgress

    @IndexedProgress.setter
    def IndexedProgress(self, IndexedProgress):
        self._IndexedProgress = IndexedProgress

    @property
    def IndexedStatus(self):
        r"""文件预处理、Embedding 向量化的状态。
New：等待解析。
Loading：文件解析中。
Failure：文件解析、写入出错。
Ready：文件解析、写入完成。

        :rtype: str
        """
        return self._IndexedStatus

    @IndexedStatus.setter
    def IndexedStatus(self, IndexedStatus):
        self._IndexedStatus = IndexedStatus

    @property
    def IndexedErrorMsg(self):
        r"""错误信息
        :rtype: str
        """
        return self._IndexedErrorMsg

    @IndexedErrorMsg.setter
    def IndexedErrorMsg(self, IndexedErrorMsg):
        self._IndexedErrorMsg = IndexedErrorMsg

    @property
    def CreateTime(self):
        r"""文件创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        r"""文件最后更新时间。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Keywords(self):
        r"""文件关键字。
        :rtype: str
        """
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords


    def _deserialize(self, params):
        self._TextLength = params.get("TextLength")
        self._ByteLength = params.get("ByteLength")
        self._IndexedProgress = params.get("IndexedProgress")
        self._IndexedStatus = params.get("IndexedStatus")
        self._IndexedErrorMsg = params.get("IndexedErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._LastUpdateTime = params.get("LastUpdateTime")
        self._Keywords = params.get("Keywords")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelationField(AbstractModel):
    r"""数据源关联的的信息

    """

    def __init__(self):
        r"""
        :param _Field: 关联关系字段
        :type Field: str
        :param _Format: 关联关系格式
        :type Format: str
        :param _RelateDataSourceName: 关联数据源名称
        :type RelateDataSourceName: str
        """
        self._Field = None
        self._Format = None
        self._RelateDataSourceName = None

    @property
    def Field(self):
        r"""关联关系字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Format(self):
        r"""关联关系格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def RelateDataSourceName(self):
        r"""关联数据源名称
        :rtype: str
        """
        return self._RelateDataSourceName

    @RelateDataSourceName.setter
    def RelateDataSourceName(self, RelateDataSourceName):
        self._RelateDataSourceName = RelateDataSourceName


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Format = params.get("Format")
        self._RelateDataSourceName = params.get("RelateDataSourceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleGroup(AbstractModel):
    r"""权限组

    """

    def __init__(self):
        r"""
        :param _Id: 权限组id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Name: 权限组名称
        :type Name: str
        :param _GroupIdentity: 权限组标识
        :type GroupIdentity: str
        :param _GroupDesc: 权限组描述
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupDesc: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _RoleList: 角色数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleList: list of WedaRole
        """
        self._Id = None
        self._Name = None
        self._GroupIdentity = None
        self._GroupDesc = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RoleList = None

    @property
    def Id(self):
        r"""权限组id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        r"""权限组名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def GroupIdentity(self):
        r"""权限组标识
        :rtype: str
        """
        return self._GroupIdentity

    @GroupIdentity.setter
    def GroupIdentity(self, GroupIdentity):
        self._GroupIdentity = GroupIdentity

    @property
    def GroupDesc(self):
        r"""权限组描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._GroupDesc

    @GroupDesc.setter
    def GroupDesc(self, GroupDesc):
        self._GroupDesc = GroupDesc

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RoleList(self):
        r"""角色数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WedaRole
        """
        return self._RoleList

    @RoleList.setter
    def RoleList(self, RoleList):
        self._RoleList = RoleList


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._GroupIdentity = params.get("GroupIdentity")
        self._GroupDesc = params.get("GroupDesc")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("RoleList") is not None:
            self._RoleList = []
            for item in params.get("RoleList"):
                obj = WedaRole()
                obj._deserialize(item)
                self._RoleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RoleListPage(AbstractModel):
    r"""角色分页

    """

    def __init__(self):
        r"""
        :param _RoleList: 角色列表
        :type RoleList: list of WedaRole
        :param _Total: 总数
        :type Total: int
        """
        self._RoleList = None
        self._Total = None

    @property
    def RoleList(self):
        r"""角色列表
        :rtype: list of WedaRole
        """
        return self._RoleList

    @RoleList.setter
    def RoleList(self, RoleList):
        self._RoleList = RoleList

    @property
    def Total(self):
        r"""总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("RoleList") is not None:
            self._RoleList = []
            for item in params.get("RoleList"):
                obj = WedaRole()
                obj._deserialize(item)
                self._RoleList.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchDocInfo(AbstractModel):
    r"""知识库搜索文档信息

    """

    def __init__(self):
        r"""
        :param _CollectionViewName: 知识库名称
        :type CollectionViewName: str
        :param _DocSetId: 文档Id
        :type DocSetId: str
        :param _DocSetName: 文档Name
        :type DocSetName: str
        :param _DocType: 文档类型
        :type DocType: str
        :param _FileTitle: 文档标题
        :type FileTitle: str
        :param _FileMetaData: 文档元信息
        :type FileMetaData: str
        :param _DocDesc: 文档描述
        :type DocDesc: str
        :param _FileSize: 文档大小
        :type FileSize: int
        :param _FileId: Cos存储文件ID
        :type FileId: str
        """
        self._CollectionViewName = None
        self._DocSetId = None
        self._DocSetName = None
        self._DocType = None
        self._FileTitle = None
        self._FileMetaData = None
        self._DocDesc = None
        self._FileSize = None
        self._FileId = None

    @property
    def CollectionViewName(self):
        r"""知识库名称
        :rtype: str
        """
        return self._CollectionViewName

    @CollectionViewName.setter
    def CollectionViewName(self, CollectionViewName):
        self._CollectionViewName = CollectionViewName

    @property
    def DocSetId(self):
        r"""文档Id
        :rtype: str
        """
        return self._DocSetId

    @DocSetId.setter
    def DocSetId(self, DocSetId):
        self._DocSetId = DocSetId

    @property
    def DocSetName(self):
        r"""文档Name
        :rtype: str
        """
        return self._DocSetName

    @DocSetName.setter
    def DocSetName(self, DocSetName):
        self._DocSetName = DocSetName

    @property
    def DocType(self):
        r"""文档类型
        :rtype: str
        """
        return self._DocType

    @DocType.setter
    def DocType(self, DocType):
        self._DocType = DocType

    @property
    def FileTitle(self):
        r"""文档标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        r"""文档元信息
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def DocDesc(self):
        r"""文档描述
        :rtype: str
        """
        return self._DocDesc

    @DocDesc.setter
    def DocDesc(self, DocDesc):
        self._DocDesc = DocDesc

    @property
    def FileSize(self):
        r"""文档大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileId(self):
        r"""Cos存储文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._CollectionViewName = params.get("CollectionViewName")
        self._DocSetId = params.get("DocSetId")
        self._DocSetName = params.get("DocSetName")
        self._DocType = params.get("DocType")
        self._FileTitle = params.get("FileTitle")
        self._FileMetaData = params.get("FileMetaData")
        self._DocDesc = params.get("DocDesc")
        self._FileSize = params.get("FileSize")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchDocListRequest(AbstractModel):
    r"""SearchDocList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CollectionView: 知识库名称
        :type CollectionView: str
        :param _SearchKey: 搜索模式
        :type SearchKey: str
        :param _SearchValue: 搜索值
        :type SearchValue: str
        :param _PageNo: 页码
        :type PageNo: int
        :param _PageSize: 页大小
        :type PageSize: int
        """
        self._EnvId = None
        self._CollectionView = None
        self._SearchKey = None
        self._SearchValue = None
        self._PageNo = None
        self._PageSize = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        r"""知识库名称
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def SearchKey(self):
        r"""搜索模式
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def SearchValue(self):
        r"""搜索值
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def PageNo(self):
        r"""页码
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        r"""页大小
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionView = params.get("CollectionView")
        self._SearchKey = params.get("SearchKey")
        self._SearchValue = params.get("SearchValue")
        self._PageNo = params.get("PageNo")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchDocListResponse(AbstractModel):
    r"""SearchDocList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 知识库文档搜索数据
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.SearchDocRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""知识库文档搜索数据
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.SearchDocRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SearchDocRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SearchDocRsp(AbstractModel):
    r"""知识库文档搜索结果

    """

    def __init__(self):
        r"""
        :param _DocInfos: 文档基本信息
        :type DocInfos: list of SearchDocInfo
        :param _Total: 文档总数
        :type Total: int
        """
        self._DocInfos = None
        self._Total = None

    @property
    def DocInfos(self):
        r"""文档基本信息
        :rtype: list of SearchDocInfo
        """
        return self._DocInfos

    @DocInfos.setter
    def DocInfos(self, DocInfos):
        self._DocInfos = DocInfos

    @property
    def Total(self):
        r"""文档总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        if params.get("DocInfos") is not None:
            self._DocInfos = []
            for item in params.get("DocInfos"):
                obj = SearchDocInfo()
                obj._deserialize(item)
                self._DocInfos.append(obj)
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TicketAuthInfo(AbstractModel):
    r"""数据源授权信息

    """

    def __init__(self):
        r"""
        :param _AuthUser: 授权用户
        :type AuthUser: str
        """
        self._AuthUser = None

    @property
    def AuthUser(self):
        r"""授权用户
        :rtype: str
        """
        return self._AuthUser

    @AuthUser.setter
    def AuthUser(self, AuthUser):
        self._AuthUser = AuthUser


    def _deserialize(self, params):
        self._AuthUser = params.get("AuthUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateKnowledgeSetRequest(AbstractModel):
    r"""UpdateKnowledgeSet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _Name: 知识库标识
        :type Name: str
        :param _Title: 知识库名称
        :type Title: str
        :param _Desc: 描述
        :type Desc: str
        :param _Active: 状态;ENABLED启用；NOT_ENABLED不启用
        :type Active: str
        :param _Meta: 知识库的meta信息
        :type Meta: str
        """
        self._EnvId = None
        self._Name = None
        self._Title = None
        self._Desc = None
        self._Active = None
        self._Meta = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        r"""知识库标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        r"""知识库名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Desc(self):
        r"""描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Active(self):
        r"""状态;ENABLED启用；NOT_ENABLED不启用
        :rtype: str
        """
        return self._Active

    @Active.setter
    def Active(self, Active):
        self._Active = Active

    @property
    def Meta(self):
        r"""知识库的meta信息
        :rtype: str
        """
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._Name = params.get("Name")
        self._Title = params.get("Title")
        self._Desc = params.get("Desc")
        self._Active = params.get("Active")
        self._Meta = params.get("Meta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateKnowledgeSetResponse(AbstractModel):
    r"""UpdateKnowledgeSet返回参数结构体

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


class UploadKnowledgeDocumentSetRequest(AbstractModel):
    r"""UploadKnowledgeDocumentSet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EnvId: 环境ID
        :type EnvId: str
        :param _CollectionView: 知识库标识
        :type CollectionView: str
        :param _FileName: 状态;ENABLED启用；NOT_ENABLED不启用
        :type FileName: str
        :param _CosUrl: 腾讯云文件存储位置的可读地址
        :type CosUrl: str
        :param _DocumentType: 文件类型，例如: .docx, .md
        :type DocumentType: str
        :param _DocumentDesc: 对文件的描述
        :type DocumentDesc: str
        :param _FileTitle: 文件标题
        :type FileTitle: str
        :param _FileMetaData: 文件元信息，为jsonstring
        :type FileMetaData: str
        :param _DocumentSetId: 文件id
        :type DocumentSetId: str
        :param _Delimiter: 使用 regex 分割文档
        :type Delimiter: str
        :param _FileId: Cos存储文件ID
        :type FileId: str
        """
        self._EnvId = None
        self._CollectionView = None
        self._FileName = None
        self._CosUrl = None
        self._DocumentType = None
        self._DocumentDesc = None
        self._FileTitle = None
        self._FileMetaData = None
        self._DocumentSetId = None
        self._Delimiter = None
        self._FileId = None

    @property
    def EnvId(self):
        r"""环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        r"""知识库标识
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def FileName(self):
        r"""状态;ENABLED启用；NOT_ENABLED不启用
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CosUrl(self):
        r"""腾讯云文件存储位置的可读地址
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def DocumentType(self):
        r"""文件类型，例如: .docx, .md
        :rtype: str
        """
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentDesc(self):
        r"""对文件的描述
        :rtype: str
        """
        return self._DocumentDesc

    @DocumentDesc.setter
    def DocumentDesc(self, DocumentDesc):
        self._DocumentDesc = DocumentDesc

    @property
    def FileTitle(self):
        r"""文件标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        r"""文件元信息，为jsonstring
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def DocumentSetId(self):
        r"""文件id
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def Delimiter(self):
        r"""使用 regex 分割文档
        :rtype: str
        """
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def FileId(self):
        r"""Cos存储文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._EnvId = params.get("EnvId")
        self._CollectionView = params.get("CollectionView")
        self._FileName = params.get("FileName")
        self._CosUrl = params.get("CosUrl")
        self._DocumentType = params.get("DocumentType")
        self._DocumentDesc = params.get("DocumentDesc")
        self._FileTitle = params.get("FileTitle")
        self._FileMetaData = params.get("FileMetaData")
        self._DocumentSetId = params.get("DocumentSetId")
        self._Delimiter = params.get("Delimiter")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadKnowledgeDocumentSetResponse(AbstractModel):
    r"""UploadKnowledgeDocumentSet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 新增文件返回信息
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.UploadKnowledgeDocumentSetRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        r"""新增文件返回信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.UploadKnowledgeDocumentSetRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UploadKnowledgeDocumentSetRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UploadKnowledgeDocumentSetRsp(AbstractModel):
    r"""上传知识库文档返回结果

    """

    def __init__(self):
        r"""
        :param _DocumentSetId: 给文件分配的 ID 信息。
        :type DocumentSetId: str
        :param _DocumentSetName: 文件名
        :type DocumentSetName: str
        :param _FileTitle: 文件标题
        :type FileTitle: str
        :param _FileMetaData: 文件元信息，为jsonstring
        :type FileMetaData: str
        :param _FileId: Cos存储文件ID
        :type FileId: str
        """
        self._DocumentSetId = None
        self._DocumentSetName = None
        self._FileTitle = None
        self._FileMetaData = None
        self._FileId = None

    @property
    def DocumentSetId(self):
        warnings.warn("parameter `DocumentSetId` is deprecated", DeprecationWarning) 

        r"""给文件分配的 ID 信息。
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        warnings.warn("parameter `DocumentSetId` is deprecated", DeprecationWarning) 

        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        r"""文件名
        :rtype: str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def FileTitle(self):
        r"""文件标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        r"""文件元信息，为jsonstring
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def FileId(self):
        r"""Cos存储文件ID
        :rtype: str
        """
        return self._FileId

    @FileId.setter
    def FileId(self, FileId):
        self._FileId = FileId


    def _deserialize(self, params):
        self._DocumentSetId = params.get("DocumentSetId")
        self._DocumentSetName = params.get("DocumentSetName")
        self._FileTitle = params.get("FileTitle")
        self._FileMetaData = params.get("FileMetaData")
        self._FileId = params.get("FileId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Weapp(AbstractModel):
    r"""低码应用详情

    """

    def __init__(self):
        r"""
        :param _Id: 应用id
        :type Id: str
        :param _Owner: 应用所属者
注意：此字段可能返回 null，表示取不到有效值。
        :type Owner: str
        :param _Name: 标识
        :type Name: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Title: 应用名称
        :type Title: str
        :param _Env: 环境信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Env: str
        :param _Status: 状态.
0:已经安装
3:安装中
4:安装失败
        :type Status: int
        :param _EnvId: 环境信息
        :type EnvId: str
        :param _EnvRegion: 环境地域
        :type EnvRegion: str
        :param _PkgId: 资源包
        :type PkgId: str
        :param _CmsProject: 应用信息是否安装到cms
注意：此字段可能返回 null，表示取不到有效值。
        :type CmsProject: int
        :param _Channel: 渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: str
        :param _TemplateId: 模板id
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateId: str
        :param _ExpireTime: 过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Source: 来源
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _IsFree: 是否计费应用
        :type IsFree: bool
        :param _ContentType: 应用内容类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentType: str
        :param _AppType: 应用类型，是否为B端应用
注意：此字段可能返回 null，表示取不到有效值。
        :type AppType: int
        :param _AttachAppId: 关联B端一样id
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachAppId: str
        :param _EType: 应用类型，是否为企业应用
注意：此字段可能返回 null，表示取不到有效值。
        :type EType: int
        :param _EData: 企业应用数据
注意：此字段可能返回 null，表示取不到有效值。
        :type EData: str
        :param _LastMpCiId: 最新一次小程序构建id
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMpCiId: str
        :param _LastMpCiStatus: 最新一次小程序状态
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMpCiStatus: str
        :param _LastWebCiId: 最新一次web构建id
注意：此字段可能返回 null，表示取不到有效值。
        :type LastWebCiId: str
        :param _LastWebCiStatus: 最新一次web状态
注意：此字段可能返回 null，表示取不到有效值。
        :type LastWebCiStatus: str
        :param _LastDeployTime: 最新部署时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastDeployTime: str
        :param _FlowId: 安装任务id
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowId: int
        :param _JobInfo: 任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :type JobInfo: :class:`tencentcloud.lowcode.v20210108.models.AppJobInfo`
        :param _Platform: 应用端
注意：此字段可能返回 null，表示取不到有效值。
        :type Platform: str
        :param _LastWebCiMode: 最新一次web构建模式
注意：此字段可能返回 null，表示取不到有效值。
        :type LastWebCiMode: int
        :param _LastMpCiMode: 最新一次小程序构建模式
注意：此字段可能返回 null，表示取不到有效值。
        :type LastMpCiMode: int
        :param _SceneType: 应用场景化入口类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SceneType: str
        :param _ClientId: client_Id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        :param _IconUrl: 图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type IconUrl: str
        :param _FaviconUrl: 页面图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :type FaviconUrl: str
        :param _BackgroundColor: 图标背景色
注意：此字段可能返回 null，表示取不到有效值。
        :type BackgroundColor: str
        :param _Favorite: 应用是否收藏
        :type Favorite: bool
        :param _PublishPlatform: 发布平台：web、mp、pc、adminPortal、xPagePC、cloudAdmin
        :type PublishPlatform: str
        """
        self._Id = None
        self._Owner = None
        self._Name = None
        self._Description = None
        self._Title = None
        self._Env = None
        self._Status = None
        self._EnvId = None
        self._EnvRegion = None
        self._PkgId = None
        self._CmsProject = None
        self._Channel = None
        self._TemplateId = None
        self._ExpireTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Source = None
        self._IsFree = None
        self._ContentType = None
        self._AppType = None
        self._AttachAppId = None
        self._EType = None
        self._EData = None
        self._LastMpCiId = None
        self._LastMpCiStatus = None
        self._LastWebCiId = None
        self._LastWebCiStatus = None
        self._LastDeployTime = None
        self._FlowId = None
        self._JobInfo = None
        self._Platform = None
        self._LastWebCiMode = None
        self._LastMpCiMode = None
        self._SceneType = None
        self._ClientId = None
        self._IconUrl = None
        self._FaviconUrl = None
        self._BackgroundColor = None
        self._Favorite = None
        self._PublishPlatform = None

    @property
    def Id(self):
        r"""应用id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Owner(self):
        r"""应用所属者
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner

    @property
    def Name(self):
        r"""标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Title(self):
        r"""应用名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Env(self):
        r"""环境信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Status(self):
        r"""状态.
0:已经安装
3:安装中
4:安装失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EnvId(self):
        r"""环境信息
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def EnvRegion(self):
        r"""环境地域
        :rtype: str
        """
        return self._EnvRegion

    @EnvRegion.setter
    def EnvRegion(self, EnvRegion):
        self._EnvRegion = EnvRegion

    @property
    def PkgId(self):
        r"""资源包
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def CmsProject(self):
        r"""应用信息是否安装到cms
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CmsProject

    @CmsProject.setter
    def CmsProject(self, CmsProject):
        self._CmsProject = CmsProject

    @property
    def Channel(self):
        r"""渠道
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def TemplateId(self):
        r"""模板id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def ExpireTime(self):
        r"""过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

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
    def Source(self):
        r"""来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def IsFree(self):
        r"""是否计费应用
        :rtype: bool
        """
        return self._IsFree

    @IsFree.setter
    def IsFree(self, IsFree):
        self._IsFree = IsFree

    @property
    def ContentType(self):
        r"""应用内容类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def AppType(self):
        r"""应用类型，是否为B端应用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppType

    @AppType.setter
    def AppType(self, AppType):
        self._AppType = AppType

    @property
    def AttachAppId(self):
        r"""关联B端一样id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttachAppId

    @AttachAppId.setter
    def AttachAppId(self, AttachAppId):
        self._AttachAppId = AttachAppId

    @property
    def EType(self):
        r"""应用类型，是否为企业应用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._EType

    @EType.setter
    def EType(self, EType):
        self._EType = EType

    @property
    def EData(self):
        r"""企业应用数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EData

    @EData.setter
    def EData(self, EData):
        self._EData = EData

    @property
    def LastMpCiId(self):
        r"""最新一次小程序构建id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastMpCiId

    @LastMpCiId.setter
    def LastMpCiId(self, LastMpCiId):
        self._LastMpCiId = LastMpCiId

    @property
    def LastMpCiStatus(self):
        r"""最新一次小程序状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastMpCiStatus

    @LastMpCiStatus.setter
    def LastMpCiStatus(self, LastMpCiStatus):
        self._LastMpCiStatus = LastMpCiStatus

    @property
    def LastWebCiId(self):
        r"""最新一次web构建id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastWebCiId

    @LastWebCiId.setter
    def LastWebCiId(self, LastWebCiId):
        self._LastWebCiId = LastWebCiId

    @property
    def LastWebCiStatus(self):
        r"""最新一次web状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastWebCiStatus

    @LastWebCiStatus.setter
    def LastWebCiStatus(self, LastWebCiStatus):
        self._LastWebCiStatus = LastWebCiStatus

    @property
    def LastDeployTime(self):
        r"""最新部署时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastDeployTime

    @LastDeployTime.setter
    def LastDeployTime(self, LastDeployTime):
        self._LastDeployTime = LastDeployTime

    @property
    def FlowId(self):
        r"""安装任务id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def JobInfo(self):
        r"""任务详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.AppJobInfo`
        """
        return self._JobInfo

    @JobInfo.setter
    def JobInfo(self, JobInfo):
        self._JobInfo = JobInfo

    @property
    def Platform(self):
        r"""应用端
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def LastWebCiMode(self):
        r"""最新一次web构建模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastWebCiMode

    @LastWebCiMode.setter
    def LastWebCiMode(self, LastWebCiMode):
        self._LastWebCiMode = LastWebCiMode

    @property
    def LastMpCiMode(self):
        r"""最新一次小程序构建模式
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastMpCiMode

    @LastMpCiMode.setter
    def LastMpCiMode(self, LastMpCiMode):
        self._LastMpCiMode = LastMpCiMode

    @property
    def SceneType(self):
        r"""应用场景化入口类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SceneType

    @SceneType.setter
    def SceneType(self, SceneType):
        self._SceneType = SceneType

    @property
    def ClientId(self):
        r"""client_Id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def IconUrl(self):
        r"""图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IconUrl

    @IconUrl.setter
    def IconUrl(self, IconUrl):
        self._IconUrl = IconUrl

    @property
    def FaviconUrl(self):
        r"""页面图标地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FaviconUrl

    @FaviconUrl.setter
    def FaviconUrl(self, FaviconUrl):
        self._FaviconUrl = FaviconUrl

    @property
    def BackgroundColor(self):
        r"""图标背景色
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor):
        self._BackgroundColor = BackgroundColor

    @property
    def Favorite(self):
        r"""应用是否收藏
        :rtype: bool
        """
        return self._Favorite

    @Favorite.setter
    def Favorite(self, Favorite):
        self._Favorite = Favorite

    @property
    def PublishPlatform(self):
        r"""发布平台：web、mp、pc、adminPortal、xPagePC、cloudAdmin
        :rtype: str
        """
        return self._PublishPlatform

    @PublishPlatform.setter
    def PublishPlatform(self, PublishPlatform):
        self._PublishPlatform = PublishPlatform


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Owner = params.get("Owner")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Title = params.get("Title")
        self._Env = params.get("Env")
        self._Status = params.get("Status")
        self._EnvId = params.get("EnvId")
        self._EnvRegion = params.get("EnvRegion")
        self._PkgId = params.get("PkgId")
        self._CmsProject = params.get("CmsProject")
        self._Channel = params.get("Channel")
        self._TemplateId = params.get("TemplateId")
        self._ExpireTime = params.get("ExpireTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._Source = params.get("Source")
        self._IsFree = params.get("IsFree")
        self._ContentType = params.get("ContentType")
        self._AppType = params.get("AppType")
        self._AttachAppId = params.get("AttachAppId")
        self._EType = params.get("EType")
        self._EData = params.get("EData")
        self._LastMpCiId = params.get("LastMpCiId")
        self._LastMpCiStatus = params.get("LastMpCiStatus")
        self._LastWebCiId = params.get("LastWebCiId")
        self._LastWebCiStatus = params.get("LastWebCiStatus")
        self._LastDeployTime = params.get("LastDeployTime")
        self._FlowId = params.get("FlowId")
        if params.get("JobInfo") is not None:
            self._JobInfo = AppJobInfo()
            self._JobInfo._deserialize(params.get("JobInfo"))
        self._Platform = params.get("Platform")
        self._LastWebCiMode = params.get("LastWebCiMode")
        self._LastMpCiMode = params.get("LastMpCiMode")
        self._SceneType = params.get("SceneType")
        self._ClientId = params.get("ClientId")
        self._IconUrl = params.get("IconUrl")
        self._FaviconUrl = params.get("FaviconUrl")
        self._BackgroundColor = params.get("BackgroundColor")
        self._Favorite = params.get("Favorite")
        self._PublishPlatform = params.get("PublishPlatform")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WedaRole(AbstractModel):
    r"""weda角色

    """

    def __init__(self):
        r"""
        :param _Name: 角色名称
        :type Name: str
        :param _RoleIdentity: 角色标识
        :type RoleIdentity: str
        :param _Id: 角色id
        :type Id: int
        :param _ParentRoleId: 父角色id
        :type ParentRoleId: int
        :param _ChildRoleId: 子角色id
        :type ChildRoleId: int
        :param _EnvIdentity: 环境标识
        :type EnvIdentity: str
        :param _IsReleased: 是否已发布
注意：此字段可能返回 null，表示取不到有效值。
        :type IsReleased: bool
        """
        self._Name = None
        self._RoleIdentity = None
        self._Id = None
        self._ParentRoleId = None
        self._ChildRoleId = None
        self._EnvIdentity = None
        self._IsReleased = None

    @property
    def Name(self):
        r"""角色名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def RoleIdentity(self):
        r"""角色标识
        :rtype: str
        """
        return self._RoleIdentity

    @RoleIdentity.setter
    def RoleIdentity(self, RoleIdentity):
        self._RoleIdentity = RoleIdentity

    @property
    def Id(self):
        r"""角色id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ParentRoleId(self):
        r"""父角色id
        :rtype: int
        """
        return self._ParentRoleId

    @ParentRoleId.setter
    def ParentRoleId(self, ParentRoleId):
        self._ParentRoleId = ParentRoleId

    @property
    def ChildRoleId(self):
        r"""子角色id
        :rtype: int
        """
        return self._ChildRoleId

    @ChildRoleId.setter
    def ChildRoleId(self, ChildRoleId):
        self._ChildRoleId = ChildRoleId

    @property
    def EnvIdentity(self):
        r"""环境标识
        :rtype: str
        """
        return self._EnvIdentity

    @EnvIdentity.setter
    def EnvIdentity(self, EnvIdentity):
        self._EnvIdentity = EnvIdentity

    @property
    def IsReleased(self):
        r"""是否已发布
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsReleased

    @IsReleased.setter
    def IsReleased(self, IsReleased):
        self._IsReleased = IsReleased


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._RoleIdentity = params.get("RoleIdentity")
        self._Id = params.get("Id")
        self._ParentRoleId = params.get("ParentRoleId")
        self._ChildRoleId = params.get("ChildRoleId")
        self._EnvIdentity = params.get("EnvIdentity")
        self._IsReleased = params.get("IsReleased")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WedaUser(AbstractModel):
    r"""weda用户

    """

    def __init__(self):
        r"""
        :param _Uin: 腾讯云主账号uin
        :type Uin: int
        :param _Name: 名字
        :type Name: str
        :param _Env: 环境
        :type Env: int
        :param _Type: 类型
        :type Type: int
        :param _NickName: 昵称
        :type NickName: str
        :param _Email: 邮箱
        :type Email: str
        :param _Phone: 手机号
        :type Phone: str
        :param _ProjectId: 项目id
        :type ProjectId: int
        :param _Uuid: 用户uuid
        :type Uuid: str
        :param _Source: 渠道，1:自建；2:企业微信导入
        :type Source: int
        :param _OpenId: 微信openid
注意：此字段可能返回 null，表示取不到有效值。
        :type OpenId: str
        :param _RelatedRoles: 关联角色
注意：此字段可能返回 null，表示取不到有效值。
        :type RelatedRoles: list of WedaRole
        :param _WechatUserId: 企业微信userid
注意：此字段可能返回 null，表示取不到有效值。
        :type WechatUserId: str
        :param _InternalUserType: 内部用户类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalUserType: int
        :param _UserId: 微搭用户id
        :type UserId: int
        :param _OrgName: 所属部门名称
        :type OrgName: str
        :param _UserSchema: 用户schema
注意：此字段可能返回 null，表示取不到有效值。
        :type UserSchema: str
        :param _UserExtend: 用户扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :type UserExtend: str
        :param _IsLicensed: 用户是否授权License
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLicensed: bool
        :param _RelatedRoleGroups: 权限组数组
注意：此字段可能返回 null，表示取不到有效值。
        :type RelatedRoleGroups: list of RoleGroup
        :param _Orgs: 兼岗部门
注意：此字段可能返回 null，表示取不到有效值。
        :type Orgs: list of OrgResp
        :param _MainOrg: 主岗部门
注意：此字段可能返回 null，表示取不到有效值。
        :type MainOrg: list of OrgResp
        :param _ParentUserId: 直属上级
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentUserId: int
        :param _PrimaryColumn: 主列字段
注意：此字段可能返回 null，表示取不到有效值。
        :type PrimaryColumn: str
        :param _AvatarUrl: 用户头像
注意：此字段可能返回 null，表示取不到有效值。
        :type AvatarUrl: str
        :param _LastLoginTime: 最后登录时间
        :type LastLoginTime: str
        """
        self._Uin = None
        self._Name = None
        self._Env = None
        self._Type = None
        self._NickName = None
        self._Email = None
        self._Phone = None
        self._ProjectId = None
        self._Uuid = None
        self._Source = None
        self._OpenId = None
        self._RelatedRoles = None
        self._WechatUserId = None
        self._InternalUserType = None
        self._UserId = None
        self._OrgName = None
        self._UserSchema = None
        self._UserExtend = None
        self._IsLicensed = None
        self._RelatedRoleGroups = None
        self._Orgs = None
        self._MainOrg = None
        self._ParentUserId = None
        self._PrimaryColumn = None
        self._AvatarUrl = None
        self._LastLoginTime = None

    @property
    def Uin(self):
        r"""腾讯云主账号uin
        :rtype: int
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Name(self):
        r"""名字
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Env(self):
        r"""环境
        :rtype: int
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Type(self):
        r"""类型
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def NickName(self):
        r"""昵称
        :rtype: str
        """
        return self._NickName

    @NickName.setter
    def NickName(self, NickName):
        self._NickName = NickName

    @property
    def Email(self):
        r"""邮箱
        :rtype: str
        """
        return self._Email

    @Email.setter
    def Email(self, Email):
        self._Email = Email

    @property
    def Phone(self):
        r"""手机号
        :rtype: str
        """
        return self._Phone

    @Phone.setter
    def Phone(self, Phone):
        self._Phone = Phone

    @property
    def ProjectId(self):
        r"""项目id
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Uuid(self):
        r"""用户uuid
        :rtype: str
        """
        return self._Uuid

    @Uuid.setter
    def Uuid(self, Uuid):
        self._Uuid = Uuid

    @property
    def Source(self):
        r"""渠道，1:自建；2:企业微信导入
        :rtype: int
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def OpenId(self):
        r"""微信openid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def RelatedRoles(self):
        r"""关联角色
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WedaRole
        """
        return self._RelatedRoles

    @RelatedRoles.setter
    def RelatedRoles(self, RelatedRoles):
        self._RelatedRoles = RelatedRoles

    @property
    def WechatUserId(self):
        r"""企业微信userid
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WechatUserId

    @WechatUserId.setter
    def WechatUserId(self, WechatUserId):
        self._WechatUserId = WechatUserId

    @property
    def InternalUserType(self):
        r"""内部用户类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._InternalUserType

    @InternalUserType.setter
    def InternalUserType(self, InternalUserType):
        self._InternalUserType = InternalUserType

    @property
    def UserId(self):
        r"""微搭用户id
        :rtype: int
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def OrgName(self):
        r"""所属部门名称
        :rtype: str
        """
        return self._OrgName

    @OrgName.setter
    def OrgName(self, OrgName):
        self._OrgName = OrgName

    @property
    def UserSchema(self):
        r"""用户schema
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserSchema

    @UserSchema.setter
    def UserSchema(self, UserSchema):
        self._UserSchema = UserSchema

    @property
    def UserExtend(self):
        r"""用户扩展信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserExtend

    @UserExtend.setter
    def UserExtend(self, UserExtend):
        self._UserExtend = UserExtend

    @property
    def IsLicensed(self):
        r"""用户是否授权License
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsLicensed

    @IsLicensed.setter
    def IsLicensed(self, IsLicensed):
        self._IsLicensed = IsLicensed

    @property
    def RelatedRoleGroups(self):
        r"""权限组数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RoleGroup
        """
        return self._RelatedRoleGroups

    @RelatedRoleGroups.setter
    def RelatedRoleGroups(self, RelatedRoleGroups):
        self._RelatedRoleGroups = RelatedRoleGroups

    @property
    def Orgs(self):
        r"""兼岗部门
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OrgResp
        """
        return self._Orgs

    @Orgs.setter
    def Orgs(self, Orgs):
        self._Orgs = Orgs

    @property
    def MainOrg(self):
        r"""主岗部门
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of OrgResp
        """
        return self._MainOrg

    @MainOrg.setter
    def MainOrg(self, MainOrg):
        self._MainOrg = MainOrg

    @property
    def ParentUserId(self):
        r"""直属上级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ParentUserId

    @ParentUserId.setter
    def ParentUserId(self, ParentUserId):
        self._ParentUserId = ParentUserId

    @property
    def PrimaryColumn(self):
        r"""主列字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrimaryColumn

    @PrimaryColumn.setter
    def PrimaryColumn(self, PrimaryColumn):
        self._PrimaryColumn = PrimaryColumn

    @property
    def AvatarUrl(self):
        r"""用户头像
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AvatarUrl

    @AvatarUrl.setter
    def AvatarUrl(self, AvatarUrl):
        self._AvatarUrl = AvatarUrl

    @property
    def LastLoginTime(self):
        r"""最后登录时间
        :rtype: str
        """
        return self._LastLoginTime

    @LastLoginTime.setter
    def LastLoginTime(self, LastLoginTime):
        self._LastLoginTime = LastLoginTime


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Name = params.get("Name")
        self._Env = params.get("Env")
        self._Type = params.get("Type")
        self._NickName = params.get("NickName")
        self._Email = params.get("Email")
        self._Phone = params.get("Phone")
        self._ProjectId = params.get("ProjectId")
        self._Uuid = params.get("Uuid")
        self._Source = params.get("Source")
        self._OpenId = params.get("OpenId")
        if params.get("RelatedRoles") is not None:
            self._RelatedRoles = []
            for item in params.get("RelatedRoles"):
                obj = WedaRole()
                obj._deserialize(item)
                self._RelatedRoles.append(obj)
        self._WechatUserId = params.get("WechatUserId")
        self._InternalUserType = params.get("InternalUserType")
        self._UserId = params.get("UserId")
        self._OrgName = params.get("OrgName")
        self._UserSchema = params.get("UserSchema")
        self._UserExtend = params.get("UserExtend")
        self._IsLicensed = params.get("IsLicensed")
        if params.get("RelatedRoleGroups") is not None:
            self._RelatedRoleGroups = []
            for item in params.get("RelatedRoleGroups"):
                obj = RoleGroup()
                obj._deserialize(item)
                self._RelatedRoleGroups.append(obj)
        if params.get("Orgs") is not None:
            self._Orgs = []
            for item in params.get("Orgs"):
                obj = OrgResp()
                obj._deserialize(item)
                self._Orgs.append(obj)
        if params.get("MainOrg") is not None:
            self._MainOrg = []
            for item in params.get("MainOrg"):
                obj = OrgResp()
                obj._deserialize(item)
                self._MainOrg.append(obj)
        self._ParentUserId = params.get("ParentUserId")
        self._PrimaryColumn = params.get("PrimaryColumn")
        self._AvatarUrl = params.get("AvatarUrl")
        self._LastLoginTime = params.get("LastLoginTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        