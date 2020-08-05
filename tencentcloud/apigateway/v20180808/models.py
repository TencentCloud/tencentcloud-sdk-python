# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class ApiEnvironmentStrategy(AbstractModel):
    """api环境绑定策略

    """

    def __init__(self):
        """
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


class ApiEnvironmentStrategyStataus(AbstractModel):
    """API绑定策略列表

    """

    def __init__(self):
        """
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


class ApiIdStatus(AbstractModel):
    """API状态

    """

    def __init__(self):
        """
        :param ServiceId: 服务唯一ID。
        :type ServiceId: str
        :param ApiId: API唯一ID。
        :type ApiId: str
        :param ApiDesc: API描述
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


class ApiInfo(AbstractModel):
    """展示api信息

    """

    def __init__(self):
        """
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
        :type ServiceParameters: list of ServiceParameter
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


class ApiKey(AbstractModel):
    """密钥详情

    """

    def __init__(self):
        """
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


class ApiKeysStatus(AbstractModel):
    """密钥列表

    """

    def __init__(self):
        """
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


class ApiRequestConfig(AbstractModel):
    """api请求配置

    """

    def __init__(self):
        """
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


class ApiUsagePlan(AbstractModel):
    """api或service绑定使用计划详情

    """

    def __init__(self):
        """
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


class ApiUsagePlanSet(AbstractModel):
    """api绑定使用计划列表

    """

    def __init__(self):
        """
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


class ApisStatus(AbstractModel):
    """描述api列表状态

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的 API 接口数量。
        :type TotalCount: int
        :param ApiIdStatusSet: API 接口列表。
        :type ApiIdStatusSet: list of DesApisStatus
        """
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


class BindEnvironmentRequest(AbstractModel):
    """BindEnvironment请求参数结构体

    """

    def __init__(self):
        """
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


class BindEnvironmentResponse(AbstractModel):
    """BindEnvironment返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class BindIPStrategyResponse(AbstractModel):
    """BindIPStrategy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class BindSecretIdsResponse(AbstractModel):
    """BindSecretIds返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        self.ServiceId = None
        self.SubDomain = None
        self.Protocol = None
        self.NetType = None
        self.IsDefaultMapping = None
        self.NetSubDomain = None
        self.CertificateId = None
        self.PathMappingSet = None


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


class BindSubDomainResponse(AbstractModel):
    """BindSubDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ConstantParameter(AbstractModel):
    """常量参数

    """

    def __init__(self):
        """
        :param Name: 常量参数名称。只有 ServiceType 是 HTTP 才会用到此参数。
        :type Name: str
        :param Desc: 常量参数描述。只有 ServiceType 是 HTTP 才会用到此参数。
        :type Desc: str
        :param Position: 常量参数位置。只有 ServiceType 是 HTTP 才会用到此参数。
        :type Position: str
        :param DefaultValue: 常量参数默认值。只有 ServiceType 是 HTTP 才会用到此参数。
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


class CreateApiKeyRequest(AbstractModel):
    """CreateApiKey请求参数结构体

    """

    def __init__(self):
        """
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


