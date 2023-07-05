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
        :type Description: str
        :param _Schema: 数据源配置
        :type Schema: str
        :param _CmsProject: cms 项目状态, 0: 重新获取详情信息，1： 不需要重新获取详情信息
        :type CmsProject: str
        :param _PkgId: 当前为环境 id
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param _SchemaVersion: schema 版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaVersion: str
        :param _CreatorId: 创建者用户 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorId: str
        :param _CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param _EnvId: 环境 id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param _DataSourceVersion: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceVersion: str
        :param _AppUsageList: 所属应用数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUsageList: list of DataSourceLinkApp
        :param _PublishedAt: 发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishedAt: str
        :param _ChildDataSourceIds: 子数据源ids
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildDataSourceIds: list of str
        :param _Fun: 数据源发布信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Fun: str
        :param _ScfStatus: 云函数状态 1 Active 2 Creating 3 Updating 4 Deleting  9 Deleted 11 CreatFailed  12 UpdateFailed 13 DeleteFailed 21 UpdateTimeOut
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfStatus: int
        :param _Methods: 自定义方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Methods: str
        :param _ChildDataSourceNames: 子数据源名数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildDataSourceNames: list of str
        :param _IsNewDataSource: 是否旧数据源 1 新 0 旧
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param _AuthStatus: 授权状态  0 授权无效 1 授权有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthStatus: int
        :param _AuthInfo: 数据源授权信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthInfo: :class:`tencentcloud.lowcode.v20210108.models.TicketAuthInfo`
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

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Schema(self):
        return self._Schema

    @Schema.setter
    def Schema(self, Schema):
        self._Schema = Schema

    @property
    def CmsProject(self):
        return self._CmsProject

    @CmsProject.setter
    def CmsProject(self, CmsProject):
        self._CmsProject = CmsProject

    @property
    def PkgId(self):
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def SchemaVersion(self):
        return self._SchemaVersion

    @SchemaVersion.setter
    def SchemaVersion(self, SchemaVersion):
        self._SchemaVersion = SchemaVersion

    @property
    def CreatorId(self):
        return self._CreatorId

    @CreatorId.setter
    def CreatorId(self, CreatorId):
        self._CreatorId = CreatorId

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def DataSourceVersion(self):
        return self._DataSourceVersion

    @DataSourceVersion.setter
    def DataSourceVersion(self, DataSourceVersion):
        self._DataSourceVersion = DataSourceVersion

    @property
    def AppUsageList(self):
        return self._AppUsageList

    @AppUsageList.setter
    def AppUsageList(self, AppUsageList):
        self._AppUsageList = AppUsageList

    @property
    def PublishedAt(self):
        return self._PublishedAt

    @PublishedAt.setter
    def PublishedAt(self, PublishedAt):
        self._PublishedAt = PublishedAt

    @property
    def ChildDataSourceIds(self):
        return self._ChildDataSourceIds

    @ChildDataSourceIds.setter
    def ChildDataSourceIds(self, ChildDataSourceIds):
        self._ChildDataSourceIds = ChildDataSourceIds

    @property
    def Fun(self):
        return self._Fun

    @Fun.setter
    def Fun(self, Fun):
        self._Fun = Fun

    @property
    def ScfStatus(self):
        return self._ScfStatus

    @ScfStatus.setter
    def ScfStatus(self, ScfStatus):
        self._ScfStatus = ScfStatus

    @property
    def Methods(self):
        return self._Methods

    @Methods.setter
    def Methods(self, Methods):
        self._Methods = Methods

    @property
    def ChildDataSourceNames(self):
        return self._ChildDataSourceNames

    @ChildDataSourceNames.setter
    def ChildDataSourceNames(self, ChildDataSourceNames):
        self._ChildDataSourceNames = ChildDataSourceNames

    @property
    def IsNewDataSource(self):
        return self._IsNewDataSource

    @IsNewDataSource.setter
    def IsNewDataSource(self, IsNewDataSource):
        self._IsNewDataSource = IsNewDataSource

    @property
    def ViewId(self):
        return self._ViewId

    @ViewId.setter
    def ViewId(self, ViewId):
        self._ViewId = ViewId

    @property
    def Configuration(self):
        return self._Configuration

    @Configuration.setter
    def Configuration(self, Configuration):
        self._Configuration = Configuration

    @property
    def TemplateCode(self):
        return self._TemplateCode

    @TemplateCode.setter
    def TemplateCode(self, TemplateCode):
        self._TemplateCode = TemplateCode

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def PublishVersion(self):
        return self._PublishVersion

    @PublishVersion.setter
    def PublishVersion(self, PublishVersion):
        self._PublishVersion = PublishVersion

    @property
    def PublishViewId(self):
        return self._PublishViewId

    @PublishViewId.setter
    def PublishViewId(self, PublishViewId):
        self._PublishViewId = PublishViewId

    @property
    def SubType(self):
        return self._SubType

    @SubType.setter
    def SubType(self, SubType):
        self._SubType = SubType

    @property
    def AuthStatus(self):
        return self._AuthStatus

    @AuthStatus.setter
    def AuthStatus(self, AuthStatus):
        self._AuthStatus = AuthStatus

    @property
    def AuthInfo(self):
        return self._AuthInfo

    @AuthInfo.setter
    def AuthInfo(self, AuthInfo):
        self._AuthInfo = AuthInfo


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
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def Count(self):
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _EditStatusUse: 是否编辑状态使用
注意：此字段可能返回 null，表示取不到有效值。
        :type EditStatusUse: int
        :param _PreviewStatusUse: 是否预览状态使用
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewStatusUse: int
        :param _OnlineStatusUse: 是否正式状态使用
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineStatusUse: int
        """
        self._Id = None
        self._Title = None
        self._EditStatusUse = None
        self._PreviewStatusUse = None
        self._OnlineStatusUse = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def EditStatusUse(self):
        return self._EditStatusUse

    @EditStatusUse.setter
    def EditStatusUse(self, EditStatusUse):
        self._EditStatusUse = EditStatusUse

    @property
    def PreviewStatusUse(self):
        return self._PreviewStatusUse

    @PreviewStatusUse.setter
    def PreviewStatusUse(self, PreviewStatusUse):
        self._PreviewStatusUse = PreviewStatusUse

    @property
    def OnlineStatusUse(self):
        return self._OnlineStatusUse

    @OnlineStatusUse.setter
    def OnlineStatusUse(self, OnlineStatusUse):
        self._OnlineStatusUse = OnlineStatusUse


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Title = params.get("Title")
        self._EditStatusUse = params.get("EditStatusUse")
        self._PreviewStatusUse = params.get("PreviewStatusUse")
        self._OnlineStatusUse = params.get("OnlineStatusUse")
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
        return self._LikeName

    @LikeName.setter
    def LikeName(self, LikeName):
        self._LikeName = LikeName

    @property
    def LikeTitle(self):
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
        :param _NotQuerySubTypeList: 查询数据源黑名单机制，比如不想要系统数据源["system"]
        :type NotQuerySubTypeList: list of str
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

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageIndex(self):
        return self._PageIndex

    @PageIndex.setter
    def PageIndex(self, PageIndex):
        self._PageIndex = PageIndex

    @property
    def EnvId(self):
        return self._EnvId

    @EnvId.setter
    def EnvId(self, EnvId):
        self._EnvId = EnvId

    @property
    def Appids(self):
        return self._Appids

    @Appids.setter
    def Appids(self, Appids):
        self._Appids = Appids

    @property
    def DataSourceIds(self):
        return self._DataSourceIds

    @DataSourceIds.setter
    def DataSourceIds(self, DataSourceIds):
        self._DataSourceIds = DataSourceIds

    @property
    def DataSourceNames(self):
        return self._DataSourceNames

    @DataSourceNames.setter
    def DataSourceNames(self, DataSourceNames):
        self._DataSourceNames = DataSourceNames

    @property
    def DataSourceType(self):
        return self._DataSourceType

    @DataSourceType.setter
    def DataSourceType(self, DataSourceType):
        self._DataSourceType = DataSourceType

    @property
    def QueryOption(self):
        return self._QueryOption

    @QueryOption.setter
    def QueryOption(self, QueryOption):
        self._QueryOption = QueryOption

    @property
    def ViewIds(self):
        return self._ViewIds

    @ViewIds.setter
    def ViewIds(self, ViewIds):
        self._ViewIds = ViewIds

    @property
    def AppLinkStatus(self):
        return self._AppLinkStatus

    @AppLinkStatus.setter
    def AppLinkStatus(self, AppLinkStatus):
        self._AppLinkStatus = AppLinkStatus

    @property
    def QueryBindToApp(self):
        return self._QueryBindToApp

    @QueryBindToApp.setter
    def QueryBindToApp(self, QueryBindToApp):
        self._QueryBindToApp = QueryBindToApp

    @property
    def QueryConnector(self):
        return self._QueryConnector

    @QueryConnector.setter
    def QueryConnector(self, QueryConnector):
        self._QueryConnector = QueryConnector

    @property
    def NotQuerySubTypeList(self):
        return self._NotQuerySubTypeList

    @NotQuerySubTypeList.setter
    def NotQuerySubTypeList(self, NotQuerySubTypeList):
        self._NotQuerySubTypeList = NotQuerySubTypeList


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
            self._Data = DataSourceDetailItems()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


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
        