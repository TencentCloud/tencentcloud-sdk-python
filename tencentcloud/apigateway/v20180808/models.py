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


class APIDoc(AbstractModel):
    """API文档基本信息

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API文档ID
        :type ApiDocId: str
        :param _ApiDocName: API文档名称
        :type ApiDocName: str
        :param _ApiDocStatus: API文档构建状态
        :type ApiDocStatus: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ApiDocId = None
        self._ApiDocName = None
        self._ApiDocStatus = None
        self._Tags = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId

    @property
    def ApiDocName(self):
        return self._ApiDocName

    @ApiDocName.setter
    def ApiDocName(self, ApiDocName):
        self._ApiDocName = ApiDocName

    @property
    def ApiDocStatus(self):
        return self._ApiDocStatus

    @ApiDocStatus.setter
    def ApiDocStatus(self, ApiDocStatus):
        self._ApiDocStatus = ApiDocStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        self._ApiDocName = params.get("ApiDocName")
        self._ApiDocStatus = params.get("ApiDocStatus")
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
        


class APIDocInfo(AbstractModel):
    """API文档详细信息

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API文档ID
        :type ApiDocId: str
        :param _ApiDocName: API文档名称
        :type ApiDocName: str
        :param _ApiDocStatus: API文档构建状态
        :type ApiDocStatus: str
        :param _ApiCount: API文档API数量
        :type ApiCount: int
        :param _ViewCount: API文档查看次数
        :type ViewCount: int
        :param _ReleaseCount: API文档发布次数
        :type ReleaseCount: int
        :param _ApiDocUri: API文档访问URI
        :type ApiDocUri: str
        :param _SharePassword: API文档分享密码
        :type SharePassword: str
        :param _UpdatedTime: API文档更新时间
        :type UpdatedTime: str
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _Environment: 环境信息
        :type Environment: str
        :param _ApiIds: 生成API文档的API ID
        :type ApiIds: list of str
        :param _ServiceName: 服务名称
        :type ServiceName: str
        :param _ApiNames: 生成API文档的API名称
        :type ApiNames: list of str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ApiDocId = None
        self._ApiDocName = None
        self._ApiDocStatus = None
        self._ApiCount = None
        self._ViewCount = None
        self._ReleaseCount = None
        self._ApiDocUri = None
        self._SharePassword = None
        self._UpdatedTime = None
        self._ServiceId = None
        self._Environment = None
        self._ApiIds = None
        self._ServiceName = None
        self._ApiNames = None
        self._Tags = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId

    @property
    def ApiDocName(self):
        return self._ApiDocName

    @ApiDocName.setter
    def ApiDocName(self, ApiDocName):
        self._ApiDocName = ApiDocName

    @property
    def ApiDocStatus(self):
        return self._ApiDocStatus

    @ApiDocStatus.setter
    def ApiDocStatus(self, ApiDocStatus):
        self._ApiDocStatus = ApiDocStatus

    @property
    def ApiCount(self):
        return self._ApiCount

    @ApiCount.setter
    def ApiCount(self, ApiCount):
        self._ApiCount = ApiCount

    @property
    def ViewCount(self):
        return self._ViewCount

    @ViewCount.setter
    def ViewCount(self, ViewCount):
        self._ViewCount = ViewCount

    @property
    def ReleaseCount(self):
        return self._ReleaseCount

    @ReleaseCount.setter
    def ReleaseCount(self, ReleaseCount):
        self._ReleaseCount = ReleaseCount

    @property
    def ApiDocUri(self):
        return self._ApiDocUri

    @ApiDocUri.setter
    def ApiDocUri(self, ApiDocUri):
        self._ApiDocUri = ApiDocUri

    @property
    def SharePassword(self):
        return self._SharePassword

    @SharePassword.setter
    def SharePassword(self, SharePassword):
        self._SharePassword = SharePassword

    @property
    def UpdatedTime(self):
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ApiNames(self):
        return self._ApiNames

    @ApiNames.setter
    def ApiNames(self, ApiNames):
        self._ApiNames = ApiNames

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        self._ApiDocName = params.get("ApiDocName")
        self._ApiDocStatus = params.get("ApiDocStatus")
        self._ApiCount = params.get("ApiCount")
        self._ViewCount = params.get("ViewCount")
        self._ReleaseCount = params.get("ReleaseCount")
        self._ApiDocUri = params.get("ApiDocUri")
        self._SharePassword = params.get("SharePassword")
        self._UpdatedTime = params.get("UpdatedTime")
        self._ServiceId = params.get("ServiceId")
        self._Environment = params.get("Environment")
        self._ApiIds = params.get("ApiIds")
        self._ServiceName = params.get("ServiceName")
        self._ApiNames = params.get("ApiNames")
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
        


