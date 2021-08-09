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
        """
        :param ApiDocId: API文档ID\n        :type ApiDocId: str\n        :param ApiDocName: API文档名称\n        :type ApiDocName: str\n        :param ApiDocStatus: API文档构建状态\n        :type ApiDocStatus: str\n        """
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
        """
        :param ApiDocId: API文档ID\n        :type ApiDocId: str\n        :param ApiDocName: API文档名称\n        :type ApiDocName: str\n        :param ApiDocStatus: API文档构建状态\n        :type ApiDocStatus: str\n        :param ApiCount: API文档API数量\n        :type ApiCount: int\n        :param ViewCount: API文档查看次数\n        :type ViewCount: int\n        :param ReleaseCount: API文档发布次数\n        :type ReleaseCount: int\n        :param ApiDocUri: API文档访问URI\n        :type ApiDocUri: str\n        :param SharePassword: API文档分享密码\n        :type SharePassword: str\n        :param UpdatedTime: API文档更新时间\n        :type UpdatedTime: str\n        :param ServiceId: 服务ID\n        :type ServiceId: str\n        :param Environment: 环境信息\n        :type Environment: str\n        :param ApiIds: 生成API文档的API ID\n        :type ApiIds: list of str\n        :param ServiceName: 服务名称\n        :type ServiceName: str\n        :param ApiNames: 生成API文档的API名称\n        :type ApiNames: list of str\n        """
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
        """
        :param TotalCount: API文档数量\n        :type TotalCount: int\n        :param APIDocSet: API文档基本信息\n        :type APIDocSet: list of APIDoc\n        """
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
        """
        :param ApiAppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAppName: str\n        :param ApiAppId: 应用ID\n        :type ApiAppId: str\n        :param ApiId: Api的ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiId: str\n        :param ApiName: Api名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiName: str\n        :param ServiceId: 服务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceId: str\n        :param AuthorizedTime: 授权绑定时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuthorizedTime: str\n        :param ApiRegion: Api所属地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiRegion: str\n        :param EnvironmentName: 授权绑定的环境
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvironmentName: str\n        """
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
        """
        :param TotalCount: 数量\n        :type TotalCount: int\n        :param ApiAppApiSet: 应用绑定的Api信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAppApiSet: list of ApiAppApiInfo\n        """
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
        """
        :param ApiAppName: 应用名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAppName: str\n        :param ApiAppId: 应用ID\n        :type ApiAppId: str\n        :param ApiAppSecret: 应用SECRET
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAppSecret: str\n        :param ApiAppDesc: 应用描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAppDesc: str\n        :param CreatedTime: 创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 修改时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param ApiAppKey: 应用KEY
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAppKey: str\n        """
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
        """
        :param TotalCount: 应用数量\n        :type TotalCount: int\n        :param ApiAppSet: 应用信息数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiAppSet: list of ApiAppInfo\n        """
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
        """
        :param ApiId: API唯一ID。\n        :type ApiId: str\n        :param ApiName: 用户自定义API名称。\n        :type ApiName: str\n        :param Path: API的路径。如/path。\n        :type Path: str\n        :param Method: API的方法。如GET。\n        :type Method: str\n        :param EnvironmentStrategySet: 环境的限流信息。\n        :type EnvironmentStrategySet: list of EnvironmentStrategy\n        """
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
        """
        :param TotalCount: API绑定的限流策略数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param ApiEnvironmentStrategySet: API绑定的限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiEnvironmentStrategySet: list of ApiEnvironmentStrategy\n        """
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
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param ApiId: API唯一ID。\n        :type ApiId: str\n        :param ApiDesc: API描述\n        :type ApiDesc: str\n        :param Path: API PATH。\n        :type Path: str\n        :param Method: API METHOD。\n        :type Method: str\n        :param CreatedTime: 服务创建时间。\n        :type CreatedTime: str\n        :param ModifiedTime: 服务修改时间。\n        :type ModifiedTime: str\n        :param ApiName: API名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiName: str\n        :param UniqVpcId: VPC唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UniqVpcId: str\n        :param ApiType: API类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiType: str\n        :param Protocol: API协议。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param IsDebugAfterCharge: 是否买后调试。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDebugAfterCharge: bool\n        :param AuthType: 授权类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuthType: str\n        :param ApiBusinessType: API业务类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiBusinessType: str\n        :param AuthRelationApiId: 关联授权API唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuthRelationApiId: str\n        :param RelationBuniessApiIds: 授权API关联的业务API列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelationBuniessApiIds: list of str\n        :param OauthConfig: oauth配置信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param TokenLocation: oauth2.0API请求，token存放位置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TokenLocation: str\n        """
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
        """
        :param ServiceId: API 所在的服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceId: str\n        :param ServiceName: API 所在的服务的名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceName: str\n        :param ServiceDesc: API 所在的服务的描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceDesc: str\n        :param ApiId: API 接口唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiId: str\n        :param ApiDesc: API 接口的描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiDesc: str\n        :param CreatedTime: 创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 最后修改时间，按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param ApiName: API 接口的名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiName: str\n        :param ApiType: API 类型。可取值为NORMAL（普通API）、TSF（微服务API）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiType: str\n        :param Protocol: API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param AuthType: API 鉴权类型。可取值为 SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuthType: str\n        :param ApiBusinessType: OAUTH API的类型。可取值为NORMAL（业务API）、OAUTH（授权API）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiBusinessType: str\n        :param AuthRelationApiId: OAUTH 业务API 关联的授权API 唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuthRelationApiId: str\n        :param OauthConfig: OAUTH配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param IsDebugAfterCharge: 是否购买后调试（云市场预留参数）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDebugAfterCharge: bool\n        :param RequestConfig: 请求的前端配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`\n        :param ResponseType: 返回类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseType: str\n        :param ResponseSuccessExample: 自定义响应配置成功响应示例。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseSuccessExample: str\n        :param ResponseFailExample: 自定义响应配置失败响应示例。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseFailExample: str\n        :param ResponseErrorCodes: 用户自定义错误码配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseErrorCodes: list of ErrorCodes\n        :param RequestParameters: 前端请求参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RequestParameters: list of ReqParameter\n        :param ServiceTimeout: API 的后端服务超时时间，单位是秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceTimeout: int\n        :param ServiceType: API 的后端服务类型。可取值为 HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceType: str\n        :param ServiceConfig: API 的后端服务配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`\n        :param ServiceParameters: API的后端服务参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceParameters: list of ServiceParameter\n        :param ConstantParameters: 常量参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConstantParameters: list of ConstantParameter\n        :param ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceMockReturnMessage: str\n        :param ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceScfFunctionName: str\n        :param ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceScfFunctionNamespace: str\n        :param ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceScfFunctionQualifier: str\n        :param ServiceScfIsIntegratedResponse: 是否开启集成响应。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceScfIsIntegratedResponse: bool\n        :param ServiceWebsocketRegisterFunctionName: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketRegisterFunctionName: str\n        :param ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketRegisterFunctionNamespace: str\n        :param ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketRegisterFunctionQualifier: str\n        :param ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketCleanupFunctionName: str\n        :param ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketCleanupFunctionNamespace: str\n        :param ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketCleanupFunctionQualifier: str\n        :param InternalDomain: WEBSOCKET 回推地址。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InternalDomain: str\n        :param ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketTransportFunctionName: str\n        :param ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketTransportFunctionNamespace: str\n        :param ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceWebsocketTransportFunctionQualifier: str\n        :param MicroServices: API绑定微服务服务列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroServices: list of MicroService\n        :param MicroServicesInfo: 微服务信息详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MicroServicesInfo: list of int\n        :param ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`\n        :param ServiceTsfHealthCheckConf: 微服务的健康检查配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param EnableCORS: 是否开启跨域。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnableCORS: bool\n        :param Tags: API绑定的tag信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param Environments: API已发布的环境信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Environments: list of str\n        :param IsBase64Encoded: 是否开启Base64编码，只有后端为scf时才会生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsBase64Encoded: bool\n        :param IsBase64Trigger: 是否开启Base64编码的header触发，只有后端为scf时才会生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsBase64Trigger: bool\n        :param Base64EncodedTriggerRules: Header触发规则，总规则数量不超过10。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule\n        """
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
                obj = ServiceParameter()
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
        """
        :param TotalCount: 插件相关的API总数。\n        :type TotalCount: int\n        :param ApiSet: 插件相关的API信息。\n        :type ApiSet: list of AvailableApiInfo\n        """
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
        """
        :param AccessKeyId: 创建的 API 密钥 ID 。\n        :type AccessKeyId: str\n        :param AccessKeySecret: 创建的 API 密钥 Key。\n        :type AccessKeySecret: str\n        :param AccessKeyType: 密钥类型，auto 或者 manual。\n        :type AccessKeyType: str\n        :param SecretName: 用户自定义密钥名称。\n        :type SecretName: str\n        :param ModifiedTime: 最后一次修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。\n        :type ModifiedTime: str\n        :param Status: 密钥状态。0表示禁用，1表示启用。\n        :type Status: int\n        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。\n        :type CreatedTime: str\n        """
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
        """
        :param TotalCount: 符合条件的 API 密钥数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param ApiKeySet: API 密钥列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiKeySet: list of ApiKey\n        """
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
        """
        :param Path: path\n        :type Path: str\n        :param Method: 方法\n        :type Method: str\n        """
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
        """
        :param ServiceId: 服务唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceId: str\n        :param ApiId: API 唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiId: str\n        :param ApiName: API 名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiName: str\n        :param Path: API 路径。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param Method: API 方法。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Method: str\n        :param UsagePlanId: 使用计划的唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanId: str\n        :param UsagePlanName: 使用计划的名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanName: str\n        :param UsagePlanDesc: 使用计划的描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanDesc: str\n        :param Environment: 使用计划绑定的服务环境。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Environment: str\n        :param InUseRequestNum: 已经使用的配额。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InUseRequestNum: int\n        :param MaxRequestNum: 请求配额总量，-1表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRequestNum: int\n        :param MaxRequestNumPreSec: 请求 QPS 上限，-1 表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRequestNumPreSec: int\n        :param CreatedTime: 使用计划创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 使用计划最后修改时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceName: str\n        """
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
        """
        :param TotalCount: API 绑定的使用计划总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param ApiUsagePlanList: API 绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiUsagePlanList: list of ApiUsagePlan\n        """
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
        


class ApisStatus(AbstractModel):
    """描述api列表状态

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的 API 接口数量。\n        :type TotalCount: int\n        :param ApiIdStatusSet: API 接口列表。\n        :type ApiIdStatusSet: list of DesApisStatus\n        """
        self.TotalCount = None
        self.ApiIdStatusSet = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ApiIdStatusSet") is not None:
            self.ApiIdStatusSet = []
            for item in params.get("ApiIdStatusSet"):
                obj = DesApisStatus()
                obj._deserialize(item)
                self.ApiIdStatusSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachPluginRequest(AbstractModel):
    """AttachPlugin请求参数结构体

    """

    def __init__(self):
        """
        :param PluginId: 绑定的API网关插件ID。\n        :type PluginId: str\n        :param ServiceId: 要操作的服务ID。\n        :type ServiceId: str\n        :param EnvironmentName: 要操作API的环境。\n        :type EnvironmentName: str\n        :param ApiIds: 要绑定的API列表。\n        :type ApiIds: list of str\n        """
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
        """
        :param Result: 绑定操作是否成功。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class AttachedApiInfo(AbstractModel):
    """插件绑定的API信息

    """

    def __init__(self):
        """
        :param ServiceId: API所在服务ID。\n        :type ServiceId: str\n        :param ServiceName: API所在服务名称。\n        :type ServiceName: str\n        :param ServiceDesc: API所在服务描述信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceDesc: str\n        :param ApiId: API ID。\n        :type ApiId: str\n        :param ApiName: API名称。\n        :type ApiName: str\n        :param ApiDesc: API描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiDesc: str\n        :param Environment: 插件绑定API的环境。\n        :type Environment: str\n        :param AttachedTime: 插件和API绑定时间。\n        :type AttachedTime: str\n        """
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
        """
        :param TotalCount: 插件绑定的API数量。\n        :type TotalCount: int\n        :param AttachedApis: 插件绑定的API信息。\n        :type AttachedApis: list of AttachedApiInfo\n        """
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
        


class AvailableApiInfo(AbstractModel):
    """插件相关的API信息。

    """

    def __init__(self):
        """
        :param ApiId: API ID。\n        :type ApiId: str\n        :param ApiName: API名称。\n        :type ApiName: str\n        :param ApiType: API类型。\n        :type ApiType: str\n        :param Path: API路径。\n        :type Path: str\n        :param Method: API方法。\n        :type Method: str\n        :param AttachedOtherPlugin: API是否绑定其他插件。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AttachedOtherPlugin: bool\n        :param IsAttached: API是否绑定当前插件。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsAttached: bool\n        """
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
        """
        :param Name: 进行编码触发的header，可选值 "Accept"和"Content_Type" 对应实际数据流请求header中的Accept和 Content-Type。\n        :type Name: str\n        :param Value: 进行编码触发的header的可选值数组, 数组元素的字符串最大长度为40，元素可以包括数字，英文字母以及特殊字符，特殊字符的可选值为： `.`    `+`    `*`   `-`   `/`  `_` 

例如 [
    "application/x-vpeg005",
    "application/xhtml+xml",
    "application/vnd.ms-project",
    "application/vnd.rn-rn_music_package"
] 等都是合法的。\n        :type Value: list of str\n        """
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
        """
        :param ApiAppId: 待绑定的应用唯一 ID 。\n        :type ApiAppId: str\n        :param Environment: 待绑定的环境。\n        :type Environment: str\n        :param ServiceId: 待绑定的服务唯一 ID。\n        :type ServiceId: str\n        :param ApiId: 待绑定的API唯一ID。\n        :type ApiId: str\n        """
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
        """
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindEnvironmentRequest(AbstractModel):
    """BindEnvironment请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanIds: 待绑定的使用计划唯一 ID 列表。\n        :type UsagePlanIds: list of str\n        :param BindType: 绑定类型，取值为API、SERVICE，默认值为SERVICE。\n        :type BindType: str\n        :param Environment: 待绑定的环境。\n        :type Environment: str\n        :param ServiceId: 待绑定的服务唯一 ID。\n        :type ServiceId: str\n        :param ApiIds: API唯一ID数组，当bindType=API时，需要传入此参数。\n        :type ApiIds: list of str\n        """
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
        """
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindIPStrategyRequest(AbstractModel):
    """BindIPStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待绑定的IP策略所属的服务唯一ID。\n        :type ServiceId: str\n        :param StrategyId: 待绑定的IP策略唯一ID。\n        :type StrategyId: str\n        :param EnvironmentName: IP策略待绑定的环境。\n        :type EnvironmentName: str\n        :param BindApiIds: IP策略待绑定的API列表。\n        :type BindApiIds: list of str\n        """
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
        """
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindSecretIdsRequest(AbstractModel):
    """BindSecretIds请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanId: 待绑定的使用计划唯一 ID。\n        :type UsagePlanId: str\n        :param AccessKeyIds: 待绑定的密钥 ID 数组。\n        :type AccessKeyIds: list of str\n        """
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
        """
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BindSubDomainRequest(AbstractModel):
    """BindSubDomain请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一 ID。\n        :type ServiceId: str\n        :param SubDomain: 待绑定的自定义的域名。\n        :type SubDomain: str\n        :param Protocol: 服务支持协议，可选值为http、https、http&https。\n        :type Protocol: str\n        :param NetType: 网络类型，可选值为OUTER、INNER。\n        :type NetType: str\n        :param IsDefaultMapping: 是否使用默认路径映射，默认为 true。为 false 时，表示自定义路径映射，此时 PathMappingSet 必填。\n        :type IsDefaultMapping: bool\n        :param NetSubDomain: 默认域名。\n        :type NetSubDomain: str\n        :param CertificateId: 待绑定自定义域名的证书唯一 ID。针对Protocol 为https或http&https可以选择上传。\n        :type CertificateId: str\n        :param PathMappingSet: 自定义域名路径映射，最多输入三个Environment，并且只能分别取值“test”、 ”prepub“、”release“。\n        :type PathMappingSet: list of PathMapping\n        :param IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。\n        :type IsForcedHttps: bool\n        """
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
        """
        :param Result: 绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class BuildAPIDocRequest(AbstractModel):
    """BuildAPIDoc请求参数结构体

    """

    def __init__(self):
        """
        :param ApiDocId: API文档ID\n        :type ApiDocId: str\n        """
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
        """
        :param Result: 操作是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ConstantParameter(AbstractModel):
    """常量参数

    """

    def __init__(self):
        """
        :param Name: 常量参数名称。只有 ServiceType 是 HTTP 才会用到此参数。\n        :type Name: str\n        :param Desc: 常量参数描述。只有 ServiceType 是 HTTP 才会用到此参数。\n        :type Desc: str\n        :param Position: 常量参数位置。只有 ServiceType 是 HTTP 才会用到此参数。\n        :type Position: str\n        :param DefaultValue: 常量参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。\n        :type DefaultValue: str\n        """
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
        


class CreateAPIDocRequest(AbstractModel):
    """CreateAPIDoc请求参数结构体

    """

    def __init__(self):
        """
        :param ApiDocName: API文档名称\n        :type ApiDocName: str\n        :param ServiceId: 服务名称\n        :type ServiceId: str\n        :param Environment: 环境名称\n        :type Environment: str\n        :param ApiIds: 生成文档的API列表\n        :type ApiIds: list of str\n        """
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
        """
        :param Result: API文档基本信息\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ApiAppName: 用户自定义应用名称。\n        :type ApiAppName: str\n        :param ApiAppDesc: 应用描述\n        :type ApiAppDesc: str\n        """
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
        """
        :param Result: 新增的应用详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param SecretName: 用户自定义密钥名称。\n        :type SecretName: str\n        :param AccessKeyType: 密钥类型，支持 auto 和 manual（自定义密钥），默认为 auto。\n        :type AccessKeyType: str\n        :param AccessKeyId: 用户自定义密钥 ID，AccessKeyType 为 manual 时必传。长度为5 - 50字符，由字母、数字、英文下划线组成。\n        :type AccessKeyId: str\n        :param AccessKeySecret: 用户自定义密钥 Key，AccessKeyType 为 manual 时必传。长度为10 - 50字符，由字母、数字、英文下划线。\n        :type AccessKeySecret: str\n        """
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
        """
        :param Result: 新增的密钥详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: API 所在的服务唯一 ID。\n        :type ServiceId: str\n        :param ServiceType: API 的后端服务类型。支持HTTP、MOCK、TSF、SCF、WEBSOCKET、TARGET（内测）。\n        :type ServiceType: str\n        :param ServiceTimeout: API 的后端服务超时时间，单位是秒。\n        :type ServiceTimeout: int\n        :param Protocol: API 的前端请求协议，支持HTTP和WEBSOCKET。\n        :type Protocol: str\n        :param RequestConfig: 请求的前端配置。\n        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.ApiRequestConfig`\n        :param ApiName: 用户自定义的 API 名称。\n        :type ApiName: str\n        :param ApiDesc: 用户自定义的 API 接口描述。\n        :type ApiDesc: str\n        :param ApiType: API 类型，支持NORMAL（普通API）和TSF（微服务API），默认为NORMAL。\n        :type ApiType: str\n        :param AuthType: API 鉴权类型。支持SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH、APP（应用认证）。默认为NONE。\n        :type AuthType: str\n        :param EnableCORS: 是否开启跨域。\n        :type EnableCORS: bool\n        :param ConstantParameters: 常量参数。\n        :type ConstantParameters: list of ConstantParameter\n        :param RequestParameters: 前端请求参数。\n        :type RequestParameters: list of RequestParameter\n        :param ApiBusinessType: 当AuthType 为 OAUTH时，该字段有效， NORMAL：业务api OAUTH：授权API。\n        :type ApiBusinessType: str\n        :param ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。\n        :type ServiceMockReturnMessage: str\n        :param MicroServices: API绑定微服务服务列表。\n        :type MicroServices: list of MicroServiceReq\n        :param ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。\n        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`\n        :param ServiceTsfHealthCheckConf: 微服务的健康检查配置。\n        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param TargetServices: target类型后端资源信息。（内测阶段）\n        :type TargetServices: list of TargetServicesReq\n        :param TargetServicesLoadBalanceConf: target类型负载均衡配置。（内测阶段）\n        :type TargetServicesLoadBalanceConf: int\n        :param TargetServicesHealthCheckConf: target健康检查配置。（内测阶段）\n        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。\n        :type ServiceScfFunctionName: str\n        :param ServiceWebsocketRegisterFunctionName: scf websocket注册函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketRegisterFunctionName: str\n        :param ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketCleanupFunctionName: str\n        :param ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketTransportFunctionName: str\n        :param ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。\n        :type ServiceScfFunctionNamespace: str\n        :param ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。\n        :type ServiceScfFunctionQualifier: str\n        :param ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketRegisterFunctionNamespace: str\n        :param ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketRegisterFunctionQualifier: str\n        :param ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketTransportFunctionNamespace: str\n        :param ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketTransportFunctionQualifier: str\n        :param ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketCleanupFunctionNamespace: str\n        :param ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketCleanupFunctionQualifier: str\n        :param ServiceScfIsIntegratedResponse: 是否开启响应集成。当后端类型是SCF时生效。\n        :type ServiceScfIsIntegratedResponse: bool\n        :param IsDebugAfterCharge: 开始调试后计费。（云市场预留字段）\n        :type IsDebugAfterCharge: bool\n        :param IsDeleteResponseErrorCodes: 是否删除自定义响应配置错误码，如果不传或者传 False，不删除，当传 True 时，则删除此 API 所有自定义响应配置错误码。\n        :type IsDeleteResponseErrorCodes: bool\n        :param ResponseType: 返回类型。\n        :type ResponseType: str\n        :param ResponseSuccessExample: 自定义响应配置成功响应示例。\n        :type ResponseSuccessExample: str\n        :param ResponseFailExample: 自定义响应配置失败响应示例。\n        :type ResponseFailExample: str\n        :param ServiceConfig: API 的后端服务配置。\n        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`\n        :param AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。\n        :type AuthRelationApiId: str\n        :param ServiceParameters: API的后端服务参数。\n        :type ServiceParameters: list of ServiceParameter\n        :param OauthConfig: oauth配置。当AuthType是OAUTH时生效。\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param ResponseErrorCodes: 用户自定义错误码配置。\n        :type ResponseErrorCodes: list of ResponseErrorCodeReq\n        :param TargetNamespaceId: tsf serverless 命名空间ID。（内测中）\n        :type TargetNamespaceId: str\n        :param UserType: 用户类型。\n        :type UserType: str\n        :param IsBase64Encoded: 是否打开Base64编码，只有后端是scf时才会生效。\n        :type IsBase64Encoded: bool\n        :param ServiceScfFunctionType: scf函数类型。当后端类型是SCF时生效。支持事件触发(EVENT)，http直通云函数(HTTP)。\n        :type ServiceScfFunctionType: str\n        """
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
        self.ServiceScfFunctionType = None


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
        self.ServiceScfFunctionType = params.get("ServiceScfFunctionType")
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
        """
        :param Result: api信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRsp`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = CreateApiRsp()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class CreateApiRsp(AbstractModel):
    """创建api返回

    """

    def __init__(self):
        """
        :param ApiId: api id
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiId: str\n        :param Path: path
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param Method: method
注意：此字段可能返回 null，表示取不到有效值。\n        :type Method: str\n        :param CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        """
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
        


class CreateIPStrategyRequest(AbstractModel):
    """CreateIPStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务的唯一ID。\n        :type ServiceId: str\n        :param StrategyName: 用户自定义的策略名称。\n        :type StrategyName: str\n        :param StrategyType: 策略类型。支持WHITE（白名单）和BLACK（黑名单）。\n        :type StrategyType: str\n        :param StrategyData: 策略详情，多个ip 使用\n 分隔符分开。\n        :type StrategyData: str\n        """
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
        """
        :param Result: 新建的IP策略详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param PluginName: 用户自定义的插件名称。最长50个字符，支持 a-z,A-Z,0-9,_, 必须字母开头，字母或者数字结尾。\n        :type PluginName: str\n        :param PluginType: 插件类型。目前支持IPControl。\n        :type PluginType: str\n        :param PluginData: 插件定义语句，支持json。\n        :type PluginData: str\n        :param Description: 插件描述，限定200字以内。\n        :type Description: str\n        """
        self.PluginName = None
        self.PluginType = None
        self.PluginData = None
        self.Description = None


    def _deserialize(self, params):
        self.PluginName = params.get("PluginName")
        self.PluginType = params.get("PluginType")
        self.PluginData = params.get("PluginData")
        self.Description = params.get("Description")
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
        """
        :param Result: 新建的插件详情。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceName: 用户自定义的服务名称。\n        :type ServiceName: str\n        :param Protocol: 服务的前端请求类型。如 http、https、http&https。\n        :type Protocol: str\n        :param ServiceDesc: 用户自定义的服务描述。\n        :type ServiceDesc: str\n        :param ExclusiveSetName: 独立集群名称，用于指定创建服务所在的独立集群。\n        :type ExclusiveSetName: str\n        :param NetTypes: 网络类型列表，用于指定支持的访问类型，INNER为内网访问，OUTER为外网访问。默认为OUTER。\n        :type NetTypes: list of str\n        :param IpVersion: IP版本号，支持IPv4和IPv6，默认为IPv4。\n        :type IpVersion: str\n        :param SetServerName: 集群名称。保留字段，tsf serverlss类型使用。\n        :type SetServerName: str\n        :param AppIdType: 用户类型。保留类型，serverless用户使用。\n        :type AppIdType: str\n        :param Tags: 标签。\n        :type Tags: list of Tag\n        :param InstanceId: 独享实例id\n        :type InstanceId: str\n        """
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
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param ServiceName: 用户自定义服务名称。\n        :type ServiceName: str\n        :param ServiceDesc: 用户自定义服务描述。\n        :type ServiceDesc: str\n        :param OuterSubDomain: 外网默认域名。\n        :type OuterSubDomain: str\n        :param InnerSubDomain: vpc内网默认域名。\n        :type InnerSubDomain: str\n        :param CreatedTime: 服务创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。\n        :type CreatedTime: str\n        :param NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。\n        :type NetTypes: list of str\n        :param IpVersion: IP版本号。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpVersion: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class CreateUsagePlanRequest(AbstractModel):
    """CreateUsagePlan请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanName: 用户自定义的使用计划名称。\n        :type UsagePlanName: str\n        :param UsagePlanDesc: 用户自定义的使用计划描述。\n        :type UsagePlanDesc: str\n        :param MaxRequestNum: 请求配额总数，取值范围为-1或者[1, 99999999]，默认为-1，表示不开启。\n        :type MaxRequestNum: int\n        :param MaxRequestNumPreSec: 每秒请求限制数，取值范围为-1或者[1, 2000]，默认-1，表示不开启。\n        :type MaxRequestNumPreSec: int\n        """
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
        """
        :param Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ApiDocId: API文档ID\n        :type ApiDocId: str\n        """
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
        """
        :param Result: 操作是否成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiAppRequest(AbstractModel):
    """DeleteApiApp请求参数结构体

    """

    def __init__(self):
        """
        :param ApiAppId: 应用唯一 ID。\n        :type ApiAppId: str\n        """
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
        """
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiKeyRequest(AbstractModel):
    """DeleteApiKey请求参数结构体

    """

    def __init__(self):
        """
        :param AccessKeyId: 待删除的密钥 ID。\n        :type AccessKeyId: str\n        """
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
        """
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteApiRequest(AbstractModel):
    """DeleteApi请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: API 所在的服务唯一 ID。\n        :type ServiceId: str\n        :param ApiId: API 接口唯一 ID。\n        :type ApiId: str\n        """
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
        """
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteIPStrategyRequest(AbstractModel):
    """DeleteIPStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待删除的IP策略所属的服务唯一ID。\n        :type ServiceId: str\n        :param StrategyId: 待删除的IP策略唯一ID。\n        :type StrategyId: str\n        """
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
        """
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeletePluginRequest(AbstractModel):
    """DeletePlugin请求参数结构体

    """

    def __init__(self):
        """
        :param PluginId: 要删除的API网关插件的ID。\n        :type PluginId: str\n        """
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
        """
        :param Result: 删除操作是否成功。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteServiceRequest(AbstractModel):
    """DeleteService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待删除服务的唯一 ID。\n        :type ServiceId: str\n        :param SkipVerification: 跳过删除前置条件校验（仅支持独享实例上的服务）\n        :type SkipVerification: int\n        """
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
        """
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteServiceSubDomainMappingRequest(AbstractModel):
    """DeleteServiceSubDomainMapping请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一 ID。\n        :type ServiceId: str\n        :param SubDomain: 服务绑定的自定义域名。\n        :type SubDomain: str\n        :param Environment: 待删除映射的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。\n        :type Environment: str\n        """
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
        """
        :param Result: 删除自定义域名的路径映射操作是否成功。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DeleteUsagePlanRequest(AbstractModel):
    """DeleteUsagePlan请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanId: 待删除的使用计划唯一 ID。\n        :type UsagePlanId: str\n        """
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
        """
        :param Result: 删除操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DemoteServiceUsagePlanRequest(AbstractModel):
    """DemoteServiceUsagePlan请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanId: 使用计划ID。\n        :type UsagePlanId: str\n        :param ServiceId: 待降级的服务唯一 ID。\n        :type ServiceId: str\n        :param Environment: 环境名称。\n        :type Environment: str\n        """
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
        """
        :param Result: 降级操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DesApisStatus(AbstractModel):
    """api状态详情

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param ApiId: API唯一ID。\n        :type ApiId: str\n        :param ApiDesc: 用户自定义的 API 接口描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiDesc: str\n        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param ApiName: API 接口的名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiName: str\n        :param VpcId: VPCID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: int\n        :param UniqVpcId: VPC唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UniqVpcId: str\n        :param ApiType: API类型。取值为NORMAL（普通API）和TSF（微服务API）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiType: str\n        :param Protocol: API协议。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param IsDebugAfterCharge: 是否买后调试。（云市场预留字段）
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDebugAfterCharge: bool\n        :param AuthType: API 鉴权类型。取值为SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH、EIAM。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuthType: str\n        :param ApiBusinessType: OAUTH API的类型。当AuthType 为 OAUTH时该字段有效， 取值为NORMAL（业务API）和 OAUTH（授权API）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiBusinessType: str\n        :param AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AuthRelationApiId: str\n        :param OauthConfig: OAUTH 配置信息。当AuthType是OAUTH时生效。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param RelationBuniessApiIds: 授权API关联的业务API列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelationBuniessApiIds: list of str\n        :param Tags: API关联的标签信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of str\n        :param Path: API 的路径，如 /path。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param Method: API 的请求方法，如 GET。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Method: str\n        """
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
        """
        :param ApiDocId: API文档ID\n        :type ApiDocId: str\n        """
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
        """
        :param Result: API文档详细信息\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: API文档列表信息\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDocs`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 要查询的服务ID。\n        :type ServiceId: str\n        :param PluginId: 要查询的插件ID。\n        :type PluginId: str\n        :param EnvironmentName: 环境信息。\n        :type EnvironmentName: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 插件相关API的列表。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfoSummary`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ApiAppId: 应用ID\n        :type ApiAppId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 过滤条件。支持ApiId、ApiName、ServiceId、Environment 、KeyWord（ 可以匹配name或者ID）。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 应用绑定的Api列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ApiAppId: 应用ID。\n        :type ApiAppId: str\n        """
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
        """
        :param Result: 应用详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 过滤条件。支持ApiAppId、ApiAppName、KeyWord（ 可以匹配name或者ID）。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 应用列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppInfos`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 服务ID\n        :type ServiceId: str\n        :param ApiIds: Api的ID的数组\n        :type ApiIds: list of str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 过滤条件。支持ApiAppId、Environment、KeyWord（ 可以匹配name或者ID）。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 应用绑定的Api列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiAppApiInfos`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: API所属服务唯一ID。\n        :type ServiceId: str\n        :param EnvironmentNames: 环境列表。\n        :type EnvironmentNames: list of str\n        :param ApiId: API唯一ID。\n        :type ApiId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: api绑定策略详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiEnvironmentStrategyStataus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: API 所在的服务唯一 ID。\n        :type ServiceId: str\n        :param ApiId: API 接口唯一 ID。\n        :type ApiId: str\n        :param ApiRegion: Api所属地域\n        :type ApiRegion: str\n        """
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
        """
        :param Result: API 详情。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param AccessKeyId: API 密钥 ID。\n        :type AccessKeyId: str\n        """
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
        """
        :param Result: 密钥详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 过滤条件。支持AccessKeyId、AccessKeySecret、SecretName、NotUsagePlanId、Status、KeyWord（ 可以匹配name或者path）。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 密钥列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKeysStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: API 所在的服务唯一 ID。\n        :type ServiceId: str\n        :param ApiId: API 接口唯一 ID。\n        :type ApiId: str\n        """
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
        """
        :param Result: API 详情。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApiInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeApiUsagePlanRequest(AbstractModel):
    """DescribeApiUsagePlan请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待查询的服务唯一 ID。\n        :type ServiceId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: api绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiUsagePlanSet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: API 所在的服务唯一 ID。\n        :type ServiceId: str\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为 20，最大值为 100\n        :type Limit: int\n        :param Filters: API过滤条件。支持ApiId、ApiName、ApiPath、ApiType、AuthRelationApiId、AuthType、ApiBuniessType、NotUsagePlanId、Environment、Tags (values为 $tag_key:tag_value的列表)、TagKeys （values 为 tag key的列表）。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: API 详情列表。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApisStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ApisStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeIPStrategyApisStatusRequest(AbstractModel):
    """DescribeIPStrategyApisStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param StrategyId: 策略唯一ID。\n        :type StrategyId: str\n        :param EnvironmentName: 策略所在环境。\n        :type EnvironmentName: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 过滤条件。支持 ApiPath、ApiName、KeyWord（模糊查询Path 和Name）。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 环境绑定API列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategyApiStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param StrategyId: IP 策略唯一ID。\n        :type StrategyId: str\n        :param EnvironmentName: 策略关联的环境。\n        :type EnvironmentName: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 过滤条件。预留字段，目前不支持过滤。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: IP策略详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategy`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param Filters: 过滤条件。支持StrategyName。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 符合条件的策略列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.IPStrategysStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param StartTime: 日志开始时间\n        :type StartTime: str\n        :param EndTime: 日志结束时间\n        :type EndTime: str\n        :param ServiceId: 服务id\n        :type ServiceId: str\n        :param Filters: 保留字段\n        :type Filters: list of Filter\n        :param Limit: 单次要返回的日志条数，单次返回的最大条数为100\n        :type Limit: int\n        :param ConText: 根据上次返回的ConText，获取后续的内容，最多可获取10000条\n        :type ConText: str\n        :param Sort: 按时间排序 asc（升序）或者 desc（降序），默认为 desc\n        :type Sort: str\n        :param Query: 保留字段\n        :type Query: str\n        :param LogQuerys: 检索条件,支持的检索条件如下：