class CreateApiKeyResponse(AbstractModel):
    """CreateApiKey返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param ServiceType: API 的后端服务类型。支持HTTP、MOCK、TSF、CLB、SCF、WEBSOCKET、TARGET（内测）。
        :type ServiceType: str
        :param ServiceTimeout: API 的后端服务超时时间，单位是秒。
        :type ServiceTimeout: int
        :param Protocol: API 的前端请求类型，如 HTTP 或 HTTPS 或者 HTTP 和 HTTPS。
        :type Protocol: str
        :param RequestConfig: 请求的前端配置。
        :type RequestConfig: :class:`tencentcloud.apigateway.v20180808.models.ApiRequestConfig`
        :param ApiName: 用户自定义的 API 名称。
        :type ApiName: str
        :param ApiDesc: 用户自定义的 API 接口描述。
        :type ApiDesc: str
        :param ApiType: API 类型，支持NORMAL（普通API）和TSF（微服务API），默认为NORMAL。
        :type ApiType: str
        :param AuthType: API 鉴权类型。支持SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH。默认为NONE。
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


class CreateApiResponse(AbstractModel):
    """CreateApi返回参数结构体

    """

    def __init__(self):
        """
        :param Result: api信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.CreateApiRsp`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ApiId: str
        :param Path: path
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Method: method
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


class CreateIPStrategyRequest(AbstractModel):
    """CreateIPStrategy请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 服务的唯一ID。
        :type ServiceId: str
        :param StrategyName: 用户自定义的策略名称。
        :type StrategyName: str
        :param StrategyType: 策略类型。支持WHITE（白名单）和BLACK（黑名单）。
        :type StrategyType: str
        :param StrategyData: 策略详情。
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


class CreateIPStrategyResponse(AbstractModel):
    """CreateIPStrategy返回参数结构体

    """

    def __init__(self):
        """
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


class CreateServiceRequest(AbstractModel):
    """CreateService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceName: 用户自定义的服务名称。如果没传，则系统自动生成一个唯一名称。
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
        """
        self.ServiceName = None
        self.Protocol = None
        self.ServiceDesc = None
        self.ExclusiveSetName = None
        self.NetTypes = None
        self.IpVersion = None
        self.SetServerName = None
        self.AppIdType = None


    def _deserialize(self, params):
        self.ServiceName = params.get("ServiceName")
        self.Protocol = params.get("Protocol")
        self.ServiceDesc = params.get("ServiceDesc")
        self.ExclusiveSetName = params.get("ExclusiveSetName")
        self.NetTypes = params.get("NetTypes")
        self.IpVersion = params.get("IpVersion")
        self.SetServerName = params.get("SetServerName")
        self.AppIdType = params.get("AppIdType")


class CreateServiceResponse(AbstractModel):
    """CreateService返回参数结构体

    """

    def __init__(self):
        """
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


class CreateUsagePlanRequest(AbstractModel):
    """CreateUsagePlan请求参数结构体

    """

    def __init__(self):
        """
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


class CreateUsagePlanResponse(AbstractModel):
    """CreateUsagePlan返回参数结构体

    """

    def __init__(self):
        """
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


class DeleteApiKeyRequest(AbstractModel):
    """DeleteApiKey请求参数结构体

    """

    def __init__(self):
        """
        :param AccessKeyId: 待删除的密钥 ID。
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")


class DeleteApiKeyResponse(AbstractModel):
    """DeleteApiKey返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DeleteApiResponse(AbstractModel):
    """DeleteApi返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DeleteIPStrategyResponse(AbstractModel):
    """DeleteIPStrategy返回参数结构体

    """

    def __init__(self):
        """
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


class DeleteServiceRequest(AbstractModel):
    """DeleteService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待删除服务的唯一 ID。
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")


class DeleteServiceResponse(AbstractModel):
    """DeleteService返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DeleteServiceSubDomainMappingResponse(AbstractModel):
    """DeleteServiceSubDomainMapping返回参数结构体

    """

    def __init__(self):
        """
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


class DeleteUsagePlanRequest(AbstractModel):
    """DeleteUsagePlan请求参数结构体

    """

    def __init__(self):
        """
        :param UsagePlanId: 待删除的使用计划唯一 ID。
        :type UsagePlanId: str
        """
        self.UsagePlanId = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")


class DeleteUsagePlanResponse(AbstractModel):
    """DeleteUsagePlan返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DemoteServiceUsagePlanResponse(AbstractModel):
    """DemoteServiceUsagePlan返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        :param AuthType: API 鉴权类型。取值为SECRET（密钥对鉴权）、NONE（免鉴权）、OAUTH。
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


class DescribeApiEnvironmentStrategyRequest(AbstractModel):
    """DescribeApiEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeApiEnvironmentStrategyResponse(AbstractModel):
    """DescribeApiEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeApiKeyRequest(AbstractModel):
    """DescribeApiKey请求参数结构体

    """

    def __init__(self):
        """
        :param AccessKeyId: API 密钥 ID。
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")


class DescribeApiKeyResponse(AbstractModel):
    """DescribeApiKey返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeApiKeysStatusResponse(AbstractModel):
    """DescribeApiKeysStatus返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeApiResponse(AbstractModel):
    """DescribeApi返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeApiUsagePlanRequest(AbstractModel):
    """DescribeApiUsagePlan请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeApiUsagePlanResponse(AbstractModel):
    """DescribeApiUsagePlan返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param ServiceId: API 所在的服务唯一 ID。
        :type ServiceId: str
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Limit: 返回数量，默认为 20，最大值为 100
        :type Limit: int
        :param Filters: API过滤条件。支持ApiId、ApiName、ApiPath、ApiType、AuthRelationApiId、AuthType、ApiBuniessType、NotUsagePlanId、Environment、Tags (values为 $tag_key:tag_value的列表)、TagKeys （values 为 tag key的列表）。
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


class DescribeApisStatusResponse(AbstractModel):
    """DescribeApisStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Result: API 详情列表。
        :type Result: :class:`tencentcloud.apigateway.v20180808.models.ApisStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeIPStrategyApisStatusResponse(AbstractModel):
    """DescribeIPStrategyApisStatus返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeIPStrategyResponse(AbstractModel):
    """DescribeIPStrategy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeIPStrategysStatusResponse(AbstractModel):
    """DescribeIPStrategysStatus返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeLogSearchResponse(AbstractModel):
    """DescribeLogSearch返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeServiceEnvironmentListRequest(AbstractModel):
    """DescribeServiceEnvironmentList请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeServiceEnvironmentListResponse(AbstractModel):
    """DescribeServiceEnvironmentList返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeServiceEnvironmentReleaseHistoryResponse(AbstractModel):
    """DescribeServiceEnvironmentReleaseHistory返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeServiceEnvironmentStrategyResponse(AbstractModel):
    """DescribeServiceEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeServiceReleaseVersionRequest(AbstractModel):
    """DescribeServiceReleaseVersion请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeServiceReleaseVersionResponse(AbstractModel):
    """DescribeServiceReleaseVersion返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeServiceRequest(AbstractModel):
    """DescribeService请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceId: 待查询的服务唯一 ID。
        :type ServiceId: str
        """
        self.ServiceId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")