class APIDocs(AbstractModel):
    """API文档列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: API文档数量
        :type TotalCount: int
        :param _APIDocSet: API文档基本信息
        :type APIDocSet: list of APIDoc
        """
        self._TotalCount = None
        self._APIDocSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def APIDocSet(self):
        return self._APIDocSet

    @APIDocSet.setter
    def APIDocSet(self, APIDocSet):
        self._APIDocSet = APIDocSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("APIDocSet") is not None:
            self._APIDocSet = []
            for item in params.get("APIDocSet"):
                obj = APIDoc()
                obj._deserialize(item)
                self._APIDocSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppApiInfo(AbstractModel):
    """应用绑定的Api信息

    """

    def __init__(self):
        r"""
        :param _ApiAppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppName: str
        :param _ApiAppId: 应用ID
        :type ApiAppId: str
        :param _ApiId: Api的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param _ApiName: Api名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param _ServiceId: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _AuthorizedTime: 授权绑定时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizedTime: str
        :param _ApiRegion: Api所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiRegion: str
        :param _EnvironmentName: 授权绑定的环境
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        """
        self._ApiAppName = None
        self._ApiAppId = None
        self._ApiId = None
        self._ApiName = None
        self._ServiceId = None
        self._AuthorizedTime = None
        self._ApiRegion = None
        self._EnvironmentName = None

    @property
    def ApiAppName(self):
        return self._ApiAppName

    @ApiAppName.setter
    def ApiAppName(self, ApiAppName):
        self._ApiAppName = ApiAppName

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def AuthorizedTime(self):
        return self._AuthorizedTime

    @AuthorizedTime.setter
    def AuthorizedTime(self, AuthorizedTime):
        self._AuthorizedTime = AuthorizedTime

    @property
    def ApiRegion(self):
        return self._ApiRegion

    @ApiRegion.setter
    def ApiRegion(self, ApiRegion):
        self._ApiRegion = ApiRegion

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName


    def _deserialize(self, params):
        self._ApiAppName = params.get("ApiAppName")
        self._ApiAppId = params.get("ApiAppId")
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ServiceId = params.get("ServiceId")
        self._AuthorizedTime = params.get("AuthorizedTime")
        self._ApiRegion = params.get("ApiRegion")
        self._EnvironmentName = params.get("EnvironmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppApiInfos(AbstractModel):
    """应用信息集

    """

    def __init__(self):
        r"""
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _ApiAppApiSet: 应用绑定的Api信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppApiSet: list of ApiAppApiInfo
        """
        self._TotalCount = None
        self._ApiAppApiSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiAppApiSet(self):
        return self._ApiAppApiSet

    @ApiAppApiSet.setter
    def ApiAppApiSet(self, ApiAppApiSet):
        self._ApiAppApiSet = ApiAppApiSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiAppApiSet") is not None:
            self._ApiAppApiSet = []
            for item in params.get("ApiAppApiSet"):
                obj = ApiAppApiInfo()
                obj._deserialize(item)
                self._ApiAppApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppInfo(AbstractModel):
    """应用信息

    """

    def __init__(self):
        r"""
        :param _ApiAppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppName: str
        :param _ApiAppId: 应用ID
        :type ApiAppId: str
        :param _ApiAppSecret: 应用SECRET
注意:此字段可能返回null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppSecret: str
        :param _ApiAppDesc: 应用描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppDesc: str
        :param _CreatedTime: 创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 修改时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _ApiAppKey: 应用KEY
注意:此字段可能返回null，表示取不到有效值
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppKey: str
        """
        self._ApiAppName = None
        self._ApiAppId = None
        self._ApiAppSecret = None
        self._ApiAppDesc = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiAppKey = None

    @property
    def ApiAppName(self):
        return self._ApiAppName

    @ApiAppName.setter
    def ApiAppName(self, ApiAppName):
        self._ApiAppName = ApiAppName

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def ApiAppSecret(self):
        return self._ApiAppSecret

    @ApiAppSecret.setter
    def ApiAppSecret(self, ApiAppSecret):
        self._ApiAppSecret = ApiAppSecret

    @property
    def ApiAppDesc(self):
        return self._ApiAppDesc

    @ApiAppDesc.setter
    def ApiAppDesc(self, ApiAppDesc):
        self._ApiAppDesc = ApiAppDesc

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiAppKey(self):
        return self._ApiAppKey

    @ApiAppKey.setter
    def ApiAppKey(self, ApiAppKey):
        self._ApiAppKey = ApiAppKey


    def _deserialize(self, params):
        self._ApiAppName = params.get("ApiAppName")
        self._ApiAppId = params.get("ApiAppId")
        self._ApiAppSecret = params.get("ApiAppSecret")
        self._ApiAppDesc = params.get("ApiAppDesc")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiAppKey = params.get("ApiAppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppInfos(AbstractModel):
    """应用信息集

    """

    def __init__(self):
        r"""
        :param _TotalCount: 应用数量
        :type TotalCount: int
        :param _ApiAppSet: 应用信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppSet: list of ApiAppInfo
        """
        self._TotalCount = None
        self._ApiAppSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiAppSet(self):
        return self._ApiAppSet

    @ApiAppSet.setter
    def ApiAppSet(self, ApiAppSet):
        self._ApiAppSet = ApiAppSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiAppSet") is not None:
            self._ApiAppSet = []
            for item in params.get("ApiAppSet"):
                obj = ApiAppInfo()
                obj._deserialize(item)
                self._ApiAppSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiEnvironmentStrategy(AbstractModel):
    """api环境绑定策略

    """

    def __init__(self):
        r"""
        :param _ApiId: API唯一ID。
        :type ApiId: str
        :param _ApiName: 用户自定义API名称。
        :type ApiName: str
        :param _Path: API的路径。如/path。
        :type Path: str
        :param _Method: API的方法。如GET。
        :type Method: str
        :param _EnvironmentStrategySet: 环境的限流信息。
        :type EnvironmentStrategySet: list of EnvironmentStrategy
        """
        self._ApiId = None
        self._ApiName = None
        self._Path = None
        self._Method = None
        self._EnvironmentStrategySet = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def EnvironmentStrategySet(self):
        return self._EnvironmentStrategySet

    @EnvironmentStrategySet.setter
    def EnvironmentStrategySet(self, EnvironmentStrategySet):
        self._EnvironmentStrategySet = EnvironmentStrategySet


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        if params.get("EnvironmentStrategySet") is not None:
            self._EnvironmentStrategySet = []
            for item in params.get("EnvironmentStrategySet"):
                obj = EnvironmentStrategy()
                obj._deserialize(item)
                self._EnvironmentStrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiEnvironmentStrategyStatus(AbstractModel):
    """API绑定策略列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: API绑定的限流策略数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApiEnvironmentStrategySet: API绑定的限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiEnvironmentStrategySet: list of ApiEnvironmentStrategy
        """
        self._TotalCount = None
        self._ApiEnvironmentStrategySet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiEnvironmentStrategySet(self):
        return self._ApiEnvironmentStrategySet

    @ApiEnvironmentStrategySet.setter
    def ApiEnvironmentStrategySet(self, ApiEnvironmentStrategySet):
        self._ApiEnvironmentStrategySet = ApiEnvironmentStrategySet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiEnvironmentStrategySet") is not None:
            self._ApiEnvironmentStrategySet = []
            for item in params.get("ApiEnvironmentStrategySet"):
                obj = ApiEnvironmentStrategy()
                obj._deserialize(item)
                self._ApiEnvironmentStrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiIdStatus(AbstractModel):
    """API状态

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _ApiId: API唯一ID。
        :type ApiId: str
        :param _ApiDesc: API描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param _Path: API PATH。
        :type Path: str
        :param _Method: API METHOD。
        :type Method: str
        :param _CreatedTime: 服务创建时间。
        :type CreatedTime: str
        :param _ModifiedTime: 服务修改时间。
        :type ModifiedTime: str
        :param _ApiName: API名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param _UniqVpcId: VPC唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _ApiType: API类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param _Protocol: API协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _IsDebugAfterCharge: 是否买后调试。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDebugAfterCharge: bool
        :param _AuthType: 授权类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param _ApiBusinessType: API业务类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiBusinessType: str
        :param _AuthRelationApiId: 关联授权API唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthRelationApiId: str
        :param _RelationBuniessApiIds: 授权API关联的业务API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationBuniessApiIds: list of str
        :param _OauthConfig: oauth配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _TokenLocation: oauth2.0API请求，token存放位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenLocation: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiDesc = None
        self._Path = None
        self._Method = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiName = None
        self._UniqVpcId = None
        self._ApiType = None
        self._Protocol = None
        self._IsDebugAfterCharge = None
        self._AuthType = None
        self._ApiBusinessType = None
        self._AuthRelationApiId = None
        self._RelationBuniessApiIds = None
        self._OauthConfig = None
        self._TokenLocation = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def RelationBuniessApiIds(self):
        warnings.warn("parameter `RelationBuniessApiIds` is deprecated", DeprecationWarning) 

        return self._RelationBuniessApiIds

    @RelationBuniessApiIds.setter
    def RelationBuniessApiIds(self, RelationBuniessApiIds):
        warnings.warn("parameter `RelationBuniessApiIds` is deprecated", DeprecationWarning) 

        self._RelationBuniessApiIds = RelationBuniessApiIds

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def TokenLocation(self):
        return self._TokenLocation

    @TokenLocation.setter
    def TokenLocation(self, TokenLocation):
        self._TokenLocation = TokenLocation


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiDesc = params.get("ApiDesc")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiName = params.get("ApiName")
        self._UniqVpcId = params.get("UniqVpcId")
        self._ApiType = params.get("ApiType")
        self._Protocol = params.get("Protocol")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self._AuthType = params.get("AuthType")
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        self._RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        self._TokenLocation = params.get("TokenLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfo(AbstractModel):
    """展示api信息

    """

    def __init__(self):
        r"""
        :param _ServiceId: API 所在的服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _ServiceName: API 所在的服务的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _ServiceDesc: API 所在的服务的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param _ApiId: API 接口唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param _ApiDesc: API 接口的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param _CreatedTime: 创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 最后修改时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _ApiName: API 接口的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param _ApiType: API 类型。可取值为NORMAL（普通API）、TSF（微服务API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param _Protocol: API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _AuthType: API 鉴权类型。可取值为 SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param _ApiBusinessType: OAUTH API的类型。可取值为NORMAL（业务API）、OAUTH（授权API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiBusinessType: str
        :param _AuthRelationApiId: OAUTH 业务API 关联的授权API 唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthRelationApiId: str
        :param _OauthConfig: OAUTH配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _IsDebugAfterCharge: 是否购买后调试（云市场预留参数）。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDebugAfterCharge: bool
        :param _RequestConfig: 请求的前端配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param _ResponseType: 返回类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseType: str
        :param _ResponseSuccessExample: 自定义响应配置成功响应示例。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseSuccessExample: str
        :param _ResponseFailExample: 自定义响应配置失败响应示例。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseFailExample: str
        :param _ResponseErrorCodes: 用户自定义错误码配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseErrorCodes: list of ErrorCodes
        :param _RequestParameters: 前端请求参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestParameters: list of ReqParameter
        :param _ServiceTimeout: API 的后端服务超时时间，单位是秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTimeout: int
        :param _ServiceType: API 的后端服务类型。可取值为 HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _ServiceConfig: API 的后端服务配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param _ServiceParameters: API的后端服务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceParameters: list of DescribeApiResultServiceParametersInfo
        :param _ConstantParameters: 常量参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConstantParameters: list of ConstantParameter
        :param _ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceMockReturnMessage: str
        :param _ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfFunctionName: str
        :param _ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfFunctionNamespace: str
        :param _ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfFunctionQualifier: str
        :param _ServiceScfIsIntegratedResponse: 是否开启集成响应。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfIsIntegratedResponse: bool
        :param _ServiceWebsocketRegisterFunctionName: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketRegisterFunctionName: str
        :param _ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param _ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param _ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketCleanupFunctionName: str
        :param _ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param _ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param _InternalDomain: WEBSOCKET 回推地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalDomain: str
        :param _ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketTransportFunctionName: str
        :param _ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param _ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param _MicroServices: API绑定微服务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroServices: list of MicroService
        :param _MicroServicesInfo: 微服务信息详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroServicesInfo: list of int
        :param _ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param _ServiceTsfHealthCheckConf: 微服务的健康检查配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _EnableCORS: 是否开启跨域。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableCORS: bool
        :param _Tags: API绑定的tag信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _Environments: API已发布的环境信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Environments: list of str
        :param _IsBase64Encoded: 是否开启Base64编码，只有后端为scf时才会生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBase64Encoded: bool
        :param _IsBase64Trigger: 是否开启Base64编码的header触发，只有后端为scf时才会生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBase64Trigger: bool
        :param _Base64EncodedTriggerRules: Header触发规则，总规则数量不超过10。
注意：此字段可能返回 null，表示取不到有效值。
        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule
        :param _ServiceScfEventIsAsyncCall: 是否开启SCF Event异步调用。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfEventIsAsyncCall: bool
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._ApiId = None
        self._ApiDesc = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiName = None
        self._ApiType = None
        self._Protocol = None
        self._AuthType = None
        self._ApiBusinessType = None
        self._AuthRelationApiId = None
        self._OauthConfig = None
        self._IsDebugAfterCharge = None
        self._RequestConfig = None
        self._ResponseType = None
        self._ResponseSuccessExample = None
        self._ResponseFailExample = None
        self._ResponseErrorCodes = None
        self._RequestParameters = None
        self._ServiceTimeout = None
        self._ServiceType = None
        self._ServiceConfig = None
        self._ServiceParameters = None
        self._ConstantParameters = None
        self._ServiceMockReturnMessage = None
        self._ServiceScfFunctionName = None
        self._ServiceScfFunctionNamespace = None
        self._ServiceScfFunctionQualifier = None
        self._ServiceScfIsIntegratedResponse = None
        self._ServiceWebsocketRegisterFunctionName = None
        self._ServiceWebsocketRegisterFunctionNamespace = None
        self._ServiceWebsocketRegisterFunctionQualifier = None
        self._ServiceWebsocketCleanupFunctionName = None
        self._ServiceWebsocketCleanupFunctionNamespace = None
        self._ServiceWebsocketCleanupFunctionQualifier = None
        self._InternalDomain = None
        self._ServiceWebsocketTransportFunctionName = None
        self._ServiceWebsocketTransportFunctionNamespace = None
        self._ServiceWebsocketTransportFunctionQualifier = None
        self._MicroServices = None
        self._MicroServicesInfo = None
        self._ServiceTsfLoadBalanceConf = None
        self._ServiceTsfHealthCheckConf = None
        self._EnableCORS = None
        self._Tags = None
        self._Environments = None
        self._IsBase64Encoded = None
        self._IsBase64Trigger = None
        self._Base64EncodedTriggerRules = None
        self._ServiceScfEventIsAsyncCall = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def RequestConfig(self):
        return self._RequestConfig

    @RequestConfig.setter
    def RequestConfig(self, RequestConfig):
        self._RequestConfig = RequestConfig

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseSuccessExample(self):
        return self._ResponseSuccessExample

    @ResponseSuccessExample.setter
    def ResponseSuccessExample(self, ResponseSuccessExample):
        self._ResponseSuccessExample = ResponseSuccessExample

    @property
    def ResponseFailExample(self):
        return self._ResponseFailExample

    @ResponseFailExample.setter
    def ResponseFailExample(self, ResponseFailExample):
        self._ResponseFailExample = ResponseFailExample

    @property
    def ResponseErrorCodes(self):
        return self._ResponseErrorCodes

    @ResponseErrorCodes.setter
    def ResponseErrorCodes(self, ResponseErrorCodes):
        self._ResponseErrorCodes = ResponseErrorCodes

    @property
    def RequestParameters(self):
        return self._RequestParameters

    @RequestParameters.setter
    def RequestParameters(self, RequestParameters):
        self._RequestParameters = RequestParameters

    @property
    def ServiceTimeout(self):
        return self._ServiceTimeout

    @ServiceTimeout.setter
    def ServiceTimeout(self, ServiceTimeout):
        self._ServiceTimeout = ServiceTimeout

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ServiceConfig(self):
        return self._ServiceConfig

    @ServiceConfig.setter
    def ServiceConfig(self, ServiceConfig):
        self._ServiceConfig = ServiceConfig

    @property
    def ServiceParameters(self):
        return self._ServiceParameters

    @ServiceParameters.setter
    def ServiceParameters(self, ServiceParameters):
        self._ServiceParameters = ServiceParameters

    @property
    def ConstantParameters(self):
        return self._ConstantParameters

    @ConstantParameters.setter
    def ConstantParameters(self, ConstantParameters):
        self._ConstantParameters = ConstantParameters

    @property
    def ServiceMockReturnMessage(self):
        return self._ServiceMockReturnMessage

    @ServiceMockReturnMessage.setter
    def ServiceMockReturnMessage(self, ServiceMockReturnMessage):
        self._ServiceMockReturnMessage = ServiceMockReturnMessage

    @property
    def ServiceScfFunctionName(self):
        return self._ServiceScfFunctionName

    @ServiceScfFunctionName.setter
    def ServiceScfFunctionName(self, ServiceScfFunctionName):
        self._ServiceScfFunctionName = ServiceScfFunctionName

    @property
    def ServiceScfFunctionNamespace(self):
        return self._ServiceScfFunctionNamespace

    @ServiceScfFunctionNamespace.setter
    def ServiceScfFunctionNamespace(self, ServiceScfFunctionNamespace):
        self._ServiceScfFunctionNamespace = ServiceScfFunctionNamespace

    @property
    def ServiceScfFunctionQualifier(self):
        return self._ServiceScfFunctionQualifier

    @ServiceScfFunctionQualifier.setter
    def ServiceScfFunctionQualifier(self, ServiceScfFunctionQualifier):
        self._ServiceScfFunctionQualifier = ServiceScfFunctionQualifier

    @property
    def ServiceScfIsIntegratedResponse(self):
        return self._ServiceScfIsIntegratedResponse

    @ServiceScfIsIntegratedResponse.setter
    def ServiceScfIsIntegratedResponse(self, ServiceScfIsIntegratedResponse):
        self._ServiceScfIsIntegratedResponse = ServiceScfIsIntegratedResponse

    @property
    def ServiceWebsocketRegisterFunctionName(self):
        return self._ServiceWebsocketRegisterFunctionName

    @ServiceWebsocketRegisterFunctionName.setter
    def ServiceWebsocketRegisterFunctionName(self, ServiceWebsocketRegisterFunctionName):
        self._ServiceWebsocketRegisterFunctionName = ServiceWebsocketRegisterFunctionName

    @property
    def ServiceWebsocketRegisterFunctionNamespace(self):
        return self._ServiceWebsocketRegisterFunctionNamespace

    @ServiceWebsocketRegisterFunctionNamespace.setter
    def ServiceWebsocketRegisterFunctionNamespace(self, ServiceWebsocketRegisterFunctionNamespace):
        self._ServiceWebsocketRegisterFunctionNamespace = ServiceWebsocketRegisterFunctionNamespace

    @property
    def ServiceWebsocketRegisterFunctionQualifier(self):
        return self._ServiceWebsocketRegisterFunctionQualifier

    @ServiceWebsocketRegisterFunctionQualifier.setter
    def ServiceWebsocketRegisterFunctionQualifier(self, ServiceWebsocketRegisterFunctionQualifier):
        self._ServiceWebsocketRegisterFunctionQualifier = ServiceWebsocketRegisterFunctionQualifier

    @property
    def ServiceWebsocketCleanupFunctionName(self):
        return self._ServiceWebsocketCleanupFunctionName

    @ServiceWebsocketCleanupFunctionName.setter
    def ServiceWebsocketCleanupFunctionName(self, ServiceWebsocketCleanupFunctionName):
        self._ServiceWebsocketCleanupFunctionName = ServiceWebsocketCleanupFunctionName

    @property
    def ServiceWebsocketCleanupFunctionNamespace(self):
        return self._ServiceWebsocketCleanupFunctionNamespace

    @ServiceWebsocketCleanupFunctionNamespace.setter
    def ServiceWebsocketCleanupFunctionNamespace(self, ServiceWebsocketCleanupFunctionNamespace):
        self._ServiceWebsocketCleanupFunctionNamespace = ServiceWebsocketCleanupFunctionNamespace

    @property
    def ServiceWebsocketCleanupFunctionQualifier(self):
        return self._ServiceWebsocketCleanupFunctionQualifier

    @ServiceWebsocketCleanupFunctionQualifier.setter
    def ServiceWebsocketCleanupFunctionQualifier(self, ServiceWebsocketCleanupFunctionQualifier):
        self._ServiceWebsocketCleanupFunctionQualifier = ServiceWebsocketCleanupFunctionQualifier

    @property
    def InternalDomain(self):
        return self._InternalDomain

    @InternalDomain.setter
    def InternalDomain(self, InternalDomain):
        self._InternalDomain = InternalDomain

    @property
    def ServiceWebsocketTransportFunctionName(self):
        return self._ServiceWebsocketTransportFunctionName

    @ServiceWebsocketTransportFunctionName.setter
    def ServiceWebsocketTransportFunctionName(self, ServiceWebsocketTransportFunctionName):
        self._ServiceWebsocketTransportFunctionName = ServiceWebsocketTransportFunctionName

    @property
    def ServiceWebsocketTransportFunctionNamespace(self):
        return self._ServiceWebsocketTransportFunctionNamespace

    @ServiceWebsocketTransportFunctionNamespace.setter
    def ServiceWebsocketTransportFunctionNamespace(self, ServiceWebsocketTransportFunctionNamespace):
        self._ServiceWebsocketTransportFunctionNamespace = ServiceWebsocketTransportFunctionNamespace

    @property
    def ServiceWebsocketTransportFunctionQualifier(self):
        return self._ServiceWebsocketTransportFunctionQualifier

    @ServiceWebsocketTransportFunctionQualifier.setter
    def ServiceWebsocketTransportFunctionQualifier(self, ServiceWebsocketTransportFunctionQualifier):
        self._ServiceWebsocketTransportFunctionQualifier = ServiceWebsocketTransportFunctionQualifier

    @property
    def MicroServices(self):
        return self._MicroServices

    @MicroServices.setter
    def MicroServices(self, MicroServices):
        self._MicroServices = MicroServices

    @property
    def MicroServicesInfo(self):
        return self._MicroServicesInfo

    @MicroServicesInfo.setter
    def MicroServicesInfo(self, MicroServicesInfo):
        self._MicroServicesInfo = MicroServicesInfo

    @property
    def ServiceTsfLoadBalanceConf(self):
        return self._ServiceTsfLoadBalanceConf

    @ServiceTsfLoadBalanceConf.setter
    def ServiceTsfLoadBalanceConf(self, ServiceTsfLoadBalanceConf):
        self._ServiceTsfLoadBalanceConf = ServiceTsfLoadBalanceConf

    @property
    def ServiceTsfHealthCheckConf(self):
        return self._ServiceTsfHealthCheckConf

    @ServiceTsfHealthCheckConf.setter
    def ServiceTsfHealthCheckConf(self, ServiceTsfHealthCheckConf):
        self._ServiceTsfHealthCheckConf = ServiceTsfHealthCheckConf

    @property
    def EnableCORS(self):
        return self._EnableCORS

    @EnableCORS.setter
    def EnableCORS(self, EnableCORS):
        self._EnableCORS = EnableCORS

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Environments(self):
        return self._Environments

    @Environments.setter
    def Environments(self, Environments):
        self._Environments = Environments

    @property
    def IsBase64Encoded(self):
        return self._IsBase64Encoded

    @IsBase64Encoded.setter
    def IsBase64Encoded(self, IsBase64Encoded):
        self._IsBase64Encoded = IsBase64Encoded

    @property
    def IsBase64Trigger(self):
        return self._IsBase64Trigger

    @IsBase64Trigger.setter
    def IsBase64Trigger(self, IsBase64Trigger):
        self._IsBase64Trigger = IsBase64Trigger

    @property
    def Base64EncodedTriggerRules(self):
        return self._Base64EncodedTriggerRules

    @Base64EncodedTriggerRules.setter
    def Base64EncodedTriggerRules(self, Base64EncodedTriggerRules):
        self._Base64EncodedTriggerRules = Base64EncodedTriggerRules

    @property
    def ServiceScfEventIsAsyncCall(self):
        return self._ServiceScfEventIsAsyncCall

    @ServiceScfEventIsAsyncCall.setter
    def ServiceScfEventIsAsyncCall(self, ServiceScfEventIsAsyncCall):
        self._ServiceScfEventIsAsyncCall = ServiceScfEventIsAsyncCall


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._ApiId = params.get("ApiId")
        self._ApiDesc = params.get("ApiDesc")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiName = params.get("ApiName")
        self._ApiType = params.get("ApiType")
        self._Protocol = params.get("Protocol")
        self._AuthType = params.get("AuthType")
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        if params.get("RequestConfig") is not None:
            self._RequestConfig = RequestConfig()
            self._RequestConfig._deserialize(params.get("RequestConfig"))
        self._ResponseType = params.get("ResponseType")
        self._ResponseSuccessExample = params.get("ResponseSuccessExample")
        self._ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ResponseErrorCodes") is not None:
            self._ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ErrorCodes()
                obj._deserialize(item)
                self._ResponseErrorCodes.append(obj)
        if params.get("RequestParameters") is not None:
            self._RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = ReqParameter()
                obj._deserialize(item)
                self._RequestParameters.append(obj)
        self._ServiceTimeout = params.get("ServiceTimeout")
        self._ServiceType = params.get("ServiceType")
        if params.get("ServiceConfig") is not None:
            self._ServiceConfig = ServiceConfig()
            self._ServiceConfig._deserialize(params.get("ServiceConfig"))
        if params.get("ServiceParameters") is not None:
            self._ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = DescribeApiResultServiceParametersInfo()
                obj._deserialize(item)
                self._ServiceParameters.append(obj)
        if params.get("ConstantParameters") is not None:
            self._ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self._ConstantParameters.append(obj)
        self._ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        self._ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self._ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self._ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self._ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self._ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self._ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self._ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self._ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self._ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self._ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self._InternalDomain = params.get("InternalDomain")
        self._ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self._ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self._ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        if params.get("MicroServices") is not None:
            self._MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroService()
                obj._deserialize(item)
                self._MicroServices.append(obj)
        self._MicroServicesInfo = params.get("MicroServicesInfo")
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self._ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self._ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self._ServiceTsfHealthCheckConf = HealthCheckConf()
            self._ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        self._EnableCORS = params.get("EnableCORS")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Environments = params.get("Environments")
        self._IsBase64Encoded = params.get("IsBase64Encoded")
        self._IsBase64Trigger = params.get("IsBase64Trigger")
        if params.get("Base64EncodedTriggerRules") is not None:
            self._Base64EncodedTriggerRules = []
            for item in params.get("Base64EncodedTriggerRules"):
                obj = Base64EncodedTriggerRule()
                obj._deserialize(item)
                self._Base64EncodedTriggerRules.append(obj)
        self._ServiceScfEventIsAsyncCall = params.get("ServiceScfEventIsAsyncCall")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfoSummary(AbstractModel):
    """插件相关的API列表信息。

    """

    def __init__(self):
        r"""
        :param _TotalCount: 插件相关的API总数。
        :type TotalCount: int
        :param _ApiSet: 插件相关的API信息。
        :type ApiSet: list of AvailableApiInfo
        """
        self._TotalCount = None
        self._ApiSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiSet(self):
        return self._ApiSet

    @ApiSet.setter
    def ApiSet(self, ApiSet):
        self._ApiSet = ApiSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiSet") is not None:
            self._ApiSet = []
            for item in params.get("ApiSet"):
                obj = AvailableApiInfo()
                obj._deserialize(item)
                self._ApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiKey(AbstractModel):
    """密钥详情

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 创建的 API 密钥 ID 。
        :type AccessKeyId: str
        :param _AccessKeySecret: 创建的 API 密钥 Key。
        :type AccessKeySecret: str
        :param _AccessKeyType: 密钥类型，auto 或者 manual。
        :type AccessKeyType: str
        :param _SecretName: 用户自定义密钥名称。
        :type SecretName: str
        :param _ModifiedTime: 最后一次修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type ModifiedTime: str
        :param _Status: 密钥状态。0表示禁用，1表示启用。
        :type Status: int
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type CreatedTime: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._AccessKeyId = None
        self._AccessKeySecret = None
        self._AccessKeyType = None
        self._SecretName = None
        self._ModifiedTime = None
        self._Status = None
        self._CreatedTime = None
        self._Tags = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def AccessKeySecret(self):
        return self._AccessKeySecret

    @AccessKeySecret.setter
    def AccessKeySecret(self, AccessKeySecret):
        self._AccessKeySecret = AccessKeySecret

    @property
    def AccessKeyType(self):
        return self._AccessKeyType

    @AccessKeyType.setter
    def AccessKeyType(self, AccessKeyType):
        self._AccessKeyType = AccessKeyType

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._AccessKeySecret = params.get("AccessKeySecret")
        self._AccessKeyType = params.get("AccessKeyType")
        self._SecretName = params.get("SecretName")
        self._ModifiedTime = params.get("ModifiedTime")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
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
        


class ApiKeysStatus(AbstractModel):
    """密钥列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的 API 密钥数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApiKeySet: API 密钥列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiKeySet: list of ApiKey
        """
        self._TotalCount = None
        self._ApiKeySet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiKeySet(self):
        return self._ApiKeySet

    @ApiKeySet.setter
    def ApiKeySet(self, ApiKeySet):
        self._ApiKeySet = ApiKeySet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiKeySet") is not None:
            self._ApiKeySet = []
            for item in params.get("ApiKeySet"):
                obj = ApiKey()
                obj._deserialize(item)
                self._ApiKeySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiRequestConfig(AbstractModel):
    """api请求配置

    """

    def __init__(self):
        r"""
        :param _Path: path
        :type Path: str
        :param _Method: 方法
        :type Method: str
        """
        self._Path = None
        self._Method = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiUsagePlan(AbstractModel):
    """api或service绑定使用计划详情

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _ApiId: API 唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param _ApiName: API 名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param _Path: API 路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Method: API 方法。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _UsagePlanId: 使用计划的唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanId: str
        :param _UsagePlanName: 使用计划的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanName: str
        :param _UsagePlanDesc: 使用计划的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param _Environment: 使用计划绑定的服务环境。
注意：此字段可能返回 null，表示取不到有效值。
        :type Environment: str
        :param _InUseRequestNum: 已经使用的配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type InUseRequestNum: int
        :param _MaxRequestNum: 请求配额总量，-1表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param _MaxRequestNumPreSec: 请求 QPS 上限，-1 表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param _CreatedTime: 使用计划创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 使用计划最后修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiName = None
        self._Path = None
        self._Method = None
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._Environment = None
        self._InUseRequestNum = None
        self._MaxRequestNum = None
        self._MaxRequestNumPreSec = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ServiceName = None
        self._Tags = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def InUseRequestNum(self):
        return self._InUseRequestNum

    @InUseRequestNum.setter
    def InUseRequestNum(self, InUseRequestNum):
        self._InUseRequestNum = InUseRequestNum

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._Environment = params.get("Environment")
        self._InUseRequestNum = params.get("InUseRequestNum")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ServiceName = params.get("ServiceName")
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
        


class ApiUsagePlanSet(AbstractModel):
    """api绑定使用计划列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: API 绑定的使用计划总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApiUsagePlanList: API 绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiUsagePlanList: list of ApiUsagePlan
        """
        self._TotalCount = None
        self._ApiUsagePlanList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiUsagePlanList(self):
        return self._ApiUsagePlanList

    @ApiUsagePlanList.setter
    def ApiUsagePlanList(self, ApiUsagePlanList):
        self._ApiUsagePlanList = ApiUsagePlanList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiUsagePlanList") is not None:
            self._ApiUsagePlanList = []
            for item in params.get("ApiUsagePlanList"):
                obj = ApiUsagePlan()
                obj._deserialize(item)
                self._ApiUsagePlanList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApigatewayTags(AbstractModel):
    """key-value

    """


class AttachPluginRequest(AbstractModel):
    """AttachPlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: 绑定的API网关插件ID。
        :type PluginId: str
        :param _ServiceId: 要操作的服务ID。
        :type ServiceId: str
        :param _EnvironmentName: 要操作API的环境。
        :type EnvironmentName: str
        :param _ApiIds: 要绑定的API列表。
        :type ApiIds: list of str
        """
        self._PluginId = None
        self._ServiceId = None
        self._EnvironmentName = None
        self._ApiIds = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachPluginResponse(AbstractModel):
    """AttachPlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 绑定操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class AttachedApiInfo(AbstractModel):
    """插件绑定的API信息

    """

    def __init__(self):
        r"""
        :param _ServiceId: API所在服务ID。
        :type ServiceId: str
        :param _ServiceName: API所在服务名称。
        :type ServiceName: str
        :param _ServiceDesc: API所在服务描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param _ApiId: API ID。
        :type ApiId: str
        :param _ApiName: API名称。
        :type ApiName: str
        :param _ApiDesc: API描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param _Environment: 插件绑定API的环境。
        :type Environment: str
        :param _AttachedTime: 插件和API绑定时间。
        :type AttachedTime: str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._ApiId = None
        self._ApiName = None
        self._ApiDesc = None
        self._Environment = None
        self._AttachedTime = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def AttachedTime(self):
        return self._AttachedTime

    @AttachedTime.setter
    def AttachedTime(self, AttachedTime):
        self._AttachedTime = AttachedTime


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ApiDesc = params.get("ApiDesc")
        self._Environment = params.get("Environment")
        self._AttachedTime = params.get("AttachedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedApiSummary(AbstractModel):
    """插件绑定的API列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 插件绑定的API数量。
        :type TotalCount: int
        :param _AttachedApis: 插件绑定的API信息。
        :type AttachedApis: list of AttachedApiInfo
        """
        self._TotalCount = None
        self._AttachedApis = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AttachedApis(self):
        return self._AttachedApis

    @AttachedApis.setter
    def AttachedApis(self, AttachedApis):
        self._AttachedApis = AttachedApis


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AttachedApis") is not None:
            self._AttachedApis = []
            for item in params.get("AttachedApis"):
                obj = AttachedApiInfo()
                obj._deserialize(item)
                self._AttachedApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedPluginInfo(AbstractModel):
    """已绑定的插件信息。

    """

    def __init__(self):
        r"""
        :param _PluginId: 插件ID。
        :type PluginId: str
        :param _Environment: 环境信息。
        :type Environment: str
        :param _AttachedTime: 绑定时间。
        :type AttachedTime: str
        :param _PluginName: 插件名称。
        :type PluginName: str
        :param _PluginType: 插件类型。
        :type PluginType: str
        :param _Description: 插件描述。
        :type Description: str
        :param _PluginData: 插件定义语句。
        :type PluginData: str
        """
        self._PluginId = None
        self._Environment = None
        self._AttachedTime = None
        self._PluginName = None
        self._PluginType = None
        self._Description = None
        self._PluginData = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def AttachedTime(self):
        return self._AttachedTime

    @AttachedTime.setter
    def AttachedTime(self, AttachedTime):
        self._AttachedTime = AttachedTime

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PluginData(self):
        return self._PluginData

    @PluginData.setter
    def PluginData(self, PluginData):
        self._PluginData = PluginData


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._Environment = params.get("Environment")
        self._AttachedTime = params.get("AttachedTime")
        self._PluginName = params.get("PluginName")
        self._PluginType = params.get("PluginType")
        self._Description = params.get("Description")
        self._PluginData = params.get("PluginData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedPluginSummary(AbstractModel):
    """已绑定的插件信息。

    """

    def __init__(self):
        r"""
        :param _TotalCount: 已绑定的插件总数。
        :type TotalCount: int
        :param _PluginSummary: 已绑定的插件信息。
        :type PluginSummary: list of AttachedPluginInfo
        """
        self._TotalCount = None
        self._PluginSummary = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PluginSummary(self):
        return self._PluginSummary

    @PluginSummary.setter
    def PluginSummary(self, PluginSummary):
        self._PluginSummary = PluginSummary


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PluginSummary") is not None:
            self._PluginSummary = []
            for item in params.get("PluginSummary"):
                obj = AttachedPluginInfo()
                obj._deserialize(item)
                self._PluginSummary.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableApiInfo(AbstractModel):
    """插件相关的API信息。

    """

    def __init__(self):
        r"""
        :param _ApiId: API ID。
        :type ApiId: str
        :param _ApiName: API名称。
        :type ApiName: str
        :param _ApiType: API类型。
        :type ApiType: str
        :param _Path: API路径。
        :type Path: str
        :param _Method: API方法。
        :type Method: str
        :param _AttachedOtherPlugin: API是否绑定其他插件。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachedOtherPlugin: bool
        :param _IsAttached: API是否绑定当前插件。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAttached: bool
        """
        self._ApiId = None
        self._ApiName = None
        self._ApiType = None
        self._Path = None
        self._Method = None
        self._AttachedOtherPlugin = None
        self._IsAttached = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def AttachedOtherPlugin(self):
        return self._AttachedOtherPlugin

    @AttachedOtherPlugin.setter
    def AttachedOtherPlugin(self, AttachedOtherPlugin):
        self._AttachedOtherPlugin = AttachedOtherPlugin

    @property
    def IsAttached(self):
        return self._IsAttached

    @IsAttached.setter
    def IsAttached(self, IsAttached):
        self._IsAttached = IsAttached


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ApiType = params.get("ApiType")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._AttachedOtherPlugin = params.get("AttachedOtherPlugin")
        self._IsAttached = params.get("IsAttached")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Base64EncodedTriggerRule(AbstractModel):
    """Base64编码的header触发规则

    """

    def __init__(self):
        r"""
        :param _Name: 进行编码触发的header，可选值 "Accept"和"Content_Type" 对应实际数据流请求header中的Accept和 Content-Type。
        :type Name: str
        :param _Value: 进行编码触发的header的可选值数组, 数组元素的字符串最大长度为40，元素可以包括数字，英文字母以及特殊字符，特殊字符的可选值为： `.`    `+`    `*`   `-`   `/`  `_` 

例如 [
    "application/x-vpeg005",
    "application/xhtml+xml",
    "application/vnd.ms-project",
    "application/vnd.rn-rn_music_package"
] 等都是合法的。
        :type Value: list of str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiAppRequest(AbstractModel):
    """BindApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiAppId: 待绑定的应用唯一 ID 。
        :type ApiAppId: str
        :param _Environment: 待绑定的环境。
        :type Environment: str
        :param _ServiceId: 待绑定的服务唯一 ID。
        :type ServiceId: str
        :param _ApiId: 待绑定的API唯一ID。
        :type ApiId: str
        """
        self._ApiAppId = None
        self._Environment = None
        self._ServiceId = None
        self._ApiId = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._Environment = params.get("Environment")
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiAppResponse(AbstractModel):
    """BindApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindApiInfo(AbstractModel):
    """vpc通道绑定的api信息

    """

    def __init__(self):
        r"""
        :param _ApiId: api唯一id
        :type ApiId: str
        :param _ServiceId: Service唯一id
        :type ServiceId: str
        :param _ApiName: api名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param _ServiceName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _BindTime: 绑定时间
        :type BindTime: str
        """
        self._ApiId = None
        self._ServiceId = None
        self._ApiName = None
        self._ServiceName = None
        self._BindTime = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def BindTime(self):
        return self._BindTime

    @BindTime.setter
    def BindTime(self, BindTime):
        self._BindTime = BindTime


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ServiceId = params.get("ServiceId")
        self._ApiName = params.get("ApiName")
        self._ServiceName = params.get("ServiceName")
        self._BindTime = params.get("BindTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvironmentRequest(AbstractModel):
    """BindEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanIds: 待绑定的使用计划唯一 ID 列表。
        :type UsagePlanIds: list of str
        :param _BindType: 绑定类型，取值为API、SERVICE，默认值为SERVICE。
        :type BindType: str
        :param _Environment: 待绑定的环境。
        :type Environment: str
        :param _ServiceId: 待绑定的服务唯一 ID。
        :type ServiceId: str
        :param _ApiIds: API唯一ID数组，当bindType=API时，需要传入此参数。
        :type ApiIds: list of str
        """
        self._UsagePlanIds = None
        self._BindType = None
        self._Environment = None
        self._ServiceId = None
        self._ApiIds = None

    @property
    def UsagePlanIds(self):
        return self._UsagePlanIds

    @UsagePlanIds.setter
    def UsagePlanIds(self, UsagePlanIds):
        self._UsagePlanIds = UsagePlanIds

    @property
    def BindType(self):
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._UsagePlanIds = params.get("UsagePlanIds")
        self._BindType = params.get("BindType")
        self._Environment = params.get("Environment")
        self._ServiceId = params.get("ServiceId")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvironmentResponse(AbstractModel):
    """BindEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindIPStrategyRequest(AbstractModel):
    """BindIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待绑定的IP策略所属的服务唯一ID。
        :type ServiceId: str
        :param _StrategyId: 待绑定的IP策略唯一ID。
        :type StrategyId: str
        :param _EnvironmentName: IP策略待绑定的环境。
        :type EnvironmentName: str
        :param _BindApiIds: IP策略待绑定的API列表。
        :type BindApiIds: list of str
        """
        self._ServiceId = None
        self._StrategyId = None
        self._EnvironmentName = None
        self._BindApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def BindApiIds(self):
        return self._BindApiIds

    @BindApiIds.setter
    def BindApiIds(self, BindApiIds):
        self._BindApiIds = BindApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._BindApiIds = params.get("BindApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindIPStrategyResponse(AbstractModel):
    """BindIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindSecretIdsRequest(AbstractModel):
    """BindSecretIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 待绑定的使用计划唯一 ID。
        :type UsagePlanId: str
        :param _AccessKeyIds: 待绑定的密钥 ID 数组。
        :type AccessKeyIds: list of str
        """
        self._UsagePlanId = None
        self._AccessKeyIds = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def AccessKeyIds(self):
        return self._AccessKeyIds

    @AccessKeyIds.setter
    def AccessKeyIds(self, AccessKeyIds):
        self._AccessKeyIds = AccessKeyIds


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._AccessKeyIds = params.get("AccessKeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSecretIdsResponse(AbstractModel):
    """BindSecretIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class BindSubDomainRequest(AbstractModel):
    """BindSubDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param _SubDomain: 待绑定的自定义的域名。
        :type SubDomain: str
        :param _Protocol: 服务支持协议，可选值为http、https、http&https。
        :type Protocol: str
        :param _NetType: 网络类型，可选值为OUTER、INNER。
        :type NetType: str
        :param _IsDefaultMapping: 是否使用默认路径映射，默认为 true。为 false 时，表示自定义路径映射，此时 PathMappingSet 必填。
        :type IsDefaultMapping: bool
        :param _NetSubDomain: 默认域名。
        :type NetSubDomain: str
        :param _CertificateId: 待绑定自定义域名的证书唯一 ID。针对Protocol 为https或http&https可以选择上传。
        :type CertificateId: str
        :param _PathMappingSet: 自定义域名路径映射，最多输入三个Environment，并且只能分别取值“test”、 ”prepub“、”release“。
        :type PathMappingSet: list of PathMapping
        :param _IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。
        :type IsForcedHttps: bool
        """
        self._ServiceId = None
        self._SubDomain = None
        self._Protocol = None
        self._NetType = None
        self._IsDefaultMapping = None
        self._NetSubDomain = None
        self._CertificateId = None
        self._PathMappingSet = None
        self._IsForcedHttps = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def IsDefaultMapping(self):
        return self._IsDefaultMapping

    @IsDefaultMapping.setter
    def IsDefaultMapping(self, IsDefaultMapping):
        self._IsDefaultMapping = IsDefaultMapping

    @property
    def NetSubDomain(self):
        return self._NetSubDomain

    @NetSubDomain.setter
    def NetSubDomain(self, NetSubDomain):
        self._NetSubDomain = NetSubDomain

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def PathMappingSet(self):
        return self._PathMappingSet

    @PathMappingSet.setter
    def PathMappingSet(self, PathMappingSet):
        self._PathMappingSet = PathMappingSet

    @property
    def IsForcedHttps(self):
        return self._IsForcedHttps

    @IsForcedHttps.setter
    def IsForcedHttps(self, IsForcedHttps):
        self._IsForcedHttps = IsForcedHttps


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        self._Protocol = params.get("Protocol")
        self._NetType = params.get("NetType")
        self._IsDefaultMapping = params.get("IsDefaultMapping")
        self._NetSubDomain = params.get("NetSubDomain")
        self._CertificateId = params.get("CertificateId")
        if params.get("PathMappingSet") is not None:
            self._PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self._PathMappingSet.append(obj)
        self._IsForcedHttps = params.get("IsForcedHttps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSubDomainResponse(AbstractModel):
    """BindSubDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class BuildAPIDocRequest(AbstractModel):
    """BuildAPIDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self._ApiDocId = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildAPIDocResponse(AbstractModel):
    """BuildAPIDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ConstantParameter(AbstractModel):
    """常量参数

    """

    def __init__(self):
        r"""
        :param _Name: 常量参数名称。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Desc: 常量参数描述。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _Position: 常量参数位置。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: str
        :param _DefaultValue: 常量参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        """
        self._Name = None
        self._Desc = None
        self._Position = None
        self._DefaultValue = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Position = params.get("Position")
        self._DefaultValue = params.get("DefaultValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosConfig(AbstractModel):
    """cos类型的api配置

    """

    def __init__(self):
        r"""
        :param _Action: API调用后端COS的方式，前端请求方法与Action的可选值为：
GET：GetObject
PUT：PutObject
POST：PostObject、AppendObject
HEAD： HeadObject
DELETE： DeleteObject。
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _BucketName: API后端COS的存储桶名。
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketName: str
        :param _Authorization: API调用后端COS的签名开关，默认为false。
注意：此字段可能返回 null，表示取不到有效值。
        :type Authorization: bool
        :param _PathMatchMode: API后端COS的路径匹配模式，可选值：
BackEndPath ： 后端路径匹配
FullPath ： 全路径匹配

默认值为：BackEndPath
注意：此字段可能返回 null，表示取不到有效值。
        :type PathMatchMode: str
        """
        self._Action = None
        self._BucketName = None
        self._Authorization = None
        self._PathMatchMode = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def BucketName(self):
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def Authorization(self):
        return self._Authorization

    @Authorization.setter
    def Authorization(self, Authorization):
        self._Authorization = Authorization

    @property
    def PathMatchMode(self):
        return self._PathMatchMode

    @PathMatchMode.setter
    def PathMatchMode(self, PathMatchMode):
        self._PathMatchMode = PathMatchMode


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._BucketName = params.get("BucketName")
        self._Authorization = params.get("Authorization")
        self._PathMatchMode = params.get("PathMatchMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIDocRequest(AbstractModel):
    """CreateAPIDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiDocName: API文档名称
        :type ApiDocName: str
        :param _ServiceId: 服务名称
        :type ServiceId: str
        :param _Environment: 环境名称
        :type Environment: str
        :param _ApiIds: 生成文档的API列表
        :type ApiIds: list of str
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._ApiDocName = None
        self._ServiceId = None
        self._Environment = None
        self._ApiIds = None
        self._Tags = None

    @property
    def ApiDocName(self):
        return self._ApiDocName

    @ApiDocName.setter
    def ApiDocName(self, ApiDocName):
        self._ApiDocName = ApiDocName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ApiDocName = params.get("ApiDocName")
        self._ServiceId = params.get("ServiceId")
        self._Environment = params.get("Environment")
        self._ApiIds = params.get("ApiIds")
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
        


class CreateAPIDocResponse(AbstractModel):
    """CreateAPIDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API文档基本信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDoc()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateApiAppRequest(AbstractModel):
    """CreateApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiAppName: 用户自定义应用名称。
        :type ApiAppName: str
        :param _ApiAppDesc: 应用描述
        :type ApiAppDesc: str
        """
        self._ApiAppName = None
        self._ApiAppDesc = None

    @property
    def ApiAppName(self):
        return self._ApiAppName

    @ApiAppName.setter
    def ApiAppName(self, ApiAppName):
        self._ApiAppName = ApiAppName

    @property
    def ApiAppDesc(self):
        return self._ApiAppDesc

    @ApiAppDesc.setter
    def ApiAppDesc(self, ApiAppDesc):
        self._ApiAppDesc = ApiAppDesc


    def _deserialize(self, params):
        self._ApiAppName = params.get("ApiAppName")
        self._ApiAppDesc = params.get("ApiAppDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiAppResponse(AbstractModel):
    """CreateApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 新增的应用详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateApiKeyRequest(AbstractModel):
    """CreateApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecretName: 用户自定义密钥名称。
        :type SecretName: str
        :param _AccessKeyType: 密钥类型，支持 auto 和 manual（自定义密钥），默认为 auto。
        :type AccessKeyType: str
        :param _AccessKeyId: 用户自定义密钥 ID，AccessKeyType 为 manual 时必传。长度为5 - 50字符，由字母、数字、英文下划线组成。
        :type AccessKeyId: str
        :param _AccessKeySecret: 用户自定义密钥 Key，AccessKeyType 为 manual 时必传。长度为10 - 50字符，由字母、数字、英文下划线。
        :type AccessKeySecret: str
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._SecretName = None
        self._AccessKeyType = None
        self._AccessKeyId = None
        self._AccessKeySecret = None
        self._Tags = None

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def AccessKeyType(self):
        return self._AccessKeyType

    @AccessKeyType.setter
    def AccessKeyType(self, AccessKeyType):
        self._AccessKeyType = AccessKeyType

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def AccessKeySecret(self):
        return self._AccessKeySecret

    @AccessKeySecret.setter
    def AccessKeySecret(self, AccessKeySecret):
        self._AccessKeySecret = AccessKeySecret

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._SecretName = params.get("SecretName")
        self._AccessKeyType = params.get("AccessKeyType")
        self._AccessKeyId = params.get("AccessKeyId")
        self._AccessKeySecret = params.get("AccessKeySecret")
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
        


class CreateApiKeyResponse(AbstractModel):
    """CreateApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 新增的密钥详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiKey()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateApiRequest(AbstractModel):
    """CreateApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param _ServiceType: API 的后端服务类型。支持HTTP、MOCK、TSF、SCF、EB、TARGET、VPC、UPSTREAM、GRPC、COS、WEBSOCKET。
        :type ServiceType: str
        :param _ServiceTimeout: API 的后端服务超时时间，单位是秒。
        :type ServiceTimeout: int
        :param _Protocol: API 的前端请求协议，支持HTTP和WEBSOCKET。
        :type Protocol: str
        :param _RequestConfig: 请求的前端配置。
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.ApiRequestConfig`
        :param _ApiName: 用户自定义的 API 名称。
        :type ApiName: str
        :param _ApiDesc: 用户自定义的 API 接口描述。
        :type ApiDesc: str
        :param _ApiType: API 类型，支持NORMAL（普通API）和TSF（微服务API），默认为NORMAL。
        :type ApiType: str
        :param _AuthType: API 鉴权类型。支持SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH、APP（应用认证）。默认为NONE。
        :type AuthType: str
        :param _EnableCORS: 是否开启跨域。
        :type EnableCORS: bool
        :param _ConstantParameters: 常量参数。
        :type ConstantParameters: list of ConstantParameter
        :param _RequestParameters: 前端请求参数。
        :type RequestParameters: list of RequestParameter
        :param _ApiBusinessType: 当AuthType 为 OAUTH时，该字段有效， NORMAL：业务api OAUTH：授权API。
        :type ApiBusinessType: str
        :param _ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。
        :type ServiceMockReturnMessage: str
        :param _MicroServices: API绑定微服务列表。
        :type MicroServices: list of MicroServiceReq
        :param _ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param _ServiceTsfHealthCheckConf: 微服务的健康检查配置。
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _TargetServices: target类型后端资源信息。（内测阶段）
        :type TargetServices: list of TargetServicesReq
        :param _TargetServicesLoadBalanceConf: target类型负载均衡配置。（内测阶段）
        :type TargetServicesLoadBalanceConf: int
        :param _TargetServicesHealthCheckConf: target健康检查配置。（内测阶段）
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。
        :type ServiceScfFunctionName: str
        :param _ServiceWebsocketRegisterFunctionName: scf websocket注册函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionName: str
        :param _ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionName: str
        :param _ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionName: str
        :param _ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。
        :type ServiceScfFunctionNamespace: str
        :param _ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。
        :type ServiceScfFunctionQualifier: str
        :param _ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param _ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param _ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param _ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param _ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param _ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param _ServiceScfIsIntegratedResponse: 是否开启响应集成。当后端类型是SCF时生效。
        :type ServiceScfIsIntegratedResponse: bool
        :param _IsDebugAfterCharge: 开始调试后计费。（云市场预留字段）
        :type IsDebugAfterCharge: bool
        :param _IsDeleteResponseErrorCodes: 是否删除自定义响应配置错误码，如果不传或者传 False，不删除，当传 True 时，则删除此 API 所有自定义响应配置错误码。
        :type IsDeleteResponseErrorCodes: bool
        :param _ResponseType: 返回类型。
        :type ResponseType: str
        :param _ResponseSuccessExample: 自定义响应配置成功响应示例。
        :type ResponseSuccessExample: str
        :param _ResponseFailExample: 自定义响应配置失败响应示例。
        :type ResponseFailExample: str
        :param _ServiceConfig: API 的后端服务配置。
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param _AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
        :type AuthRelationApiId: str
        :param _ServiceParameters: API的后端服务参数。
        :type ServiceParameters: list of ServiceParameter
        :param _OauthConfig: oauth配置。当AuthType是OAUTH时生效。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _ResponseErrorCodes: 用户自定义错误码配置。
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param _TargetNamespaceId: tsf serverless 命名空间ID。（内测中）
        :type TargetNamespaceId: str
        :param _UserType: 用户类型。
        :type UserType: str
        :param _IsBase64Encoded: 是否打开Base64编码，只有后端是scf时才会生效。
        :type IsBase64Encoded: bool
        :param _EventBusId: 事件总线ID。
        :type EventBusId: str
        :param _ServiceScfFunctionType: scf函数类型。当后端类型是SCF时生效。支持事件触发(EVENT)，http直通云函数(HTTP)。
        :type ServiceScfFunctionType: str
        :param _ServiceScfEventIsAsyncCall: 是否开启SCF Event异步调用。
        :type ServiceScfEventIsAsyncCall: bool
        :param _EIAMAppType: EIAM应用类型。
        :type EIAMAppType: str
        :param _EIAMAuthType: EIAM应用认证类型，支持仅认证（AuthenticationOnly）、认证和鉴权（Authorization）。
        :type EIAMAuthType: str
        :param _TokenTimeout: EIAM应用Token 有效时间，单位为秒，默认为7200秒。
        :type TokenTimeout: int
        :param _EIAMAppId: EIAM应用ID。
        :type EIAMAppId: str
        :param _Owner: 资源的Owner
        :type Owner: str
        """
        self._ServiceId = None
        self._ServiceType = None
        self._ServiceTimeout = None
        self._Protocol = None
        self._RequestConfig = None
        self._ApiName = None
        self._ApiDesc = None
        self._ApiType = None
        self._AuthType = None
        self._EnableCORS = None
        self._ConstantParameters = None
        self._RequestParameters = None
        self._ApiBusinessType = None
        self._ServiceMockReturnMessage = None
        self._MicroServices = None
        self._ServiceTsfLoadBalanceConf = None
        self._ServiceTsfHealthCheckConf = None
        self._TargetServices = None
        self._TargetServicesLoadBalanceConf = None
        self._TargetServicesHealthCheckConf = None
        self._ServiceScfFunctionName = None
        self._ServiceWebsocketRegisterFunctionName = None
        self._ServiceWebsocketCleanupFunctionName = None
        self._ServiceWebsocketTransportFunctionName = None
        self._ServiceScfFunctionNamespace = None
        self._ServiceScfFunctionQualifier = None
        self._ServiceWebsocketRegisterFunctionNamespace = None
        self._ServiceWebsocketRegisterFunctionQualifier = None
        self._ServiceWebsocketTransportFunctionNamespace = None
        self._ServiceWebsocketTransportFunctionQualifier = None
        self._ServiceWebsocketCleanupFunctionNamespace = None
        self._ServiceWebsocketCleanupFunctionQualifier = None
        self._ServiceScfIsIntegratedResponse = None
        self._IsDebugAfterCharge = None
        self._IsDeleteResponseErrorCodes = None
        self._ResponseType = None
        self._ResponseSuccessExample = None
        self._ResponseFailExample = None
        self._ServiceConfig = None
        self._AuthRelationApiId = None
        self._ServiceParameters = None
        self._OauthConfig = None
        self._ResponseErrorCodes = None
        self._TargetNamespaceId = None
        self._UserType = None
        self._IsBase64Encoded = None
        self._EventBusId = None
        self._ServiceScfFunctionType = None
        self._ServiceScfEventIsAsyncCall = None
        self._EIAMAppType = None
        self._EIAMAuthType = None
        self._TokenTimeout = None
        self._EIAMAppId = None
        self._Owner = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ServiceTimeout(self):
        return self._ServiceTimeout

    @ServiceTimeout.setter
    def ServiceTimeout(self, ServiceTimeout):
        self._ServiceTimeout = ServiceTimeout

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RequestConfig(self):
        return self._RequestConfig

    @RequestConfig.setter
    def RequestConfig(self, RequestConfig):
        self._RequestConfig = RequestConfig

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def EnableCORS(self):
        return self._EnableCORS

    @EnableCORS.setter
    def EnableCORS(self, EnableCORS):
        self._EnableCORS = EnableCORS

    @property
    def ConstantParameters(self):
        return self._ConstantParameters

    @ConstantParameters.setter
    def ConstantParameters(self, ConstantParameters):
        self._ConstantParameters = ConstantParameters

    @property
    def RequestParameters(self):
        return self._RequestParameters

    @RequestParameters.setter
    def RequestParameters(self, RequestParameters):
        self._RequestParameters = RequestParameters

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def ServiceMockReturnMessage(self):
        return self._ServiceMockReturnMessage

    @ServiceMockReturnMessage.setter
    def ServiceMockReturnMessage(self, ServiceMockReturnMessage):
        self._ServiceMockReturnMessage = ServiceMockReturnMessage

    @property
    def MicroServices(self):
        return self._MicroServices

    @MicroServices.setter
    def MicroServices(self, MicroServices):
        self._MicroServices = MicroServices

    @property
    def ServiceTsfLoadBalanceConf(self):
        return self._ServiceTsfLoadBalanceConf

    @ServiceTsfLoadBalanceConf.setter
    def ServiceTsfLoadBalanceConf(self, ServiceTsfLoadBalanceConf):
        self._ServiceTsfLoadBalanceConf = ServiceTsfLoadBalanceConf

    @property
    def ServiceTsfHealthCheckConf(self):
        return self._ServiceTsfHealthCheckConf

    @ServiceTsfHealthCheckConf.setter
    def ServiceTsfHealthCheckConf(self, ServiceTsfHealthCheckConf):
        self._ServiceTsfHealthCheckConf = ServiceTsfHealthCheckConf

    @property
    def TargetServices(self):
        return self._TargetServices

    @TargetServices.setter
    def TargetServices(self, TargetServices):
        self._TargetServices = TargetServices

    @property
    def TargetServicesLoadBalanceConf(self):
        return self._TargetServicesLoadBalanceConf

    @TargetServicesLoadBalanceConf.setter
    def TargetServicesLoadBalanceConf(self, TargetServicesLoadBalanceConf):
        self._TargetServicesLoadBalanceConf = TargetServicesLoadBalanceConf

    @property
    def TargetServicesHealthCheckConf(self):
        return self._TargetServicesHealthCheckConf

    @TargetServicesHealthCheckConf.setter
    def TargetServicesHealthCheckConf(self, TargetServicesHealthCheckConf):
        self._TargetServicesHealthCheckConf = TargetServicesHealthCheckConf

    @property
    def ServiceScfFunctionName(self):
        return self._ServiceScfFunctionName

    @ServiceScfFunctionName.setter
    def ServiceScfFunctionName(self, ServiceScfFunctionName):
        self._ServiceScfFunctionName = ServiceScfFunctionName

    @property
    def ServiceWebsocketRegisterFunctionName(self):
        return self._ServiceWebsocketRegisterFunctionName

    @ServiceWebsocketRegisterFunctionName.setter
    def ServiceWebsocketRegisterFunctionName(self, ServiceWebsocketRegisterFunctionName):
        self._ServiceWebsocketRegisterFunctionName = ServiceWebsocketRegisterFunctionName

    @property
    def ServiceWebsocketCleanupFunctionName(self):
        return self._ServiceWebsocketCleanupFunctionName

    @ServiceWebsocketCleanupFunctionName.setter
    def ServiceWebsocketCleanupFunctionName(self, ServiceWebsocketCleanupFunctionName):
        self._ServiceWebsocketCleanupFunctionName = ServiceWebsocketCleanupFunctionName

    @property
    def ServiceWebsocketTransportFunctionName(self):
        return self._ServiceWebsocketTransportFunctionName

    @ServiceWebsocketTransportFunctionName.setter
    def ServiceWebsocketTransportFunctionName(self, ServiceWebsocketTransportFunctionName):
        self._ServiceWebsocketTransportFunctionName = ServiceWebsocketTransportFunctionName

    @property
    def ServiceScfFunctionNamespace(self):
        return self._ServiceScfFunctionNamespace

    @ServiceScfFunctionNamespace.setter
    def ServiceScfFunctionNamespace(self, ServiceScfFunctionNamespace):
        self._ServiceScfFunctionNamespace = ServiceScfFunctionNamespace

    @property
    def ServiceScfFunctionQualifier(self):
        return self._ServiceScfFunctionQualifier

    @ServiceScfFunctionQualifier.setter
    def ServiceScfFunctionQualifier(self, ServiceScfFunctionQualifier):
        self._ServiceScfFunctionQualifier = ServiceScfFunctionQualifier

    @property
    def ServiceWebsocketRegisterFunctionNamespace(self):
        return self._ServiceWebsocketRegisterFunctionNamespace

    @ServiceWebsocketRegisterFunctionNamespace.setter
    def ServiceWebsocketRegisterFunctionNamespace(self, ServiceWebsocketRegisterFunctionNamespace):
        self._ServiceWebsocketRegisterFunctionNamespace = ServiceWebsocketRegisterFunctionNamespace

    @property
    def ServiceWebsocketRegisterFunctionQualifier(self):
        return self._ServiceWebsocketRegisterFunctionQualifier

    @ServiceWebsocketRegisterFunctionQualifier.setter
    def ServiceWebsocketRegisterFunctionQualifier(self, ServiceWebsocketRegisterFunctionQualifier):
        self._ServiceWebsocketRegisterFunctionQualifier = ServiceWebsocketRegisterFunctionQualifier

    @property
    def ServiceWebsocketTransportFunctionNamespace(self):
        return self._ServiceWebsocketTransportFunctionNamespace

    @ServiceWebsocketTransportFunctionNamespace.setter
    def ServiceWebsocketTransportFunctionNamespace(self, ServiceWebsocketTransportFunctionNamespace):
        self._ServiceWebsocketTransportFunctionNamespace = ServiceWebsocketTransportFunctionNamespace

    @property
    def ServiceWebsocketTransportFunctionQualifier(self):
        return self._ServiceWebsocketTransportFunctionQualifier

    @ServiceWebsocketTransportFunctionQualifier.setter
    def ServiceWebsocketTransportFunctionQualifier(self, ServiceWebsocketTransportFunctionQualifier):
        self._ServiceWebsocketTransportFunctionQualifier = ServiceWebsocketTransportFunctionQualifier

    @property
    def ServiceWebsocketCleanupFunctionNamespace(self):
        return self._ServiceWebsocketCleanupFunctionNamespace

    @ServiceWebsocketCleanupFunctionNamespace.setter
    def ServiceWebsocketCleanupFunctionNamespace(self, ServiceWebsocketCleanupFunctionNamespace):
        self._ServiceWebsocketCleanupFunctionNamespace = ServiceWebsocketCleanupFunctionNamespace

    @property
    def ServiceWebsocketCleanupFunctionQualifier(self):
        return self._ServiceWebsocketCleanupFunctionQualifier

    @ServiceWebsocketCleanupFunctionQualifier.setter
    def ServiceWebsocketCleanupFunctionQualifier(self, ServiceWebsocketCleanupFunctionQualifier):
        self._ServiceWebsocketCleanupFunctionQualifier = ServiceWebsocketCleanupFunctionQualifier

    @property
    def ServiceScfIsIntegratedResponse(self):
        return self._ServiceScfIsIntegratedResponse

    @ServiceScfIsIntegratedResponse.setter
    def ServiceScfIsIntegratedResponse(self, ServiceScfIsIntegratedResponse):
        self._ServiceScfIsIntegratedResponse = ServiceScfIsIntegratedResponse

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def IsDeleteResponseErrorCodes(self):
        return self._IsDeleteResponseErrorCodes

    @IsDeleteResponseErrorCodes.setter
    def IsDeleteResponseErrorCodes(self, IsDeleteResponseErrorCodes):
        self._IsDeleteResponseErrorCodes = IsDeleteResponseErrorCodes

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseSuccessExample(self):
        return self._ResponseSuccessExample

    @ResponseSuccessExample.setter
    def ResponseSuccessExample(self, ResponseSuccessExample):
        self._ResponseSuccessExample = ResponseSuccessExample

    @property
    def ResponseFailExample(self):
        return self._ResponseFailExample

    @ResponseFailExample.setter
    def ResponseFailExample(self, ResponseFailExample):
        self._ResponseFailExample = ResponseFailExample

    @property
    def ServiceConfig(self):
        return self._ServiceConfig

    @ServiceConfig.setter
    def ServiceConfig(self, ServiceConfig):
        self._ServiceConfig = ServiceConfig

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def ServiceParameters(self):
        return self._ServiceParameters

    @ServiceParameters.setter
    def ServiceParameters(self, ServiceParameters):
        self._ServiceParameters = ServiceParameters

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def ResponseErrorCodes(self):
        return self._ResponseErrorCodes

    @ResponseErrorCodes.setter
    def ResponseErrorCodes(self, ResponseErrorCodes):
        self._ResponseErrorCodes = ResponseErrorCodes

    @property
    def TargetNamespaceId(self):
        return self._TargetNamespaceId

    @TargetNamespaceId.setter
    def TargetNamespaceId(self, TargetNamespaceId):
        self._TargetNamespaceId = TargetNamespaceId

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def IsBase64Encoded(self):
        return self._IsBase64Encoded

    @IsBase64Encoded.setter
    def IsBase64Encoded(self, IsBase64Encoded):
        self._IsBase64Encoded = IsBase64Encoded

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def ServiceScfFunctionType(self):
        return self._ServiceScfFunctionType

    @ServiceScfFunctionType.setter
    def ServiceScfFunctionType(self, ServiceScfFunctionType):
        self._ServiceScfFunctionType = ServiceScfFunctionType

    @property
    def ServiceScfEventIsAsyncCall(self):
        return self._ServiceScfEventIsAsyncCall

    @ServiceScfEventIsAsyncCall.setter
    def ServiceScfEventIsAsyncCall(self, ServiceScfEventIsAsyncCall):
        self._ServiceScfEventIsAsyncCall = ServiceScfEventIsAsyncCall

    @property
    def EIAMAppType(self):
        return self._EIAMAppType

    @EIAMAppType.setter
    def EIAMAppType(self, EIAMAppType):
        self._EIAMAppType = EIAMAppType

    @property
    def EIAMAuthType(self):
        return self._EIAMAuthType

    @EIAMAuthType.setter
    def EIAMAuthType(self, EIAMAuthType):
        self._EIAMAuthType = EIAMAuthType

    @property
    def TokenTimeout(self):
        return self._TokenTimeout

    @TokenTimeout.setter
    def TokenTimeout(self, TokenTimeout):
        self._TokenTimeout = TokenTimeout

    @property
    def EIAMAppId(self):
        return self._EIAMAppId

    @EIAMAppId.setter
    def EIAMAppId(self, EIAMAppId):
        self._EIAMAppId = EIAMAppId

    @property
    def Owner(self):
        return self._Owner

    @Owner.setter
    def Owner(self, Owner):
        self._Owner = Owner


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceType = params.get("ServiceType")
        self._ServiceTimeout = params.get("ServiceTimeout")
        self._Protocol = params.get("Protocol")
        if params.get("RequestConfig") is not None:
            self._RequestConfig = ApiRequestConfig()
            self._RequestConfig._deserialize(params.get("RequestConfig"))
        self._ApiName = params.get("ApiName")
        self._ApiDesc = params.get("ApiDesc")
        self._ApiType = params.get("ApiType")
        self._AuthType = params.get("AuthType")
        self._EnableCORS = params.get("EnableCORS")
        if params.get("ConstantParameters") is not None:
            self._ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self._ConstantParameters.append(obj)
        if params.get("RequestParameters") is not None:
            self._RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = RequestParameter()
                obj._deserialize(item)
                self._RequestParameters.append(obj)
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        if params.get("MicroServices") is not None:
            self._MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroServiceReq()
                obj._deserialize(item)
                self._MicroServices.append(obj)
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self._ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self._ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self._ServiceTsfHealthCheckConf = HealthCheckConf()
            self._ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        if params.get("TargetServices") is not None:
            self._TargetServices = []
            for item in params.get("TargetServices"):
                obj = TargetServicesReq()
                obj._deserialize(item)
                self._TargetServices.append(obj)
        self._TargetServicesLoadBalanceConf = params.get("TargetServicesLoadBalanceConf")
        if params.get("TargetServicesHealthCheckConf") is not None:
            self._TargetServicesHealthCheckConf = HealthCheckConf()
            self._TargetServicesHealthCheckConf._deserialize(params.get("TargetServicesHealthCheckConf"))
        self._ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self._ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self._ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self._ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self._ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self._ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self._ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self._ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self._ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self._ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        self._ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self._ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self._ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self._IsDeleteResponseErrorCodes = params.get("IsDeleteResponseErrorCodes")
        self._ResponseType = params.get("ResponseType")
        self._ResponseSuccessExample = params.get("ResponseSuccessExample")
        self._ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ServiceConfig") is not None:
            self._ServiceConfig = ServiceConfig()
            self._ServiceConfig._deserialize(params.get("ServiceConfig"))
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("ServiceParameters") is not None:
            self._ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self._ServiceParameters.append(obj)
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        if params.get("ResponseErrorCodes") is not None:
            self._ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ResponseErrorCodeReq()
                obj._deserialize(item)
                self._ResponseErrorCodes.append(obj)
        self._TargetNamespaceId = params.get("TargetNamespaceId")
        self._UserType = params.get("UserType")
        self._IsBase64Encoded = params.get("IsBase64Encoded")
        self._EventBusId = params.get("EventBusId")
        self._ServiceScfFunctionType = params.get("ServiceScfFunctionType")
        self._ServiceScfEventIsAsyncCall = params.get("ServiceScfEventIsAsyncCall")
        self._EIAMAppType = params.get("EIAMAppType")
        self._EIAMAuthType = params.get("EIAMAuthType")
        self._TokenTimeout = params.get("TokenTimeout")
        self._EIAMAppId = params.get("EIAMAppId")
        self._Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiResponse(AbstractModel):
    """CreateApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: api信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiResultInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateApiResultInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateApiResultInfo(AbstractModel):
    """创建api返回

    """

    def __init__(self):
        r"""
        :param _ApiId: api id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param _Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Method: 请求方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        """
        self._ApiId = None
        self._Path = None
        self._Method = None
        self._CreatedTime = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiRsp(AbstractModel):
    """创建api返回

    """

    def __init__(self):
        r"""
        :param _ApiId: api id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param _Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Method: 请求方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _Status: 导入状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ErrMsg: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param _ApiName: api name
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        """
        self._ApiId = None
        self._Path = None
        self._Method = None
        self._CreatedTime = None
        self._Status = None
        self._ErrMsg = None
        self._ApiName = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrMsg(self):
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._CreatedTime = params.get("CreatedTime")
        self._Status = params.get("Status")
        self._ErrMsg = params.get("ErrMsg")
        self._ApiName = params.get("ApiName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiRspSet(AbstractModel):
    """CreateApiRsp  返回加TotalCount

    """

    def __init__(self):
        r"""
        :param _TotalCount: 个数
        :type TotalCount: int
        :param _ApiSet: 返回的数组
        :type ApiSet: list of CreateApiRsp
        """
        self._TotalCount = None
        self._ApiSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiSet(self):
        return self._ApiSet

    @ApiSet.setter
    def ApiSet(self, ApiSet):
        self._ApiSet = ApiSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiSet") is not None:
            self._ApiSet = []
            for item in params.get("ApiSet"):
                obj = CreateApiRsp()
                obj._deserialize(item)
                self._ApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPStrategyRequest(AbstractModel):
    """CreateIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务的唯一ID。
        :type ServiceId: str
        :param _StrategyName: 用户自定义的策略名称。
        :type StrategyName: str
        :param _StrategyType: 策略类型。支持WHITE（白名单）和BLACK（黑名单）。
        :type StrategyType: str
        :param _StrategyData: 策略详情，多个ip 使用\n 分隔符分开。
        :type StrategyData: str
        """
        self._ServiceId = None
        self._StrategyName = None
        self._StrategyType = None
        self._StrategyData = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def StrategyData(self):
        return self._StrategyData

    @StrategyData.setter
    def StrategyData(self, StrategyData):
        self._StrategyData = StrategyData


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyName = params.get("StrategyName")
        self._StrategyType = params.get("StrategyType")
        self._StrategyData = params.get("StrategyData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPStrategyResponse(AbstractModel):
    """CreateIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 新建的IP策略详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IPStrategy()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreatePluginRequest(AbstractModel):
    """CreatePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginName: 用户自定义的插件名称。最长50个字符，最短2个字符，支持 a-z,A-Z,0-9,_, 必须字母开头，字母或者数字结尾。
        :type PluginName: str
        :param _PluginType: 插件类型。目前支持IPControl, TrafficControl, Cors, CustomReq, CustomAuth，Routing，TrafficControlByParameter, CircuitBreaker, ProxyCache。
        :type PluginType: str
        :param _PluginData: 插件定义语句，支持json。
        :type PluginData: str
        :param _Description: 插件描述，限定200字以内。
        :type Description: str
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._PluginName = None
        self._PluginType = None
        self._PluginData = None
        self._Description = None
        self._Tags = None

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def PluginData(self):
        return self._PluginData

    @PluginData.setter
    def PluginData(self, PluginData):
        self._PluginData = PluginData

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
        self._PluginName = params.get("PluginName")
        self._PluginType = params.get("PluginType")
        self._PluginData = params.get("PluginData")
        self._Description = params.get("Description")
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
        


class CreatePluginResponse(AbstractModel):
    """CreatePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 新建的插件详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = Plugin()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceName: 用户自定义的服务名称。
        :type ServiceName: str
        :param _Protocol: 服务的前端请求类型。如 http、https、http&https。
        :type Protocol: str
        :param _ServiceDesc: 用户自定义的服务描述。
        :type ServiceDesc: str
        :param _NetTypes: 网络类型列表，用于指定支持的访问类型，INNER为内网访问，OUTER为外网访问。默认为OUTER。
        :type NetTypes: list of str
        :param _IpVersion: IP版本号，仅支持IPv4。
        :type IpVersion: str
        :param _SetServerName: 集群名称。保留字段，tsf serverless类型使用。
        :type SetServerName: str
        :param _AppIdType: 用户类型。保留类型，serverless用户使用。
        :type AppIdType: str
        :param _Tags: 标签。
        :type Tags: list of Tag
        :param _InstanceId: 独享实例id
        :type InstanceId: str
        :param _UniqVpcId: vpc属性，选择VPC后不可修改，为服务选择VPC后，可对接该VPC下的后端资源
        :type UniqVpcId: str
        """
        self._ServiceName = None
        self._Protocol = None
        self._ServiceDesc = None
        self._NetTypes = None
        self._IpVersion = None
        self._SetServerName = None
        self._AppIdType = None
        self._Tags = None
        self._InstanceId = None
        self._UniqVpcId = None

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def SetServerName(self):
        return self._SetServerName

    @SetServerName.setter
    def SetServerName(self, SetServerName):
        self._SetServerName = SetServerName

    @property
    def AppIdType(self):
        return self._AppIdType

    @AppIdType.setter
    def AppIdType(self, AppIdType):
        self._AppIdType = AppIdType

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId


    def _deserialize(self, params):
        self._ServiceName = params.get("ServiceName")
        self._Protocol = params.get("Protocol")
        self._ServiceDesc = params.get("ServiceDesc")
        self._NetTypes = params.get("NetTypes")
        self._IpVersion = params.get("IpVersion")
        self._SetServerName = params.get("SetServerName")
        self._AppIdType = params.get("AppIdType")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceResponse(AbstractModel):
    """CreateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _ServiceName: 用户自定义服务名称。
        :type ServiceName: str
        :param _ServiceDesc: 用户自定义服务描述。
        :type ServiceDesc: str
        :param _OuterSubDomain: 外网默认域名。
        :type OuterSubDomain: str
        :param _InnerSubDomain: vpc内网默认域名。
        :type InnerSubDomain: str
        :param _CreatedTime: 服务创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type CreatedTime: str
        :param _NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。
        :type NetTypes: list of str
        :param _IpVersion: IP版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpVersion: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._OuterSubDomain = None
        self._InnerSubDomain = None
        self._CreatedTime = None
        self._NetTypes = None
        self._IpVersion = None
        self._RequestId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def OuterSubDomain(self):
        return self._OuterSubDomain

    @OuterSubDomain.setter
    def OuterSubDomain(self, OuterSubDomain):
        self._OuterSubDomain = OuterSubDomain

    @property
    def InnerSubDomain(self):
        return self._InnerSubDomain

    @InnerSubDomain.setter
    def InnerSubDomain(self, InnerSubDomain):
        self._InnerSubDomain = InnerSubDomain

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._OuterSubDomain = params.get("OuterSubDomain")
        self._InnerSubDomain = params.get("InnerSubDomain")
        self._CreatedTime = params.get("CreatedTime")
        self._NetTypes = params.get("NetTypes")
        self._IpVersion = params.get("IpVersion")
        self._RequestId = params.get("RequestId")


class CreateUpstreamRequest(AbstractModel):
    """CreateUpstream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Scheme: 后端协议，取值范围：HTTP, HTTPS,gRPC，gRPCs
        :type Scheme: str
        :param _Algorithm: 负载均衡算法，取值范围：ROUND-ROBIN
        :type Algorithm: str
        :param _UniqVpcId: VPC唯一ID
        :type UniqVpcId: str
        :param _UpstreamName: 后端通道名字
        :type UpstreamName: str
        :param _UpstreamDescription: 后端通道描述
        :type UpstreamDescription: str
        :param _UpstreamType: 后端访问类型，取值范围：IP_PORT, K8S
        :type UpstreamType: str
        :param _Retries: 请求重试次数，默认3次
        :type Retries: int
        :param _UpstreamHost: 网关转发到后端的Host请求头
        :type UpstreamHost: str
        :param _Nodes: 后端节点
        :type Nodes: list of UpstreamNode
        :param _Tags: 标签
        :type Tags: list of Tag
        :param _HealthChecker: 健康检查配置，目前只支持VPC通道
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param _K8sService: K8S容器服务的配置
        :type K8sService: list of K8sService
        """
        self._Scheme = None
        self._Algorithm = None
        self._UniqVpcId = None
        self._UpstreamName = None
        self._UpstreamDescription = None
        self._UpstreamType = None
        self._Retries = None
        self._UpstreamHost = None
        self._Nodes = None
        self._Tags = None
        self._HealthChecker = None
        self._K8sService = None

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UpstreamName(self):
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def UpstreamDescription(self):
        return self._UpstreamDescription

    @UpstreamDescription.setter
    def UpstreamDescription(self, UpstreamDescription):
        self._UpstreamDescription = UpstreamDescription

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamHost(self):
        return self._UpstreamHost

    @UpstreamHost.setter
    def UpstreamHost(self, UpstreamHost):
        self._UpstreamHost = UpstreamHost

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HealthChecker(self):
        return self._HealthChecker

    @HealthChecker.setter
    def HealthChecker(self, HealthChecker):
        self._HealthChecker = HealthChecker

    @property
    def K8sService(self):
        return self._K8sService

    @K8sService.setter
    def K8sService(self, K8sService):
        self._K8sService = K8sService


    def _deserialize(self, params):
        self._Scheme = params.get("Scheme")
        self._Algorithm = params.get("Algorithm")
        self._UniqVpcId = params.get("UniqVpcId")
        self._UpstreamName = params.get("UpstreamName")
        self._UpstreamDescription = params.get("UpstreamDescription")
        self._UpstreamType = params.get("UpstreamType")
        self._Retries = params.get("Retries")
        self._UpstreamHost = params.get("UpstreamHost")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("HealthChecker") is not None:
            self._HealthChecker = UpstreamHealthChecker()
            self._HealthChecker._deserialize(params.get("HealthChecker"))
        if params.get("K8sService") is not None:
            self._K8sService = []
            for item in params.get("K8sService"):
                obj = K8sService()
                obj._deserialize(item)
                self._K8sService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUpstreamResponse(AbstractModel):
    """CreateUpstream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UpstreamId: 创建返回的唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UpstreamId = None
        self._RequestId = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._RequestId = params.get("RequestId")


class CreateUsagePlanRequest(AbstractModel):
    """CreateUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanName: 用户自定义的使用计划名称。
        :type UsagePlanName: str
        :param _UsagePlanDesc: 用户自定义的使用计划描述。
        :type UsagePlanDesc: str
        :param _MaxRequestNum: 请求配额总数，取值范围为-1或者[1, 99999999]，默认为-1，表示不开启。
        :type MaxRequestNum: int
        :param _MaxRequestNumPreSec: 每秒请求限制数，取值范围为-1或者[1, 2000]，默认-1，表示不开启。
        :type MaxRequestNumPreSec: int
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNum = None
        self._MaxRequestNumPreSec = None
        self._Tags = None

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
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
        


class CreateUsagePlanResponse(AbstractModel):
    """CreateUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DeleteAPIDocRequest(AbstractModel):
    """DeleteAPIDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self._ApiDocId = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAPIDocResponse(AbstractModel):
    """DeleteAPIDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 操作是否成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApiAppRequest(AbstractModel):
    """DeleteApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiAppId: 应用唯一 ID。
        :type ApiAppId: str
        """
        self._ApiAppId = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiAppResponse(AbstractModel):
    """DeleteApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApiKeyRequest(AbstractModel):
    """DeleteApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 待删除的密钥 ID。
        :type AccessKeyId: str
        """
        self._AccessKeyId = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiKeyResponse(AbstractModel):
    """DeleteApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteApiRequest(AbstractModel):
    """DeleteApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param _ApiId: API 接口唯一 ID。
        :type ApiId: str
        """
        self._ServiceId = None
        self._ApiId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiResponse(AbstractModel):
    """DeleteApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteIPStrategyRequest(AbstractModel):
    """DeleteIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待删除的IP策略所属的服务唯一ID。
        :type ServiceId: str
        :param _StrategyId: 待删除的IP策略唯一ID。
        :type StrategyId: str
        """
        self._ServiceId = None
        self._StrategyId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIPStrategyResponse(AbstractModel):
    """DeleteIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeletePluginRequest(AbstractModel):
    """DeletePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: 要删除的API网关插件的ID。
        :type PluginId: str
        """
        self._PluginId = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePluginResponse(AbstractModel):
    """DeletePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待删除服务的唯一 ID。
        :type ServiceId: str
        :param _SkipVerification: 跳过删除前置条件校验（仅支持独享实例上的服务）
        :type SkipVerification: int
        """
        self._ServiceId = None
        self._SkipVerification = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SkipVerification(self):
        return self._SkipVerification

    @SkipVerification.setter
    def SkipVerification(self, SkipVerification):
        self._SkipVerification = SkipVerification


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SkipVerification = params.get("SkipVerification")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceResponse(AbstractModel):
    """DeleteService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteServiceSubDomainMappingRequest(AbstractModel):
    """DeleteServiceSubDomainMapping请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param _SubDomain: 服务绑定的自定义域名。
        :type SubDomain: str
        :param _Environment: 待删除映射的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。
        :type Environment: str
        """
        self._ServiceId = None
        self._SubDomain = None
        self._Environment = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        self._Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceSubDomainMappingResponse(AbstractModel):
    """DeleteServiceSubDomainMapping返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除自定义域名的路径映射操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DeleteUpstreamRequest(AbstractModel):
    """DeleteUpstream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UpstreamId: 待删除的后端通道ID
        :type UpstreamId: str
        """
        self._UpstreamId = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUpstreamResponse(AbstractModel):
    """DeleteUpstream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UpstreamId: 成功删除的后端通道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UpstreamId = None
        self._RequestId = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._RequestId = params.get("RequestId")


class DeleteUsagePlanRequest(AbstractModel):
    """DeleteUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 待删除的使用计划唯一 ID。
        :type UsagePlanId: str
        """
        self._UsagePlanId = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsagePlanResponse(AbstractModel):
    """DeleteUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DemoteServiceUsagePlanRequest(AbstractModel):
    """DemoteServiceUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 使用计划ID。
        :type UsagePlanId: str
        :param _ServiceId: 待降级的服务唯一 ID。
        :type ServiceId: str
        :param _Environment: 环境名称。
        :type Environment: str
        """
        self._UsagePlanId = None
        self._ServiceId = None
        self._Environment = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._ServiceId = params.get("ServiceId")
        self._Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DemoteServiceUsagePlanResponse(AbstractModel):
    """DemoteServiceUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 降级操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DesApisStatus(AbstractModel):
    """api状态详情

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _ApiId: API唯一ID。
        :type ApiId: str
        :param _ApiDesc: 用户自定义的 API 接口描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _ApiName: API 接口的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param _VpcId: VPCID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param _UniqVpcId: VPC唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _ApiType: API类型。取值为NORMAL（普通API）和TSF（微服务API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param _Protocol: API协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _IsDebugAfterCharge: 是否买后调试。（云市场预留字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDebugAfterCharge: bool
        :param _AuthType: API 鉴权类型。取值为SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH、EIAM。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param _ApiBusinessType: OAUTH API的类型。当AuthType 为 OAUTH时该字段有效， 取值为NORMAL（业务API）和 OAUTH（授权API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiBusinessType: str
        :param _AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthRelationApiId: str
        :param _OauthConfig: OAUTH 配置信息。当AuthType是OAUTH时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _RelationBuniessApiIds: 授权API关联的业务API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationBuniessApiIds: list of str
        :param _Tags: API关联的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _Path: API 的路径，如 /path。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Method: API 的请求方法，如 GET。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiDesc = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiName = None
        self._VpcId = None
        self._UniqVpcId = None
        self._ApiType = None
        self._Protocol = None
        self._IsDebugAfterCharge = None
        self._AuthType = None
        self._ApiBusinessType = None
        self._AuthRelationApiId = None
        self._OauthConfig = None
        self._RelationBuniessApiIds = None
        self._Tags = None
        self._Path = None
        self._Method = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def RelationBuniessApiIds(self):
        warnings.warn("parameter `RelationBuniessApiIds` is deprecated", DeprecationWarning) 

        return self._RelationBuniessApiIds

    @RelationBuniessApiIds.setter
    def RelationBuniessApiIds(self, RelationBuniessApiIds):
        warnings.warn("parameter `RelationBuniessApiIds` is deprecated", DeprecationWarning) 

        self._RelationBuniessApiIds = RelationBuniessApiIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiDesc = params.get("ApiDesc")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiName = params.get("ApiName")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._ApiType = params.get("ApiType")
        self._Protocol = params.get("Protocol")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self._AuthType = params.get("AuthType")
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        self._RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        self._Tags = params.get("Tags")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocDetailRequest(AbstractModel):
    """DescribeAPIDocDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self._ApiDocId = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocDetailResponse(AbstractModel):
    """DescribeAPIDocDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API文档详细信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDocInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAPIDocsRequest(AbstractModel):
    """DescribeAPIDocs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocsResponse(AbstractModel):
    """DescribeAPIDocs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API文档列表信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocs`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDocs()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeAllPluginApisRequest(AbstractModel):
    """DescribeAllPluginApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 要查询的服务ID。
        :type ServiceId: str
        :param _PluginId: 要查询的插件ID。
        :type PluginId: str
        :param _EnvironmentName: 环境信息。
        :type EnvironmentName: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._ServiceId = None
        self._PluginId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._PluginId = params.get("PluginId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllPluginApisResponse(AbstractModel):
    """DescribeAllPluginApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 插件相关API的列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfoSummary`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiInfoSummary()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiAppBindApisStatusRequest(AbstractModel):
    """DescribeApiAppBindApisStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiAppId: 应用ID
        :type ApiAppId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件。支持ApiId、ApiName、ServiceId、Environment 、KeyWord（ 可以匹配name或者ID）。
        :type Filters: list of Filter
        """
        self._ApiAppId = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppBindApisStatusResponse(AbstractModel):
    """DescribeApiAppBindApisStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 应用绑定的Api列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppApiInfos()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiAppRequest(AbstractModel):
    """DescribeApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiAppId: 应用ID。
        :type ApiAppId: str
        """
        self._ApiAppId = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppResponse(AbstractModel):
    """DescribeApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 应用详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppInfos()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiAppsStatusRequest(AbstractModel):
    """DescribeApiAppsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件。支持ApiAppId、ApiAppName、KeyWord（ 可以匹配name或者ID）。
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppsStatusResponse(AbstractModel):
    """DescribeApiAppsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 应用列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppInfos()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiBindApiAppsStatusRequest(AbstractModel):
    """DescribeApiBindApiAppsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _ApiIds: Api的ID的数组
        :type ApiIds: list of str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件。支持ApiAppId、Environment、KeyWord（ 可以匹配name或者ID）。
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._ApiIds = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiIds = params.get("ApiIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiBindApiAppsStatusResponse(AbstractModel):
    """DescribeApiBindApiAppsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 应用绑定的Api列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiAppApiInfos()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiEnvironmentStrategyRequest(AbstractModel):
    """DescribeApiEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: API所属服务唯一ID。
        :type ServiceId: str
        :param _EnvironmentNames: 环境列表。
        :type EnvironmentNames: list of str
        :param _ApiId: API唯一ID。
        :type ApiId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._ServiceId = None
        self._EnvironmentNames = None
        self._ApiId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentNames(self):
        return self._EnvironmentNames

    @EnvironmentNames.setter
    def EnvironmentNames(self, EnvironmentNames):
        self._EnvironmentNames = EnvironmentNames

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentNames = params.get("EnvironmentNames")
        self._ApiId = params.get("ApiId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiEnvironmentStrategyResponse(AbstractModel):
    """DescribeApiEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: api绑定策略详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiEnvironmentStrategyStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiEnvironmentStrategyStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiForApiAppRequest(AbstractModel):
    """DescribeApiForApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param _ApiId: API 接口唯一 ID。
        :type ApiId: str
        :param _ApiRegion: Api所属地域
        :type ApiRegion: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiRegion = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiRegion(self):
        return self._ApiRegion

    @ApiRegion.setter
    def ApiRegion(self, ApiRegion):
        self._ApiRegion = ApiRegion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiRegion = params.get("ApiRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiForApiAppResponse(AbstractModel):
    """DescribeApiForApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API 详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiKeyRequest(AbstractModel):
    """DescribeApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: API 密钥 ID。
        :type AccessKeyId: str
        """
        self._AccessKeyId = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeyResponse(AbstractModel):
    """DescribeApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 密钥详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiKey()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiKeysStatusRequest(AbstractModel):
    """DescribeApiKeysStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件。支持AccessKeyId、AccessKeySecret、SecretName、NotUsagePlanId、Status、KeyWord（ 可以匹配name或者path）。
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeysStatusResponse(AbstractModel):
    """DescribeApiKeysStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 密钥列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKeysStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiKeysStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiRequest(AbstractModel):
    """DescribeApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param _ApiId: API 接口唯一 ID。
        :type ApiId: str
        """
        self._ServiceId = None
        self._ApiId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiResponse(AbstractModel):
    """DescribeApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API 详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApiResultServiceParametersInfo(AbstractModel):
    """ServiceParameter

    """

    def __init__(self):
        r"""
        :param _Name: API的后端服务参数名称。只有ServiceType是HTTP才会用到此参数。前后端参数名称可不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Position: API 的后端服务参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。前后端参数位置可配置不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: str
        :param _RelevantRequestParameterPosition: API 的后端服务参数对应的前端参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterPosition: str
        :param _RelevantRequestParameterName: API 的后端服务参数对应的前端参数名称。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterName: str
        :param _DefaultValue: API 的后端服务参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        :param _RelevantRequestParameterDesc: API 的后端服务参数备注。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterDesc: str
        """
        self._Name = None
        self._Position = None
        self._RelevantRequestParameterPosition = None
        self._RelevantRequestParameterName = None
        self._DefaultValue = None
        self._RelevantRequestParameterDesc = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def RelevantRequestParameterPosition(self):
        return self._RelevantRequestParameterPosition

    @RelevantRequestParameterPosition.setter
    def RelevantRequestParameterPosition(self, RelevantRequestParameterPosition):
        self._RelevantRequestParameterPosition = RelevantRequestParameterPosition

    @property
    def RelevantRequestParameterName(self):
        return self._RelevantRequestParameterName

    @RelevantRequestParameterName.setter
    def RelevantRequestParameterName(self, RelevantRequestParameterName):
        self._RelevantRequestParameterName = RelevantRequestParameterName

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def RelevantRequestParameterDesc(self):
        return self._RelevantRequestParameterDesc

    @RelevantRequestParameterDesc.setter
    def RelevantRequestParameterDesc(self, RelevantRequestParameterDesc):
        self._RelevantRequestParameterDesc = RelevantRequestParameterDesc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Position = params.get("Position")
        self._RelevantRequestParameterPosition = params.get("RelevantRequestParameterPosition")
        self._RelevantRequestParameterName = params.get("RelevantRequestParameterName")
        self._DefaultValue = params.get("DefaultValue")
        self._RelevantRequestParameterDesc = params.get("RelevantRequestParameterDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiUsagePlanRequest(AbstractModel):
    """DescribeApiUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiUsagePlanResponse(AbstractModel):
    """DescribeApiUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: api绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiUsagePlanSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiUsagePlanSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApisStatusRequest(AbstractModel):
    """DescribeApisStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param _Filters: API过滤条件。支持ApiId、ApiName、ApiPath、ApiType、AuthRelationApiId、AuthType、ApiBuniessType、NotUsagePlanId、 Environment、Tags (values为 $tag_key:tag_value的列表)、TagKeys （values 为 tag key的列表），其中NotUsagePlanId和Environment必须同时使用，不能单独使用一个。
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApisStatusResponse(AbstractModel):
    """DescribeApisStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API 详情列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeApisStatusResultInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeApisStatusResultInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeApisStatusResultApiIdStatusSetInfo(AbstractModel):
    """api状态详情

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _ApiId: API唯一ID。
        :type ApiId: str
        :param _ApiDesc: 用户自定义的 API 接口描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _ApiName: API 接口的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param _VpcId: VPCID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param _UniqVpcId: VPC唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _ApiType: API类型。取值为NORMAL（普通API）和TSF（微服务API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param _Protocol: API协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _IsDebugAfterCharge: 是否买后调试。（云市场预留字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDebugAfterCharge: bool
        :param _AuthType: API 鉴权类型。取值为SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH、EIAM。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param _ApiBusinessType: OAUTH API的类型。当AuthType 为 OAUTH时该字段有效， 取值为NORMAL（业务API）和 OAUTH（授权API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiBusinessType: str
        :param _AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthRelationApiId: str
        :param _OauthConfig: OAUTH 配置信息。当AuthType是OAUTH时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _RelationBuniessApiIds: 授权API关联的业务API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationBuniessApiIds: list of str
        :param _Tags: API关联的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApigatewayTags
        :param _Path: API 的路径，如 /path。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Method: API 的请求方法，如 GET。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiDesc = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ApiName = None
        self._VpcId = None
        self._UniqVpcId = None
        self._ApiType = None
        self._Protocol = None
        self._IsDebugAfterCharge = None
        self._AuthType = None
        self._ApiBusinessType = None
        self._AuthRelationApiId = None
        self._OauthConfig = None
        self._RelationBuniessApiIds = None
        self._Tags = None
        self._Path = None
        self._Method = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def RelationBuniessApiIds(self):
        warnings.warn("parameter `RelationBuniessApiIds` is deprecated", DeprecationWarning) 

        return self._RelationBuniessApiIds

    @RelationBuniessApiIds.setter
    def RelationBuniessApiIds(self, RelationBuniessApiIds):
        warnings.warn("parameter `RelationBuniessApiIds` is deprecated", DeprecationWarning) 

        self._RelationBuniessApiIds = RelationBuniessApiIds

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiDesc = params.get("ApiDesc")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ApiName = params.get("ApiName")
        self._VpcId = params.get("VpcId")
        self._UniqVpcId = params.get("UniqVpcId")
        self._ApiType = params.get("ApiType")
        self._Protocol = params.get("Protocol")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self._AuthType = params.get("AuthType")
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        self._RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = ApigatewayTags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApisStatusResultInfo(AbstractModel):
    """描述api列表状态

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的 API 接口数量。
        :type TotalCount: int
        :param _ApiIdStatusSet: API 接口列表。
        :type ApiIdStatusSet: list of DescribeApisStatusResultApiIdStatusSetInfo
        """
        self._TotalCount = None
        self._ApiIdStatusSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiIdStatusSet(self):
        return self._ApiIdStatusSet

    @ApiIdStatusSet.setter
    def ApiIdStatusSet(self, ApiIdStatusSet):
        self._ApiIdStatusSet = ApiIdStatusSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self._ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = DescribeApisStatusResultApiIdStatusSetInfo()
                obj._deserialize(item)
                self._ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExclusiveInstanceDetailRequest(AbstractModel):
    """DescribeExclusiveInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享实例唯一id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExclusiveInstanceDetailResponse(AbstractModel):
    """DescribeExclusiveInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 独享实例详情
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.InstanceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = InstanceDetail()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeExclusiveInstanceRegionsRequest(AbstractModel):
    """DescribeExclusiveInstanceRegions请求参数结构体

    """


class DescribeExclusiveInstanceRegionsResponse(AbstractModel):
    """DescribeExclusiveInstanceRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeExclusiveInstancesRequest(AbstractModel):
    """DescribeExclusiveInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页查询，limit
        :type Limit: int
        :param _Offset: 分页查询，offset
        :type Offset: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExclusiveInstancesResponse(AbstractModel):
    """DescribeExclusiveInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 独享实例列表查询结果
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeExclusiveInstancesResult`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeExclusiveInstancesResult()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeExclusiveInstancesResult(AbstractModel):
    """数据结构

    """


class DescribeExclusiveInstancesStatusRequest(AbstractModel):
    """DescribeExclusiveInstancesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页查询，limit
        :type Limit: int
        :param _Offset: 分页查询，offset
        :type Offset: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExclusiveInstancesStatusResponse(AbstractModel):
    """DescribeExclusiveInstancesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 独享实例列表查询结果
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.InstanceSummary`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = InstanceSummary()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIPStrategyApisStatusRequest(AbstractModel):
    """DescribeIPStrategyApisStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _StrategyId: 策略唯一ID。
        :type StrategyId: str
        :param _EnvironmentName: 策略所在环境。
        :type EnvironmentName: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件。支持 ApiPath、ApiName、KeyWord（模糊查询Path 和Name）。
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._StrategyId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategyApisStatusResponse(AbstractModel):
    """DescribeIPStrategyApisStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 环境绑定API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategyApiStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IPStrategyApiStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIPStrategyRequest(AbstractModel):
    """DescribeIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _StrategyId: IP 策略唯一ID。
        :type StrategyId: str
        :param _EnvironmentName: 策略关联的环境。
        :type EnvironmentName: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件。预留字段，目前不支持过滤。
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._StrategyId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategyResponse(AbstractModel):
    """DescribeIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: IP策略详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IPStrategy()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeIPStrategysStatusRequest(AbstractModel):
    """DescribeIPStrategysStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _Filters: 过滤条件。支持StrategyName。
        :type Filters: list of Filter
        """
        self._ServiceId = None
        self._Filters = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategysStatusResponse(AbstractModel):
    """DescribeIPStrategysStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 符合条件的策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategiesStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = IPStrategiesStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeLogSearchRequest(AbstractModel):
    """DescribeLogSearch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 日志开始时间
        :type StartTime: str
        :param _EndTime: 日志结束时间
        :type EndTime: str
        :param _ServiceId: 服务id
        :type ServiceId: str
        :param _Filters: 保留字段
        :type Filters: list of Filter
        :param _Limit: 单次要返回的日志条数，单次返回的最大条数为100
        :type Limit: int
        :param _ConText: 根据上次返回的ConText，获取后续的内容，最多可获取10000条
        :type ConText: str
        :param _Sort: 按时间排序 asc（升序）或者 desc（降序），默认为 desc
        :type Sort: str
        :param _Query: 保留字段
        :type Query: str
        :param _LogQuerys: 检索条件,支持的检索条件如下：
req_id：“=”
api_id：“=”
cip：“=”
uip：“:”
err_msg：“:”
rsp_st：“=” 、“!=” 、 “:” 、 “>” 、 “<”
req_t：”>=“ 、 ”<=“

说明：
“:”表示包含，“!=”表示不等于，字段含义见输出参数的LogSet说明
        :type LogQuerys: list of LogQuery
        """
        self._StartTime = None
        self._EndTime = None
        self._ServiceId = None
        self._Filters = None
        self._Limit = None
        self._ConText = None
        self._Sort = None
        self._Query = None
        self._LogQuerys = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ConText(self):
        return self._ConText

    @ConText.setter
    def ConText(self, ConText):
        self._ConText = ConText

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def LogQuerys(self):
        warnings.warn("parameter `LogQuerys` is deprecated", DeprecationWarning) 

        return self._LogQuerys

    @LogQuerys.setter
    def LogQuerys(self, LogQuerys):
        warnings.warn("parameter `LogQuerys` is deprecated", DeprecationWarning) 

        self._LogQuerys = LogQuerys


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ServiceId = params.get("ServiceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._ConText = params.get("ConText")
        self._Sort = params.get("Sort")
        self._Query = params.get("Query")
        if params.get("LogQuerys") is not None:
            self._LogQuerys = []
            for item in params.get("LogQuerys"):
                obj = LogQuery()
                obj._deserialize(item)
                self._LogQuerys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogSearchResponse(AbstractModel):
    """DescribeLogSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ConText: 获取更多检索结果的游标，值为""表示无后续结果
        :type ConText: str
        :param _LogSet: 由0或多条日志组成，每条日志格式如下：
'[$app_id][$env_name][$service_id][$http_host][$api_id][$uri][$scheme][rsp_st:$status][ups_st:$upstream_status]'
'[cip:$remote_addr][uip:$upstream_addr][vip:$server_addr][rsp_len:$bytes_sent][req_len:$request_length]'
'[req_t:$request_time][ups_rsp_t:$upstream_response_time][ups_conn_t:$upstream_connect_time][ups_head_t:$upstream_header_time]’
'[err_msg:$err_msg][tcp_rtt:$tcpinfo_rtt][$pid][$time_local][req_id:$request_id]';

说明：
app_id： 用户 ID。
env_name：环境名称。
service_id： 服务 ID。
http_host： 域名。
api_id： API 的 ID。
uri：请求的路径。
scheme： HTTP/HTTPS 协议。
rsp_st： 请求响应状态码。
ups_st： 后端业务服务器的响应状态码（如果请求透传到后端，改变量不为空。如果请求在 APIGW 就被拦截了，那么该变量显示为 -）。
cip： 客户端 IP。
uip： 后端业务服务（upstream）的 IP。
vip： 请求访问的 VIP。
rsp_len： 响应长度。
req_len： 请求长度。
req_t： 请求响应的总时间。
ups_rsp_t： 后端响应的总时间（apigw 建立连接到接收到后端响应的时间）。
ups_conn_t: 与后端业务服务器连接建立成功时间。
ups_head_t：后端响应的头部到达时间。
err_msg： 错误信息。
tcp_rtt： 客户端 TCP 连接信息，RTT（Round Trip Time）由三部分组成：链路的传播时间（propagation delay）、末端系统的处理时间、路由器缓存中的排队和处理时间（queuing delay）。
req_id：请求id。
        :type LogSet: list of str
        :param _TotalCount: 单次搜索返回的日志条数，TotalCount <= Limit
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ConText = None
        self._LogSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ConText(self):
        return self._ConText

    @ConText.setter
    def ConText(self, ConText):
        self._ConText = ConText

    @property
    def LogSet(self):
        return self._LogSet

    @LogSet.setter
    def LogSet(self, LogSet):
        self._LogSet = LogSet

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ConText = params.get("ConText")
        self._LogSet = params.get("LogSet")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePluginApisRequest(AbstractModel):
    """DescribePluginApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: 查询的插件ID。
        :type PluginId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._PluginId = None
        self._Limit = None
        self._Offset = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginApisResponse(AbstractModel):
    """DescribePluginApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 插件绑定的API列表信息。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedApiSummary`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AttachedApiSummary()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePluginRequest(AbstractModel):
    """DescribePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: 要查询的插件ID。
        :type PluginId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._PluginId = None
        self._Limit = None
        self._Offset = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginResponse(AbstractModel):
    """DescribePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 插件详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = Plugin()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePluginsByApiRequest(AbstractModel):
    """DescribePluginsByApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiId: 要查询的API ID。
        :type ApiId: str
        :param _ServiceId: 要查询的服务ID。
        :type ServiceId: str
        :param _EnvironmentName: 环境信息。
        :type EnvironmentName: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._ApiId = None
        self._ServiceId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginsByApiResponse(AbstractModel):
    """DescribePluginsByApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 插件可绑定的API列表信息。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedPluginSummary`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = AttachedPluginSummary()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribePluginsRequest(AbstractModel):
    """DescribePlugins请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginIds: 要查询的插件列表。
        :type PluginIds: list of str
        :param _PluginName: 要查询的插件名称。
        :type PluginName: str
        :param _PluginType: 要查询的插件类型。
        :type PluginType: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件。预留字段，目前不支持过滤。
        :type Filters: list of Filter
        """
        self._PluginIds = None
        self._PluginName = None
        self._PluginType = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def PluginIds(self):
        return self._PluginIds

    @PluginIds.setter
    def PluginIds(self, PluginIds):
        self._PluginIds = PluginIds

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._PluginIds = params.get("PluginIds")
        self._PluginName = params.get("PluginName")
        self._PluginType = params.get("PluginType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginsResponse(AbstractModel):
    """DescribePlugins返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 插件详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.PluginSummary`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = PluginSummary()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceEnvironmentListRequest(AbstractModel):
    """DescribeServiceEnvironmentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentListResponse(AbstractModel):
    """DescribeServiceEnvironmentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 服务绑定环境详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceEnvironmentSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceEnvironmentReleaseHistoryRequest(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param _EnvironmentName: 环境名称。
        :type EnvironmentName: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._ServiceId = None
        self._EnvironmentName = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentReleaseHistoryResponse(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 服务发布历史。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseHistory`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceReleaseHistory()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceEnvironmentStrategyRequest(AbstractModel):
    """DescribeServiceEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentStrategyResponse(AbstractModel):
    """DescribeServiceEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentStrategyStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceEnvironmentStrategyStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceForApiAppRequest(AbstractModel):
    """DescribeServiceForApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param _ApiRegion: 服务所属的地域
        :type ApiRegion: str
        """
        self._ServiceId = None
        self._ApiRegion = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiRegion(self):
        return self._ApiRegion

    @ApiRegion.setter
    def ApiRegion(self, ApiRegion):
        self._ApiRegion = ApiRegion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiRegion = params.get("ApiRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceForApiAppResponse(AbstractModel):
    """DescribeServiceForApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _AvailableEnvironments: 服务 环境列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableEnvironments: list of str
        :param _ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _ServiceDesc: 服务描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param _Protocol: 服务支持协议，可选值为http、https、http&https。
        :type Protocol: str
        :param _CreatedTime: 服务创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 服务修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。
        :type NetTypes: list of str
        :param _InternalSubDomain: 内网访问子域名。
        :type InternalSubDomain: str
        :param _OuterSubDomain: 外网访问子域名。
        :type OuterSubDomain: str
        :param _InnerHttpPort: 内网访问http服务端口号。
        :type InnerHttpPort: int
        :param _InnerHttpsPort: 内网访问https端口号。
        :type InnerHttpsPort: int
        :param _ApiTotalCount: API总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiTotalCount: int
        :param _ApiIdStatusSet: API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiIdStatusSet: list of ApiIdStatus
        :param _UsagePlanTotalCount: 使用计划总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanTotalCount: int
        :param _UsagePlanList: 使用计划数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanList: list of UsagePlan
        :param _IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpVersion: str
        :param _UserType: 此服务的用户类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param _SetId: 预留字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type SetId: int
        :param _Tags: 服务绑定的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceId = None
        self._AvailableEnvironments = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._Protocol = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._NetTypes = None
        self._InternalSubDomain = None
        self._OuterSubDomain = None
        self._InnerHttpPort = None
        self._InnerHttpsPort = None
        self._ApiTotalCount = None
        self._ApiIdStatusSet = None
        self._UsagePlanTotalCount = None
        self._UsagePlanList = None
        self._IpVersion = None
        self._UserType = None
        self._SetId = None
        self._Tags = None
        self._RequestId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def AvailableEnvironments(self):
        return self._AvailableEnvironments

    @AvailableEnvironments.setter
    def AvailableEnvironments(self, AvailableEnvironments):
        self._AvailableEnvironments = AvailableEnvironments

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def InternalSubDomain(self):
        return self._InternalSubDomain

    @InternalSubDomain.setter
    def InternalSubDomain(self, InternalSubDomain):
        self._InternalSubDomain = InternalSubDomain

    @property
    def OuterSubDomain(self):
        return self._OuterSubDomain

    @OuterSubDomain.setter
    def OuterSubDomain(self, OuterSubDomain):
        self._OuterSubDomain = OuterSubDomain

    @property
    def InnerHttpPort(self):
        return self._InnerHttpPort

    @InnerHttpPort.setter
    def InnerHttpPort(self, InnerHttpPort):
        self._InnerHttpPort = InnerHttpPort

    @property
    def InnerHttpsPort(self):
        return self._InnerHttpsPort

    @InnerHttpsPort.setter
    def InnerHttpsPort(self, InnerHttpsPort):
        self._InnerHttpsPort = InnerHttpsPort

    @property
    def ApiTotalCount(self):
        return self._ApiTotalCount

    @ApiTotalCount.setter
    def ApiTotalCount(self, ApiTotalCount):
        self._ApiTotalCount = ApiTotalCount

    @property
    def ApiIdStatusSet(self):
        return self._ApiIdStatusSet

    @ApiIdStatusSet.setter
    def ApiIdStatusSet(self, ApiIdStatusSet):
        self._ApiIdStatusSet = ApiIdStatusSet

    @property
    def UsagePlanTotalCount(self):
        return self._UsagePlanTotalCount

    @UsagePlanTotalCount.setter
    def UsagePlanTotalCount(self, UsagePlanTotalCount):
        self._UsagePlanTotalCount = UsagePlanTotalCount

    @property
    def UsagePlanList(self):
        return self._UsagePlanList

    @UsagePlanList.setter
    def UsagePlanList(self, UsagePlanList):
        self._UsagePlanList = UsagePlanList

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._AvailableEnvironments = params.get("AvailableEnvironments")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._Protocol = params.get("Protocol")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._NetTypes = params.get("NetTypes")
        self._InternalSubDomain = params.get("InternalSubDomain")
        self._OuterSubDomain = params.get("OuterSubDomain")
        self._InnerHttpPort = params.get("InnerHttpPort")
        self._InnerHttpsPort = params.get("InnerHttpsPort")
        self._ApiTotalCount = params.get("ApiTotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self._ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = ApiIdStatus()
                obj._deserialize(item)
                self._ApiIdStatusSet.append(obj)
        self._UsagePlanTotalCount = params.get("UsagePlanTotalCount")
        if params.get("UsagePlanList") is not None:
            self._UsagePlanList = []
            for item in params.get("UsagePlanList"):
                obj = UsagePlan()
                obj._deserialize(item)
                self._UsagePlanList.append(obj)
        self._IpVersion = params.get("IpVersion")
        self._UserType = params.get("UserType")
        self._SetId = params.get("SetId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeServiceReleaseVersionRequest(AbstractModel):
    """DescribeServiceReleaseVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceReleaseVersionResponse(AbstractModel):
    """DescribeServiceReleaseVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 服务发布版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseVersion`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceReleaseVersion()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceReleaseVersionResultVersionListInfo(AbstractModel):
    """服务发布列表详情

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _VersionDesc: 版本描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionDesc: str
        """
        self._VersionName = None
        self._VersionDesc = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionDesc(self):
        return self._VersionDesc

    @VersionDesc.setter
    def VersionDesc(self, VersionDesc):
        self._VersionDesc = VersionDesc


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._VersionDesc = params.get("VersionDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceRequest(AbstractModel):
    """DescribeService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        """
        self._ServiceId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceResponse(AbstractModel):
    """DescribeService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _AvailableEnvironments: 服务 环境列表。
        :type AvailableEnvironments: list of str
        :param _ServiceName: 服务名称。
        :type ServiceName: str
        :param _ServiceDesc: 服务描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param _Protocol: 服务支持协议，可选值为http、https、http&https。
        :type Protocol: str
        :param _CreatedTime: 服务创建时间。
        :type CreatedTime: str
        :param _ModifiedTime: 服务修改时间。
        :type ModifiedTime: str
        :param _NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。
        :type NetTypes: list of str
        :param _InternalSubDomain: 内网访问子域名。
        :type InternalSubDomain: str
        :param _OuterSubDomain: 外网访问子域名。
        :type OuterSubDomain: str
        :param _InnerHttpPort: 内网访问http服务端口号。
        :type InnerHttpPort: int
        :param _InnerHttpsPort: 内网访问https端口号。
        :type InnerHttpsPort: int
        :param _ApiTotalCount: API总数。
        :type ApiTotalCount: int
        :param _ApiIdStatusSet: API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiIdStatusSet: list of ApiIdStatus
        :param _UsagePlanTotalCount: 使用计划总数量。
        :type UsagePlanTotalCount: int
        :param _UsagePlanList: 使用计划数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanList: list of UsagePlan
        :param _IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpVersion: str
        :param _UserType: 此服务的用户类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param _SetId: 预留字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type SetId: int
        :param _Tags: 服务绑定的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _InstanceId: 独享实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 独享实例name
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _SetType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SetType: str
        :param _DeploymentType: 服务部署的集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentType: str
        :param _SpecialUse: 特殊用途, NULL和DEFAULT表示无特殊用途，其他用途如HTTP_DNS等
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialUse: str
        :param _UniqVpcId: vpc属性，存量可能为空字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceId = None
        self._AvailableEnvironments = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._Protocol = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._NetTypes = None
        self._InternalSubDomain = None
        self._OuterSubDomain = None
        self._InnerHttpPort = None
        self._InnerHttpsPort = None
        self._ApiTotalCount = None
        self._ApiIdStatusSet = None
        self._UsagePlanTotalCount = None
        self._UsagePlanList = None
        self._IpVersion = None
        self._UserType = None
        self._SetId = None
        self._Tags = None
        self._InstanceId = None
        self._InstanceName = None
        self._SetType = None
        self._DeploymentType = None
        self._SpecialUse = None
        self._UniqVpcId = None
        self._RequestId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def AvailableEnvironments(self):
        return self._AvailableEnvironments

    @AvailableEnvironments.setter
    def AvailableEnvironments(self, AvailableEnvironments):
        self._AvailableEnvironments = AvailableEnvironments

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def InternalSubDomain(self):
        return self._InternalSubDomain

    @InternalSubDomain.setter
    def InternalSubDomain(self, InternalSubDomain):
        self._InternalSubDomain = InternalSubDomain

    @property
    def OuterSubDomain(self):
        return self._OuterSubDomain

    @OuterSubDomain.setter
    def OuterSubDomain(self, OuterSubDomain):
        self._OuterSubDomain = OuterSubDomain

    @property
    def InnerHttpPort(self):
        return self._InnerHttpPort

    @InnerHttpPort.setter
    def InnerHttpPort(self, InnerHttpPort):
        self._InnerHttpPort = InnerHttpPort

    @property
    def InnerHttpsPort(self):
        return self._InnerHttpsPort

    @InnerHttpsPort.setter
    def InnerHttpsPort(self, InnerHttpsPort):
        self._InnerHttpsPort = InnerHttpsPort

    @property
    def ApiTotalCount(self):
        return self._ApiTotalCount

    @ApiTotalCount.setter
    def ApiTotalCount(self, ApiTotalCount):
        self._ApiTotalCount = ApiTotalCount

    @property
    def ApiIdStatusSet(self):
        return self._ApiIdStatusSet

    @ApiIdStatusSet.setter
    def ApiIdStatusSet(self, ApiIdStatusSet):
        self._ApiIdStatusSet = ApiIdStatusSet

    @property
    def UsagePlanTotalCount(self):
        return self._UsagePlanTotalCount

    @UsagePlanTotalCount.setter
    def UsagePlanTotalCount(self, UsagePlanTotalCount):
        self._UsagePlanTotalCount = UsagePlanTotalCount

    @property
    def UsagePlanList(self):
        return self._UsagePlanList

    @UsagePlanList.setter
    def UsagePlanList(self, UsagePlanList):
        self._UsagePlanList = UsagePlanList

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def UserType(self):
        return self._UserType

    @UserType.setter
    def UserType(self, UserType):
        self._UserType = UserType

    @property
    def SetId(self):
        return self._SetId

    @SetId.setter
    def SetId(self, SetId):
        self._SetId = SetId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def SetType(self):
        return self._SetType

    @SetType.setter
    def SetType(self, SetType):
        self._SetType = SetType

    @property
    def DeploymentType(self):
        return self._DeploymentType

    @DeploymentType.setter
    def DeploymentType(self, DeploymentType):
        self._DeploymentType = DeploymentType

    @property
    def SpecialUse(self):
        return self._SpecialUse

    @SpecialUse.setter
    def SpecialUse(self, SpecialUse):
        self._SpecialUse = SpecialUse

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._AvailableEnvironments = params.get("AvailableEnvironments")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._Protocol = params.get("Protocol")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._NetTypes = params.get("NetTypes")
        self._InternalSubDomain = params.get("InternalSubDomain")
        self._OuterSubDomain = params.get("OuterSubDomain")
        self._InnerHttpPort = params.get("InnerHttpPort")
        self._InnerHttpsPort = params.get("InnerHttpsPort")
        self._ApiTotalCount = params.get("ApiTotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self._ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = ApiIdStatus()
                obj._deserialize(item)
                self._ApiIdStatusSet.append(obj)
        self._UsagePlanTotalCount = params.get("UsagePlanTotalCount")
        if params.get("UsagePlanList") is not None:
            self._UsagePlanList = []
            for item in params.get("UsagePlanList"):
                obj = UsagePlan()
                obj._deserialize(item)
                self._UsagePlanList.append(obj)
        self._IpVersion = params.get("IpVersion")
        self._UserType = params.get("UserType")
        self._SetId = params.get("SetId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._SetType = params.get("SetType")
        self._DeploymentType = params.get("DeploymentType")
        self._SpecialUse = params.get("SpecialUse")
        self._UniqVpcId = params.get("UniqVpcId")
        self._RequestId = params.get("RequestId")


class DescribeServiceSubDomainMappingsRequest(AbstractModel):
    """DescribeServiceSubDomainMappings请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param _SubDomain: 服务绑定的自定义域名。
        :type SubDomain: str
        """
        self._ServiceId = None
        self._SubDomain = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceSubDomainMappingsResponse(AbstractModel):
    """DescribeServiceSubDomainMappings返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 自定义路径映射列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceSubDomainMappings`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceSubDomainMappings()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceSubDomainsRequest(AbstractModel):
    """DescribeServiceSubDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceSubDomainsResponse(AbstractModel):
    """DescribeServiceSubDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询服务自定义域名列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DomainSets`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DomainSets()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServiceUsagePlanRequest(AbstractModel):
    """DescribeServiceUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._ServiceId = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceUsagePlanResponse(AbstractModel):
    """DescribeServiceUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 服务绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceUsagePlanSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServiceUsagePlanSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeServicesStatusRequest(AbstractModel):
    """DescribeServicesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件。支持ServiceId、ServiceName、NotUsagePlanId、Environment、IpVersion、InstanceId、NetType、EIAMAppId。
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServicesStatusResponse(AbstractModel):
    """DescribeServicesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 服务列表查询结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServicesStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ServicesStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUpstreamBindApis(AbstractModel):
    """查询后端通道绑定API列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _BindApiSet: 绑定的API信息
        :type BindApiSet: list of BindApiInfo
        """
        self._TotalCount = None
        self._BindApiSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BindApiSet(self):
        return self._BindApiSet

    @BindApiSet.setter
    def BindApiSet(self, BindApiSet):
        self._BindApiSet = BindApiSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("BindApiSet") is not None:
            self._BindApiSet = []
            for item in params.get("BindApiSet"):
                obj = BindApiInfo()
                obj._deserialize(item)
                self._BindApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamBindApisRequest(AbstractModel):
    """DescribeUpstreamBindApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页起始位置
        :type Offset: int
        :param _UpstreamId: 后端通道ID
        :type UpstreamId: str
        :param _Filters: ServiceId和ApiId过滤查询
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._UpstreamId = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._UpstreamId = params.get("UpstreamId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamBindApisResponse(AbstractModel):
    """DescribeUpstreamBindApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询结果
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamBindApis`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeUpstreamBindApis()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUpstreamInfo(AbstractModel):
    """查询后端通道返回信息

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _UpstreamSet: 查询列表
        :type UpstreamSet: list of UpstreamInfo
        """
        self._TotalCount = None
        self._UpstreamSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UpstreamSet(self):
        return self._UpstreamSet

    @UpstreamSet.setter
    def UpstreamSet(self, UpstreamSet):
        self._UpstreamSet = UpstreamSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UpstreamSet") is not None:
            self._UpstreamSet = []
            for item in params.get("UpstreamSet"):
                obj = UpstreamInfo()
                obj._deserialize(item)
                self._UpstreamSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamsRequest(AbstractModel):
    """DescribeUpstreams请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小
        :type Limit: int
        :param _Offset: 分页起始位置
        :type Offset: int
        :param _Filters: 过滤条件，支持后端通道ID（UpstreamId）、后端通道名字（UpstreamName）过滤查询
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamsResponse(AbstractModel):
    """DescribeUpstreams返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 查询结果
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = DescribeUpstreamInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUsagePlanEnvironmentsRequest(AbstractModel):
    """DescribeUsagePlanEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 待查询的使用计划唯一 ID。
        :type UsagePlanId: str
        :param _BindType: 定义类型，取值为 API、SERVICE，默认值为 SERVICE。
        :type BindType: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._UsagePlanId = None
        self._BindType = None
        self._Limit = None
        self._Offset = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def BindType(self):
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._BindType = params.get("BindType")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanEnvironmentsResponse(AbstractModel):
    """DescribeUsagePlanEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 使用计划绑定详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanEnvironmentStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanEnvironmentStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUsagePlanRequest(AbstractModel):
    """DescribeUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 待查询的使用计划唯一 ID。
        :type UsagePlanId: str
        """
        self._UsagePlanId = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanResponse(AbstractModel):
    """DescribeUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUsagePlanSecretIdsRequest(AbstractModel):
    """DescribeUsagePlanSecretIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 绑定的使用计划唯一 ID。
        :type UsagePlanId: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self._UsagePlanId = None
        self._Limit = None
        self._Offset = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanSecretIdsResponse(AbstractModel):
    """DescribeUsagePlanSecretIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 使用计划绑定的密钥列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanBindSecretStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanBindSecretStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DescribeUsagePlansStatusRequest(AbstractModel):
    """DescribeUsagePlansStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 使用计划过滤条件。支持UsagePlanId、UsagePlanName、NotServiceId、NotApiId、Environment。
        :type Filters: list of Filter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlansStatusResponse(AbstractModel):
    """DescribeUsagePlansStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlansStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlansStatus()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class DetachPluginRequest(AbstractModel):
    """DetachPlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: 要解绑的API网关插件ID。
        :type PluginId: str
        :param _ServiceId: 要操作的服务ID。
        :type ServiceId: str
        :param _EnvironmentName: 要操作API的环境。
        :type EnvironmentName: str
        :param _ApiId: 要解绑的API ID。
        :type ApiId: str
        """
        self._PluginId = None
        self._ServiceId = None
        self._EnvironmentName = None
        self._ApiId = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachPluginResponse(AbstractModel):
    """DetachPlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 解绑操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DisableApiKeyRequest(AbstractModel):
    """DisableApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 待禁用的密钥 ID。
        :type AccessKeyId: str
        """
        self._AccessKeyId = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApiKeyResponse(AbstractModel):
    """DisableApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 禁用密钥操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DomainSetList(AbstractModel):
    """服务自定义域名列表

    """

    def __init__(self):
        r"""
        :param _DomainName: 域名名称。
        :type DomainName: str
        :param _Status: 域名解析状态。1 表示正常解析，0 表示解析失败。
        :type Status: int
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        :param _IsDefaultMapping: 是否使用默认路径映射。
        :type IsDefaultMapping: bool
        :param _Protocol: 自定义域名协议类型。
        :type Protocol: str
        :param _NetType: 网络类型（'INNER' 或 'OUTER'）。
        :type NetType: str
        :param _IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。
        :type IsForcedHttps: bool
        :param _RegistrationStatus: 域名备案注册状态
        :type RegistrationStatus: bool
        """
        self._DomainName = None
        self._Status = None
        self._CertificateId = None
        self._IsDefaultMapping = None
        self._Protocol = None
        self._NetType = None
        self._IsForcedHttps = None
        self._RegistrationStatus = None

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsDefaultMapping(self):
        return self._IsDefaultMapping

    @IsDefaultMapping.setter
    def IsDefaultMapping(self, IsDefaultMapping):
        self._IsDefaultMapping = IsDefaultMapping

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def IsForcedHttps(self):
        return self._IsForcedHttps

    @IsForcedHttps.setter
    def IsForcedHttps(self, IsForcedHttps):
        self._IsForcedHttps = IsForcedHttps

    @property
    def RegistrationStatus(self):
        return self._RegistrationStatus

    @RegistrationStatus.setter
    def RegistrationStatus(self, RegistrationStatus):
        self._RegistrationStatus = RegistrationStatus


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._Status = params.get("Status")
        self._CertificateId = params.get("CertificateId")
        self._IsDefaultMapping = params.get("IsDefaultMapping")
        self._Protocol = params.get("Protocol")
        self._NetType = params.get("NetType")
        self._IsForcedHttps = params.get("IsForcedHttps")
        self._RegistrationStatus = params.get("RegistrationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainSets(AbstractModel):
    """自定义服务域名展示

    """

    def __init__(self):
        r"""
        :param _TotalCount: 服务下的自定义域名数量。
        :type TotalCount: int
        :param _DomainSet: 自定义服务域名列表。
        :type DomainSet: list of DomainSetList
        """
        self._TotalCount = None
        self._DomainSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DomainSet(self):
        return self._DomainSet

    @DomainSet.setter
    def DomainSet(self, DomainSet):
        self._DomainSet = DomainSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DomainSet") is not None:
            self._DomainSet = []
            for item in params.get("DomainSet"):
                obj = DomainSetList()
                obj._deserialize(item)
                self._DomainSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApiKeyRequest(AbstractModel):
    """EnableApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 待启用的密钥 ID。
        :type AccessKeyId: str
        """
        self._AccessKeyId = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApiKeyResponse(AbstractModel):
    """EnableApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 启动密钥操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """服务发布的环境信息。

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: 环境名称。
        :type EnvironmentName: str
        :param _Url: 访问路径。
        :type Url: str
        :param _Status: 发布状态，1 表示已发布，0 表示未发布。
        :type Status: int
        :param _VersionName: 运行版本。
        :type VersionName: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._EnvironmentName = None
        self._Url = None
        self._Status = None
        self._VersionName = None
        self._CreateTime = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._VersionName = params.get("VersionName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentStrategy(AbstractModel):
    """环境限流

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: 环境名
        :type EnvironmentName: str
        :param _Quota: 限流值
        :type Quota: int
        """
        self._EnvironmentName = None
        self._Quota = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Quota(self):
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._Quota = params.get("Quota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorCodes(AbstractModel):
    """用户自定义错误码

    """

    def __init__(self):
        r"""
        :param _Code: 自定义响应配置错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param _Msg: 自定义响应配置错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param _Desc: 自定义响应配置错误码备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param _ConvertedCode: 自定义错误码转换。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConvertedCode: int
        :param _NeedConvert: 是否需要开启错误码转换。
注意：此字段可能返回 null，表示取不到有效值。
        :type NeedConvert: bool
        """
        self._Code = None
        self._Msg = None
        self._Desc = None
        self._ConvertedCode = None
        self._NeedConvert = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ConvertedCode(self):
        return self._ConvertedCode

    @ConvertedCode.setter
    def ConvertedCode(self, ConvertedCode):
        self._ConvertedCode = ConvertedCode

    @property
    def NeedConvert(self):
        return self._NeedConvert

    @NeedConvert.setter
    def NeedConvert(self, NeedConvert):
        self._NeedConvert = NeedConvert


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Desc = params.get("Desc")
        self._ConvertedCode = params.get("ConvertedCode")
        self._NeedConvert = params.get("NeedConvert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckConf(AbstractModel):
    """健康检查配置，包括TsfHealthCheckConf和TargetServicesHealthCheckConf

    """

    def __init__(self):
        r"""
        :param _IsHealthCheck: 是否开启健康检查。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsHealthCheck: bool
        :param _RequestVolumeThreshold: 健康检查阈值。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestVolumeThreshold: int
        :param _SleepWindowInMilliseconds: 窗口大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type SleepWindowInMilliseconds: int
        :param _ErrorThresholdPercentage: 阈值百分比。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorThresholdPercentage: int
        """
        self._IsHealthCheck = None
        self._RequestVolumeThreshold = None
        self._SleepWindowInMilliseconds = None
        self._ErrorThresholdPercentage = None

    @property
    def IsHealthCheck(self):
        return self._IsHealthCheck

    @IsHealthCheck.setter
    def IsHealthCheck(self, IsHealthCheck):
        self._IsHealthCheck = IsHealthCheck

    @property
    def RequestVolumeThreshold(self):
        return self._RequestVolumeThreshold

    @RequestVolumeThreshold.setter
    def RequestVolumeThreshold(self, RequestVolumeThreshold):
        self._RequestVolumeThreshold = RequestVolumeThreshold

    @property
    def SleepWindowInMilliseconds(self):
        return self._SleepWindowInMilliseconds

    @SleepWindowInMilliseconds.setter
    def SleepWindowInMilliseconds(self, SleepWindowInMilliseconds):
        self._SleepWindowInMilliseconds = SleepWindowInMilliseconds

    @property
    def ErrorThresholdPercentage(self):
        return self._ErrorThresholdPercentage

    @ErrorThresholdPercentage.setter
    def ErrorThresholdPercentage(self, ErrorThresholdPercentage):
        self._ErrorThresholdPercentage = ErrorThresholdPercentage


    def _deserialize(self, params):
        self._IsHealthCheck = params.get("IsHealthCheck")
        self._RequestVolumeThreshold = params.get("RequestVolumeThreshold")
        self._SleepWindowInMilliseconds = params.get("SleepWindowInMilliseconds")
        self._ErrorThresholdPercentage = params.get("ErrorThresholdPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategiesStatus(AbstractModel):
    """策略列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 策略数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _StrategySet: 策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategySet: list of IPStrategy
        """
        self._TotalCount = None
        self._StrategySet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StrategySet(self):
        return self._StrategySet

    @StrategySet.setter
    def StrategySet(self, StrategySet):
        self._StrategySet = StrategySet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("StrategySet") is not None:
            self._StrategySet = []
            for item in params.get("StrategySet"):
                obj = IPStrategy()
                obj._deserialize(item)
                self._StrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategy(AbstractModel):
    """ip策略

    """

    def __init__(self):
        r"""
        :param _StrategyId: 策略唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: str
        :param _StrategyName: 用户自定义策略名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyName: str
        :param _StrategyType: 策略类型。支持WHITE（白名单）和BLACK（黑名单）。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyType: str
        :param _StrategyData: IP列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyData: str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _ServiceId: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _BindApiTotalCount: 策略绑定的API数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindApiTotalCount: int
        :param _BindApis: 绑定的API详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindApis: list of DesApisStatus
        """
        self._StrategyId = None
        self._StrategyName = None
        self._StrategyType = None
        self._StrategyData = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ServiceId = None
        self._BindApiTotalCount = None
        self._BindApis = None

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def StrategyType(self):
        return self._StrategyType

    @StrategyType.setter
    def StrategyType(self, StrategyType):
        self._StrategyType = StrategyType

    @property
    def StrategyData(self):
        return self._StrategyData

    @StrategyData.setter
    def StrategyData(self, StrategyData):
        self._StrategyData = StrategyData

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def BindApiTotalCount(self):
        return self._BindApiTotalCount

    @BindApiTotalCount.setter
    def BindApiTotalCount(self, BindApiTotalCount):
        self._BindApiTotalCount = BindApiTotalCount

    @property
    def BindApis(self):
        return self._BindApis

    @BindApis.setter
    def BindApis(self, BindApis):
        self._BindApis = BindApis


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._StrategyType = params.get("StrategyType")
        self._StrategyData = params.get("StrategyData")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ServiceId = params.get("ServiceId")
        self._BindApiTotalCount = params.get("BindApiTotalCount")
        if params.get("BindApis") is not None:
            self._BindApis = []
            for item in params.get("BindApis"):
                obj = DesApisStatus()
                obj._deserialize(item)
                self._BindApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategyApi(AbstractModel):
    """策略绑定api列表

    """

    def __init__(self):
        r"""
        :param _ApiId: API 唯一 ID。
        :type ApiId: str
        :param _ApiName: 用户自定义的 API 名称。
        :type ApiName: str
        :param _ApiType: API 类型。取值为NORMAL（普通API）和TSF （微服务API）。
        :type ApiType: str
        :param _Path: API 的路径。如 /path。
        :type Path: str
        :param _Method: API 的请求方法。如 GET。
        :type Method: str
        :param _OtherIPStrategyId: API 已经绑定的其他策略唯一ID。
        :type OtherIPStrategyId: str
        :param _OtherEnvironmentName: API 已经绑定的环境。
        :type OtherEnvironmentName: str
        """
        self._ApiId = None
        self._ApiName = None
        self._ApiType = None
        self._Path = None
        self._Method = None
        self._OtherIPStrategyId = None
        self._OtherEnvironmentName = None

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def OtherIPStrategyId(self):
        return self._OtherIPStrategyId

    @OtherIPStrategyId.setter
    def OtherIPStrategyId(self, OtherIPStrategyId):
        self._OtherIPStrategyId = OtherIPStrategyId

    @property
    def OtherEnvironmentName(self):
        return self._OtherEnvironmentName

    @OtherEnvironmentName.setter
    def OtherEnvironmentName(self, OtherEnvironmentName):
        self._OtherEnvironmentName = OtherEnvironmentName


    def _deserialize(self, params):
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ApiType = params.get("ApiType")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._OtherIPStrategyId = params.get("OtherIPStrategyId")
        self._OtherEnvironmentName = params.get("OtherEnvironmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategyApiStatus(AbstractModel):
    """ip策略绑定api详情

    """

    def __init__(self):
        r"""
        :param _TotalCount: 环境绑定API数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ApiIdStatusSet: 环境绑定API详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiIdStatusSet: list of IPStrategyApi
        """
        self._TotalCount = None
        self._ApiIdStatusSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ApiIdStatusSet(self):
        return self._ApiIdStatusSet

    @ApiIdStatusSet.setter
    def ApiIdStatusSet(self, ApiIdStatusSet):
        self._ApiIdStatusSet = ApiIdStatusSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self._ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = IPStrategyApi()
                obj._deserialize(item)
                self._ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportOpenApiRequest(AbstractModel):
    """ImportOpenApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: API所在的服务唯一ID。
        :type ServiceId: str
        :param _Content: openAPI正文内容。
        :type Content: str
        :param _EncodeType: Content格式，只能是YAML或者JSON，默认是YAML。
        :type EncodeType: str
        :param _ContentVersion: Content版本，默认是openAPI，目前只支持openAPI。
        :type ContentVersion: str
        """
        self._ServiceId = None
        self._Content = None
        self._EncodeType = None
        self._ContentVersion = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def EncodeType(self):
        return self._EncodeType

    @EncodeType.setter
    def EncodeType(self, EncodeType):
        self._EncodeType = EncodeType

    @property
    def ContentVersion(self):
        return self._ContentVersion

    @ContentVersion.setter
    def ContentVersion(self, ContentVersion):
        self._ContentVersion = ContentVersion


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Content = params.get("Content")
        self._EncodeType = params.get("EncodeType")
        self._ContentVersion = params.get("ContentVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportOpenApiResponse(AbstractModel):
    """ImportOpenApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 导入OpenApi返回参数。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRspSet`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = CreateApiRspSet()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """独享实例预付费详情

    """

    def __init__(self):
        r"""
        :param _RenewFlag: 自动续费标示
        :type RenewFlag: str
        :param _ExpiredTime: 预付费到期时间
        :type ExpiredTime: str
        """
        self._RenewFlag = None
        self._ExpiredTime = None

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def ExpiredTime(self):
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime


    def _deserialize(self, params):
        self._RenewFlag = params.get("RenewFlag")
        self._ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """独享实例详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享实例唯一id
        :type InstanceId: str
        :param _Zone: 可用区
        :type Zone: str
        :param _InstanceName: 独享实例名字
        :type InstanceName: str
        :param _InstanceDescription: 独享实例描述
        :type InstanceDescription: str
        :param _InstanceChargeType: 独享实例计费类型
        :type InstanceChargeType: str
        :param _InstanceState: 独享实例状态
        :type InstanceState: str
        :param _InstanceChargePrepaid: 独享实例预付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.apigateway.v20180808.models.InstanceChargePrepaid`
        :param _InstanceType: 独享实例类型
        :type InstanceType: str
        :param _NetworkConfig: 独享实例网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConfig: :class:`tencentcloud.apigateway.v20180808.models.NetworkConfig`
        :param _VpcConfig: 独享实例vpc配置
        :type VpcConfig: :class:`tencentcloud.apigateway.v20180808.models.VpcConfig`
        :param _Parameters: 独享实例参数配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Parameters: list of ParameterInfo
        :param _IsolationStartedTime: 独享实例隔离时间
        :type IsolationStartedTime: str
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _Zones: 可用区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: list of str
        """
        self._InstanceId = None
        self._Zone = None
        self._InstanceName = None
        self._InstanceDescription = None
        self._InstanceChargeType = None
        self._InstanceState = None
        self._InstanceChargePrepaid = None
        self._InstanceType = None
        self._NetworkConfig = None
        self._VpcConfig = None
        self._Parameters = None
        self._IsolationStartedTime = None
        self._CreatedTime = None
        self._Zones = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Zone(self):
        return self._Zone

    @Zone.setter
    def Zone(self, Zone):
        self._Zone = Zone

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceDescription(self):
        return self._InstanceDescription

    @InstanceDescription.setter
    def InstanceDescription(self, InstanceDescription):
        self._InstanceDescription = InstanceDescription

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def NetworkConfig(self):
        return self._NetworkConfig

    @NetworkConfig.setter
    def NetworkConfig(self, NetworkConfig):
        self._NetworkConfig = NetworkConfig

    @property
    def VpcConfig(self):
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def IsolationStartedTime(self):
        return self._IsolationStartedTime

    @IsolationStartedTime.setter
    def IsolationStartedTime(self, IsolationStartedTime):
        self._IsolationStartedTime = IsolationStartedTime

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Zones(self):
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Zone = params.get("Zone")
        self._InstanceName = params.get("InstanceName")
        self._InstanceDescription = params.get("InstanceDescription")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceState = params.get("InstanceState")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._InstanceType = params.get("InstanceType")
        if params.get("NetworkConfig") is not None:
            self._NetworkConfig = NetworkConfig()
            self._NetworkConfig._deserialize(params.get("NetworkConfig"))
        if params.get("VpcConfig") is not None:
            self._VpcConfig = VpcConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = ParameterInfo()
                obj._deserialize(item)
                self._Parameters.append(obj)
        self._IsolationStartedTime = params.get("IsolationStartedTime")
        self._CreatedTime = params.get("CreatedTime")
        self._Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """独享实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享实例唯一id
        :type InstanceId: str
        :param _InstanceName: 独享实例name
        :type InstanceName: str
        :param _InstanceDescription: 独享实例描述
        :type InstanceDescription: str
        :param _InstanceChargeType: 独享实例计费类型
        :type InstanceChargeType: str
        :param _InstanceType: 独享实例类型
        :type InstanceType: str
        :param _InstanceState: 独享实例状态
        :type InstanceState: str
        :param _CreatedTime: 独享实例创建时间
        :type CreatedTime: str
        :param _DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param _ResourceId: 资源ID同唯一id
        :type ResourceId: str
        :param _OuterIpList: 公网IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type OuterIpList: list of str
        :param _InnerIpList: 内网IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerIpList: list of str
        :param _InstanceChargePrepaid: 专享实例计费信息
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.apigateway.v20180808.models.InstanceChargePrepaid`
        :param _UniqVpcId: 所属vpc
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceDescription = None
        self._InstanceChargeType = None
        self._InstanceType = None
        self._InstanceState = None
        self._CreatedTime = None
        self._DealName = None
        self._ResourceId = None
        self._OuterIpList = None
        self._InnerIpList = None
        self._InstanceChargePrepaid = None
        self._UniqVpcId = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceDescription(self):
        return self._InstanceDescription

    @InstanceDescription.setter
    def InstanceDescription(self, InstanceDescription):
        self._InstanceDescription = InstanceDescription

    @property
    def InstanceChargeType(self):
        return self._InstanceChargeType

    @InstanceChargeType.setter
    def InstanceChargeType(self, InstanceChargeType):
        self._InstanceChargeType = InstanceChargeType

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceState(self):
        return self._InstanceState

    @InstanceState.setter
    def InstanceState(self, InstanceState):
        self._InstanceState = InstanceState

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def DealName(self):
        return self._DealName

    @DealName.setter
    def DealName(self, DealName):
        self._DealName = DealName

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def OuterIpList(self):
        return self._OuterIpList

    @OuterIpList.setter
    def OuterIpList(self, OuterIpList):
        self._OuterIpList = OuterIpList

    @property
    def InnerIpList(self):
        return self._InnerIpList

    @InnerIpList.setter
    def InnerIpList(self, InnerIpList):
        self._InnerIpList = InnerIpList

    @property
    def InstanceChargePrepaid(self):
        return self._InstanceChargePrepaid

    @InstanceChargePrepaid.setter
    def InstanceChargePrepaid(self, InstanceChargePrepaid):
        self._InstanceChargePrepaid = InstanceChargePrepaid

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceDescription = params.get("InstanceDescription")
        self._InstanceChargeType = params.get("InstanceChargeType")
        self._InstanceType = params.get("InstanceType")
        self._InstanceState = params.get("InstanceState")
        self._CreatedTime = params.get("CreatedTime")
        self._DealName = params.get("DealName")
        self._ResourceId = params.get("ResourceId")
        self._OuterIpList = params.get("OuterIpList")
        self._InnerIpList = params.get("InnerIpList")
        if params.get("InstanceChargePrepaid") is not None:
            self._InstanceChargePrepaid = InstanceChargePrepaid()
            self._InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self._UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParameterInput(AbstractModel):
    """独享实例参数信息

    """

    def __init__(self):
        r"""
        :param _Name: ServiceRequestNumPreSec，ApiRequestNumPreSec
        :type Name: str
        :param _Value: 参数值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSummary(AbstractModel):
    """专享查询列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 专享实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _InstanceSet: 专享实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSet: list of InstanceInfo
        """
        self._TotalCount = None
        self._InstanceSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceSet(self):
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sLabel(AbstractModel):
    """k8s Label

    """

    def __init__(self):
        r"""
        :param _Key: Label的Key
        :type Key: str
        :param _Value: Label的Value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sService(AbstractModel):
    """k8s 服务的配置

    """

    def __init__(self):
        r"""
        :param _Weight: 权重
        :type Weight: int
        :param _ClusterId: k8s集群ID
        :type ClusterId: str
        :param _Namespace: 容器命名空间
        :type Namespace: str
        :param _ServiceName: 容器服务的名字
        :type ServiceName: str
        :param _Port: 服务的端口
        :type Port: int
        :param _ExtraLabels: 额外选择的Pod的Label
        :type ExtraLabels: list of K8sLabel
        :param _Name: 自定义的服务名字，可选
        :type Name: str
        """
        self._Weight = None
        self._ClusterId = None
        self._Namespace = None
        self._ServiceName = None
        self._Port = None
        self._ExtraLabels = None
        self._Name = None

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ExtraLabels(self):
        return self._ExtraLabels

    @ExtraLabels.setter
    def ExtraLabels(self, ExtraLabels):
        self._ExtraLabels = ExtraLabels

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Weight = params.get("Weight")
        self._ClusterId = params.get("ClusterId")
        self._Namespace = params.get("Namespace")
        self._ServiceName = params.get("ServiceName")
        self._Port = params.get("Port")
        if params.get("ExtraLabels") is not None:
            self._ExtraLabels = []
            for item in params.get("ExtraLabels"):
                obj = K8sLabel()
                obj._deserialize(item)
                self._ExtraLabels.append(obj)
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogQuery(AbstractModel):
    """检索条件入参

    """

    def __init__(self):
        r"""
        :param _Name: 检索字段
        :type Name: str
        :param _Operator: 操作符
        :type Operator: str
        :param _Value: 检索值
        :type Value: str
        """
        self._Name = None
        self._Operator = None
        self._Value = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MicroService(AbstractModel):
    """API绑定的微服务信息。

    """

    def __init__(self):
        r"""
        :param _ClusterId: 微服务集群ID。
        :type ClusterId: str
        :param _NamespaceId: 微服务命名空间ID。
        :type NamespaceId: str
        :param _MicroServiceName: 微服务名称。
        :type MicroServiceName: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._MicroServiceName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def MicroServiceName(self):
        return self._MicroServiceName

    @MicroServiceName.setter
    def MicroServiceName(self, MicroServiceName):
        self._MicroServiceName = MicroServiceName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._MicroServiceName = params.get("MicroServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MicroServiceReq(AbstractModel):
    """tsf类型入参

    """

    def __init__(self):
        r"""
        :param _ClusterId: 微服务集群。
        :type ClusterId: str
        :param _NamespaceId: 微服务命名空间。
        :type NamespaceId: str
        :param _MicroServiceName: 微服务名称。
        :type MicroServiceName: str
        """
        self._ClusterId = None
        self._NamespaceId = None
        self._MicroServiceName = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def NamespaceId(self):
        return self._NamespaceId

    @NamespaceId.setter
    def NamespaceId(self, NamespaceId):
        self._NamespaceId = NamespaceId

    @property
    def MicroServiceName(self):
        return self._MicroServiceName

    @MicroServiceName.setter
    def MicroServiceName(self, MicroServiceName):
        self._MicroServiceName = MicroServiceName


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._NamespaceId = params.get("NamespaceId")
        self._MicroServiceName = params.get("MicroServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAPIDocRequest(AbstractModel):
    """ModifyAPIDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiDocName: API文档名称
        :type ApiDocName: str
        :param _ServiceId: 服务名称
        :type ServiceId: str
        :param _Environment: 环境名称
        :type Environment: str
        :param _ApiIds: 生成文档的API列表
        :type ApiIds: list of str
        :param _ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self._ApiDocName = None
        self._ServiceId = None
        self._Environment = None
        self._ApiIds = None
        self._ApiDocId = None

    @property
    def ApiDocName(self):
        return self._ApiDocName

    @ApiDocName.setter
    def ApiDocName(self, ApiDocName):
        self._ApiDocName = ApiDocName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocName = params.get("ApiDocName")
        self._ServiceId = params.get("ServiceId")
        self._Environment = params.get("Environment")
        self._ApiIds = params.get("ApiIds")
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAPIDocResponse(AbstractModel):
    """ModifyAPIDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API文档基本信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDoc()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyApiAppRequest(AbstractModel):
    """ModifyApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiAppId: 应用唯一 ID。
        :type ApiAppId: str
        :param _ApiAppName: 修改的应用名称
        :type ApiAppName: str
        :param _ApiAppDesc: 修改的应用描述
        :type ApiAppDesc: str
        """
        self._ApiAppId = None
        self._ApiAppName = None
        self._ApiAppDesc = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def ApiAppName(self):
        return self._ApiAppName

    @ApiAppName.setter
    def ApiAppName(self, ApiAppName):
        self._ApiAppName = ApiAppName

    @property
    def ApiAppDesc(self):
        return self._ApiAppDesc

    @ApiAppDesc.setter
    def ApiAppDesc(self, ApiAppDesc):
        self._ApiAppDesc = ApiAppDesc


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._ApiAppName = params.get("ApiAppName")
        self._ApiAppDesc = params.get("ApiAppDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiAppResponse(AbstractModel):
    """ModifyApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApiEnvironmentStrategyRequest(AbstractModel):
    """ModifyApiEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param _Strategy: 限流值。
        :type Strategy: int
        :param _EnvironmentName: 环境名。
        :type EnvironmentName: str
        :param _ApiIds: API列表。
        :type ApiIds: list of str
        """
        self._ServiceId = None
        self._Strategy = None
        self._EnvironmentName = None
        self._ApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Strategy = params.get("Strategy")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiEnvironmentStrategyResponse(AbstractModel):
    """ModifyApiEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyApiIncrementRequest(AbstractModel):
    """ModifyApiIncrement请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务ID
        :type ServiceId: str
        :param _ApiId: 接口ID
        :type ApiId: str
        :param _BusinessType: 需要修改的API auth类型(可选择OAUTH-授权API)
        :type BusinessType: str
        :param _PublicKey: oauth接口需要修改的公钥值
        :type PublicKey: str
        :param _LoginRedirectUrl: oauth接口重定向地址
        :type LoginRedirectUrl: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._BusinessType = None
        self._PublicKey = None
        self._LoginRedirectUrl = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def BusinessType(self):
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def LoginRedirectUrl(self):
        return self._LoginRedirectUrl

    @LoginRedirectUrl.setter
    def LoginRedirectUrl(self, LoginRedirectUrl):
        self._LoginRedirectUrl = LoginRedirectUrl


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._BusinessType = params.get("BusinessType")
        self._PublicKey = params.get("PublicKey")
        self._LoginRedirectUrl = params.get("LoginRedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiIncrementResponse(AbstractModel):
    """ModifyApiIncrement返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyApiRequest(AbstractModel):
    """ModifyApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param _ServiceType: API 的后端服务类型。支持HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。
        :type ServiceType: str
        :param _RequestConfig: 请求的前端配置。
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param _ApiId: API 接口唯一 ID。
        :type ApiId: str
        :param _ApiName: 用户自定义的 API 名称。
        :type ApiName: str
        :param _ApiDesc: 用户自定义的 API 接口描述。
        :type ApiDesc: str
        :param _ApiType: API 类型，支持NORMAL和TSF，默认为NORMAL。
        :type ApiType: str
        :param _AuthType: API 鉴权类型。支持SECRET、NONE、OAUTH、APP。默认为NONE。
        :type AuthType: str
        :param _AuthRequired: 是否需要签名认证，True 表示需要，False 表示不需要。待废弃。
        :type AuthRequired: bool
        :param _ServiceTimeout: API 的后端服务超时时间，单位是秒。
        :type ServiceTimeout: int
        :param _Protocol: API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。修改api时推荐必填
        :type Protocol: str
        :param _EnableCORS: 是否需要开启跨域，Ture 表示需要，False 表示不需要。
        :type EnableCORS: bool
        :param _ConstantParameters: 常量参数。
        :type ConstantParameters: list of ConstantParameter
        :param _RequestParameters: 前端请求参数。
        :type RequestParameters: list of ReqParameter
        :param _ApiBusinessType: 当AuthType 为 OAUTH时，该字段有效， NORMAL：业务api   OAUTH：授权API。
        :type ApiBusinessType: str
        :param _ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。
        :type ServiceMockReturnMessage: str
        :param _MicroServices: API绑定微服务列表。
        :type MicroServices: list of MicroServiceReq
        :param _ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param _ServiceTsfHealthCheckConf: 微服务的健康检查配置。
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _TargetServicesLoadBalanceConf: target类型负载均衡配置。（内测阶段）
        :type TargetServicesLoadBalanceConf: int
        :param _TargetServicesHealthCheckConf: target健康检查配置。（内测阶段）
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param _ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。
        :type ServiceScfFunctionName: str
        :param _ServiceWebsocketRegisterFunctionName: scf websocket注册函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionName: str
        :param _ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionName: str
        :param _ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionName: str
        :param _ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。
        :type ServiceScfFunctionNamespace: str
        :param _ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。
        :type ServiceScfFunctionQualifier: str
        :param _ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param _ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param _ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param _ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param _ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param _ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param _ServiceScfIsIntegratedResponse: 是否开启响应集成。当后端类型是SCF时生效。
        :type ServiceScfIsIntegratedResponse: bool
        :param _IsDebugAfterCharge: 开始调试后计费。（云市场预留字段）
        :type IsDebugAfterCharge: bool
        :param _TagSpecifications: 标签。
        :type TagSpecifications: :class:`tencentcloud.apigateway.v20180808.models.Tag`
        :param _IsDeleteResponseErrorCodes: 是否删除自定义响应配置错误码，如果不传或者传 False，不删除，当传 True 时，则删除此 API 所有自定义响应配置错误码。
        :type IsDeleteResponseErrorCodes: bool
        :param _ResponseType: 返回类型。
        :type ResponseType: str
        :param _ResponseSuccessExample: 自定义响应配置成功响应示例。
        :type ResponseSuccessExample: str
        :param _ResponseFailExample: 自定义响应配置失败响应示例。
        :type ResponseFailExample: str
        :param _ServiceConfig: API 的后端服务配置。
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param _AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
        :type AuthRelationApiId: str
        :param _ServiceParameters: API的后端服务参数。
        :type ServiceParameters: list of ServiceParameter
        :param _OauthConfig: oauth配置。当AuthType是OAUTH时生效。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param _ResponseErrorCodes: 用户自定义错误码配置。
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param _IsBase64Encoded: 是否开启Base64编码，只有后端为scf时才会生效。
        :type IsBase64Encoded: bool
        :param _IsBase64Trigger: 是否开启Base64编码的header触发，只有后端为scf时才会生效。
        :type IsBase64Trigger: bool
        :param _Base64EncodedTriggerRules: Header触发规则，总规则数不能超过10。
        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule
        :param _EventBusId: 事件总线ID。
        :type EventBusId: str
        :param _ServiceScfFunctionType: scf函数类型。当后端类型是SCF时生效。支持事件触发(EVENT)，http直通云函数(HTTP)。
        :type ServiceScfFunctionType: str
        :param _ServiceScfEventIsAsyncCall: 是否开启SCF Event异步调用。
        :type ServiceScfEventIsAsyncCall: bool
        :param _EIAMAppType: EIAM应用类型。
        :type EIAMAppType: str
        :param _EIAMAuthType: EIAM应用认证类型，支持仅认证（AuthenticationOnly）、认证和鉴权（Authorization）。
        :type EIAMAuthType: str
        :param _EIAMAppId: EIAM应用Token 有效时间，单位为秒，默认为7200秒。
        :type EIAMAppId: str
        :param _TokenTimeout: EIAM应用ID。
        :type TokenTimeout: int
        """
        self._ServiceId = None
        self._ServiceType = None
        self._RequestConfig = None
        self._ApiId = None
        self._ApiName = None
        self._ApiDesc = None
        self._ApiType = None
        self._AuthType = None
        self._AuthRequired = None
        self._ServiceTimeout = None
        self._Protocol = None
        self._EnableCORS = None
        self._ConstantParameters = None
        self._RequestParameters = None
        self._ApiBusinessType = None
        self._ServiceMockReturnMessage = None
        self._MicroServices = None
        self._ServiceTsfLoadBalanceConf = None
        self._ServiceTsfHealthCheckConf = None
        self._TargetServicesLoadBalanceConf = None
        self._TargetServicesHealthCheckConf = None
        self._ServiceScfFunctionName = None
        self._ServiceWebsocketRegisterFunctionName = None
        self._ServiceWebsocketCleanupFunctionName = None
        self._ServiceWebsocketTransportFunctionName = None
        self._ServiceScfFunctionNamespace = None
        self._ServiceScfFunctionQualifier = None
        self._ServiceWebsocketRegisterFunctionNamespace = None
        self._ServiceWebsocketRegisterFunctionQualifier = None
        self._ServiceWebsocketTransportFunctionNamespace = None
        self._ServiceWebsocketTransportFunctionQualifier = None
        self._ServiceWebsocketCleanupFunctionNamespace = None
        self._ServiceWebsocketCleanupFunctionQualifier = None
        self._ServiceScfIsIntegratedResponse = None
        self._IsDebugAfterCharge = None
        self._TagSpecifications = None
        self._IsDeleteResponseErrorCodes = None
        self._ResponseType = None
        self._ResponseSuccessExample = None
        self._ResponseFailExample = None
        self._ServiceConfig = None
        self._AuthRelationApiId = None
        self._ServiceParameters = None
        self._OauthConfig = None
        self._ResponseErrorCodes = None
        self._IsBase64Encoded = None
        self._IsBase64Trigger = None
        self._Base64EncodedTriggerRules = None
        self._EventBusId = None
        self._ServiceScfFunctionType = None
        self._ServiceScfEventIsAsyncCall = None
        self._EIAMAppType = None
        self._EIAMAuthType = None
        self._EIAMAppId = None
        self._TokenTimeout = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def RequestConfig(self):
        return self._RequestConfig

    @RequestConfig.setter
    def RequestConfig(self, RequestConfig):
        self._RequestConfig = RequestConfig

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def ApiDesc(self):
        return self._ApiDesc

    @ApiDesc.setter
    def ApiDesc(self, ApiDesc):
        self._ApiDesc = ApiDesc

    @property
    def ApiType(self):
        return self._ApiType

    @ApiType.setter
    def ApiType(self, ApiType):
        self._ApiType = ApiType

    @property
    def AuthType(self):
        return self._AuthType

    @AuthType.setter
    def AuthType(self, AuthType):
        self._AuthType = AuthType

    @property
    def AuthRequired(self):
        return self._AuthRequired

    @AuthRequired.setter
    def AuthRequired(self, AuthRequired):
        self._AuthRequired = AuthRequired

    @property
    def ServiceTimeout(self):
        return self._ServiceTimeout

    @ServiceTimeout.setter
    def ServiceTimeout(self, ServiceTimeout):
        self._ServiceTimeout = ServiceTimeout

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def EnableCORS(self):
        return self._EnableCORS

    @EnableCORS.setter
    def EnableCORS(self, EnableCORS):
        self._EnableCORS = EnableCORS

    @property
    def ConstantParameters(self):
        return self._ConstantParameters

    @ConstantParameters.setter
    def ConstantParameters(self, ConstantParameters):
        self._ConstantParameters = ConstantParameters

    @property
    def RequestParameters(self):
        return self._RequestParameters

    @RequestParameters.setter
    def RequestParameters(self, RequestParameters):
        self._RequestParameters = RequestParameters

    @property
    def ApiBusinessType(self):
        return self._ApiBusinessType

    @ApiBusinessType.setter
    def ApiBusinessType(self, ApiBusinessType):
        self._ApiBusinessType = ApiBusinessType

    @property
    def ServiceMockReturnMessage(self):
        return self._ServiceMockReturnMessage

    @ServiceMockReturnMessage.setter
    def ServiceMockReturnMessage(self, ServiceMockReturnMessage):
        self._ServiceMockReturnMessage = ServiceMockReturnMessage

    @property
    def MicroServices(self):
        return self._MicroServices

    @MicroServices.setter
    def MicroServices(self, MicroServices):
        self._MicroServices = MicroServices

    @property
    def ServiceTsfLoadBalanceConf(self):
        return self._ServiceTsfLoadBalanceConf

    @ServiceTsfLoadBalanceConf.setter
    def ServiceTsfLoadBalanceConf(self, ServiceTsfLoadBalanceConf):
        self._ServiceTsfLoadBalanceConf = ServiceTsfLoadBalanceConf

    @property
    def ServiceTsfHealthCheckConf(self):
        return self._ServiceTsfHealthCheckConf

    @ServiceTsfHealthCheckConf.setter
    def ServiceTsfHealthCheckConf(self, ServiceTsfHealthCheckConf):
        self._ServiceTsfHealthCheckConf = ServiceTsfHealthCheckConf

    @property
    def TargetServicesLoadBalanceConf(self):
        return self._TargetServicesLoadBalanceConf

    @TargetServicesLoadBalanceConf.setter
    def TargetServicesLoadBalanceConf(self, TargetServicesLoadBalanceConf):
        self._TargetServicesLoadBalanceConf = TargetServicesLoadBalanceConf

    @property
    def TargetServicesHealthCheckConf(self):
        return self._TargetServicesHealthCheckConf

    @TargetServicesHealthCheckConf.setter
    def TargetServicesHealthCheckConf(self, TargetServicesHealthCheckConf):
        self._TargetServicesHealthCheckConf = TargetServicesHealthCheckConf

    @property
    def ServiceScfFunctionName(self):
        return self._ServiceScfFunctionName

    @ServiceScfFunctionName.setter
    def ServiceScfFunctionName(self, ServiceScfFunctionName):
        self._ServiceScfFunctionName = ServiceScfFunctionName

    @property
    def ServiceWebsocketRegisterFunctionName(self):
        return self._ServiceWebsocketRegisterFunctionName

    @ServiceWebsocketRegisterFunctionName.setter
    def ServiceWebsocketRegisterFunctionName(self, ServiceWebsocketRegisterFunctionName):
        self._ServiceWebsocketRegisterFunctionName = ServiceWebsocketRegisterFunctionName

    @property
    def ServiceWebsocketCleanupFunctionName(self):
        return self._ServiceWebsocketCleanupFunctionName

    @ServiceWebsocketCleanupFunctionName.setter
    def ServiceWebsocketCleanupFunctionName(self, ServiceWebsocketCleanupFunctionName):
        self._ServiceWebsocketCleanupFunctionName = ServiceWebsocketCleanupFunctionName

    @property
    def ServiceWebsocketTransportFunctionName(self):
        return self._ServiceWebsocketTransportFunctionName

    @ServiceWebsocketTransportFunctionName.setter
    def ServiceWebsocketTransportFunctionName(self, ServiceWebsocketTransportFunctionName):
        self._ServiceWebsocketTransportFunctionName = ServiceWebsocketTransportFunctionName

    @property
    def ServiceScfFunctionNamespace(self):
        return self._ServiceScfFunctionNamespace

    @ServiceScfFunctionNamespace.setter
    def ServiceScfFunctionNamespace(self, ServiceScfFunctionNamespace):
        self._ServiceScfFunctionNamespace = ServiceScfFunctionNamespace

    @property
    def ServiceScfFunctionQualifier(self):
        return self._ServiceScfFunctionQualifier

    @ServiceScfFunctionQualifier.setter
    def ServiceScfFunctionQualifier(self, ServiceScfFunctionQualifier):
        self._ServiceScfFunctionQualifier = ServiceScfFunctionQualifier

    @property
    def ServiceWebsocketRegisterFunctionNamespace(self):
        return self._ServiceWebsocketRegisterFunctionNamespace

    @ServiceWebsocketRegisterFunctionNamespace.setter
    def ServiceWebsocketRegisterFunctionNamespace(self, ServiceWebsocketRegisterFunctionNamespace):
        self._ServiceWebsocketRegisterFunctionNamespace = ServiceWebsocketRegisterFunctionNamespace

    @property
    def ServiceWebsocketRegisterFunctionQualifier(self):
        return self._ServiceWebsocketRegisterFunctionQualifier

    @ServiceWebsocketRegisterFunctionQualifier.setter
    def ServiceWebsocketRegisterFunctionQualifier(self, ServiceWebsocketRegisterFunctionQualifier):
        self._ServiceWebsocketRegisterFunctionQualifier = ServiceWebsocketRegisterFunctionQualifier

    @property
    def ServiceWebsocketTransportFunctionNamespace(self):
        return self._ServiceWebsocketTransportFunctionNamespace

    @ServiceWebsocketTransportFunctionNamespace.setter
    def ServiceWebsocketTransportFunctionNamespace(self, ServiceWebsocketTransportFunctionNamespace):
        self._ServiceWebsocketTransportFunctionNamespace = ServiceWebsocketTransportFunctionNamespace

    @property
    def ServiceWebsocketTransportFunctionQualifier(self):
        return self._ServiceWebsocketTransportFunctionQualifier

    @ServiceWebsocketTransportFunctionQualifier.setter
    def ServiceWebsocketTransportFunctionQualifier(self, ServiceWebsocketTransportFunctionQualifier):
        self._ServiceWebsocketTransportFunctionQualifier = ServiceWebsocketTransportFunctionQualifier

    @property
    def ServiceWebsocketCleanupFunctionNamespace(self):
        return self._ServiceWebsocketCleanupFunctionNamespace

    @ServiceWebsocketCleanupFunctionNamespace.setter
    def ServiceWebsocketCleanupFunctionNamespace(self, ServiceWebsocketCleanupFunctionNamespace):
        self._ServiceWebsocketCleanupFunctionNamespace = ServiceWebsocketCleanupFunctionNamespace

    @property
    def ServiceWebsocketCleanupFunctionQualifier(self):
        return self._ServiceWebsocketCleanupFunctionQualifier

    @ServiceWebsocketCleanupFunctionQualifier.setter
    def ServiceWebsocketCleanupFunctionQualifier(self, ServiceWebsocketCleanupFunctionQualifier):
        self._ServiceWebsocketCleanupFunctionQualifier = ServiceWebsocketCleanupFunctionQualifier

    @property
    def ServiceScfIsIntegratedResponse(self):
        return self._ServiceScfIsIntegratedResponse

    @ServiceScfIsIntegratedResponse.setter
    def ServiceScfIsIntegratedResponse(self, ServiceScfIsIntegratedResponse):
        self._ServiceScfIsIntegratedResponse = ServiceScfIsIntegratedResponse

    @property
    def IsDebugAfterCharge(self):
        return self._IsDebugAfterCharge

    @IsDebugAfterCharge.setter
    def IsDebugAfterCharge(self, IsDebugAfterCharge):
        self._IsDebugAfterCharge = IsDebugAfterCharge

    @property
    def TagSpecifications(self):
        return self._TagSpecifications

    @TagSpecifications.setter
    def TagSpecifications(self, TagSpecifications):
        self._TagSpecifications = TagSpecifications

    @property
    def IsDeleteResponseErrorCodes(self):
        return self._IsDeleteResponseErrorCodes

    @IsDeleteResponseErrorCodes.setter
    def IsDeleteResponseErrorCodes(self, IsDeleteResponseErrorCodes):
        self._IsDeleteResponseErrorCodes = IsDeleteResponseErrorCodes

    @property
    def ResponseType(self):
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def ResponseSuccessExample(self):
        return self._ResponseSuccessExample

    @ResponseSuccessExample.setter
    def ResponseSuccessExample(self, ResponseSuccessExample):
        self._ResponseSuccessExample = ResponseSuccessExample

    @property
    def ResponseFailExample(self):
        return self._ResponseFailExample

    @ResponseFailExample.setter
    def ResponseFailExample(self, ResponseFailExample):
        self._ResponseFailExample = ResponseFailExample

    @property
    def ServiceConfig(self):
        return self._ServiceConfig

    @ServiceConfig.setter
    def ServiceConfig(self, ServiceConfig):
        self._ServiceConfig = ServiceConfig

    @property
    def AuthRelationApiId(self):
        return self._AuthRelationApiId

    @AuthRelationApiId.setter
    def AuthRelationApiId(self, AuthRelationApiId):
        self._AuthRelationApiId = AuthRelationApiId

    @property
    def ServiceParameters(self):
        return self._ServiceParameters

    @ServiceParameters.setter
    def ServiceParameters(self, ServiceParameters):
        self._ServiceParameters = ServiceParameters

    @property
    def OauthConfig(self):
        return self._OauthConfig

    @OauthConfig.setter
    def OauthConfig(self, OauthConfig):
        self._OauthConfig = OauthConfig

    @property
    def ResponseErrorCodes(self):
        return self._ResponseErrorCodes

    @ResponseErrorCodes.setter
    def ResponseErrorCodes(self, ResponseErrorCodes):
        self._ResponseErrorCodes = ResponseErrorCodes

    @property
    def IsBase64Encoded(self):
        return self._IsBase64Encoded

    @IsBase64Encoded.setter
    def IsBase64Encoded(self, IsBase64Encoded):
        self._IsBase64Encoded = IsBase64Encoded

    @property
    def IsBase64Trigger(self):
        return self._IsBase64Trigger

    @IsBase64Trigger.setter
    def IsBase64Trigger(self, IsBase64Trigger):
        self._IsBase64Trigger = IsBase64Trigger

    @property
    def Base64EncodedTriggerRules(self):
        return self._Base64EncodedTriggerRules

    @Base64EncodedTriggerRules.setter
    def Base64EncodedTriggerRules(self, Base64EncodedTriggerRules):
        self._Base64EncodedTriggerRules = Base64EncodedTriggerRules

    @property
    def EventBusId(self):
        return self._EventBusId

    @EventBusId.setter
    def EventBusId(self, EventBusId):
        self._EventBusId = EventBusId

    @property
    def ServiceScfFunctionType(self):
        return self._ServiceScfFunctionType

    @ServiceScfFunctionType.setter
    def ServiceScfFunctionType(self, ServiceScfFunctionType):
        self._ServiceScfFunctionType = ServiceScfFunctionType

    @property
    def ServiceScfEventIsAsyncCall(self):
        return self._ServiceScfEventIsAsyncCall

    @ServiceScfEventIsAsyncCall.setter
    def ServiceScfEventIsAsyncCall(self, ServiceScfEventIsAsyncCall):
        self._ServiceScfEventIsAsyncCall = ServiceScfEventIsAsyncCall

    @property
    def EIAMAppType(self):
        return self._EIAMAppType

    @EIAMAppType.setter
    def EIAMAppType(self, EIAMAppType):
        self._EIAMAppType = EIAMAppType

    @property
    def EIAMAuthType(self):
        return self._EIAMAuthType

    @EIAMAuthType.setter
    def EIAMAuthType(self, EIAMAuthType):
        self._EIAMAuthType = EIAMAuthType

    @property
    def EIAMAppId(self):
        return self._EIAMAppId

    @EIAMAppId.setter
    def EIAMAppId(self, EIAMAppId):
        self._EIAMAppId = EIAMAppId

    @property
    def TokenTimeout(self):
        return self._TokenTimeout

    @TokenTimeout.setter
    def TokenTimeout(self, TokenTimeout):
        self._TokenTimeout = TokenTimeout


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceType = params.get("ServiceType")
        if params.get("RequestConfig") is not None:
            self._RequestConfig = RequestConfig()
            self._RequestConfig._deserialize(params.get("RequestConfig"))
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._ApiDesc = params.get("ApiDesc")
        self._ApiType = params.get("ApiType")
        self._AuthType = params.get("AuthType")
        self._AuthRequired = params.get("AuthRequired")
        self._ServiceTimeout = params.get("ServiceTimeout")
        self._Protocol = params.get("Protocol")
        self._EnableCORS = params.get("EnableCORS")
        if params.get("ConstantParameters") is not None:
            self._ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self._ConstantParameters.append(obj)
        if params.get("RequestParameters") is not None:
            self._RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = ReqParameter()
                obj._deserialize(item)
                self._RequestParameters.append(obj)
        self._ApiBusinessType = params.get("ApiBusinessType")
        self._ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        if params.get("MicroServices") is not None:
            self._MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroServiceReq()
                obj._deserialize(item)
                self._MicroServices.append(obj)
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self._ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self._ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self._ServiceTsfHealthCheckConf = HealthCheckConf()
            self._ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        self._TargetServicesLoadBalanceConf = params.get("TargetServicesLoadBalanceConf")
        if params.get("TargetServicesHealthCheckConf") is not None:
            self._TargetServicesHealthCheckConf = HealthCheckConf()
            self._TargetServicesHealthCheckConf._deserialize(params.get("TargetServicesHealthCheckConf"))
        self._ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self._ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self._ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self._ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self._ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self._ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self._ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self._ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self._ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self._ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        self._ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self._ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self._ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self._IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        if params.get("TagSpecifications") is not None:
            self._TagSpecifications = Tag()
            self._TagSpecifications._deserialize(params.get("TagSpecifications"))
        self._IsDeleteResponseErrorCodes = params.get("IsDeleteResponseErrorCodes")
        self._ResponseType = params.get("ResponseType")
        self._ResponseSuccessExample = params.get("ResponseSuccessExample")
        self._ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ServiceConfig") is not None:
            self._ServiceConfig = ServiceConfig()
            self._ServiceConfig._deserialize(params.get("ServiceConfig"))
        self._AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("ServiceParameters") is not None:
            self._ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self._ServiceParameters.append(obj)
        if params.get("OauthConfig") is not None:
            self._OauthConfig = OauthConfig()
            self._OauthConfig._deserialize(params.get("OauthConfig"))
        if params.get("ResponseErrorCodes") is not None:
            self._ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ResponseErrorCodeReq()
                obj._deserialize(item)
                self._ResponseErrorCodes.append(obj)
        self._IsBase64Encoded = params.get("IsBase64Encoded")
        self._IsBase64Trigger = params.get("IsBase64Trigger")
        if params.get("Base64EncodedTriggerRules") is not None:
            self._Base64EncodedTriggerRules = []
            for item in params.get("Base64EncodedTriggerRules"):
                obj = Base64EncodedTriggerRule()
                obj._deserialize(item)
                self._Base64EncodedTriggerRules.append(obj)
        self._EventBusId = params.get("EventBusId")
        self._ServiceScfFunctionType = params.get("ServiceScfFunctionType")
        self._ServiceScfEventIsAsyncCall = params.get("ServiceScfEventIsAsyncCall")
        self._EIAMAppType = params.get("EIAMAppType")
        self._EIAMAuthType = params.get("EIAMAuthType")
        self._EIAMAppId = params.get("EIAMAppId")
        self._TokenTimeout = params.get("TokenTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiResponse(AbstractModel):
    """ModifyApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifyExclusiveInstanceRequest(AbstractModel):
    """ModifyExclusiveInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 独享实例唯一id
        :type InstanceId: str
        :param _InstanceName: 独享实例name
        :type InstanceName: str
        :param _InstanceDescription: 独享实例描述
        :type InstanceDescription: str
        :param _Parameters: 独享实例参数配置
        :type Parameters: list of InstanceParameterInput
        """
        self._InstanceId = None
        self._InstanceName = None
        self._InstanceDescription = None
        self._Parameters = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def InstanceDescription(self):
        return self._InstanceDescription

    @InstanceDescription.setter
    def InstanceDescription(self, InstanceDescription):
        self._InstanceDescription = InstanceDescription

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._InstanceDescription = params.get("InstanceDescription")
        if params.get("Parameters") is not None:
            self._Parameters = []
            for item in params.get("Parameters"):
                obj = InstanceParameterInput()
                obj._deserialize(item)
                self._Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExclusiveInstanceResponse(AbstractModel):
    """ModifyExclusiveInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 独享实例详情信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.InstanceDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = InstanceDetail()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyIPStrategyRequest(AbstractModel):
    """ModifyIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待修改的策略所属服务的唯一ID。
        :type ServiceId: str
        :param _StrategyId: 待修改的策略唯一ID。
        :type StrategyId: str
        :param _StrategyData: 待修改的策略详情。
        :type StrategyData: str
        """
        self._ServiceId = None
        self._StrategyId = None
        self._StrategyData = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyData(self):
        return self._StrategyData

    @StrategyData.setter
    def StrategyData(self, StrategyData):
        self._StrategyData = StrategyData


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._StrategyData = params.get("StrategyData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIPStrategyResponse(AbstractModel):
    """ModifyIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyPluginRequest(AbstractModel):
    """ModifyPlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PluginId: 要修改的插件ID。
        :type PluginId: str
        :param _PluginName: 要修改的API网关插件名称。最长50个字符，支持 a-z,A-Z,0-9,_, 必须字母开头，字母或者数字结尾。
        :type PluginName: str
        :param _Description: 要修改的插件描述，限定200字以内。
        :type Description: str
        :param _PluginData: 要修改的插件定义语句，支持json。
        :type PluginData: str
        """
        self._PluginId = None
        self._PluginName = None
        self._Description = None
        self._PluginData = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def PluginData(self):
        return self._PluginData

    @PluginData.setter
    def PluginData(self, PluginData):
        self._PluginData = PluginData


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._PluginName = params.get("PluginName")
        self._Description = params.get("Description")
        self._PluginData = params.get("PluginData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPluginResponse(AbstractModel):
    """ModifyPlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyServiceEnvironmentStrategyRequest(AbstractModel):
    """ModifyServiceEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务的唯一ID。
        :type ServiceId: str
        :param _Strategy: 限流值。
        :type Strategy: int
        :param _EnvironmentNames: 环境列表。
        :type EnvironmentNames: list of str
        """
        self._ServiceId = None
        self._Strategy = None
        self._EnvironmentNames = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def EnvironmentNames(self):
        return self._EnvironmentNames

    @EnvironmentNames.setter
    def EnvironmentNames(self, EnvironmentNames):
        self._EnvironmentNames = EnvironmentNames


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._Strategy = params.get("Strategy")
        self._EnvironmentNames = params.get("EnvironmentNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceEnvironmentStrategyResponse(AbstractModel):
    """ModifyServiceEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyServiceRequest(AbstractModel):
    """ModifyService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待修改服务的唯一 Id。
        :type ServiceId: str
        :param _ServiceName: 修改后的服务名称。
        :type ServiceName: str
        :param _ServiceDesc: 修改后的服务描述。
        :type ServiceDesc: str
        :param _Protocol: 修改后的服务前端请求类型，如 http、https和 http&https。
        :type Protocol: str
        :param _NetTypes: 网络类型列表，用于指定支持的访问类型，INNER为内网访问，OUTER为外网访问。默认为OUTER。
        :type NetTypes: list of str
        :param _UniqVpcId: vpc属性，选择VPC后不可修改。为服务选择VPC后，可对接该VPC下的后端资源
        :type UniqVpcId: str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._ServiceDesc = None
        self._Protocol = None
        self._NetTypes = None
        self._UniqVpcId = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._ServiceDesc = params.get("ServiceDesc")
        self._Protocol = params.get("Protocol")
        self._NetTypes = params.get("NetTypes")
        self._UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceResponse(AbstractModel):
    """ModifyService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ModifySubDomainRequest(AbstractModel):
    """ModifySubDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param _SubDomain: 待修改路径映射的自定义的域名。
        :type SubDomain: str
        :param _IsDefaultMapping: 是否修改为使用默认路径映射。为 true，表示使用默认路径映射，为 false，表示使用自定义路径映射。
        :type IsDefaultMapping: bool
        :param _CertificateId: 证书 ID，协议包含 HTTPS 的时候要传该字段。
        :type CertificateId: str
        :param _Protocol: 修改后的自定义域名协议类型。（http，https 或 http&https)
        :type Protocol: str
        :param _PathMappingSet: 修改后的路径映射列表。
        :type PathMappingSet: list of PathMapping
        :param _NetType: 网络类型 （'INNER' 或 'OUTER'）
        :type NetType: str
        :param _IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。
        :type IsForcedHttps: bool
        """
        self._ServiceId = None
        self._SubDomain = None
        self._IsDefaultMapping = None
        self._CertificateId = None
        self._Protocol = None
        self._PathMappingSet = None
        self._NetType = None
        self._IsForcedHttps = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def IsDefaultMapping(self):
        return self._IsDefaultMapping

    @IsDefaultMapping.setter
    def IsDefaultMapping(self, IsDefaultMapping):
        self._IsDefaultMapping = IsDefaultMapping

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PathMappingSet(self):
        return self._PathMappingSet

    @PathMappingSet.setter
    def PathMappingSet(self, PathMappingSet):
        self._PathMappingSet = PathMappingSet

    @property
    def NetType(self):
        return self._NetType

    @NetType.setter
    def NetType(self, NetType):
        self._NetType = NetType

    @property
    def IsForcedHttps(self):
        return self._IsForcedHttps

    @IsForcedHttps.setter
    def IsForcedHttps(self, IsForcedHttps):
        self._IsForcedHttps = IsForcedHttps


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        self._IsDefaultMapping = params.get("IsDefaultMapping")
        self._CertificateId = params.get("CertificateId")
        self._Protocol = params.get("Protocol")
        if params.get("PathMappingSet") is not None:
            self._PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self._PathMappingSet.append(obj)
        self._NetType = params.get("NetType")
        self._IsForcedHttps = params.get("IsForcedHttps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubDomainResponse(AbstractModel):
    """ModifySubDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 修改自定义域名操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class ModifyUpstreamRequest(AbstractModel):
    """ModifyUpstream请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UpstreamId: 后端通道唯一ID
        :type UpstreamId: str
        :param _UpstreamName: 后端通道名字
        :type UpstreamName: str
        :param _UpstreamDescription: 后端通道描述
        :type UpstreamDescription: str
        :param _Scheme: 后端协议，取值范围：HTTP, HTTPS
        :type Scheme: str
        :param _UpstreamType: 后端访问类型，取值范围：IP_PORT, K8S
        :type UpstreamType: str
        :param _Algorithm: 负载均衡算法，取值范围：ROUND_ROBIN
        :type Algorithm: str
        :param _UniqVpcId: VPC唯一ID
        :type UniqVpcId: str
        :param _Retries: 请求重试次数，默认3次
        :type Retries: int
        :param _UpstreamHost: 网关转发到后端的 Host 请求头
        :type UpstreamHost: str
        :param _Nodes: 后端节点列表
        :type Nodes: list of UpstreamNode
        :param _HealthChecker: 健康检查配置，目前只支持VPC通道
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param _K8sService: 容器服务配置
        :type K8sService: list of K8sService
        """
        self._UpstreamId = None
        self._UpstreamName = None
        self._UpstreamDescription = None
        self._Scheme = None
        self._UpstreamType = None
        self._Algorithm = None
        self._UniqVpcId = None
        self._Retries = None
        self._UpstreamHost = None
        self._Nodes = None
        self._HealthChecker = None
        self._K8sService = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def UpstreamName(self):
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def UpstreamDescription(self):
        return self._UpstreamDescription

    @UpstreamDescription.setter
    def UpstreamDescription(self, UpstreamDescription):
        self._UpstreamDescription = UpstreamDescription

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def UpstreamHost(self):
        return self._UpstreamHost

    @UpstreamHost.setter
    def UpstreamHost(self, UpstreamHost):
        self._UpstreamHost = UpstreamHost

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def HealthChecker(self):
        return self._HealthChecker

    @HealthChecker.setter
    def HealthChecker(self, HealthChecker):
        self._HealthChecker = HealthChecker

    @property
    def K8sService(self):
        return self._K8sService

    @K8sService.setter
    def K8sService(self, K8sService):
        self._K8sService = K8sService


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._UpstreamName = params.get("UpstreamName")
        self._UpstreamDescription = params.get("UpstreamDescription")
        self._Scheme = params.get("Scheme")
        self._UpstreamType = params.get("UpstreamType")
        self._Algorithm = params.get("Algorithm")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Retries = params.get("Retries")
        self._UpstreamHost = params.get("UpstreamHost")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        if params.get("HealthChecker") is not None:
            self._HealthChecker = UpstreamHealthChecker()
            self._HealthChecker._deserialize(params.get("HealthChecker"))
        if params.get("K8sService") is not None:
            self._K8sService = []
            for item in params.get("K8sService"):
                obj = K8sService()
                obj._deserialize(item)
                self._K8sService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUpstreamResponse(AbstractModel):
    """ModifyUpstream返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 返回修改后的后端通道信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ModifyUpstreamResultInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ModifyUpstreamResultInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ModifyUpstreamResultInfo(AbstractModel):
    """后端通道详细信息

    """

    def __init__(self):
        r"""
        :param _UpstreamId: 后端通道唯一ID
        :type UpstreamId: str
        :param _UpstreamName: 后端通道名字
        :type UpstreamName: str
        :param _UpstreamDescription: 后端通道描述
        :type UpstreamDescription: str
        :param _Scheme: 后端协议，取值范围：HTTP, HTTPS
        :type Scheme: str
        :param _Algorithm: 负载均衡算法，取值范围：ROUND_ROBIN
        :type Algorithm: str
        :param _UniqVpcId: VPC唯一ID
        :type UniqVpcId: str
        :param _Retries: 请求重试次数
        :type Retries: int
        :param _Nodes: 后端节点
        :type Nodes: list of UpstreamNode
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _HealthChecker: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param _UpstreamType: 后端的类型，取值范围：IP_PORT, K8S
        :type UpstreamType: str
        :param _K8sServices: K8S容器服务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type K8sServices: list of K8sService
        :param _UpstreamHost: 网关转发给后端的Host请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHost: str
        """
        self._UpstreamId = None
        self._UpstreamName = None
        self._UpstreamDescription = None
        self._Scheme = None
        self._Algorithm = None
        self._UniqVpcId = None
        self._Retries = None
        self._Nodes = None
        self._CreatedTime = None
        self._HealthChecker = None
        self._UpstreamType = None
        self._K8sServices = None
        self._UpstreamHost = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def UpstreamName(self):
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def UpstreamDescription(self):
        return self._UpstreamDescription

    @UpstreamDescription.setter
    def UpstreamDescription(self, UpstreamDescription):
        self._UpstreamDescription = UpstreamDescription

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def HealthChecker(self):
        return self._HealthChecker

    @HealthChecker.setter
    def HealthChecker(self, HealthChecker):
        self._HealthChecker = HealthChecker

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def K8sServices(self):
        return self._K8sServices

    @K8sServices.setter
    def K8sServices(self, K8sServices):
        self._K8sServices = K8sServices

    @property
    def UpstreamHost(self):
        return self._UpstreamHost

    @UpstreamHost.setter
    def UpstreamHost(self, UpstreamHost):
        self._UpstreamHost = UpstreamHost


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._UpstreamName = params.get("UpstreamName")
        self._UpstreamDescription = params.get("UpstreamDescription")
        self._Scheme = params.get("Scheme")
        self._Algorithm = params.get("Algorithm")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Retries = params.get("Retries")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._CreatedTime = params.get("CreatedTime")
        if params.get("HealthChecker") is not None:
            self._HealthChecker = UpstreamHealthChecker()
            self._HealthChecker._deserialize(params.get("HealthChecker"))
        self._UpstreamType = params.get("UpstreamType")
        if params.get("K8sServices") is not None:
            self._K8sServices = []
            for item in params.get("K8sServices"):
                obj = K8sService()
                obj._deserialize(item)
                self._K8sServices.append(obj)
        self._UpstreamHost = params.get("UpstreamHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUsagePlanRequest(AbstractModel):
    """ModifyUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 使用计划唯一 ID。
        :type UsagePlanId: str
        :param _UsagePlanName: 修改后的用户自定义的使用计划名称。
        :type UsagePlanName: str
        :param _UsagePlanDesc: 修改后的用户自定义的使用计划描述。
        :type UsagePlanDesc: str
        :param _MaxRequestNum: 请求配额总数，取值范围为-1或者[1, 99999999]，默认为-1，表示不开启。
        :type MaxRequestNum: int
        :param _MaxRequestNumPreSec: 每秒请求限制数，取值范围为-1或者[1, 2000]，默认-1，表示不开启。
        :type MaxRequestNumPreSec: int
        """
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNum = None
        self._MaxRequestNumPreSec = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUsagePlanResponse(AbstractModel):
    """ModifyUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = UsagePlanInfo()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class NetworkConfig(AbstractModel):
    """独享实例网络配置

    """

    def __init__(self):
        r"""
        :param _InternetMaxBandwidthOut: 最大出带宽
        :type InternetMaxBandwidthOut: int
        :param _EnableInternetInbound: EnableInternetInbound信息
        :type EnableInternetInbound: bool
        :param _EnableInternetOutbound: EnableInternetOutbound信息
        :type EnableInternetOutbound: bool
        :param _InboundIpAddresses: InboundIpAddresses信息
        :type InboundIpAddresses: list of str
        :param _OutboundIpAddresses: OutboundIpAddresses信息
        :type OutboundIpAddresses: list of str
        """
        self._InternetMaxBandwidthOut = None
        self._EnableInternetInbound = None
        self._EnableInternetOutbound = None
        self._InboundIpAddresses = None
        self._OutboundIpAddresses = None

    @property
    def InternetMaxBandwidthOut(self):
        return self._InternetMaxBandwidthOut

    @InternetMaxBandwidthOut.setter
    def InternetMaxBandwidthOut(self, InternetMaxBandwidthOut):
        self._InternetMaxBandwidthOut = InternetMaxBandwidthOut

    @property
    def EnableInternetInbound(self):
        return self._EnableInternetInbound

    @EnableInternetInbound.setter
    def EnableInternetInbound(self, EnableInternetInbound):
        self._EnableInternetInbound = EnableInternetInbound

    @property
    def EnableInternetOutbound(self):
        return self._EnableInternetOutbound

    @EnableInternetOutbound.setter
    def EnableInternetOutbound(self, EnableInternetOutbound):
        self._EnableInternetOutbound = EnableInternetOutbound

    @property
    def InboundIpAddresses(self):
        return self._InboundIpAddresses

    @InboundIpAddresses.setter
    def InboundIpAddresses(self, InboundIpAddresses):
        self._InboundIpAddresses = InboundIpAddresses

    @property
    def OutboundIpAddresses(self):
        return self._OutboundIpAddresses

    @OutboundIpAddresses.setter
    def OutboundIpAddresses(self, OutboundIpAddresses):
        self._OutboundIpAddresses = OutboundIpAddresses


    def _deserialize(self, params):
        self._InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self._EnableInternetInbound = params.get("EnableInternetInbound")
        self._EnableInternetOutbound = params.get("EnableInternetOutbound")
        self._InboundIpAddresses = params.get("InboundIpAddresses")
        self._OutboundIpAddresses = params.get("OutboundIpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OauthConfig(AbstractModel):
    """Oauth授权配置信息

    """

    def __init__(self):
        r"""
        :param _PublicKey: 公钥，用于验证用户token。
        :type PublicKey: str
        :param _TokenLocation: token传递位置。
        :type TokenLocation: str
        :param _LoginRedirectUrl: 重定向地址，用于引导用户登录操作。
        :type LoginRedirectUrl: str
        """
        self._PublicKey = None
        self._TokenLocation = None
        self._LoginRedirectUrl = None

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def TokenLocation(self):
        return self._TokenLocation

    @TokenLocation.setter
    def TokenLocation(self, TokenLocation):
        self._TokenLocation = TokenLocation

    @property
    def LoginRedirectUrl(self):
        return self._LoginRedirectUrl

    @LoginRedirectUrl.setter
    def LoginRedirectUrl(self, LoginRedirectUrl):
        self._LoginRedirectUrl = LoginRedirectUrl


    def _deserialize(self, params):
        self._PublicKey = params.get("PublicKey")
        self._TokenLocation = params.get("TokenLocation")
        self._LoginRedirectUrl = params.get("LoginRedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterInfo(AbstractModel):
    """独享实例配置参数

    """

    def __init__(self):
        r"""
        :param _Name: 名字
        :type Name: str
        :param _Value: 当前值
        :type Value: int
        :param _Default: 默认值
        :type Default: int
        :param _Unit: 单位
        :type Unit: str
        :param _Type: 类型, integer|string
        :type Type: str
        :param _Minimum: 最小
        :type Minimum: int
        :param _Maximum: 最大
        :type Maximum: int
        :param _ModifedTime: 修改时间
        :type ModifedTime: str
        :param _ValueString: 字符类型的值，当Type为string时才有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueString: str
        :param _DefaultValueString: 字符类型的默认值，当Type为string时才有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValueString: str
        :param _Range: 可调整范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: str
        """
        self._Name = None
        self._Value = None
        self._Default = None
        self._Unit = None
        self._Type = None
        self._Minimum = None
        self._Maximum = None
        self._ModifedTime = None
        self._ValueString = None
        self._DefaultValueString = None
        self._Range = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Default(self):
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def Unit(self):
        return self._Unit

    @Unit.setter
    def Unit(self, Unit):
        self._Unit = Unit

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Minimum(self):
        return self._Minimum

    @Minimum.setter
    def Minimum(self, Minimum):
        self._Minimum = Minimum

    @property
    def Maximum(self):
        return self._Maximum

    @Maximum.setter
    def Maximum(self, Maximum):
        self._Maximum = Maximum

    @property
    def ModifedTime(self):
        warnings.warn("parameter `ModifedTime` is deprecated", DeprecationWarning) 

        return self._ModifedTime

    @ModifedTime.setter
    def ModifedTime(self, ModifedTime):
        warnings.warn("parameter `ModifedTime` is deprecated", DeprecationWarning) 

        self._ModifedTime = ModifedTime

    @property
    def ValueString(self):
        return self._ValueString

    @ValueString.setter
    def ValueString(self, ValueString):
        self._ValueString = ValueString

    @property
    def DefaultValueString(self):
        return self._DefaultValueString

    @DefaultValueString.setter
    def DefaultValueString(self, DefaultValueString):
        self._DefaultValueString = DefaultValueString

    @property
    def Range(self):
        return self._Range

    @Range.setter
    def Range(self, Range):
        self._Range = Range


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Default = params.get("Default")
        self._Unit = params.get("Unit")
        self._Type = params.get("Type")
        self._Minimum = params.get("Minimum")
        self._Maximum = params.get("Maximum")
        self._ModifedTime = params.get("ModifedTime")
        self._ValueString = params.get("ValueString")
        self._DefaultValueString = params.get("DefaultValueString")
        self._Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathMapping(AbstractModel):
    """自定义域名的路径映射。

    """

    def __init__(self):
        r"""
        :param _Path: 路径。
        :type Path: str
        :param _Environment: 发布环境，可选值为“test”、 ”prepub“、”release“。
        :type Environment: str
        """
        self._Path = None
        self._Environment = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Plugin(AbstractModel):
    """API网关插件详情。

    """

    def __init__(self):
        r"""
        :param _PluginId: 插件ID。
        :type PluginId: str
        :param _PluginName: 插件名称。
        :type PluginName: str
        :param _PluginType: 插件类型。
        :type PluginType: str
        :param _PluginData: 插件定义语句。
        :type PluginData: str
        :param _Description: 插件描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _CreatedTime: 插件创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type CreatedTime: str
        :param _ModifiedTime: 插件修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type ModifiedTime: str
        :param _AttachedApiTotalCount: 插件绑定的API总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachedApiTotalCount: int
        :param _AttachedApis: 插件绑定的API信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachedApis: list of AttachedApiInfo
        """
        self._PluginId = None
        self._PluginName = None
        self._PluginType = None
        self._PluginData = None
        self._Description = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._AttachedApiTotalCount = None
        self._AttachedApis = None

    @property
    def PluginId(self):
        return self._PluginId

    @PluginId.setter
    def PluginId(self, PluginId):
        self._PluginId = PluginId

    @property
    def PluginName(self):
        return self._PluginName

    @PluginName.setter
    def PluginName(self, PluginName):
        self._PluginName = PluginName

    @property
    def PluginType(self):
        return self._PluginType

    @PluginType.setter
    def PluginType(self, PluginType):
        self._PluginType = PluginType

    @property
    def PluginData(self):
        return self._PluginData

    @PluginData.setter
    def PluginData(self, PluginData):
        self._PluginData = PluginData

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def AttachedApiTotalCount(self):
        return self._AttachedApiTotalCount

    @AttachedApiTotalCount.setter
    def AttachedApiTotalCount(self, AttachedApiTotalCount):
        self._AttachedApiTotalCount = AttachedApiTotalCount

    @property
    def AttachedApis(self):
        return self._AttachedApis

    @AttachedApis.setter
    def AttachedApis(self, AttachedApis):
        self._AttachedApis = AttachedApis


    def _deserialize(self, params):
        self._PluginId = params.get("PluginId")
        self._PluginName = params.get("PluginName")
        self._PluginType = params.get("PluginType")
        self._PluginData = params.get("PluginData")
        self._Description = params.get("Description")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._AttachedApiTotalCount = params.get("AttachedApiTotalCount")
        if params.get("AttachedApis") is not None:
            self._AttachedApis = []
            for item in params.get("AttachedApis"):
                obj = AttachedApiInfo()
                obj._deserialize(item)
                self._AttachedApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginSummary(AbstractModel):
    """插件列表详情。

    """

    def __init__(self):
        r"""
        :param _TotalCount: 插件个数。
        :type TotalCount: int
        :param _PluginSet: 插件详情。
        :type PluginSet: list of Plugin
        """
        self._TotalCount = None
        self._PluginSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PluginSet(self):
        return self._PluginSet

    @PluginSet.setter
    def PluginSet(self, PluginSet):
        self._PluginSet = PluginSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PluginSet") is not None:
            self._PluginSet = []
            for item in params.get("PluginSet"):
                obj = Plugin()
                obj._deserialize(item)
                self._PluginSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseService(AbstractModel):
    """发布服务返回

    """

    def __init__(self):
        r"""
        :param _ReleaseDesc: 发布时的备注信息填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseDesc: str
        :param _ReleaseVersion: 发布的版本id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseVersion: str
        """
        self._ReleaseDesc = None
        self._ReleaseVersion = None

    @property
    def ReleaseDesc(self):
        return self._ReleaseDesc

    @ReleaseDesc.setter
    def ReleaseDesc(self, ReleaseDesc):
        self._ReleaseDesc = ReleaseDesc

    @property
    def ReleaseVersion(self):
        return self._ReleaseVersion

    @ReleaseVersion.setter
    def ReleaseVersion(self, ReleaseVersion):
        self._ReleaseVersion = ReleaseVersion


    def _deserialize(self, params):
        self._ReleaseDesc = params.get("ReleaseDesc")
        self._ReleaseVersion = params.get("ReleaseVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseServiceRequest(AbstractModel):
    """ReleaseService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待发布服务的唯一 ID。
        :type ServiceId: str
        :param _EnvironmentName: 待发布的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。
        :type EnvironmentName: str
        :param _ReleaseDesc: 本次的发布描述。
        :type ReleaseDesc: str
        :param _ApiIds: apiId列表，预留字段，默认全量api发布。
        :type ApiIds: list of str
        """
        self._ServiceId = None
        self._EnvironmentName = None
        self._ReleaseDesc = None
        self._ApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ReleaseDesc(self):
        return self._ReleaseDesc

    @ReleaseDesc.setter
    def ReleaseDesc(self, ReleaseDesc):
        self._ReleaseDesc = ReleaseDesc

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ReleaseDesc = params.get("ReleaseDesc")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseServiceResponse(AbstractModel):
    """ReleaseService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 发布信息。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ReleaseService`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ReleaseService()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ReqParameter(AbstractModel):
    """请求参数

    """

    def __init__(self):
        r"""
        :param _Name: API 的前端参数名称。
        :type Name: str
        :param _Position: API 的前端参数位置，如 header。目前支持 header、query、path。
        :type Position: str
        :param _Type: API 的前端参数类型，如 String、int。
        :type Type: str
        :param _DefaultValue: API 的前端参数默认值。
        :type DefaultValue: str
        :param _Required: API 的前端参数是否必填，True：表示必填，False：表示可选。
        :type Required: bool
        :param _Desc: API 的前端参数备注。
        :type Desc: str
        """
        self._Name = None
        self._Position = None
        self._Type = None
        self._DefaultValue = None
        self._Required = None
        self._Desc = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Position = params.get("Position")
        self._Type = params.get("Type")
        self._DefaultValue = params.get("DefaultValue")
        self._Required = params.get("Required")
        self._Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestConfig(AbstractModel):
    """前端路径配置

    """

    def __init__(self):
        r"""
        :param _Path: API 的路径，如 /path。
        :type Path: str
        :param _Method: API 的请求方法，如 GET。
        :type Method: str
        """
        self._Path = None
        self._Method = None

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestParameter(AbstractModel):
    """请求参数

    """

    def __init__(self):
        r"""
        :param _Name: 请求参数名称
        :type Name: str
        :param _Desc: 描述
        :type Desc: str
        :param _Position: 参数位置
        :type Position: str
        :param _Type: 参数类型
        :type Type: str
        :param _DefaultValue: 默认值
        :type DefaultValue: str
        :param _Required: 是否必须
        :type Required: bool
        """
        self._Name = None
        self._Desc = None
        self._Position = None
        self._Type = None
        self._DefaultValue = None
        self._Required = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def Required(self):
        return self._Required

    @Required.setter
    def Required(self, Required):
        self._Required = Required


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Desc = params.get("Desc")
        self._Position = params.get("Position")
        self._Type = params.get("Type")
        self._DefaultValue = params.get("DefaultValue")
        self._Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAPIDocPasswordRequest(AbstractModel):
    """ResetAPIDocPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self._ApiDocId = None

    @property
    def ApiDocId(self):
        return self._ApiDocId

    @ApiDocId.setter
    def ApiDocId(self, ApiDocId):
        self._ApiDocId = ApiDocId


    def _deserialize(self, params):
        self._ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAPIDocPasswordResponse(AbstractModel):
    """ResetAPIDocPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: API文档基本信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = APIDoc()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class ResponseErrorCodeReq(AbstractModel):
    """错误码入参

    """

    def __init__(self):
        r"""
        :param _Code: 自定义响应配置错误码。
        :type Code: int
        :param _Msg: 自定义响应配置错误信息。
        :type Msg: str
        :param _Desc: 自定义响应配置错误码备注。
        :type Desc: str
        :param _ConvertedCode: 自定义错误码转换。
        :type ConvertedCode: int
        :param _NeedConvert: 是否需要开启错误码转换。
        :type NeedConvert: bool
        """
        self._Code = None
        self._Msg = None
        self._Desc = None
        self._ConvertedCode = None
        self._NeedConvert = None

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Desc(self):
        return self._Desc

    @Desc.setter
    def Desc(self, Desc):
        self._Desc = Desc

    @property
    def ConvertedCode(self):
        return self._ConvertedCode

    @ConvertedCode.setter
    def ConvertedCode(self, ConvertedCode):
        self._ConvertedCode = ConvertedCode

    @property
    def NeedConvert(self):
        return self._NeedConvert

    @NeedConvert.setter
    def NeedConvert(self, NeedConvert):
        self._NeedConvert = NeedConvert


    def _deserialize(self, params):
        self._Code = params.get("Code")
        self._Msg = params.get("Msg")
        self._Desc = params.get("Desc")
        self._ConvertedCode = params.get("ConvertedCode")
        self._NeedConvert = params.get("NeedConvert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """展示服务列表用

    """

    def __init__(self):
        r"""
        :param _InnerHttpsPort: 内网访问https端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpsPort: int
        :param _ServiceDesc: 用户自定义的服务描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param _Protocol: 服务的前端请求类型。如http、https 或者 http&https。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _NetTypes: 服务支持的网络类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetTypes: list of str
        :param _ExclusiveSetName: 独占集群名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusiveSetName: str
        :param _ServiceId: 服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpVersion: str
        :param _AvailableEnvironments: 已经发布的环境列表。如test、prepub、release。
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableEnvironments: list of str
        :param _ServiceName: 用户自定义的服务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _OuterSubDomain: 系统为该服务分配的外网域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type OuterSubDomain: str
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _InnerHttpPort: 内网访问http端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpPort: int
        :param _InnerSubDomain: 系统为该服务自动分配的内网域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerSubDomain: str
        :param _TradeIsolateStatus: 服务的计费状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeIsolateStatus: int
        :param _Tags: 服务绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _InstanceId: 独享实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _SetType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SetType: str
        :param _DeploymentType: 服务部署的集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentType: str
        """
        self._InnerHttpsPort = None
        self._ServiceDesc = None
        self._Protocol = None
        self._ModifiedTime = None
        self._NetTypes = None
        self._ExclusiveSetName = None
        self._ServiceId = None
        self._IpVersion = None
        self._AvailableEnvironments = None
        self._ServiceName = None
        self._OuterSubDomain = None
        self._CreatedTime = None
        self._InnerHttpPort = None
        self._InnerSubDomain = None
        self._TradeIsolateStatus = None
        self._Tags = None
        self._InstanceId = None
        self._SetType = None
        self._DeploymentType = None

    @property
    def InnerHttpsPort(self):
        return self._InnerHttpsPort

    @InnerHttpsPort.setter
    def InnerHttpsPort(self, InnerHttpsPort):
        self._InnerHttpsPort = InnerHttpsPort

    @property
    def ServiceDesc(self):
        return self._ServiceDesc

    @ServiceDesc.setter
    def ServiceDesc(self, ServiceDesc):
        self._ServiceDesc = ServiceDesc

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def NetTypes(self):
        return self._NetTypes

    @NetTypes.setter
    def NetTypes(self, NetTypes):
        self._NetTypes = NetTypes

    @property
    def ExclusiveSetName(self):
        return self._ExclusiveSetName

    @ExclusiveSetName.setter
    def ExclusiveSetName(self, ExclusiveSetName):
        self._ExclusiveSetName = ExclusiveSetName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def IpVersion(self):
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def AvailableEnvironments(self):
        return self._AvailableEnvironments

    @AvailableEnvironments.setter
    def AvailableEnvironments(self, AvailableEnvironments):
        self._AvailableEnvironments = AvailableEnvironments

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def OuterSubDomain(self):
        return self._OuterSubDomain

    @OuterSubDomain.setter
    def OuterSubDomain(self, OuterSubDomain):
        self._OuterSubDomain = OuterSubDomain

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def InnerHttpPort(self):
        return self._InnerHttpPort

    @InnerHttpPort.setter
    def InnerHttpPort(self, InnerHttpPort):
        self._InnerHttpPort = InnerHttpPort

    @property
    def InnerSubDomain(self):
        return self._InnerSubDomain

    @InnerSubDomain.setter
    def InnerSubDomain(self, InnerSubDomain):
        self._InnerSubDomain = InnerSubDomain

    @property
    def TradeIsolateStatus(self):
        return self._TradeIsolateStatus

    @TradeIsolateStatus.setter
    def TradeIsolateStatus(self, TradeIsolateStatus):
        self._TradeIsolateStatus = TradeIsolateStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SetType(self):
        return self._SetType

    @SetType.setter
    def SetType(self, SetType):
        self._SetType = SetType

    @property
    def DeploymentType(self):
        return self._DeploymentType

    @DeploymentType.setter
    def DeploymentType(self, DeploymentType):
        self._DeploymentType = DeploymentType


    def _deserialize(self, params):
        self._InnerHttpsPort = params.get("InnerHttpsPort")
        self._ServiceDesc = params.get("ServiceDesc")
        self._Protocol = params.get("Protocol")
        self._ModifiedTime = params.get("ModifiedTime")
        self._NetTypes = params.get("NetTypes")
        self._ExclusiveSetName = params.get("ExclusiveSetName")
        self._ServiceId = params.get("ServiceId")
        self._IpVersion = params.get("IpVersion")
        self._AvailableEnvironments = params.get("AvailableEnvironments")
        self._ServiceName = params.get("ServiceName")
        self._OuterSubDomain = params.get("OuterSubDomain")
        self._CreatedTime = params.get("CreatedTime")
        self._InnerHttpPort = params.get("InnerHttpPort")
        self._InnerSubDomain = params.get("InnerSubDomain")
        self._TradeIsolateStatus = params.get("TradeIsolateStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._SetType = params.get("SetType")
        self._DeploymentType = params.get("DeploymentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceConfig(AbstractModel):
    """ServiceConfig配置

    """

    def __init__(self):
        r"""
        :param _Product: 后端类型。启用vpc时生效，目前支持的类型为clb, cvm和upstream
        :type Product: str
        :param _UniqVpcId: vpc 的唯一ID。
        :type UniqVpcId: str
        :param _Url: API 的后端服务url。如果ServiceType是HTTP，则此参数必传。
        :type Url: str
        :param _Path: API 的后端服务路径，如 /path。如果 ServiceType 是 HTTP，则此参数必传。前后端路径可不同。
        :type Path: str
        :param _Method: API的后端服务请求方法，如 GET。如果 ServiceType 是 HTTP，则此参数必传。前后端方法可不同。
        :type Method: str
        :param _UpstreamId: 当绑定vpc通道才需要
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamId: str
        :param _CosConfig: API后端COS配置。如果 ServiceType 是 COS，则此参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosConfig: :class:`tencentcloud.apigateway.v20180808.models.CosConfig`
        """
        self._Product = None
        self._UniqVpcId = None
        self._Url = None
        self._Path = None
        self._Method = None
        self._UpstreamId = None
        self._CosConfig = None

    @property
    def Product(self):
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def CosConfig(self):
        return self._CosConfig

    @CosConfig.setter
    def CosConfig(self, CosConfig):
        self._CosConfig = CosConfig


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Url = params.get("Url")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._UpstreamId = params.get("UpstreamId")
        if params.get("CosConfig") is not None:
            self._CosConfig = CosConfig()
            self._CosConfig._deserialize(params.get("CosConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentSet(AbstractModel):
    """服务绑定环境详情

    """

    def __init__(self):
        r"""
        :param _TotalCount: 服务绑定环境总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _EnvironmentList: 服务绑定环境列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentList: list of Environment
        """
        self._TotalCount = None
        self._EnvironmentList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentList(self):
        return self._EnvironmentList

    @EnvironmentList.setter
    def EnvironmentList(self, EnvironmentList):
        self._EnvironmentList = EnvironmentList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self._EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = Environment()
                obj._deserialize(item)
                self._EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentStrategy(AbstractModel):
    """服务环境策略

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: 环境名。
        :type EnvironmentName: str
        :param _Url: 访问服务对应环境的url。
        :type Url: str
        :param _Status: 发布状态。
        :type Status: int
        :param _VersionName: 发布的版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _Strategy: 限流值。
        :type Strategy: int
        :param _MaxStrategy: 最大限流值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStrategy: int
        """
        self._EnvironmentName = None
        self._Url = None
        self._Status = None
        self._VersionName = None
        self._Strategy = None
        self._MaxStrategy = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Strategy(self):
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def MaxStrategy(self):
        return self._MaxStrategy

    @MaxStrategy.setter
    def MaxStrategy(self, MaxStrategy):
        self._MaxStrategy = MaxStrategy


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._VersionName = params.get("VersionName")
        self._Strategy = params.get("Strategy")
        self._MaxStrategy = params.get("MaxStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentStrategyStatus(AbstractModel):
    """环境绑定策略列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 限流策略数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _EnvironmentList: 限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentList: list of ServiceEnvironmentStrategy
        """
        self._TotalCount = None
        self._EnvironmentList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentList(self):
        return self._EnvironmentList

    @EnvironmentList.setter
    def EnvironmentList(self, EnvironmentList):
        self._EnvironmentList = EnvironmentList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self._EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = ServiceEnvironmentStrategy()
                obj._deserialize(item)
                self._EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceParameter(AbstractModel):
    """ServiceParameter

    """

    def __init__(self):
        r"""
        :param _Name: API的后端服务参数名称。只有ServiceType是HTTP才会用到此参数。前后端参数名称可不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Position: API 的后端服务参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。前后端参数位置可配置不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: str
        :param _RelevantRequestParameterPosition: API 的后端服务参数对应的前端参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterPosition: str
        :param _RelevantRequestParameterName: API 的后端服务参数对应的前端参数名称。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterName: str
        :param _DefaultValue: API 的后端服务参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        :param _RelevantRequestParameterDesc: API 的后端服务参数备注。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterDesc: str
        :param _RelevantRequestParameterType: API 的后端服务参数类型。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterType: str
        """
        self._Name = None
        self._Position = None
        self._RelevantRequestParameterPosition = None
        self._RelevantRequestParameterName = None
        self._DefaultValue = None
        self._RelevantRequestParameterDesc = None
        self._RelevantRequestParameterType = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        self._Position = Position

    @property
    def RelevantRequestParameterPosition(self):
        return self._RelevantRequestParameterPosition

    @RelevantRequestParameterPosition.setter
    def RelevantRequestParameterPosition(self, RelevantRequestParameterPosition):
        self._RelevantRequestParameterPosition = RelevantRequestParameterPosition

    @property
    def RelevantRequestParameterName(self):
        return self._RelevantRequestParameterName

    @RelevantRequestParameterName.setter
    def RelevantRequestParameterName(self, RelevantRequestParameterName):
        self._RelevantRequestParameterName = RelevantRequestParameterName

    @property
    def DefaultValue(self):
        return self._DefaultValue

    @DefaultValue.setter
    def DefaultValue(self, DefaultValue):
        self._DefaultValue = DefaultValue

    @property
    def RelevantRequestParameterDesc(self):
        return self._RelevantRequestParameterDesc

    @RelevantRequestParameterDesc.setter
    def RelevantRequestParameterDesc(self, RelevantRequestParameterDesc):
        self._RelevantRequestParameterDesc = RelevantRequestParameterDesc

    @property
    def RelevantRequestParameterType(self):
        return self._RelevantRequestParameterType

    @RelevantRequestParameterType.setter
    def RelevantRequestParameterType(self, RelevantRequestParameterType):
        self._RelevantRequestParameterType = RelevantRequestParameterType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Position = params.get("Position")
        self._RelevantRequestParameterPosition = params.get("RelevantRequestParameterPosition")
        self._RelevantRequestParameterName = params.get("RelevantRequestParameterName")
        self._DefaultValue = params.get("DefaultValue")
        self._RelevantRequestParameterDesc = params.get("RelevantRequestParameterDesc")
        self._RelevantRequestParameterType = params.get("RelevantRequestParameterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseHistory(AbstractModel):
    """服务发布历史

    """

    def __init__(self):
        r"""
        :param _TotalCount: 发布版本总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _VersionList: 历史版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionList: list of ServiceReleaseHistoryInfo
        """
        self._TotalCount = None
        self._VersionList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VersionList(self):
        return self._VersionList

    @VersionList.setter
    def VersionList(self, VersionList):
        self._VersionList = VersionList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VersionList") is not None:
            self._VersionList = []
            for item in params.get("VersionList"):
                obj = ServiceReleaseHistoryInfo()
                obj._deserialize(item)
                self._VersionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseHistoryInfo(AbstractModel):
    """服务发布列表详情

    """

    def __init__(self):
        r"""
        :param _VersionName: 版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _VersionDesc: 版本描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionDesc: str
        :param _ReleaseTime: 版本发布时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        """
        self._VersionName = None
        self._VersionDesc = None
        self._ReleaseTime = None

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def VersionDesc(self):
        return self._VersionDesc

    @VersionDesc.setter
    def VersionDesc(self, VersionDesc):
        self._VersionDesc = VersionDesc

    @property
    def ReleaseTime(self):
        return self._ReleaseTime

    @ReleaseTime.setter
    def ReleaseTime(self, ReleaseTime):
        self._ReleaseTime = ReleaseTime


    def _deserialize(self, params):
        self._VersionName = params.get("VersionName")
        self._VersionDesc = params.get("VersionDesc")
        self._ReleaseTime = params.get("ReleaseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseVersion(AbstractModel):
    """服务发布版本

    """

    def __init__(self):
        r"""
        :param _TotalCount: 发布版本总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _VersionList: 发布版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionList: list of DescribeServiceReleaseVersionResultVersionListInfo
        """
        self._TotalCount = None
        self._VersionList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VersionList(self):
        return self._VersionList

    @VersionList.setter
    def VersionList(self, VersionList):
        self._VersionList = VersionList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VersionList") is not None:
            self._VersionList = []
            for item in params.get("VersionList"):
                obj = DescribeServiceReleaseVersionResultVersionListInfo()
                obj._deserialize(item)
                self._VersionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSubDomainMappings(AbstractModel):
    """服务自定义域名路径映射

    """

    def __init__(self):
        r"""
        :param _IsDefaultMapping: 是否使用默认路径映射，为 True 表示使用默认路径映射；为 False 的话，表示使用自定义路径映射，此时 PathMappingSet 不为空。
        :type IsDefaultMapping: bool
        :param _PathMappingSet: 自定义路径映射列表。
        :type PathMappingSet: list of PathMapping
        """
        self._IsDefaultMapping = None
        self._PathMappingSet = None

    @property
    def IsDefaultMapping(self):
        return self._IsDefaultMapping

    @IsDefaultMapping.setter
    def IsDefaultMapping(self, IsDefaultMapping):
        self._IsDefaultMapping = IsDefaultMapping

    @property
    def PathMappingSet(self):
        return self._PathMappingSet

    @PathMappingSet.setter
    def PathMappingSet(self, PathMappingSet):
        self._PathMappingSet = PathMappingSet


    def _deserialize(self, params):
        self._IsDefaultMapping = params.get("IsDefaultMapping")
        if params.get("PathMappingSet") is not None:
            self._PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self._PathMappingSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceUsagePlanSet(AbstractModel):
    """服务绑定使用计划列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 服务上绑定的使用计划总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ServiceUsagePlanList: 服务上绑定的使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceUsagePlanList: list of ApiUsagePlan
        """
        self._TotalCount = None
        self._ServiceUsagePlanList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServiceUsagePlanList(self):
        return self._ServiceUsagePlanList

    @ServiceUsagePlanList.setter
    def ServiceUsagePlanList(self, ServiceUsagePlanList):
        self._ServiceUsagePlanList = ServiceUsagePlanList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ServiceUsagePlanList") is not None:
            self._ServiceUsagePlanList = []
            for item in params.get("ServiceUsagePlanList"):
                obj = ApiUsagePlan()
                obj._deserialize(item)
                self._ServiceUsagePlanList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicesStatus(AbstractModel):
    """服务列表展示

    """

    def __init__(self):
        r"""
        :param _TotalCount: 服务列表总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _ServiceSet: 服务列表详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceSet: list of Service
        """
        self._TotalCount = None
        self._ServiceSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ServiceSet(self):
        return self._ServiceSet

    @ServiceSet.setter
    def ServiceSet(self, ServiceSet):
        self._ServiceSet = ServiceSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("ServiceSet") is not None:
            self._ServiceSet = []
            for item in params.get("ServiceSet"):
                obj = Service()
                obj._deserialize(item)
                self._ServiceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """API绑定的标签信息。

    """

    def __init__(self):
        r"""
        :param _Key: 标签的 key。
        :type Key: str
        :param _Value: 便签的 value。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetServicesReq(AbstractModel):
    """tsf serverless入参

    """

    def __init__(self):
        r"""
        :param _VmIp: vm ip
        :type VmIp: str
        :param _VpcId: vpc id
        :type VpcId: str
        :param _VmPort: vm port
        :type VmPort: int
        :param _HostIp: cvm所在宿主机ip
        :type HostIp: str
        :param _DockerIp: docker ip
        :type DockerIp: str
        """
        self._VmIp = None
        self._VpcId = None
        self._VmPort = None
        self._HostIp = None
        self._DockerIp = None

    @property
    def VmIp(self):
        return self._VmIp

    @VmIp.setter
    def VmIp(self, VmIp):
        self._VmIp = VmIp

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def VmPort(self):
        return self._VmPort

    @VmPort.setter
    def VmPort(self, VmPort):
        self._VmPort = VmPort

    @property
    def HostIp(self):
        return self._HostIp

    @HostIp.setter
    def HostIp(self, HostIp):
        self._HostIp = HostIp

    @property
    def DockerIp(self):
        return self._DockerIp

    @DockerIp.setter
    def DockerIp(self, DockerIp):
        self._DockerIp = DockerIp


    def _deserialize(self, params):
        self._VmIp = params.get("VmIp")
        self._VpcId = params.get("VpcId")
        self._VmPort = params.get("VmPort")
        self._HostIp = params.get("HostIp")
        self._DockerIp = params.get("DockerIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfLoadBalanceConfResp(AbstractModel):
    """TsfLoadBalanceConf 出参使用

    """

    def __init__(self):
        r"""
        :param _IsLoadBalance: 是否开启负载均衡。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLoadBalance: bool
        :param _Method: 负载均衡方式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _SessionStickRequired: 是否开启会话保持。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionStickRequired: bool
        :param _SessionStickTimeout: 会话保持超时时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionStickTimeout: int
        """
        self._IsLoadBalance = None
        self._Method = None
        self._SessionStickRequired = None
        self._SessionStickTimeout = None

    @property
    def IsLoadBalance(self):
        return self._IsLoadBalance

    @IsLoadBalance.setter
    def IsLoadBalance(self, IsLoadBalance):
        self._IsLoadBalance = IsLoadBalance

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def SessionStickRequired(self):
        return self._SessionStickRequired

    @SessionStickRequired.setter
    def SessionStickRequired(self, SessionStickRequired):
        self._SessionStickRequired = SessionStickRequired

    @property
    def SessionStickTimeout(self):
        return self._SessionStickTimeout

    @SessionStickTimeout.setter
    def SessionStickTimeout(self, SessionStickTimeout):
        self._SessionStickTimeout = SessionStickTimeout


    def _deserialize(self, params):
        self._IsLoadBalance = params.get("IsLoadBalance")
        self._Method = params.get("Method")
        self._SessionStickRequired = params.get("SessionStickRequired")
        self._SessionStickTimeout = params.get("SessionStickTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindEnvironmentRequest(AbstractModel):
    """UnBindEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BindType: 绑定类型，取值为 API、SERVICE，默认值为 SERVICE。
        :type BindType: str
        :param _UsagePlanIds: 待绑定的使用计划唯一 ID 列表。
        :type UsagePlanIds: list of str
        :param _Environment: 待解绑的服务环境。
        :type Environment: str
        :param _ServiceId: 待解绑的服务唯一 ID。
        :type ServiceId: str
        :param _ApiIds: API 唯一 ID 数组，当 BindType=API 时，需要传入此参数。
        :type ApiIds: list of str
        """
        self._BindType = None
        self._UsagePlanIds = None
        self._Environment = None
        self._ServiceId = None
        self._ApiIds = None

    @property
    def BindType(self):
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def UsagePlanIds(self):
        return self._UsagePlanIds

    @UsagePlanIds.setter
    def UsagePlanIds(self, UsagePlanIds):
        self._UsagePlanIds = UsagePlanIds

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._BindType = params.get("BindType")
        self._UsagePlanIds = params.get("UsagePlanIds")
        self._Environment = params.get("Environment")
        self._ServiceId = params.get("ServiceId")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindEnvironmentResponse(AbstractModel):
    """UnBindEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnBindIPStrategyRequest(AbstractModel):
    """UnBindIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待解绑的服务唯一ID。
        :type ServiceId: str
        :param _StrategyId: 待解绑的IP策略唯一ID。
        :type StrategyId: str
        :param _EnvironmentName: 待解绑的环境。
        :type EnvironmentName: str
        :param _UnBindApiIds: 待解绑的 API 列表。
        :type UnBindApiIds: list of str
        """
        self._ServiceId = None
        self._StrategyId = None
        self._EnvironmentName = None
        self._UnBindApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def StrategyId(self):
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def UnBindApiIds(self):
        return self._UnBindApiIds

    @UnBindApiIds.setter
    def UnBindApiIds(self, UnBindApiIds):
        self._UnBindApiIds = UnBindApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._StrategyId = params.get("StrategyId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._UnBindApiIds = params.get("UnBindApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindIPStrategyResponse(AbstractModel):
    """UnBindIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnBindSecretIdsRequest(AbstractModel):
    """UnBindSecretIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 待解绑的使用计划唯一 ID。
        :type UsagePlanId: str
        :param _AccessKeyIds: 待解绑的密钥 ID 数组。
        :type AccessKeyIds: list of str
        """
        self._UsagePlanId = None
        self._AccessKeyIds = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def AccessKeyIds(self):
        return self._AccessKeyIds

    @AccessKeyIds.setter
    def AccessKeyIds(self, AccessKeyIds):
        self._AccessKeyIds = AccessKeyIds


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._AccessKeyIds = params.get("AccessKeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindSecretIdsResponse(AbstractModel):
    """UnBindSecretIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnBindSubDomainRequest(AbstractModel):
    """UnBindSubDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param _SubDomain: 待解绑的自定义的域名。
        :type SubDomain: str
        """
        self._ServiceId = None
        self._SubDomain = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindSubDomainResponse(AbstractModel):
    """UnBindSubDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 解绑自定义域名操作是否成功。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnReleaseServiceRequest(AbstractModel):
    """UnReleaseService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待下线服务的唯一 ID。
        :type ServiceId: str
        :param _EnvironmentName: 待下线的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。
        :type EnvironmentName: str
        :param _ApiIds: 保留字段，待下线的API列表。
        :type ApiIds: list of str
        """
        self._ServiceId = None
        self._EnvironmentName = None
        self._ApiIds = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ApiIds(self):
        return self._ApiIds

    @ApiIds.setter
    def ApiIds(self, ApiIds):
        self._ApiIds = ApiIds


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnReleaseServiceResponse(AbstractModel):
    """UnReleaseService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 下线操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UnbindApiAppRequest(AbstractModel):
    """UnbindApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiAppId: 待绑定的应用唯一 ID 。
        :type ApiAppId: str
        :param _Environment: 待绑定的环境。
        :type Environment: str
        :param _ServiceId: 待绑定的服务唯一 ID。
        :type ServiceId: str
        :param _ApiId: 待绑定的API唯一ID。
        :type ApiId: str
        """
        self._ApiAppId = None
        self._Environment = None
        self._ServiceId = None
        self._ApiId = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._Environment = params.get("Environment")
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindApiAppResponse(AbstractModel):
    """UnbindApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 解除绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpdateApiAppKeyRequest(AbstractModel):
    """UpdateApiAppKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiAppId: 应用唯一 ID。
        :type ApiAppId: str
        :param _ApiAppKey: 应用的Key。
        :type ApiAppKey: str
        :param _ApiAppSecret: 应用的Secret。
        :type ApiAppSecret: str
        """
        self._ApiAppId = None
        self._ApiAppKey = None
        self._ApiAppSecret = None

    @property
    def ApiAppId(self):
        return self._ApiAppId

    @ApiAppId.setter
    def ApiAppId(self, ApiAppId):
        self._ApiAppId = ApiAppId

    @property
    def ApiAppKey(self):
        return self._ApiAppKey

    @ApiAppKey.setter
    def ApiAppKey(self, ApiAppKey):
        self._ApiAppKey = ApiAppKey

    @property
    def ApiAppSecret(self):
        return self._ApiAppSecret

    @ApiAppSecret.setter
    def ApiAppSecret(self, ApiAppSecret):
        self._ApiAppSecret = ApiAppSecret


    def _deserialize(self, params):
        self._ApiAppId = params.get("ApiAppId")
        self._ApiAppKey = params.get("ApiAppKey")
        self._ApiAppSecret = params.get("ApiAppSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiAppKeyResponse(AbstractModel):
    """UpdateApiAppKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 更新操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpdateApiKeyRequest(AbstractModel):
    """UpdateApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 待更换的密钥 ID。
        :type AccessKeyId: str
        :param _AccessKeySecret: 待更换的密钥 Key，更新自定义密钥时，该字段为必传。长度10 - 50字符，包括字母、数字、英文下划线。
        :type AccessKeySecret: str
        """
        self._AccessKeyId = None
        self._AccessKeySecret = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def AccessKeySecret(self):
        return self._AccessKeySecret

    @AccessKeySecret.setter
    def AccessKeySecret(self, AccessKeySecret):
        self._AccessKeySecret = AccessKeySecret


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._AccessKeySecret = params.get("AccessKeySecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiKeyResponse(AbstractModel):
    """UpdateApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 更换后的密钥详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self._Result = ApiKey()
            self._Result._deserialize(params.get("Result"))
        self._RequestId = params.get("RequestId")


class UpdateServiceRequest(AbstractModel):
    """UpdateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceId: 待切换服务的唯一 Id。
        :type ServiceId: str
        :param _EnvironmentName: 待切换的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。
        :type EnvironmentName: str
        :param _VersionName: 切换的版本号。
        :type VersionName: str
        :param _UpdateDesc: 本次的切换描述。
        :type UpdateDesc: str
        """
        self._ServiceId = None
        self._EnvironmentName = None
        self._VersionName = None
        self._UpdateDesc = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def VersionName(self):
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def UpdateDesc(self):
        return self._UpdateDesc

    @UpdateDesc.setter
    def UpdateDesc(self, UpdateDesc):
        self._UpdateDesc = UpdateDesc


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._EnvironmentName = params.get("EnvironmentName")
        self._VersionName = params.get("VersionName")
        self._UpdateDesc = params.get("UpdateDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServiceResponse(AbstractModel):
    """UpdateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 切换版本操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UpstreamHealthChecker(AbstractModel):
    """后端通道健康检查参数配置

    """

    def __init__(self):
        r"""
        :param _EnableActiveCheck: 标识是否开启主动健康检查。
        :type EnableActiveCheck: bool
        :param _EnablePassiveCheck: 标识是否开启被动健康检查。
        :type EnablePassiveCheck: bool
        :param _HealthyHttpStatus: 健康检查时，判断为成功请求的 HTTP 状态码。
        :type HealthyHttpStatus: str
        :param _UnhealthyHttpStatus: 健康检查时，判断为失败请求的 HTTP 状态码。
        :type UnhealthyHttpStatus: str
        :param _TcpFailureThreshold: TCP连续错误阈值。0 表示禁用 TCP 检查。取值范围：[0, 254]。
        :type TcpFailureThreshold: int
        :param _TimeoutThreshold: 连续超时阈值。0 表示禁用超时检查。取值范围：[0, 254]。
        :type TimeoutThreshold: int
        :param _HttpFailureThreshold: HTTP连续错误阈值。0 表示禁用HTTP检查。取值范围：[0, 254]。
        :type HttpFailureThreshold: int
        :param _ActiveCheckHttpPath: 主动健康检查时探测请求的路径。默认为"/"。
        :type ActiveCheckHttpPath: str
        :param _ActiveCheckTimeout: 主动健康检查的探测请求超时，单位秒。默认为5秒。
        :type ActiveCheckTimeout: int
        :param _ActiveCheckInterval: 主动健康检查的时间间隔，默认5秒。
        :type ActiveCheckInterval: int
        :param _ActiveRequestHeader: 主动健康检查时探测请求的的请求头。
        :type ActiveRequestHeader: list of UpstreamHealthCheckerReqHeaders
        :param _UnhealthyTimeout: 异常节点的状态自动恢复时间，单位秒。当只开启被动检查的话，必须设置为 > 0 的值，否则被动异常节点将无法恢复。默认30秒。
        :type UnhealthyTimeout: int
        """
        self._EnableActiveCheck = None
        self._EnablePassiveCheck = None
        self._HealthyHttpStatus = None
        self._UnhealthyHttpStatus = None
        self._TcpFailureThreshold = None
        self._TimeoutThreshold = None
        self._HttpFailureThreshold = None
        self._ActiveCheckHttpPath = None
        self._ActiveCheckTimeout = None
        self._ActiveCheckInterval = None
        self._ActiveRequestHeader = None
        self._UnhealthyTimeout = None

    @property
    def EnableActiveCheck(self):
        return self._EnableActiveCheck

    @EnableActiveCheck.setter
    def EnableActiveCheck(self, EnableActiveCheck):
        self._EnableActiveCheck = EnableActiveCheck

    @property
    def EnablePassiveCheck(self):
        return self._EnablePassiveCheck

    @EnablePassiveCheck.setter
    def EnablePassiveCheck(self, EnablePassiveCheck):
        self._EnablePassiveCheck = EnablePassiveCheck

    @property
    def HealthyHttpStatus(self):
        return self._HealthyHttpStatus

    @HealthyHttpStatus.setter
    def HealthyHttpStatus(self, HealthyHttpStatus):
        self._HealthyHttpStatus = HealthyHttpStatus

    @property
    def UnhealthyHttpStatus(self):
        return self._UnhealthyHttpStatus

    @UnhealthyHttpStatus.setter
    def UnhealthyHttpStatus(self, UnhealthyHttpStatus):
        self._UnhealthyHttpStatus = UnhealthyHttpStatus

    @property
    def TcpFailureThreshold(self):
        return self._TcpFailureThreshold

    @TcpFailureThreshold.setter
    def TcpFailureThreshold(self, TcpFailureThreshold):
        self._TcpFailureThreshold = TcpFailureThreshold

    @property
    def TimeoutThreshold(self):
        return self._TimeoutThreshold

    @TimeoutThreshold.setter
    def TimeoutThreshold(self, TimeoutThreshold):
        self._TimeoutThreshold = TimeoutThreshold

    @property
    def HttpFailureThreshold(self):
        return self._HttpFailureThreshold

    @HttpFailureThreshold.setter
    def HttpFailureThreshold(self, HttpFailureThreshold):
        self._HttpFailureThreshold = HttpFailureThreshold

    @property
    def ActiveCheckHttpPath(self):
        return self._ActiveCheckHttpPath

    @ActiveCheckHttpPath.setter
    def ActiveCheckHttpPath(self, ActiveCheckHttpPath):
        self._ActiveCheckHttpPath = ActiveCheckHttpPath

    @property
    def ActiveCheckTimeout(self):
        return self._ActiveCheckTimeout

    @ActiveCheckTimeout.setter
    def ActiveCheckTimeout(self, ActiveCheckTimeout):
        self._ActiveCheckTimeout = ActiveCheckTimeout

    @property
    def ActiveCheckInterval(self):
        return self._ActiveCheckInterval

    @ActiveCheckInterval.setter
    def ActiveCheckInterval(self, ActiveCheckInterval):
        self._ActiveCheckInterval = ActiveCheckInterval

    @property
    def ActiveRequestHeader(self):
        return self._ActiveRequestHeader

    @ActiveRequestHeader.setter
    def ActiveRequestHeader(self, ActiveRequestHeader):
        self._ActiveRequestHeader = ActiveRequestHeader

    @property
    def UnhealthyTimeout(self):
        return self._UnhealthyTimeout

    @UnhealthyTimeout.setter
    def UnhealthyTimeout(self, UnhealthyTimeout):
        self._UnhealthyTimeout = UnhealthyTimeout


    def _deserialize(self, params):
        self._EnableActiveCheck = params.get("EnableActiveCheck")
        self._EnablePassiveCheck = params.get("EnablePassiveCheck")
        self._HealthyHttpStatus = params.get("HealthyHttpStatus")
        self._UnhealthyHttpStatus = params.get("UnhealthyHttpStatus")
        self._TcpFailureThreshold = params.get("TcpFailureThreshold")
        self._TimeoutThreshold = params.get("TimeoutThreshold")
        self._HttpFailureThreshold = params.get("HttpFailureThreshold")
        self._ActiveCheckHttpPath = params.get("ActiveCheckHttpPath")
        self._ActiveCheckTimeout = params.get("ActiveCheckTimeout")
        self._ActiveCheckInterval = params.get("ActiveCheckInterval")
        if params.get("ActiveRequestHeader") is not None:
            self._ActiveRequestHeader = []
            for item in params.get("ActiveRequestHeader"):
                obj = UpstreamHealthCheckerReqHeaders()
                obj._deserialize(item)
                self._ActiveRequestHeader.append(obj)
        self._UnhealthyTimeout = params.get("UnhealthyTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamHealthCheckerReqHeaders(AbstractModel):
    """后端通道主动健康检查的请求头配置

    """


class UpstreamInfo(AbstractModel):
    """后端通道详细信息

    """

    def __init__(self):
        r"""
        :param _UpstreamId: 后端通道唯一ID
        :type UpstreamId: str
        :param _UpstreamName: 后端通道名字
        :type UpstreamName: str
        :param _UpstreamDescription: 后端通道描述
        :type UpstreamDescription: str
        :param _Scheme: 后端协议，取值范围：HTTP, HTTPS
        :type Scheme: str
        :param _Algorithm: 负载均衡算法，取值范围：ROUND_ROBIN
        :type Algorithm: str
        :param _UniqVpcId: VPC唯一ID
        :type UniqVpcId: str
        :param _Retries: 请求重试次数
        :type Retries: int
        :param _Nodes: 后端节点
        :type Nodes: list of UpstreamNode
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param _HealthChecker: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param _UpstreamType: 后端的类型，取值范围：IP_PORT, K8S
        :type UpstreamType: str
        :param _K8sServices: K8S容器服务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type K8sServices: list of K8sService
        :param _UpstreamHost: 网关转发给后端的Host请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHost: str
        """
        self._UpstreamId = None
        self._UpstreamName = None
        self._UpstreamDescription = None
        self._Scheme = None
        self._Algorithm = None
        self._UniqVpcId = None
        self._Retries = None
        self._Nodes = None
        self._CreatedTime = None
        self._Tags = None
        self._HealthChecker = None
        self._UpstreamType = None
        self._K8sServices = None
        self._UpstreamHost = None

    @property
    def UpstreamId(self):
        return self._UpstreamId

    @UpstreamId.setter
    def UpstreamId(self, UpstreamId):
        self._UpstreamId = UpstreamId

    @property
    def UpstreamName(self):
        return self._UpstreamName

    @UpstreamName.setter
    def UpstreamName(self, UpstreamName):
        self._UpstreamName = UpstreamName

    @property
    def UpstreamDescription(self):
        return self._UpstreamDescription

    @UpstreamDescription.setter
    def UpstreamDescription(self, UpstreamDescription):
        self._UpstreamDescription = UpstreamDescription

    @property
    def Scheme(self):
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Retries(self):
        return self._Retries

    @Retries.setter
    def Retries(self, Retries):
        self._Retries = Retries

    @property
    def Nodes(self):
        return self._Nodes

    @Nodes.setter
    def Nodes(self, Nodes):
        self._Nodes = Nodes

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def HealthChecker(self):
        return self._HealthChecker

    @HealthChecker.setter
    def HealthChecker(self, HealthChecker):
        self._HealthChecker = HealthChecker

    @property
    def UpstreamType(self):
        return self._UpstreamType

    @UpstreamType.setter
    def UpstreamType(self, UpstreamType):
        self._UpstreamType = UpstreamType

    @property
    def K8sServices(self):
        return self._K8sServices

    @K8sServices.setter
    def K8sServices(self, K8sServices):
        self._K8sServices = K8sServices

    @property
    def UpstreamHost(self):
        return self._UpstreamHost

    @UpstreamHost.setter
    def UpstreamHost(self, UpstreamHost):
        self._UpstreamHost = UpstreamHost


    def _deserialize(self, params):
        self._UpstreamId = params.get("UpstreamId")
        self._UpstreamName = params.get("UpstreamName")
        self._UpstreamDescription = params.get("UpstreamDescription")
        self._Scheme = params.get("Scheme")
        self._Algorithm = params.get("Algorithm")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Retries = params.get("Retries")
        if params.get("Nodes") is not None:
            self._Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self._Nodes.append(obj)
        self._CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("HealthChecker") is not None:
            self._HealthChecker = UpstreamHealthChecker()
            self._HealthChecker._deserialize(params.get("HealthChecker"))
        self._UpstreamType = params.get("UpstreamType")
        if params.get("K8sServices") is not None:
            self._K8sServices = []
            for item in params.get("K8sServices"):
                obj = K8sService()
                obj._deserialize(item)
                self._K8sServices.append(obj)
        self._UpstreamHost = params.get("UpstreamHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamNode(AbstractModel):
    """后端通道后端节点元数据

    """

    def __init__(self):
        r"""
        :param _Host: IP或域名
        :type Host: str
        :param _Port: 端口[0, 65535]
        :type Port: int
        :param _Weight: 权重[0, 100], 0为禁用
        :type Weight: int
        :param _VmInstanceId: CVM实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VmInstanceId: str
        :param _Tags: 染色标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param _Healthy: 节点健康状态，创建、编辑时不需要传该参数。OFF：关闭，HEALTHY：健康，UNHEALTHY：异常，NO_DATA：数据未上报。目前只支持VPC通道。
注意：此字段可能返回 null，表示取不到有效值。
        :type Healthy: str
        :param _ServiceName: K8S容器服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param _NameSpace: K8S命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NameSpace: str
        :param _ClusterId: TKE集群的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param _Source: Node的来源，取值范围：K8S
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param _UniqueServiceName: API网关内部记录唯一的服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqueServiceName: str
        """
        self._Host = None
        self._Port = None
        self._Weight = None
        self._VmInstanceId = None
        self._Tags = None
        self._Healthy = None
        self._ServiceName = None
        self._NameSpace = None
        self._ClusterId = None
        self._Source = None
        self._UniqueServiceName = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def VmInstanceId(self):
        return self._VmInstanceId

    @VmInstanceId.setter
    def VmInstanceId(self, VmInstanceId):
        self._VmInstanceId = VmInstanceId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Healthy(self):
        return self._Healthy

    @Healthy.setter
    def Healthy(self, Healthy):
        self._Healthy = Healthy

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def NameSpace(self):
        return self._NameSpace

    @NameSpace.setter
    def NameSpace(self, NameSpace):
        self._NameSpace = NameSpace

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def Source(self):
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def UniqueServiceName(self):
        return self._UniqueServiceName

    @UniqueServiceName.setter
    def UniqueServiceName(self, UniqueServiceName):
        self._UniqueServiceName = UniqueServiceName


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        self._VmInstanceId = params.get("VmInstanceId")
        self._Tags = params.get("Tags")
        self._Healthy = params.get("Healthy")
        self._ServiceName = params.get("ServiceName")
        self._NameSpace = params.get("NameSpace")
        self._ClusterId = params.get("ClusterId")
        self._Source = params.get("Source")
        self._UniqueServiceName = params.get("UniqueServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlan(AbstractModel):
    """usagePlan详情

    """

    def __init__(self):
        r"""
        :param _Environment: 环境名称。
        :type Environment: str
        :param _UsagePlanId: 使用计划唯一ID。
        :type UsagePlanId: str
        :param _UsagePlanName: 使用计划名称。
        :type UsagePlanName: str
        :param _UsagePlanDesc: 使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param _MaxRequestNumPreSec: 使用计划qps，-1表示没有限制。
        :type MaxRequestNumPreSec: int
        :param _CreatedTime: 使用计划时间。
        :type CreatedTime: str
        :param _ModifiedTime: 使用计划修改时间。
        :type ModifiedTime: str
        """
        self._Environment = None
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNumPreSec = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._Environment = params.get("Environment")
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindEnvironment(AbstractModel):
    """使用计划绑定环境信息

    """

    def __init__(self):
        r"""
        :param _EnvironmentName: 环境名。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param _ServiceId: 服务唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        """
        self._EnvironmentName = None
        self._ServiceId = None

    @property
    def EnvironmentName(self):
        return self._EnvironmentName

    @EnvironmentName.setter
    def EnvironmentName(self, EnvironmentName):
        self._EnvironmentName = EnvironmentName

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId


    def _deserialize(self, params):
        self._EnvironmentName = params.get("EnvironmentName")
        self._ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindSecret(AbstractModel):
    """使用计划绑定密钥

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 密钥ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKeyId: str
        :param _SecretName: 密钥名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param _Status: 密钥状态，0表示已禁用，1表示启用中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self._AccessKeyId = None
        self._SecretName = None
        self._Status = None

    @property
    def AccessKeyId(self):
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._SecretName = params.get("SecretName")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindSecretStatus(AbstractModel):
    """使用计划绑定密钥列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 使用计划绑定密钥的数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _AccessKeyList: 密钥详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKeyList: list of UsagePlanBindSecret
        """
        self._TotalCount = None
        self._AccessKeyList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccessKeyList(self):
        return self._AccessKeyList

    @AccessKeyList.setter
    def AccessKeyList(self, AccessKeyList):
        self._AccessKeyList = AccessKeyList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccessKeyList") is not None:
            self._AccessKeyList = []
            for item in params.get("AccessKeyList"):
                obj = UsagePlanBindSecret()
                obj._deserialize(item)
                self._AccessKeyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanEnvironment(AbstractModel):
    """使用计划绑定环境详情。

    """

    def __init__(self):
        r"""
        :param _ServiceId: 绑定的服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param _ApiId: API 的唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param _ApiName: API 的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param _Path: API 的路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Method: API 的方法。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param _Environment: 已经绑定的环境名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Environment: str
        :param _InUseRequestNum: 已经使用的配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type InUseRequestNum: int
        :param _MaxRequestNum: 最大请求量。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param _MaxRequestNumPreSec: 每秒最大请求次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        """
        self._ServiceId = None
        self._ApiId = None
        self._ApiName = None
        self._Path = None
        self._Method = None
        self._Environment = None
        self._InUseRequestNum = None
        self._MaxRequestNum = None
        self._MaxRequestNumPreSec = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._ServiceName = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ApiId(self):
        return self._ApiId

    @ApiId.setter
    def ApiId(self, ApiId):
        self._ApiId = ApiId

    @property
    def ApiName(self):
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def Path(self):
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Method(self):
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Environment(self):
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def InUseRequestNum(self):
        return self._InUseRequestNum

    @InUseRequestNum.setter
    def InUseRequestNum(self, InUseRequestNum):
        self._InUseRequestNum = InUseRequestNum

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ApiId = params.get("ApiId")
        self._ApiName = params.get("ApiName")
        self._Path = params.get("Path")
        self._Method = params.get("Method")
        self._Environment = params.get("Environment")
        self._InUseRequestNum = params.get("InUseRequestNum")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanEnvironmentStatus(AbstractModel):
    """使用计划绑定环境的列表。

    """

    def __init__(self):
        r"""
        :param _TotalCount: 使用计划绑定的服务的环境数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _EnvironmentList: 使用计划已经绑定的各个服务的环境状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentList: list of UsagePlanEnvironment
        """
        self._TotalCount = None
        self._EnvironmentList = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def EnvironmentList(self):
        return self._EnvironmentList

    @EnvironmentList.setter
    def EnvironmentList(self, EnvironmentList):
        self._EnvironmentList = EnvironmentList


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self._EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = UsagePlanEnvironment()
                obj._deserialize(item)
                self._EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanInfo(AbstractModel):
    """使用计划详情。

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 使用计划唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanId: str
        :param _UsagePlanName: 使用计划名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanName: str
        :param _UsagePlanDesc: 使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param _MaxRequestNumPreSec: 每秒请求限制数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param _MaxRequestNum: 最大调用次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _BindSecretIdTotalCount: 绑定密钥的数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindSecretIdTotalCount: int
        :param _BindSecretIds: 绑定密钥的详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindSecretIds: list of str
        :param _BindEnvironmentTotalCount: 绑定环境数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindEnvironmentTotalCount: int
        :param _BindEnvironments: 绑定环境详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindEnvironments: list of UsagePlanBindEnvironment
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNumPreSec = None
        self._MaxRequestNum = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._BindSecretIdTotalCount = None
        self._BindSecretIds = None
        self._BindEnvironmentTotalCount = None
        self._BindEnvironments = None
        self._Tags = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def BindSecretIdTotalCount(self):
        return self._BindSecretIdTotalCount

    @BindSecretIdTotalCount.setter
    def BindSecretIdTotalCount(self, BindSecretIdTotalCount):
        self._BindSecretIdTotalCount = BindSecretIdTotalCount

    @property
    def BindSecretIds(self):
        return self._BindSecretIds

    @BindSecretIds.setter
    def BindSecretIds(self, BindSecretIds):
        self._BindSecretIds = BindSecretIds

    @property
    def BindEnvironmentTotalCount(self):
        return self._BindEnvironmentTotalCount

    @BindEnvironmentTotalCount.setter
    def BindEnvironmentTotalCount(self, BindEnvironmentTotalCount):
        self._BindEnvironmentTotalCount = BindEnvironmentTotalCount

    @property
    def BindEnvironments(self):
        return self._BindEnvironments

    @BindEnvironments.setter
    def BindEnvironments(self, BindEnvironments):
        self._BindEnvironments = BindEnvironments

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        self._BindSecretIdTotalCount = params.get("BindSecretIdTotalCount")
        self._BindSecretIds = params.get("BindSecretIds")
        self._BindEnvironmentTotalCount = params.get("BindEnvironmentTotalCount")
        if params.get("BindEnvironments") is not None:
            self._BindEnvironments = []
            for item in params.get("BindEnvironments"):
                obj = UsagePlanBindEnvironment()
                obj._deserialize(item)
                self._BindEnvironments.append(obj)
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
        


class UsagePlanStatusInfo(AbstractModel):
    """用于使用计划列表展示

    """

    def __init__(self):
        r"""
        :param _UsagePlanId: 使用计划唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanId: str
        :param _UsagePlanName: 用户自定义的使用计划名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanName: str
        :param _UsagePlanDesc: 用户自定义的使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param _MaxRequestNumPreSec: 每秒最大请求次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param _MaxRequestNum: 请求配额总量，-1表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param _CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._UsagePlanId = None
        self._UsagePlanName = None
        self._UsagePlanDesc = None
        self._MaxRequestNumPreSec = None
        self._MaxRequestNum = None
        self._CreatedTime = None
        self._ModifiedTime = None
        self._Tags = None

    @property
    def UsagePlanId(self):
        return self._UsagePlanId

    @UsagePlanId.setter
    def UsagePlanId(self, UsagePlanId):
        self._UsagePlanId = UsagePlanId

    @property
    def UsagePlanName(self):
        return self._UsagePlanName

    @UsagePlanName.setter
    def UsagePlanName(self, UsagePlanName):
        self._UsagePlanName = UsagePlanName

    @property
    def UsagePlanDesc(self):
        return self._UsagePlanDesc

    @UsagePlanDesc.setter
    def UsagePlanDesc(self, UsagePlanDesc):
        self._UsagePlanDesc = UsagePlanDesc

    @property
    def MaxRequestNumPreSec(self):
        return self._MaxRequestNumPreSec

    @MaxRequestNumPreSec.setter
    def MaxRequestNumPreSec(self, MaxRequestNumPreSec):
        self._MaxRequestNumPreSec = MaxRequestNumPreSec

    @property
    def MaxRequestNum(self):
        return self._MaxRequestNum

    @MaxRequestNum.setter
    def MaxRequestNum(self, MaxRequestNum):
        self._MaxRequestNum = MaxRequestNum

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._UsagePlanId = params.get("UsagePlanId")
        self._UsagePlanName = params.get("UsagePlanName")
        self._UsagePlanDesc = params.get("UsagePlanDesc")
        self._MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self._MaxRequestNum = params.get("MaxRequestNum")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
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
        


class UsagePlansStatus(AbstractModel):
    """使用计划列表

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的使用计划数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _UsagePlanStatusSet: 使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanStatusSet: list of UsagePlanStatusInfo
        """
        self._TotalCount = None
        self._UsagePlanStatusSet = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def UsagePlanStatusSet(self):
        return self._UsagePlanStatusSet

    @UsagePlanStatusSet.setter
    def UsagePlanStatusSet(self, UsagePlanStatusSet):
        self._UsagePlanStatusSet = UsagePlanStatusSet


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("UsagePlanStatusSet") is not None:
            self._UsagePlanStatusSet = []
            for item in params.get("UsagePlanStatusSet"):
                obj = UsagePlanStatusInfo()
                obj._deserialize(item)
                self._UsagePlanStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcConfig(AbstractModel):
    """独享实例vpc配置信息

    """

    def __init__(self):
        r"""
        :param _UniqVpcId: vpcid
        :type UniqVpcId: str
        :param _UniqSubnetId: subnetid
        :type UniqSubnetId: str
        """
        self._UniqVpcId = None
        self._UniqSubnetId = None

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def UniqSubnetId(self):
        return self._UniqSubnetId

    @UniqSubnetId.setter
    def UniqSubnetId(self, UniqSubnetId):
        self._UniqSubnetId = UniqSubnetId


    def _deserialize(self, params):
        self._UniqVpcId = params.get("UniqVpcId")
        self._UniqSubnetId = params.get("UniqSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        