req_id：“=”
api_id：“=”
cip：“=”
uip：“:”
err_msg：“:”
rsp_st：“=” 、“!=” 、 “:” 、 “>” 、 “<”
req_t：”>=“ 、 ”<=“

说明：
“:”表示包含，“!=”表示不等于，字段含义见输出参数的LogSet说明\n        :type LogQuerys: list of LogQuery\n        """
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
        """
        :param ConText: 获取更多检索结果的游标，值为""表示无后续结果\n        :type ConText: str\n        :param LogSet: 由0或多条日志组成，每条日志格式如下：
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
req_id：请求id。\n        :type LogSet: list of str\n        :param TotalCount: 单次搜索返回的日志条数，TotalCount <= Limit\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param PluginId: 查询的插件ID。\n        :type PluginId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 插件绑定的API列表信息。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.AttachedApiSummary`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param PluginId: 要查询的插件ID。\n        :type PluginId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 插件详情。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.Plugin`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = Plugin()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribePluginsRequest(AbstractModel):
    """DescribePlugins请求参数结构体

    """

    def __init__(self):
        """
        :param PluginIds: 要查询的插件列表。\n        :type PluginIds: list of str\n        :param PluginName: 要查询的插件名称。\n        :type PluginName: str\n        :param PluginType: 要查询的插件类型。\n        :type PluginType: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 过滤条件。预留字段，目前不支持过滤。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 插件详情。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.PluginSummary`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 待查询的服务唯一 ID。\n        :type ServiceId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 服务绑定环境详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentSet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 待查询的服务唯一 ID。\n        :type ServiceId: str\n        :param EnvironmentName: 环境名称。\n        :type EnvironmentName: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 服务发布历史。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseHistory`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceEnvironmentStrategyStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 待查询的服务唯一 ID。\n        :type ServiceId: str\n        :param ApiRegion: 服务所属的地域\n        :type ApiRegion: str\n        """
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
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param AvailableEnvironments: 服务 环境列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AvailableEnvironments: list of str\n        :param ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceName: str\n        :param ServiceDesc: 服务描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceDesc: str\n        :param Protocol: 服务支持协议，可选值为http、https、http&https。\n        :type Protocol: str\n        :param CreatedTime: 服务创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 服务修改时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param ExclusiveSetName: 独立集群名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExclusiveSetName: str\n        :param NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。\n        :type NetTypes: list of str\n        :param InternalSubDomain: 内网访问子域名。\n        :type InternalSubDomain: str\n        :param OuterSubDomain: 外网访问子域名。\n        :type OuterSubDomain: str\n        :param InnerHttpPort: 内网访问http服务端口号。\n        :type InnerHttpPort: int\n        :param InnerHttpsPort: 内网访问https端口号。\n        :type InnerHttpsPort: int\n        :param ApiTotalCount: API总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiTotalCount: int\n        :param ApiIdStatusSet: API列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiIdStatusSet: list of ApiIdStatus\n        :param UsagePlanTotalCount: 使用计划总数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanTotalCount: int\n        :param UsagePlanList: 使用计划数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanList: list of UsagePlan\n        :param IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpVersion: str\n        :param UserType: 此服务的用户类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserType: str\n        :param SetId: 预留字段。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SetId: int\n        :param Tags: 服务绑定的标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 待查询的服务唯一 ID。\n        :type ServiceId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        """
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
        """
        :param Result: 服务发布版本列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceReleaseVersion`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServiceReleaseVersion()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeServiceRequest(AbstractModel):
    """DescribeService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待查询的服务唯一 ID。\n        :type ServiceId: str\n        """
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
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param AvailableEnvironments: 服务 环境列表。\n        :type AvailableEnvironments: list of str\n        :param ServiceName: 服务名称。\n        :type ServiceName: str\n        :param ServiceDesc: 服务描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceDesc: str\n        :param Protocol: 服务支持协议，可选值为http、https、http&https。\n        :type Protocol: str\n        :param CreatedTime: 服务创建时间。\n        :type CreatedTime: str\n        :param ModifiedTime: 服务修改时间。\n        :type ModifiedTime: str\n        :param ExclusiveSetName: 独立集群名称。\n        :type ExclusiveSetName: str\n        :param NetTypes: 网络类型列表，INNER为内网访问，OUTER为外网访问。\n        :type NetTypes: list of str\n        :param InternalSubDomain: 内网访问子域名。\n        :type InternalSubDomain: str\n        :param OuterSubDomain: 外网访问子域名。\n        :type OuterSubDomain: str\n        :param InnerHttpPort: 内网访问http服务端口号。\n        :type InnerHttpPort: int\n        :param InnerHttpsPort: 内网访问https端口号。\n        :type InnerHttpsPort: int\n        :param ApiTotalCount: API总数。\n        :type ApiTotalCount: int\n        :param ApiIdStatusSet: API列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiIdStatusSet: list of ApiIdStatus\n        :param UsagePlanTotalCount: 使用计划总数量。\n        :type UsagePlanTotalCount: int\n        :param UsagePlanList: 使用计划数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanList: list of UsagePlan\n        :param IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpVersion: str\n        :param UserType: 此服务的用户类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserType: str\n        :param SetId: 预留字段。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SetId: int\n        :param Tags: 服务绑定的标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param InstanceId: 独享实例id
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param InstanceName: 独享实例name
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param SetType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type SetType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class DescribeServiceSubDomainMappingsRequest(AbstractModel):
    """DescribeServiceSubDomainMappings请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一 ID。\n        :type ServiceId: str\n        :param SubDomain: 服务绑定的自定义域名。\n        :type SubDomain: str\n        """
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
        """
        :param Result: 自定义路径映射列表。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceSubDomainMappings`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 服务唯一 ID。\n        :type ServiceId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 查询服务自定义域名列表。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DomainSets`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 待查询的服务唯一 ID。\n        :type ServiceId: str\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        """
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
        """
        :param Result: 服务绑定使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServiceUsagePlanSet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 过滤条件。支持ServiceId、ServiceName、NotUsagePlanId、Environment、IpVersion。InstanceId\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 服务列表查询结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ServicesStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = ServicesStatus()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class DescribeUsagePlanEnvironmentsRequest(AbstractModel):
    """DescribeUsagePlanEnvironments请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanId: 待查询的使用计划唯一 ID。\n        :type UsagePlanId: str\n        :param BindType: 定类型，取值为 API、SERVICE，默认值为 SERVICE。\n        :type BindType: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 使用计划绑定详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanEnvironmentStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param UsagePlanId: 待查询的使用计划唯一 ID。\n        :type UsagePlanId: str\n        """
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
        """
        :param Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param UsagePlanId: 绑定的使用计划唯一 ID。\n        :type UsagePlanId: str\n        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        """
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
        """
        :param Result: 使用计划绑定的密钥列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanBindSecretStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Limit: 返回数量，默认为 20，最大值为 100。\n        :type Limit: int\n        :param Offset: 偏移量，默认为 0。\n        :type Offset: int\n        :param Filters: 使用计划过滤条件。支持UsagePlanId、UsagePlanName、NotServiceId、NotApiId、Environment。\n        :type Filters: list of Filter\n        """
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
        """
        :param Result: 使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlansStatus`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param PluginId: 要解绑的API网关插件ID。\n        :type PluginId: str\n        :param ServiceId: 要操作的服务ID。\n        :type ServiceId: str\n        :param EnvironmentName: 要操作API的环境。\n        :type EnvironmentName: str\n        :param ApiId: 要解绑的API ID。\n        :type ApiId: str\n        """
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
        """
        :param Result: 解绑操作是否成功。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DisableApiKeyRequest(AbstractModel):
    """DisableApiKey请求参数结构体

    """

    def __init__(self):
        """
        :param AccessKeyId: 待禁用的密钥 ID。\n        :type AccessKeyId: str\n        """
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
        """
        :param Result: 禁用密钥操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DocumentSDK(AbstractModel):
    """api文档下载

    """

    def __init__(self):
        """
        :param DocumentURL: 生成的 document 会存放到 COS 中，此出参返回产生文件的下载链接。\n        :type DocumentURL: str\n        :param SdkURL: 生成的 SDK 会存放到 COS 中，此出参返回产生 SDK 文件的下载链接。\n        :type SdkURL: str\n        """
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
        """
        :param DomainName: 域名名称。\n        :type DomainName: str\n        :param Status: 域名解析状态。True 表示正常解析，False 表示解析失败。\n        :type Status: int\n        :param CertificateId: 证书ID。\n        :type CertificateId: str\n        :param IsDefaultMapping: 是否使用默认路径映射。\n        :type IsDefaultMapping: bool\n        :param Protocol: 自定义域名协议类型。\n        :type Protocol: str\n        :param NetType: 网络类型（'INNER' 或 'OUTER'）。\n        :type NetType: str\n        :param IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。\n        :type IsForcedHttps: bool\n        :param RegistrationStatus: 域名备案注册状态\n        :type RegistrationStatus: bool\n        """
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
        """
        :param TotalCount: 服务下的自定义域名数量。\n        :type TotalCount: int\n        :param DomainSet: 自定义服务域名列表。\n        :type DomainSet: list of DomainSetList\n        """
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
        """
        :param AccessKeyId: 待启用的密钥 ID。\n        :type AccessKeyId: str\n        """
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
        """
        :param Result: 启动密钥操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class Environment(AbstractModel):
    """服务发布的环境信息。

    """

    def __init__(self):
        """
        :param EnvironmentName: 环境名称。\n        :type EnvironmentName: str\n        :param Url: 访问路径。\n        :type Url: str\n        :param Status: 发布状态，1 表示已发布，0 表示未发布。\n        :type Status: int\n        :param VersionName: 运行版本。\n        :type VersionName: str\n        """
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
        """
        :param EnvironmentName: 环境名\n        :type EnvironmentName: str\n        :param Quota: 限流值\n        :type Quota: int\n        :param MaxQuota: 限流最大值
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxQuota: int\n        """
        self.EnvironmentName = None
        self.Quota = None
        self.MaxQuota = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Quota = params.get("Quota")
        self.MaxQuota = params.get("MaxQuota")
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
        """
        :param Code: 自定义响应配置错误码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        :param Msg: 自定义响应配置错误信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Msg: str\n        :param Desc: 自定义响应配置错误码备注。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Desc: str\n        :param ConvertedCode: 自定义错误码转换。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConvertedCode: int\n        :param NeedConvert: 是否需要开启错误码转换。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NeedConvert: bool\n        """
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
        """
        :param Name: 需要过滤的字段。\n        :type Name: str\n        :param Values: 字段的过滤值。\n        :type Values: list of str\n        """
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
        """
        :param ServiceId: 待创建文档的服务唯一 ID。\n        :type ServiceId: str\n        :param GenEnvironment: 待创建 SDK 的服务所在环境。\n        :type GenEnvironment: str\n        :param GenLanguage: 待创建 SDK 的语言。当前只支持 Python 和 JavaScript。\n        :type GenLanguage: str\n        """
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
        """
        :param Result: api文档&sdk链接。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.DocumentSDK`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param IsHealthCheck: 是否开启健康检查。\n        :type IsHealthCheck: bool\n        :param RequestVolumeThreshold: 健康检查阈值。\n        :type RequestVolumeThreshold: int\n        :param SleepWindowInMilliseconds: 窗口大小。\n        :type SleepWindowInMilliseconds: int\n        :param ErrorThresholdPercentage: 阈值百分比。\n        :type ErrorThresholdPercentage: int\n        """
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
        """
        :param StrategyId: 策略唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StrategyId: str\n        :param StrategyName: 用户自定义策略名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StrategyName: str\n        :param StrategyType: 策略类型。支持WHITE（白名单）和BLACK（黑名单）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StrategyType: str\n        :param StrategyData: IP列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StrategyData: str\n        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 修改时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param ServiceId: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceId: str\n        :param BindApiTotalCount: 策略绑定的API数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindApiTotalCount: int\n        :param BindApis: 绑定的API详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindApis: list of DesApisStatus\n        """
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
        """
        :param ApiId: API 唯一 ID。\n        :type ApiId: str\n        :param ApiName: 用户自定义的 API 名称。\n        :type ApiName: str\n        :param ApiType: API 类型。取值为NORMAL（普通API）和TSF （微服务API）。\n        :type ApiType: str\n        :param Path: API 的路径。如 /path。\n        :type Path: str\n        :param Method: API 的请求方法。如 GET。\n        :type Method: str\n        :param OtherIPStrategyId: API 已经绑定的其他策略唯一ID。\n        :type OtherIPStrategyId: str\n        :param OtherEnvironmentName: API 已经绑定的环境。\n        :type OtherEnvironmentName: str\n        """
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
        """
        :param TotalCount: 环境绑定API数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param ApiIdStatusSet: 环境绑定API详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiIdStatusSet: list of IPStrategyApi\n        """
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
        """
        :param TotalCount: 策略数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param StrategySet: 策略列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StrategySet: list of IPStrategy\n        """
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
        