class DescribeServiceResponse(AbstractModel):
    """DescribeService返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeServiceSubDomainMappingsRequest(AbstractModel):
    """DescribeServiceSubDomainMappings请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeServiceSubDomainMappingsResponse(AbstractModel):
    """DescribeServiceSubDomainMappings返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeServiceSubDomainsResponse(AbstractModel):
    """DescribeServiceSubDomains返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeServiceUsagePlanResponse(AbstractModel):
    """DescribeServiceUsagePlan返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param Offset: 偏移量，默认为 0。
        :type Offset: int
        :param Filters: 过滤条件。支持ServiceId、ServiceName、NotUsagePlanId、Environment、IpVersion。
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


class DescribeServicesStatusResponse(AbstractModel):
    """DescribeServicesStatus返回参数结构体

    """

    def __init__(self):
        """
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


class DescribeUsagePlanEnvironmentsRequest(AbstractModel):
    """DescribeUsagePlanEnvironments请求参数结构体

    """

    def __init__(self):
        """
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


class DescribeUsagePlanEnvironmentsResponse(AbstractModel):
    """DescribeUsagePlanEnvironments返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param UsagePlanId: 待查询的使用计划唯一 ID。
        :type UsagePlanId: str
        """
        self.UsagePlanId = None


    def _deserialize(self, params):
        self.UsagePlanId = params.get("UsagePlanId")


class DescribeUsagePlanResponse(AbstractModel):
    """DescribeUsagePlan返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeUsagePlanSecretIdsResponse(AbstractModel):
    """DescribeUsagePlanSecretIds返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DescribeUsagePlansStatusResponse(AbstractModel):
    """DescribeUsagePlansStatus返回参数结构体

    """

    def __init__(self):
        """
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


