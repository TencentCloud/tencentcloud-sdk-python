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
        :param Id: 数据源 ID
        :type Id: str
        :param Title: 数据源名称
        :type Title: str
        :param Name: 数据源标识
        :type Name: str
        :param Type: 数据源类型
        :type Type: str
        :param Description: 数据源描述
        :type Description: str
        :param Schema: 数据源配置
        :type Schema: str
        :param CmsProject: cms 项目状态, 0: 重新获取详情信息，1： 不需要重新获取详情信息
        :type CmsProject: str
        :param PkgId: 当前为环境 id
注意：此字段可能返回 null，表示取不到有效值。
        :type PkgId: str
        :param SchemaVersion: schema 版本信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SchemaVersion: str
        :param CreatorId: 创建者用户 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorId: str
        :param CreatedAt: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedAt: str
        :param UpdatedAt: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedAt: str
        :param EnvId: 环境 id
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvId: str
        :param DataSourceVersion: 版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DataSourceVersion: str
        :param AppUsageList: 所属应用数组
注意：此字段可能返回 null，表示取不到有效值。
        :type AppUsageList: list of DataSourceLinkApp
        :param PublishedAt: 发布时间
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishedAt: str
        :param ChildDataSourceIds: 子数据源ids
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildDataSourceIds: list of str
        :param Fun: 数据源发布信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Fun: str
        :param ScfStatus: 云函数状态 1 Active 2 Creating 3 Updating 4 Deleting  9 Deleted 11 CreatFailed  12 UpdateFailed 13 DeleteFailed 21 UpdateTimeOut
注意：此字段可能返回 null，表示取不到有效值。
        :type ScfStatus: int
        :param Methods: 自定义方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Methods: str
        :param ChildDataSourceNames: 子数据源名数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ChildDataSourceNames: list of str
        :param IsNewDataSource: 是否旧数据源 1 新 0 旧
注意：此字段可能返回 null，表示取不到有效值。
        :type IsNewDataSource: int
        :param ViewId: 数据源视图id
注意：此字段可能返回 null，表示取不到有效值。
        :type ViewId: str
        :param Configuration: 数据源属性配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Configuration: str
        :param TemplateCode: 外部数据源模板code
注意：此字段可能返回 null，表示取不到有效值。
        :type TemplateCode: str
        :param Source: 外部数据源模板来源 0 空模板 1 腾讯文档 2 腾讯会议 3 企业微信 4 微信电商
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: int
        :param PublishVersion: 发布版本
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishVersion: str
        :param PublishViewId: 发布视图id
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishViewId: str
        :param SubType: 数据源子类型   "database" 标准模型 "custom-database" 自定义模型 "system" 系统模型 "connector" 连接器 "custom-connector" 自定义连接器 "hidden" 隐藏数据源
注意：此字段可能返回 null，表示取不到有效值。
        :type SubType: str
        :param AuthStatus: 授权状态  0 授权无效 1 授权有效
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthStatus: int
        :param AuthInfo: 数据源授权信息
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthInfo: :class:`tencentcloud.lowcode.v20210108.models.TicketAuthInfo`
        """
        self.Id = None
        self.Title = None
        self.Name = None
        self.Type = None
        self.Description = None
        self.Schema = None
        self.CmsProject = None
        self.PkgId = None
        self.SchemaVersion = None
        self.CreatorId = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.EnvId = None
        self.DataSourceVersion = None
        self.AppUsageList = None
        self.PublishedAt = None
        self.ChildDataSourceIds = None
        self.Fun = None
        self.ScfStatus = None
        self.Methods = None
        self.ChildDataSourceNames = None
        self.IsNewDataSource = None
        self.ViewId = None
        self.Configuration = None
        self.TemplateCode = None
        self.Source = None
        self.PublishVersion = None
        self.PublishViewId = None
        self.SubType = None
        self.AuthStatus = None
        self.AuthInfo = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Title = params.get("Title")
        self.Name = params.get("Name")
        self.Type = params.get("Type")
        self.Description = params.get("Description")
        self.Schema = params.get("Schema")
        self.CmsProject = params.get("CmsProject")
        self.PkgId = params.get("PkgId")
        self.SchemaVersion = params.get("SchemaVersion")
        self.CreatorId = params.get("CreatorId")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.EnvId = params.get("EnvId")
        self.DataSourceVersion = params.get("DataSourceVersion")
        if params.get("AppUsageList") is not None:
            self.AppUsageList = []
            for item in params.get("AppUsageList"):
                obj = DataSourceLinkApp()
                obj._deserialize(item)
                self.AppUsageList.append(obj)
        self.PublishedAt = params.get("PublishedAt")
        self.ChildDataSourceIds = params.get("ChildDataSourceIds")
        self.Fun = params.get("Fun")
        self.ScfStatus = params.get("ScfStatus")
        self.Methods = params.get("Methods")
        self.ChildDataSourceNames = params.get("ChildDataSourceNames")
        self.IsNewDataSource = params.get("IsNewDataSource")
        self.ViewId = params.get("ViewId")
        self.Configuration = params.get("Configuration")
        self.TemplateCode = params.get("TemplateCode")
        self.Source = params.get("Source")
        self.PublishVersion = params.get("PublishVersion")
        self.PublishViewId = params.get("PublishViewId")
        self.SubType = params.get("SubType")
        self.AuthStatus = params.get("AuthStatus")
        if params.get("AuthInfo") is not None:
            self.AuthInfo = TicketAuthInfo()
            self.AuthInfo._deserialize(params.get("AuthInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceDetailItems(AbstractModel):
    """数据详情列表

    """

    def __init__(self):
        r"""
        :param Rows: 数据详情列表
        :type Rows: list of DataSourceDetail
        :param Count: 数据源列表总个数
        :type Count: int
        """
        self.Rows = None
        self.Count = None


    def _deserialize(self, params):
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = DataSourceDetail()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.Count = params.get("Count")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceLinkApp(AbstractModel):
    """数据源关联App信息

    """

    def __init__(self):
        r"""
        :param Id: 应用Id
        :type Id: str
        :param Title: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param EditStatusUse: 是否编辑状态使用
