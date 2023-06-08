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
        :param ApiDocId: API文档ID
        :type ApiDocId: str
        :param ApiDocName: API文档名称
        :type ApiDocName: str
        :param ApiDocStatus: API文档构建状态
        :type ApiDocStatus: str
        """
        self.ApiDocId = None
        self.ApiDocName = None
        self.ApiDocStatus = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        self.ApiDocName = params.get("ApiDocName")
        self.ApiDocStatus = params.get("ApiDocStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class APIDocInfo(AbstractModel):
    """API文档详细信息

    """

    def __init__(self):
        r"""
        :param ApiDocId: API文档ID
        :type ApiDocId: str
        :param ApiDocName: API文档名称
        :type ApiDocName: str
        :param ApiDocStatus: API文档构建状态
        :type ApiDocStatus: str
        :param ApiCount: API文档API数量
        :type ApiCount: int
        :param ViewCount: API文档查看次数
        :type ViewCount: int
        :param ReleaseCount: API文档发布次数
        :type ReleaseCount: int
        :param ApiDocUri: API文档访问URI
        :type ApiDocUri: str
        :param SharePassword: API文档分享密码
        :type SharePassword: str
        :param UpdatedTime: API文档更新时间
        :type UpdatedTime: str
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param Environment: 环境信息
        :type Environment: str
        :param ApiIds: 生成API文档的API ID
        :type ApiIds: list of str
        :param ServiceName: 服务名称
        :type ServiceName: str
        :param ApiNames: 生成API文档的API名称
        :type ApiNames: list of str
        """
        self.ApiDocId = None
        self.ApiDocName = None
        self.ApiDocStatus = None
        self.ApiCount = None
        self.ViewCount = None
        self.ReleaseCount = None
        self.ApiDocUri = None
        self.SharePassword = None
        self.UpdatedTime = None
        self.ServiceId = None
        self.Environment = None
        self.ApiIds = None
        self.ServiceName = None
        self.ApiNames = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        self.ApiDocName = params.get("ApiDocName")
        self.ApiDocStatus = params.get("ApiDocStatus")
        self.ApiCount = params.get("ApiCount")
        self.ViewCount = params.get("ViewCount")
        self.ReleaseCount = params.get("ReleaseCount")
        self.ApiDocUri = params.get("ApiDocUri")
        self.SharePassword = params.get("SharePassword")
        self.UpdatedTime = params.get("UpdatedTime")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")
        self.ApiIds = params.get("ApiIds")
        self.ServiceName = params.get("ServiceName")
        self.ApiNames = params.get("ApiNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class APIDocs(AbstractModel):
    """API文档列表

    """

    def __init__(self):
        r"""
        :param TotalCount: API文档数量
        :type TotalCount: int
        :param APIDocSet: API文档基本信息
        :type APIDocSet: list of APIDoc
        """
        self.TotalCount = None
        self.APIDocSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("APIDocSet") is not None:
            self.APIDocSet = []
            for item in params.get("APIDocSet"):
                obj = APIDoc()
                obj._deserialize(item)
                self.APIDocSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppApiInfo(AbstractModel):
    """应用绑定的Api信息

    """

    def __init__(self):
        r"""
        :param ApiAppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppName: str
        :param ApiAppId: 应用ID
        :type ApiAppId: str
        :param ApiId: Api的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param ApiName: Api名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param ServiceId: 服务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param AuthorizedTime: 授权绑定时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizedTime: str
        :param ApiRegion: Api所属地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiRegion: str
        :param EnvironmentName: 授权绑定的环境
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        """
        self.ApiAppName = None
        self.ApiAppId = None
        self.ApiId = None
        self.ApiName = None
        self.ServiceId = None
        self.AuthorizedTime = None
        self.ApiRegion = None
        self.EnvironmentName = None


    def _deserialize(self, params):
        self.ApiAppName = params.get("ApiAppName")
        self.ApiAppId = params.get("ApiAppId")
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ServiceId = params.get("ServiceId")
        self.AuthorizedTime = params.get("AuthorizedTime")
        self.ApiRegion = params.get("ApiRegion")
        self.EnvironmentName = params.get("EnvironmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppApiInfos(AbstractModel):
    """应用信息集

    """

    def __init__(self):
        r"""
        :param TotalCount: 数量
        :type TotalCount: int
        :param ApiAppApiSet: 应用绑定的Api信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppApiSet: list of ApiAppApiInfo
        """
        self.TotalCount = None
        self.ApiAppApiSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiAppApiSet") is not None:
            self.ApiAppApiSet = []
            for item in params.get("ApiAppApiSet"):
                obj = ApiAppApiInfo()
                obj._deserialize(item)
                self.ApiAppApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppInfo(AbstractModel):
    """应用信息

    """

    def __init__(self):
        r"""
        :param ApiAppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppName: str
        :param ApiAppId: 应用ID
        :type ApiAppId: str
        :param ApiAppSecret: 应用SECRET
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppSecret: str
        :param ApiAppDesc: 应用描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppDesc: str
        :param CreatedTime: 创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 修改时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param ApiAppKey: 应用KEY
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppKey: str
        """
        self.ApiAppName = None
        self.ApiAppId = None
        self.ApiAppSecret = None
        self.ApiAppDesc = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiAppKey = None


    def _deserialize(self, params):
        self.ApiAppName = params.get("ApiAppName")
        self.ApiAppId = params.get("ApiAppId")
        self.ApiAppSecret = params.get("ApiAppSecret")
        self.ApiAppDesc = params.get("ApiAppDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiAppKey = params.get("ApiAppKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiAppInfos(AbstractModel):
    """应用信息集

    """

    def __init__(self):
        r"""
        :param TotalCount: 应用数量
        :type TotalCount: int
        :param ApiAppSet: 应用信息数组
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiAppSet: list of ApiAppInfo
        """
        self.TotalCount = None
        self.ApiAppSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiAppSet") is not None:
            self.ApiAppSet = []
            for item in params.get("ApiAppSet"):
                obj = ApiAppInfo()
                obj._deserialize(item)
                self.ApiAppSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiEnvironmentStrategy(AbstractModel):
    """api环境绑定策略

    """

    def __init__(self):
        r"""
        :param ApiId: API唯一ID。
        :type ApiId: str
        :param ApiName: 用户自定义API名称。
        :type ApiName: str
        :param Path: API的路径。如/path。
        :type Path: str
        :param Method: API的方法。如GET。
        :type Method: str
        :param EnvironmentStrategySet: 环境的限流信息。
        :type EnvironmentStrategySet: list of EnvironmentStrategy
        """
        self.ApiId = None
        self.ApiName = None
        self.Path = None
        self.Method = None
        self.EnvironmentStrategySet = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        if params.get("EnvironmentStrategySet") is not None:
            self.EnvironmentStrategySet = []
            for item in params.get("EnvironmentStrategySet"):
                obj = EnvironmentStrategy()
                obj._deserialize(item)
                self.EnvironmentStrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiEnvironmentStrategyStataus(AbstractModel):
    """API绑定策略列表

    """

    def __init__(self):
        r"""
        :param TotalCount: API绑定的限流策略数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ApiEnvironmentStrategySet: API绑定的限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiEnvironmentStrategySet: list of ApiEnvironmentStrategy
        """
        self.TotalCount = None
        self.ApiEnvironmentStrategySet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiEnvironmentStrategySet") is not None:
            self.ApiEnvironmentStrategySet = []
            for item in params.get("ApiEnvironmentStrategySet"):
                obj = ApiEnvironmentStrategy()
                obj._deserialize(item)
                self.ApiEnvironmentStrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiIdStatus(AbstractModel):
    """API状态

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param ApiId: API唯一ID。
        :type ApiId: str
        :param ApiDesc: API描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param Path: API PATH。
        :type Path: str
        :param Method: API METHOD。
        :type Method: str
        :param CreatedTime: 服务创建时间。
        :type CreatedTime: str
        :param ModifiedTime: 服务修改时间。
        :type ModifiedTime: str
        :param ApiName: API名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param UniqVpcId: VPC唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param ApiType: API类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param Protocol: API协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param IsDebugAfterCharge: 是否买后调试。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDebugAfterCharge: bool
        :param AuthType: 授权类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param ApiBusinessType: API业务类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiBusinessType: str
        :param AuthRelationApiId: 关联授权API唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthRelationApiId: str
        :param RelationBuniessApiIds: 授权API关联的业务API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationBuniessApiIds: list of str
        :param OauthConfig: oauth配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param TokenLocation: oauth2.0API请求，token存放位置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TokenLocation: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiDesc = None
        self.Path = None
        self.Method = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiName = None
        self.UniqVpcId = None
        self.ApiType = None
        self.Protocol = None
        self.IsDebugAfterCharge = None
        self.AuthType = None
        self.ApiBusinessType = None
        self.AuthRelationApiId = None
        self.RelationBuniessApiIds = None
        self.OauthConfig = None
        self.TokenLocation = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiDesc = params.get("ApiDesc")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiName = params.get("ApiName")
        self.UniqVpcId = params.get("UniqVpcId")
        self.ApiType = params.get("ApiType")
        self.Protocol = params.get("Protocol")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self.AuthType = params.get("AuthType")
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        self.RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        self.TokenLocation = params.get("TokenLocation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfo(AbstractModel):
    """展示api信息

    """

    def __init__(self):
        r"""
        :param ServiceId: API 所在的服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param ServiceName: API 所在的服务的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param ServiceDesc: API 所在的服务的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param ApiId: API 接口唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param ApiDesc: API 接口的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param CreatedTime: 创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 最后修改时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param ApiName: API 接口的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param ApiType: API 类型。可取值为NORMAL（普通API）、TSF（微服务API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param Protocol: API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param AuthType: API 鉴权类型。可取值为 SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param ApiBusinessType: OAUTH API的类型。可取值为NORMAL（业务API）、OAUTH（授权API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiBusinessType: str
        :param AuthRelationApiId: OAUTH 业务API 关联的授权API 唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthRelationApiId: str
        :param OauthConfig: OAUTH配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param IsDebugAfterCharge: 是否购买后调试（云市场预留参数）。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDebugAfterCharge: bool
        :param RequestConfig: 请求的前端配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param ResponseType: 返回类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseType: str
        :param ResponseSuccessExample: 自定义响应配置成功响应示例。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseSuccessExample: str
        :param ResponseFailExample: 自定义响应配置失败响应示例。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseFailExample: str
        :param ResponseErrorCodes: 用户自定义错误码配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseErrorCodes: list of ErrorCodes
        :param RequestParameters: 前端请求参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestParameters: list of ReqParameter
        :param ServiceTimeout: API 的后端服务超时时间，单位是秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTimeout: int
        :param ServiceType: API 的后端服务类型。可取值为 HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param ServiceConfig: API 的后端服务配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param ServiceParameters: API的后端服务参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceParameters: list of DescribeApiResultServiceParametersInfo
        :param ConstantParameters: 常量参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConstantParameters: list of ConstantParameter
        :param ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceMockReturnMessage: str
        :param ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfFunctionName: str
        :param ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: 是否开启集成响应。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceScfIsIntegratedResponse: bool
        :param ServiceWebsocketRegisterFunctionName: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param InternalDomain: WEBSOCKET 回推地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type InternalDomain: str
        :param ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param MicroServices: API绑定微服务服务列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroServices: list of MicroService
        :param MicroServicesInfo: 微服务信息详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type MicroServicesInfo: list of int
        :param ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: 微服务的健康检查配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param EnableCORS: 是否开启跨域。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnableCORS: bool
        :param Tags: API绑定的tag信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param Environments: API已发布的环境信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Environments: list of str
        :param IsBase64Encoded: 是否开启Base64编码，只有后端为scf时才会生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBase64Encoded: bool
        :param IsBase64Trigger: 是否开启Base64编码的header触发，只有后端为scf时才会生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsBase64Trigger: bool
        :param Base64EncodedTriggerRules: Header触发规则，总规则数量不超过10。
注意：此字段可能返回 null，表示取不到有效值。
        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule
        """
        self.ServiceId = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.ApiId = None
        self.ApiDesc = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiName = None
        self.ApiType = None
        self.Protocol = None
        self.AuthType = None
        self.ApiBusinessType = None
        self.AuthRelationApiId = None
        self.OauthConfig = None
        self.IsDebugAfterCharge = None
        self.RequestConfig = None
        self.ResponseType = None
        self.ResponseSuccessExample = None
        self.ResponseFailExample = None
        self.ResponseErrorCodes = None
        self.RequestParameters = None
        self.ServiceTimeout = None
        self.ServiceType = None
        self.ServiceConfig = None
        self.ServiceParameters = None
        self.ConstantParameters = None
        self.ServiceMockReturnMessage = None
        self.ServiceScfFunctionName = None
        self.ServiceScfFunctionNamespace = None
        self.ServiceScfFunctionQualifier = None
        self.ServiceScfIsIntegratedResponse = None
        self.ServiceWebsocketRegisterFunctionName = None
        self.ServiceWebsocketRegisterFunctionNamespace = None
        self.ServiceWebsocketRegisterFunctionQualifier = None
        self.ServiceWebsocketCleanupFunctionName = None
        self.ServiceWebsocketCleanupFunctionNamespace = None
        self.ServiceWebsocketCleanupFunctionQualifier = None
        self.InternalDomain = None
        self.ServiceWebsocketTransportFunctionName = None
        self.ServiceWebsocketTransportFunctionNamespace = None
        self.ServiceWebsocketTransportFunctionQualifier = None
        self.MicroServices = None
        self.MicroServicesInfo = None
        self.ServiceTsfLoadBalanceConf = None
        self.ServiceTsfHealthCheckConf = None
        self.EnableCORS = None
        self.Tags = None
        self.Environments = None
        self.IsBase64Encoded = None
        self.IsBase64Trigger = None
        self.Base64EncodedTriggerRules = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.ApiId = params.get("ApiId")
        self.ApiDesc = params.get("ApiDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiName = params.get("ApiName")
        self.ApiType = params.get("ApiType")
        self.Protocol = params.get("Protocol")
        self.AuthType = params.get("AuthType")
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        if params.get("RequestConfig") is not None:
            self.RequestConfig = RequestConfig()
            self.RequestConfig._deserialize(params.get("RequestConfig"))
        self.ResponseType = params.get("ResponseType")
        self.ResponseSuccessExample = params.get("ResponseSuccessExample")
        self.ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ResponseErrorCodes") is not None:
            self.ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ErrorCodes()
                obj._deserialize(item)
                self.ResponseErrorCodes.append(obj)
        if params.get("RequestParameters") is not None:
            self.RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = ReqParameter()
                obj._deserialize(item)
                self.RequestParameters.append(obj)
        self.ServiceTimeout = params.get("ServiceTimeout")
        self.ServiceType = params.get("ServiceType")
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = ServiceConfig()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        if params.get("ServiceParameters") is not None:
            self.ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = DescribeApiResultServiceParametersInfo()
                obj._deserialize(item)
                self.ServiceParameters.append(obj)
        if params.get("ConstantParameters") is not None:
            self.ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self.ConstantParameters.append(obj)
        self.ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        self.ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self.ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self.ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self.ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self.ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self.ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self.ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self.ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self.ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self.ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self.InternalDomain = params.get("InternalDomain")
        self.ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self.ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self.ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        if params.get("MicroServices") is not None:
            self.MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroService()
                obj._deserialize(item)
                self.MicroServices.append(obj)
        self.MicroServicesInfo = params.get("MicroServicesInfo")
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self.ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self.ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self.ServiceTsfHealthCheckConf = HealthCheckConf()
            self.ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        self.EnableCORS = params.get("EnableCORS")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Environments = params.get("Environments")
        self.IsBase64Encoded = params.get("IsBase64Encoded")
        self.IsBase64Trigger = params.get("IsBase64Trigger")
        if params.get("Base64EncodedTriggerRules") is not None:
            self.Base64EncodedTriggerRules = []
            for item in params.get("Base64EncodedTriggerRules"):
                obj = Base64EncodedTriggerRule()
                obj._deserialize(item)
                self.Base64EncodedTriggerRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiInfoSummary(AbstractModel):
    """插件相关的API列表信息。

    """

    def __init__(self):
        r"""
        :param TotalCount: 插件相关的API总数。
        :type TotalCount: int
        :param ApiSet: 插件相关的API信息。
        :type ApiSet: list of AvailableApiInfo
        """
        self.TotalCount = None
        self.ApiSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiSet") is not None:
            self.ApiSet = []
            for item in params.get("ApiSet"):
                obj = AvailableApiInfo()
                obj._deserialize(item)
                self.ApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiKey(AbstractModel):
    """密钥详情

    """

    def __init__(self):
        r"""
        :param AccessKeyId: 创建的 API 密钥 ID 。
        :type AccessKeyId: str
        :param AccessKeySecret: 创建的 API 密钥 Key。
        :type AccessKeySecret: str
        :param AccessKeyType: 密钥类型，auto 或者 manual。
        :type AccessKeyType: str
        :param SecretName: 用户自定义密钥名称。
        :type SecretName: str
        :param ModifiedTime: 最后一次修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type ModifiedTime: str
        :param Status: 密钥状态。0表示禁用，1表示启用。
        :type Status: int
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type CreatedTime: str
        """
        self.AccessKeyId = None
        self.AccessKeySecret = None
        self.AccessKeyType = None
        self.SecretName = None
        self.ModifiedTime = None
        self.Status = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.AccessKeySecret = params.get("AccessKeySecret")
        self.AccessKeyType = params.get("AccessKeyType")
        self.SecretName = params.get("SecretName")
        self.ModifiedTime = params.get("ModifiedTime")
        self.Status = params.get("Status")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiKeysStatus(AbstractModel):
    """密钥列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的 API 密钥数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ApiKeySet: API 密钥列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiKeySet: list of ApiKey
        """
        self.TotalCount = None
        self.ApiKeySet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiKeySet") is not None:
            self.ApiKeySet = []
            for item in params.get("ApiKeySet"):
                obj = ApiKey()
                obj._deserialize(item)
                self.ApiKeySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiRequestConfig(AbstractModel):
    """api请求配置

    """

    def __init__(self):
        r"""
        :param Path: path
        :type Path: str
        :param Method: 方法
        :type Method: str
        """
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiUsagePlan(AbstractModel):
    """api或service绑定使用计划详情

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param ApiId: API 唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param ApiName: API 名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param Path: API 路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Method: API 方法。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param UsagePlanId: 使用计划的唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanId: str
        :param UsagePlanName: 使用计划的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanName: str
        :param UsagePlanDesc: 使用计划的描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param Environment: 使用计划绑定的服务环境。
注意：此字段可能返回 null，表示取不到有效值。
        :type Environment: str
        :param InUseRequestNum: 已经使用的配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type InUseRequestNum: int
        :param MaxRequestNum: 请求配额总量，-1表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: 请求 QPS 上限，-1 表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param CreatedTime: 使用计划创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 使用计划最后修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiName = None
        self.Path = None
        self.Method = None
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.Environment = None
        self.InUseRequestNum = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.Environment = params.get("Environment")
        self.InUseRequestNum = params.get("InUseRequestNum")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApiUsagePlanSet(AbstractModel):
    """api绑定使用计划列表

    """

    def __init__(self):
        r"""
        :param TotalCount: API 绑定的使用计划总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ApiUsagePlanList: API 绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiUsagePlanList: list of ApiUsagePlan
        """
        self.TotalCount = None
        self.ApiUsagePlanList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiUsagePlanList") is not None:
            self.ApiUsagePlanList = []
            for item in params.get("ApiUsagePlanList"):
                obj = ApiUsagePlan()
                obj._deserialize(item)
                self.ApiUsagePlanList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param PluginId: 绑定的API网关插件ID。
        :type PluginId: str
        :param ServiceId: 要操作的服务ID。
        :type ServiceId: str
        :param EnvironmentName: 要操作API的环境。
        :type EnvironmentName: str
        :param ApiIds: 要绑定的API列表。
        :type ApiIds: list of str
        """
        self.PluginId = None
        self.ServiceId = None
        self.EnvironmentName = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachPluginResponse(AbstractModel):
    """AttachPlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 绑定操作是否成功。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class AttachedApiInfo(AbstractModel):
    """插件绑定的API信息

    """

    def __init__(self):
        r"""
        :param ServiceId: API所在服务ID。
        :type ServiceId: str
        :param ServiceName: API所在服务名称。
        :type ServiceName: str
        :param ServiceDesc: API所在服务描述信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param ApiId: API ID。
        :type ApiId: str
        :param ApiName: API名称。
        :type ApiName: str
        :param ApiDesc: API描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param Environment: 插件绑定API的环境。
        :type Environment: str
        :param AttachedTime: 插件和API绑定时间。
        :type AttachedTime: str
        """
        self.ServiceId = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.ApiId = None
        self.ApiName = None
        self.ApiDesc = None
        self.Environment = None
        self.AttachedTime = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ApiDesc = params.get("ApiDesc")
        self.Environment = params.get("Environment")
        self.AttachedTime = params.get("AttachedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedApiSummary(AbstractModel):
    """插件绑定的API列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 插件绑定的API数量。
        :type TotalCount: int
        :param AttachedApis: 插件绑定的API信息。
        :type AttachedApis: list of AttachedApiInfo
        """
        self.TotalCount = None
        self.AttachedApis = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AttachedApis") is not None:
            self.AttachedApis = []
            for item in params.get("AttachedApis"):
                obj = AttachedApiInfo()
                obj._deserialize(item)
                self.AttachedApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedPluginInfo(AbstractModel):
    """已绑定的插件信息。

    """

    def __init__(self):
        r"""
        :param PluginId: 插件ID。
        :type PluginId: str
        :param Environment: 环境信息。
        :type Environment: str
        :param AttachedTime: 绑定时间。
        :type AttachedTime: str
        :param PluginName: 插件名称。
        :type PluginName: str
        :param PluginType: 插件类型。
        :type PluginType: str
        :param Description: 插件描述。
        :type Description: str
        :param PluginData: 插件定义语句。
        :type PluginData: str
        """
        self.PluginId = None
        self.Environment = None
        self.AttachedTime = None
        self.PluginName = None
        self.PluginType = None
        self.Description = None
        self.PluginData = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.Environment = params.get("Environment")
        self.AttachedTime = params.get("AttachedTime")
        self.PluginName = params.get("PluginName")
        self.PluginType = params.get("PluginType")
        self.Description = params.get("Description")
        self.PluginData = params.get("PluginData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachedPluginSummary(AbstractModel):
    """已绑定的插件信息。

    """

    def __init__(self):
        r"""
        :param TotalCount: 已绑定的插件总数。
        :type TotalCount: int
        :param PluginSummary: 已绑定的插件信息。
        :type PluginSummary: list of AttachedPluginInfo
        """
        self.TotalCount = None
        self.PluginSummary = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PluginSummary") is not None:
            self.PluginSummary = []
            for item in params.get("PluginSummary"):
                obj = AttachedPluginInfo()
                obj._deserialize(item)
                self.PluginSummary.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvailableApiInfo(AbstractModel):
    """插件相关的API信息。

    """

    def __init__(self):
        r"""
        :param ApiId: API ID。
        :type ApiId: str
        :param ApiName: API名称。
        :type ApiName: str
        :param ApiType: API类型。
        :type ApiType: str
        :param Path: API路径。
        :type Path: str
        :param Method: API方法。
        :type Method: str
        :param AttachedOtherPlugin: API是否绑定其他插件。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachedOtherPlugin: bool
        :param IsAttached: API是否绑定当前插件。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsAttached: bool
        """
        self.ApiId = None
        self.ApiName = None
        self.ApiType = None
        self.Path = None
        self.Method = None
        self.AttachedOtherPlugin = None
        self.IsAttached = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ApiType = params.get("ApiType")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.AttachedOtherPlugin = params.get("AttachedOtherPlugin")
        self.IsAttached = params.get("IsAttached")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Base64EncodedTriggerRule(AbstractModel):
    """Base64编码的header触发规则

    """

    def __init__(self):
        r"""
        :param Name: 进行编码触发的header，可选值 "Accept"和"Content_Type" 对应实际数据流请求header中的Accept和 Content-Type。
        :type Name: str
        :param Value: 进行编码触发的header的可选值数组, 数组元素的字符串最大长度为40，元素可以包括数字，英文字母以及特殊字符，特殊字符的可选值为： `.`    `+`    `*`   `-`   `/`  `_` 

例如 [
    "application/x-vpeg005",
    "application/xhtml+xml",
    "application/vnd.ms-project",
    "application/vnd.rn-rn_music_package"
] 等都是合法的。
        :type Value: list of str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiAppRequest(AbstractModel):
    """BindApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiAppId: 待绑定的应用唯一 ID 。
        :type ApiAppId: str
        :param Environment: 待绑定的环境。
        :type Environment: str
        :param ServiceId: 待绑定的服务唯一 ID。
        :type ServiceId: str
        :param ApiId: 待绑定的API唯一ID。
        :type ApiId: str
        """
        self.ApiAppId = None
        self.Environment = None
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.Environment = params.get("Environment")
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindApiAppResponse(AbstractModel):
    """BindApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindApiInfo(AbstractModel):
    """vpc通道绑定的api信息

    """

    def __init__(self):
        r"""
        :param ApiId: api唯一id
        :type ApiId: str
        :param ServiceId: Service唯一id
        :type ServiceId: str
        :param ApiName: api名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param ServiceName: 服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param BindTime: 绑定时间
        :type BindTime: str
        """
        self.ApiId = None
        self.ServiceId = None
        self.ApiName = None
        self.ServiceName = None
        self.BindTime = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ServiceId = params.get("ServiceId")
        self.ApiName = params.get("ApiName")
        self.ServiceName = params.get("ServiceName")
        self.BindTime = params.get("BindTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvironmentRequest(AbstractModel):
    """BindEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanIds: 待绑定的使用计划唯一 ID 列表。
        :type UsagePlanIds: list of str
        :param BindType: 绑定类型，取值为API、SERVICE，默认值为SERVICE。
        :type BindType: str
        :param Environment: 待绑定的环境。
        :type Environment: str
        :param ServiceId: 待绑定的服务唯一 ID。
        :type ServiceId: str
        :param ApiIds: API唯一ID数组，当bindType=API时，需要传入此参数。
        :type ApiIds: list of str
        """
        self.UsagePlanIds = None
        self.BindType = None
        self.Environment = None
        self.ServiceId = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.UsagePlanIds = params.get("UsagePlanIds")
        self.BindType = params.get("BindType")
        self.Environment = params.get("Environment")
        self.ServiceId = params.get("ServiceId")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindEnvironmentResponse(AbstractModel):
    """BindEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindIPStrategyRequest(AbstractModel):
    """BindIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待绑定的IP策略所属的服务唯一ID。
        :type ServiceId: str
        :param StrategyId: 待绑定的IP策略唯一ID。
        :type StrategyId: str
        :param EnvironmentName: IP策略待绑定的环境。
        :type EnvironmentName: str
        :param BindApiIds: IP策略待绑定的API列表。
        :type BindApiIds: list of str
        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.BindApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.BindApiIds = params.get("BindApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindIPStrategyResponse(AbstractModel):
    """BindIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindSecretIdsRequest(AbstractModel):
    """BindSecretIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 待绑定的使用计划唯一 ID。
        :type UsagePlanId: str
        :param AccessKeyIds: 待绑定的密钥 ID 数组。
        :type AccessKeyIds: list of str
        """
        self.UsagePlanId = None
        self.AccessKeyIds = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.AccessKeyIds = params.get("AccessKeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSecretIdsResponse(AbstractModel):
    """BindSecretIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindSubDomainRequest(AbstractModel):
    """BindSubDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param SubDomain: 待绑定的自定义的域名。
        :type SubDomain: str
        :param Protocol: 服务支持协议，可选值为http、https、http&https。
        :type Protocol: str
        :param NetType: 网络类型，可选值为OUTER、INNER。
        :type NetType: str
        :param IsDefaultMapping: 是否使用默认路径映射，默认为 true。为 false 时，表示自定义路径映射，此时 PathMappingSet 必填。
        :type IsDefaultMapping: bool
        :param NetSubDomain: 默认域名。
        :type NetSubDomain: str
        :param CertificateId: 待绑定自定义域名的证书唯一 ID。针对Protocol 为https或http&https可以选择上传。
        :type CertificateId: str
        :param PathMappingSet: 自定义域名路径映射，最多输入三个Environment，并且只能分别取值“test”、 ”prepub“、”release“。
        :type PathMappingSet: list of PathMapping
        :param IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。
        :type IsForcedHttps: bool
        """
        self.ServiceId = None
        self.SubDomain = None
        self.Protocol = None
        self.NetType = None
        self.IsDefaultMapping = None
        self.NetSubDomain = None
        self.CertificateId = None
        self.PathMappingSet = None
        self.IsForcedHttps = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        self.Protocol = params.get("Protocol")
        self.NetType = params.get("NetType")
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        self.NetSubDomain = params.get("NetSubDomain")
        self.CertificateId = params.get("CertificateId")
        if params.get("PathMappingSet") is not None:
            self.PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self.PathMappingSet.append(obj)
        self.IsForcedHttps = params.get("IsForcedHttps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindSubDomainResponse(AbstractModel):
    """BindSubDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BuildAPIDocRequest(AbstractModel):
    """BuildAPIDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self.ApiDocId = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BuildAPIDocResponse(AbstractModel):
    """BuildAPIDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 操作是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ConstantParameter(AbstractModel):
    """常量参数

    """

    def __init__(self):
        r"""
        :param Name: 常量参数名称。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Desc: 常量参数描述。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param Position: 常量参数位置。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: str
        :param DefaultValue: 常量参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        """
        self.Name = None
        self.Desc = None
        self.Position = None
        self.DefaultValue = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Position = params.get("Position")
        self.DefaultValue = params.get("DefaultValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosConfig(AbstractModel):
    """cos类型的api配置

    """

    def __init__(self):
        r"""
        :param Action: API调用后端COS的方式，前端请求方法与Action的可选值为：
GET：GetObject
PUT：PutObject
POST：PostObject、AppendObject
HEAD： HeadObject
DELETE： DeleteObject。
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param BucketName: API后端COS的存储桶名。
注意：此字段可能返回 null，表示取不到有效值。
        :type BucketName: str
        :param Authorization: API调用后端COS的签名开关，默认为false。
注意：此字段可能返回 null，表示取不到有效值。
        :type Authorization: bool
        :param PathMatchMode: API后端COS的路径匹配模式，可选值：
BackEndPath ： 后端路径匹配
FullPath ： 全路径匹配

默认值为：BackEndPath
注意：此字段可能返回 null，表示取不到有效值。
        :type PathMatchMode: str
        """
        self.Action = None
        self.BucketName = None
        self.Authorization = None
        self.PathMatchMode = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.BucketName = params.get("BucketName")
        self.Authorization = params.get("Authorization")
        self.PathMatchMode = params.get("PathMatchMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIDocRequest(AbstractModel):
    """CreateAPIDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiDocName: API文档名称
        :type ApiDocName: str
        :param ServiceId: 服务名称
        :type ServiceId: str
        :param Environment: 环境名称
        :type Environment: str
        :param ApiIds: 生成文档的API列表
        :type ApiIds: list of str
        """
        self.ApiDocName = None
        self.ServiceId = None
        self.Environment = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ApiDocName = params.get("ApiDocName")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIDocResponse(AbstractModel):
    """CreateAPIDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: API文档基本信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDoc()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiAppRequest(AbstractModel):
    """CreateApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiAppName: 用户自定义应用名称。
        :type ApiAppName: str
        :param ApiAppDesc: 应用描述
        :type ApiAppDesc: str
        """
        self.ApiAppName = None
        self.ApiAppDesc = None


    def _deserialize(self, params):
        self.ApiAppName = params.get("ApiAppName")
        self.ApiAppDesc = params.get("ApiAppDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiAppResponse(AbstractModel):
    """CreateApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 新增的应用详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiKeyRequest(AbstractModel):
    """CreateApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecretName: 用户自定义密钥名称。
        :type SecretName: str
        :param AccessKeyType: 密钥类型，支持 auto 和 manual（自定义密钥），默认为 auto。
        :type AccessKeyType: str
        :param AccessKeyId: 用户自定义密钥 ID，AccessKeyType 为 manual 时必传。长度为5 - 50字符，由字母、数字、英文下划线组成。
        :type AccessKeyId: str
        :param AccessKeySecret: 用户自定义密钥 Key，AccessKeyType 为 manual 时必传。长度为10 - 50字符，由字母、数字、英文下划线。
        :type AccessKeySecret: str
        """
        self.SecretName = None
        self.AccessKeyType = None
        self.AccessKeyId = None
        self.AccessKeySecret = None


    def _deserialize(self, params):
        self.SecretName = params.get("SecretName")
        self.AccessKeyType = params.get("AccessKeyType")
        self.AccessKeyId = params.get("AccessKeyId")
        self.AccessKeySecret = params.get("AccessKeySecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiKeyResponse(AbstractModel):
    """CreateApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 新增的密钥详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKey()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiRequest(AbstractModel):
    """CreateApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param ServiceType: API 的后端服务类型。支持HTTP、MOCK、TSF、SCF、WEBSOCKET、TARGET（内测）。
        :type ServiceType: str
        :param ServiceTimeout: API 的后端服务超时时间，单位是秒。
        :type ServiceTimeout: int
        :param Protocol: API 的前端请求协议，支持HTTP和WEBSOCKET。
        :type Protocol: str
        :param RequestConfig: 请求的前端配置。
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.ApiRequestConfig`
        :param ApiName: 用户自定义的 API 名称。
        :type ApiName: str
        :param ApiDesc: 用户自定义的 API 接口描述。
        :type ApiDesc: str
        :param ApiType: API 类型，支持NORMAL（普通API）和TSF（微服务API），默认为NORMAL。
        :type ApiType: str
        :param AuthType: API 鉴权类型。支持SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH、APP（应用认证）。默认为NONE。
        :type AuthType: str
        :param EnableCORS: 是否开启跨域。
        :type EnableCORS: bool
        :param ConstantParameters: 常量参数。
        :type ConstantParameters: list of ConstantParameter
        :param RequestParameters: 前端请求参数。
        :type RequestParameters: list of RequestParameter
        :param ApiBusinessType: 当AuthType 为 OAUTH时，该字段有效， NORMAL：业务api OAUTH：授权API。
        :type ApiBusinessType: str
        :param ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。
        :type ServiceMockReturnMessage: str
        :param MicroServices: API绑定微服务服务列表。
        :type MicroServices: list of MicroServiceReq
        :param ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: 微服务的健康检查配置。
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param TargetServices: target类型后端资源信息。（内测阶段）
        :type TargetServices: list of TargetServicesReq
        :param TargetServicesLoadBalanceConf: target类型负载均衡配置。（内测阶段）
        :type TargetServicesLoadBalanceConf: int
        :param TargetServicesHealthCheckConf: target健康检查配置。（内测阶段）
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。
        :type ServiceScfFunctionName: str
        :param ServiceWebsocketRegisterFunctionName: scf websocket注册函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。
        :type ServiceScfFunctionQualifier: str
        :param ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: 是否开启响应集成。当后端类型是SCF时生效。
        :type ServiceScfIsIntegratedResponse: bool
        :param IsDebugAfterCharge: 开始调试后计费。（云市场预留字段）
        :type IsDebugAfterCharge: bool
        :param IsDeleteResponseErrorCodes: 是否删除自定义响应配置错误码，如果不传或者传 False，不删除，当传 True 时，则删除此 API 所有自定义响应配置错误码。
        :type IsDeleteResponseErrorCodes: bool
        :param ResponseType: 返回类型。
        :type ResponseType: str
        :param ResponseSuccessExample: 自定义响应配置成功响应示例。
        :type ResponseSuccessExample: str
        :param ResponseFailExample: 自定义响应配置失败响应示例。
        :type ResponseFailExample: str
        :param ServiceConfig: API 的后端服务配置。
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
        :type AuthRelationApiId: str
        :param ServiceParameters: API的后端服务参数。
        :type ServiceParameters: list of ServiceParameter
        :param OauthConfig: oauth配置。当AuthType是OAUTH时生效。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param ResponseErrorCodes: 用户自定义错误码配置。
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param TargetNamespaceId: tsf serverless 命名空间ID。（内测中）
        :type TargetNamespaceId: str
        :param UserType: 用户类型。
        :type UserType: str
        :param IsBase64Encoded: 是否打开Base64编码，只有后端是scf时才会生效。
        :type IsBase64Encoded: bool
        :param EventBusId: 事件总线ID。
        :type EventBusId: str
        :param ServiceScfFunctionType: scf函数类型。当后端类型是SCF时生效。支持事件触发(EVENT)，http直通云函数(HTTP)。
        :type ServiceScfFunctionType: str
        :param EIAMAppType: EIAM应用类型。
        :type EIAMAppType: str
        :param EIAMAuthType: EIAM应用认证类型，支持仅认证（AuthenticationOnly）、认证和鉴权（Authorization）。
        :type EIAMAuthType: str
        :param TokenTimeout: EIAM应用Token 有效时间，单位为秒，默认为7200秒。
        :type TokenTimeout: int
        :param EIAMAppId: EIAM应用ID。
        :type EIAMAppId: str
        :param Owner: 资源的Owner
        :type Owner: str
        """
        self.ServiceId = None
        self.ServiceType = None
        self.ServiceTimeout = None
        self.Protocol = None
        self.RequestConfig = None
        self.ApiName = None
        self.ApiDesc = None
        self.ApiType = None
        self.AuthType = None
        self.EnableCORS = None
        self.ConstantParameters = None
        self.RequestParameters = None
        self.ApiBusinessType = None
        self.ServiceMockReturnMessage = None
        self.MicroServices = None
        self.ServiceTsfLoadBalanceConf = None
        self.ServiceTsfHealthCheckConf = None
        self.TargetServices = None
        self.TargetServicesLoadBalanceConf = None
        self.TargetServicesHealthCheckConf = None
        self.ServiceScfFunctionName = None
        self.ServiceWebsocketRegisterFunctionName = None
        self.ServiceWebsocketCleanupFunctionName = None
        self.ServiceWebsocketTransportFunctionName = None
        self.ServiceScfFunctionNamespace = None
        self.ServiceScfFunctionQualifier = None
        self.ServiceWebsocketRegisterFunctionNamespace = None
        self.ServiceWebsocketRegisterFunctionQualifier = None
        self.ServiceWebsocketTransportFunctionNamespace = None
        self.ServiceWebsocketTransportFunctionQualifier = None
        self.ServiceWebsocketCleanupFunctionNamespace = None
        self.ServiceWebsocketCleanupFunctionQualifier = None
        self.ServiceScfIsIntegratedResponse = None
        self.IsDebugAfterCharge = None
        self.IsDeleteResponseErrorCodes = None
        self.ResponseType = None
        self.ResponseSuccessExample = None
        self.ResponseFailExample = None
        self.ServiceConfig = None
        self.AuthRelationApiId = None
        self.ServiceParameters = None
        self.OauthConfig = None
        self.ResponseErrorCodes = None
        self.TargetNamespaceId = None
        self.UserType = None
        self.IsBase64Encoded = None
        self.EventBusId = None
        self.ServiceScfFunctionType = None
        self.EIAMAppType = None
        self.EIAMAuthType = None
        self.TokenTimeout = None
        self.EIAMAppId = None
        self.Owner = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceType = params.get("ServiceType")
        self.ServiceTimeout = params.get("ServiceTimeout")
        self.Protocol = params.get("Protocol")
        if params.get("RequestConfig") is not None:
            self.RequestConfig = ApiRequestConfig()
            self.RequestConfig._deserialize(params.get("RequestConfig"))
        self.ApiName = params.get("ApiName")
        self.ApiDesc = params.get("ApiDesc")
        self.ApiType = params.get("ApiType")
        self.AuthType = params.get("AuthType")
        self.EnableCORS = params.get("EnableCORS")
        if params.get("ConstantParameters") is not None:
            self.ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self.ConstantParameters.append(obj)
        if params.get("RequestParameters") is not None:
            self.RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = RequestParameter()
                obj._deserialize(item)
                self.RequestParameters.append(obj)
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        if params.get("MicroServices") is not None:
            self.MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroServiceReq()
                obj._deserialize(item)
                self.MicroServices.append(obj)
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self.ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self.ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self.ServiceTsfHealthCheckConf = HealthCheckConf()
            self.ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        if params.get("TargetServices") is not None:
            self.TargetServices = []
            for item in params.get("TargetServices"):
                obj = TargetServicesReq()
                obj._deserialize(item)
                self.TargetServices.append(obj)
        self.TargetServicesLoadBalanceConf = params.get("TargetServicesLoadBalanceConf")
        if params.get("TargetServicesHealthCheckConf") is not None:
            self.TargetServicesHealthCheckConf = HealthCheckConf()
            self.TargetServicesHealthCheckConf._deserialize(params.get("TargetServicesHealthCheckConf"))
        self.ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self.ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self.ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self.ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self.ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self.ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self.ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self.ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self.ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self.ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        self.ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self.ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self.ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self.IsDeleteResponseErrorCodes = params.get("IsDeleteResponseErrorCodes")
        self.ResponseType = params.get("ResponseType")
        self.ResponseSuccessExample = params.get("ResponseSuccessExample")
        self.ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = ServiceConfig()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("ServiceParameters") is not None:
            self.ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self.ServiceParameters.append(obj)
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        if params.get("ResponseErrorCodes") is not None:
            self.ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ResponseErrorCodeReq()
                obj._deserialize(item)
                self.ResponseErrorCodes.append(obj)
        self.TargetNamespaceId = params.get("TargetNamespaceId")
        self.UserType = params.get("UserType")
        self.IsBase64Encoded = params.get("IsBase64Encoded")
        self.EventBusId = params.get("EventBusId")
        self.ServiceScfFunctionType = params.get("ServiceScfFunctionType")
        self.EIAMAppType = params.get("EIAMAppType")
        self.EIAMAuthType = params.get("EIAMAuthType")
        self.TokenTimeout = params.get("TokenTimeout")
        self.EIAMAppId = params.get("EIAMAppId")
        self.Owner = params.get("Owner")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiResponse(AbstractModel):
    """CreateApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: api信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiResultInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateApiResultInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiResultInfo(AbstractModel):
    """创建api返回

    """

    def __init__(self):
        r"""
        :param ApiId: api id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Method: 请求方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        """
        self.ApiId = None
        self.Path = None
        self.Method = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiRsp(AbstractModel):
    """创建api返回

    """

    def __init__(self):
        r"""
        :param ApiId: api id
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param Path: 路径
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Method: 请求方法
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param Status: 导入状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param ErrMsg: 异常信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrMsg: str
        :param ApiName: api name
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        """
        self.ApiId = None
        self.Path = None
        self.Method = None
        self.CreatedTime = None
        self.Status = None
        self.ErrMsg = None
        self.ApiName = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.CreatedTime = params.get("CreatedTime")
        self.Status = params.get("Status")
        self.ErrMsg = params.get("ErrMsg")
        self.ApiName = params.get("ApiName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiRspSet(AbstractModel):
    """CreateApiRsp  返回加TotalCount

    """

    def __init__(self):
        r"""
        :param TotalCount: 个数
        :type TotalCount: int
        :param ApiSet: 返回的数组
        :type ApiSet: list of CreateApiRsp
        """
        self.TotalCount = None
        self.ApiSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiSet") is not None:
            self.ApiSet = []
            for item in params.get("ApiSet"):
                obj = CreateApiRsp()
                obj._deserialize(item)
                self.ApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPStrategyRequest(AbstractModel):
    """CreateIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务的唯一ID。
        :type ServiceId: str
        :param StrategyName: 用户自定义的策略名称。
        :type StrategyName: str
        :param StrategyType: 策略类型。支持WHITE（白名单）和BLACK（黑名单）。
        :type StrategyType: str
        :param StrategyData: 策略详情，多个ip 使用\n 分隔符分开。
        :type StrategyData: str
        """
        self.ServiceId = None
        self.StrategyName = None
        self.StrategyType = None
        self.StrategyData = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyName = params.get("StrategyName")
        self.StrategyType = params.get("StrategyType")
        self.StrategyData = params.get("StrategyData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPStrategyResponse(AbstractModel):
    """CreateIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 新建的IP策略详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IPStrategy()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreatePluginRequest(AbstractModel):
    """CreatePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginName: 用户自定义的插件名称。最长50个字符，最短2个字符，支持 a-z,A-Z,0-9,_, 必须字母开头，字母或者数字结尾。
        :type PluginName: str
        :param PluginType: 插件类型。目前支持IPControl, TrafficControl, Cors, CustomReq, CustomAuth，Routing，TrafficControlByParameter, CircuitBreaker, ProxyCache。
        :type PluginType: str
        :param PluginData: 插件定义语句，支持json。
        :type PluginData: str
        :param Description: 插件描述，限定200字以内。
        :type Description: str
        :param Tags: 标签
        :type Tags: list of Tag
        """
        self.PluginName = None
        self.PluginType = None
        self.PluginData = None
        self.Description = None
        self.Tags = None


    def _deserialize(self, params):
        self.PluginName = params.get("PluginName")
        self.PluginType = params.get("PluginType")
        self.PluginData = params.get("PluginData")
        self.Description = params.get("Description")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePluginResponse(AbstractModel):
    """CreatePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 新建的插件详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Plugin()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateServiceRequest(AbstractModel):
    """CreateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceName: 用户自定义的服务名称。
        :type ServiceName: str
        :param Protocol: 服务的前端请求类型。如 http、https、http&https。
        :type Protocol: str
        :param ServiceDesc: 用户自定义的服务描述。
        :type ServiceDesc: str
        :param ExclusiveSetName: 独立集群名称，用于指定创建服务所在的独立集群。
        :type ExclusiveSetName: str
        :param NetTypes: 网络类型列表，用于指定支持的访问类型，INNER为内网访问，OUTER为外网访问。默认为OUTER。
        :type NetTypes: list of str
        :param IpVersion: IP版本号，支持IPv4和IPv6，默认为IPv4。
        :type IpVersion: str
        :param SetServerName: 集群名称。保留字段，tsf serverlss类型使用。
        :type SetServerName: str
        :param AppIdType: 用户类型。保留类型，serverless用户使用。
        :type AppIdType: str
        :param Tags: 标签。
        :type Tags: list of Tag
        :param InstanceId: 独享实例id
        :type InstanceId: str
        :param UniqVpcId: vpc属性
        :type UniqVpcId: str
        """
        self.ServiceName = None
        self.Protocol = None
        self.ServiceDesc = None
        self.ExclusiveSetName = None
        self.NetTypes = None
        self.IpVersion = None
        self.SetServerName = None
        self.AppIdType = None
        self.Tags = None
        self.InstanceId = None
        self.UniqVpcId = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.Protocol = params.get("Protocol")
        self.ServiceDesc = params.get("ServiceDesc")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.NetTypes = params.get("NetTypes")
        self.IpVersion = params.get("IpVersion")
        self.SetServerName = params.get("SetServerName")
        self.AppIdType = params.get("AppIdType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.UniqVpcId = params.get("UniqVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceResponse(AbstractModel):
    """CreateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param ServiceName: 用户自定义服务名称。
        :type ServiceName: str
        :param ServiceDesc: 用户自定义服务描述。
        :type ServiceDesc: str
        :param OuterSubDomain: 外网默认域名。
        :type OuterSubDomain: str
        :param InnerSubDomain: vpc内网默认域名。
        :type InnerSubDomain: str
        :param CreatedTime: 服务创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type CreatedTime: str
        :param NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。
        :type NetTypes: list of str
        :param IpVersion: IP版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpVersion: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceId = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.OuterSubDomain = None
        self.InnerSubDomain = None
        self.CreatedTime = None
        self.NetTypes = None
        self.IpVersion = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.OuterSubDomain = params.get("OuterSubDomain")
        self.InnerSubDomain = params.get("InnerSubDomain")
        self.CreatedTime = params.get("CreatedTime")
        self.NetTypes = params.get("NetTypes")
        self.IpVersion = params.get("IpVersion")
        self.RequestId = params.get("RequestId")


class CreateUpstreamRequest(AbstractModel):
    """CreateUpstream请求参数结构体

    """

    def __init__(self):
        r"""
        :param Scheme: 后端协议，取值范围：HTTP, HTTPS
        :type Scheme: str
        :param Algorithm: 负载均衡算法，取值范围：ROUND-ROBIN
        :type Algorithm: str
        :param UniqVpcId: VPC唯一ID
        :type UniqVpcId: str
        :param UpstreamName: 后端通道名字
        :type UpstreamName: str
        :param UpstreamDescription: 后端通道描述
        :type UpstreamDescription: str
        :param UpstreamType: 后端访问类型，取值范围：IP_PORT, K8S
        :type UpstreamType: str
        :param Retries: 请求重试次数，默认3次
        :type Retries: int
        :param UpstreamHost: 网关转发到后端的Host请求头
        :type UpstreamHost: str
        :param Nodes: 后端节点
        :type Nodes: list of UpstreamNode
        :param Tags: 标签
        :type Tags: list of Tag
        :param HealthChecker: 健康检查配置，目前只支持VPC通道
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param K8sService: K8S容器服务的配置
        :type K8sService: list of K8sService
        """
        self.Scheme = None
        self.Algorithm = None
        self.UniqVpcId = None
        self.UpstreamName = None
        self.UpstreamDescription = None
        self.UpstreamType = None
        self.Retries = None
        self.UpstreamHost = None
        self.Nodes = None
        self.Tags = None
        self.HealthChecker = None
        self.K8sService = None


    def _deserialize(self, params):
        self.Scheme = params.get("Scheme")
        self.Algorithm = params.get("Algorithm")
        self.UniqVpcId = params.get("UniqVpcId")
        self.UpstreamName = params.get("UpstreamName")
        self.UpstreamDescription = params.get("UpstreamDescription")
        self.UpstreamType = params.get("UpstreamType")
        self.Retries = params.get("Retries")
        self.UpstreamHost = params.get("UpstreamHost")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("HealthChecker") is not None:
            self.HealthChecker = UpstreamHealthChecker()
            self.HealthChecker._deserialize(params.get("HealthChecker"))
        if params.get("K8sService") is not None:
            self.K8sService = []
            for item in params.get("K8sService"):
                obj = K8sService()
                obj._deserialize(item)
                self.K8sService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUpstreamResponse(AbstractModel):
    """CreateUpstream返回参数结构体

    """

    def __init__(self):
        r"""
        :param UpstreamId: 创建返回的唯一ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UpstreamId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.RequestId = params.get("RequestId")


class CreateUsagePlanRequest(AbstractModel):
    """CreateUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanName: 用户自定义的使用计划名称。
        :type UsagePlanName: str
        :param UsagePlanDesc: 用户自定义的使用计划描述。
        :type UsagePlanDesc: str
        :param MaxRequestNum: 请求配额总数，取值范围为-1或者[1, 99999999]，默认为-1，表示不开启。
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: 每秒请求限制数，取值范围为-1或者[1, 2000]，默认-1，表示不开启。
        :type MaxRequestNumPreSec: int
        """
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None


    def _deserialize(self, params):
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUsagePlanResponse(AbstractModel):
    """CreateUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DeleteAPIDocRequest(AbstractModel):
    """DeleteAPIDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self.ApiDocId = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAPIDocResponse(AbstractModel):
    """DeleteAPIDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 操作是否成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiAppRequest(AbstractModel):
    """DeleteApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiAppId: 应用唯一 ID。
        :type ApiAppId: str
        """
        self.ApiAppId = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiAppResponse(AbstractModel):
    """DeleteApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiKeyRequest(AbstractModel):
    """DeleteApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessKeyId: 待删除的密钥 ID。
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiKeyResponse(AbstractModel):
    """DeleteApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiRequest(AbstractModel):
    """DeleteApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param ApiId: API 接口唯一 ID。
        :type ApiId: str
        """
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteApiResponse(AbstractModel):
    """DeleteApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteIPStrategyRequest(AbstractModel):
    """DeleteIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待删除的IP策略所属的服务唯一ID。
        :type ServiceId: str
        :param StrategyId: 待删除的IP策略唯一ID。
        :type StrategyId: str
        """
        self.ServiceId = None
        self.StrategyId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIPStrategyResponse(AbstractModel):
    """DeleteIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeletePluginRequest(AbstractModel):
    """DeletePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginId: 要删除的API网关插件的ID。
        :type PluginId: str
        """
        self.PluginId = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePluginResponse(AbstractModel):
    """DeletePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除操作是否成功。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待删除服务的唯一 ID。
        :type ServiceId: str
        :param SkipVerification: 跳过删除前置条件校验（仅支持独享实例上的服务）
        :type SkipVerification: int
        """
        self.ServiceId = None
        self.SkipVerification = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SkipVerification = params.get("SkipVerification")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceResponse(AbstractModel):
    """DeleteService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteServiceSubDomainMappingRequest(AbstractModel):
    """DeleteServiceSubDomainMapping请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param SubDomain: 服务绑定的自定义域名。
        :type SubDomain: str
        :param Environment: 待删除映射的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。
        :type Environment: str
        """
        self.ServiceId = None
        self.SubDomain = None
        self.Environment = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceSubDomainMappingResponse(AbstractModel):
    """DeleteServiceSubDomainMapping返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除自定义域名的路径映射操作是否成功。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteUpstreamRequest(AbstractModel):
    """DeleteUpstream请求参数结构体

    """

    def __init__(self):
        r"""
        :param UpstreamId: 待删除的后端通道ID
        :type UpstreamId: str
        """
        self.UpstreamId = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUpstreamResponse(AbstractModel):
    """DeleteUpstream返回参数结构体

    """

    def __init__(self):
        r"""
        :param UpstreamId: 成功删除的后端通道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UpstreamId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.RequestId = params.get("RequestId")


class DeleteUsagePlanRequest(AbstractModel):
    """DeleteUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 待删除的使用计划唯一 ID。
        :type UsagePlanId: str
        """
        self.UsagePlanId = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUsagePlanResponse(AbstractModel):
    """DeleteUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DemoteServiceUsagePlanRequest(AbstractModel):
    """DemoteServiceUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 使用计划ID。
        :type UsagePlanId: str
        :param ServiceId: 待降级的服务唯一 ID。
        :type ServiceId: str
        :param Environment: 环境名称。
        :type Environment: str
        """
        self.UsagePlanId = None
        self.ServiceId = None
        self.Environment = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DemoteServiceUsagePlanResponse(AbstractModel):
    """DemoteServiceUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 降级操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DesApisStatus(AbstractModel):
    """api状态详情

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param ApiId: API唯一ID。
        :type ApiId: str
        :param ApiDesc: 用户自定义的 API 接口描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param ApiName: API 接口的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param VpcId: VPCID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param UniqVpcId: VPC唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param ApiType: API类型。取值为NORMAL（普通API）和TSF（微服务API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param Protocol: API协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param IsDebugAfterCharge: 是否买后调试。（云市场预留字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDebugAfterCharge: bool
        :param AuthType: API 鉴权类型。取值为SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH、EIAM。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param ApiBusinessType: OAUTH API的类型。当AuthType 为 OAUTH时该字段有效， 取值为NORMAL（业务API）和 OAUTH（授权API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiBusinessType: str
        :param AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthRelationApiId: str
        :param OauthConfig: OAUTH 配置信息。当AuthType是OAUTH时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param RelationBuniessApiIds: 授权API关联的业务API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationBuniessApiIds: list of str
        :param Tags: API关联的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param Path: API 的路径，如 /path。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Method: API 的请求方法，如 GET。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiDesc = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiName = None
        self.VpcId = None
        self.UniqVpcId = None
        self.ApiType = None
        self.Protocol = None
        self.IsDebugAfterCharge = None
        self.AuthType = None
        self.ApiBusinessType = None
        self.AuthRelationApiId = None
        self.OauthConfig = None
        self.RelationBuniessApiIds = None
        self.Tags = None
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiDesc = params.get("ApiDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiName = params.get("ApiName")
        self.VpcId = params.get("VpcId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.ApiType = params.get("ApiType")
        self.Protocol = params.get("Protocol")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self.AuthType = params.get("AuthType")
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        self.RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        self.Tags = params.get("Tags")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocDetailRequest(AbstractModel):
    """DescribeAPIDocDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self.ApiDocId = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocDetailResponse(AbstractModel):
    """DescribeAPIDocDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: API文档详细信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDocInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeAPIDocsRequest(AbstractModel):
    """DescribeAPIDocs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAPIDocsResponse(AbstractModel):
    """DescribeAPIDocs返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: API文档列表信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocs`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDocs()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeAllPluginApisRequest(AbstractModel):
    """DescribeAllPluginApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 要查询的服务ID。
        :type ServiceId: str
        :param PluginId: 要查询的插件ID。
        :type PluginId: str
        :param EnvironmentName: 环境信息。
        :type EnvironmentName: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.ServiceId = None
        self.PluginId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.PluginId = params.get("PluginId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAllPluginApisResponse(AbstractModel):
    """DescribeAllPluginApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 插件相关API的列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfoSummary`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiInfoSummary()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiAppBindApisStatusRequest(AbstractModel):
    """DescribeApiAppBindApisStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiAppId: 应用ID
        :type ApiAppId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。支持ApiId、ApiName、ServiceId、Environment 、KeyWord（ 可以匹配name或者ID）。
        :type Filters: list of Filter
        """
        self.ApiAppId = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppBindApisStatusResponse(AbstractModel):
    """DescribeApiAppBindApisStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 应用绑定的Api列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppApiInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiAppRequest(AbstractModel):
    """DescribeApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiAppId: 应用ID。
        :type ApiAppId: str
        """
        self.ApiAppId = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppResponse(AbstractModel):
    """DescribeApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 应用详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiAppsStatusRequest(AbstractModel):
    """DescribeApiAppsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。支持ApiAppId、ApiAppName、KeyWord（ 可以匹配name或者ID）。
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiAppsStatusResponse(AbstractModel):
    """DescribeApiAppsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 应用列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiBindApiAppsStatusRequest(AbstractModel):
    """DescribeApiBindApiAppsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param ApiIds: Api的ID的数组
        :type ApiIds: list of str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。支持ApiAppId、Environment、KeyWord（ 可以匹配name或者ID）。
        :type Filters: list of Filter
        """
        self.ServiceId = None
        self.ApiIds = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiIds = params.get("ApiIds")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiBindApiAppsStatusResponse(AbstractModel):
    """DescribeApiBindApiAppsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 应用绑定的Api列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiAppApiInfos()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiEnvironmentStrategyRequest(AbstractModel):
    """DescribeApiEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: API所属服务唯一ID。
        :type ServiceId: str
        :param EnvironmentNames: 环境列表。
        :type EnvironmentNames: list of str
        :param ApiId: API唯一ID。
        :type ApiId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.ServiceId = None
        self.EnvironmentNames = None
        self.ApiId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentNames = params.get("EnvironmentNames")
        self.ApiId = params.get("ApiId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiEnvironmentStrategyResponse(AbstractModel):
    """DescribeApiEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: api绑定策略详情
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiEnvironmentStrategyStataus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiEnvironmentStrategyStataus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiForApiAppRequest(AbstractModel):
    """DescribeApiForApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param ApiId: API 接口唯一 ID。
        :type ApiId: str
        :param ApiRegion: Api所属地域
        :type ApiRegion: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiRegion = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiRegion = params.get("ApiRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiForApiAppResponse(AbstractModel):
    """DescribeApiForApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: API 详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiKeyRequest(AbstractModel):
    """DescribeApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessKeyId: API 密钥 ID。
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeyResponse(AbstractModel):
    """DescribeApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 密钥详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKey()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiKeysStatusRequest(AbstractModel):
    """DescribeApiKeysStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。支持AccessKeyId、AccessKeySecret、SecretName、NotUsagePlanId、Status、KeyWord（ 可以匹配name或者path）。
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeysStatusResponse(AbstractModel):
    """DescribeApiKeysStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 密钥列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKeysStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKeysStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiRequest(AbstractModel):
    """DescribeApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param ApiId: API 接口唯一 ID。
        :type ApiId: str
        """
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiResponse(AbstractModel):
    """DescribeApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: API 详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiResultServiceParametersInfo(AbstractModel):
    """ServiceParameter

    """

    def __init__(self):
        r"""
        :param Name: API的后端服务参数名称。只有ServiceType是HTTP才会用到此参数。前后端参数名称可不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Position: API 的后端服务参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。前后端参数位置可配置不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: str
        :param RelevantRequestParameterPosition: API 的后端服务参数对应的前端参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterPosition: str
        :param RelevantRequestParameterName: API 的后端服务参数对应的前端参数名称。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterName: str
        :param DefaultValue: API 的后端服务参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        :param RelevantRequestParameterDesc: API 的后端服务参数备注。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterDesc: str
        """
        self.Name = None
        self.Position = None
        self.RelevantRequestParameterPosition = None
        self.RelevantRequestParameterName = None
        self.DefaultValue = None
        self.RelevantRequestParameterDesc = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Position = params.get("Position")
        self.RelevantRequestParameterPosition = params.get("RelevantRequestParameterPosition")
        self.RelevantRequestParameterName = params.get("RelevantRequestParameterName")
        self.DefaultValue = params.get("DefaultValue")
        self.RelevantRequestParameterDesc = params.get("RelevantRequestParameterDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiUsagePlanRequest(AbstractModel):
    """DescribeApiUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiUsagePlanResponse(AbstractModel):
    """DescribeApiUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: api绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiUsagePlanSet`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiUsagePlanSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApisStatusRequest(AbstractModel):
    """DescribeApisStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param Filters: API过滤条件。支持ApiId、ApiName、ApiPath、ApiType、AuthRelationApiId、AuthType、ApiBuniessType、NotUsagePlanId、 Environment、Tags (values为 $tag_key:tag_value的列表)、TagKeys （values 为 tag key的列表），其中NotUsagePlanId和Environment必须同时使用，不能单独使用一个。
        :type Filters: list of Filter
        """
        self.ServiceId = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApisStatusResponse(AbstractModel):
    """DescribeApisStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: API 详情列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeApisStatusResultInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeApisStatusResultInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApisStatusResultApiIdStatusSetInfo(AbstractModel):
    """api状态详情

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param ApiId: API唯一ID。
        :type ApiId: str
        :param ApiDesc: 用户自定义的 API 接口描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiDesc: str
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param ApiName: API 接口的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param VpcId: VPCID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: int
        :param UniqVpcId: VPC唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqVpcId: str
        :param ApiType: API类型。取值为NORMAL（普通API）和TSF（微服务API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiType: str
        :param Protocol: API协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param IsDebugAfterCharge: 是否买后调试。（云市场预留字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDebugAfterCharge: bool
        :param AuthType: API 鉴权类型。取值为SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH、EIAM。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: str
        :param ApiBusinessType: OAUTH API的类型。当AuthType 为 OAUTH时该字段有效， 取值为NORMAL（业务API）和 OAUTH（授权API）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiBusinessType: str
        :param AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthRelationApiId: str
        :param OauthConfig: OAUTH 配置信息。当AuthType是OAUTH时生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param RelationBuniessApiIds: 授权API关联的业务API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelationBuniessApiIds: list of str
        :param Tags: API关联的标签信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of ApigatewayTags
        :param Path: API 的路径，如 /path。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Method: API 的请求方法，如 GET。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiDesc = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ApiName = None
        self.VpcId = None
        self.UniqVpcId = None
        self.ApiType = None
        self.Protocol = None
        self.IsDebugAfterCharge = None
        self.AuthType = None
        self.ApiBusinessType = None
        self.AuthRelationApiId = None
        self.OauthConfig = None
        self.RelationBuniessApiIds = None
        self.Tags = None
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiDesc = params.get("ApiDesc")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ApiName = params.get("ApiName")
        self.VpcId = params.get("VpcId")
        self.UniqVpcId = params.get("UniqVpcId")
        self.ApiType = params.get("ApiType")
        self.Protocol = params.get("Protocol")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        self.AuthType = params.get("AuthType")
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        self.RelationBuniessApiIds = params.get("RelationBuniessApiIds")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = ApigatewayTags()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApisStatusResultInfo(AbstractModel):
    """描述api列表状态

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的 API 接口数量。
        :type TotalCount: int
        :param ApiIdStatusSet: API 接口列表。
        :type ApiIdStatusSet: list of DescribeApisStatusResultApiIdStatusSetInfo
        """
        self.TotalCount = None
        self.ApiIdStatusSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self.ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = DescribeApisStatusResultApiIdStatusSetInfo()
                obj._deserialize(item)
                self.ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExclusiveInstanceDetailRequest(AbstractModel):
    """DescribeExclusiveInstanceDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享实例唯一id
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExclusiveInstanceDetailResponse(AbstractModel):
    """DescribeExclusiveInstanceDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 独享实例详情
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.InstanceDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceDetail()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeExclusiveInstancesRequest(AbstractModel):
    """DescribeExclusiveInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页查询，limit
        :type Limit: int
        :param Offset: 分页查询，offset
        :type Offset: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExclusiveInstancesResponse(AbstractModel):
    """DescribeExclusiveInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 独享实例列表查询结果
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeExclusiveInstancesResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeExclusiveInstancesResult()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeExclusiveInstancesResult(AbstractModel):
    """数据结构

    """


class DescribeExclusiveInstancesStatusRequest(AbstractModel):
    """DescribeExclusiveInstancesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页查询，limit
        :type Limit: int
        :param Offset: 分页查询，offset
        :type Offset: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeExclusiveInstancesStatusResponse(AbstractModel):
    """DescribeExclusiveInstancesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 独享实例列表查询结果
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.InstanceSummary`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceSummary()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIPStrategyApisStatusRequest(AbstractModel):
    """DescribeIPStrategyApisStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param StrategyId: 策略唯一ID。
        :type StrategyId: str
        :param EnvironmentName: 策略所在环境。
        :type EnvironmentName: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。支持 ApiPath、ApiName、KeyWord（模糊查询Path 和Name）。
        :type Filters: list of Filter
        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategyApisStatusResponse(AbstractModel):
    """DescribeIPStrategyApisStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 环境绑定API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategyApiStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IPStrategyApiStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIPStrategyRequest(AbstractModel):
    """DescribeIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param StrategyId: IP 策略唯一ID。
        :type StrategyId: str
        :param EnvironmentName: 策略关联的环境。
        :type EnvironmentName: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。预留字段，目前不支持过滤。
        :type Filters: list of Filter
        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategyResponse(AbstractModel):
    """DescribeIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: IP策略详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IPStrategy()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIPStrategysStatusRequest(AbstractModel):
    """DescribeIPStrategysStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param Filters: 过滤条件。支持StrategyName。
        :type Filters: list of Filter
        """
        self.ServiceId = None
        self.Filters = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIPStrategysStatusResponse(AbstractModel):
    """DescribeIPStrategysStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 符合条件的策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategysStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = IPStrategysStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeLogSearchRequest(AbstractModel):
    """DescribeLogSearch请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 日志开始时间
        :type StartTime: str
        :param EndTime: 日志结束时间
        :type EndTime: str
        :param ServiceId: 服务id
        :type ServiceId: str
        :param Filters: 保留字段
        :type Filters: list of Filter
        :param Limit: 单次要返回的日志条数，单次返回的最大条数为100
        :type Limit: int
        :param ConText: 根据上次返回的ConText，获取后续的内容，最多可获取10000条
        :type ConText: str
        :param Sort: 按时间排序 asc（升序）或者 desc（降序），默认为 desc
        :type Sort: str
        :param Query: 保留字段
        :type Query: str
        :param LogQuerys: 检索条件,支持的检索条件如下：
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
        self.StartTime = None
        self.EndTime = None
        self.ServiceId = None
        self.Filters = None
        self.Limit = None
        self.ConText = None
        self.Sort = None
        self.Query = None
        self.LogQuerys = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ServiceId = params.get("ServiceId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Limit = params.get("Limit")
        self.ConText = params.get("ConText")
        self.Sort = params.get("Sort")
        self.Query = params.get("Query")
        if params.get("LogQuerys") is not None:
            self.LogQuerys = []
            for item in params.get("LogQuerys"):
                obj = LogQuery()
                obj._deserialize(item)
                self.LogQuerys.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLogSearchResponse(AbstractModel):
    """DescribeLogSearch返回参数结构体

    """

    def __init__(self):
        r"""
        :param ConText: 获取更多检索结果的游标，值为""表示无后续结果
        :type ConText: str
        :param LogSet: 由0或多条日志组成，每条日志格式如下：
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
        :param TotalCount: 单次搜索返回的日志条数，TotalCount <= Limit
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ConText = None
        self.LogSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ConText = params.get("ConText")
        self.LogSet = params.get("LogSet")
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePluginApisRequest(AbstractModel):
    """DescribePluginApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginId: 查询的插件ID。
        :type PluginId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.PluginId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginApisResponse(AbstractModel):
    """DescribePluginApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 插件绑定的API列表信息。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedApiSummary`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AttachedApiSummary()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePluginRequest(AbstractModel):
    """DescribePlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginId: 要查询的插件ID。
        :type PluginId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.PluginId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginResponse(AbstractModel):
    """DescribePlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 插件详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Plugin()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePluginsByApiRequest(AbstractModel):
    """DescribePluginsByApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiId: 要查询的API ID。
        :type ApiId: str
        :param ServiceId: 要查询的服务ID。
        :type ServiceId: str
        :param EnvironmentName: 环境信息。
        :type EnvironmentName: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.ApiId = None
        self.ServiceId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginsByApiResponse(AbstractModel):
    """DescribePluginsByApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 插件可绑定的API列表信息。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedPluginSummary`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = AttachedPluginSummary()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePluginsRequest(AbstractModel):
    """DescribePlugins请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginIds: 要查询的插件列表。
        :type PluginIds: list of str
        :param PluginName: 要查询的插件名称。
        :type PluginName: str
        :param PluginType: 要查询的插件类型。
        :type PluginType: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。预留字段，目前不支持过滤。
        :type Filters: list of Filter
        """
        self.PluginIds = None
        self.PluginName = None
        self.PluginType = None
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.PluginIds = params.get("PluginIds")
        self.PluginName = params.get("PluginName")
        self.PluginType = params.get("PluginType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePluginsResponse(AbstractModel):
    """DescribePlugins返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 插件详情。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.PluginSummary`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = PluginSummary()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceEnvironmentListRequest(AbstractModel):
    """DescribeServiceEnvironmentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentListResponse(AbstractModel):
    """DescribeServiceEnvironmentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 服务绑定环境详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentSet`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceEnvironmentSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceEnvironmentReleaseHistoryRequest(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param EnvironmentName: 环境名称。
        :type EnvironmentName: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentReleaseHistoryResponse(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 服务发布历史。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseHistory`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceReleaseHistory()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceEnvironmentStrategyRequest(AbstractModel):
    """DescribeServiceEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceEnvironmentStrategyResponse(AbstractModel):
    """DescribeServiceEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentStrategyStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceEnvironmentStrategyStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceForApiAppRequest(AbstractModel):
    """DescribeServiceForApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param ApiRegion: 服务所属的地域
        :type ApiRegion: str
        """
        self.ServiceId = None
        self.ApiRegion = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiRegion = params.get("ApiRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceForApiAppResponse(AbstractModel):
    """DescribeServiceForApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param AvailableEnvironments: 服务 环境列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableEnvironments: list of str
        :param ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param ServiceDesc: 服务描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param Protocol: 服务支持协议，可选值为http、https、http&https。
        :type Protocol: str
        :param CreatedTime: 服务创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 服务修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param ExclusiveSetName: 独立集群名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusiveSetName: str
        :param NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。
        :type NetTypes: list of str
        :param InternalSubDomain: 内网访问子域名。
        :type InternalSubDomain: str
        :param OuterSubDomain: 外网访问子域名。
        :type OuterSubDomain: str
        :param InnerHttpPort: 内网访问http服务端口号。
        :type InnerHttpPort: int
        :param InnerHttpsPort: 内网访问https端口号。
        :type InnerHttpsPort: int
        :param ApiTotalCount: API总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiTotalCount: int
        :param ApiIdStatusSet: API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiIdStatusSet: list of ApiIdStatus
        :param UsagePlanTotalCount: 使用计划总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanTotalCount: int
        :param UsagePlanList: 使用计划数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanList: list of UsagePlan
        :param IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpVersion: str
        :param UserType: 此服务的用户类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param SetId: 预留字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type SetId: int
        :param Tags: 服务绑定的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceId = None
        self.AvailableEnvironments = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.Protocol = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ExclusiveSetName = None
        self.NetTypes = None
        self.InternalSubDomain = None
        self.OuterSubDomain = None
        self.InnerHttpPort = None
        self.InnerHttpsPort = None
        self.ApiTotalCount = None
        self.ApiIdStatusSet = None
        self.UsagePlanTotalCount = None
        self.UsagePlanList = None
        self.IpVersion = None
        self.UserType = None
        self.SetId = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.AvailableEnvironments = params.get("AvailableEnvironments")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.Protocol = params.get("Protocol")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.NetTypes = params.get("NetTypes")
        self.InternalSubDomain = params.get("InternalSubDomain")
        self.OuterSubDomain = params.get("OuterSubDomain")
        self.InnerHttpPort = params.get("InnerHttpPort")
        self.InnerHttpsPort = params.get("InnerHttpsPort")
        self.ApiTotalCount = params.get("ApiTotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self.ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = ApiIdStatus()
                obj._deserialize(item)
                self.ApiIdStatusSet.append(obj)
        self.UsagePlanTotalCount = params.get("UsagePlanTotalCount")
        if params.get("UsagePlanList") is not None:
            self.UsagePlanList = []
            for item in params.get("UsagePlanList"):
                obj = UsagePlan()
                obj._deserialize(item)
                self.UsagePlanList.append(obj)
        self.IpVersion = params.get("IpVersion")
        self.UserType = params.get("UserType")
        self.SetId = params.get("SetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeServiceReleaseVersionRequest(AbstractModel):
    """DescribeServiceReleaseVersion请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceReleaseVersionResponse(AbstractModel):
    """DescribeServiceReleaseVersion返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 服务发布版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseVersion`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceReleaseVersion()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceReleaseVersionResultVersionListInfo(AbstractModel):
    """服务发布列表详情

    """

    def __init__(self):
        r"""
        :param VersionName: 版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param VersionDesc: 版本描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionDesc: str
        """
        self.VersionName = None
        self.VersionDesc = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.VersionDesc = params.get("VersionDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceRequest(AbstractModel):
    """DescribeService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceResponse(AbstractModel):
    """DescribeService返回参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param AvailableEnvironments: 服务 环境列表。
        :type AvailableEnvironments: list of str
        :param ServiceName: 服务名称。
        :type ServiceName: str
        :param ServiceDesc: 服务描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param Protocol: 服务支持协议，可选值为http、https、http&https。
        :type Protocol: str
        :param CreatedTime: 服务创建时间。
        :type CreatedTime: str
        :param ModifiedTime: 服务修改时间。
        :type ModifiedTime: str
        :param ExclusiveSetName: 独立集群名称。
        :type ExclusiveSetName: str
        :param NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。
        :type NetTypes: list of str
        :param InternalSubDomain: 内网访问子域名。
        :type InternalSubDomain: str
        :param OuterSubDomain: 外网访问子域名。
        :type OuterSubDomain: str
        :param InnerHttpPort: 内网访问http服务端口号。
        :type InnerHttpPort: int
        :param InnerHttpsPort: 内网访问https端口号。
        :type InnerHttpsPort: int
        :param ApiTotalCount: API总数。
        :type ApiTotalCount: int
        :param ApiIdStatusSet: API列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiIdStatusSet: list of ApiIdStatus
        :param UsagePlanTotalCount: 使用计划总数量。
        :type UsagePlanTotalCount: int
        :param UsagePlanList: 使用计划数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanList: list of UsagePlan
        :param IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpVersion: str
        :param UserType: 此服务的用户类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserType: str
        :param SetId: 预留字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type SetId: int
        :param Tags: 服务绑定的标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param InstanceId: 独享实例id
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 独享实例name
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param SetType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SetType: str
        :param DeploymentType: 服务部署的集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentType: str
        :param SpecialUse: 特殊用途, NULL和DEFAULT表示无特殊用途，其他用途如HTTP_DNS等
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecialUse: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceId = None
        self.AvailableEnvironments = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.Protocol = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ExclusiveSetName = None
        self.NetTypes = None
        self.InternalSubDomain = None
        self.OuterSubDomain = None
        self.InnerHttpPort = None
        self.InnerHttpsPort = None
        self.ApiTotalCount = None
        self.ApiIdStatusSet = None
        self.UsagePlanTotalCount = None
        self.UsagePlanList = None
        self.IpVersion = None
        self.UserType = None
        self.SetId = None
        self.Tags = None
        self.InstanceId = None
        self.InstanceName = None
        self.SetType = None
        self.DeploymentType = None
        self.SpecialUse = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.AvailableEnvironments = params.get("AvailableEnvironments")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.Protocol = params.get("Protocol")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.NetTypes = params.get("NetTypes")
        self.InternalSubDomain = params.get("InternalSubDomain")
        self.OuterSubDomain = params.get("OuterSubDomain")
        self.InnerHttpPort = params.get("InnerHttpPort")
        self.InnerHttpsPort = params.get("InnerHttpsPort")
        self.ApiTotalCount = params.get("ApiTotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self.ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = ApiIdStatus()
                obj._deserialize(item)
                self.ApiIdStatusSet.append(obj)
        self.UsagePlanTotalCount = params.get("UsagePlanTotalCount")
        if params.get("UsagePlanList") is not None:
            self.UsagePlanList = []
            for item in params.get("UsagePlanList"):
                obj = UsagePlan()
                obj._deserialize(item)
                self.UsagePlanList.append(obj)
        self.IpVersion = params.get("IpVersion")
        self.UserType = params.get("UserType")
        self.SetId = params.get("SetId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.SetType = params.get("SetType")
        self.DeploymentType = params.get("DeploymentType")
        self.SpecialUse = params.get("SpecialUse")
        self.RequestId = params.get("RequestId")


class DescribeServiceSubDomainMappingsRequest(AbstractModel):
    """DescribeServiceSubDomainMappings请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param SubDomain: 服务绑定的自定义域名。
        :type SubDomain: str
        """
        self.ServiceId = None
        self.SubDomain = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceSubDomainMappingsResponse(AbstractModel):
    """DescribeServiceSubDomainMappings返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 自定义路径映射列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceSubDomainMappings`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceSubDomainMappings()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceSubDomainsRequest(AbstractModel):
    """DescribeServiceSubDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceSubDomainsResponse(AbstractModel):
    """DescribeServiceSubDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 查询服务自定义域名列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DomainSets`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DomainSets()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceUsagePlanRequest(AbstractModel):
    """DescribeServiceUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self.ServiceId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServiceUsagePlanResponse(AbstractModel):
    """DescribeServiceUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 服务绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceUsagePlanSet`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceUsagePlanSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServicesStatusRequest(AbstractModel):
    """DescribeServicesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。支持ServiceId、ServiceName、NotUsagePlanId、Environment、IpVersion、InstanceId、NetType、EIAMAppId。
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeServicesStatusResponse(AbstractModel):
    """DescribeServicesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 服务列表查询结果。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServicesStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServicesStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUpstreamBindApis(AbstractModel):
    """查询后端通道绑定API列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
        :type TotalCount: int
        :param BindApiSet: 绑定的API信息
        :type BindApiSet: list of BindApiInfo
        """
        self.TotalCount = None
        self.BindApiSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BindApiSet") is not None:
            self.BindApiSet = []
            for item in params.get("BindApiSet"):
                obj = BindApiInfo()
                obj._deserialize(item)
                self.BindApiSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamBindApisRequest(AbstractModel):
    """DescribeUpstreamBindApis请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页大小
        :type Limit: int
        :param Offset: 分页起始位置
        :type Offset: int
        :param UpstreamId: 后端通道ID
        :type UpstreamId: str
        :param Filters: ServiceId和ApiId过滤查询
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.UpstreamId = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.UpstreamId = params.get("UpstreamId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamBindApisResponse(AbstractModel):
    """DescribeUpstreamBindApis返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 查询结果
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamBindApis`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeUpstreamBindApis()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUpstreamInfo(AbstractModel):
    """查询后端通道返回信息

    """

    def __init__(self):
        r"""
        :param TotalCount: 查询总数
        :type TotalCount: int
        :param UpstreamSet: 查询列表
        :type UpstreamSet: list of UpstreamInfo
        """
        self.TotalCount = None
        self.UpstreamSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UpstreamSet") is not None:
            self.UpstreamSet = []
            for item in params.get("UpstreamSet"):
                obj = UpstreamInfo()
                obj._deserialize(item)
                self.UpstreamSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamsRequest(AbstractModel):
    """DescribeUpstreams请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 分页大小
        :type Limit: int
        :param Offset: 分页起始位置
        :type Offset: int
        :param Filters: 过滤条件，支持后端通道ID（UpstreamId）、后端通道名字（UpstreamName）过滤查询
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUpstreamsResponse(AbstractModel):
    """DescribeUpstreams返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 查询结果
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DescribeUpstreamInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DescribeUpstreamInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanEnvironmentsRequest(AbstractModel):
    """DescribeUsagePlanEnvironments请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 待查询的使用计划唯一 ID。
        :type UsagePlanId: str
        :param BindType: 定类型，取值为 API、SERVICE，默认值为 SERVICE。
        :type BindType: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.UsagePlanId = None
        self.BindType = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.BindType = params.get("BindType")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanEnvironmentsResponse(AbstractModel):
    """DescribeUsagePlanEnvironments返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 使用计划绑定详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanEnvironmentStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanEnvironmentStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanRequest(AbstractModel):
    """DescribeUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 待查询的使用计划唯一 ID。
        :type UsagePlanId: str
        """
        self.UsagePlanId = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanResponse(AbstractModel):
    """DescribeUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanSecretIdsRequest(AbstractModel):
    """DescribeUsagePlanSecretIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 绑定的使用计划唯一 ID。
        :type UsagePlanId: str
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        """
        self.UsagePlanId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlanSecretIdsResponse(AbstractModel):
    """DescribeUsagePlanSecretIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 使用计划绑定的密钥列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanBindSecretStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanBindSecretStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlansStatusRequest(AbstractModel):
    """DescribeUsagePlansStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 使用计划过滤条件。支持UsagePlanId、UsagePlanName、NotServiceId、NotApiId、Environment。
        :type Filters: list of Filter
        """
        self.Limit = None
        self.Offset = None
        self.Filters = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsagePlansStatusResponse(AbstractModel):
    """DescribeUsagePlansStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlansStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlansStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DetachPluginRequest(AbstractModel):
    """DetachPlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginId: 要解绑的API网关插件ID。
        :type PluginId: str
        :param ServiceId: 要操作的服务ID。
        :type ServiceId: str
        :param EnvironmentName: 要操作API的环境。
        :type EnvironmentName: str
        :param ApiId: 要解绑的API ID。
        :type ApiId: str
        """
        self.PluginId = None
        self.ServiceId = None
        self.EnvironmentName = None
        self.ApiId = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachPluginResponse(AbstractModel):
    """DetachPlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 解绑操作是否成功。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableApiKeyRequest(AbstractModel):
    """DisableApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessKeyId: 待禁用的密钥 ID。
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableApiKeyResponse(AbstractModel):
    """DisableApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 禁用密钥操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DocumentSDK(AbstractModel):
    """api文档下载

    """

    def __init__(self):
        r"""
        :param DocumentURL: 生成的 document 会存放到 COS 中，此出参返回产生文件的下载链接。
        :type DocumentURL: str
        :param SdkURL: 生成的 SDK 会存放到 COS 中，此出参返回产生 SDK 文件的下载链接。
        :type SdkURL: str
        """
        self.DocumentURL = None
        self.SdkURL = None


    def _deserialize(self, params):
        self.DocumentURL = params.get("DocumentURL")
        self.SdkURL = params.get("SdkURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainSetList(AbstractModel):
    """服务自定义域名列表

    """

    def __init__(self):
        r"""
        :param DomainName: 域名名称。
        :type DomainName: str
        :param Status: 域名解析状态。1 表示正常解析，0 表示解析失败。
        :type Status: int
        :param CertificateId: 证书ID。
        :type CertificateId: str
        :param IsDefaultMapping: 是否使用默认路径映射。
        :type IsDefaultMapping: bool
        :param Protocol: 自定义域名协议类型。
        :type Protocol: str
        :param NetType: 网络类型（'INNER' 或 'OUTER'）。
        :type NetType: str
        :param IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。
        :type IsForcedHttps: bool
        :param RegistrationStatus: 域名备案注册状态
        :type RegistrationStatus: bool
        """
        self.DomainName = None
        self.Status = None
        self.CertificateId = None
        self.IsDefaultMapping = None
        self.Protocol = None
        self.NetType = None
        self.IsForcedHttps = None
        self.RegistrationStatus = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        self.CertificateId = params.get("CertificateId")
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        self.Protocol = params.get("Protocol")
        self.NetType = params.get("NetType")
        self.IsForcedHttps = params.get("IsForcedHttps")
        self.RegistrationStatus = params.get("RegistrationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainSets(AbstractModel):
    """自定义服务域名展示

    """

    def __init__(self):
        r"""
        :param TotalCount: 服务下的自定义域名数量。
        :type TotalCount: int
        :param DomainSet: 自定义服务域名列表。
        :type DomainSet: list of DomainSetList
        """
        self.TotalCount = None
        self.DomainSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DomainSet") is not None:
            self.DomainSet = []
            for item in params.get("DomainSet"):
                obj = DomainSetList()
                obj._deserialize(item)
                self.DomainSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApiKeyRequest(AbstractModel):
    """EnableApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessKeyId: 待启用的密钥 ID。
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableApiKeyResponse(AbstractModel):
    """EnableApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 启动密钥操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """服务发布的环境信息。

    """

    def __init__(self):
        r"""
        :param EnvironmentName: 环境名称。
        :type EnvironmentName: str
        :param Url: 访问路径。
        :type Url: str
        :param Status: 发布状态，1 表示已发布，0 表示未发布。
        :type Status: int
        :param VersionName: 运行版本。
        :type VersionName: str
        """
        self.EnvironmentName = None
        self.Url = None
        self.Status = None
        self.VersionName = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.VersionName = params.get("VersionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnvironmentStrategy(AbstractModel):
    """环境限流

    """

    def __init__(self):
        r"""
        :param EnvironmentName: 环境名
        :type EnvironmentName: str
        :param Quota: 限流值
        :type Quota: int
        """
        self.EnvironmentName = None
        self.Quota = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Quota = params.get("Quota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorCodes(AbstractModel):
    """用户自定义错误码

    """

    def __init__(self):
        r"""
        :param Code: 自定义响应配置错误码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        :param Msg: 自定义响应配置错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Msg: str
        :param Desc: 自定义响应配置错误码备注。
注意：此字段可能返回 null，表示取不到有效值。
        :type Desc: str
        :param ConvertedCode: 自定义错误码转换。
注意：此字段可能返回 null，表示取不到有效值。
        :type ConvertedCode: int
        :param NeedConvert: 是否需要开启错误码转换。
注意：此字段可能返回 null，表示取不到有效值。
        :type NeedConvert: bool
        """
        self.Code = None
        self.Msg = None
        self.Desc = None
        self.ConvertedCode = None
        self.NeedConvert = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Desc = params.get("Desc")
        self.ConvertedCode = params.get("ConvertedCode")
        self.NeedConvert = params.get("NeedConvert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param Name: 需要过滤的字段。
        :type Name: str
        :param Values: 字段的过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApiDocumentRequest(AbstractModel):
    """GenerateApiDocument请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待创建文档的服务唯一 ID。
        :type ServiceId: str
        :param GenEnvironment: 待创建 SDK 的服务所在环境。
        :type GenEnvironment: str
        :param GenLanguage: 待创建 SDK 的语言。当前只支持 Python 和 JavaScript。
        :type GenLanguage: str
        """
        self.ServiceId = None
        self.GenEnvironment = None
        self.GenLanguage = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.GenEnvironment = params.get("GenEnvironment")
        self.GenLanguage = params.get("GenLanguage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateApiDocumentResponse(AbstractModel):
    """GenerateApiDocument返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: api文档&sdk链接。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DocumentSDK`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = DocumentSDK()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class HealthCheckConf(AbstractModel):
    """健康检查配置，包括TsfHealthCheckConf和TargetServicesHealthCheckConf

    """

    def __init__(self):
        r"""
        :param IsHealthCheck: 是否开启健康检查。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsHealthCheck: bool
        :param RequestVolumeThreshold: 健康检查阈值。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestVolumeThreshold: int
        :param SleepWindowInMilliseconds: 窗口大小。
注意：此字段可能返回 null，表示取不到有效值。
        :type SleepWindowInMilliseconds: int
        :param ErrorThresholdPercentage: 阈值百分比。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorThresholdPercentage: int
        """
        self.IsHealthCheck = None
        self.RequestVolumeThreshold = None
        self.SleepWindowInMilliseconds = None
        self.ErrorThresholdPercentage = None


    def _deserialize(self, params):
        self.IsHealthCheck = params.get("IsHealthCheck")
        self.RequestVolumeThreshold = params.get("RequestVolumeThreshold")
        self.SleepWindowInMilliseconds = params.get("SleepWindowInMilliseconds")
        self.ErrorThresholdPercentage = params.get("ErrorThresholdPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategy(AbstractModel):
    """ip策略

    """

    def __init__(self):
        r"""
        :param StrategyId: 策略唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyId: str
        :param StrategyName: 用户自定义策略名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyName: str
        :param StrategyType: 策略类型。支持WHITE（白名单）和BLACK（黑名单）。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyType: str
        :param StrategyData: IP列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategyData: str
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 修改时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param ServiceId: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param BindApiTotalCount: 策略绑定的API数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindApiTotalCount: int
        :param BindApis: 绑定的API详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindApis: list of DesApisStatus
        """
        self.StrategyId = None
        self.StrategyName = None
        self.StrategyType = None
        self.StrategyData = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ServiceId = None
        self.BindApiTotalCount = None
        self.BindApis = None


    def _deserialize(self, params):
        self.StrategyId = params.get("StrategyId")
        self.StrategyName = params.get("StrategyName")
        self.StrategyType = params.get("StrategyType")
        self.StrategyData = params.get("StrategyData")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ServiceId = params.get("ServiceId")
        self.BindApiTotalCount = params.get("BindApiTotalCount")
        if params.get("BindApis") is not None:
            self.BindApis = []
            for item in params.get("BindApis"):
                obj = DesApisStatus()
                obj._deserialize(item)
                self.BindApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategyApi(AbstractModel):
    """策略绑定api列表

    """

    def __init__(self):
        r"""
        :param ApiId: API 唯一 ID。
        :type ApiId: str
        :param ApiName: 用户自定义的 API 名称。
        :type ApiName: str
        :param ApiType: API 类型。取值为NORMAL（普通API）和TSF （微服务API）。
        :type ApiType: str
        :param Path: API 的路径。如 /path。
        :type Path: str
        :param Method: API 的请求方法。如 GET。
        :type Method: str
        :param OtherIPStrategyId: API 已经绑定的其他策略唯一ID。
        :type OtherIPStrategyId: str
        :param OtherEnvironmentName: API 已经绑定的环境。
        :type OtherEnvironmentName: str
        """
        self.ApiId = None
        self.ApiName = None
        self.ApiType = None
        self.Path = None
        self.Method = None
        self.OtherIPStrategyId = None
        self.OtherEnvironmentName = None


    def _deserialize(self, params):
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ApiType = params.get("ApiType")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.OtherIPStrategyId = params.get("OtherIPStrategyId")
        self.OtherEnvironmentName = params.get("OtherEnvironmentName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategyApiStatus(AbstractModel):
    """ip策略绑定api详情

    """

    def __init__(self):
        r"""
        :param TotalCount: 环境绑定API数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ApiIdStatusSet: 环境绑定API详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiIdStatusSet: list of IPStrategyApi
        """
        self.TotalCount = None
        self.ApiIdStatusSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self.ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = IPStrategyApi()
                obj._deserialize(item)
                self.ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPStrategysStatus(AbstractModel):
    """策略列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 策略数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param StrategySet: 策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type StrategySet: list of IPStrategy
        """
        self.TotalCount = None
        self.StrategySet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("StrategySet") is not None:
            self.StrategySet = []
            for item in params.get("StrategySet"):
                obj = IPStrategy()
                obj._deserialize(item)
                self.StrategySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportOpenApiRequest(AbstractModel):
    """ImportOpenApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: API所在的服务唯一ID。
        :type ServiceId: str
        :param Content: openAPI正文内容。
        :type Content: str
        :param EncodeType: Content格式，只能是YAML或者JSON，默认是YAML。
        :type EncodeType: str
        :param ContentVersion: Content版本，默认是openAPI，目前只支持openAPI。
        :type ContentVersion: str
        """
        self.ServiceId = None
        self.Content = None
        self.EncodeType = None
        self.ContentVersion = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Content = params.get("Content")
        self.EncodeType = params.get("EncodeType")
        self.ContentVersion = params.get("ContentVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportOpenApiResponse(AbstractModel):
    """ImportOpenApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 导入OpenApi返回参数。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRspSet`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateApiRspSet()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """独享实例预付费详情

    """

    def __init__(self):
        r"""
        :param RenewFlag: 自动续费标示
        :type RenewFlag: str
        :param ExpiredTime: 预付费到期时间
        :type ExpiredTime: str
        """
        self.RenewFlag = None
        self.ExpiredTime = None


    def _deserialize(self, params):
        self.RenewFlag = params.get("RenewFlag")
        self.ExpiredTime = params.get("ExpiredTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceDetail(AbstractModel):
    """独享实例详情

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享实例唯一id
        :type InstanceId: str
        :param Zone: 可用区
        :type Zone: str
        :param InstanceName: 独享实例名字
        :type InstanceName: str
        :param InstanceDescription: 独享实例描述
        :type InstanceDescription: str
        :param InstanceChargeType: 独享实例计费类型
        :type InstanceChargeType: str
        :param InstanceState: 独享实例状态
        :type InstanceState: str
        :param InstanceChargePrepaid: 独享实例预付费类型
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargePrepaid: :class:`tencentcloud.apigateway.v20180808.models.InstanceChargePrepaid`
        :param InstanceType: 独享实例类型
        :type InstanceType: str
        :param NetworkConfig: 独享实例网络类型
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkConfig: :class:`tencentcloud.apigateway.v20180808.models.NetworkConfig`
        :param VpcConfig: 独享实例vpc配置
        :type VpcConfig: :class:`tencentcloud.apigateway.v20180808.models.VpcConfig`
        :param Parameters: 独享实例参数配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Parameters: list of ParameterInfo
        :param IsolationStartedTime: 独享实例隔离时间
        :type IsolationStartedTime: str
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param Zones: 可用区列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Zones: str
        """
        self.InstanceId = None
        self.Zone = None
        self.InstanceName = None
        self.InstanceDescription = None
        self.InstanceChargeType = None
        self.InstanceState = None
        self.InstanceChargePrepaid = None
        self.InstanceType = None
        self.NetworkConfig = None
        self.VpcConfig = None
        self.Parameters = None
        self.IsolationStartedTime = None
        self.CreatedTime = None
        self.Zones = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Zone = params.get("Zone")
        self.InstanceName = params.get("InstanceName")
        self.InstanceDescription = params.get("InstanceDescription")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InstanceState = params.get("InstanceState")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.InstanceType = params.get("InstanceType")
        if params.get("NetworkConfig") is not None:
            self.NetworkConfig = NetworkConfig()
            self.NetworkConfig._deserialize(params.get("NetworkConfig"))
        if params.get("VpcConfig") is not None:
            self.VpcConfig = VpcConfig()
            self.VpcConfig._deserialize(params.get("VpcConfig"))
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = ParameterInfo()
                obj._deserialize(item)
                self.Parameters.append(obj)
        self.IsolationStartedTime = params.get("IsolationStartedTime")
        self.CreatedTime = params.get("CreatedTime")
        self.Zones = params.get("Zones")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceInfo(AbstractModel):
    """独享实例信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享实例唯一id
        :type InstanceId: str
        :param InstanceName: 独享实例name
        :type InstanceName: str
        :param InstanceDescription: 独享实例描述
        :type InstanceDescription: str
        :param InstanceChargeType: 独享实例计费类型
        :type InstanceChargeType: str
        :param InstanceType: 独享实例类型
        :type InstanceType: str
        :param InstanceState: 独享实例状态
        :type InstanceState: str
        :param CreatedTime: 独享实例创建时间
        :type CreatedTime: str
        :param DealName: 订单号
注意：此字段可能返回 null，表示取不到有效值。
        :type DealName: str
        :param ResourceId: 资源ID同唯一id
        :type ResourceId: str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceDescription = None
        self.InstanceChargeType = None
        self.InstanceType = None
        self.InstanceState = None
        self.CreatedTime = None
        self.DealName = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceDescription = params.get("InstanceDescription")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InstanceType = params.get("InstanceType")
        self.InstanceState = params.get("InstanceState")
        self.CreatedTime = params.get("CreatedTime")
        self.DealName = params.get("DealName")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceParameterInput(AbstractModel):
    """独享实例参数信息

    """

    def __init__(self):
        r"""
        :param Name: ServiceRequestNumPreSec，ApiRequestNumPreSec
        :type Name: str
        :param Value: 参数值
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceSummary(AbstractModel):
    """专享查询列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 专享实例总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param InstanceSet: 专享实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceSet: list of InstanceInfo
        """
        self.TotalCount = None
        self.InstanceSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = InstanceInfo()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sLabel(AbstractModel):
    """k8s Label

    """

    def __init__(self):
        r"""
        :param Key: Label的Key
        :type Key: str
        :param Value: Label的Value
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class K8sService(AbstractModel):
    """k8s 服务的配置

    """

    def __init__(self):
        r"""
        :param Weight: 权重
        :type Weight: int
        :param ClusterId: k8s集群ID
        :type ClusterId: str
        :param Namespace: 容器命名空间
        :type Namespace: str
        :param ServiceName: 容器服务的名字
        :type ServiceName: str
        :param Port: 服务的端口
        :type Port: int
        :param ExtraLabels: 额外选择的Pod的Label
        :type ExtraLabels: list of K8sLabel
        :param Name: 自定义的服务名字，可选
        :type Name: str
        """
        self.Weight = None
        self.ClusterId = None
        self.Namespace = None
        self.ServiceName = None
        self.Port = None
        self.ExtraLabels = None
        self.Name = None


    def _deserialize(self, params):
        self.Weight = params.get("Weight")
        self.ClusterId = params.get("ClusterId")
        self.Namespace = params.get("Namespace")
        self.ServiceName = params.get("ServiceName")
        self.Port = params.get("Port")
        if params.get("ExtraLabels") is not None:
            self.ExtraLabels = []
            for item in params.get("ExtraLabels"):
                obj = K8sLabel()
                obj._deserialize(item)
                self.ExtraLabels.append(obj)
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogQuery(AbstractModel):
    """检索条件入参

    """

    def __init__(self):
        r"""
        :param Name: 检索字段
        :type Name: str
        :param Operator: 操作符
        :type Operator: str
        :param Value: 检索值
        :type Value: str
        """
        self.Name = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MicroService(AbstractModel):
    """API绑定的微服务信息。

    """

    def __init__(self):
        r"""
        :param ClusterId: 微服务集群ID。
        :type ClusterId: str
        :param NamespaceId: 微服务命名空间ID。
        :type NamespaceId: str
        :param MicroServiceName: 微服务名称。
        :type MicroServiceName: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.MicroServiceName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.MicroServiceName = params.get("MicroServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MicroServiceReq(AbstractModel):
    """tsf类型入参

    """

    def __init__(self):
        r"""
        :param ClusterId: 微服务集群。
        :type ClusterId: str
        :param NamespaceId: 微服务命名空间。
        :type NamespaceId: str
        :param MicroServiceName: 微服务名称。
        :type MicroServiceName: str
        """
        self.ClusterId = None
        self.NamespaceId = None
        self.MicroServiceName = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.NamespaceId = params.get("NamespaceId")
        self.MicroServiceName = params.get("MicroServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAPIDocRequest(AbstractModel):
    """ModifyAPIDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiDocId: API文档ID
        :type ApiDocId: str
        :param ApiDocName: API文档名称
        :type ApiDocName: str
        :param ServiceId: 服务名称
        :type ServiceId: str
        :param Environment: 环境名称
        :type Environment: str
        :param ApiIds: 生成文档的API列表
        :type ApiIds: list of str
        """
        self.ApiDocId = None
        self.ApiDocName = None
        self.ServiceId = None
        self.Environment = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        self.ApiDocName = params.get("ApiDocName")
        self.ServiceId = params.get("ServiceId")
        self.Environment = params.get("Environment")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAPIDocResponse(AbstractModel):
    """ModifyAPIDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: API文档基本信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDoc()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyApiAppRequest(AbstractModel):
    """ModifyApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiAppId: 应用唯一 ID。
        :type ApiAppId: str
        :param ApiAppName: 修改的应用名称
        :type ApiAppName: str
        :param ApiAppDesc: 修改的应用描述
        :type ApiAppDesc: str
        """
        self.ApiAppId = None
        self.ApiAppName = None
        self.ApiAppDesc = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.ApiAppName = params.get("ApiAppName")
        self.ApiAppDesc = params.get("ApiAppDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiAppResponse(AbstractModel):
    """ModifyApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyApiEnvironmentStrategyRequest(AbstractModel):
    """ModifyApiEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param Strategy: 限流值。
        :type Strategy: int
        :param EnvironmentName: 环境名。
        :type EnvironmentName: str
        :param ApiIds: API列表。
        :type ApiIds: list of str
        """
        self.ServiceId = None
        self.Strategy = None
        self.EnvironmentName = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Strategy = params.get("Strategy")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiEnvironmentStrategyResponse(AbstractModel):
    """ModifyApiEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyApiIncrementRequest(AbstractModel):
    """ModifyApiIncrement请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务ID
        :type ServiceId: str
        :param ApiId: 接口ID
        :type ApiId: str
        :param BusinessType: 需要修改的API auth类型(可选择OAUTH-授权API)
        :type BusinessType: str
        :param PublicKey: oauth接口需要修改的公钥值
        :type PublicKey: str
        :param LoginRedirectUrl: oauth接口重定向地址
        :type LoginRedirectUrl: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.BusinessType = None
        self.PublicKey = None
        self.LoginRedirectUrl = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.BusinessType = params.get("BusinessType")
        self.PublicKey = params.get("PublicKey")
        self.LoginRedirectUrl = params.get("LoginRedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiIncrementResponse(AbstractModel):
    """ModifyApiIncrement返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApiRequest(AbstractModel):
    """ModifyApi请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param ServiceType: API 的后端服务类型。支持HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。
        :type ServiceType: str
        :param RequestConfig: 请求的前端配置。
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`
        :param ApiId: API 接口唯一 ID。
        :type ApiId: str
        :param ApiName: 用户自定义的 API 名称。
        :type ApiName: str
        :param ApiDesc: 用户自定义的 API 接口描述。
        :type ApiDesc: str
        :param ApiType: API 类型，支持NORMAL和TSF，默认为NORMAL。
        :type ApiType: str
        :param AuthType: API 鉴权类型。支持SECRET、NONE、OAUTH、APP。默认为NONE。
        :type AuthType: str
        :param AuthRequired: 是否需要签名认证，True 表示需要，False 表示不需要。待废弃。
        :type AuthRequired: bool
        :param ServiceTimeout: API 的后端服务超时时间，单位是秒。
        :type ServiceTimeout: int
        :param Protocol: API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。
        :type Protocol: str
        :param EnableCORS: 是否需要开启跨域，Ture 表示需要，False 表示不需要。
        :type EnableCORS: bool
        :param ConstantParameters: 常量参数。
        :type ConstantParameters: list of ConstantParameter
        :param RequestParameters: 前端请求参数。
        :type RequestParameters: list of ReqParameter
        :param ApiBusinessType: 当AuthType 为 OAUTH时，该字段有效， NORMAL：业务api   OAUTH：授权API。
        :type ApiBusinessType: str
        :param ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。
        :type ServiceMockReturnMessage: str
        :param MicroServices: API绑定微服务服务列表。
        :type MicroServices: list of MicroServiceReq
        :param ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。
        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`
        :param ServiceTsfHealthCheckConf: 微服务的健康检查配置。
        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param TargetServicesLoadBalanceConf: target类型负载均衡配置。（内测阶段）
        :type TargetServicesLoadBalanceConf: int
        :param TargetServicesHealthCheckConf: target健康检查配置。（内测阶段）
        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`
        :param ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。
        :type ServiceScfFunctionName: str
        :param ServiceWebsocketRegisterFunctionName: scf websocket注册函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionName: str
        :param ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionName: str
        :param ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionName: str
        :param ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。
        :type ServiceScfFunctionNamespace: str
        :param ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。
        :type ServiceScfFunctionQualifier: str
        :param ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionNamespace: str
        :param ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketRegisterFunctionQualifier: str
        :param ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionNamespace: str
        :param ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketTransportFunctionQualifier: str
        :param ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionNamespace: str
        :param ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
        :type ServiceWebsocketCleanupFunctionQualifier: str
        :param ServiceScfIsIntegratedResponse: 是否开启响应集成。当后端类型是SCF时生效。
        :type ServiceScfIsIntegratedResponse: bool
        :param IsDebugAfterCharge: 开始调试后计费。（云市场预留字段）
        :type IsDebugAfterCharge: bool
        :param TagSpecifications: 标签。
        :type TagSpecifications: :class:`tencentcloud.apigateway.v20180808.models.Tag`
        :param IsDeleteResponseErrorCodes: 是否删除自定义响应配置错误码，如果不传或者传 False，不删除，当传 True 时，则删除此 API 所有自定义响应配置错误码。
        :type IsDeleteResponseErrorCodes: bool
        :param ResponseType: 返回类型。
        :type ResponseType: str
        :param ResponseSuccessExample: 自定义响应配置成功响应示例。
        :type ResponseSuccessExample: str
        :param ResponseFailExample: 自定义响应配置失败响应示例。
        :type ResponseFailExample: str
        :param ServiceConfig: API 的后端服务配置。
        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`
        :param AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
        :type AuthRelationApiId: str
        :param ServiceParameters: API的后端服务参数。
        :type ServiceParameters: list of ServiceParameter
        :param OauthConfig: oauth配置。当AuthType是OAUTH时生效。
        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`
        :param ResponseErrorCodes: 用户自定义错误码配置。
        :type ResponseErrorCodes: list of ResponseErrorCodeReq
        :param IsBase64Encoded: 是否开启Base64编码，只有后端为scf时才会生效。
        :type IsBase64Encoded: bool
        :param IsBase64Trigger: 是否开启Base64编码的header触发，只有后端为scf时才会生效。
        :type IsBase64Trigger: bool
        :param Base64EncodedTriggerRules: Header触发规则，总规则数不能超过10。
        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule
        :param EventBusId: 事件总线ID。
        :type EventBusId: str
        :param ServiceScfFunctionType: scf函数类型。当后端类型是SCF时生效。支持事件触发(EVENT)，http直通云函数(HTTP)。
        :type ServiceScfFunctionType: str
        :param EIAMAppType: EIAM应用类型。
        :type EIAMAppType: str
        :param EIAMAuthType: EIAM应用认证类型，支持仅认证（AuthenticationOnly）、认证和鉴权（Authorization）。
        :type EIAMAuthType: str
        :param EIAMAppId: EIAM应用Token 有效时间，单位为秒，默认为7200秒。
        :type EIAMAppId: str
        :param TokenTimeout: EIAM应用ID。
        :type TokenTimeout: int
        """
        self.ServiceId = None
        self.ServiceType = None
        self.RequestConfig = None
        self.ApiId = None
        self.ApiName = None
        self.ApiDesc = None
        self.ApiType = None
        self.AuthType = None
        self.AuthRequired = None
        self.ServiceTimeout = None
        self.Protocol = None
        self.EnableCORS = None
        self.ConstantParameters = None
        self.RequestParameters = None
        self.ApiBusinessType = None
        self.ServiceMockReturnMessage = None
        self.MicroServices = None
        self.ServiceTsfLoadBalanceConf = None
        self.ServiceTsfHealthCheckConf = None
        self.TargetServicesLoadBalanceConf = None
        self.TargetServicesHealthCheckConf = None
        self.ServiceScfFunctionName = None
        self.ServiceWebsocketRegisterFunctionName = None
        self.ServiceWebsocketCleanupFunctionName = None
        self.ServiceWebsocketTransportFunctionName = None
        self.ServiceScfFunctionNamespace = None
        self.ServiceScfFunctionQualifier = None
        self.ServiceWebsocketRegisterFunctionNamespace = None
        self.ServiceWebsocketRegisterFunctionQualifier = None
        self.ServiceWebsocketTransportFunctionNamespace = None
        self.ServiceWebsocketTransportFunctionQualifier = None
        self.ServiceWebsocketCleanupFunctionNamespace = None
        self.ServiceWebsocketCleanupFunctionQualifier = None
        self.ServiceScfIsIntegratedResponse = None
        self.IsDebugAfterCharge = None
        self.TagSpecifications = None
        self.IsDeleteResponseErrorCodes = None
        self.ResponseType = None
        self.ResponseSuccessExample = None
        self.ResponseFailExample = None
        self.ServiceConfig = None
        self.AuthRelationApiId = None
        self.ServiceParameters = None
        self.OauthConfig = None
        self.ResponseErrorCodes = None
        self.IsBase64Encoded = None
        self.IsBase64Trigger = None
        self.Base64EncodedTriggerRules = None
        self.EventBusId = None
        self.ServiceScfFunctionType = None
        self.EIAMAppType = None
        self.EIAMAuthType = None
        self.EIAMAppId = None
        self.TokenTimeout = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceType = params.get("ServiceType")
        if params.get("RequestConfig") is not None:
            self.RequestConfig = RequestConfig()
            self.RequestConfig._deserialize(params.get("RequestConfig"))
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.ApiDesc = params.get("ApiDesc")
        self.ApiType = params.get("ApiType")
        self.AuthType = params.get("AuthType")
        self.AuthRequired = params.get("AuthRequired")
        self.ServiceTimeout = params.get("ServiceTimeout")
        self.Protocol = params.get("Protocol")
        self.EnableCORS = params.get("EnableCORS")
        if params.get("ConstantParameters") is not None:
            self.ConstantParameters = []
            for item in params.get("ConstantParameters"):
                obj = ConstantParameter()
                obj._deserialize(item)
                self.ConstantParameters.append(obj)
        if params.get("RequestParameters") is not None:
            self.RequestParameters = []
            for item in params.get("RequestParameters"):
                obj = ReqParameter()
                obj._deserialize(item)
                self.RequestParameters.append(obj)
        self.ApiBusinessType = params.get("ApiBusinessType")
        self.ServiceMockReturnMessage = params.get("ServiceMockReturnMessage")
        if params.get("MicroServices") is not None:
            self.MicroServices = []
            for item in params.get("MicroServices"):
                obj = MicroServiceReq()
                obj._deserialize(item)
                self.MicroServices.append(obj)
        if params.get("ServiceTsfLoadBalanceConf") is not None:
            self.ServiceTsfLoadBalanceConf = TsfLoadBalanceConfResp()
            self.ServiceTsfLoadBalanceConf._deserialize(params.get("ServiceTsfLoadBalanceConf"))
        if params.get("ServiceTsfHealthCheckConf") is not None:
            self.ServiceTsfHealthCheckConf = HealthCheckConf()
            self.ServiceTsfHealthCheckConf._deserialize(params.get("ServiceTsfHealthCheckConf"))
        self.TargetServicesLoadBalanceConf = params.get("TargetServicesLoadBalanceConf")
        if params.get("TargetServicesHealthCheckConf") is not None:
            self.TargetServicesHealthCheckConf = HealthCheckConf()
            self.TargetServicesHealthCheckConf._deserialize(params.get("TargetServicesHealthCheckConf"))
        self.ServiceScfFunctionName = params.get("ServiceScfFunctionName")
        self.ServiceWebsocketRegisterFunctionName = params.get("ServiceWebsocketRegisterFunctionName")
        self.ServiceWebsocketCleanupFunctionName = params.get("ServiceWebsocketCleanupFunctionName")
        self.ServiceWebsocketTransportFunctionName = params.get("ServiceWebsocketTransportFunctionName")
        self.ServiceScfFunctionNamespace = params.get("ServiceScfFunctionNamespace")
        self.ServiceScfFunctionQualifier = params.get("ServiceScfFunctionQualifier")
        self.ServiceWebsocketRegisterFunctionNamespace = params.get("ServiceWebsocketRegisterFunctionNamespace")
        self.ServiceWebsocketRegisterFunctionQualifier = params.get("ServiceWebsocketRegisterFunctionQualifier")
        self.ServiceWebsocketTransportFunctionNamespace = params.get("ServiceWebsocketTransportFunctionNamespace")
        self.ServiceWebsocketTransportFunctionQualifier = params.get("ServiceWebsocketTransportFunctionQualifier")
        self.ServiceWebsocketCleanupFunctionNamespace = params.get("ServiceWebsocketCleanupFunctionNamespace")
        self.ServiceWebsocketCleanupFunctionQualifier = params.get("ServiceWebsocketCleanupFunctionQualifier")
        self.ServiceScfIsIntegratedResponse = params.get("ServiceScfIsIntegratedResponse")
        self.IsDebugAfterCharge = params.get("IsDebugAfterCharge")
        if params.get("TagSpecifications") is not None:
            self.TagSpecifications = Tag()
            self.TagSpecifications._deserialize(params.get("TagSpecifications"))
        self.IsDeleteResponseErrorCodes = params.get("IsDeleteResponseErrorCodes")
        self.ResponseType = params.get("ResponseType")
        self.ResponseSuccessExample = params.get("ResponseSuccessExample")
        self.ResponseFailExample = params.get("ResponseFailExample")
        if params.get("ServiceConfig") is not None:
            self.ServiceConfig = ServiceConfig()
            self.ServiceConfig._deserialize(params.get("ServiceConfig"))
        self.AuthRelationApiId = params.get("AuthRelationApiId")
        if params.get("ServiceParameters") is not None:
            self.ServiceParameters = []
            for item in params.get("ServiceParameters"):
                obj = ServiceParameter()
                obj._deserialize(item)
                self.ServiceParameters.append(obj)
        if params.get("OauthConfig") is not None:
            self.OauthConfig = OauthConfig()
            self.OauthConfig._deserialize(params.get("OauthConfig"))
        if params.get("ResponseErrorCodes") is not None:
            self.ResponseErrorCodes = []
            for item in params.get("ResponseErrorCodes"):
                obj = ResponseErrorCodeReq()
                obj._deserialize(item)
                self.ResponseErrorCodes.append(obj)
        self.IsBase64Encoded = params.get("IsBase64Encoded")
        self.IsBase64Trigger = params.get("IsBase64Trigger")
        if params.get("Base64EncodedTriggerRules") is not None:
            self.Base64EncodedTriggerRules = []
            for item in params.get("Base64EncodedTriggerRules"):
                obj = Base64EncodedTriggerRule()
                obj._deserialize(item)
                self.Base64EncodedTriggerRules.append(obj)
        self.EventBusId = params.get("EventBusId")
        self.ServiceScfFunctionType = params.get("ServiceScfFunctionType")
        self.EIAMAppType = params.get("EIAMAppType")
        self.EIAMAuthType = params.get("EIAMAuthType")
        self.EIAMAppId = params.get("EIAMAppId")
        self.TokenTimeout = params.get("TokenTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyApiResponse(AbstractModel):
    """ModifyApi返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyExclusiveInstanceRequest(AbstractModel):
    """ModifyExclusiveInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 独享实例唯一id
        :type InstanceId: str
        :param InstanceName: 独享实例name
        :type InstanceName: str
        :param InstanceDescription: 独享实例描述
        :type InstanceDescription: str
        :param Parameters: 独享实例参数配置
        :type Parameters: list of InstanceParameterInput
        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceDescription = None
        self.Parameters = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceDescription = params.get("InstanceDescription")
        if params.get("Parameters") is not None:
            self.Parameters = []
            for item in params.get("Parameters"):
                obj = InstanceParameterInput()
                obj._deserialize(item)
                self.Parameters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyExclusiveInstanceResponse(AbstractModel):
    """ModifyExclusiveInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 独享实例详情信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.InstanceDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = InstanceDetail()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyIPStrategyRequest(AbstractModel):
    """ModifyIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待修改的策略所属服务的唯一ID。
        :type ServiceId: str
        :param StrategyId: 待修改的策略唯一ID。
        :type StrategyId: str
        :param StrategyData: 待修改的策略详情。
        :type StrategyData: str
        """
        self.ServiceId = None
        self.StrategyId = None
        self.StrategyData = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.StrategyData = params.get("StrategyData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIPStrategyResponse(AbstractModel):
    """ModifyIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyPluginRequest(AbstractModel):
    """ModifyPlugin请求参数结构体

    """

    def __init__(self):
        r"""
        :param PluginId: 要修改的插件ID。
        :type PluginId: str
        :param PluginName: 要修改的API网关插件名称。最长50个字符，支持 a-z,A-Z,0-9,_, 必须字母开头，字母或者数字结尾。
        :type PluginName: str
        :param Description: 要修改的插件描述，限定200字以内。
        :type Description: str
        :param PluginData: 要修改的插件定义语句，支持json。
        :type PluginData: str
        """
        self.PluginId = None
        self.PluginName = None
        self.Description = None
        self.PluginData = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.PluginName = params.get("PluginName")
        self.Description = params.get("Description")
        self.PluginData = params.get("PluginData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPluginResponse(AbstractModel):
    """ModifyPlugin返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 修改操作是否成功。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceEnvironmentStrategyRequest(AbstractModel):
    """ModifyServiceEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务的唯一ID。
        :type ServiceId: str
        :param Strategy: 限流值。
        :type Strategy: int
        :param EnvironmentNames: 环境列表。
        :type EnvironmentNames: list of str
        """
        self.ServiceId = None
        self.Strategy = None
        self.EnvironmentNames = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.Strategy = params.get("Strategy")
        self.EnvironmentNames = params.get("EnvironmentNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceEnvironmentStrategyResponse(AbstractModel):
    """ModifyServiceEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceRequest(AbstractModel):
    """ModifyService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待修改服务的唯一 Id。
        :type ServiceId: str
        :param ServiceName: 修改后的服务名称。
        :type ServiceName: str
        :param ServiceDesc: 修改后的服务描述。
        :type ServiceDesc: str
        :param Protocol: 修改后的服务前端请求类型，如 http、https和 http&https。
        :type Protocol: str
        :param NetTypes: 网络类型列表，用于指定支持的访问类型，INNER为内网访问，OUTER为外网访问。默认为OUTER。
        :type NetTypes: list of str
        """
        self.ServiceId = None
        self.ServiceName = None
        self.ServiceDesc = None
        self.Protocol = None
        self.NetTypes = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.ServiceDesc = params.get("ServiceDesc")
        self.Protocol = params.get("Protocol")
        self.NetTypes = params.get("NetTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceResponse(AbstractModel):
    """ModifyService返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubDomainRequest(AbstractModel):
    """ModifySubDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param SubDomain: 待修改路径映射的自定义的域名。
        :type SubDomain: str
        :param IsDefaultMapping: 是否修改为使用默认路径映射。为 true，表示使用默认路径映射，为 false，表示使用自定义路径映射。
        :type IsDefaultMapping: bool
        :param CertificateId: 证书 ID，协议包含 HTTPS 的时候要传该字段。
        :type CertificateId: str
        :param Protocol: 修改后的自定义域名协议类型。（http，https 或 http&https)
        :type Protocol: str
        :param PathMappingSet: 修改后的路径映射列表。
        :type PathMappingSet: list of PathMapping
        :param NetType: 网络类型 （'INNER' 或 'OUTER'）
        :type NetType: str
        :param IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。
        :type IsForcedHttps: bool
        """
        self.ServiceId = None
        self.SubDomain = None
        self.IsDefaultMapping = None
        self.CertificateId = None
        self.Protocol = None
        self.PathMappingSet = None
        self.NetType = None
        self.IsForcedHttps = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        self.CertificateId = params.get("CertificateId")
        self.Protocol = params.get("Protocol")
        if params.get("PathMappingSet") is not None:
            self.PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self.PathMappingSet.append(obj)
        self.NetType = params.get("NetType")
        self.IsForcedHttps = params.get("IsForcedHttps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubDomainResponse(AbstractModel):
    """ModifySubDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 修改自定义域名操作是否成功。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyUpstreamRequest(AbstractModel):
    """ModifyUpstream请求参数结构体

    """

    def __init__(self):
        r"""
        :param UpstreamId: 后端通道唯一ID
        :type UpstreamId: str
        :param UpstreamName: 后端通道名字
        :type UpstreamName: str
        :param UpstreamDescription: 后端通道描述
        :type UpstreamDescription: str
        :param Scheme: 后端协议，取值范围：HTTP, HTTPS
        :type Scheme: str
        :param UpstreamType: 后端访问类型，取值范围：IP_PORT, K8S
        :type UpstreamType: str
        :param Algorithm: 负载均衡算法，取值范围：ROUND_ROBIN
        :type Algorithm: str
        :param UniqVpcId: VPC唯一ID
        :type UniqVpcId: str
        :param Retries: 请求重试次数，默认3次
        :type Retries: int
        :param UpstreamHost: 网关转发到后端的 Host 请求头
        :type UpstreamHost: str
        :param Nodes: 后端节点列表
        :type Nodes: list of UpstreamNode
        :param HealthChecker: 健康检查配置，目前只支持VPC通道
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param K8sService: 容器服务配置
        :type K8sService: list of K8sService
        """
        self.UpstreamId = None
        self.UpstreamName = None
        self.UpstreamDescription = None
        self.Scheme = None
        self.UpstreamType = None
        self.Algorithm = None
        self.UniqVpcId = None
        self.Retries = None
        self.UpstreamHost = None
        self.Nodes = None
        self.HealthChecker = None
        self.K8sService = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.UpstreamName = params.get("UpstreamName")
        self.UpstreamDescription = params.get("UpstreamDescription")
        self.Scheme = params.get("Scheme")
        self.UpstreamType = params.get("UpstreamType")
        self.Algorithm = params.get("Algorithm")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Retries = params.get("Retries")
        self.UpstreamHost = params.get("UpstreamHost")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        if params.get("HealthChecker") is not None:
            self.HealthChecker = UpstreamHealthChecker()
            self.HealthChecker._deserialize(params.get("HealthChecker"))
        if params.get("K8sService") is not None:
            self.K8sService = []
            for item in params.get("K8sService"):
                obj = K8sService()
                obj._deserialize(item)
                self.K8sService.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUpstreamResponse(AbstractModel):
    """ModifyUpstream返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 返回修改后的后端通道信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ModifyUpstreamResultInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ModifyUpstreamResultInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ModifyUpstreamResultInfo(AbstractModel):
    """后端通道详细信息

    """

    def __init__(self):
        r"""
        :param UpstreamId: 后端通道唯一ID
        :type UpstreamId: str
        :param UpstreamName: 后端通道名字
        :type UpstreamName: str
        :param UpstreamDescription: 后端通道描述
        :type UpstreamDescription: str
        :param Scheme: 后端协议，取值范围：HTTP, HTTPS
        :type Scheme: str
        :param Algorithm: 负载均衡算法，取值范围：ROUND_ROBIN
        :type Algorithm: str
        :param UniqVpcId: VPC唯一ID
        :type UniqVpcId: str
        :param Retries: 请求重试次数
        :type Retries: int
        :param Nodes: 后端节点
        :type Nodes: list of UpstreamNode
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param HealthChecker: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param UpstreamType: 后端的类型，取值范围：IP_PORT, K8S
        :type UpstreamType: str
        :param K8sServices: K8S容器服务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type K8sServices: list of K8sService
        :param UpstreamHost: 网关转发给后端的Host请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHost: str
        """
        self.UpstreamId = None
        self.UpstreamName = None
        self.UpstreamDescription = None
        self.Scheme = None
        self.Algorithm = None
        self.UniqVpcId = None
        self.Retries = None
        self.Nodes = None
        self.CreatedTime = None
        self.HealthChecker = None
        self.UpstreamType = None
        self.K8sServices = None
        self.UpstreamHost = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.UpstreamName = params.get("UpstreamName")
        self.UpstreamDescription = params.get("UpstreamDescription")
        self.Scheme = params.get("Scheme")
        self.Algorithm = params.get("Algorithm")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Retries = params.get("Retries")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.CreatedTime = params.get("CreatedTime")
        if params.get("HealthChecker") is not None:
            self.HealthChecker = UpstreamHealthChecker()
            self.HealthChecker._deserialize(params.get("HealthChecker"))
        self.UpstreamType = params.get("UpstreamType")
        if params.get("K8sServices") is not None:
            self.K8sServices = []
            for item in params.get("K8sServices"):
                obj = K8sService()
                obj._deserialize(item)
                self.K8sServices.append(obj)
        self.UpstreamHost = params.get("UpstreamHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUsagePlanRequest(AbstractModel):
    """ModifyUsagePlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 使用计划唯一 ID。
        :type UsagePlanId: str
        :param UsagePlanName: 修改后的用户自定义的使用计划名称。
        :type UsagePlanName: str
        :param UsagePlanDesc: 修改后的用户自定义的使用计划描述。
        :type UsagePlanDesc: str
        :param MaxRequestNum: 请求配额总数，取值范围为-1或者[1, 99999999]，默认为-1，表示不开启。
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: 每秒请求限制数，取值范围为-1或者[1, 2000]，默认-1，表示不开启。
        :type MaxRequestNumPreSec: int
        """
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUsagePlanResponse(AbstractModel):
    """ModifyUsagePlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class NetworkConfig(AbstractModel):
    """独享实例网络配置

    """

    def __init__(self):
        r"""
        :param InternetMaxBandwidthOut: 最大出带宽
        :type InternetMaxBandwidthOut: int
        :param EnableInternetInbound: EnableInternetInbound信息
        :type EnableInternetInbound: bool
        :param EnableInternetOutbound: EnableInternetOutbound信息
        :type EnableInternetOutbound: bool
        :param InboundIpAddresses: InboundIpAddresses信息
        :type InboundIpAddresses: list of str
        :param OutboundIpAddresses: OutboundIpAddresses信息
        :type OutboundIpAddresses: list of str
        """
        self.InternetMaxBandwidthOut = None
        self.EnableInternetInbound = None
        self.EnableInternetOutbound = None
        self.InboundIpAddresses = None
        self.OutboundIpAddresses = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.EnableInternetInbound = params.get("EnableInternetInbound")
        self.EnableInternetOutbound = params.get("EnableInternetOutbound")
        self.InboundIpAddresses = params.get("InboundIpAddresses")
        self.OutboundIpAddresses = params.get("OutboundIpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OauthConfig(AbstractModel):
    """Oauth授权配置信息

    """

    def __init__(self):
        r"""
        :param PublicKey: 公钥，用于验证用户token。
        :type PublicKey: str
        :param TokenLocation: token传递位置。
        :type TokenLocation: str
        :param LoginRedirectUrl: 重定向地址，用于引导用户登录操作。
        :type LoginRedirectUrl: str
        """
        self.PublicKey = None
        self.TokenLocation = None
        self.LoginRedirectUrl = None


    def _deserialize(self, params):
        self.PublicKey = params.get("PublicKey")
        self.TokenLocation = params.get("TokenLocation")
        self.LoginRedirectUrl = params.get("LoginRedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParameterInfo(AbstractModel):
    """独享实例配置参数

    """

    def __init__(self):
        r"""
        :param Name: 名字
        :type Name: str
        :param Value: 当前值
        :type Value: int
        :param Default: 默认值
        :type Default: int
        :param Unit: 单位
        :type Unit: str
        :param Type: 类型, integer|string
        :type Type: str
        :param Minimum: 最小
        :type Minimum: int
        :param Maximum: 最大
        :type Maximum: int
        :param ModifedTime: 修改时间
        :type ModifedTime: str
        :param ValueString: 字符类型的值，当Type为string时才有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueString: str
        :param DefaultValueString: 字符类型的默认值，当Type为string时才有意义
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValueString: str
        :param Range: 可调整范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Range: str
        """
        self.Name = None
        self.Value = None
        self.Default = None
        self.Unit = None
        self.Type = None
        self.Minimum = None
        self.Maximum = None
        self.ModifedTime = None
        self.ValueString = None
        self.DefaultValueString = None
        self.Range = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Default = params.get("Default")
        self.Unit = params.get("Unit")
        self.Type = params.get("Type")
        self.Minimum = params.get("Minimum")
        self.Maximum = params.get("Maximum")
        self.ModifedTime = params.get("ModifedTime")
        self.ValueString = params.get("ValueString")
        self.DefaultValueString = params.get("DefaultValueString")
        self.Range = params.get("Range")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathMapping(AbstractModel):
    """自定义域名的路径映射。

    """

    def __init__(self):
        r"""
        :param Path: 路径。
        :type Path: str
        :param Environment: 发布环境，可选值为“test”、 ”prepub“、”release“。
        :type Environment: str
        """
        self.Path = None
        self.Environment = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Environment = params.get("Environment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Plugin(AbstractModel):
    """API网关插件详情。

    """

    def __init__(self):
        r"""
        :param PluginId: 插件ID。
        :type PluginId: str
        :param PluginName: 插件名称。
        :type PluginName: str
        :param PluginType: 插件类型。
        :type PluginType: str
        :param PluginData: 插件定义语句。
        :type PluginData: str
        :param Description: 插件描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param CreatedTime: 插件创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type CreatedTime: str
        :param ModifiedTime: 插件修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
        :type ModifiedTime: str
        :param AttachedApiTotalCount: 插件绑定的API总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachedApiTotalCount: int
        :param AttachedApis: 插件绑定的API信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type AttachedApis: list of AttachedApiInfo
        """
        self.PluginId = None
        self.PluginName = None
        self.PluginType = None
        self.PluginData = None
        self.Description = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.AttachedApiTotalCount = None
        self.AttachedApis = None


    def _deserialize(self, params):
        self.PluginId = params.get("PluginId")
        self.PluginName = params.get("PluginName")
        self.PluginType = params.get("PluginType")
        self.PluginData = params.get("PluginData")
        self.Description = params.get("Description")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.AttachedApiTotalCount = params.get("AttachedApiTotalCount")
        if params.get("AttachedApis") is not None:
            self.AttachedApis = []
            for item in params.get("AttachedApis"):
                obj = AttachedApiInfo()
                obj._deserialize(item)
                self.AttachedApis.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PluginSummary(AbstractModel):
    """插件列表详情。

    """

    def __init__(self):
        r"""
        :param TotalCount: 插件个数。
        :type TotalCount: int
        :param PluginSet: 插件详情。
        :type PluginSet: list of Plugin
        """
        self.TotalCount = None
        self.PluginSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("PluginSet") is not None:
            self.PluginSet = []
            for item in params.get("PluginSet"):
                obj = Plugin()
                obj._deserialize(item)
                self.PluginSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseService(AbstractModel):
    """发布服务返回

    """

    def __init__(self):
        r"""
        :param ReleaseDesc: 发布时的备注信息填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseDesc: str
        :param ReleaseVersion: 发布的版本id。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseVersion: str
        """
        self.ReleaseDesc = None
        self.ReleaseVersion = None


    def _deserialize(self, params):
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ReleaseVersion = params.get("ReleaseVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseServiceRequest(AbstractModel):
    """ReleaseService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待发布服务的唯一 ID。
        :type ServiceId: str
        :param EnvironmentName: 待发布的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。
        :type EnvironmentName: str
        :param ReleaseDesc: 本次的发布描述。
        :type ReleaseDesc: str
        :param ApiIds: apiId列表，预留字段，默认全量api发布。
        :type ApiIds: list of str
        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.ReleaseDesc = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ReleaseDesc = params.get("ReleaseDesc")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseServiceResponse(AbstractModel):
    """ReleaseService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 发布信息。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ReleaseService`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ReleaseService()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ReqParameter(AbstractModel):
    """请求参数

    """

    def __init__(self):
        r"""
        :param Name: API 的前端参数名称。
        :type Name: str
        :param Position: API 的前端参数位置，如 header。目前支持 header、query、path。
        :type Position: str
        :param Type: API 的前端参数类型，如 String、int。
        :type Type: str
        :param DefaultValue: API 的前端参数默认值。
        :type DefaultValue: str
        :param Required: API 的前端参数是否必填，True：表示必填，False：表示可选。
        :type Required: bool
        :param Desc: API 的前端参数备注。
        :type Desc: str
        """
        self.Name = None
        self.Position = None
        self.Type = None
        self.DefaultValue = None
        self.Required = None
        self.Desc = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Position = params.get("Position")
        self.Type = params.get("Type")
        self.DefaultValue = params.get("DefaultValue")
        self.Required = params.get("Required")
        self.Desc = params.get("Desc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestConfig(AbstractModel):
    """前端路径配置

    """

    def __init__(self):
        r"""
        :param Path: API 的路径，如 /path。
        :type Path: str
        :param Method: API 的请求方法，如 GET。
        :type Method: str
        """
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestParameter(AbstractModel):
    """请求参数

    """

    def __init__(self):
        r"""
        :param Name: 请求参数名称
        :type Name: str
        :param Desc: 描述
        :type Desc: str
        :param Position: 参数位置
        :type Position: str
        :param Type: 参数类型
        :type Type: str
        :param DefaultValue: 默认值
        :type DefaultValue: str
        :param Required: 是否必须
        :type Required: bool
        """
        self.Name = None
        self.Desc = None
        self.Position = None
        self.Type = None
        self.DefaultValue = None
        self.Required = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Desc = params.get("Desc")
        self.Position = params.get("Position")
        self.Type = params.get("Type")
        self.DefaultValue = params.get("DefaultValue")
        self.Required = params.get("Required")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAPIDocPasswordRequest(AbstractModel):
    """ResetAPIDocPassword请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiDocId: API文档ID
        :type ApiDocId: str
        """
        self.ApiDocId = None


    def _deserialize(self, params):
        self.ApiDocId = params.get("ApiDocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAPIDocPasswordResponse(AbstractModel):
    """ResetAPIDocPassword返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: API文档基本信息
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = APIDoc()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class ResponseErrorCodeReq(AbstractModel):
    """错误码入参

    """

    def __init__(self):
        r"""
        :param Code: 自定义响应配置错误码。
        :type Code: int
        :param Msg: 自定义响应配置错误信息。
        :type Msg: str
        :param Desc: 自定义响应配置错误码备注。
        :type Desc: str
        :param ConvertedCode: 自定义错误码转换。
        :type ConvertedCode: int
        :param NeedConvert: 是否需要开启错误码转换。
        :type NeedConvert: bool
        """
        self.Code = None
        self.Msg = None
        self.Desc = None
        self.ConvertedCode = None
        self.NeedConvert = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Msg = params.get("Msg")
        self.Desc = params.get("Desc")
        self.ConvertedCode = params.get("ConvertedCode")
        self.NeedConvert = params.get("NeedConvert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Service(AbstractModel):
    """展示服务列表用

    """

    def __init__(self):
        r"""
        :param InnerHttpsPort: 内网访问https端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpsPort: int
        :param ServiceDesc: 用户自定义的服务描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceDesc: str
        :param Protocol: 服务的前端请求类型。如http、https 或者 http&https。
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param NetTypes: 服务支持的网络类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type NetTypes: list of str
        :param ExclusiveSetName: 独占集群名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExclusiveSetName: str
        :param ServiceId: 服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpVersion: str
        :param AvailableEnvironments: 已经发布的环境列表。如test、prepub、release。
注意：此字段可能返回 null，表示取不到有效值。
        :type AvailableEnvironments: list of str
        :param ServiceName: 用户自定义的服务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param OuterSubDomain: 系统为该服务分配的外网域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type OuterSubDomain: str
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param InnerHttpPort: 内网访问http端口。
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerHttpPort: int
        :param InnerSubDomain: 系统为该服务自动分配的内网域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type InnerSubDomain: str
        :param TradeIsolateStatus: 服务的计费状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type TradeIsolateStatus: int
        :param Tags: 服务绑定的标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param InstanceId: 独享实例
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param SetType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SetType: str
        :param DeploymentType: 服务部署的集群类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DeploymentType: str
        """
        self.InnerHttpsPort = None
        self.ServiceDesc = None
        self.Protocol = None
        self.ModifiedTime = None
        self.NetTypes = None
        self.ExclusiveSetName = None
        self.ServiceId = None
        self.IpVersion = None
        self.AvailableEnvironments = None
        self.ServiceName = None
        self.OuterSubDomain = None
        self.CreatedTime = None
        self.InnerHttpPort = None
        self.InnerSubDomain = None
        self.TradeIsolateStatus = None
        self.Tags = None
        self.InstanceId = None
        self.SetType = None
        self.DeploymentType = None


    def _deserialize(self, params):
        self.InnerHttpsPort = params.get("InnerHttpsPort")
        self.ServiceDesc = params.get("ServiceDesc")
        self.Protocol = params.get("Protocol")
        self.ModifiedTime = params.get("ModifiedTime")
        self.NetTypes = params.get("NetTypes")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.ServiceId = params.get("ServiceId")
        self.IpVersion = params.get("IpVersion")
        self.AvailableEnvironments = params.get("AvailableEnvironments")
        self.ServiceName = params.get("ServiceName")
        self.OuterSubDomain = params.get("OuterSubDomain")
        self.CreatedTime = params.get("CreatedTime")
        self.InnerHttpPort = params.get("InnerHttpPort")
        self.InnerSubDomain = params.get("InnerSubDomain")
        self.TradeIsolateStatus = params.get("TradeIsolateStatus")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.SetType = params.get("SetType")
        self.DeploymentType = params.get("DeploymentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceConfig(AbstractModel):
    """ServiceConfig配置

    """

    def __init__(self):
        r"""
        :param Product: 后端类型。启用vpc时生效，目前支持的类型为clb, cvm和upstream
        :type Product: str
        :param UniqVpcId: vpc 的唯一ID。
        :type UniqVpcId: str
        :param Url: API 的后端服务url。如果ServiceType是HTTP，则此参数必传。
        :type Url: str
        :param Path: API 的后端服务路径，如 /path。如果 ServiceType 是 HTTP，则此参数必传。前后端路径可不同。
        :type Path: str
        :param Method: API的后端服务请求方法，如 GET。如果 ServiceType 是 HTTP，则此参数必传。前后端方法可不同。
        :type Method: str
        :param UpstreamId: 当绑定vpc通道才需要
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamId: str
        :param CosConfig: API后端COS配置。如果 ServiceType 是 COS，则此参数必传。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosConfig: :class:`tencentcloud.apigateway.v20180808.models.CosConfig`
        """
        self.Product = None
        self.UniqVpcId = None
        self.Url = None
        self.Path = None
        self.Method = None
        self.UpstreamId = None
        self.CosConfig = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Url = params.get("Url")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.UpstreamId = params.get("UpstreamId")
        if params.get("CosConfig") is not None:
            self.CosConfig = CosConfig()
            self.CosConfig._deserialize(params.get("CosConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentSet(AbstractModel):
    """服务绑定环境详情

    """

    def __init__(self):
        r"""
        :param TotalCount: 服务绑定环境总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param EnvironmentList: 服务绑定环境列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentList: list of Environment
        """
        self.TotalCount = None
        self.EnvironmentList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self.EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = Environment()
                obj._deserialize(item)
                self.EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentStrategy(AbstractModel):
    """服务环境策略

    """

    def __init__(self):
        r"""
        :param EnvironmentName: 环境名。
        :type EnvironmentName: str
        :param Url: 访问服务对应环境的url。
        :type Url: str
        :param Status: 发布状态。
        :type Status: int
        :param VersionName: 发布的版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param Strategy: 限流值。
        :type Strategy: int
        :param MaxStrategy: 最大限流值
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxStrategy: int
        """
        self.EnvironmentName = None
        self.Url = None
        self.Status = None
        self.VersionName = None
        self.Strategy = None
        self.MaxStrategy = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.VersionName = params.get("VersionName")
        self.Strategy = params.get("Strategy")
        self.MaxStrategy = params.get("MaxStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceEnvironmentStrategyStatus(AbstractModel):
    """环境绑定策略列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 限流策略数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param EnvironmentList: 限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentList: list of ServiceEnvironmentStrategy
        """
        self.TotalCount = None
        self.EnvironmentList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self.EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = ServiceEnvironmentStrategy()
                obj._deserialize(item)
                self.EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceParameter(AbstractModel):
    """ServiceParameter

    """

    def __init__(self):
        r"""
        :param Name: API的后端服务参数名称。只有ServiceType是HTTP才会用到此参数。前后端参数名称可不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Position: API 的后端服务参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。前后端参数位置可配置不同。
注意：此字段可能返回 null，表示取不到有效值。
        :type Position: str
        :param RelevantRequestParameterPosition: API 的后端服务参数对应的前端参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterPosition: str
        :param RelevantRequestParameterName: API 的后端服务参数对应的前端参数名称。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterName: str
        :param DefaultValue: API 的后端服务参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type DefaultValue: str
        :param RelevantRequestParameterDesc: API 的后端服务参数备注。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterDesc: str
        :param RelevantRequestParameterType: API 的后端服务参数类型。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。
        :type RelevantRequestParameterType: str
        """
        self.Name = None
        self.Position = None
        self.RelevantRequestParameterPosition = None
        self.RelevantRequestParameterName = None
        self.DefaultValue = None
        self.RelevantRequestParameterDesc = None
        self.RelevantRequestParameterType = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Position = params.get("Position")
        self.RelevantRequestParameterPosition = params.get("RelevantRequestParameterPosition")
        self.RelevantRequestParameterName = params.get("RelevantRequestParameterName")
        self.DefaultValue = params.get("DefaultValue")
        self.RelevantRequestParameterDesc = params.get("RelevantRequestParameterDesc")
        self.RelevantRequestParameterType = params.get("RelevantRequestParameterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseHistory(AbstractModel):
    """服务发布历史

    """

    def __init__(self):
        r"""
        :param TotalCount: 发布版本总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param VersionList: 历史版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionList: list of ServiceReleaseHistoryInfo
        """
        self.TotalCount = None
        self.VersionList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VersionList") is not None:
            self.VersionList = []
            for item in params.get("VersionList"):
                obj = ServiceReleaseHistoryInfo()
                obj._deserialize(item)
                self.VersionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseHistoryInfo(AbstractModel):
    """服务发布列表详情

    """

    def __init__(self):
        r"""
        :param VersionName: 版本号。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param VersionDesc: 版本描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionDesc: str
        :param ReleaseTime: 版本发布时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReleaseTime: str
        """
        self.VersionName = None
        self.VersionDesc = None
        self.ReleaseTime = None


    def _deserialize(self, params):
        self.VersionName = params.get("VersionName")
        self.VersionDesc = params.get("VersionDesc")
        self.ReleaseTime = params.get("ReleaseTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceReleaseVersion(AbstractModel):
    """服务发布版本

    """

    def __init__(self):
        r"""
        :param TotalCount: 发布版本总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param VersionList: 发布版本列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionList: list of DescribeServiceReleaseVersionResultVersionListInfo
        """
        self.TotalCount = None
        self.VersionList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VersionList") is not None:
            self.VersionList = []
            for item in params.get("VersionList"):
                obj = DescribeServiceReleaseVersionResultVersionListInfo()
                obj._deserialize(item)
                self.VersionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceSubDomainMappings(AbstractModel):
    """服务自定义域名路径映射

    """

    def __init__(self):
        r"""
        :param IsDefaultMapping: 是否使用默认路径映射，为 True 表示使用默认路径映射；为 False 的话，表示使用自定义路径映射，此时 PathMappingSet 不为空。
        :type IsDefaultMapping: bool
        :param PathMappingSet: 自定义路径映射列表。
        :type PathMappingSet: list of PathMapping
        """
        self.IsDefaultMapping = None
        self.PathMappingSet = None


    def _deserialize(self, params):
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        if params.get("PathMappingSet") is not None:
            self.PathMappingSet = []
            for item in params.get("PathMappingSet"):
                obj = PathMapping()
                obj._deserialize(item)
                self.PathMappingSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceUsagePlanSet(AbstractModel):
    """服务绑定使用计划列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 服务上绑定的使用计划总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ServiceUsagePlanList: 服务上绑定的使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceUsagePlanList: list of ApiUsagePlan
        """
        self.TotalCount = None
        self.ServiceUsagePlanList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceUsagePlanList") is not None:
            self.ServiceUsagePlanList = []
            for item in params.get("ServiceUsagePlanList"):
                obj = ApiUsagePlan()
                obj._deserialize(item)
                self.ServiceUsagePlanList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServicesStatus(AbstractModel):
    """服务列表展示

    """

    def __init__(self):
        r"""
        :param TotalCount: 服务列表总数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param ServiceSet: 服务列表详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceSet: list of Service
        """
        self.TotalCount = None
        self.ServiceSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceSet") is not None:
            self.ServiceSet = []
            for item in params.get("ServiceSet"):
                obj = Service()
                obj._deserialize(item)
                self.ServiceSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """API绑定的标签信息。

    """

    def __init__(self):
        r"""
        :param Key: 标签的 key。
        :type Key: str
        :param Value: 便签的 value。
        :type Value: str
        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetServicesReq(AbstractModel):
    """tsf serverless入参

    """

    def __init__(self):
        r"""
        :param VmIp: vm ip
        :type VmIp: str
        :param VpcId: vpc id
        :type VpcId: str
        :param VmPort: vm port
        :type VmPort: int
        :param HostIp: cvm所在宿主机ip
        :type HostIp: str
        :param DockerIp: docker ip
        :type DockerIp: str
        """
        self.VmIp = None
        self.VpcId = None
        self.VmPort = None
        self.HostIp = None
        self.DockerIp = None


    def _deserialize(self, params):
        self.VmIp = params.get("VmIp")
        self.VpcId = params.get("VpcId")
        self.VmPort = params.get("VmPort")
        self.HostIp = params.get("HostIp")
        self.DockerIp = params.get("DockerIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TsfLoadBalanceConfResp(AbstractModel):
    """TsfLoadBalanceConf 出参使用

    """

    def __init__(self):
        r"""
        :param IsLoadBalance: 是否开启负载均衡。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsLoadBalance: bool
        :param Method: 负载均衡方式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param SessionStickRequired: 是否开启会话保持。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionStickRequired: bool
        :param SessionStickTimeout: 会话保持超时时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionStickTimeout: int
        """
        self.IsLoadBalance = None
        self.Method = None
        self.SessionStickRequired = None
        self.SessionStickTimeout = None


    def _deserialize(self, params):
        self.IsLoadBalance = params.get("IsLoadBalance")
        self.Method = params.get("Method")
        self.SessionStickRequired = params.get("SessionStickRequired")
        self.SessionStickTimeout = params.get("SessionStickTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindEnvironmentRequest(AbstractModel):
    """UnBindEnvironment请求参数结构体

    """

    def __init__(self):
        r"""
        :param BindType: 绑定类型，取值为 API、SERVICE，默认值为 SERVICE。
        :type BindType: str
        :param UsagePlanIds: 待绑定的使用计划唯一 ID 列表。
        :type UsagePlanIds: list of str
        :param Environment: 待解绑的服务环境。
        :type Environment: str
        :param ServiceId: 待解绑的服务唯一 ID。
        :type ServiceId: str
        :param ApiIds: API 唯一 ID 数组，当 BindType=API 时，需要传入此参数。
        :type ApiIds: list of str
        """
        self.BindType = None
        self.UsagePlanIds = None
        self.Environment = None
        self.ServiceId = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.BindType = params.get("BindType")
        self.UsagePlanIds = params.get("UsagePlanIds")
        self.Environment = params.get("Environment")
        self.ServiceId = params.get("ServiceId")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindEnvironmentResponse(AbstractModel):
    """UnBindEnvironment返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindIPStrategyRequest(AbstractModel):
    """UnBindIPStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待解绑的服务唯一ID。
        :type ServiceId: str
        :param StrategyId: 待解绑的IP策略唯一ID。
        :type StrategyId: str
        :param EnvironmentName: 待解绑的环境。
        :type EnvironmentName: str
        :param UnBindApiIds: 待解绑的 API 列表。
        :type UnBindApiIds: list of str
        """
        self.ServiceId = None
        self.StrategyId = None
        self.EnvironmentName = None
        self.UnBindApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.StrategyId = params.get("StrategyId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.UnBindApiIds = params.get("UnBindApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindIPStrategyResponse(AbstractModel):
    """UnBindIPStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindSecretIdsRequest(AbstractModel):
    """UnBindSecretIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 待解绑的使用计划唯一 ID。
        :type UsagePlanId: str
        :param AccessKeyIds: 待解绑的密钥 ID 数组。
        :type AccessKeyIds: list of str
        """
        self.UsagePlanId = None
        self.AccessKeyIds = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.AccessKeyIds = params.get("AccessKeyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindSecretIdsResponse(AbstractModel):
    """UnBindSecretIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindSubDomainRequest(AbstractModel):
    """UnBindSubDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 服务唯一 ID。
        :type ServiceId: str
        :param SubDomain: 待解绑的自定义的域名。
        :type SubDomain: str
        """
        self.ServiceId = None
        self.SubDomain = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.SubDomain = params.get("SubDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnBindSubDomainResponse(AbstractModel):
    """UnBindSubDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 解绑自定义域名操作是否成功。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnReleaseServiceRequest(AbstractModel):
    """UnReleaseService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待下线服务的唯一 ID。
        :type ServiceId: str
        :param EnvironmentName: 待下线的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。
        :type EnvironmentName: str
        :param ApiIds: 保留字段，待下线的API列表。
        :type ApiIds: list of str
        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.ApiIds = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.ApiIds = params.get("ApiIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnReleaseServiceResponse(AbstractModel):
    """UnReleaseService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 下线操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnbindApiAppRequest(AbstractModel):
    """UnbindApiApp请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiAppId: 待绑定的应用唯一 ID 。
        :type ApiAppId: str
        :param Environment: 待绑定的环境。
        :type Environment: str
        :param ServiceId: 待绑定的服务唯一 ID。
        :type ServiceId: str
        :param ApiId: 待绑定的API唯一ID。
        :type ApiId: str
        """
        self.ApiAppId = None
        self.Environment = None
        self.ServiceId = None
        self.ApiId = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.Environment = params.get("Environment")
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnbindApiAppResponse(AbstractModel):
    """UnbindApiApp返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 解除绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiAppKeyRequest(AbstractModel):
    """UpdateApiAppKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param ApiAppId: 应用唯一 ID。
        :type ApiAppId: str
        :param ApiAppKey: 应用的Key。
        :type ApiAppKey: str
        :param ApiAppSecret: 应用的Secret。
        :type ApiAppSecret: str
        """
        self.ApiAppId = None
        self.ApiAppKey = None
        self.ApiAppSecret = None


    def _deserialize(self, params):
        self.ApiAppId = params.get("ApiAppId")
        self.ApiAppKey = params.get("ApiAppKey")
        self.ApiAppSecret = params.get("ApiAppSecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiAppKeyResponse(AbstractModel):
    """UpdateApiAppKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 更新操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiKeyRequest(AbstractModel):
    """UpdateApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessKeyId: 待更换的密钥 ID。
        :type AccessKeyId: str
        :param AccessKeySecret: 待更换的密钥 Key，更新自定义密钥时，该字段为必传。长度10 - 50字符，包括字母、数字、英文下划线。
        :type AccessKeySecret: str
        """
        self.AccessKeyId = None
        self.AccessKeySecret = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.AccessKeySecret = params.get("AccessKeySecret")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateApiKeyResponse(AbstractModel):
    """UpdateApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 更换后的密钥详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiKey()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class UpdateServiceRequest(AbstractModel):
    """UpdateService请求参数结构体

    """

    def __init__(self):
        r"""
        :param ServiceId: 待切换服务的唯一 Id。
        :type ServiceId: str
        :param EnvironmentName: 待切换的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。
        :type EnvironmentName: str
        :param VersionName: 切换的版本号。
        :type VersionName: str
        :param UpdateDesc: 本次的切换描述。
        :type UpdateDesc: str
        """
        self.ServiceId = None
        self.EnvironmentName = None
        self.VersionName = None
        self.UpdateDesc = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.EnvironmentName = params.get("EnvironmentName")
        self.VersionName = params.get("VersionName")
        self.UpdateDesc = params.get("UpdateDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateServiceResponse(AbstractModel):
    """UpdateService返回参数结构体

    """

    def __init__(self):
        r"""
        :param Result: 切换版本操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpstreamHealthChecker(AbstractModel):
    """后端通道健康检查参数配置

    """

    def __init__(self):
        r"""
        :param EnableActiveCheck: 标识是否开启主动健康检查。
        :type EnableActiveCheck: bool
        :param EnablePassiveCheck: 标识是否开启被动健康检查。
        :type EnablePassiveCheck: bool
        :param HealthyHttpStatus: 健康检查时，判断为成功请求的 HTTP 状态码。
        :type HealthyHttpStatus: str
        :param UnhealthyHttpStatus: 健康检查时，判断为失败请求的 HTTP 状态码。
        :type UnhealthyHttpStatus: str
        :param TcpFailureThreshold: TCP连续错误阈值。0 表示禁用 TCP 检查。取值范围：[0, 254]。
        :type TcpFailureThreshold: int
        :param TimeoutThreshold: 连续超时阈值。0 表示禁用超时检查。取值范围：[0, 254]。
        :type TimeoutThreshold: int
        :param HttpFailureThreshold: HTTP连续错误阈值。0 表示禁用HTTP检查。取值范围：[0, 254]。
        :type HttpFailureThreshold: int
        :param ActiveCheckHttpPath: 主动健康检查时探测请求的路径。默认为"/"。
        :type ActiveCheckHttpPath: str
        :param ActiveCheckTimeout: 主动健康检查的探测请求超时，单位秒。默认为5秒。
        :type ActiveCheckTimeout: int
        :param ActiveCheckInterval: 主动健康检查的时间间隔，默认5秒。
        :type ActiveCheckInterval: int
        :param ActiveRequestHeader: 主动健康检查时探测请求的的请求头。
        :type ActiveRequestHeader: list of UpstreamHealthCheckerReqHeaders
        :param UnhealthyTimeout: 异常节点的状态自动恢复时间，单位秒。当只开启被动检查的话，必须设置为 > 0 的值，否则被动异常节点将无法恢复。默认30秒。
        :type UnhealthyTimeout: int
        """
        self.EnableActiveCheck = None
        self.EnablePassiveCheck = None
        self.HealthyHttpStatus = None
        self.UnhealthyHttpStatus = None
        self.TcpFailureThreshold = None
        self.TimeoutThreshold = None
        self.HttpFailureThreshold = None
        self.ActiveCheckHttpPath = None
        self.ActiveCheckTimeout = None
        self.ActiveCheckInterval = None
        self.ActiveRequestHeader = None
        self.UnhealthyTimeout = None


    def _deserialize(self, params):
        self.EnableActiveCheck = params.get("EnableActiveCheck")
        self.EnablePassiveCheck = params.get("EnablePassiveCheck")
        self.HealthyHttpStatus = params.get("HealthyHttpStatus")
        self.UnhealthyHttpStatus = params.get("UnhealthyHttpStatus")
        self.TcpFailureThreshold = params.get("TcpFailureThreshold")
        self.TimeoutThreshold = params.get("TimeoutThreshold")
        self.HttpFailureThreshold = params.get("HttpFailureThreshold")
        self.ActiveCheckHttpPath = params.get("ActiveCheckHttpPath")
        self.ActiveCheckTimeout = params.get("ActiveCheckTimeout")
        self.ActiveCheckInterval = params.get("ActiveCheckInterval")
        if params.get("ActiveRequestHeader") is not None:
            self.ActiveRequestHeader = []
            for item in params.get("ActiveRequestHeader"):
                obj = UpstreamHealthCheckerReqHeaders()
                obj._deserialize(item)
                self.ActiveRequestHeader.append(obj)
        self.UnhealthyTimeout = params.get("UnhealthyTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param UpstreamId: 后端通道唯一ID
        :type UpstreamId: str
        :param UpstreamName: 后端通道名字
        :type UpstreamName: str
        :param UpstreamDescription: 后端通道描述
        :type UpstreamDescription: str
        :param Scheme: 后端协议，取值范围：HTTP, HTTPS
        :type Scheme: str
        :param Algorithm: 负载均衡算法，取值范围：ROUND_ROBIN
        :type Algorithm: str
        :param UniqVpcId: VPC唯一ID
        :type UniqVpcId: str
        :param Retries: 请求重试次数
        :type Retries: int
        :param Nodes: 后端节点
        :type Nodes: list of UpstreamNode
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        :param HealthChecker: 健康检查配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthChecker: :class:`tencentcloud.apigateway.v20180808.models.UpstreamHealthChecker`
        :param UpstreamType: 后端的类型，取值范围：IP_PORT, K8S
        :type UpstreamType: str
        :param K8sServices: K8S容器服务配置
注意：此字段可能返回 null，表示取不到有效值。
        :type K8sServices: list of K8sService
        :param UpstreamHost: 网关转发给后端的Host请求头
注意：此字段可能返回 null，表示取不到有效值。
        :type UpstreamHost: str
        """
        self.UpstreamId = None
        self.UpstreamName = None
        self.UpstreamDescription = None
        self.Scheme = None
        self.Algorithm = None
        self.UniqVpcId = None
        self.Retries = None
        self.Nodes = None
        self.CreatedTime = None
        self.Tags = None
        self.HealthChecker = None
        self.UpstreamType = None
        self.K8sServices = None
        self.UpstreamHost = None


    def _deserialize(self, params):
        self.UpstreamId = params.get("UpstreamId")
        self.UpstreamName = params.get("UpstreamName")
        self.UpstreamDescription = params.get("UpstreamDescription")
        self.Scheme = params.get("Scheme")
        self.Algorithm = params.get("Algorithm")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Retries = params.get("Retries")
        if params.get("Nodes") is not None:
            self.Nodes = []
            for item in params.get("Nodes"):
                obj = UpstreamNode()
                obj._deserialize(item)
                self.Nodes.append(obj)
        self.CreatedTime = params.get("CreatedTime")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("HealthChecker") is not None:
            self.HealthChecker = UpstreamHealthChecker()
            self.HealthChecker._deserialize(params.get("HealthChecker"))
        self.UpstreamType = params.get("UpstreamType")
        if params.get("K8sServices") is not None:
            self.K8sServices = []
            for item in params.get("K8sServices"):
                obj = K8sService()
                obj._deserialize(item)
                self.K8sServices.append(obj)
        self.UpstreamHost = params.get("UpstreamHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpstreamNode(AbstractModel):
    """后端通道后端节点元数据

    """

    def __init__(self):
        r"""
        :param Host: IP或域名
        :type Host: str
        :param Port: 端口[0, 65535]
        :type Port: int
        :param Weight: 权重[0, 100], 0为禁用
        :type Weight: int
        :param VmInstanceId: CVM实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type VmInstanceId: str
        :param Tags: 染色标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param Healthy: 节点健康状态，创建、编辑时不需要传该参数。OFF：关闭，HEALTHY：健康，UNHEALTHY：异常，NO_DATA：数据未上报。目前只支持VPC通道。
注意：此字段可能返回 null，表示取不到有效值。
        :type Healthy: str
        :param ServiceName: K8S容器服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        :param NameSpace: K8S命名空间
注意：此字段可能返回 null，表示取不到有效值。
        :type NameSpace: str
        :param ClusterId: TKE集群的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClusterId: str
        :param Source: Node的来源，取值范围：K8S
注意：此字段可能返回 null，表示取不到有效值。
        :type Source: str
        :param UniqueServiceName: API网关内部记录唯一的服务名字
注意：此字段可能返回 null，表示取不到有效值。
        :type UniqueServiceName: str
        """
        self.Host = None
        self.Port = None
        self.Weight = None
        self.VmInstanceId = None
        self.Tags = None
        self.Healthy = None
        self.ServiceName = None
        self.NameSpace = None
        self.ClusterId = None
        self.Source = None
        self.UniqueServiceName = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.VmInstanceId = params.get("VmInstanceId")
        self.Tags = params.get("Tags")
        self.Healthy = params.get("Healthy")
        self.ServiceName = params.get("ServiceName")
        self.NameSpace = params.get("NameSpace")
        self.ClusterId = params.get("ClusterId")
        self.Source = params.get("Source")
        self.UniqueServiceName = params.get("UniqueServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlan(AbstractModel):
    """usagePlan详情

    """

    def __init__(self):
        r"""
        :param Environment: 环境名称。
        :type Environment: str
        :param UsagePlanId: 使用计划唯一ID。
        :type UsagePlanId: str
        :param UsagePlanName: 使用计划名称。
        :type UsagePlanName: str
        :param UsagePlanDesc: 使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param MaxRequestNumPreSec: 使用计划qps，-1表示没有限制。
        :type MaxRequestNumPreSec: int
        :param CreatedTime: 使用计划时间。
        :type CreatedTime: str
        :param ModifiedTime: 使用计划修改时间。
        :type ModifiedTime: str
        """
        self.Environment = None
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNumPreSec = None
        self.CreatedTime = None
        self.ModifiedTime = None


    def _deserialize(self, params):
        self.Environment = params.get("Environment")
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindEnvironment(AbstractModel):
    """使用计划绑定环境信息

    """

    def __init__(self):
        r"""
        :param EnvironmentName: 环境名。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentName: str
        :param ServiceId: 服务唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        """
        self.EnvironmentName = None
        self.ServiceId = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.ServiceId = params.get("ServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindSecret(AbstractModel):
    """使用计划绑定密钥

    """

    def __init__(self):
        r"""
        :param AccessKeyId: 密钥ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKeyId: str
        :param SecretName: 密钥名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param Status: 密钥状态，0表示已禁用，1表示启用中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.AccessKeyId = None
        self.SecretName = None
        self.Status = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")
        self.SecretName = params.get("SecretName")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanBindSecretStatus(AbstractModel):
    """使用计划绑定密钥列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 使用计划绑定密钥的数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param AccessKeyList: 密钥详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKeyList: list of UsagePlanBindSecret
        """
        self.TotalCount = None
        self.AccessKeyList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccessKeyList") is not None:
            self.AccessKeyList = []
            for item in params.get("AccessKeyList"):
                obj = UsagePlanBindSecret()
                obj._deserialize(item)
                self.AccessKeyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanEnvironment(AbstractModel):
    """使用计划绑定环境详情。

    """

    def __init__(self):
        r"""
        :param ServiceId: 绑定的服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceId: str
        :param ApiId: API 的唯一ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param ApiName: API 的名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiName: str
        :param Path: API 的路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Method: API 的方法。
注意：此字段可能返回 null，表示取不到有效值。
        :type Method: str
        :param Environment: 已经绑定的环境名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Environment: str
        :param InUseRequestNum: 已经使用的配额。
注意：此字段可能返回 null，表示取不到有效值。
        :type InUseRequestNum: int
        :param MaxRequestNum: 最大请求量。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param MaxRequestNumPreSec: 每秒最大请求次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceName: str
        """
        self.ServiceId = None
        self.ApiId = None
        self.ApiName = None
        self.Path = None
        self.Method = None
        self.Environment = None
        self.InUseRequestNum = None
        self.MaxRequestNum = None
        self.MaxRequestNumPreSec = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ApiId = params.get("ApiId")
        self.ApiName = params.get("ApiName")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.Environment = params.get("Environment")
        self.InUseRequestNum = params.get("InUseRequestNum")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanEnvironmentStatus(AbstractModel):
    """使用计划绑定环境的列表。

    """

    def __init__(self):
        r"""
        :param TotalCount: 使用计划绑定的服务的环境数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param EnvironmentList: 使用计划已经绑定的各个服务的环境状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type EnvironmentList: list of UsagePlanEnvironment
        """
        self.TotalCount = None
        self.EnvironmentList = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("EnvironmentList") is not None:
            self.EnvironmentList = []
            for item in params.get("EnvironmentList"):
                obj = UsagePlanEnvironment()
                obj._deserialize(item)
                self.EnvironmentList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanInfo(AbstractModel):
    """使用计划详情。

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 使用计划唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanId: str
        :param UsagePlanName: 使用计划名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanName: str
        :param UsagePlanDesc: 使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param MaxRequestNumPreSec: 每秒请求限制数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param MaxRequestNum: 最大调用次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        :param BindSecretIdTotalCount: 绑定密钥的数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindSecretIdTotalCount: int
        :param BindSecretIds: 绑定密钥的详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindSecretIds: list of str
        :param BindEnvironmentTotalCount: 绑定环境数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindEnvironmentTotalCount: int
        :param BindEnvironments: 绑定环境详情。
注意：此字段可能返回 null，表示取不到有效值。
        :type BindEnvironments: list of UsagePlanBindEnvironment
        """
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNumPreSec = None
        self.MaxRequestNum = None
        self.CreatedTime = None
        self.ModifiedTime = None
        self.BindSecretIdTotalCount = None
        self.BindSecretIds = None
        self.BindEnvironmentTotalCount = None
        self.BindEnvironments = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        self.BindSecretIdTotalCount = params.get("BindSecretIdTotalCount")
        self.BindSecretIds = params.get("BindSecretIds")
        self.BindEnvironmentTotalCount = params.get("BindEnvironmentTotalCount")
        if params.get("BindEnvironments") is not None:
            self.BindEnvironments = []
            for item in params.get("BindEnvironments"):
                obj = UsagePlanBindEnvironment()
                obj._deserialize(item)
                self.BindEnvironments.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlanStatusInfo(AbstractModel):
    """用于使用计划列表展示

    """

    def __init__(self):
        r"""
        :param UsagePlanId: 使用计划唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanId: str
        :param UsagePlanName: 用户自定义的使用计划名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanName: str
        :param UsagePlanDesc: 用户自定义的使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param MaxRequestNumPreSec: 每秒最大请求次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param MaxRequestNum: 请求配额总量，-1表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifiedTime: str
        """
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.MaxRequestNumPreSec = None
        self.MaxRequestNum = None
        self.CreatedTime = None
        self.ModifiedTime = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")
        self.UsagePlanName = params.get("UsagePlanName")
        self.UsagePlanDesc = params.get("UsagePlanDesc")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsagePlansStatus(AbstractModel):
    """使用计划列表

    """

    def __init__(self):
        r"""
        :param TotalCount: 符合条件的使用计划数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param UsagePlanStatusSet: 使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanStatusSet: list of UsagePlanStatusInfo
        """
        self.TotalCount = None
        self.UsagePlanStatusSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("UsagePlanStatusSet") is not None:
            self.UsagePlanStatusSet = []
            for item in params.get("UsagePlanStatusSet"):
                obj = UsagePlanStatusInfo()
                obj._deserialize(item)
                self.UsagePlanStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcConfig(AbstractModel):
    """独享实例vpc配置信息

    """

    def __init__(self):
        r"""
        :param UniqVpcId: vpcid
        :type UniqVpcId: str
        :param UniqSubnetId: subnetid
        :type UniqSubnetId: str
        """
        self.UniqVpcId = None
        self.UniqSubnetId = None


    def _deserialize(self, params):
        self.UniqVpcId = params.get("UniqVpcId")
        self.UniqSubnetId = params.get("UniqSubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        