class DisableApiKeyRequest(AbstractModel):
    """DisableApiKey请求参数结构体

    """

    def __init__(self):
        """
        :param AccessKeyId: 待禁用的密钥 ID。
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")


class DisableApiKeyResponse(AbstractModel):
    """DisableApiKey返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class DomainSetList(AbstractModel):
    """服务自定义域名列表

    """

    def __init__(self):
        """
        :param DomainName: 域名名称。
        :type DomainName: str
        :param Status: 域名解析状态。True 表示正常解析，False 表示解析失败。
        :type Status: int
        :param CertificateId: 证书ID。
        :type CertificateId: str
        :param IsDefaultMapping: 是否使用默认路径映射。
        :type IsDefaultMapping: bool
        :param Protocol: 自定义域名协议类型。
        :type Protocol: str
        :param NetType: 网络类型（'INNER' 或 'OUTER'）。
        :type NetType: str
        """
        self.DomainName = None
        self.Status = None
        self.CertificateId = None
        self.IsDefaultMapping = None
        self.Protocol = None
        self.NetType = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Status = params.get("Status")
        self.CertificateId = params.get("CertificateId")
        self.IsDefaultMapping = params.get("IsDefaultMapping")
        self.Protocol = params.get("Protocol")
        self.NetType = params.get("NetType")


class DomainSets(AbstractModel):
    """自定义服务域名展示

    """

    def __init__(self):
        """
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


class EnableApiKeyRequest(AbstractModel):
    """EnableApiKey请求参数结构体

    """

    def __init__(self):
        """
        :param AccessKeyId: 待启用的密钥 ID。
        :type AccessKeyId: str
        """
        self.AccessKeyId = None


    def _deserialize(self, params):
        self.AccessKeyId = params.get("AccessKeyId")


class EnableApiKeyResponse(AbstractModel):
    """EnableApiKey返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class EnvironmentStrategy(AbstractModel):
    """环境限流

    """

    def __init__(self):
        """
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


class ErrorCodes(AbstractModel):
    """用户自定义错误码

    """

    def __init__(self):
        """
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


class Filter(AbstractModel):
    """>描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > * 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > * 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >

    """

    def __init__(self):
        """
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


class GenerateApiDocumentRequest(AbstractModel):
    """GenerateApiDocument请求参数结构体

    """

    def __init__(self):
        """
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


class GenerateApiDocumentResponse(AbstractModel):
    """GenerateApiDocument返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param IsHealthCheck: 是否开启健康检查。
        :type IsHealthCheck: bool
        :param RequestVolumeThreshold: 健康检查阈值。
        :type RequestVolumeThreshold: int
        :param SleepWindowInMilliseconds: 窗口大小。
        :type SleepWindowInMilliseconds: int
        :param ErrorThresholdPercentage: 阈值百分比。
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


class IPStrategy(AbstractModel):
    """ip策略

    """

    def __init__(self):
        """
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


class IPStrategyApi(AbstractModel):
    """策略绑定api列表

    """

    def __init__(self):
        """
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


class IPStrategyApiStatus(AbstractModel):
    """ip策略绑定api详情

    """

    def __init__(self):
        """
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


class IPStrategysStatus(AbstractModel):
    """策略列表

    """

    def __init__(self):
        """
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


class LogQuery(AbstractModel):
    """检索条件入参

    """

    def __init__(self):
        """
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


class MicroService(AbstractModel):
    """API绑定的微服务信息。

    """

    def __init__(self):
        """
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


class MicroServiceReq(AbstractModel):
    """tsf类型入参

    """

    def __init__(self):
        """
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


class ModifyApiEnvironmentStrategyRequest(AbstractModel):
    """ModifyApiEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyApiEnvironmentStrategyResponse(AbstractModel):
    """ModifyApiEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ModifyApiIncrementResponse(AbstractModel):
    """ModifyApiIncrement返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        :param AuthType: API 鉴权类型。支持SECRET、NONE、OAUTH。默认为NONE。
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


class ModifyApiResponse(AbstractModel):
    """ModifyApi返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIPStrategyRequest(AbstractModel):
    """ModifyIPStrategy请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyIPStrategyResponse(AbstractModel):
    """ModifyIPStrategy返回参数结构体

    """

    def __init__(self):
        """
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