注意：此字段可能返回 null，表示取不到有效值。
        :type EditStatusUse: int
        :param PreviewStatusUse: 是否预览状态使用
注意：此字段可能返回 null，表示取不到有效值。
        :type PreviewStatusUse: int
        :param OnlineStatusUse: 是否正式状态使用
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineStatusUse: int
        """
        self.Id = None
        self.Title = None
        self.EditStatusUse = None
        self.PreviewStatusUse = None
        self.OnlineStatusUse = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Title = params.get("Title")
        self.EditStatusUse = params.get("EditStatusUse")
        self.PreviewStatusUse = params.get("PreviewStatusUse")
        self.OnlineStatusUse = params.get("OnlineStatusUse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DataSourceQueryOption(AbstractModel):
    """数据源模糊查询参数

    """

    def __init__(self):
        r"""
        :param LikeName: 数据源标识模糊匹配
        :type LikeName: str
        :param LikeTitle: 数据源名称模糊匹配
        :type LikeTitle: str
        """
        self.LikeName = None
        self.LikeTitle = None


    def _deserialize(self, params):
        self.LikeName = params.get("LikeName")
        self.LikeTitle = params.get("LikeTitle")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSourceListRequest(AbstractModel):
    """DescribeDataSourceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param PageSize: 每页条数
        :type PageSize: int
        :param PageIndex: 页码
        :type PageIndex: int
        :param EnvId: 环境 id
        :type EnvId: str
        :param Appids: 应用id数组
        :type Appids: list of str
        :param DataSourceIds: 数据源id数组
        :type DataSourceIds: list of str
        :param DataSourceNames: 数据源名称数组
        :type DataSourceNames: list of str
        :param DataSourceType: 数据源类型 database-自建数据源；cloud-integration-自定义数据源
        :type DataSourceType: str
        :param QueryOption: 数据源模糊查询参数
        :type QueryOption: :class:`tencentcloud.lowcode.v20210108.models.DataSourceQueryOption`
        :param ViewIds: 数据源视图Id数组
        :type ViewIds: list of str
        :param AppLinkStatus: 查询未关联应用的数据源，0:未关联，该参数配合 AppIds 参数一块使用
        :type AppLinkStatus: int
        :param QueryBindToApp: 查询应用绑定数据源: 0: 否,1: 是
        :type QueryBindToApp: int
        :param QueryConnector: 查询连接器 0 数据模型 1 连接器 2 自定义连接器
        :type QueryConnector: int
        :param NotQuerySubTypeList: 查询数据源黑名单机制，比如不想要系统数据源["system"]
        :type NotQuerySubTypeList: list of str
        """
        self.PageSize = None
        self.PageIndex = None
        self.EnvId = None
        self.Appids = None
        self.DataSourceIds = None
        self.DataSourceNames = None
        self.DataSourceType = None
        self.QueryOption = None
        self.ViewIds = None
        self.AppLinkStatus = None
        self.QueryBindToApp = None
        self.QueryConnector = None
        self.NotQuerySubTypeList = None


    def _deserialize(self, params):
        self.PageSize = params.get("PageSize")
        self.PageIndex = params.get("PageIndex")
        self.EnvId = params.get("EnvId")
        self.Appids = params.get("Appids")
        self.DataSourceIds = params.get("DataSourceIds")
        self.DataSourceNames = params.get("DataSourceNames")
        self.DataSourceType = params.get("DataSourceType")
        if params.get("QueryOption") is not None:
            self.QueryOption = DataSourceQueryOption()
            self.QueryOption._deserialize(params.get("QueryOption"))
        self.ViewIds = params.get("ViewIds")
        self.AppLinkStatus = params.get("AppLinkStatus")
        self.QueryBindToApp = params.get("QueryBindToApp")
        self.QueryConnector = params.get("QueryConnector")
        self.NotQuerySubTypeList = params.get("NotQuerySubTypeList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDataSourceListResponse(AbstractModel):
    """DescribeDataSourceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: data 数据
        :type Data: :class:`tencentcloud.lowcode.v20210108.models.DataSourceDetailItems`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DataSourceDetailItems()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class TicketAuthInfo(AbstractModel):
    """数据源授权信息

    """

    def __init__(self):
        r"""
        :param AuthUser: 授权用户
        :type AuthUser: str
        """
        self.AuthUser = None


    def _deserialize(self, params):
        self.AuthUser = params.get("AuthUser")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        