class LogQuery(AbstractModel):
    """检索条件入参

    """

    def __init__(self):
        """
        :param Name: 检索字段\n        :type Name: str\n        :param Operator: 操作符\n        :type Operator: str\n        :param Value: 检索值\n        :type Value: str\n        """
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
        """
        :param ClusterId: 微服务集群ID。\n        :type ClusterId: str\n        :param NamespaceId: 微服务命名空间ID。\n        :type NamespaceId: str\n        :param MicroServiceName: 微服务名称。\n        :type MicroServiceName: str\n        """
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
        """
        :param ClusterId: 微服务集群。\n        :type ClusterId: str\n        :param NamespaceId: 微服务命名空间。\n        :type NamespaceId: str\n        :param MicroServiceName: 微服务名称。\n        :type MicroServiceName: str\n        """
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
        """
        :param ApiDocId: API文档ID\n        :type ApiDocId: str\n        :param ApiDocName: API文档名称\n        :type ApiDocName: str\n        :param ServiceId: 服务名称\n        :type ServiceId: str\n        :param Environment: 环境名称\n        :type Environment: str\n        :param ApiIds: 生成文档的API列表\n        :type ApiIds: list of str\n        """
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
        """
        :param Result: API文档基本信息\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ApiAppId: 应用唯一 ID。\n        :type ApiAppId: str\n        :param ApiAppName: 修改的应用名称\n        :type ApiAppName: str\n        :param ApiAppDesc: 修改的应用描述\n        :type ApiAppDesc: str\n        """
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
        """
        :param Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyApiEnvironmentStrategyRequest(AbstractModel):
    """ModifyApiEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一ID。\n        :type ServiceId: str\n        :param Strategy: 限流值。\n        :type Strategy: int\n        :param EnvironmentName: 环境名。\n        :type EnvironmentName: str\n        :param ApiIds: API列表。\n        :type ApiIds: list of str\n        """
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
        """
        :param Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyApiIncrementRequest(AbstractModel):
    """ModifyApiIncrement请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务ID\n        :type ServiceId: str\n        :param ApiId: 接口ID\n        :type ApiId: str\n        :param BusinessType: 需要修改的API auth类型(可选择OAUTH-授权API)\n        :type BusinessType: str\n        :param PublicKey: oauth接口需要修改的公钥值\n        :type PublicKey: str\n        :param LoginRedirectUrl: oauth接口重定向地址\n        :type LoginRedirectUrl: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyApiRequest(AbstractModel):
    """ModifyApi请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: API 所在的服务唯一 ID。\n        :type ServiceId: str\n        :param ServiceType: API 的后端服务类型。支持HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。\n        :type ServiceType: str\n        :param RequestConfig: 请求的前端配置。\n        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.RequestConfig`\n        :param ApiId: API 接口唯一 ID。\n        :type ApiId: str\n        :param ApiName: 用户自定义的 API 名称。\n        :type ApiName: str\n        :param ApiDesc: 用户自定义的 API 接口描述。\n        :type ApiDesc: str\n        :param ApiType: API 类型，支持NORMAL和TSF，默认为NORMAL。\n        :type ApiType: str\n        :param AuthType: API 鉴权类型。支持SECRET、NONE、OAUTH、APP。默认为NONE。\n        :type AuthType: str\n        :param AuthRequired: 是否需要签名认证，True 表示需要，False 表示不需要。待废弃。\n        :type AuthRequired: bool\n        :param ServiceTimeout: API 的后端服务超时时间，单位是秒。\n        :type ServiceTimeout: int\n        :param Protocol: API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。\n        :type Protocol: str\n        :param EnableCORS: 是否需要开启跨域，Ture 表示需要，False 表示不需要。\n        :type EnableCORS: bool\n        :param ConstantParameters: 常量参数。\n        :type ConstantParameters: list of ConstantParameter\n        :param RequestParameters: 前端请求参数。\n        :type RequestParameters: list of ReqParameter\n        :param ApiBusinessType: 当AuthType 为 OAUTH时，该字段有效， NORMAL：业务api   OAUTH：授权API。\n        :type ApiBusinessType: str\n        :param ServiceMockReturnMessage: API 的后端 Mock 返回信息。如果 ServiceType 是 Mock，则此参数必传。\n        :type ServiceMockReturnMessage: str\n        :param MicroServices: API绑定微服务服务列表。\n        :type MicroServices: list of MicroServiceReq\n        :param ServiceTsfLoadBalanceConf: 微服务的负载均衡配置。\n        :type ServiceTsfLoadBalanceConf: :class:`tencentcloud.apigateway.v20180808.models.TsfLoadBalanceConfResp`\n        :param ServiceTsfHealthCheckConf: 微服务的健康检查配置。\n        :type ServiceTsfHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param TargetServicesLoadBalanceConf: target类型负载均衡配置。（内测阶段）\n        :type TargetServicesLoadBalanceConf: int\n        :param TargetServicesHealthCheckConf: target健康检查配置。（内测阶段）\n        :type TargetServicesHealthCheckConf: :class:`tencentcloud.apigateway.v20180808.models.HealthCheckConf`\n        :param ServiceScfFunctionName: scf 函数名称。当后端类型是SCF时生效。\n        :type ServiceScfFunctionName: str\n        :param ServiceWebsocketRegisterFunctionName: scf websocket注册函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketRegisterFunctionName: str\n        :param ServiceWebsocketCleanupFunctionName: scf websocket清理函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketCleanupFunctionName: str\n        :param ServiceWebsocketTransportFunctionName: scf websocket传输函数。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketTransportFunctionName: str\n        :param ServiceScfFunctionNamespace: scf 函数命名空间。当后端类型是SCF时生效。\n        :type ServiceScfFunctionNamespace: str\n        :param ServiceScfFunctionQualifier: scf函数版本。当后端类型是SCF时生效。\n        :type ServiceScfFunctionQualifier: str\n        :param ServiceWebsocketRegisterFunctionNamespace: scf websocket注册函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketRegisterFunctionNamespace: str\n        :param ServiceWebsocketRegisterFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketRegisterFunctionQualifier: str\n        :param ServiceWebsocketTransportFunctionNamespace: scf websocket传输函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketTransportFunctionNamespace: str\n        :param ServiceWebsocketTransportFunctionQualifier: scf websocket传输函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketTransportFunctionQualifier: str\n        :param ServiceWebsocketCleanupFunctionNamespace: scf websocket清理函数命名空间。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketCleanupFunctionNamespace: str\n        :param ServiceWebsocketCleanupFunctionQualifier: scf websocket清理函数版本。当前端类型是WEBSOCKET且后端类型是SCF时生效。\n        :type ServiceWebsocketCleanupFunctionQualifier: str\n        :param ServiceScfIsIntegratedResponse: 是否开启响应集成。当后端类型是SCF时生效。\n        :type ServiceScfIsIntegratedResponse: bool\n        :param IsDebugAfterCharge: 开始调试后计费。（云市场预留字段）\n        :type IsDebugAfterCharge: bool\n        :param TagSpecifications: 标签。\n        :type TagSpecifications: :class:`tencentcloud.apigateway.v20180808.models.Tag`\n        :param IsDeleteResponseErrorCodes: 是否删除自定义响应配置错误码，如果不传或者传 False，不删除，当传 True 时，则删除此 API 所有自定义响应配置错误码。\n        :type IsDeleteResponseErrorCodes: bool\n        :param ResponseType: 返回类型。\n        :type ResponseType: str\n        :param ResponseSuccessExample: 自定义响应配置成功响应示例。\n        :type ResponseSuccessExample: str\n        :param ResponseFailExample: 自定义响应配置失败响应示例。\n        :type ResponseFailExample: str\n        :param ServiceConfig: API 的后端服务配置。\n        :type ServiceConfig: :class:`tencentcloud.apigateway.v20180808.models.ServiceConfig`\n        :param AuthRelationApiId: 关联的授权API 唯一 ID，当AuthType为OAUTH且ApiBusinessType为NORMAL时生效。标示业务API绑定的oauth2.0授权API唯一ID。\n        :type AuthRelationApiId: str\n        :param ServiceParameters: API的后端服务参数。\n        :type ServiceParameters: list of ServiceParameter\n        :param OauthConfig: oauth配置。当AuthType是OAUTH时生效。\n        :type OauthConfig: :class:`tencentcloud.apigateway.v20180808.models.OauthConfig`\n        :param ResponseErrorCodes: 用户自定义错误码配置。\n        :type ResponseErrorCodes: list of ResponseErrorCodeReq\n        :param IsBase64Encoded: 是否开启Base64编码，只有后端为scf时才会生效。\n        :type IsBase64Encoded: bool\n        :param IsBase64Trigger: 是否开启Base64编码的header触发，只有后端为scf时才会生效。\n        :type IsBase64Trigger: bool\n        :param Base64EncodedTriggerRules: Header触发规则，总规则数不能超过10。\n        :type Base64EncodedTriggerRules: list of Base64EncodedTriggerRule\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIPStrategyRequest(AbstractModel):
    """ModifyIPStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待修改的策略所属服务的唯一ID。\n        :type ServiceId: str\n        :param StrategyId: 待修改的策略唯一ID。\n        :type StrategyId: str\n        :param StrategyData: 待修改的策略详情。\n        :type StrategyData: str\n        """
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
        """
        :param Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyPluginRequest(AbstractModel):
    """ModifyPlugin请求参数结构体

    """

    def __init__(self):
        """
        :param PluginId: 要修改的插件ID。\n        :type PluginId: str\n        :param PluginName: 要修改的API网关插件名称。最长50个字符，支持 a-z,A-Z,0-9,_, 必须字母开头，字母或者数字结尾。\n        :type PluginName: str\n        :param Description: 要修改的插件描述，限定200字以内。\n        :type Description: str\n        :param PluginData: 要修改的插件定义语句，支持json。\n        :type PluginData: str\n        """
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
        """
        :param Result: 修改操作是否成功。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceEnvironmentStrategyRequest(AbstractModel):
    """ModifyServiceEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务的唯一ID。\n        :type ServiceId: str\n        :param Strategy: 限流值。\n        :type Strategy: int\n        :param EnvironmentNames: 环境列表。\n        :type EnvironmentNames: list of str\n        """
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
        """
        :param Result: 修改操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyServiceRequest(AbstractModel):
    """ModifyService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待修改服务的唯一 Id。\n        :type ServiceId: str\n        :param ServiceName: 修改后的服务名称。\n        :type ServiceName: str\n        :param ServiceDesc: 修改后的服务描述。\n        :type ServiceDesc: str\n        :param Protocol: 修改后的服务前端请求类型，如 http、https和 http&https。\n        :type Protocol: str\n        :param NetTypes: 网络类型列表，用于指定支持的访问类型，INNER为内网访问，OUTER为外网访问。默认为OUTER。\n        :type NetTypes: list of str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubDomainRequest(AbstractModel):
    """ModifySubDomain请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一 ID。\n        :type ServiceId: str\n        :param SubDomain: 待修改路径映射的自定义的域名。\n        :type SubDomain: str\n        :param IsDefaultMapping: 是否修改为使用默认路径映射。为 true，表示使用默认路径映射，为 false，表示使用自定义路径映射。\n        :type IsDefaultMapping: bool\n        :param CertificateId: 证书 ID，协议包含 HTTPS 的时候要传该字段。\n        :type CertificateId: str\n        :param Protocol: 修改后的自定义域名协议类型。（http，https 或 http&https)\n        :type Protocol: str\n        :param PathMappingSet: 修改后的路径映射列表。\n        :type PathMappingSet: list of PathMapping\n        :param NetType: 网络类型 （'INNER' 或 'OUTER'）\n        :type NetType: str\n        :param IsForcedHttps: 是否将HTTP请求强制跳转 HTTPS，默认为false。参数为 true时，API网关会将所有使用该自定义域名的 HTTP 协议的请求重定向至 HTTPS 协议进行转发。\n        :type IsForcedHttps: bool\n        """
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
        """
        :param Result: 修改自定义域名操作是否成功。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class ModifyUsagePlanRequest(AbstractModel):
    """ModifyUsagePlan请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanId: 使用计划唯一 ID。\n        :type UsagePlanId: str\n        :param UsagePlanName: 修改后的用户自定义的使用计划名称。\n        :type UsagePlanName: str\n        :param UsagePlanDesc: 修改后的用户自定义的使用计划描述。\n        :type UsagePlanDesc: str\n        :param MaxRequestNum: 请求配额总数，取值范围为-1或者[1, 99999999]，默认为-1，表示不开启。\n        :type MaxRequestNum: int\n        :param MaxRequestNumPreSec: 每秒请求限制数，取值范围为-1或者[1, 2000]，默认-1，表示不开启。\n        :type MaxRequestNumPreSec: int\n        """
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
        """
        :param Result: 使用计划详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.UsagePlanInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = UsagePlanInfo()
            self.Result._deserialize(params.get("Result"))
        self.RequestId = params.get("RequestId")


class OauthConfig(AbstractModel):
    """Oauth授权配置信息

    """

    def __init__(self):
        """
        :param PublicKey: 公钥，用于验证用户token。\n        :type PublicKey: str\n        :param TokenLocation: token传递位置。\n        :type TokenLocation: str\n        :param LoginRedirectUrl: 重定向地址，用于引导用户登录操作。\n        :type LoginRedirectUrl: str\n        """
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
        


class PathMapping(AbstractModel):
    """自定义域名的路径映射。

    """

    def __init__(self):
        """
        :param Path: 路径。\n        :type Path: str\n        :param Environment: 发布环境，可选值为“test”、 ”prepub“、”release“。\n        :type Environment: str\n        """
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
        """
        :param PluginId: 插件ID。\n        :type PluginId: str\n        :param PluginName: 插件名称。\n        :type PluginName: str\n        :param PluginType: 插件类型。\n        :type PluginType: str\n        :param PluginData: 插件定义语句。\n        :type PluginData: str\n        :param Description: 插件描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param CreatedTime: 插件创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。\n        :type CreatedTime: str\n        :param ModifiedTime: 插件修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。\n        :type ModifiedTime: str\n        :param AttachedApiTotalCount: 插件绑定的API总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AttachedApiTotalCount: int\n        :param AttachedApis: 插件绑定的API信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AttachedApis: list of AttachedApiInfo\n        """
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
        """
        :param TotalCount: 插件个数。\n        :type TotalCount: int\n        :param PluginSet: 插件详情。\n        :type PluginSet: list of Plugin\n        """
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
        """
        :param ReleaseDesc: 发布时的备注信息填写。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseDesc: str\n        :param ReleaseVersion: 发布的版本id。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseVersion: str\n        """
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
        """
        :param ServiceId: 待发布服务的唯一 ID。\n        :type ServiceId: str\n        :param EnvironmentName: 待发布的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。\n        :type EnvironmentName: str\n        :param ReleaseDesc: 本次的发布描述。\n        :type ReleaseDesc: str\n        :param ApiIds: apiId列表，预留字段，默认全量api发布。\n        :type ApiIds: list of str\n        """
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
        """
        :param Result: 发布信息。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ReleaseService`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Name: API 的前端参数名称。\n        :type Name: str\n        :param Position: API 的前端参数位置，如 header。目前支持 header、query、path。\n        :type Position: str\n        :param Type: API 的前端参数类型，如 String、int。\n        :type Type: str\n        :param DefaultValue: API 的前端参数默认值。\n        :type DefaultValue: str\n        :param Required: API 的前端参数是否必填，True：表示必填，False：表示可选。\n        :type Required: bool\n        :param Desc: API 的前端参数备注。\n        :type Desc: str\n        """
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
        """
        :param Path: API 的路径，如 /path。\n        :type Path: str\n        :param Method: API 的请求方法，如 GET。\n        :type Method: str\n        """
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
        """
        :param Name: 请求参数名称\n        :type Name: str\n        :param Desc: 描述\n        :type Desc: str\n        :param Position: 参数位置\n        :type Position: str\n        :param Type: 参数类型\n        :type Type: str\n        :param DefaultValue: 默认值\n        :type DefaultValue: str\n        :param Required: 是否必须\n        :type Required: bool\n        """
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
        """
        :param ApiDocId: API文档ID\n        :type ApiDocId: str\n        """
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
        """
        :param Result: API文档基本信息\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.APIDoc`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Code: 自定义响应配置错误码。\n        :type Code: int\n        :param Msg: 自定义响应配置错误信息。\n        :type Msg: str\n        :param Desc: 自定义响应配置错误码备注。\n        :type Desc: str\n        :param ConvertedCode: 自定义错误码转换。\n        :type ConvertedCode: int\n        :param NeedConvert: 是否需要开启错误码转换。\n        :type NeedConvert: bool\n        """
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
        """
        :param InnerHttpsPort: 内网访问https端口。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerHttpsPort: int\n        :param ServiceDesc: 用户自定义的服务描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceDesc: str\n        :param Protocol: 服务的前端请求类型。如http、https 或者 http&https。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param NetTypes: 服务支持的网络类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetTypes: list of str\n        :param ExclusiveSetName: 独占集群名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExclusiveSetName: str\n        :param ServiceId: 服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceId: str\n        :param IpVersion: IP版本。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpVersion: str\n        :param AvailableEnvironments: 已经发布的环境列表。如test、prepub、release。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AvailableEnvironments: list of str\n        :param ServiceName: 用户自定义的服务名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceName: str\n        :param OuterSubDomain: 系统为该服务分配的外网域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OuterSubDomain: str\n        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param InnerHttpPort: 内网访问http端口。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerHttpPort: int\n        :param InnerSubDomain: 系统为该服务自动分配的内网域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InnerSubDomain: str\n        :param TradeIsolateStatus: 服务的计费状态。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TradeIsolateStatus: int\n        :param Tags: 服务绑定的标签
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tag\n        :param InstanceId: 独享实例
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param SetType: 集群类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type SetType: str\n        """
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
        """
        :param Product: 后端类型。启用vpc时生效，目前支持的类型为clb和vpc通道\n        :type Product: str\n        :param UniqVpcId: vpc 的唯一ID。\n        :type UniqVpcId: str\n        :param Url: API 的后端服务url。如果ServiceType是HTTP，则此参数必传。\n        :type Url: str\n        :param Path: API 的后端服务路径，如 /path。如果 ServiceType 是 HTTP，则此参数必传。前后端路径可不同。\n        :type Path: str\n        :param Method: API的后端服务请求方法，如 GET。如果 ServiceType 是 HTTP，则此参数必传。前后端方法可不同。\n        :type Method: str\n        """
        self.Product = None
        self.UniqVpcId = None
        self.Url = None
        self.Path = None
        self.Method = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        self.UniqVpcId = params.get("UniqVpcId")
        self.Url = params.get("Url")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
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
        """
        :param TotalCount: 服务绑定环境总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param EnvironmentList: 服务绑定环境列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvironmentList: list of Environment\n        """
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
        """
        :param EnvironmentName: 环境名。\n        :type EnvironmentName: str\n        :param Url: 访问服务对应环境的url。\n        :type Url: str\n        :param Status: 发布状态。\n        :type Status: int\n        :param VersionName: 发布的版本号。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionName: str\n        :param Strategy: 限流值。\n        :type Strategy: int\n        :param MaxStrategy: 最大限流值
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxStrategy: int\n        """
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
        """
        :param TotalCount: 限流策略数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param EnvironmentList: 限流策略列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvironmentList: list of ServiceEnvironmentStrategy\n        """
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
        """
        :param Name: API的后端服务参数名称。只有ServiceType是HTTP才会用到此参数。前后端参数名称可不同。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Position: API 的后端服务参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。前后端参数位置可配置不同。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Position: str\n        :param RelevantRequestParameterPosition: API 的后端服务参数对应的前端参数位置，如 head。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelevantRequestParameterPosition: str\n        :param RelevantRequestParameterName: API 的后端服务参数对应的前端参数名称。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelevantRequestParameterName: str\n        :param DefaultValue: API 的后端服务参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DefaultValue: str\n        :param RelevantRequestParameterDesc: API 的后端服务参数备注。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelevantRequestParameterDesc: str\n        :param RelevantRequestParameterType: API 的后端服务参数类型。只有 ServiceType 是 HTTP 才会用到此参数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RelevantRequestParameterType: str\n        """
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
        """
        :param TotalCount: 发布版本总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param VersionList: 历史版本列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionList: list of ServiceReleaseHistoryInfo\n        """
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
        """
        :param VersionName: 版本号。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionName: str\n        :param VersionDesc: 版本描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionDesc: str\n        :param ReleaseTime: 版本发布时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReleaseTime: str\n        """
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
        """
        :param TotalCount: 发布版本总数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param VersionList: 发布版本列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VersionList: list of ServiceReleaseHistoryInfo\n        """
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
        


class ServiceSubDomainMappings(AbstractModel):
    """服务自定义域名路径映射

    """

    def __init__(self):
        """
        :param IsDefaultMapping: 是否使用默认路径映射，为 True 表示使用默认路径映射；为 False 的话，表示使用自定义路径映射，此时 PathMappingSet 不为空。\n        :type IsDefaultMapping: bool\n        :param PathMappingSet: 自定义路径映射列表。\n        :type PathMappingSet: list of PathMapping\n        """
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
        """
        :param TotalCount: 服务上绑定的使用计划总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param ServiceUsagePlanList: 服务上绑定的使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceUsagePlanList: list of ApiUsagePlan\n        """
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
        """
        :param TotalCount: 服务列表总数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param ServiceSet: 服务列表详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceSet: list of Service\n        """
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
        """
        :param Key: 标签的 key。\n        :type Key: str\n        :param Value: 便签的 value。\n        :type Value: str\n        """
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
        """
        :param VmIp: vm ip\n        :type VmIp: str\n        :param VpcId: vpc id\n        :type VpcId: str\n        :param VmPort: vm port\n        :type VmPort: int\n        :param HostIp: cvm所在宿主机ip\n        :type HostIp: str\n        :param DockerIp: docker ip\n        :type DockerIp: str\n        """
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
        """
        :param IsLoadBalance: 是否开启负载均衡。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsLoadBalance: bool\n        :param Method: 负载均衡方式。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Method: str\n        :param SessionStickRequired: 是否开启会话保持。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SessionStickRequired: bool\n        :param SessionStickTimeout: 会话保持超时时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SessionStickTimeout: int\n        """
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
        """
        :param BindType: 绑定类型，取值为 API、SERVICE，默认值为 SERVICE。\n        :type BindType: str\n        :param UsagePlanIds: 待绑定的使用计划唯一 ID 列表。\n        :type UsagePlanIds: list of str\n        :param Environment: 待解绑的服务环境。\n        :type Environment: str\n        :param ServiceId: 待解绑的服务唯一 ID。\n        :type ServiceId: str\n        :param ApiIds: API 唯一 ID 数组，当 BindType=API 时，需要传入此参数。\n        :type ApiIds: list of str\n        """
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
        """
        :param Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindIPStrategyRequest(AbstractModel):
    """UnBindIPStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待解绑的服务唯一ID。\n        :type ServiceId: str\n        :param StrategyId: 待解绑的IP策略唯一ID。\n        :type StrategyId: str\n        :param EnvironmentName: 待解绑的环境。\n        :type EnvironmentName: str\n        :param UnBindApiIds: 待解绑的 API 列表。\n        :type UnBindApiIds: list of str\n        """
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
        """
        :param Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindSecretIdsRequest(AbstractModel):
    """UnBindSecretIds请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanId: 待解绑的使用计划唯一 ID。\n        :type UsagePlanId: str\n        :param AccessKeyIds: 待解绑的密钥 ID 数组。\n        :type AccessKeyIds: list of str\n        """
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
        """
        :param Result: 解绑操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnBindSubDomainRequest(AbstractModel):
    """UnBindSubDomain请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一 ID。\n        :type ServiceId: str\n        :param SubDomain: 待解绑的自定义的域名。\n        :type SubDomain: str\n        """
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
        """
        :param Result: 解绑自定义域名操作是否成功。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnReleaseServiceRequest(AbstractModel):
    """UnReleaseService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待下线服务的唯一 ID。\n        :type ServiceId: str\n        :param EnvironmentName: 待下线的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。\n        :type EnvironmentName: str\n        :param ApiIds: 保留字段，待下线的API列表。\n        :type ApiIds: list of str\n        """
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
        """
        :param Result: 下线操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UnbindApiAppRequest(AbstractModel):
    """UnbindApiApp请求参数结构体

    """

    def __init__(self):
        """
        :param ApiAppId: 待绑定的应用唯一 ID 。\n        :type ApiAppId: str\n        :param Environment: 待绑定的环境。\n        :type Environment: str\n        :param ServiceId: 待绑定的服务唯一 ID。\n        :type ServiceId: str\n        :param ApiId: 待绑定的API唯一ID。\n        :type ApiId: str\n        """
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
        """
        :param Result: 解除绑定操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiAppKeyRequest(AbstractModel):
    """UpdateApiAppKey请求参数结构体

    """

    def __init__(self):
        """
        :param ApiAppId: 应用唯一 ID。\n        :type ApiAppId: str\n        :param ApiAppKey: 应用的Key。\n        :type ApiAppKey: str\n        :param ApiAppSecret: 应用的Secret。\n        :type ApiAppSecret: str\n        """
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
        """
        :param Result: 更新操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UpdateApiKeyRequest(AbstractModel):
    """UpdateApiKey请求参数结构体

    """

    def __init__(self):
        """
        :param AccessKeyId: 待更换的密钥 ID。\n        :type AccessKeyId: str\n        :param AccessKeySecret: 待更换的密钥 Key，更新自定义密钥时，该字段为必传。长度10 - 50字符，包括字母、数字、英文下划线。\n        :type AccessKeySecret: str\n        """
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
        """
        :param Result: 更换后的密钥详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApiKey`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ServiceId: 待切换服务的唯一 Id。\n        :type ServiceId: str\n        :param EnvironmentName: 待切换的环境名称，当前支持三个环境，test（测试环境）、prepub（预发布环境）和 release（发布环境）。\n        :type EnvironmentName: str\n        :param VersionName: 切换的版本号。\n        :type VersionName: str\n        :param UpdateDesc: 本次的切换描述。\n        :type UpdateDesc: str\n        """
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
        """
        :param Result: 切换版本操作是否成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UsagePlan(AbstractModel):
    """usagePlan详情

    """

    def __init__(self):
        """
        :param Environment: 环境名称。\n        :type Environment: str\n        :param UsagePlanId: 使用计划唯一ID。\n        :type UsagePlanId: str\n        :param UsagePlanName: 使用计划名称。\n        :type UsagePlanName: str\n        :param UsagePlanDesc: 使用计划描述。\n        :type UsagePlanDesc: str\n        :param MaxRequestNumPreSec: 使用计划qps，-1表示没有限制。\n        :type MaxRequestNumPreSec: int\n        :param CreatedTime: 使用计划时间。\n        :type CreatedTime: str\n        :param ModifiedTime: 使用计划修改时间。\n        :type ModifiedTime: str\n        """
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
        """
        :param EnvironmentName: 环境名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvironmentName: str\n        :param ServiceId: 服务唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceId: str\n        """
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
        """
        :param AccessKeyId: 密钥ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessKeyId: str\n        :param SecretName: 密钥名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretName: str\n        :param Status: 密钥状态，0表示已禁用，1表示启用中。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        """
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
        """
        :param TotalCount: 使用计划绑定密钥的数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param AccessKeyList: 密钥详情列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessKeyList: list of UsagePlanBindSecret\n        """
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
        """
        :param ServiceId: 绑定的服务唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceId: str\n        :param ApiId: API 的唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiId: str\n        :param ApiName: API 的名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ApiName: str\n        :param Path: API 的路径。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param Method: API 的方法。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Method: str\n        :param Environment: 已经绑定的环境名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Environment: str\n        :param InUseRequestNum: 已经使用的配额。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InUseRequestNum: int\n        :param MaxRequestNum: 最大请求量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRequestNum: int\n        :param MaxRequestNumPreSec: 每秒最大请求次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRequestNumPreSec: int\n        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param ServiceName: 服务名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceName: str\n        """
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
        """
        :param TotalCount: 使用计划绑定的服务的环境数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param EnvironmentList: 使用计划已经绑定的各个服务的环境状态。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EnvironmentList: list of UsagePlanEnvironment\n        """
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
        """
        :param UsagePlanId: 使用计划唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanId: str\n        :param UsagePlanName: 使用计划名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanName: str\n        :param UsagePlanDesc: 使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanDesc: str\n        :param InitQuota: 初始化调用次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InitQuota: int\n        :param MaxRequestNumPreSec: 每秒请求限制数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRequestNumPreSec: int\n        :param MaxRequestNum: 最大调用次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRequestNum: int\n        :param IsHide: 是否隐藏。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsHide: int\n        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        :param BindSecretIdTotalCount: 绑定密钥的数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindSecretIdTotalCount: int\n        :param BindSecretIds: 绑定密钥的详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindSecretIds: list of str\n        :param BindEnvironmentTotalCount: 绑定环境数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindEnvironmentTotalCount: int\n        :param BindEnvironments: 绑定环境详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BindEnvironments: list of UsagePlanBindEnvironment\n        """
        self.UsagePlanId = None
        self.UsagePlanName = None
        self.UsagePlanDesc = None
        self.InitQuota = None
        self.MaxRequestNumPreSec = None
        self.MaxRequestNum = None
        self.IsHide = None
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
        self.InitQuota = params.get("InitQuota")
        self.MaxRequestNumPreSec = params.get("MaxRequestNumPreSec")
        self.MaxRequestNum = params.get("MaxRequestNum")
        self.IsHide = params.get("IsHide")
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
        """
        :param UsagePlanId: 使用计划唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanId: str\n        :param UsagePlanName: 用户自定义的使用计划名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanName: str\n        :param UsagePlanDesc: 用户自定义的使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanDesc: str\n        :param MaxRequestNumPreSec: 每秒最大请求次数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRequestNumPreSec: int\n        :param MaxRequestNum: 请求配额总量，-1表示没有限制。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxRequestNum: int\n        :param CreatedTime: 创建时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ModifiedTime: 最后修改时间。按照 ISO8601 标准表示，并且使用 UTC 时间。格式为：YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifiedTime: str\n        """
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
        """
        :param TotalCount: 符合条件的使用计划数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param UsagePlanStatusSet: 使用计划列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UsagePlanStatusSet: list of UsagePlanStatusInfo\n        """
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
        