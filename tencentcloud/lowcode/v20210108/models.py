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


class CreateKnowledgeSetRequest(AbstractModel):
    """CreateKnowledgeSet请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        """知识库标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        """知识库名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Desc(self):
        """描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Meta(self):
        """知识库的meta信息
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
    """CreateKnowledgeSet返回参数结构体

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


class DataSourceDetail(AbstractModel):
    """数据源详情列表

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
        """数据源 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Title(self):
        """数据源名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Name(self):
        """数据源标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """数据源类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        """数据源描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Schema(self):
        """数据源配置
        :rtype: str
        """
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def CmsProject(self):
        """cms 项目状态, 0: 重新获取详情信息，1： 不需要重新获取详情信息
        :rtype: str
        """
        return self._CmsProject

    @CmsProject.setter
    def CmsProject(self, CmsProject):
        self._CmsProject = CmsProject

    @property
    def PkgId(self):
        """当前为环境 id
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def SchemaVersion(self):
        """schema 版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SchemaVersion

    @SchemaVersion.setter
    def SchemaVersion(self, SchemaVersion):
        self._SchemaVersion = SchemaVersion

    @property
    def CreatorId(self):
        """创建者用户 ID
        :rtype: str
        """
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def CreatedAt(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def EnvId(self):
        """环境 id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DataSourceVersion(self):
        """版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DataSourceVersion

    @DataSourceVersion.setter
    def DataSourceVersion(self, DataSourceVersion):
        self._DataSourceVersion = DataSourceVersion

    @property
    def AppUsageList(self):
        """所属应用数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DataSourceLinkApp
        """
        return self._AppUsageList

    @AppUsageList.setter
    def AppUsageList(self, AppUsageList):
        self._AppUsageList = AppUsageList

    @property
    def PublishedAt(self):
        """发布时间
        :rtype: str
        """
        return self._PublishedAt

    @PublishedAt.setter
    def PublishedAt(self, PublishedAt):
        self._PublishedAt = PublishedAt

    @property
    def ChildDataSourceIds(self):
        """子数据源ids
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ChildDataSourceIds

    @ChildDataSourceIds.setter
    def ChildDataSourceIds(self, ChildDataSourceIds):
        self._ChildDataSourceIds = ChildDataSourceIds

    @property
    def Fun(self):
        """数据源发布信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Fun

    @Fun.setter
    def Fun(self, Fun):
        self._Fun = Fun

    @property
    def ScfStatus(self):
        """云函数状态 1 Active 2 Creating 3 Updating 4 Deleting  9 Deleted 11 CreatFailed  12 UpdateFailed 13 DeleteFailed 21 UpdateTimeOut
        :rtype: int
        """
        return self._ScfStatus

    @ScfStatus.setter
    def ScfStatus(self, ScfStatus):
        self._ScfStatus = ScfStatus

    @property
    def Methods(self):
        """自定义方法
        :rtype: str
        """
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def ChildDataSourceNames(self):
        """子数据源名数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._ChildDataSourceNames

    @ChildDataSourceNames.setter
    def ChildDataSourceNames(self, ChildDataSourceNames):
        self._ChildDataSourceNames = ChildDataSourceNames

    @property
    def IsNewDataSource(self):
        """是否旧数据源 1 新 0 旧
        :rtype: int
        """
        return self._IsNewDataSource

    @IsNewDataSource.setter
    def IsNewDataSource(self, IsNewDataSource):
        self._IsNewDataSource = IsNewDataSource

    @property
    def ViewId(self):
        """数据源视图id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ViewId

    @ViewId.setter
    def ViewId(self, ViewId):
        self._ViewId = ViewId

    @property
    def Configuration(self):
        """数据源属性配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def TemplateCode(self):
        """外部数据源模板code
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TemplateCode

    @TemplateCode.setter
    def TemplateCode(self, TemplateCode):
        self._TemplateCode = TemplateCode

    @property
    def Source(self):
        """外部数据源模板来源 0 空模板 1 腾讯文档 2 腾讯会议 3 企业微信 4 微信电商
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

        """发布版本
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
        """发布视图id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublishViewId

    @PublishViewId.setter
    def PublishViewId(self, PublishViewId):
        self._PublishViewId = PublishViewId

    @property
    def SubType(self):
        """数据源子类型   "database" 标准模型 "custom-database" 自定义模型 "system" 系统模型 "connector" 连接器 "custom-connector" 自定义连接器 "hidden" 隐藏数据源
        :rtype: str
        """
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def AuthStatus(self):
        """授权状态  0 授权无效 1 授权有效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def AuthInfo(self):
        """数据源授权信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.TicketAuthInfo`
        """
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo

    @property
    def PublishStatus(self):
        """1发布0未发布
        :rtype: int
        """
        return self._PublishStatus

    @PublishStatus.setter
    def PublishStatus(self, PublishStatus):
        self._PublishStatus = PublishStatus

    @property
    def UpdateVersion(self):
        """更新版本
        :rtype: int
        """
        return self._UpdateVersion

    @UpdateVersion.setter
    def UpdateVersion(self, UpdateVersion):
        self._UpdateVersion = UpdateVersion

    @property
    def RelationFieldList(self):
        """模型关联关系字段列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RelationField
        """
        return self._RelationFieldList

    @RelationFieldList.setter
    def RelationFieldList(self, RelationFieldList):
        self._RelationFieldList = RelationFieldList

    @property
    def DbInstanceType(self):
        """db实例类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DbInstanceType

    @DbInstanceType.setter
    def DbInstanceType(self, DbInstanceType):
        self._DbInstanceType = DbInstanceType

    @property
    def PreviewTableName(self):
        """体验环境db表名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PreviewTableName

    @PreviewTableName.setter
    def PreviewTableName(self, PreviewTableName):
        self._PreviewTableName = PreviewTableName

    @property
    def PublishedTableName(self):
        """正式环境db表名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PublishedTableName

    @PublishedTableName.setter
    def PublishedTableName(self, PublishedTableName):
        self._PublishedTableName = PublishedTableName

    @property
    def DbSourceType(self):
        """DB来源类型
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
    """数据详情列表

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
        """数据详情列表
        :rtype: list of DataSourceDetail
        """
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Count(self):
        """数据源列表总个数
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
    """数据源关联App信息

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
        """应用Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Title(self):
        """应用名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def EditStatusUse(self):
        """是否编辑状态使用
        :rtype: int
        """
        return self._EditStatusUse

    @EditStatusUse.setter
    def EditStatusUse(self, EditStatusUse):
        self._EditStatusUse = EditStatusUse

    @property
    def PreviewStatusUse(self):
        """是否预览状态使用
        :rtype: int
        """
        return self._PreviewStatusUse

    @PreviewStatusUse.setter
    def PreviewStatusUse(self, PreviewStatusUse):
        self._PreviewStatusUse = PreviewStatusUse

    @property
    def OnlineStatusUse(self):
        """是否正式状态使用
        :rtype: int
        """
        return self._OnlineStatusUse

    @OnlineStatusUse.setter
    def OnlineStatusUse(self, OnlineStatusUse):
        self._OnlineStatusUse = OnlineStatusUse

    @property
    def DataSourceId(self):
        """数据源ID
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
    """数据源模糊查询参数

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
        """数据源标识模糊匹配
        :rtype: str
        """
        return self._LikeName

    @LikeName.setter
    def LikeName(self, LikeName):
        self._LikeName = LikeName

    @property
    def LikeTitle(self):
        """数据源名称模糊匹配
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
        


class DeleteKnowledgeDocumentSetRequest(AbstractModel):
    """DeleteKnowledgeDocumentSet请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        """知识库标识
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def Query(self):
        """删除时制定的条件
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
    """DeleteKnowledgeDocumentSet返回参数结构体

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
        """新增文件返回信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DeleteKnowledgeDocumentSetRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DeleteKnowledgeDocumentSetRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeleteKnowledgeDocumentSetRsp(AbstractModel):
    """删除文档出参

    """

    def __init__(self):
        r"""
        :param _AffectedCount: 删除文档数量。
        :type AffectedCount: int
        """
        self._AffectedCount = None

    @property
    def AffectedCount(self):
        """删除文档数量。
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
    """DeleteKnowledgeSet请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        """知识库标识
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
    """DeleteKnowledgeSet返回参数结构体

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


class DescribeDataSourceListRequest(AbstractModel):
    """DescribeDataSourceList请求参数结构体

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
        """每页条数
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageIndex(self):
        """页码
        :rtype: int
        """
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def EnvId(self):
        """环境 id
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Appids(self):
        """应用id数组
        :rtype: list of str
        """
        return self._Appids

    @Appids.setter
    def Appids(self, Appids):
        self._Appids = Appids

    @property
    def DataSourceIds(self):
        """数据源id数组
        :rtype: list of str
        """
        return self._DataSourceIds

    @DataSourceIds.setter
    def DataSourceIds(self, DataSourceIds):
        self._DataSourceIds = DataSourceIds

    @property
    def DataSourceNames(self):
        """数据源名称数组
        :rtype: list of str
        """
        return self._DataSourceNames

    @DataSourceNames.setter
    def DataSourceNames(self, DataSourceNames):
        self._DataSourceNames = DataSourceNames

    @property
    def DataSourceType(self):
        """数据源类型 database-自建数据源；cloud-integration-自定义数据源
        :rtype: str
        """
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def QueryOption(self):
        """数据源模糊查询参数
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DataSourceQueryOption`
        """
        return self._QueryOption

    @QueryOption.setter
    def QueryOption(self, QueryOption):
        self._QueryOption = QueryOption

    @property
    def ViewIds(self):
        """数据源视图Id数组
        :rtype: list of str
        """
        return self._ViewIds

    @ViewIds.setter
    def ViewIds(self, ViewIds):
        self._ViewIds = ViewIds

    @property
    def AppLinkStatus(self):
        """查询未关联应用的数据源，0:未关联，该参数配合 AppIds 参数一块使用
        :rtype: int
        """
        return self._AppLinkStatus

    @AppLinkStatus.setter
    def AppLinkStatus(self, AppLinkStatus):
        self._AppLinkStatus = AppLinkStatus

    @property
    def QueryBindToApp(self):
        """查询应用绑定数据源: 0: 否,1: 是
        :rtype: int
        """
        return self._QueryBindToApp

    @QueryBindToApp.setter
    def QueryBindToApp(self, QueryBindToApp):
        self._QueryBindToApp = QueryBindToApp

    @property
    def QueryConnector(self):
        """查询连接器 0 数据模型 1 连接器 2 自定义连接器
        :rtype: int
        """
        return self._QueryConnector

    @QueryConnector.setter
    def QueryConnector(self, QueryConnector):
        self._QueryConnector = QueryConnector

    @property
    def NotQuerySubTypeList(self):
        """废弃中
        :rtype: list of str
        """
        return self._NotQuerySubTypeList

    @NotQuerySubTypeList.setter
    def NotQuerySubTypeList(self, NotQuerySubTypeList):
        self._NotQuerySubTypeList = NotQuerySubTypeList

    @property
    def ChannelList(self):
        """查询channelList
        :rtype: list of str
        """
        return self._ChannelList

    @ChannelList.setter
    def ChannelList(self, ChannelList):
        self._ChannelList = ChannelList

    @property
    def QueryDataSourceRelationList(self):
        """是否查询数据源关联关系
        :rtype: bool
        """
        return self._QueryDataSourceRelationList

    @QueryDataSourceRelationList.setter
    def QueryDataSourceRelationList(self, QueryDataSourceRelationList):
        self._QueryDataSourceRelationList = QueryDataSourceRelationList

    @property
    def DbInstanceType(self):
        """db实例类型
        :rtype: str
        """
        return self._DbInstanceType

    @DbInstanceType.setter
    def DbInstanceType(self, DbInstanceType):
        self._DbInstanceType = DbInstanceType

    @property
    def DatabaseTableNames(self):
        """数据库表名列表
        :rtype: list of str
        """
        return self._DatabaseTableNames

    @DatabaseTableNames.setter
    def DatabaseTableNames(self, DatabaseTableNames):
        self._DatabaseTableNames = DatabaseTableNames

    @property
    def QuerySystemModel(self):
        """是否查询系统模型，默认为true，需要显示设置为False才能过滤系统模型
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
    """DescribeDataSourceList返回参数结构体

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
        """data 数据
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DataSourceDetailItems`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DataSourceDetailItems()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeDocumentSetDetailRequest(AbstractModel):
    """DescribeKnowledgeDocumentSetDetail请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        """知识库标识
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def DocumentSetName(self):
        """文件名
        :rtype: str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def DocumentSetId(self):
        """文件id
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
    """DescribeKnowledgeDocumentSetDetail返回参数结构体

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
        """新增文件返回信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetDetailRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeKnowledgeDocumentSetDetailRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeDocumentSetDetailRsp(AbstractModel):
    """上传知识库文档返回结果

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
        """获取的数量。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def DocumentSet(self):
        """文档信息
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
    """DescribeKnowledgeDocumentSetList请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        """知识库标识
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def Query(self):
        """查询条件
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
    """DescribeKnowledgeDocumentSetList返回参数结构体

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
        """新增文件返回信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.DescribeKnowledgeDocumentSetListRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = DescribeKnowledgeDocumentSetListRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DescribeKnowledgeDocumentSetListRsp(AbstractModel):
    """删除文档出参

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
        """文件集
        :rtype: list of QureyKnowledgeDocumentSet
        """
        return self._DocumentSets

    @DocumentSets.setter
    def DocumentSets(self, DocumentSets):
        self._DocumentSets = DocumentSets

    @property
    def Count(self):
        """条数
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
    """DescribeKnowledgeSetList请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        """知识库标识，精准查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        """知识库名称，精准查询
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Offset(self):
        """分页起始位
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QueryMode(self):
        """NoPage标识不分页
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
    """DescribeKnowledgeSetList返回参数结构体

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
        """知识库列表
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSetRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = KnowledgeSetRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DocumentQuery(AbstractModel):
    """删除文档时查询入参

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
        """文件ids
        :rtype: list of str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        """文件名集合
        :rtype: list of str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def Filter(self):
        """使用创建 CollectionView 指定的 Filter 索引的字段设置查询过滤表达式
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
    """文档信息

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
        """文档id
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        """文档名
        :rtype: str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def Text(self):
        """文件完整内容。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TextPrefix(self):
        """文件内容前 200个字符。
        :rtype: str
        """
        return self._TextPrefix

    @TextPrefix.setter
    def TextPrefix(self, TextPrefix):
        self._TextPrefix = TextPrefix

    @property
    def DocumentSetInfo(self):
        """文件详情
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeDocumentSetInfo`
        """
        return self._DocumentSetInfo

    @DocumentSetInfo.setter
    def DocumentSetInfo(self, DocumentSetInfo):
        self._DocumentSetInfo = DocumentSetInfo

    @property
    def SplitterPreprocess(self):
        """文件拆分信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSplitterPreprocess`
        """
        return self._SplitterPreprocess

    @SplitterPreprocess.setter
    def SplitterPreprocess(self, SplitterPreprocess):
        self._SplitterPreprocess = SplitterPreprocess

    @property
    def Name(self):
        """未使用
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def FileTitle(self):
        """文档标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        """文档元信息，必须为jsonstring
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def Author(self):
        """作者
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def DocStatus(self):
        """上传文件状态
        :rtype: str
        """
        return self._DocStatus

    @DocStatus.setter
    def DocStatus(self, DocStatus):
        self._DocStatus = DocStatus

    @property
    def ErrMsg(self):
        """文件上传失败的具体原因
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def FileId(self):
        """Cos存储文件ID
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
    """文档信息

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
        """文件的字符数。
        :rtype: int
        """
        return self._TextLength

    @TextLength.setter
    def TextLength(self, TextLength):
        self._TextLength = TextLength

    @property
    def ByteLength(self):
        """文件的字节数。
        :rtype: int
        """
        return self._ByteLength

    @ByteLength.setter
    def ByteLength(self, ByteLength):
        self._ByteLength = ByteLength

    @property
    def IndexedProgress(self):
        """文件被预处理、Embedding 向量化的进度。
        :rtype: int
        """
        return self._IndexedProgress

    @IndexedProgress.setter
    def IndexedProgress(self, IndexedProgress):
        self._IndexedProgress = IndexedProgress

    @property
    def IndexedStatus(self):
        """文件预处理、Embedding 向量化的状态。
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
        """文件创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        """文件最后更新时间。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Keywords(self):
        """文件关键字。
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
    """知识库信息

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
        """知识库标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        """知识库名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Desc(self):
        """描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Active(self):
        """状态，
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
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Meta(self):
        """知识库的meta信息
        :rtype: str
        """
        return self._Meta

    @Meta.setter
    def Meta(self, Meta):
        self._Meta = Meta

    @property
    def TotalSize(self):
        """知识库容量,单位字节
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
    """查询知识库列表返回

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
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def KnowledgeSets(self):
        """知识库列表
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
    """文件拆分信息

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
        """在对文件拆分时，配置是否将 Title 追加到切分后的段落后面一并 Embedding。取值如下所示：
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
        """在对文件拆分时，配置是否将关键字 keywords 追加到切分后的段落一并 Embedding。取值如下所示：
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
        


class PageQuery(AbstractModel):
    """查询条件

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
        """文件id数组，表示要查询的文件的所有 ID，支持批量查询，数组元素范围[1,20]。
        :rtype: list of str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        """表示要查询的文档名称，支持批量查询，数组元素范围[1,20]。
        :rtype: list of str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def Limit(self):
        """取值范围：[1,16384]
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """设置分页偏移量，用于控制分页查询返回结果的起始位置，方便用户对数据进行分页展示和浏览。
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
        """设置后，其他字段为空值
        :rtype: list of str
        """
        return self._OutputFields

    @OutputFields.setter
    def OutputFields(self, OutputFields):
        self._OutputFields = OutputFields

    @property
    def Filter(self):
        """使用创建 CollectionView 指定的 Filter 索引的字段设置查询过滤表达式。
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
        


class QureyKnowledgeDocumentSet(AbstractModel):
    """搜索数据的集合

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
        """文件id
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        """文件名
        :rtype: str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def TextPrefix(self):
        """文件内容前 200个字符。
        :rtype: str
        """
        return self._TextPrefix

    @TextPrefix.setter
    def TextPrefix(self, TextPrefix):
        self._TextPrefix = TextPrefix

    @property
    def SplitterPreprocess(self):
        """文件拆分信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.KnowledgeSplitterPreprocess`
        """
        return self._SplitterPreprocess

    @SplitterPreprocess.setter
    def SplitterPreprocess(self, SplitterPreprocess):
        self._SplitterPreprocess = SplitterPreprocess

    @property
    def DocumentSetInfo(self):
        """文件详情
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.QureyKnowledgeDocumentSetInfo`
        """
        return self._DocumentSetInfo

    @DocumentSetInfo.setter
    def DocumentSetInfo(self, DocumentSetInfo):
        self._DocumentSetInfo = DocumentSetInfo

    @property
    def FileTitle(self):
        """文件标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        """文件元信息，必须为jsonstring
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def Name(self):
        """name
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Author(self):
        """作者
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def DocStatus(self):
        """文档上传状态
        :rtype: str
        """
        return self._DocStatus

    @DocStatus.setter
    def DocStatus(self, DocStatus):
        self._DocStatus = DocStatus

    @property
    def ErrMsg(self):
        """上传文件失败时具体的错误消息
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def FileId(self):
        """Cos存储文件ID
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
    """查询文件集合信息详情

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
        """文件的字符数。
        :rtype: int
        """
        return self._TextLength

    @TextLength.setter
    def TextLength(self, TextLength):
        self._TextLength = TextLength

    @property
    def ByteLength(self):
        """文件的字节数。
        :rtype: int
        """
        return self._ByteLength

    @ByteLength.setter
    def ByteLength(self, ByteLength):
        self._ByteLength = ByteLength

    @property
    def IndexedProgress(self):
        """文件被预处理、Embedding 向量化的进度。
        :rtype: int
        """
        return self._IndexedProgress

    @IndexedProgress.setter
    def IndexedProgress(self, IndexedProgress):
        self._IndexedProgress = IndexedProgress

    @property
    def IndexedStatus(self):
        """文件预处理、Embedding 向量化的状态。
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
        """错误信息
        :rtype: str
        """
        return self._IndexedErrorMsg

    @IndexedErrorMsg.setter
    def IndexedErrorMsg(self, IndexedErrorMsg):
        self._IndexedErrorMsg = IndexedErrorMsg

    @property
    def CreateTime(self):
        """文件创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def LastUpdateTime(self):
        """文件最后更新时间。
        :rtype: str
        """
        return self._LastUpdateTime

    @LastUpdateTime.setter
    def LastUpdateTime(self, LastUpdateTime):
        self._LastUpdateTime = LastUpdateTime

    @property
    def Keywords(self):
        """文件关键字。
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
    """数据源关联的的信息

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
        """关联关系字段
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Format(self):
        """关联关系格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def RelateDataSourceName(self):
        """关联数据源名称
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
        


class SearchDocInfo(AbstractModel):
    """知识库搜索文档信息

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
        """知识库名称
        :rtype: str
        """
        return self._CollectionViewName

    @CollectionViewName.setter
    def CollectionViewName(self, CollectionViewName):
        self._CollectionViewName = CollectionViewName

    @property
    def DocSetId(self):
        """文档Id
        :rtype: str
        """
        return self._DocSetId

    @DocSetId.setter
    def DocSetId(self, DocSetId):
        self._DocSetId = DocSetId

    @property
    def DocSetName(self):
        """文档Name
        :rtype: str
        """
        return self._DocSetName

    @DocSetName.setter
    def DocSetName(self, DocSetName):
        self._DocSetName = DocSetName

    @property
    def DocType(self):
        """文档类型
        :rtype: str
        """
        return self._DocType

    @DocType.setter
    def DocType(self, DocType):
        self._DocType = DocType

    @property
    def FileTitle(self):
        """文档标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        """文档元信息
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def DocDesc(self):
        """文档描述
        :rtype: str
        """
        return self._DocDesc

    @DocDesc.setter
    def DocDesc(self, DocDesc):
        self._DocDesc = DocDesc

    @property
    def FileSize(self):
        """文档大小
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize

    @property
    def FileId(self):
        """Cos存储文件ID
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
    """SearchDocList请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        """知识库名称
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def SearchKey(self):
        """搜索模式
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def SearchValue(self):
        """搜索值
        :rtype: str
        """
        return self._SearchValue

    @SearchValue.setter
    def SearchValue(self, SearchValue):
        self._SearchValue = SearchValue

    @property
    def PageNo(self):
        """页码
        :rtype: int
        """
        return self._PageNo

    @PageNo.setter
    def PageNo(self, PageNo):
        self._PageNo = PageNo

    @property
    def PageSize(self):
        """页大小
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
    """SearchDocList返回参数结构体

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
        """知识库文档搜索数据
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.SearchDocRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = SearchDocRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class SearchDocRsp(AbstractModel):
    """知识库文档搜索结果

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
        """文档基本信息
        :rtype: list of SearchDocInfo
        """
        return self._DocInfos

    @DocInfos.setter
    def DocInfos(self, DocInfos):
        self._DocInfos = DocInfos

    @property
    def Total(self):
        """文档总数
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
    """数据源授权信息

    """

    def __init__(self):
        r"""
        :param _AuthUser: 授权用户
        :type AuthUser: str
        """
        self._AuthUser = None

    @property
    def AuthUser(self):
        """授权用户
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
    """UpdateKnowledgeSet请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Name(self):
        """知识库标识
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Title(self):
        """知识库名称
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Desc(self):
        """描述
        :rtype: str
        """
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Active(self):
        """状态;ENABLED启用；NOT_ENABLED不启用
        :rtype: str
        """
        return self._Active

    @Active.setter
    def Active(self, Active):
        self._Active = Active

    @property
    def Meta(self):
        """知识库的meta信息
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
    """UpdateKnowledgeSet返回参数结构体

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


class UploadKnowledgeDocumentSetRequest(AbstractModel):
    """UploadKnowledgeDocumentSet请求参数结构体

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
        """环境ID
        :rtype: str
        """
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def CollectionView(self):
        """知识库标识
        :rtype: str
        """
        return self._CollectionView

    @CollectionView.setter
    def CollectionView(self, CollectionView):
        self._CollectionView = CollectionView

    @property
    def FileName(self):
        """状态;ENABLED启用；NOT_ENABLED不启用
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def CosUrl(self):
        """腾讯云文件存储位置的可读地址
        :rtype: str
        """
        return self._CosUrl

    @CosUrl.setter
    def CosUrl(self, CosUrl):
        self._CosUrl = CosUrl

    @property
    def DocumentType(self):
        """文件类型，例如: .docx, .md
        :rtype: str
        """
        return self._DocumentType

    @DocumentType.setter
    def DocumentType(self, DocumentType):
        self._DocumentType = DocumentType

    @property
    def DocumentDesc(self):
        """对文件的描述
        :rtype: str
        """
        return self._DocumentDesc

    @DocumentDesc.setter
    def DocumentDesc(self, DocumentDesc):
        self._DocumentDesc = DocumentDesc

    @property
    def FileTitle(self):
        """文件标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        """文件元信息，为jsonstring
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def DocumentSetId(self):
        """文件id
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        self._DocumentSetId = DocumentSetId

    @property
    def Delimiter(self):
        """使用 regex 分割文档
        :rtype: str
        """
        return self._Delimiter

    @Delimiter.setter
    def Delimiter(self, Delimiter):
        self._Delimiter = Delimiter

    @property
    def FileId(self):
        """Cos存储文件ID
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
    """UploadKnowledgeDocumentSet返回参数结构体

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
        """新增文件返回信息
        :rtype: :class:`tencentcloud.lowcode.v20210108.models.UploadKnowledgeDocumentSetRsp`
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = UploadKnowledgeDocumentSetRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class UploadKnowledgeDocumentSetRsp(AbstractModel):
    """上传知识库文档返回结果

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

        """给文件分配的 ID 信息。
        :rtype: str
        """
        return self._DocumentSetId

    @DocumentSetId.setter
    def DocumentSetId(self, DocumentSetId):
        warnings.warn("parameter `DocumentSetId` is deprecated", DeprecationWarning) 

        self._DocumentSetId = DocumentSetId

    @property
    def DocumentSetName(self):
        """文件名
        :rtype: str
        """
        return self._DocumentSetName

    @DocumentSetName.setter
    def DocumentSetName(self, DocumentSetName):
        self._DocumentSetName = DocumentSetName

    @property
    def FileTitle(self):
        """文件标题
        :rtype: str
        """
        return self._FileTitle

    @FileTitle.setter
    def FileTitle(self, FileTitle):
        self._FileTitle = FileTitle

    @property
    def FileMetaData(self):
        """文件元信息，为jsonstring
        :rtype: str
        """
        return self._FileMetaData

    @FileMetaData.setter
    def FileMetaData(self, FileMetaData):
        self._FileMetaData = FileMetaData

    @property
    def FileId(self):
        """Cos存储文件ID
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
        