class ModifyServiceEnvironmentStrategyRequest(AbstractModel):
    """ModifyServiceEnvironmentStrategy请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyServiceEnvironmentStrategyResponse(AbstractModel):
    """ModifyServiceEnvironmentStrategy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class ModifyServiceResponse(AbstractModel):
    """ModifyService返回参数结构体

    """

    def __init__(self):
        """
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
        """
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
        """
        self.ServiceId = None
        self.SubDomain = None
        self.IsDefaultMapping = None
        self.CertificateId = None
        self.Protocol = None
        self.PathMappingSet = None
        self.NetType = None


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


class ModifySubDomainResponse(AbstractModel):
    """ModifySubDomain返回参数结构体

    """

    def __init__(self):
        """
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


class ModifyUsagePlanRequest(AbstractModel):
    """ModifyUsagePlan请求参数结构体

    """

    def __init__(self):
        """
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


class ModifyUsagePlanResponse(AbstractModel):
    """ModifyUsagePlan返回参数结构体

    """

    def __init__(self):
        """
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


class OauthConfig(AbstractModel):
    """Oauth授权配置信息

    """

    def __init__(self):
        """
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


class PathMapping(AbstractModel):
    """自定义域名的路径映射。

    """

    def __init__(self):
        """
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


class ReleaseService(AbstractModel):
    """发布服务返回

    """

    def __init__(self):
        """
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


class ReleaseServiceRequest(AbstractModel):
    """ReleaseService请求参数结构体

    """

    def __init__(self):
        """
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


class ReleaseServiceResponse(AbstractModel):
    """ReleaseService返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Name: API 的前端参数名称。
        :type Name: str
        :param Position: API 的前端参数位置，如 head。目前支持 head、query、path。
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


class RequestConfig(AbstractModel):
    """前端路径配置

    """

    def __init__(self):
        """
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


class RequestParameter(AbstractModel):
    """请求参数

    """

    def __init__(self):
        """
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


class ResponseErrorCodeReq(AbstractModel):
    """错误码入参

    """

    def __init__(self):
        """
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


class Service(AbstractModel):
    """展示服务列表用

    """

    def __init__(self):
        """
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


class ServiceConfig(AbstractModel):
    """ServiceConfig

    """

    def __init__(self):
        """
        :param Product: 后端类型。启用vpc时生效，目前支持的类型为clb。
        :type Product: str
        :param UniqVpcId: vpc 的唯一ID。
        :type UniqVpcId: str
        :param Url: API 的后端服务url。如果ServiceType是HTTP，则此参数必传。
        :type Url: str
        :param Path: API 的后端服务路径，如 /path。如果 ServiceType 是 HTTP，则此参数必传。前后端路径可不同。
        :type Path: str
        :param Method: API的后端服务请求方法，如 GET。如果 ServiceType 是 HTTP，则此参数必传。前后端方法可不同。
        :type Method: str
        """
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


class ServiceEnvironmentSet(AbstractModel):
    """服务绑定环境详情

    """

    def __init__(self):
        """
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


class ServiceEnvironmentStrategy(AbstractModel):
    """服务环境策略

    """

    def __init__(self):
        """
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
        """
        self.EnvironmentName = None
        self.Url = None
        self.Status = None
        self.VersionName = None
        self.Strategy = None


    def _deserialize(self, params):
        self.EnvironmentName = params.get("EnvironmentName")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.VersionName = params.get("VersionName")
        self.Strategy = params.get("Strategy")


class ServiceEnvironmentStrategyStatus(AbstractModel):
    """环境绑定策略列表

    """

    def __init__(self):
        """
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


class ServiceParameter(AbstractModel):
    """ServiceParameter

    """

    def __init__(self):
        """
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


class ServiceReleaseHistory(AbstractModel):
    """服务发布历史

    """

    def __init__(self):
        """
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


class ServiceReleaseHistoryInfo(AbstractModel):
    """服务发布列表详情

    """

    def __init__(self):
        """
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


class ServiceReleaseVersion(AbstractModel):
    """服务发布版本

    """

    def __init__(self):
        """
        :param TotalCount: 发布版本总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param VersionList: 发布版本列表。
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


class ServiceSubDomainMappings(AbstractModel):
    """服务自定义域名路径映射

    """

    def __init__(self):
        """
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


class ServiceUsagePlanSet(AbstractModel):
    """服务绑定使用计划列表

    """

    def __init__(self):
        """
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


class ServicesStatus(AbstractModel):
    """服务列表展示

    """

    def __init__(self):
        """
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


class Tag(AbstractModel):
    """API绑定的标签信息。

    """

    def __init__(self):
        """
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


class TargetServicesReq(AbstractModel):
    """tsf serverless入参

    """

    def __init__(self):
        """
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


class TsfLoadBalanceConfResp(AbstractModel):
    """TsfLoadBalanceConf 出参使用

    """

    def __init__(self):
        """
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


class UnBindEnvironmentRequest(AbstractModel):
    """UnBindEnvironment请求参数结构体

    """

    def __init__(self):
        """
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


class UnBindEnvironmentResponse(AbstractModel):
    """UnBindEnvironment返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UnBindIPStrategyResponse(AbstractModel):
    """UnBindIPStrategy返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UnBindSecretIdsResponse(AbstractModel):
    """UnBindSecretIds返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UnBindSubDomainResponse(AbstractModel):
    """UnBindSubDomain返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UnReleaseServiceResponse(AbstractModel):
    """UnReleaseService返回参数结构体

    """

    def __init__(self):
        """
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


class UpdateApiKeyRequest(AbstractModel):
    """UpdateApiKey请求参数结构体

    """

    def __init__(self):
        """
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


class UpdateApiKeyResponse(AbstractModel):
    """UpdateApiKey返回参数结构体

    """

    def __init__(self):
        """
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
        """
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


class UpdateServiceResponse(AbstractModel):
    """UpdateService返回参数结构体

    """

    def __init__(self):
        """
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


class UsagePlan(AbstractModel):
    """usagePlan详情

    """

    def __init__(self):
        """
        :param Environment: 环境名称。
        :type Environment: str
        :param UsagePlanId: 使用计划唯一ID。
        :type UsagePlanId: str
        :param UsagePlanName: 使用计划名称。
        :type UsagePlanName: str
        :param UsagePlanDesc: 使用计划描述。
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


class UsagePlanBindEnvironment(AbstractModel):
    """使用计划绑定环境信息

    """

    def __init__(self):
        """
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


class UsagePlanBindSecret(AbstractModel):
    """使用计划绑定密钥

    """

    def __init__(self):
        """
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


class UsagePlanBindSecretStatus(AbstractModel):
    """使用计划绑定密钥列表

    """

    def __init__(self):
        """
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


class UsagePlanEnvironment(AbstractModel):
    """使用计划绑定环境详情。

    """

    def __init__(self):
        """
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


class UsagePlanEnvironmentStatus(AbstractModel):
    """使用计划绑定环境的列表。

    """

    def __init__(self):
        """
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


class UsagePlanInfo(AbstractModel):
    """使用计划详情。

    """

    def __init__(self):
        """
        :param UsagePlanId: 使用计划唯一 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanId: str
        :param UsagePlanName: 使用计划名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanName: str
        :param UsagePlanDesc: 使用计划描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type UsagePlanDesc: str
        :param InitQuota: 初始化调用次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type InitQuota: int
        :param MaxRequestNumPreSec: 每秒请求限制数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNumPreSec: int
        :param MaxRequestNum: 最大调用次数。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxRequestNum: int
        :param IsHide: 是否隐藏。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsHide: int
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


class UsagePlanStatusInfo(AbstractModel):
    """用于使用计划列表展示

    """

    def __init__(self):
        """
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


class UsagePlansStatus(AbstractModel):
    """使用计划列表

    """

    def __init__(self):
        """
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