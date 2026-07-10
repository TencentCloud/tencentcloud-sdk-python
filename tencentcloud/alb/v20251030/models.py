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


class AccessLogConfig(AbstractModel):
    r"""访问日志配置。

    """

    def __init__(self):
        r"""
        :param _LogSetId: 负载均衡日志服务(CLS)的日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogSetId: str
        :param _LogTopicId: 负载均衡日志服务(CLS)的日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogTopicId: str
        """
        self._LogSetId = None
        self._LogTopicId = None

    @property
    def LogSetId(self):
        r"""负载均衡日志服务(CLS)的日志集ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogSetId

    @LogSetId.setter
    def LogSetId(self, LogSetId):
        self._LogSetId = LogSetId

    @property
    def LogTopicId(self):
        r"""负载均衡日志服务(CLS)的日志主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LogTopicId

    @LogTopicId.setter
    def LogTopicId(self, LogTopicId):
        self._LogTopicId = LogTopicId


    def _deserialize(self, params):
        self._LogSetId = params.get("LogSetId")
        self._LogTopicId = params.get("LogTopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTargetsToTargetGroupRequest(AbstractModel):
    r"""AddTargetsToTargetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupId: str
        :param _Targets: 需要添加至目标组的后端服务列表。单次请求最多支持添加 **50** 个后端服务。
        :type Targets: list of TargetToAdd
        :param _DryRun: 是否预览此次请求。 
- **false**（默认）：发送普通请求，直接添加后端服务至目标组。 
- **true**：发送预览请求，检查添加后端服务的参数、格式、业务限制等是否符合要求。
        :type DryRun: bool
        """
        self._TargetGroupId = None
        self._Targets = None
        self._DryRun = None

    @property
    def TargetGroupId(self):
        r"""目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Targets(self):
        r"""需要添加至目标组的后端服务列表。单次请求最多支持添加 **50** 个后端服务。
        :rtype: list of TargetToAdd
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def DryRun(self):
        r"""是否预览此次请求。 
- **false**（默认）：发送普通请求，直接添加后端服务至目标组。 
- **true**：发送预览请求，检查添加后端服务的参数、格式、业务限制等是否符合要求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetToAdd()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddTargetsToTargetGroupResponse(AbstractModel):
    r"""AddTargetsToTargetGroup返回参数结构体

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


class AssociateBandwidthPackageWithLoadBalancerRequest(AbstractModel):
    r"""AssociateBandwidthPackageWithLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BandwidthPackageId: 共享带宽包 ID。
        :type BandwidthPackageId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。

> 若您未指定，则系统自动使用API请求的**RequestId**作为**ClientToken**标识。每次API请求的**RequestId**不一样。
        :type ClientToken: str
        :param _DryRun: 是否只预检此次请求。取值：
- **true**：发送检查请求，不会将共享带宽包绑定到负载均衡实例。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。
- **false**（默认值）：发送正常请求，通过检查后返回HTTP 2xx状态码并直接进行操作。
        :type DryRun: bool
        """
        self._BandwidthPackageId = None
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def BandwidthPackageId(self):
        r"""共享带宽包 ID。
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。

> 若您未指定，则系统自动使用API请求的**RequestId**作为**ClientToken**标识。每次API请求的**RequestId**不一样。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""是否只预检此次请求。取值：
- **true**：发送检查请求，不会将共享带宽包绑定到负载均衡实例。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。
- **false**（默认值）：发送正常请求，通过检查后返回HTTP 2xx状态码并直接进行操作。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateBandwidthPackageWithLoadBalancerResponse(AbstractModel):
    r"""AssociateBandwidthPackageWithLoadBalancer返回参数结构体

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


class AssociateListenerAdditionalCertificatesRequest(AbstractModel):
    r"""AssociateListenerAdditionalCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 扩展证书 ID 列表。
        :type CertificateIds: list of str
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _ClientToken: 客户端 Token，用于保证请求的幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken 只支持 ASCII 字符。
若您未指定，则系统自动使用 API 请求的 RequestId 作为 ClientToken 标识。每次 API 请求的 RequestId 不一样。
        :type ClientToken: str
        :param _DryRun: 是否只预检此次请求，取值：
true：发送检查请求，不会为HTTPS和QUIC监听器添加扩展证书。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码DryRunOperation。
false（默认值）：发送正常请求，通过检查后返回HTTP2xx状态码并直接进行操作。
        :type DryRun: str
        """
        self._CertificateIds = None
        self._ListenerId = None
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def CertificateIds(self):
        r"""扩展证书 ID 列表。
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""客户端 Token，用于保证请求的幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken 只支持 ASCII 字符。
若您未指定，则系统自动使用 API 请求的 RequestId 作为 ClientToken 标识。每次 API 请求的 RequestId 不一样。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""是否只预检此次请求，取值：
true：发送检查请求，不会为HTTPS和QUIC监听器添加扩展证书。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码DryRunOperation。
false（默认值）：发送正常请求，通过检查后返回HTTP2xx状态码并直接进行操作。
        :rtype: str
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateListenerAdditionalCertificatesResponse(AbstractModel):
    r"""AssociateListenerAdditionalCertificates返回参数结构体

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


class CertificateInfo(AbstractModel):
    r"""证书信息

    """

    def __init__(self):
        r"""
        :param _AssociatedTime: 证书绑定时间。
        :type AssociatedTime: str
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _CertificateType: 证书类型。取值：CA或SVR（服务器证书）。
        :type CertificateType: str
        :param _IsDefault: 是否为监听器默认证书。取值：
true：默认证书。
false：扩展证书。
        :type IsDefault: bool
        :param _Status: 证书与监听器的绑定状态。取值：Associated（已关联）、Associating（关联中）、Disassociating（解除关联中）、Error（异常）。
        :type Status: str
        """
        self._AssociatedTime = None
        self._CertificateId = None
        self._CertificateType = None
        self._IsDefault = None
        self._Status = None

    @property
    def AssociatedTime(self):
        r"""证书绑定时间。
        :rtype: str
        """
        return self._AssociatedTime

    @AssociatedTime.setter
    def AssociatedTime(self, AssociatedTime):
        self._AssociatedTime = AssociatedTime

    @property
    def CertificateId(self):
        r"""证书 ID。
        :rtype: str
        """
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateType(self):
        r"""证书类型。取值：CA或SVR（服务器证书）。
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def IsDefault(self):
        r"""是否为监听器默认证书。取值：
true：默认证书。
false：扩展证书。
        :rtype: bool
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def Status(self):
        r"""证书与监听器的绑定状态。取值：Associated（已关联）、Associating（关联中）、Disassociating（解除关联中）、Error（异常）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._AssociatedTime = params.get("AssociatedTime")
        self._CertificateId = params.get("CertificateId")
        self._CertificateType = params.get("CertificateType")
        self._IsDefault = params.get("IsDefault")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHealthCheckTemplateRequest(AbstractModel):
    r"""CreateHealthCheckTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DryRun: 是否预览此次请求。
- **false**（默认）：发送普通请求，直接修改健康检查模板。
- **true**：发送预览请求，检查修改健康检查模板的参数、格式、业务限制等是否符合要求。
        :type DryRun: bool
        :param _HealthCheckCodes: 健康检查状态码。取值：
- 当健康检查协议为**HTTP/HTTPS**时：
	- **http_1xx**
	- **http_2xx**（默认值）
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- 当健康检查协议为**GRPC/GRPCS**时：默认值为**12**，数值范围为**0-99**，输入值可为数值、多个数值或者范围以及相互组合，如：
	- **"20"**
	- **"0-99"**
        :type HealthCheckCodes: list of str
        :param _HealthCheckHealthyThreshold: 判定后端服务健康的阈值，当健康检查连续成功多少次后，后端服务的状态由**不健康**变为**健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :type HealthCheckHealthyThreshold: int
        :param _HealthCheckHost: 健康检查域名。
长度限制为 **1-255** 个字符。
可包含小写字母、数字、短划线（-）和半角句号（.）。

> 仅当 **HealthCheckProtocol** 设置为 **HTTP/HTTPS/GRPC/GRPCS** 时，该参数生效。
        :type HealthCheckHost: str
        :param _HealthCheckHttpVersion: 健康检查 HTTP 协议版本，取值：
- **HTTP1.1**（默认）
- **HTTP1.0** 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :type HealthCheckHttpVersion: str
        :param _HealthCheckInterval: 健康检查的时间间隔。单位：秒。 取值范围：**2**-**300**。 默认值：**5**。
        :type HealthCheckInterval: int
        :param _HealthCheckMethod: 健康检查方法，取值： - **GET** - **HEAD**（默认值） 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :type HealthCheckMethod: str
        :param _HealthCheckPath: 健康检查的转发规则路径。 长度为 **1-80** 个字符，只能使用字母、数字、字符`-/.%?#&=`以及扩展字符`_;~!（)*[]@$^:',+`。 URL 必须以正斜线（/）开头。 
> 仅当**HealthCheckProtocol**为**HTTP/HTTPS/GRPC/GRPCS**时，转发规则路径参数生效。
        :type HealthCheckPath: str
        :param _HealthCheckPort: 健康检查访问后端服务器的端口。  取值范围：**0-65535**。  默认值：**0**，表示后端服务器的端口。
        :type HealthCheckPort: int
        :param _HealthCheckProtocol: 健康检查协议。取值：
- **HTTP**（默认）：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。
- **HTTPS**：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。（数据加密，相比 HTTP 更安全。）
- **TCP**：通过发送 SYN 握手报文来检测服务器端口是否存活。
- **GRPC**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
- **GRPCS**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
        :type HealthCheckProtocol: str
        :param _HealthCheckTemplateName: 健康检查模板名称。长度为 **1-255** 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :type HealthCheckTemplateName: str
        :param _HealthCheckTimeout: 健康检查的响应超时时间。单位：秒。
取值范围：**2**-**60**。
默认值：**2**。
        :type HealthCheckTimeout: int
        :param _HealthCheckUnhealthyThreshold: 判定后端服务不健康的阈值，当健康检查连续失败多少次后，后端服务的状态由**健康**变为**不健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :type HealthCheckUnhealthyThreshold: int
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        """
        self._DryRun = None
        self._HealthCheckCodes = None
        self._HealthCheckHealthyThreshold = None
        self._HealthCheckHost = None
        self._HealthCheckHttpVersion = None
        self._HealthCheckInterval = None
        self._HealthCheckMethod = None
        self._HealthCheckPath = None
        self._HealthCheckPort = None
        self._HealthCheckProtocol = None
        self._HealthCheckTemplateName = None
        self._HealthCheckTimeout = None
        self._HealthCheckUnhealthyThreshold = None
        self._Tags = None

    @property
    def DryRun(self):
        r"""是否预览此次请求。
- **false**（默认）：发送普通请求，直接修改健康检查模板。
- **true**：发送预览请求，检查修改健康检查模板的参数、格式、业务限制等是否符合要求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def HealthCheckCodes(self):
        r"""健康检查状态码。取值：
- 当健康检查协议为**HTTP/HTTPS**时：
	- **http_1xx**
	- **http_2xx**（默认值）
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- 当健康检查协议为**GRPC/GRPCS**时：默认值为**12**，数值范围为**0-99**，输入值可为数值、多个数值或者范围以及相互组合，如：
	- **"20"**
	- **"0-99"**
        :rtype: list of str
        """
        return self._HealthCheckCodes

    @HealthCheckCodes.setter
    def HealthCheckCodes(self, HealthCheckCodes):
        self._HealthCheckCodes = HealthCheckCodes

    @property
    def HealthCheckHealthyThreshold(self):
        r"""判定后端服务健康的阈值，当健康检查连续成功多少次后，后端服务的状态由**不健康**变为**健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckHealthyThreshold

    @HealthCheckHealthyThreshold.setter
    def HealthCheckHealthyThreshold(self, HealthCheckHealthyThreshold):
        self._HealthCheckHealthyThreshold = HealthCheckHealthyThreshold

    @property
    def HealthCheckHost(self):
        r"""健康检查域名。
长度限制为 **1-255** 个字符。
可包含小写字母、数字、短划线（-）和半角句号（.）。

> 仅当 **HealthCheckProtocol** 设置为 **HTTP/HTTPS/GRPC/GRPCS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckHost

    @HealthCheckHost.setter
    def HealthCheckHost(self, HealthCheckHost):
        self._HealthCheckHost = HealthCheckHost

    @property
    def HealthCheckHttpVersion(self):
        r"""健康检查 HTTP 协议版本，取值：
- **HTTP1.1**（默认）
- **HTTP1.0** 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckHttpVersion

    @HealthCheckHttpVersion.setter
    def HealthCheckHttpVersion(self, HealthCheckHttpVersion):
        self._HealthCheckHttpVersion = HealthCheckHttpVersion

    @property
    def HealthCheckInterval(self):
        r"""健康检查的时间间隔。单位：秒。 取值范围：**2**-**300**。 默认值：**5**。
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def HealthCheckMethod(self):
        r"""健康检查方法，取值： - **GET** - **HEAD**（默认值） 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod

    @property
    def HealthCheckPath(self):
        r"""健康检查的转发规则路径。 长度为 **1-80** 个字符，只能使用字母、数字、字符`-/.%?#&=`以及扩展字符`_;~!（)*[]@$^:',+`。 URL 必须以正斜线（/）开头。 
> 仅当**HealthCheckProtocol**为**HTTP/HTTPS/GRPC/GRPCS**时，转发规则路径参数生效。
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckPort(self):
        r"""健康检查访问后端服务器的端口。  取值范围：**0-65535**。  默认值：**0**，表示后端服务器的端口。
        :rtype: int
        """
        return self._HealthCheckPort

    @HealthCheckPort.setter
    def HealthCheckPort(self, HealthCheckPort):
        self._HealthCheckPort = HealthCheckPort

    @property
    def HealthCheckProtocol(self):
        r"""健康检查协议。取值：
- **HTTP**（默认）：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。
- **HTTPS**：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。（数据加密，相比 HTTP 更安全。）
- **TCP**：通过发送 SYN 握手报文来检测服务器端口是否存活。
- **GRPC**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
- **GRPCS**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
        :rtype: str
        """
        return self._HealthCheckProtocol

    @HealthCheckProtocol.setter
    def HealthCheckProtocol(self, HealthCheckProtocol):
        self._HealthCheckProtocol = HealthCheckProtocol

    @property
    def HealthCheckTemplateName(self):
        r"""健康检查模板名称。长度为 **1-255** 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :rtype: str
        """
        return self._HealthCheckTemplateName

    @HealthCheckTemplateName.setter
    def HealthCheckTemplateName(self, HealthCheckTemplateName):
        self._HealthCheckTemplateName = HealthCheckTemplateName

    @property
    def HealthCheckTimeout(self):
        r"""健康检查的响应超时时间。单位：秒。
取值范围：**2**-**60**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckUnhealthyThreshold(self):
        r"""判定后端服务不健康的阈值，当健康检查连续失败多少次后，后端服务的状态由**健康**变为**不健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckUnhealthyThreshold

    @HealthCheckUnhealthyThreshold.setter
    def HealthCheckUnhealthyThreshold(self, HealthCheckUnhealthyThreshold):
        self._HealthCheckUnhealthyThreshold = HealthCheckUnhealthyThreshold

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        self._HealthCheckCodes = params.get("HealthCheckCodes")
        self._HealthCheckHealthyThreshold = params.get("HealthCheckHealthyThreshold")
        self._HealthCheckHost = params.get("HealthCheckHost")
        self._HealthCheckHttpVersion = params.get("HealthCheckHttpVersion")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckPort = params.get("HealthCheckPort")
        self._HealthCheckProtocol = params.get("HealthCheckProtocol")
        self._HealthCheckTemplateName = params.get("HealthCheckTemplateName")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckUnhealthyThreshold = params.get("HealthCheckUnhealthyThreshold")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHealthCheckTemplateResponse(AbstractModel):
    r"""CreateHealthCheckTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplateId: 健康检查模板 ID，格式为 hct- 后接字母数字。所有接口（创建、查询、修改、删除）均使用 hct- 前缀。
        :type HealthCheckTemplateId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthCheckTemplateId = None
        self._RequestId = None

    @property
    def HealthCheckTemplateId(self):
        r"""健康检查模板 ID，格式为 hct- 后接字母数字。所有接口（创建、查询、修改、删除）均使用 hct- 前缀。
        :rtype: str
        """
        return self._HealthCheckTemplateId

    @HealthCheckTemplateId.setter
    def HealthCheckTemplateId(self, HealthCheckTemplateId):
        self._HealthCheckTemplateId = HealthCheckTemplateId

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
        self._HealthCheckTemplateId = params.get("HealthCheckTemplateId")
        self._RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    r"""CreateListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DefaultActions: 默认转发规则动作列表。目前监听器仅支持添加 1 个默认转发规则动作。
        :type DefaultActions: list of DefaultAction
        :param _ListenerPort: 负载均衡实例前端使用的端口。  取值：1~65535。
        :type ListenerPort: int
        :param _ListenerProtocol: 监听协议。  取值：HTTP、HTTPS 或 QUIC。
        :type ListenerProtocol: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _CaCertificateIds: 监听器配置的CA证书ID列表。目前监听器仅支持添加 1 个 CA 证书。
当 CaEnabled 参数取值为 true 时，此参数必填。
        :type CaCertificateIds: list of str
        :param _CaEnabled: 是否开启双向认证。
取值：
true：开启。
false（默认值）：不开启。
        :type CaEnabled: bool
        :param _CertificateIds: 服务器证书 ID 列表。
        :type CertificateIds: list of str
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。  

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。
        :type ClientToken: str
        :param _GzipEnabled: 是否开启Gzip压缩。取值:true(默认值):是。false:否
        :type GzipEnabled: bool
        :param _Http2Enabled: 是否开启HTTP/2特性。HTTP 协议默认 false，HTTPS 协议默认 true。只有 HTTPS 协议支持此参数。
        :type Http2Enabled: bool
        :param _IdleTimeout: 连接空闲超时时间。单位：秒。
取值范围：1~600。
默认值：15。
如果在超时时间内一直没有访问请求，负载均衡会断开当前连接，在下次请求到来时创建新的连接。
        :type IdleTimeout: int
        :param _ListenerName: 自定义监听名称。  长度为 1~255 个字符，必须是中文和无害字符串中的字符，  可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :type ListenerName: str
        :param _RequestTimeout: 请求超时时间。单位：秒。
取值：1~600。
默认值：60。
如果在超时时间内后端服务器没有返回响应，负载均衡将放弃等待，并给客户端返回HTTP 504错误码。
        :type RequestTimeout: int
        :param _SecurityPolicyId: 安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :type SecurityPolicyId: str
        :param _Tags: 标签列表。最大支持20个。
        :type Tags: list of TagInfo
        :param _XForwardedForConfig: X-Forwarded-For配置
        :type XForwardedForConfig: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        self._DefaultActions = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._LoadBalancerId = None
        self._CaCertificateIds = None
        self._CaEnabled = None
        self._CertificateIds = None
        self._ClientToken = None
        self._GzipEnabled = None
        self._Http2Enabled = None
        self._IdleTimeout = None
        self._ListenerName = None
        self._RequestTimeout = None
        self._SecurityPolicyId = None
        self._Tags = None
        self._XForwardedForConfig = None

    @property
    def DefaultActions(self):
        r"""默认转发规则动作列表。目前监听器仅支持添加 1 个默认转发规则动作。
        :rtype: list of DefaultAction
        """
        return self._DefaultActions

    @DefaultActions.setter
    def DefaultActions(self, DefaultActions):
        self._DefaultActions = DefaultActions

    @property
    def ListenerPort(self):
        r"""负载均衡实例前端使用的端口。  取值：1~65535。
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""监听协议。  取值：HTTP、HTTPS 或 QUIC。
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def CaCertificateIds(self):
        r"""监听器配置的CA证书ID列表。目前监听器仅支持添加 1 个 CA 证书。
当 CaEnabled 参数取值为 true 时，此参数必填。
        :rtype: list of str
        """
        return self._CaCertificateIds

    @CaCertificateIds.setter
    def CaCertificateIds(self, CaCertificateIds):
        self._CaCertificateIds = CaCertificateIds

    @property
    def CaEnabled(self):
        r"""是否开启双向认证。
取值：
true：开启。
false（默认值）：不开启。
        :rtype: bool
        """
        return self._CaEnabled

    @CaEnabled.setter
    def CaEnabled(self, CaEnabled):
        self._CaEnabled = CaEnabled

    @property
    def CertificateIds(self):
        r"""服务器证书 ID 列表。
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。  

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def GzipEnabled(self):
        r"""是否开启Gzip压缩。取值:true(默认值):是。false:否
        :rtype: bool
        """
        return self._GzipEnabled

    @GzipEnabled.setter
    def GzipEnabled(self, GzipEnabled):
        self._GzipEnabled = GzipEnabled

    @property
    def Http2Enabled(self):
        r"""是否开启HTTP/2特性。HTTP 协议默认 false，HTTPS 协议默认 true。只有 HTTPS 协议支持此参数。
        :rtype: bool
        """
        return self._Http2Enabled

    @Http2Enabled.setter
    def Http2Enabled(self, Http2Enabled):
        self._Http2Enabled = Http2Enabled

    @property
    def IdleTimeout(self):
        r"""连接空闲超时时间。单位：秒。
取值范围：1~600。
默认值：15。
如果在超时时间内一直没有访问请求，负载均衡会断开当前连接，在下次请求到来时创建新的连接。
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ListenerName(self):
        r"""自定义监听名称。  长度为 1~255 个字符，必须是中文和无害字符串中的字符，  可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def RequestTimeout(self):
        r"""请求超时时间。单位：秒。
取值：1~600。
默认值：60。
如果在超时时间内后端服务器没有返回响应，负载均衡将放弃等待，并给客户端返回HTTP 504错误码。
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def SecurityPolicyId(self):
        r"""安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def Tags(self):
        r"""标签列表。最大支持20个。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def XForwardedForConfig(self):
        r"""X-Forwarded-For配置
        :rtype: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        return self._XForwardedForConfig

    @XForwardedForConfig.setter
    def XForwardedForConfig(self, XForwardedForConfig):
        self._XForwardedForConfig = XForwardedForConfig


    def _deserialize(self, params):
        if params.get("DefaultActions") is not None:
            self._DefaultActions = []
            for item in params.get("DefaultActions"):
                obj = DefaultAction()
                obj._deserialize(item)
                self._DefaultActions.append(obj)
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._CaCertificateIds = params.get("CaCertificateIds")
        self._CaEnabled = params.get("CaEnabled")
        self._CertificateIds = params.get("CertificateIds")
        self._ClientToken = params.get("ClientToken")
        self._GzipEnabled = params.get("GzipEnabled")
        self._Http2Enabled = params.get("Http2Enabled")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ListenerName = params.get("ListenerName")
        self._RequestTimeout = params.get("RequestTimeout")
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("XForwardedForConfig") is not None:
            self._XForwardedForConfig = XForwardedForConfig()
            self._XForwardedForConfig._deserialize(params.get("XForwardedForConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    r"""CreateListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerId = None
        self._RequestId = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

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
        self._ListenerId = params.get("ListenerId")
        self._RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    r"""CreateLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressType: 应用型负载均衡的地址类型。取值：

- **Internet**：负载均衡具有公网IP地址，DNS域名被解析到公网IP，因此可以在公网环境访问。

- **Intranet**：负载均衡只有私网IP地址，DNS域名被解析到私网IP，因此只能被负载均衡所在VPC的内网环境访问。
        :type AddressType: str
        :param _LoadBalancerBillingConfig: 应用型负载均衡实例计费配置。
        :type LoadBalancerBillingConfig: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        :param _VpcId: 私有网络 ID。
        :type VpcId: str
        :param _ZoneMappings: 可用区及私有网络子网映射列表，最多支持添加10个可用区。若当前地域支持2个及以上的可用区，至少需要添加2个可用区。
        :type ZoneMappings: list of ZoneMappingsItem
        :param _AddressIpVersion: IP 地址版本，取值 IPv4 或 IPv6。
        :type AddressIpVersion: str
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。
        :type ClientToken: str
        :param _DeleteProtection: 删除保护配置。
        :type DeleteProtection: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        :param _DryRun: 是否只预检此次请求，取值：

- **true**：发送检查请求，不会创建应用型负载均衡实例。检查项包括是否填写了必需参数、请求格式和业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。

- **false**（默认值）：发送正常请求，通过检查后返回HTTP 2xx状态码并直接进行操作。
        :type DryRun: bool
        :param _InternetAddressType: EIP 地址类型，可取值：
- **EIP**: 普通弹性公网 IP
- **AntiDDoSEIP**: 高防EIP
- **AnycastEIP**: 加速 EIP
- **HighQualityEIP**: 精品 IP。仅新加坡和中国香港支持精品IP。
- **ResidentialEIP**: 原生 IP

不传默认是EIP。
        :type InternetAddressType: str
        :param _LoadBalancerName: 应用型负载均衡实例名称。长度为1~80个字符，可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）。
        :type LoadBalancerName: str
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        """
        self._AddressType = None
        self._LoadBalancerBillingConfig = None
        self._VpcId = None
        self._ZoneMappings = None
        self._AddressIpVersion = None
        self._ClientToken = None
        self._DeleteProtection = None
        self._DryRun = None
        self._InternetAddressType = None
        self._LoadBalancerName = None
        self._Tags = None

    @property
    def AddressType(self):
        r"""应用型负载均衡的地址类型。取值：

- **Internet**：负载均衡具有公网IP地址，DNS域名被解析到公网IP，因此可以在公网环境访问。

- **Intranet**：负载均衡只有私网IP地址，DNS域名被解析到私网IP，因此只能被负载均衡所在VPC的内网环境访问。
        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def LoadBalancerBillingConfig(self):
        r"""应用型负载均衡实例计费配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        """
        return self._LoadBalancerBillingConfig

    @LoadBalancerBillingConfig.setter
    def LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):
        self._LoadBalancerBillingConfig = LoadBalancerBillingConfig

    @property
    def VpcId(self):
        r"""私有网络 ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ZoneMappings(self):
        r"""可用区及私有网络子网映射列表，最多支持添加10个可用区。若当前地域支持2个及以上的可用区，至少需要添加2个可用区。
        :rtype: list of ZoneMappingsItem
        """
        return self._ZoneMappings

    @ZoneMappings.setter
    def ZoneMappings(self, ZoneMappings):
        self._ZoneMappings = ZoneMappings

    @property
    def AddressIpVersion(self):
        r"""IP 地址版本，取值 IPv4 或 IPv6。
        :rtype: str
        """
        return self._AddressIpVersion

    @AddressIpVersion.setter
    def AddressIpVersion(self, AddressIpVersion):
        self._AddressIpVersion = AddressIpVersion

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeleteProtection(self):
        r"""删除保护配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        """
        return self._DeleteProtection

    @DeleteProtection.setter
    def DeleteProtection(self, DeleteProtection):
        self._DeleteProtection = DeleteProtection

    @property
    def DryRun(self):
        r"""是否只预检此次请求，取值：

- **true**：发送检查请求，不会创建应用型负载均衡实例。检查项包括是否填写了必需参数、请求格式和业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。

- **false**（默认值）：发送正常请求，通过检查后返回HTTP 2xx状态码并直接进行操作。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def InternetAddressType(self):
        r"""EIP 地址类型，可取值：
- **EIP**: 普通弹性公网 IP
- **AntiDDoSEIP**: 高防EIP
- **AnycastEIP**: 加速 EIP
- **HighQualityEIP**: 精品 IP。仅新加坡和中国香港支持精品IP。
- **ResidentialEIP**: 原生 IP

不传默认是EIP。
        :rtype: str
        """
        return self._InternetAddressType

    @InternetAddressType.setter
    def InternetAddressType(self, InternetAddressType):
        self._InternetAddressType = InternetAddressType

    @property
    def LoadBalancerName(self):
        r"""应用型负载均衡实例名称。长度为1~80个字符，可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._AddressType = params.get("AddressType")
        if params.get("LoadBalancerBillingConfig") is not None:
            self._LoadBalancerBillingConfig = LoadBalancerBillingConfig()
            self._LoadBalancerBillingConfig._deserialize(params.get("LoadBalancerBillingConfig"))
        self._VpcId = params.get("VpcId")
        if params.get("ZoneMappings") is not None:
            self._ZoneMappings = []
            for item in params.get("ZoneMappings"):
                obj = ZoneMappingsItem()
                obj._deserialize(item)
                self._ZoneMappings.append(obj)
        self._AddressIpVersion = params.get("AddressIpVersion")
        self._ClientToken = params.get("ClientToken")
        if params.get("DeleteProtection") is not None:
            self._DeleteProtection = DeletionProtectionConfig()
            self._DeleteProtection._deserialize(params.get("DeleteProtection"))
        self._DryRun = params.get("DryRun")
        self._InternetAddressType = params.get("InternetAddressType")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    r"""CreateLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerId = None
        self._RequestId = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

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
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._RequestId = params.get("RequestId")


class CreateRulesRequest(AbstractModel):
    r"""CreateRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _Rules: 转发规则列表。
        :type Rules: list of RuleInput
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。  从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。  若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。
        :type ClientToken: str
        :param _DryRun: 是否只预检查此次请求。
        :type DryRun: bool
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._Rules = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Rules(self):
        r"""转发规则列表。
        :rtype: list of RuleInput
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。  从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。  若您未指定，则系统自动使用API请求的RequestId作为ClientToken标识。每次API请求的RequestId不一样。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""是否只预检查此次请求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleInput()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRulesResponse(AbstractModel):
    r"""CreateRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RuleIds: 转发规则 ID 列表，ID 格式为 rule- 后接 8 位字母数字。
        :type RuleIds: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RuleIds = None
        self._RequestId = None

    @property
    def RuleIds(self):
        r"""转发规则 ID 列表，ID 格式为 rule- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

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
        self._RuleIds = params.get("RuleIds")
        self._RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    r"""CreateSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ciphers: <p>安全策略支持的加密套件列表。加密套件用于协商客户端与服务端之间的加密算法。</p><p><strong>配置说明：</strong></p><ul><li>加密套件的可选范围取决于所选的 TLS 协议版本（TLSVersions 参数）。</li><li>只要加密套件被任意一个已选 TLS 版本支持，即可添加到列表中。</li><li>若 TLSVersions 包含 TLSv1.3：可不指定 TLSv1.3 专属加密套件（系统将自动补全全部 TLSv1.3 套件）；若指定，则必须包含全部 TLSv1.3 专属加密套件，不支持仅指定部分。</li></ul><p><strong>获取可用加密套件：</strong><br>请调用 <a href="https://cloud.tencent.com/document/api/1822/133718">DescribeSecurityPolicyCapabilities</a> 接口查询各 TLS 版本支持的加密套件列表。</p>
        :type Ciphers: list of str
        :param _TLSVersions: <p>安全策略支持的 TLS 协议版本列表。TLS（Transport Layer Security）协议用于保障客户端与负载均衡之间的通信安全。</p><p><strong>可选值：</strong></p><ul><li><strong>TLSv1.0</strong>：兼容性最好，但安全性较低，不推荐在生产环境使用。</li><li><strong>TLSv1.1</strong>：安全性略优于 TLSv1.0，但仍不推荐。</li><li><strong>TLSv1.2</strong>：目前主流的安全协议版本，兼顾安全性与兼容性。</li><li><strong>TLSv1.3</strong>：最新版本，安全性最高，性能更优，推荐优先使用。</li></ul><p><strong>建议：</strong> 生产环境建议至少选择 TLSv1.2，若客户端支持，优先启用 TLSv1.3。</p>
        :type TLSVersions: list of str
        :param _ClientToken: <p>客户端幂等性令牌。</p><p>用于保证请求的幂等性，防止因网络超时或客户端重试导致的重复创建。建议使用 UUID 作为令牌值。相同的 ClientToken 在有效期内重复请求时，服务端将返回相同的结果。</p>
        :type ClientToken: str
        :param _DryRun: <p>是否仅执行预检请求。取值：</p><ul><li><strong>true</strong>：仅执行预检请求，不实际创建资源。预检请求将验证参数格式、权限及资源配额等，帮助您在正式操作前发现潜在问题。</li><li><strong>false</strong>（默认）：执行正常请求，通过预检后将直接创建安全策略。</li></ul>
        :type DryRun: bool
        :param _SecurityPolicyName: <p>安全策略名称。用于标识和区分不同的安全策略。</p><p><strong>命名规则：</strong></p><ul><li>长度为 2~128 个字符。</li><li>必须以英文字母或中文开头。</li><li>可包含英文字母、中文、数字、半角句号（.）、下划线（_）和短划线（-）。</li></ul><p><strong>建议：</strong> 使用具有业务含义的名称，例如 &quot;prod-high-security&quot; 或 &quot;测试环境策略&quot;。</p>
        :type SecurityPolicyName: str
        :param _Tags: <p>安全策略的标签列表。标签用于对资源进行分类和管理，便于按业务、环境、部门等维度筛选和组织资源。</p><p>每个标签由键值对（Key-Value）组成，同一资源下标签键不可重复。</p>
        :type Tags: list of TagInfo
        """
        self._Ciphers = None
        self._TLSVersions = None
        self._ClientToken = None
        self._DryRun = None
        self._SecurityPolicyName = None
        self._Tags = None

    @property
    def Ciphers(self):
        r"""<p>安全策略支持的加密套件列表。加密套件用于协商客户端与服务端之间的加密算法。</p><p><strong>配置说明：</strong></p><ul><li>加密套件的可选范围取决于所选的 TLS 协议版本（TLSVersions 参数）。</li><li>只要加密套件被任意一个已选 TLS 版本支持，即可添加到列表中。</li><li>若 TLSVersions 包含 TLSv1.3：可不指定 TLSv1.3 专属加密套件（系统将自动补全全部 TLSv1.3 套件）；若指定，则必须包含全部 TLSv1.3 专属加密套件，不支持仅指定部分。</li></ul><p><strong>获取可用加密套件：</strong><br>请调用 <a href="https://cloud.tencent.com/document/api/1822/133718">DescribeSecurityPolicyCapabilities</a> 接口查询各 TLS 版本支持的加密套件列表。</p>
        :rtype: list of str
        """
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def TLSVersions(self):
        r"""<p>安全策略支持的 TLS 协议版本列表。TLS（Transport Layer Security）协议用于保障客户端与负载均衡之间的通信安全。</p><p><strong>可选值：</strong></p><ul><li><strong>TLSv1.0</strong>：兼容性最好，但安全性较低，不推荐在生产环境使用。</li><li><strong>TLSv1.1</strong>：安全性略优于 TLSv1.0，但仍不推荐。</li><li><strong>TLSv1.2</strong>：目前主流的安全协议版本，兼顾安全性与兼容性。</li><li><strong>TLSv1.3</strong>：最新版本，安全性最高，性能更优，推荐优先使用。</li></ul><p><strong>建议：</strong> 生产环境建议至少选择 TLSv1.2，若客户端支持，优先启用 TLSv1.3。</p>
        :rtype: list of str
        """
        return self._TLSVersions

    @TLSVersions.setter
    def TLSVersions(self, TLSVersions):
        self._TLSVersions = TLSVersions

    @property
    def ClientToken(self):
        r"""<p>客户端幂等性令牌。</p><p>用于保证请求的幂等性，防止因网络超时或客户端重试导致的重复创建。建议使用 UUID 作为令牌值。相同的 ClientToken 在有效期内重复请求时，服务端将返回相同的结果。</p>
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""<p>是否仅执行预检请求。取值：</p><ul><li><strong>true</strong>：仅执行预检请求，不实际创建资源。预检请求将验证参数格式、权限及资源配额等，帮助您在正式操作前发现潜在问题。</li><li><strong>false</strong>（默认）：执行正常请求，通过预检后将直接创建安全策略。</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def SecurityPolicyName(self):
        r"""<p>安全策略名称。用于标识和区分不同的安全策略。</p><p><strong>命名规则：</strong></p><ul><li>长度为 2~128 个字符。</li><li>必须以英文字母或中文开头。</li><li>可包含英文字母、中文、数字、半角句号（.）、下划线（_）和短划线（-）。</li></ul><p><strong>建议：</strong> 使用具有业务含义的名称，例如 &quot;prod-high-security&quot; 或 &quot;测试环境策略&quot;。</p>
        :rtype: str
        """
        return self._SecurityPolicyName

    @SecurityPolicyName.setter
    def SecurityPolicyName(self, SecurityPolicyName):
        self._SecurityPolicyName = SecurityPolicyName

    @property
    def Tags(self):
        r"""<p>安全策略的标签列表。标签用于对资源进行分类和管理，便于按业务、环境、部门等维度筛选和组织资源。</p><p>每个标签由键值对（Key-Value）组成，同一资源下标签键不可重复。</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Ciphers = params.get("Ciphers")
        self._TLSVersions = params.get("TLSVersions")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        self._SecurityPolicyName = params.get("SecurityPolicyName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    r"""CreateSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyId: <p>安全策略 ID，格式为 tls- 后接 8 位字母数字。</p>
        :type SecurityPolicyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityPolicyId = None
        self._RequestId = None

    @property
    def SecurityPolicyId(self):
        r"""<p>安全策略 ID，格式为 tls- 后接 8 位字母数字。</p>
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

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
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        self._RequestId = params.get("RequestId")


class CreateTargetGroupRequest(AbstractModel):
    r"""CreateTargetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetType: <p>目标组类型。取值：</p><ul><li><strong>Instance</strong>（默认）：Cvm服务器类型或者Eni网卡类型。</li></ul>
        :type TargetType: str
        :param _VpcId: <p>私有网络 ID。</p>
        :type VpcId: str
        :param _DryRun: <p>是否预览此次请求。</p><ul><li><strong>false</strong>（默认）：发送普通请求，直接创建目标组。</li><li><strong>true</strong>：发送预览请求，检查创建目标组的参数、格式、业务限制等是否符合要求。</li></ul>
        :type DryRun: bool
        :param _HealthCheckConfig: <p>健康检查配置。</p>
        :type HealthCheckConfig: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        :param _KeepaliveEnabled: <p>是否开启长连接。</p>
        :type KeepaliveEnabled: bool
        :param _Protocol: <p>后端服务协议类型。取值：</p><ul><li><strong>HTTP</strong>（默认）：支持绑定HTTP、HTTPS的监听器</li><li><strong>HTTPS</strong>：支持绑定HTTPS类型的监听器</li><li><strong>GRPC</strong>：支持绑定HTTPS类型的监听器</li><li><strong>GRPCS</strong>：支持绑定HTTPS类型的监听器</li></ul>
        :type Protocol: str
        :param _SchedulerAlgorithm: <p>调度算法。取值：</p><ul><li><strong>wrr</strong>（默认）：加权轮询，按照权重选择后端服务器，权重越高的服务器被轮询到的概率越高。</li><li><strong>wlc</strong>：加权最小连接数，当不同后端服务器权重值相同时，当前连接数越小的后端服务器被轮询到的概率越高。</li></ul>
        :type SchedulerAlgorithm: str
        :param _StickySessionConfig: <p>会话保持配置。</p>
        :type StickySessionConfig: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        :param _Tags: <p>标签。</p>
        :type Tags: list of TagInfo
        :param _TargetGroupName: <p>目标组名称。默认为目标组ID。长度为 <strong>1-255</strong> 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。</p>
        :type TargetGroupName: str
        """
        self._TargetType = None
        self._VpcId = None
        self._DryRun = None
        self._HealthCheckConfig = None
        self._KeepaliveEnabled = None
        self._Protocol = None
        self._SchedulerAlgorithm = None
        self._StickySessionConfig = None
        self._Tags = None
        self._TargetGroupName = None

    @property
    def TargetType(self):
        r"""<p>目标组类型。取值：</p><ul><li><strong>Instance</strong>（默认）：Cvm服务器类型或者Eni网卡类型。</li></ul>
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def VpcId(self):
        r"""<p>私有网络 ID。</p>
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def DryRun(self):
        r"""<p>是否预览此次请求。</p><ul><li><strong>false</strong>（默认）：发送普通请求，直接创建目标组。</li><li><strong>true</strong>：发送预览请求，检查创建目标组的参数、格式、业务限制等是否符合要求。</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def HealthCheckConfig(self):
        r"""<p>健康检查配置。</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        """
        return self._HealthCheckConfig

    @HealthCheckConfig.setter
    def HealthCheckConfig(self, HealthCheckConfig):
        self._HealthCheckConfig = HealthCheckConfig

    @property
    def KeepaliveEnabled(self):
        r"""<p>是否开启长连接。</p>
        :rtype: bool
        """
        return self._KeepaliveEnabled

    @KeepaliveEnabled.setter
    def KeepaliveEnabled(self, KeepaliveEnabled):
        self._KeepaliveEnabled = KeepaliveEnabled

    @property
    def Protocol(self):
        r"""<p>后端服务协议类型。取值：</p><ul><li><strong>HTTP</strong>（默认）：支持绑定HTTP、HTTPS的监听器</li><li><strong>HTTPS</strong>：支持绑定HTTPS类型的监听器</li><li><strong>GRPC</strong>：支持绑定HTTPS类型的监听器</li><li><strong>GRPCS</strong>：支持绑定HTTPS类型的监听器</li></ul>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SchedulerAlgorithm(self):
        r"""<p>调度算法。取值：</p><ul><li><strong>wrr</strong>（默认）：加权轮询，按照权重选择后端服务器，权重越高的服务器被轮询到的概率越高。</li><li><strong>wlc</strong>：加权最小连接数，当不同后端服务器权重值相同时，当前连接数越小的后端服务器被轮询到的概率越高。</li></ul>
        :rtype: str
        """
        return self._SchedulerAlgorithm

    @SchedulerAlgorithm.setter
    def SchedulerAlgorithm(self, SchedulerAlgorithm):
        self._SchedulerAlgorithm = SchedulerAlgorithm

    @property
    def StickySessionConfig(self):
        r"""<p>会话保持配置。</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        """
        return self._StickySessionConfig

    @StickySessionConfig.setter
    def StickySessionConfig(self, StickySessionConfig):
        self._StickySessionConfig = StickySessionConfig

    @property
    def Tags(self):
        r"""<p>标签。</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TargetGroupName(self):
        r"""<p>目标组名称。默认为目标组ID。长度为 <strong>1-255</strong> 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。</p>
        :rtype: str
        """
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName


    def _deserialize(self, params):
        self._TargetType = params.get("TargetType")
        self._VpcId = params.get("VpcId")
        self._DryRun = params.get("DryRun")
        if params.get("HealthCheckConfig") is not None:
            self._HealthCheckConfig = HealthCheckConfig()
            self._HealthCheckConfig._deserialize(params.get("HealthCheckConfig"))
        self._KeepaliveEnabled = params.get("KeepaliveEnabled")
        self._Protocol = params.get("Protocol")
        self._SchedulerAlgorithm = params.get("SchedulerAlgorithm")
        if params.get("StickySessionConfig") is not None:
            self._StickySessionConfig = StickySessionConfig()
            self._StickySessionConfig._deserialize(params.get("StickySessionConfig"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TargetGroupName = params.get("TargetGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTargetGroupResponse(AbstractModel):
    r"""CreateTargetGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: <p>目标组 ID，格式为 lbtg- 后接 8 位字母数字。</p>
        :type TargetGroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TargetGroupId = None
        self._RequestId = None

    @property
    def TargetGroupId(self):
        r"""<p>目标组 ID，格式为 lbtg- 后接 8 位字母数字。</p>
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

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
        self._TargetGroupId = params.get("TargetGroupId")
        self._RequestId = params.get("RequestId")


class DefaultAction(AbstractModel):
    r"""监听器默认规则动作

    """

    def __init__(self):
        r"""
        :param _TargetGroupConfig: 转发目标组配置。创建监听器时转发动作中的目标组配置仅支持单个目标组。
        :type TargetGroupConfig: :class:`tencentcloud.alb.v20251030.models.TargetGroupConfig`
        :param _Type: 转发动作类型。创建监听器时，默认转发动作类型仅支持转发至目标组。
        :type Type: str
        """
        self._TargetGroupConfig = None
        self._Type = None

    @property
    def TargetGroupConfig(self):
        r"""转发目标组配置。创建监听器时转发动作中的目标组配置仅支持单个目标组。
        :rtype: :class:`tencentcloud.alb.v20251030.models.TargetGroupConfig`
        """
        return self._TargetGroupConfig

    @TargetGroupConfig.setter
    def TargetGroupConfig(self, TargetGroupConfig):
        self._TargetGroupConfig = TargetGroupConfig

    @property
    def Type(self):
        r"""转发动作类型。创建监听器时，默认转发动作类型仅支持转发至目标组。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        if params.get("TargetGroupConfig") is not None:
            self._TargetGroupConfig = TargetGroupConfig()
            self._TargetGroupConfig._deserialize(params.get("TargetGroupConfig"))
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHealthCheckTemplatesRequest(AbstractModel):
    r"""DeleteHealthCheckTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplateIds: 健康检查模板 ID 列表，ID 格式为 hct- 后接字母数字。
        :type HealthCheckTemplateIds: list of str
        :param _DryRun: 是否预览此次请求。
- **false**（默认）：发送普通请求，直接删除模板。
- **true**：发送预览请求，检查删除模板的参数、格式、业务限制等是否符合要求。
        :type DryRun: bool
        """
        self._HealthCheckTemplateIds = None
        self._DryRun = None

    @property
    def HealthCheckTemplateIds(self):
        r"""健康检查模板 ID 列表，ID 格式为 hct- 后接字母数字。
        :rtype: list of str
        """
        return self._HealthCheckTemplateIds

    @HealthCheckTemplateIds.setter
    def HealthCheckTemplateIds(self, HealthCheckTemplateIds):
        self._HealthCheckTemplateIds = HealthCheckTemplateIds

    @property
    def DryRun(self):
        r"""是否预览此次请求。
- **false**（默认）：发送普通请求，直接删除模板。
- **true**：发送预览请求，检查删除模板的参数、格式、业务限制等是否符合要求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._HealthCheckTemplateIds = params.get("HealthCheckTemplateIds")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHealthCheckTemplatesResponse(AbstractModel):
    r"""DeleteHealthCheckTemplates返回参数结构体

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


class DeleteListenerRequest(AbstractModel):
    r"""DeleteListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerIds: 监听器 ID 列表，ID 格式为 lst- 后接 8 位字母数字。
        :type ListenerIds: list of str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。
        :type ClientToken: str
        """
        self._ListenerIds = None
        self._LoadBalancerId = None
        self._ClientToken = None

    @property
    def ListenerIds(self):
        r"""监听器 ID 列表，ID 格式为 lst- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        self._ListenerIds = params.get("ListenerIds")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    r"""DeleteListener返回参数结构体

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


class DeleteLoadBalancersRequest(AbstractModel):
    r"""DeleteLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerIds: 负载均衡实例 ID 列表，ID 格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerIds: list of str
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。


        :type ClientToken: str
        :param _DryRun: 是否只预检此次请求，取值：

- **true**：发送检查请求，不会删除应用型负载均衡实例。检查项包括是否填写了必需参数、请求格式和业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。

- **false**（默认值）：发送正常请求，通过检查后返回`HTTP 2xx`状态码并直接进行操作。
        :type DryRun: bool
        """
        self._LoadBalancerIds = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def LoadBalancerIds(self):
        r"""负载均衡实例 ID 列表，ID 格式为 alb- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._LoadBalancerIds

    @LoadBalancerIds.setter
    def LoadBalancerIds(self, LoadBalancerIds):
        self._LoadBalancerIds = LoadBalancerIds

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。


        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""是否只预检此次请求，取值：

- **true**：发送检查请求，不会删除应用型负载均衡实例。检查项包括是否填写了必需参数、请求格式和业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。

- **false**（默认值）：发送正常请求，通过检查后返回`HTTP 2xx`状态码并直接进行操作。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._LoadBalancerIds = params.get("LoadBalancerIds")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancersResponse(AbstractModel):
    r"""DeleteLoadBalancers返回参数结构体

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


class DeleteRulesRequest(AbstractModel):
    r"""DeleteRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _RuleIds: 转发规则 ID 列表，ID 格式为 rule- 后接 8 位字母数字。
        :type RuleIds: list of str
        :param _DryRun: 是否只预检查此次请求。
        :type DryRun: bool
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._RuleIds = None
        self._DryRun = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def RuleIds(self):
        r"""转发规则 ID 列表，ID 格式为 rule- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds

    @property
    def DryRun(self):
        r"""是否只预检查此次请求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._RuleIds = params.get("RuleIds")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRulesResponse(AbstractModel):
    r"""DeleteRules返回参数结构体

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


class DeleteSecurityPolicyRequest(AbstractModel):
    r"""DeleteSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyIds: 安全策略 ID 列表，ID 格式为 tls- 后接 8 位字母数字。
        :type SecurityPolicyIds: list of str
        :param _DryRun: 是否仅执行预检请求。取值：
- **true**：仅执行预检请求，不实际删除资源。预检请求将验证参数格式、权限及安全策略是否被引用等，帮助您在正式操作前发现潜在问题。
- **false**（默认）：执行正常请求，通过预检后将直接删除安全策略。

        :type DryRun: bool
        """
        self._SecurityPolicyIds = None
        self._DryRun = None

    @property
    def SecurityPolicyIds(self):
        r"""安全策略 ID 列表，ID 格式为 tls- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._SecurityPolicyIds

    @SecurityPolicyIds.setter
    def SecurityPolicyIds(self, SecurityPolicyIds):
        self._SecurityPolicyIds = SecurityPolicyIds

    @property
    def DryRun(self):
        r"""是否仅执行预检请求。取值：
- **true**：仅执行预检请求，不实际删除资源。预检请求将验证参数格式、权限及安全策略是否被引用等，帮助您在正式操作前发现潜在问题。
- **false**（默认）：执行正常请求，通过预检后将直接删除安全策略。

        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._SecurityPolicyIds = params.get("SecurityPolicyIds")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    r"""DeleteSecurityPolicy返回参数结构体

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


class DeleteTargetGroupsRequest(AbstractModel):
    r"""DeleteTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DryRun: 是否预览此次请求。
- **false**（默认）：发送普通请求，直接删除目标组。
- **true**：发送预览请求，检查删除目标组的参数、格式、业务限制等是否符合要求。
        :type DryRun: bool
        :param _TargetGroupIds: 目标组 ID 列表，ID 格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupIds: list of str
        """
        self._DryRun = None
        self._TargetGroupIds = None

    @property
    def DryRun(self):
        r"""是否预览此次请求。
- **false**（默认）：发送普通请求，直接删除目标组。
- **true**：发送预览请求，检查删除目标组的参数、格式、业务限制等是否符合要求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def TargetGroupIds(self):
        r"""目标组 ID 列表，ID 格式为 lbtg- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        self._TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTargetGroupsResponse(AbstractModel):
    r"""DeleteTargetGroups返回参数结构体

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


class DeletionProtectionConfig(AbstractModel):
    r"""删除保护状态信息。

    """

    def __init__(self):
        r"""
        :param _DeletionProtectionEnabled: 是否开启删除保护。开启后，可防止实例被意外删除。
- true：开启删除保护
- false：关闭删除保护
        :type DeletionProtectionEnabled: bool
        :param _Reason: 开启修改保护的原因说明。
长度为 1~255 个字符，必须是中文和无害字符串中的字符， 可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :type Reason: str
        """
        self._DeletionProtectionEnabled = None
        self._Reason = None

    @property
    def DeletionProtectionEnabled(self):
        r"""是否开启删除保护。开启后，可防止实例被意外删除。
- true：开启删除保护
- false：关闭删除保护
        :rtype: bool
        """
        return self._DeletionProtectionEnabled

    @DeletionProtectionEnabled.setter
    def DeletionProtectionEnabled(self, DeletionProtectionEnabled):
        self._DeletionProtectionEnabled = DeletionProtectionEnabled

    @property
    def Reason(self):
        r"""开启修改保护的原因说明。
长度为 1~255 个字符，必须是中文和无害字符串中的字符， 可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._DeletionProtectionEnabled = params.get("DeletionProtectionEnabled")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncJobsRequest(AbstractModel):
    r"""DescribeAsyncJobs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MaxResults: 分批次查询时每次显示的条目数。取值范围：1~100，默认值：20。
        :type MaxResults: int
        :param _NextToken: 是否拥有下一次查询的令牌（Token）。取值：  第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :type NextToken: str
        :param _RequestIds: 异步请求返回的RequestId列表
        :type RequestIds: list of str
        """
        self._MaxResults = None
        self._NextToken = None
        self._RequestIds = None

    @property
    def MaxResults(self):
        r"""分批次查询时每次显示的条目数。取值范围：1~100，默认值：20。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""是否拥有下一次查询的令牌（Token）。取值：  第一次查询和没有下一次查询时，均无需填写。 如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RequestIds(self):
        r"""异步请求返回的RequestId列表
        :rtype: list of str
        """
        return self._RequestIds

    @RequestIds.setter
    def RequestIds(self, RequestIds):
        self._RequestIds = RequestIds


    def _deserialize(self, params):
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._RequestIds = params.get("RequestIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAsyncJobsResponse(AbstractModel):
    r"""DescribeAsyncJobs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Jobs: 任务列表。
        :type Jobs: list of Job
        :param _MaxResults: 分批次查询时每次显示的条目数。
        :type MaxResults: int
        :param _NextToken: 是否拥有下一次查询的令牌（Token）。取值：  如果 NextToken 为空表示没有下一次查询。 如果 NextToken 有返回值，该取值表示下一次查询开始的令牌。
        :type NextToken: str
        :param _TotalCount: 列表条目数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Jobs = None
        self._MaxResults = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Jobs(self):
        r"""任务列表。
        :rtype: list of Job
        """
        return self._Jobs

    @Jobs.setter
    def Jobs(self, Jobs):
        self._Jobs = Jobs

    @property
    def MaxResults(self):
        r"""分批次查询时每次显示的条目数。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""是否拥有下一次查询的令牌（Token）。取值：  如果 NextToken 为空表示没有下一次查询。 如果 NextToken 有返回值，该取值表示下一次查询开始的令牌。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""列表条目数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Jobs") is not None:
            self._Jobs = []
            for item in params.get("Jobs"):
                obj = Job()
                obj._deserialize(item)
                self._Jobs.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHealthCheckTemplatesRequest(AbstractModel):
    r"""DescribeHealthCheckTemplates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <p>过滤器。通过指定的过滤条件来查询健康检查模板，支持：</p><ul><li>Name的值为<strong>HealthCheckTemplateName</strong>。通过名称来筛选健康检查模板。<strong>Values</strong>的值为模板名称列表。</li><li>Name的值为<strong>HealthCheckProtocol</strong>。通过健康检查协议来筛选健康检查模板。<strong>Values</strong>的值为协议列表。</li><li>通过标签方式筛选。</li></ul>
        :type Filters: list of Filter
        :param _HealthCheckTemplateIds: <p>健康检查模板 ID 列表，ID 格式为 hct- 后接字母数字。</p>
        :type HealthCheckTemplateIds: list of str
        :param _MaxResults: <p>返回列表的数量，默认为20，最大值为100。</p>
        :type MaxResults: str
        :param _NextToken: <p>下一次查询的Token值。第一次查询和没有下一次查询时，无需填写。<br>如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。</p>
        :type NextToken: str
        """
        self._Filters = None
        self._HealthCheckTemplateIds = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def Filters(self):
        r"""<p>过滤器。通过指定的过滤条件来查询健康检查模板，支持：</p><ul><li>Name的值为<strong>HealthCheckTemplateName</strong>。通过名称来筛选健康检查模板。<strong>Values</strong>的值为模板名称列表。</li><li>Name的值为<strong>HealthCheckProtocol</strong>。通过健康检查协议来筛选健康检查模板。<strong>Values</strong>的值为协议列表。</li><li>通过标签方式筛选。</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def HealthCheckTemplateIds(self):
        r"""<p>健康检查模板 ID 列表，ID 格式为 hct- 后接字母数字。</p>
        :rtype: list of str
        """
        return self._HealthCheckTemplateIds

    @HealthCheckTemplateIds.setter
    def HealthCheckTemplateIds(self, HealthCheckTemplateIds):
        self._HealthCheckTemplateIds = HealthCheckTemplateIds

    @property
    def MaxResults(self):
        r"""<p>返回列表的数量，默认为20，最大值为100。</p>
        :rtype: str
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""<p>下一次查询的Token值。第一次查询和没有下一次查询时，无需填写。<br>如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。</p>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._HealthCheckTemplateIds = params.get("HealthCheckTemplateIds")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHealthCheckTemplatesResponse(AbstractModel):
    r"""DescribeHealthCheckTemplates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplates: <p>健康检查模板列表。</p>
        :type HealthCheckTemplates: list of HealthCheckTemplate
        :param _NextToken: <p>下一次查询的Token值，如果当前是最后一页，返回为空。</p>
        :type NextToken: str
        :param _TotalCount: <p>经过筛选后查询到的健康检查模板总数。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HealthCheckTemplates = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def HealthCheckTemplates(self):
        r"""<p>健康检查模板列表。</p>
        :rtype: list of HealthCheckTemplate
        """
        return self._HealthCheckTemplates

    @HealthCheckTemplates.setter
    def HealthCheckTemplates(self, HealthCheckTemplates):
        self._HealthCheckTemplates = HealthCheckTemplates

    @property
    def NextToken(self):
        r"""<p>下一次查询的Token值，如果当前是最后一页，返回为空。</p>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""<p>经过筛选后查询到的健康检查模板总数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("HealthCheckTemplates") is not None:
            self._HealthCheckTemplates = []
            for item in params.get("HealthCheckTemplates"):
                obj = HealthCheckTemplate()
                obj._deserialize(item)
                self._HealthCheckTemplates.append(obj)
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeListenerCertificatesRequest(AbstractModel):
    r"""DescribeListenerCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateType: 证书类型。取值：CA或SVR（服务器证书）。
        :type CertificateType: str
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _MaxResults: 本次读取的最大数据记录数量。取值: 1~100。默认值: 20。
        :type MaxResults: int
        :param _NextToken: 下一次查询的令牌（Token）。取值：
第一次查询和没有下一次查询时，均无需填写。
如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :type NextToken: str
        """
        self._CertificateType = None
        self._ListenerId = None
        self._LoadBalancerId = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def CertificateType(self):
        r"""证书类型。取值：CA或SVR（服务器证书）。
        :rtype: str
        """
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def MaxResults(self):
        r"""本次读取的最大数据记录数量。取值: 1~100。默认值: 20。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""下一次查询的令牌（Token）。取值：
第一次查询和没有下一次查询时，均无需填写。
如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._CertificateType = params.get("CertificateType")
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerCertificatesResponse(AbstractModel):
    r"""DescribeListenerCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Certificates: 监听器绑定的证书信息列表。
        :type Certificates: list of CertificateInfo
        :param _MaxResults: 本次读取的最大数据记录数量。	
        :type MaxResults: int
        :param _NextToken: 下一次查询的令牌。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _TotalCount: 监听器绑定的证书总量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Certificates = None
        self._MaxResults = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Certificates(self):
        r"""监听器绑定的证书信息列表。
        :rtype: list of CertificateInfo
        """
        return self._Certificates

    @Certificates.setter
    def Certificates(self, Certificates):
        self._Certificates = Certificates

    @property
    def MaxResults(self):
        r"""本次读取的最大数据记录数量。	
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""下一次查询的令牌。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""监听器绑定的证书总量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Certificates") is not None:
            self._Certificates = []
            for item in params.get("Certificates"):
                obj = CertificateInfo()
                obj._deserialize(item)
                self._Certificates.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeListenerDetailRequest(AbstractModel):
    r"""DescribeListenerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        """
        self._ListenerId = None
        self._LoadBalancerId = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerDetailResponse(AbstractModel):
    r"""DescribeListenerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CaCertificateIds: 监听器绑定的CA证书ID列表。
        :type CaCertificateIds: list of str
        :param _CaEnabled: 是否开启双向认证。
        :type CaEnabled: bool
        :param _CertificateIds: 服务器证书 ID 列表。
        :type CertificateIds: list of str
        :param _CreateTime: 监听器实例的创建时间。格式：ISO 8601（例如 2025-01-01T08:30:00+08:00）
        :type CreateTime: str
        :param _DefaultActions: 规则动作列表。
        :type DefaultActions: list of DefaultAction
        :param _GzipEnabled: 是否启用 Gzip 压缩。
        :type GzipEnabled: bool
        :param _Http2Enabled: 是否开启HTTP/2特性。
        :type Http2Enabled: bool
        :param _IdleTimeout: 指定连接空闲超时时间。单位：秒。
        :type IdleTimeout: int
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _ListenerName: 自定义监听名称。
        :type ListenerName: str
        :param _ListenerPort: 负载均衡实例前端使用的端口。
        :type ListenerPort: int
        :param _ListenerProtocol: 监听协议。
        :type ListenerProtocol: str
        :param _ListenerStatus: 监听器状态。取值:=

- **Active**: 运行中。
- **Provisioning**：创建中。
- **Configuring**：变配中。
- **ProvisionFailed**：创建失败
        :type ListenerStatus: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _ModifyTime: 监听器实例的最后变更时间。格式：ISO 8601（例如 2025-01-01T08:30:00+08:00）
        :type ModifyTime: str
        :param _RequestTimeout: 请求超时时间。单位：秒。
        :type RequestTimeout: int
        :param _SecurityPolicyId: 安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :type SecurityPolicyId: str
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        :param _XForwardedForConfig: XForwardedFor配置。
        :type XForwardedForConfig: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CaCertificateIds = None
        self._CaEnabled = None
        self._CertificateIds = None
        self._CreateTime = None
        self._DefaultActions = None
        self._GzipEnabled = None
        self._Http2Enabled = None
        self._IdleTimeout = None
        self._ListenerId = None
        self._ListenerName = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._ListenerStatus = None
        self._LoadBalancerId = None
        self._ModifyTime = None
        self._RequestTimeout = None
        self._SecurityPolicyId = None
        self._Tags = None
        self._XForwardedForConfig = None
        self._RequestId = None

    @property
    def CaCertificateIds(self):
        r"""监听器绑定的CA证书ID列表。
        :rtype: list of str
        """
        return self._CaCertificateIds

    @CaCertificateIds.setter
    def CaCertificateIds(self, CaCertificateIds):
        self._CaCertificateIds = CaCertificateIds

    @property
    def CaEnabled(self):
        r"""是否开启双向认证。
        :rtype: bool
        """
        return self._CaEnabled

    @CaEnabled.setter
    def CaEnabled(self, CaEnabled):
        self._CaEnabled = CaEnabled

    @property
    def CertificateIds(self):
        r"""服务器证书 ID 列表。
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def CreateTime(self):
        r"""监听器实例的创建时间。格式：ISO 8601（例如 2025-01-01T08:30:00+08:00）
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DefaultActions(self):
        r"""规则动作列表。
        :rtype: list of DefaultAction
        """
        return self._DefaultActions

    @DefaultActions.setter
    def DefaultActions(self, DefaultActions):
        self._DefaultActions = DefaultActions

    @property
    def GzipEnabled(self):
        r"""是否启用 Gzip 压缩。
        :rtype: bool
        """
        return self._GzipEnabled

    @GzipEnabled.setter
    def GzipEnabled(self, GzipEnabled):
        self._GzipEnabled = GzipEnabled

    @property
    def Http2Enabled(self):
        r"""是否开启HTTP/2特性。
        :rtype: bool
        """
        return self._Http2Enabled

    @Http2Enabled.setter
    def Http2Enabled(self, Http2Enabled):
        self._Http2Enabled = Http2Enabled

    @property
    def IdleTimeout(self):
        r"""指定连接空闲超时时间。单位：秒。
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""自定义监听名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def ListenerPort(self):
        r"""负载均衡实例前端使用的端口。
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""监听协议。
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def ListenerStatus(self):
        r"""监听器状态。取值:=

- **Active**: 运行中。
- **Provisioning**：创建中。
- **Configuring**：变配中。
- **ProvisionFailed**：创建失败
        :rtype: str
        """
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModifyTime(self):
        r"""监听器实例的最后变更时间。格式：ISO 8601（例如 2025-01-01T08:30:00+08:00）
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RequestTimeout(self):
        r"""请求超时时间。单位：秒。
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def SecurityPolicyId(self):
        r"""安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def XForwardedForConfig(self):
        r"""XForwardedFor配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        return self._XForwardedForConfig

    @XForwardedForConfig.setter
    def XForwardedForConfig(self, XForwardedForConfig):
        self._XForwardedForConfig = XForwardedForConfig

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
        self._CaCertificateIds = params.get("CaCertificateIds")
        self._CaEnabled = params.get("CaEnabled")
        self._CertificateIds = params.get("CertificateIds")
        self._CreateTime = params.get("CreateTime")
        if params.get("DefaultActions") is not None:
            self._DefaultActions = []
            for item in params.get("DefaultActions"):
                obj = DefaultAction()
                obj._deserialize(item)
                self._DefaultActions.append(obj)
        self._GzipEnabled = params.get("GzipEnabled")
        self._Http2Enabled = params.get("Http2Enabled")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestTimeout = params.get("RequestTimeout")
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("XForwardedForConfig") is not None:
            self._XForwardedForConfig = XForwardedForConfig()
            self._XForwardedForConfig._deserialize(params.get("XForwardedForConfig"))
        self._RequestId = params.get("RequestId")


class DescribeListenerHealthStatusRequest(AbstractModel):
    r"""DescribeListenerHealthStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _IncludeRule: 是否包含转发规则的健康检查结果。为false时只返回默认转发规则的健康状态，为true时返回全部规则的健康状态(包含默认规则)。
取值：
true：是。
false（默认值）：否。
        :type IncludeRule: bool
        :param _MaxResults: 本次读取的最大数据记录数量。
取值: 1~100。
默认值: 20
        :type MaxResults: int
        :param _NextToken: 下一页查询的Token值。第一次查询时，无需填写。
        :type NextToken: str
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._IncludeRule = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def IncludeRule(self):
        r"""是否包含转发规则的健康检查结果。为false时只返回默认转发规则的健康状态，为true时返回全部规则的健康状态(包含默认规则)。
取值：
true：是。
false（默认值）：否。
        :rtype: bool
        """
        return self._IncludeRule

    @IncludeRule.setter
    def IncludeRule(self, IncludeRule):
        self._IncludeRule = IncludeRule

    @property
    def MaxResults(self):
        r"""本次读取的最大数据记录数量。
取值: 1~100。
默认值: 20
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""下一页查询的Token值。第一次查询时，无需填写。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._IncludeRule = params.get("IncludeRule")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerHealthStatusResponse(AbstractModel):
    r"""DescribeListenerHealthStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _ListenerPort: 监听器端口。
        :type ListenerPort: str
        :param _ListenerProtocol: 监听器协议。
        :type ListenerProtocol: str
        :param _NextToken: 下一次查询的令牌（Token）。为空时表示这是最后一页。
        :type NextToken: str
        :param _RuleHealthStatusInfos: 转发规则健康状态。
        :type RuleHealthStatusInfos: list of RuleHealthStatusInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ListenerId = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._NextToken = None
        self._RuleHealthStatusInfos = None
        self._RequestId = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerPort(self):
        r"""监听器端口。
        :rtype: str
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""监听器协议。
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def NextToken(self):
        r"""下一次查询的令牌（Token）。为空时表示这是最后一页。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RuleHealthStatusInfos(self):
        r"""转发规则健康状态。
        :rtype: list of RuleHealthStatusInfo
        """
        return self._RuleHealthStatusInfos

    @RuleHealthStatusInfos.setter
    def RuleHealthStatusInfos(self, RuleHealthStatusInfos):
        self._RuleHealthStatusInfos = RuleHealthStatusInfos

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
        self._ListenerId = params.get("ListenerId")
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._NextToken = params.get("NextToken")
        if params.get("RuleHealthStatusInfos") is not None:
            self._RuleHealthStatusInfos = []
            for item in params.get("RuleHealthStatusInfos"):
                obj = RuleHealthStatusInfo()
                obj._deserialize(item)
                self._RuleHealthStatusInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    r"""DescribeListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _Filters: 过滤条件列表，最大支持20个。支持以下几个字段
- **Protocol**: 协议类型
- **Tags**: 标签
        :type Filters: list of Filter
        :param _ListenerIds: 监听器 ID 列表，ID 格式为 lst- 后接 8 位字母数字。
        :type ListenerIds: list of str
        :param _MaxResults: 本次读取的最大数据记录数量。
取值: 1~100。
默认值: 20
        :type MaxResults: int
        :param _NextToken: 下一次查询的令牌（Token）。为空时查询第一页。
        :type NextToken: str
        """
        self._LoadBalancerId = None
        self._Filters = None
        self._ListenerIds = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Filters(self):
        r"""过滤条件列表，最大支持20个。支持以下几个字段
- **Protocol**: 协议类型
- **Tags**: 标签
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def ListenerIds(self):
        r"""监听器 ID 列表，ID 格式为 lst- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._ListenerIds

    @ListenerIds.setter
    def ListenerIds(self, ListenerIds):
        self._ListenerIds = ListenerIds

    @property
    def MaxResults(self):
        r"""本次读取的最大数据记录数量。
取值: 1~100。
默认值: 20
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""下一次查询的令牌（Token）。为空时查询第一页。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._ListenerIds = params.get("ListenerIds")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    r"""DescribeListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Listeners: 监听器信息。
        :type Listeners: list of ListenerOutput
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _MaxResults: 本次读取的最大数据记录数量。
        :type MaxResults: int
        :param _NextToken: 下一次查询的令牌。
        :type NextToken: str
        :param _TotalCount: 总条目数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Listeners = None
        self._LoadBalancerId = None
        self._MaxResults = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Listeners(self):
        r"""监听器信息。
        :rtype: list of ListenerOutput
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def MaxResults(self):
        r"""本次读取的最大数据记录数量。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""下一次查询的令牌。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""总条目数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerOutput()
                obj._deserialize(item)
                self._Listeners.append(obj)
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancerDetailRequest(AbstractModel):
    r"""DescribeLoadBalancerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        """
        self._LoadBalancerId = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancerDetailResponse(AbstractModel):
    r"""DescribeLoadBalancerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerDetail: 负载均衡详细信息
        :type LoadBalancerDetail: :class:`tencentcloud.alb.v20251030.models.LoadBalancerDetail`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancerDetail = None
        self._RequestId = None

    @property
    def LoadBalancerDetail(self):
        r"""负载均衡详细信息
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerDetail`
        """
        return self._LoadBalancerDetail

    @LoadBalancerDetail.setter
    def LoadBalancerDetail(self, LoadBalancerDetail):
        self._LoadBalancerDetail = LoadBalancerDetail

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
        if params.get("LoadBalancerDetail") is not None:
            self._LoadBalancerDetail = LoadBalancerDetail()
            self._LoadBalancerDetail._deserialize(params.get("LoadBalancerDetail"))
        self._RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    r"""DescribeLoadBalancers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询过滤条件，支持以下几个字段
- **LoadBalancerId**: 负载均衡实例 ID
- **LoadBalancerName**: 负载均衡名称
- **LoadBalancerStatus**: 负载均衡状态
- **VpcId**: 私有网络 ID
- **tag:tag-key**：按标签键值对筛选，tag-key 请替换为实际的标签键。例如 `tag:env` 表示按标签键 `env` 筛选。
- **AddressType**: 网络类型
    - **Intranet**: 内网
    - **Internet**: 公网 
- **AddressIpVersion**:
    - **IPv4**: IPv4 地址
    - **IPv6** IPv6 地址
        :type Filters: list of Filter
        :param _MaxResults: 分批次查询时每次显示的条目数。取值范围：**1**~**100**，默认值：**20**。


        :type MaxResults: int
        :param _NextToken: 是否拥有下一次查询的令牌（Token）。取值：
- 第一次查询和没有下一次查询时，均无需填写。
- 如果有下一次查询，取值为上一次API调用返回的**NextToken**值。
        :type NextToken: str
        """
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def Filters(self):
        r"""查询过滤条件，支持以下几个字段
- **LoadBalancerId**: 负载均衡实例 ID
- **LoadBalancerName**: 负载均衡名称
- **LoadBalancerStatus**: 负载均衡状态
- **VpcId**: 私有网络 ID
- **tag:tag-key**：按标签键值对筛选，tag-key 请替换为实际的标签键。例如 `tag:env` 表示按标签键 `env` 筛选。
- **AddressType**: 网络类型
    - **Intranet**: 内网
    - **Internet**: 公网 
- **AddressIpVersion**:
    - **IPv4**: IPv4 地址
    - **IPv6** IPv6 地址
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""分批次查询时每次显示的条目数。取值范围：**1**~**100**，默认值：**20**。


        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""是否拥有下一次查询的令牌（Token）。取值：
- 第一次查询和没有下一次查询时，均无需填写。
- 如果有下一次查询，取值为上一次API调用返回的**NextToken**值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    r"""DescribeLoadBalancers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancers: 应用型负载均衡实例列表。
        :type LoadBalancers: list of LoadBalancer
        :param _MaxResults: 分批次查询时每次显示的条目数。


        :type MaxResults: int
        :param _NextToken: 是否拥有下一次查询的令牌（Token）。取值：
- 如果**NextToken**为空表示没有下一次查询。
- 如果**NextToken**有返回值，该取值表示下一次查询开始的令牌。
        :type NextToken: str
        :param _TotalCount: 列表条目数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._LoadBalancers = None
        self._MaxResults = None
        self._NextToken = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def LoadBalancers(self):
        r"""应用型负载均衡实例列表。
        :rtype: list of LoadBalancer
        """
        return self._LoadBalancers

    @LoadBalancers.setter
    def LoadBalancers(self, LoadBalancers):
        self._LoadBalancers = LoadBalancers

    @property
    def MaxResults(self):
        r"""分批次查询时每次显示的条目数。


        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""是否拥有下一次查询的令牌（Token）。取值：
- 如果**NextToken**为空表示没有下一次查询。
- 如果**NextToken**有返回值，该取值表示下一次查询开始的令牌。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TotalCount(self):
        r"""列表条目数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("LoadBalancers") is not None:
            self._LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self._LoadBalancers.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeQuotaRequest(AbstractModel):
    r"""DescribeQuota请求参数结构体

    """

    def __init__(self):
        r"""
        :param _QuotaTypes: 配额类型列表。支持同时传入多个配额类型。查询资源级配额时，可配合 ResourceIds 传入对应资源ID；如需返回已使用量和可用量，可在 DisplayFields 中传入 used、available。

枚举说明：
- alb_quota_loadbalancers_num：每个地域可创建的 ALB 实例数。
- alb_quota_targetgroups_num：每个地域可创建的 ALB 目标组数。
- alb_quota_loadbalancer_listeners_num：每个 ALB 实例可创建的监听器数，ResourceIds 填写 ALB 实例 ID。
- alb_quota_loadbalancer_rules_num：每个 ALB 实例可添加的转发规则数，不计入默认规则，ResourceIds 填写 ALB 实例 ID。
- alb_quota_loadbalancer_certificates_num：每个 ALB 实例可添加的扩展证书数，不计入默认证书，ResourceIds 填写 ALB 实例 ID。
- alb_quota_loadbalancer_targetgroup_num：每个 ALB 实例可绑定的目标组数，ResourceIds 填写 ALB 实例 ID。
- alb_quota_loadbalancer_servers_num：每个 ALB 实例可添加的后端服务器数，ResourceIds 填写 ALB 实例 ID。
- alb_quota_server_added_num：单个后端服务器 IP 可被添加到 ALB 后端目标组的次数。
- alb_quota_targetgroup_attached_num：每个目标组可被 ALB 转发规则关联的次数，ResourceIds 填写目标组 ID。
- alb_quota_targetgroup_targets_num：每个目标组支持的后端服务器数，适用于 IP 和端口类型后端，ResourceIds 填写目标组 ID。
- alb_quota_targetgroup_targets_num_scf：每个目标组支持的 SCF 函数后端数，ResourceIds 填写目标组 ID。
- alb_quota_max_request_timeout：创建监听器时可配置的连接请求最大超时时间。
- alb_quota_max_idle_timeout：创建监听器时可配置的连接空闲最大超时时间。
- alb_quota_listener_certificates_num：单个监听器可添加的证书数量，ResourceIds 填写监听器 ID。
- alb_quota_rule_targetgroups_num：单条转发规则可绑定的目标组数量。
- alb_quota_rule_conditions_num：单条转发规则可添加的匹配条件条目数。
- alb_quota_rule_wildcards_num：单条转发规则可添加的包含通配符的匹配条目数。
- alb_quota_rule_actions_num：单条转发规则可添加的动作条目数。
- alb_quota_cipher_template_listeners_num：单个加密套件模板可关联的监听器数量。
- alb_quota_healthcheck_templates_num：每个地域可创建的健康检查模板数。
- alb_quota_securitygroup_templates_num：单个 ALB 实例支持绑定的安全组数量。
- alb_quota_securitygroup_rules_per_sg_num：单个 ALB 实例中单个安全组支持的规则条目数。
- alb_quota_security_policies_num：每个地域可创建的自定义安全策略数。
        :type QuotaTypes: list of str
        :param _DisplayFields: 显示字段列表，用于控制是否额外返回用量信息。支持 used、available：used 表示返回当前已使用量，available 表示返回当前剩余可用量。QuotaType 和 Limit 总是返回；ResourceId 会在请求传入 ResourceIds 时返回。
        :type DisplayFields: list of str
        :param _ResourceIds: 资源ID列表。用于查询具体资源维度的配额和用量；不传时查询账号或地域维度的默认配额配置。资源ID的类型由 QuotaTypes 决定，例如 ALB 实例级配额填写 ALB 实例 ID，监听器级配额填写监听器 ID，目标组级配额填写目标组 ID。
        :type ResourceIds: list of str
        """
        self._QuotaTypes = None
        self._DisplayFields = None
        self._ResourceIds = None

    @property
    def QuotaTypes(self):
        r"""配额类型列表。支持同时传入多个配额类型。查询资源级配额时，可配合 ResourceIds 传入对应资源ID；如需返回已使用量和可用量，可在 DisplayFields 中传入 used、available。

枚举说明：
- alb_quota_loadbalancers_num：每个地域可创建的 ALB 实例数。
- alb_quota_targetgroups_num：每个地域可创建的 ALB 目标组数。
- alb_quota_loadbalancer_listeners_num：每个 ALB 实例可创建的监听器数，ResourceIds 填写 ALB 实例 ID。
- alb_quota_loadbalancer_rules_num：每个 ALB 实例可添加的转发规则数，不计入默认规则，ResourceIds 填写 ALB 实例 ID。
- alb_quota_loadbalancer_certificates_num：每个 ALB 实例可添加的扩展证书数，不计入默认证书，ResourceIds 填写 ALB 实例 ID。
- alb_quota_loadbalancer_targetgroup_num：每个 ALB 实例可绑定的目标组数，ResourceIds 填写 ALB 实例 ID。
- alb_quota_loadbalancer_servers_num：每个 ALB 实例可添加的后端服务器数，ResourceIds 填写 ALB 实例 ID。
- alb_quota_server_added_num：单个后端服务器 IP 可被添加到 ALB 后端目标组的次数。
- alb_quota_targetgroup_attached_num：每个目标组可被 ALB 转发规则关联的次数，ResourceIds 填写目标组 ID。
- alb_quota_targetgroup_targets_num：每个目标组支持的后端服务器数，适用于 IP 和端口类型后端，ResourceIds 填写目标组 ID。
- alb_quota_targetgroup_targets_num_scf：每个目标组支持的 SCF 函数后端数，ResourceIds 填写目标组 ID。
- alb_quota_max_request_timeout：创建监听器时可配置的连接请求最大超时时间。
- alb_quota_max_idle_timeout：创建监听器时可配置的连接空闲最大超时时间。
- alb_quota_listener_certificates_num：单个监听器可添加的证书数量，ResourceIds 填写监听器 ID。
- alb_quota_rule_targetgroups_num：单条转发规则可绑定的目标组数量。
- alb_quota_rule_conditions_num：单条转发规则可添加的匹配条件条目数。
- alb_quota_rule_wildcards_num：单条转发规则可添加的包含通配符的匹配条目数。
- alb_quota_rule_actions_num：单条转发规则可添加的动作条目数。
- alb_quota_cipher_template_listeners_num：单个加密套件模板可关联的监听器数量。
- alb_quota_healthcheck_templates_num：每个地域可创建的健康检查模板数。
- alb_quota_securitygroup_templates_num：单个 ALB 实例支持绑定的安全组数量。
- alb_quota_securitygroup_rules_per_sg_num：单个 ALB 实例中单个安全组支持的规则条目数。
- alb_quota_security_policies_num：每个地域可创建的自定义安全策略数。
        :rtype: list of str
        """
        return self._QuotaTypes

    @QuotaTypes.setter
    def QuotaTypes(self, QuotaTypes):
        self._QuotaTypes = QuotaTypes

    @property
    def DisplayFields(self):
        r"""显示字段列表，用于控制是否额外返回用量信息。支持 used、available：used 表示返回当前已使用量，available 表示返回当前剩余可用量。QuotaType 和 Limit 总是返回；ResourceId 会在请求传入 ResourceIds 时返回。
        :rtype: list of str
        """
        return self._DisplayFields

    @DisplayFields.setter
    def DisplayFields(self, DisplayFields):
        self._DisplayFields = DisplayFields

    @property
    def ResourceIds(self):
        r"""资源ID列表。用于查询具体资源维度的配额和用量；不传时查询账号或地域维度的默认配额配置。资源ID的类型由 QuotaTypes 决定，例如 ALB 实例级配额填写 ALB 实例 ID，监听器级配额填写监听器 ID，目标组级配额填写目标组 ID。
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds


    def _deserialize(self, params):
        self._QuotaTypes = params.get("QuotaTypes")
        self._DisplayFields = params.get("DisplayFields")
        self._ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuotaResponse(AbstractModel):
    r"""DescribeQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Quotas: 配额列表。每个元素表示一个配额类型的查询结果；当请求传入 ResourceIds 时，每个元素表示一个配额类型和一个资源ID组合的查询结果。
        :type Quotas: list of QuotaInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Quotas = None
        self._RequestId = None

    @property
    def Quotas(self):
        r"""配额列表。每个元素表示一个配额类型的查询结果；当请求传入 ResourceIds 时，每个元素表示一个配额类型和一个资源ID组合的查询结果。
        :rtype: list of QuotaInfo
        """
        return self._Quotas

    @Quotas.setter
    def Quotas(self, Quotas):
        self._Quotas = Quotas

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
        if params.get("Quotas") is not None:
            self._Quotas = []
            for item in params.get("Quotas"):
                obj = QuotaInfo()
                obj._deserialize(item)
                self._Quotas.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    r"""DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _Filters: 支持的过滤条件如下：
        :type Filters: list of Filter
        :param _MaxResults: 返回列表的数量，默认为20，最大值为100。
        :type MaxResults: int
        :param _NextToken: 下一次查询的Token值。第一次查询和没有下一次查询时，无需填写。如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :type NextToken: str
        :param _RuleIds: 转发规则 ID 列表，ID 格式为 rule- 后接 8 位字母数字。
        :type RuleIds: list of str
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None
        self._RuleIds = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Filters(self):
        r"""支持的过滤条件如下：
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""返回列表的数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""下一次查询的Token值。第一次查询和没有下一次查询时，无需填写。如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def RuleIds(self):
        r"""转发规则 ID 列表，ID 格式为 rule- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    r"""DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 下一次查询的Token值，如果当前是最后一页，返回为空。
        :type NextToken: str
        :param _Rules: 转发规则列表。
        :type Rules: list of RuleOutput
        :param _TotalCount: 总的转发规则个数（根据监听器ID、规则ID等条件过滤后）。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._Rules = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""下一次查询的Token值，如果当前是最后一页，返回为空。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Rules(self):
        r"""转发规则列表。
        :rtype: list of RuleOutput
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        r"""总的转发规则个数（根据监听器ID、规则ID等条件过滤后）。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._NextToken = params.get("NextToken")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleOutput()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPoliciesRequest(AbstractModel):
    r"""DescribeSecurityPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 过滤条件列表，用于筛选符合指定条件的安全策略。多个过滤条件之间为"与"关系。

**支持的过滤条件：**
- **SecurityPolicyNames**：按安全策略名称筛选，支持模糊匹配。
- **tag:tag-key**：按标签键值对筛选，tag-key 请替换为实际的标签键。例如 `tag:env` 表示按标签键 `env` 筛选。

**说明：** 每个过滤条件最多支持 10 个取值。

        :type Filters: list of Filter
        :param _MaxResults: 单次请求返回的最大结果数。用于分页查询，与 NextToken 配合使用。

**取值范围：** 1~100。

**默认值：** 20。

        :type MaxResults: int
        :param _NextToken: 分页查询的起始令牌。用于获取下一页结果数据。

**使用说明：**
- 首次查询时无需设置此参数。
- 如果上一次查询返回了 NextToken，表示还有更多数据，请将该值传入此参数以获取下一页。
- 若上一次查询未返回 NextToken 或返回为空，表示已是最后一页。

        :type NextToken: str
        :param _SecurityPolicyIds: 安全策略 ID 列表，ID 格式为 tls- 后接 8 位字母数字。
        :type SecurityPolicyIds: list of str
        """
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None
        self._SecurityPolicyIds = None

    @property
    def Filters(self):
        r"""过滤条件列表，用于筛选符合指定条件的安全策略。多个过滤条件之间为"与"关系。

**支持的过滤条件：**
- **SecurityPolicyNames**：按安全策略名称筛选，支持模糊匹配。
- **tag:tag-key**：按标签键值对筛选，tag-key 请替换为实际的标签键。例如 `tag:env` 表示按标签键 `env` 筛选。

**说明：** 每个过滤条件最多支持 10 个取值。

        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""单次请求返回的最大结果数。用于分页查询，与 NextToken 配合使用。

**取值范围：** 1~100。

**默认值：** 20。

        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""分页查询的起始令牌。用于获取下一页结果数据。

**使用说明：**
- 首次查询时无需设置此参数。
- 如果上一次查询返回了 NextToken，表示还有更多数据，请将该值传入此参数以获取下一页。
- 若上一次查询未返回 NextToken 或返回为空，表示已是最后一页。

        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def SecurityPolicyIds(self):
        r"""安全策略 ID 列表，ID 格式为 tls- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._SecurityPolicyIds

    @SecurityPolicyIds.setter
    def SecurityPolicyIds(self, SecurityPolicyIds):
        self._SecurityPolicyIds = SecurityPolicyIds


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._SecurityPolicyIds = params.get("SecurityPolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPoliciesResponse(AbstractModel):
    r"""DescribeSecurityPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 下一页查询的起始令牌。

- 若返回值不为空，表示还有更多数据，可将此值作为下一次请求的 NextToken 参数继续查询。
- 若返回值为空或未返回此字段，表示已是最后一页。

        :type NextToken: str
        :param _SecurityPolicies: 安全策略信息列表。包含每个安全策略的详细配置，如策略 ID、名称、TLS 版本、加密套件等。

        :type SecurityPolicies: list of SecurityPolicyInfo
        :param _TotalCount: 符合过滤条件的安全策略总数。

**说明：** 此值表示满足查询条件的总记录数，而非本次返回的记录数。可用于计算分页信息。

        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._SecurityPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""下一页查询的起始令牌。

- 若返回值不为空，表示还有更多数据，可将此值作为下一次请求的 NextToken 参数继续查询。
- 若返回值为空或未返回此字段，表示已是最后一页。

        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def SecurityPolicies(self):
        r"""安全策略信息列表。包含每个安全策略的详细配置，如策略 ID、名称、TLS 版本、加密套件等。

        :rtype: list of SecurityPolicyInfo
        """
        return self._SecurityPolicies

    @SecurityPolicies.setter
    def SecurityPolicies(self, SecurityPolicies):
        self._SecurityPolicies = SecurityPolicies

    @property
    def TotalCount(self):
        r"""符合过滤条件的安全策略总数。

**说明：** 此值表示满足查询条件的总记录数，而非本次返回的记录数。可用于计算分页信息。

        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._NextToken = params.get("NextToken")
        if params.get("SecurityPolicies") is not None:
            self._SecurityPolicies = []
            for item in params.get("SecurityPolicies"):
                obj = SecurityPolicyInfo()
                obj._deserialize(item)
                self._SecurityPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyCapabilitiesRequest(AbstractModel):
    r"""DescribeSecurityPolicyCapabilities请求参数结构体

    """


class DescribeSecurityPolicyCapabilitiesResponse(AbstractModel):
    r"""DescribeSecurityPolicyCapabilities返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyCapabilities: 安全策略配置能力列表。返回当前地域支持的所有 TLS 版本及其对应的加密套件信息。

**返回内容包含：**
- 支持的 TLS 协议版本（如 TLSv1.0、TLSv1.1、TLSv1.2、TLSv1.3）。
- 每个 TLS 版本支持的加密套件列表。

**使用场景：**
- 在创建安全策略（CreateSecurityPolicy）前，调用此接口获取可选的加密套件。
- 在修改安全策略（ModifySecurityPolicyAttributes）前，确认新配置的有效性。

        :type SecurityPolicyCapabilities: list of SecurityPolicyCapability
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityPolicyCapabilities = None
        self._RequestId = None

    @property
    def SecurityPolicyCapabilities(self):
        r"""安全策略配置能力列表。返回当前地域支持的所有 TLS 版本及其对应的加密套件信息。

**返回内容包含：**
- 支持的 TLS 协议版本（如 TLSv1.0、TLSv1.1、TLSv1.2、TLSv1.3）。
- 每个 TLS 版本支持的加密套件列表。

**使用场景：**
- 在创建安全策略（CreateSecurityPolicy）前，调用此接口获取可选的加密套件。
- 在修改安全策略（ModifySecurityPolicyAttributes）前，确认新配置的有效性。

        :rtype: list of SecurityPolicyCapability
        """
        return self._SecurityPolicyCapabilities

    @SecurityPolicyCapabilities.setter
    def SecurityPolicyCapabilities(self, SecurityPolicyCapabilities):
        self._SecurityPolicyCapabilities = SecurityPolicyCapabilities

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
        if params.get("SecurityPolicyCapabilities") is not None:
            self._SecurityPolicyCapabilities = []
            for item in params.get("SecurityPolicyCapabilities"):
                obj = SecurityPolicyCapability()
                obj._deserialize(item)
                self._SecurityPolicyCapabilities.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSecurityPolicyRelationsRequest(AbstractModel):
    r"""DescribeSecurityPolicyRelations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyIds: 安全策略 ID 列表，ID 格式为 tls- 后接 8 位字母数字。
        :type SecurityPolicyIds: list of str
        """
        self._SecurityPolicyIds = None

    @property
    def SecurityPolicyIds(self):
        r"""安全策略 ID 列表，ID 格式为 tls- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._SecurityPolicyIds

    @SecurityPolicyIds.setter
    def SecurityPolicyIds(self, SecurityPolicyIds):
        self._SecurityPolicyIds = SecurityPolicyIds


    def _deserialize(self, params):
        self._SecurityPolicyIds = params.get("SecurityPolicyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyRelationsResponse(AbstractModel):
    r"""DescribeSecurityPolicyRelations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyRelations: 安全策略关联的监听器列表。返回每个安全策略所关联的 HTTPS 监听器信息。
        :type SecurityPolicyRelations: list of SecurityPolicyRelations
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityPolicyRelations = None
        self._RequestId = None

    @property
    def SecurityPolicyRelations(self):
        r"""安全策略关联的监听器列表。返回每个安全策略所关联的 HTTPS 监听器信息。
        :rtype: list of SecurityPolicyRelations
        """
        return self._SecurityPolicyRelations

    @SecurityPolicyRelations.setter
    def SecurityPolicyRelations(self, SecurityPolicyRelations):
        self._SecurityPolicyRelations = SecurityPolicyRelations

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
        if params.get("SecurityPolicyRelations") is not None:
            self._SecurityPolicyRelations = []
            for item in params.get("SecurityPolicyRelations"):
                obj = SecurityPolicyRelations()
                obj._deserialize(item)
                self._SecurityPolicyRelations.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSystemSecurityPoliciesRequest(AbstractModel):
    r"""DescribeSystemSecurityPolicies请求参数结构体

    """


class DescribeSystemSecurityPoliciesResponse(AbstractModel):
    r"""DescribeSystemSecurityPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityPolicies: 系统安全策略列表。
        :type SecurityPolicies: list of SecurityPolicyInfo
        :param _TotalCount: 安全策略总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SecurityPolicies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SecurityPolicies(self):
        r"""系统安全策略列表。
        :rtype: list of SecurityPolicyInfo
        """
        return self._SecurityPolicies

    @SecurityPolicies.setter
    def SecurityPolicies(self, SecurityPolicies):
        self._SecurityPolicies = SecurityPolicies

    @property
    def TotalCount(self):
        r"""安全策略总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("SecurityPolicies") is not None:
            self._SecurityPolicies = []
            for item in params.get("SecurityPolicies"):
                obj = SecurityPolicyInfo()
                obj._deserialize(item)
                self._SecurityPolicies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupTargetsRequest(AbstractModel):
    r"""DescribeTargetGroupTargets请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupId: str
        :param _Filters: 过滤器。通过指定的过滤条件来查询后端服务，支持：
- Name的值为**TargetId**。通过资源ID来筛选后端服务，当目标组后端类型为**Instance**时生效。**Values**的值为Cvm或Eni的资源ID。
- Name的值为**TargetIp**。通过资源IP来筛选后端服务，当目标组后端类型为**Ip**时生效。**Values**的值为后端服务的IP。
- 通过标签方式筛选。
        :type Filters: list of Filter
        :param _MaxResults: 返回列表的数量，默认为**20**，最大值为**100**。
        :type MaxResults: int
        :param _NextToken: 下一次查询的Token值。第一次查询和没有下一次查询时，无需填写。
如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :type NextToken: str
        """
        self._TargetGroupId = None
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None

    @property
    def TargetGroupId(self):
        r"""目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Filters(self):
        r"""过滤器。通过指定的过滤条件来查询后端服务，支持：
- Name的值为**TargetId**。通过资源ID来筛选后端服务，当目标组后端类型为**Instance**时生效。**Values**的值为Cvm或Eni的资源ID。
- Name的值为**TargetIp**。通过资源IP来筛选后端服务，当目标组后端类型为**Ip**时生效。**Values**的值为后端服务的IP。
- 通过标签方式筛选。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""返回列表的数量，默认为**20**，最大值为**100**。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""下一次查询的Token值。第一次查询和没有下一次查询时，无需填写。
如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupTargetsResponse(AbstractModel):
    r"""DescribeTargetGroupTargets返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 下一次查询的Token值，如果当前是最后一页，返回为空。
        :type NextToken: str
        :param _Targets: 后端服务信息。
        :type Targets: list of TargetOutput
        :param _TotalCount: 目标组内后端服务总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._Targets = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""下一次查询的Token值，如果当前是最后一页，返回为空。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def Targets(self):
        r"""后端服务信息。
        :rtype: list of TargetOutput
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def TotalCount(self):
        r"""目标组内后端服务总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._NextToken = params.get("NextToken")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetOutput()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupsByTargetRequest(AbstractModel):
    r"""DescribeTargetGroupsByTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetId: 后端服务实例 ID，CVM 实例格式为 ins- 后接 8 位字母数字。
        :type TargetId: list of str
        """
        self._TargetId = None

    @property
    def TargetId(self):
        r"""后端服务实例 ID，CVM 实例格式为 ins- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId


    def _deserialize(self, params):
        self._TargetId = params.get("TargetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupsByTargetResponse(AbstractModel):
    r"""DescribeTargetGroupsByTarget返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTargetGroupsRequest(AbstractModel):
    r"""DescribeTargetGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters:  过滤器。通过指定的过滤条件来查询后端服务，支持：
- Name的值为**VpcId**。通过VPC实例来筛选目标组。**Values**的值为VPC唯一ID列表。
- Name的值为**TargetType**。通过后端服务类型来筛选目标组。**Values**的值可以取为**Instance**。
- Name的值为**TargetGroupName**。通过目标组名称来筛选目标组。**Values**的值为目标组名称列表。
- Name的值为**Protocol**。通过目标组后端服务协议来筛选目标组。**Values**的值为目标组后端服务协议列表。
- 通过标签方式筛选。
        :type Filters: list of Filter
        :param _MaxResults: 返回列表的数量，默认为**20**，最大值为**100**。
        :type MaxResults: int
        :param _NextToken: 下一次查询的Token值。第一次查询和没有下一次查询时，无需填写。
如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :type NextToken: str
        :param _TargetGroupIds: 目标组 ID 列表，ID 格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupIds: list of str
        """
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None
        self._TargetGroupIds = None

    @property
    def Filters(self):
        r""" 过滤器。通过指定的过滤条件来查询后端服务，支持：
- Name的值为**VpcId**。通过VPC实例来筛选目标组。**Values**的值为VPC唯一ID列表。
- Name的值为**TargetType**。通过后端服务类型来筛选目标组。**Values**的值可以取为**Instance**。
- Name的值为**TargetGroupName**。通过目标组名称来筛选目标组。**Values**的值为目标组名称列表。
- Name的值为**Protocol**。通过目标组后端服务协议来筛选目标组。**Values**的值为目标组后端服务协议列表。
- 通过标签方式筛选。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""返回列表的数量，默认为**20**，最大值为**100**。
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""下一次查询的Token值。第一次查询和没有下一次查询时，无需填写。
如果有下一次查询，取值为上一次 API 调用返回的 NextToken 值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TargetGroupIds(self):
        r"""目标组 ID 列表，ID 格式为 lbtg- 后接 8 位字母数字。
        :rtype: list of str
        """
        return self._TargetGroupIds

    @TargetGroupIds.setter
    def TargetGroupIds(self, TargetGroupIds):
        self._TargetGroupIds = TargetGroupIds


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._TargetGroupIds = params.get("TargetGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetGroupsResponse(AbstractModel):
    r"""DescribeTargetGroups返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NextToken: 下一次查询的Token值，如果当前是最后一页，返回为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type NextToken: str
        :param _TargetGroups: 目标组信息。
        :type TargetGroups: list of TargetGroupOutput
        :param _TotalCount: 目标组总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NextToken = None
        self._TargetGroups = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def NextToken(self):
        r"""下一次查询的Token值，如果当前是最后一页，返回为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def TargetGroups(self):
        r"""目标组信息。
        :rtype: list of TargetGroupOutput
        """
        return self._TargetGroups

    @TargetGroups.setter
    def TargetGroups(self, TargetGroups):
        self._TargetGroups = TargetGroups

    @property
    def TotalCount(self):
        r"""目标组总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        self._NextToken = params.get("NextToken")
        if params.get("TargetGroups") is not None:
            self._TargetGroups = []
            for item in params.get("TargetGroups"):
                obj = TargetGroupOutput()
                obj._deserialize(item)
                self._TargetGroups.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeZonesRequest(AbstractModel):
    r"""DescribeZones请求参数结构体

    """


class DescribeZonesResponse(AbstractModel):
    r"""DescribeZones返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Zones: 可用区列表
        :type Zones: list of Zone
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Zones = None
        self._RequestId = None

    @property
    def Zones(self):
        r"""可用区列表
        :rtype: list of Zone
        """
        return self._Zones

    @Zones.setter
    def Zones(self, Zones):
        self._Zones = Zones

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
        if params.get("Zones") is not None:
            self._Zones = []
            for item in params.get("Zones"):
                obj = Zone()
                obj._deserialize(item)
                self._Zones.append(obj)
        self._RequestId = params.get("RequestId")


class DisassociateBandwidthPackageFromLoadBalancerRequest(AbstractModel):
    r"""DisassociateBandwidthPackageFromLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BandwidthPackageId: 共享带宽包 ID。
        :type BandwidthPackageId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。

> 若您未指定，则系统自动使用API请求的**RequestId**作为**ClientToken**标识。每次API请求的**RequestId**不一样。
        :type ClientToken: str
        :param _DryRun: 是否只预检此次请求。取值：
- **true**：发送检查请求，不会将共享带宽包从负载均衡实例中移除。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。
- **false**（默认值）：发送正常请求，通过检查后返回HTTP 2xx状态码并直接进行操作。
        :type DryRun: bool
        """
        self._BandwidthPackageId = None
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def BandwidthPackageId(self):
        r"""共享带宽包 ID。
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。

> 若您未指定，则系统自动使用API请求的**RequestId**作为**ClientToken**标识。每次API请求的**RequestId**不一样。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""是否只预检此次请求。取值：
- **true**：发送检查请求，不会将共享带宽包从负载均衡实例中移除。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。
- **false**（默认值）：发送正常请求，通过检查后返回HTTP 2xx状态码并直接进行操作。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateBandwidthPackageFromLoadBalancerResponse(AbstractModel):
    r"""DisassociateBandwidthPackageFromLoadBalancer返回参数结构体

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


class DisassociateListenerAdditionalCertificatesRequest(AbstractModel):
    r"""DisassociateListenerAdditionalCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 待解绑的扩展证书 ID 列表。
        :type CertificateIds: list of str
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _ClientToken: 客户端 Token，用于保证请求的幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken 只支持 ASCII 字符。
若您未指定，则系统自动使用 API 请求的 RequestId 作为 ClientToken 标识。每次 API 请求的 RequestId 不一样。  
        :type ClientToken: str
        :param _DryRun: 是否只预检此次请求，取值：
true：发送检查请求，不会从 HTTPS和QUIC监听器解绑扩展证书。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码DryRunOperation。
false（默认值）：发送正常请求，通过检查后返回HTTP 2xx状态码并直接进行操作。
        :type DryRun: str
        """
        self._CertificateIds = None
        self._ListenerId = None
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DryRun = None

    @property
    def CertificateIds(self):
        r"""待解绑的扩展证书 ID 列表。
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""客户端 Token，用于保证请求的幂等性。从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken 只支持 ASCII 字符。
若您未指定，则系统自动使用 API 请求的 RequestId 作为 ClientToken 标识。每次 API 请求的 RequestId 不一样。  
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DryRun(self):
        r"""是否只预检此次请求，取值：
true：发送检查请求，不会从 HTTPS和QUIC监听器解绑扩展证书。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码DryRunOperation。
false（默认值）：发送正常请求，通过检查后返回HTTP 2xx状态码并直接进行操作。
        :rtype: str
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateListenerAdditionalCertificatesResponse(AbstractModel):
    r"""DisassociateListenerAdditionalCertificates返回参数结构体

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


class Filter(AbstractModel):
    r"""过滤器条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤器的名称
        :type Name: str
        :param _Values: 过滤器的值数组
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤器的名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""过滤器的值数组
        :rtype: list of str
        """
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
        


class FixedResponseInfo(AbstractModel):
    r"""固定应答信息

    """

    def __init__(self):
        r"""
        :param _HttpCode: 返回的HTTP响应码，支持 2xx、4xx、5xx。
        :type HttpCode: int
        :param _Content: 返回的固定内容。只支持 ASCII 字符，最大1KB。
        :type Content: str
        :param _ContentType: 返回固定内容的格式。
取值：text/plain、text/css、text/html、application/javascript或application/json。
        :type ContentType: str
        """
        self._HttpCode = None
        self._Content = None
        self._ContentType = None

    @property
    def HttpCode(self):
        r"""返回的HTTP响应码，支持 2xx、4xx、5xx。
        :rtype: int
        """
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def Content(self):
        r"""返回的固定内容。只支持 ASCII 字符，最大1KB。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ContentType(self):
        r"""返回固定内容的格式。
取值：text/plain、text/css、text/html、application/javascript或application/json。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType


    def _deserialize(self, params):
        self._HttpCode = params.get("HttpCode")
        self._Content = params.get("Content")
        self._ContentType = params.get("ContentType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPCookieInfo(AbstractModel):
    r"""HTTP Cookie信息

    """

    def __init__(self):
        r"""
        :param _Key: Cookie的键，长度1~64个字符，支持字母、数字、下划线。
        :type Key: str
        :param _Value: Cookie的值，长度1~128个字符，支持可打印字符。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""Cookie的键，长度1~64个字符，支持字母、数字、下划线。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""Cookie的值，长度1~128个字符，支持可打印字符。
        :rtype: str
        """
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
        


class HTTPHeaderInfo(AbstractModel):
    r"""HTTP Header信息

    """

    def __init__(self):
        r"""
        :param _Key: HTTP Header的键，长度1 ~ 40个字符，支持的字符集为：a-z A-Z 0-9 - _ 。
不支持中文，不支持Host，Cookie。
        :type Key: str
        :param _Values: HTTP Header的值，长度1 ~ 128个字符，支持可打印字符。
不支持"，开头和结尾不能是空格，结尾不能是\。
        :type Values: list of str
        """
        self._Key = None
        self._Values = None

    @property
    def Key(self):
        r"""HTTP Header的键，长度1 ~ 40个字符，支持的字符集为：a-z A-Z 0-9 - _ 。
不支持中文，不支持Host，Cookie。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        r"""HTTP Header的值，长度1 ~ 128个字符，支持可打印字符。
不支持"，开头和结尾不能是空格，结尾不能是\。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPQueryStringInfo(AbstractModel):
    r"""HTTP查询字符串信息

    """

    def __init__(self):
        r"""
        :param _Key: 查询字符串的键，长度1 ~ 16个字符。支持可打印字符，不支持空格和#[]{}\|<>&。
支持 * 多字符通配，? 单字符通配。


        :type Key: str
        :param _Value: 查询字符串的值，长度1 ~ 128字符，支持可打印字符，不支持空格和#[]{}\|<>&。
支持 * 多字符通配，? 单字符通配。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""查询字符串的键，长度1 ~ 16个字符。支持可打印字符，不支持空格和#[]{}\|<>&。
支持 * 多字符通配，? 单字符通配。


        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""查询字符串的值，长度1 ~ 128字符，支持可打印字符，不支持空格和#[]{}\|<>&。
支持 * 多字符通配，? 单字符通配。
        :rtype: str
        """
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
        


class HTTPRedirectInfo(AbstractModel):
    r"""HTTP重定向信息

    """

    def __init__(self):
        r"""
        :param _HttpCode: <p>重定向的HTTP码，支持301、302、303、307、 308。</p>
        :type HttpCode: int
        :param _Host: <p>重定向的主机地址，默认值${host}。长度3 ~ 128个字符，支持的字符集为：a-z 0-9 _ . -。</p>
        :type Host: str
        :param _Path: <p>重定向的路径，默认值${path}。长度1 ~ 128个字符，支持的字符集为：a-z A-Z 0-9  ? =  _  . - / : 。</p>
        :type Path: str
        :param _Port: <p>重定向的端口，默认值 ${port}。取值1 ~ 65535。</p>
        :type Port: str
        :param _Protocol: <p>重定向的协议，取值：HTTP,HTTPS，默认值${protocol}。</p>
        :type Protocol: str
        :param _Query: <p>重定向的查询字符串，默认值${query}。长度1 ~ 128字符，支持可打印字符，不支持 #[]{}|&lt;&gt;&amp; 和空格。</p>
        :type Query: str
        """
        self._HttpCode = None
        self._Host = None
        self._Path = None
        self._Port = None
        self._Protocol = None
        self._Query = None

    @property
    def HttpCode(self):
        r"""<p>重定向的HTTP码，支持301、302、303、307、 308。</p>
        :rtype: int
        """
        return self._HttpCode

    @HttpCode.setter
    def HttpCode(self, HttpCode):
        self._HttpCode = HttpCode

    @property
    def Host(self):
        r"""<p>重定向的主机地址，默认值${host}。长度3 ~ 128个字符，支持的字符集为：a-z 0-9 _ . -。</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Path(self):
        r"""<p>重定向的路径，默认值${path}。长度1 ~ 128个字符，支持的字符集为：a-z A-Z 0-9  ? =  _  . - / : 。</p>
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Port(self):
        r"""<p>重定向的端口，默认值 ${port}。取值1 ~ 65535。</p>
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        r"""<p>重定向的协议，取值：HTTP,HTTPS，默认值${protocol}。</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Query(self):
        r"""<p>重定向的查询字符串，默认值${query}。长度1 ~ 128字符，支持可打印字符，不支持 #[]{}|&lt;&gt;&amp; 和空格。</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._HttpCode = params.get("HttpCode")
        self._Host = params.get("Host")
        self._Path = params.get("Path")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPRewriteInfo(AbstractModel):
    r"""HTTP重写信息

    """

    def __init__(self):
        r"""
        :param _Host: <p>重写的主机地址，默认值${host}。长度3 ~ 128个字符，支持的字符集为：a-z 0-9 _ . -。</p>
        :type Host: str
        :param _Path: <p>重写的路径，默认值${path}。长度1 ~ 128个字符，支持的字符集为：a-z A-Z 0-9 ? = _ . - / : 。</p>
        :type Path: str
        :param _Query: <p>重写的查询字符串，默认值${query}。长度1 ~ 128字符，支持可打印字符，不支持 #[]{}|&lt;&gt;&amp; 和空格。</p>
        :type Query: str
        """
        self._Host = None
        self._Path = None
        self._Query = None

    @property
    def Host(self):
        r"""<p>重写的主机地址，默认值${host}。长度3 ~ 128个字符，支持的字符集为：a-z 0-9 _ . -。</p>
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Path(self):
        r"""<p>重写的路径，默认值${path}。长度1 ~ 128个字符，支持的字符集为：a-z A-Z 0-9 ? = _ . - / : 。</p>
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Query(self):
        r"""<p>重写的查询字符串，默认值${query}。长度1 ~ 128字符，支持可打印字符，不支持 #[]{}|&lt;&gt;&amp; 和空格。</p>
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._Path = params.get("Path")
        self._Query = params.get("Query")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckConfig(AbstractModel):
    r"""健康检查配置

    """

    def __init__(self):
        r"""
        :param _HealthCheckEnabled: 是否开启健康检查。
- **true**：开启。
- **false**：不开启。
        :type HealthCheckEnabled: bool
        :param _HealthCheckCodes: 健康检查状态码。取值：
- 当健康检查协议为**HTTP/HTTPS**时：
	- **http_1xx**
	- **http_2xx**（默认值）
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- 当健康检查协议为**gRPC**时：默认值为12，数值范围为0-99，输入值可为数值、多个数值或者范围以及相互组合，如：
	- **"20"**
	- **"0-99"**
> 仅当**HealthCheckProtocol**设置为**HTTP** 、**HTTPS**、**GRPC** 或者**GRPCS**时，该参数生效。
        :type HealthCheckCodes: list of str
        :param _HealthCheckHealthyThreshold: 判定后端服务健康的阈值，当健康检查连续成功多少次后，后端服务的状态由**不健康**变为**健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :type HealthCheckHealthyThreshold: int
        :param _HealthCheckHost: 健康检查域名。该参数不设置时默认使用后端服务的内网IP作为健康检查地址。
域名限制：
- 长度限制为 **1-255** 个字符。
- 可包含小写字母、数字、短划线（-）和半角句号（.）。
- 至少包含一个半角句号（.），半角句号（.）不能出现在开头或结尾。
- 最右侧的域标签，只能包含字母，不能包含数字或短划线（-）。
- 短划线（-）不能出现在开头或结尾。
>仅当 **HealthCheckProtocol** 设置为 **HTTP、HTTPS** 、**GRPC**、**GRPCS** 时，该参数生效。
        :type HealthCheckHost: str
        :param _HealthCheckHttpVersion: 健康检查 HTTP 协议版本，取值：
- **HTTP1.1**（默认）
- **HTTP1.0** 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :type HealthCheckHttpVersion: str
        :param _HealthCheckInterval: 健康检查的时间间隔。单位：秒。
取值范围：**2**-**300**。
默认值：**5**。
        :type HealthCheckInterval: int
        :param _HealthCheckMethod: 健康检查方法，取值：
- **GET**
- **HEAD**（默认值）
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :type HealthCheckMethod: str
        :param _HealthCheckPath: 健康检查的转发规则路径。
长度为 1~80 个字符，只能使用字母、数字、字符`-/.%?#&=`以及扩展字符`_;~!（)*[]@$^:',+`。 URL 必须以正斜线（/）开头。
> 仅当**HealthCheckProtocol**为**HTTP**、**HTTPS** 、**GRPC**、**GRPCS**时，转发规则路径参数生效。
        :type HealthCheckPath: str
        :param _HealthCheckPort: 健康检查访问后端服务器的端口。

取值范围：**0-65535**。

默认值：**0**，表示后端服务器的端口。
        :type HealthCheckPort: int
        :param _HealthCheckProtocol: 健康检查协议。取值：
- **HTTP**（默认）：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。
- **HTTPS**：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。（数据加密，相比 HTTP 更安全。）
- **TCP**：通过发送 SYN 握手报文来检测服务器端口是否存活。
- **GRPC**：通过发送 POST 请求来检查服务器应用是否健康。
- **GRPCS**：通过发送 POST 请求来检查服务器应用是否健康。
        :type HealthCheckProtocol: str
        :param _HealthCheckTimeout: 健康检查的响应超时时间。单位：秒。
取值范围：**2**-**60**。
默认值：**2**。
        :type HealthCheckTimeout: int
        :param _HealthCheckUnhealthyThreshold: 判定后端服务不健康的阈值，当健康检查连续失败多少次后，后端服务的状态由**健康**变为**不健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :type HealthCheckUnhealthyThreshold: int
        """
        self._HealthCheckEnabled = None
        self._HealthCheckCodes = None
        self._HealthCheckHealthyThreshold = None
        self._HealthCheckHost = None
        self._HealthCheckHttpVersion = None
        self._HealthCheckInterval = None
        self._HealthCheckMethod = None
        self._HealthCheckPath = None
        self._HealthCheckPort = None
        self._HealthCheckProtocol = None
        self._HealthCheckTimeout = None
        self._HealthCheckUnhealthyThreshold = None

    @property
    def HealthCheckEnabled(self):
        r"""是否开启健康检查。
- **true**：开启。
- **false**：不开启。
        :rtype: bool
        """
        return self._HealthCheckEnabled

    @HealthCheckEnabled.setter
    def HealthCheckEnabled(self, HealthCheckEnabled):
        self._HealthCheckEnabled = HealthCheckEnabled

    @property
    def HealthCheckCodes(self):
        r"""健康检查状态码。取值：
- 当健康检查协议为**HTTP/HTTPS**时：
	- **http_1xx**
	- **http_2xx**（默认值）
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- 当健康检查协议为**gRPC**时：默认值为12，数值范围为0-99，输入值可为数值、多个数值或者范围以及相互组合，如：
	- **"20"**
	- **"0-99"**
> 仅当**HealthCheckProtocol**设置为**HTTP** 、**HTTPS**、**GRPC** 或者**GRPCS**时，该参数生效。
        :rtype: list of str
        """
        return self._HealthCheckCodes

    @HealthCheckCodes.setter
    def HealthCheckCodes(self, HealthCheckCodes):
        self._HealthCheckCodes = HealthCheckCodes

    @property
    def HealthCheckHealthyThreshold(self):
        r"""判定后端服务健康的阈值，当健康检查连续成功多少次后，后端服务的状态由**不健康**变为**健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckHealthyThreshold

    @HealthCheckHealthyThreshold.setter
    def HealthCheckHealthyThreshold(self, HealthCheckHealthyThreshold):
        self._HealthCheckHealthyThreshold = HealthCheckHealthyThreshold

    @property
    def HealthCheckHost(self):
        r"""健康检查域名。该参数不设置时默认使用后端服务的内网IP作为健康检查地址。
域名限制：
- 长度限制为 **1-255** 个字符。
- 可包含小写字母、数字、短划线（-）和半角句号（.）。
- 至少包含一个半角句号（.），半角句号（.）不能出现在开头或结尾。
- 最右侧的域标签，只能包含字母，不能包含数字或短划线（-）。
- 短划线（-）不能出现在开头或结尾。
>仅当 **HealthCheckProtocol** 设置为 **HTTP、HTTPS** 、**GRPC**、**GRPCS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckHost

    @HealthCheckHost.setter
    def HealthCheckHost(self, HealthCheckHost):
        self._HealthCheckHost = HealthCheckHost

    @property
    def HealthCheckHttpVersion(self):
        r"""健康检查 HTTP 协议版本，取值：
- **HTTP1.1**（默认）
- **HTTP1.0** 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckHttpVersion

    @HealthCheckHttpVersion.setter
    def HealthCheckHttpVersion(self, HealthCheckHttpVersion):
        self._HealthCheckHttpVersion = HealthCheckHttpVersion

    @property
    def HealthCheckInterval(self):
        r"""健康检查的时间间隔。单位：秒。
取值范围：**2**-**300**。
默认值：**5**。
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def HealthCheckMethod(self):
        r"""健康检查方法，取值：
- **GET**
- **HEAD**（默认值）
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod

    @property
    def HealthCheckPath(self):
        r"""健康检查的转发规则路径。
长度为 1~80 个字符，只能使用字母、数字、字符`-/.%?#&=`以及扩展字符`_;~!（)*[]@$^:',+`。 URL 必须以正斜线（/）开头。
> 仅当**HealthCheckProtocol**为**HTTP**、**HTTPS** 、**GRPC**、**GRPCS**时，转发规则路径参数生效。
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckPort(self):
        r"""健康检查访问后端服务器的端口。

取值范围：**0-65535**。

默认值：**0**，表示后端服务器的端口。
        :rtype: int
        """
        return self._HealthCheckPort

    @HealthCheckPort.setter
    def HealthCheckPort(self, HealthCheckPort):
        self._HealthCheckPort = HealthCheckPort

    @property
    def HealthCheckProtocol(self):
        r"""健康检查协议。取值：
- **HTTP**（默认）：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。
- **HTTPS**：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。（数据加密，相比 HTTP 更安全。）
- **TCP**：通过发送 SYN 握手报文来检测服务器端口是否存活。
- **GRPC**：通过发送 POST 请求来检查服务器应用是否健康。
- **GRPCS**：通过发送 POST 请求来检查服务器应用是否健康。
        :rtype: str
        """
        return self._HealthCheckProtocol

    @HealthCheckProtocol.setter
    def HealthCheckProtocol(self, HealthCheckProtocol):
        self._HealthCheckProtocol = HealthCheckProtocol

    @property
    def HealthCheckTimeout(self):
        r"""健康检查的响应超时时间。单位：秒。
取值范围：**2**-**60**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckUnhealthyThreshold(self):
        r"""判定后端服务不健康的阈值，当健康检查连续失败多少次后，后端服务的状态由**健康**变为**不健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckUnhealthyThreshold

    @HealthCheckUnhealthyThreshold.setter
    def HealthCheckUnhealthyThreshold(self, HealthCheckUnhealthyThreshold):
        self._HealthCheckUnhealthyThreshold = HealthCheckUnhealthyThreshold


    def _deserialize(self, params):
        self._HealthCheckEnabled = params.get("HealthCheckEnabled")
        self._HealthCheckCodes = params.get("HealthCheckCodes")
        self._HealthCheckHealthyThreshold = params.get("HealthCheckHealthyThreshold")
        self._HealthCheckHost = params.get("HealthCheckHost")
        self._HealthCheckHttpVersion = params.get("HealthCheckHttpVersion")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckPort = params.get("HealthCheckPort")
        self._HealthCheckProtocol = params.get("HealthCheckProtocol")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckUnhealthyThreshold = params.get("HealthCheckUnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheckTemplate(AbstractModel):
    r"""健康检查模板信息

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _HealthCheckCodes: 健康检查状态码。取值：
- 当健康检查协议为**HTTP/HTTPS**时：
	- **http_1xx**
	- **http_2xx**（默认值）
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- 当健康检查协议为**GRPC/GRPCS**时：默认值为**12**，数值范围为**0-99**，输入值可为数值、多个数值或者范围以及相互组合，如：
	- **"20"**
	- **"0-99"**
        :type HealthCheckCodes: list of str
        :param _HealthCheckHealthyThreshold: 判定后端服务健康的阈值，当健康检查连续成功多少次后，后端服务的状态由**不健康**变为**健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :type HealthCheckHealthyThreshold: int
        :param _HealthCheckHost: 健康检查域名。
长度限制为 **1-255** 个字符。
可包含小写字母、数字、短划线（-）和半角句号（.）。

> 仅当 **HealthCheckProtocol** 设置为 **HTTP/HTTPS/GRPC/GRPCS** 时，该参数生效。
        :type HealthCheckHost: str
        :param _HealthCheckHttpVersion: 健康检查 HTTP 协议版本，取值：
- **HTTP1.1**（默认）
- **HTTP1.0** 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :type HealthCheckHttpVersion: str
        :param _HealthCheckInterval: 健康检查的时间间隔。单位：秒。
取值范围：**2**-**300**。
默认值：**5**。
        :type HealthCheckInterval: int
        :param _HealthCheckMethod: 健康检查方法，取值：
- **GET**
- **HEAD**（默认值）
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :type HealthCheckMethod: str
        :param _HealthCheckPath: 健康检查的转发规则路径。 长度为 **1-80** 个字符，只能使用字母、数字、字符`-/.%?#&=`以及扩展字符`_;~!（)*[]@$^:',+`。 URL 必须以正斜线（/）开头。 
> 仅当**HealthCheckProtocol**为**HTTP/HTTPS/GRPC/GRPCS**时，转发规则路径参数生效。
        :type HealthCheckPath: str
        :param _HealthCheckPort: 健康检查访问后端服务器的端口。

取值范围：**0-65535**。

默认值：**0**，表示后端服务器的端口。
        :type HealthCheckPort: int
        :param _HealthCheckProtocol: 健康检查协议。取值：
- **HTTP**（默认）：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。
- **HTTPS**：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。（数据加密，相比 HTTP 更安全。）
- **TCP**：通过发送 SYN 握手报文来检测服务器端口是否存活。
- **GRPC**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
- **GRPCS**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
        :type HealthCheckProtocol: str
        :param _HealthCheckTemplateId: 健康检查模板 ID，格式为 hct- 后接字母数字。所有接口（创建、查询、修改、删除）均使用 hct- 前缀。
        :type HealthCheckTemplateId: str
        :param _HealthCheckTemplateName: 健康检查模板名称。长度为 **1-255** 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :type HealthCheckTemplateName: str
        :param _HealthCheckTimeout: 健康检查的响应超时时间。单位：秒。
取值范围：**2**-**60**。
默认值：**2**。
        :type HealthCheckTimeout: int
        :param _HealthCheckUnhealthyThreshold: 判定后端服务不健康的阈值，当健康检查连续失败多少次后，后端服务的状态由**健康**变为**不健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :type HealthCheckUnhealthyThreshold: int
        :param _ModifyTime: 修改时间。
        :type ModifyTime: str
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        """
        self._CreateTime = None
        self._HealthCheckCodes = None
        self._HealthCheckHealthyThreshold = None
        self._HealthCheckHost = None
        self._HealthCheckHttpVersion = None
        self._HealthCheckInterval = None
        self._HealthCheckMethod = None
        self._HealthCheckPath = None
        self._HealthCheckPort = None
        self._HealthCheckProtocol = None
        self._HealthCheckTemplateId = None
        self._HealthCheckTemplateName = None
        self._HealthCheckTimeout = None
        self._HealthCheckUnhealthyThreshold = None
        self._ModifyTime = None
        self._Tags = None

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def HealthCheckCodes(self):
        r"""健康检查状态码。取值：
- 当健康检查协议为**HTTP/HTTPS**时：
	- **http_1xx**
	- **http_2xx**（默认值）
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- 当健康检查协议为**GRPC/GRPCS**时：默认值为**12**，数值范围为**0-99**，输入值可为数值、多个数值或者范围以及相互组合，如：
	- **"20"**
	- **"0-99"**
        :rtype: list of str
        """
        return self._HealthCheckCodes

    @HealthCheckCodes.setter
    def HealthCheckCodes(self, HealthCheckCodes):
        self._HealthCheckCodes = HealthCheckCodes

    @property
    def HealthCheckHealthyThreshold(self):
        r"""判定后端服务健康的阈值，当健康检查连续成功多少次后，后端服务的状态由**不健康**变为**健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckHealthyThreshold

    @HealthCheckHealthyThreshold.setter
    def HealthCheckHealthyThreshold(self, HealthCheckHealthyThreshold):
        self._HealthCheckHealthyThreshold = HealthCheckHealthyThreshold

    @property
    def HealthCheckHost(self):
        r"""健康检查域名。
长度限制为 **1-255** 个字符。
可包含小写字母、数字、短划线（-）和半角句号（.）。

> 仅当 **HealthCheckProtocol** 设置为 **HTTP/HTTPS/GRPC/GRPCS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckHost

    @HealthCheckHost.setter
    def HealthCheckHost(self, HealthCheckHost):
        self._HealthCheckHost = HealthCheckHost

    @property
    def HealthCheckHttpVersion(self):
        r"""健康检查 HTTP 协议版本，取值：
- **HTTP1.1**（默认）
- **HTTP1.0** 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckHttpVersion

    @HealthCheckHttpVersion.setter
    def HealthCheckHttpVersion(self, HealthCheckHttpVersion):
        self._HealthCheckHttpVersion = HealthCheckHttpVersion

    @property
    def HealthCheckInterval(self):
        r"""健康检查的时间间隔。单位：秒。
取值范围：**2**-**300**。
默认值：**5**。
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def HealthCheckMethod(self):
        r"""健康检查方法，取值：
- **GET**
- **HEAD**（默认值）
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod

    @property
    def HealthCheckPath(self):
        r"""健康检查的转发规则路径。 长度为 **1-80** 个字符，只能使用字母、数字、字符`-/.%?#&=`以及扩展字符`_;~!（)*[]@$^:',+`。 URL 必须以正斜线（/）开头。 
> 仅当**HealthCheckProtocol**为**HTTP/HTTPS/GRPC/GRPCS**时，转发规则路径参数生效。
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckPort(self):
        r"""健康检查访问后端服务器的端口。

取值范围：**0-65535**。

默认值：**0**，表示后端服务器的端口。
        :rtype: int
        """
        return self._HealthCheckPort

    @HealthCheckPort.setter
    def HealthCheckPort(self, HealthCheckPort):
        self._HealthCheckPort = HealthCheckPort

    @property
    def HealthCheckProtocol(self):
        r"""健康检查协议。取值：
- **HTTP**（默认）：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。
- **HTTPS**：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。（数据加密，相比 HTTP 更安全。）
- **TCP**：通过发送 SYN 握手报文来检测服务器端口是否存活。
- **GRPC**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
- **GRPCS**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
        :rtype: str
        """
        return self._HealthCheckProtocol

    @HealthCheckProtocol.setter
    def HealthCheckProtocol(self, HealthCheckProtocol):
        self._HealthCheckProtocol = HealthCheckProtocol

    @property
    def HealthCheckTemplateId(self):
        r"""健康检查模板 ID，格式为 hct- 后接字母数字。所有接口（创建、查询、修改、删除）均使用 hct- 前缀。
        :rtype: str
        """
        return self._HealthCheckTemplateId

    @HealthCheckTemplateId.setter
    def HealthCheckTemplateId(self, HealthCheckTemplateId):
        self._HealthCheckTemplateId = HealthCheckTemplateId

    @property
    def HealthCheckTemplateName(self):
        r"""健康检查模板名称。长度为 **1-255** 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :rtype: str
        """
        return self._HealthCheckTemplateName

    @HealthCheckTemplateName.setter
    def HealthCheckTemplateName(self, HealthCheckTemplateName):
        self._HealthCheckTemplateName = HealthCheckTemplateName

    @property
    def HealthCheckTimeout(self):
        r"""健康检查的响应超时时间。单位：秒。
取值范围：**2**-**60**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckUnhealthyThreshold(self):
        r"""判定后端服务不健康的阈值，当健康检查连续失败多少次后，后端服务的状态由**健康**变为**不健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckUnhealthyThreshold

    @HealthCheckUnhealthyThreshold.setter
    def HealthCheckUnhealthyThreshold(self, HealthCheckUnhealthyThreshold):
        self._HealthCheckUnhealthyThreshold = HealthCheckUnhealthyThreshold

    @property
    def ModifyTime(self):
        r"""修改时间。
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        self._HealthCheckCodes = params.get("HealthCheckCodes")
        self._HealthCheckHealthyThreshold = params.get("HealthCheckHealthyThreshold")
        self._HealthCheckHost = params.get("HealthCheckHost")
        self._HealthCheckHttpVersion = params.get("HealthCheckHttpVersion")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckPort = params.get("HealthCheckPort")
        self._HealthCheckProtocol = params.get("HealthCheckProtocol")
        self._HealthCheckTemplateId = params.get("HealthCheckTemplateId")
        self._HealthCheckTemplateName = params.get("HealthCheckTemplateName")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckUnhealthyThreshold = params.get("HealthCheckUnhealthyThreshold")
        self._ModifyTime = params.get("ModifyTime")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPAddressInfo(AbstractModel):
    r"""应用型负载均衡可用区子网映射中的 IP 信息数据结构

    """

    def __init__(self):
        r"""
        :param _Address: IP 地址
        :type Address: str
        :param _AddressId: EIP AddressId
        :type AddressId: str
        """
        self._Address = None
        self._AddressId = None

    @property
    def Address(self):
        r"""IP 地址
        :rtype: str
        """
        return self._Address

    @Address.setter
    def Address(self, Address):
        self._Address = Address

    @property
    def AddressId(self):
        r"""EIP AddressId
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId


    def _deserialize(self, params):
        self._Address = params.get("Address")
        self._AddressId = params.get("AddressId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateLoadBalancerRequest(AbstractModel):
    r"""InquirePriceCreateLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ChargeType: 实例的计费类型。默认POSTPAID_BY_HOUR，仅取值 POSTPAID_BY_HOUR：表示按量计费。
        :type ChargeType: str
        """
        self._ChargeType = None

    @property
    def ChargeType(self):
        r"""实例的计费类型。默认POSTPAID_BY_HOUR，仅取值 POSTPAID_BY_HOUR：表示按量计费。
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType


    def _deserialize(self, params):
        self._ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateLoadBalancerResponse(AbstractModel):
    r"""InquirePriceCreateLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Price: 询价结果。
        :type Price: :class:`tencentcloud.alb.v20251030.models.Price`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Price = None
        self._RequestId = None

    @property
    def Price(self):
        r"""询价结果。
        :rtype: :class:`tencentcloud.alb.v20251030.models.Price`
        """
        return self._Price

    @Price.setter
    def Price(self, Price):
        self._Price = Price

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
        if params.get("Price") is not None:
            self._Price = Price()
            self._Price._deserialize(params.get("Price"))
        self._RequestId = params.get("RequestId")


class InsertHTTPHeaderInfo(AbstractModel):
    r"""插入HTTP Header信息

    """

    def __init__(self):
        r"""
        :param _Key: 插入的HTTP Header键，长度1 ~ 40个字符，支持的字符集为：a-z A-Z 0-9 - _ 。
不支持中文，不支持Cookie,Host,Content-Length,Connection,Upgrade,transfer-encoding,keep-alive,te,authority,x-forwarded-for,x-forwarded-proto,x-forwarded-host,x-forwarded-port。
        :type Key: str
        :param _Value: HTTP Header值的类型。
ValueType为SystemDefined时，取值范围 ClientPort：客户端端口，ClientIp：客户端 IP 地址，Protocol：客户端请求的协议，CLBPort：负载均衡实例监听端口。
ValueType为UserDefined时，长度1 ~ 128的可打印字符，不支持"，开头和结尾不能为空格，结尾不能为\。
ValueType为ReferenceHeader时，引用请求头中的某一个header，长度1~128的可打印字符，不支持"，开头和结尾不能为空格，结尾不能为\。
        :type Value: str
        :param _ValueType: HTTP Header值的类型，取值：
SystemDefined：系统定义的header。
UserDefined：用户自定义的header。
ReferenceHeader：引用请求头中的某一个header。
        :type ValueType: str
        """
        self._Key = None
        self._Value = None
        self._ValueType = None

    @property
    def Key(self):
        r"""插入的HTTP Header键，长度1 ~ 40个字符，支持的字符集为：a-z A-Z 0-9 - _ 。
不支持中文，不支持Cookie,Host,Content-Length,Connection,Upgrade,transfer-encoding,keep-alive,te,authority,x-forwarded-for,x-forwarded-proto,x-forwarded-host,x-forwarded-port。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""HTTP Header值的类型。
ValueType为SystemDefined时，取值范围 ClientPort：客户端端口，ClientIp：客户端 IP 地址，Protocol：客户端请求的协议，CLBPort：负载均衡实例监听端口。
ValueType为UserDefined时，长度1 ~ 128的可打印字符，不支持"，开头和结尾不能为空格，结尾不能为\。
ValueType为ReferenceHeader时，引用请求头中的某一个header，长度1~128的可打印字符，不支持"，开头和结尾不能为空格，结尾不能为\。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueType(self):
        r"""HTTP Header值的类型，取值：
SystemDefined：系统定义的header。
UserDefined：用户自定义的header。
ReferenceHeader：引用请求头中的某一个header。
        :rtype: str
        """
        return self._ValueType

    @ValueType.setter
    def ValueType(self, ValueType):
        self._ValueType = ValueType


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        self._ValueType = params.get("ValueType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Job(AbstractModel):
    r"""异步任务信息

    """

    def __init__(self):
        r"""
        :param _ApiName: 操作接口名称。
        :type ApiName: str
        :param _FlowId: 任务流Id
        :type FlowId: int
        :param _RequestId: 任务请求Id。
        :type RequestId: str
        :param _ResourceIds: 资源ID列表
        :type ResourceIds: list of str
        :param _Status: 任务状态。取值：Processing、Succeeded、Failed。
        :type Status: str
        """
        self._ApiName = None
        self._FlowId = None
        self._RequestId = None
        self._ResourceIds = None
        self._Status = None

    @property
    def ApiName(self):
        r"""操作接口名称。
        :rtype: str
        """
        return self._ApiName

    @ApiName.setter
    def ApiName(self, ApiName):
        self._ApiName = ApiName

    @property
    def FlowId(self):
        r"""任务流Id
        :rtype: int
        """
        return self._FlowId

    @FlowId.setter
    def FlowId(self, FlowId):
        self._FlowId = FlowId

    @property
    def RequestId(self):
        r"""任务请求Id。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def ResourceIds(self):
        r"""资源ID列表
        :rtype: list of str
        """
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Status(self):
        r"""任务状态。取值：Processing、Succeeded、Failed。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ApiName = params.get("ApiName")
        self._FlowId = params.get("FlowId")
        self._RequestId = params.get("RequestId")
        self._ResourceIds = params.get("ResourceIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerOutput(AbstractModel):
    r"""监听器简要信息出参

    """

    def __init__(self):
        r"""
        :param _CaEnable: 是否开启双向认证。
        :type CaEnable: bool
        :param _CreateTime: 监听器实例的创建时间。格式：ISO 8601（例如 2025-01-01T08:30:00+08:00）
        :type CreateTime: str
        :param _GzipEnabled: 是否启用 Gzip 压缩。
        :type GzipEnabled: bool
        :param _Http2Enable: 是否启用http2。
        :type Http2Enable: bool
        :param _IdleTimeout: 空闲超时时间。
        :type IdleTimeout: int
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _ListenerName: 监听器名称。
        :type ListenerName: str
        :param _ListenerPort: 监听器端口。
        :type ListenerPort: int
        :param _ListenerProtocol: 监听器协议。
        :type ListenerProtocol: str
        :param _ListenerStatus: 监听器状态。取值:=

- **Active**: 运行中。
- **Provisioning**：创建中。
- **Configuring**：变配中。
- **ProvisionFailed**：创建失败
        :type ListenerStatus: str
        :param _ModifyTime: 监听器实例的最后变更时间。格式：ISO 8601（例如 2025-01-01T08:30:00+08:00）
        :type ModifyTime: str
        :param _RequestTimeout: 请求超时时间。
        :type RequestTimeout: int
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        :param _TlsSecurityPolicyId: 安全策略 ID。
        :type TlsSecurityPolicyId: str
        :param _XForwardedForConfig: XForwardedFor配置。
        :type XForwardedForConfig: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        self._CaEnable = None
        self._CreateTime = None
        self._GzipEnabled = None
        self._Http2Enable = None
        self._IdleTimeout = None
        self._ListenerId = None
        self._ListenerName = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._ListenerStatus = None
        self._ModifyTime = None
        self._RequestTimeout = None
        self._Tags = None
        self._TlsSecurityPolicyId = None
        self._XForwardedForConfig = None

    @property
    def CaEnable(self):
        r"""是否开启双向认证。
        :rtype: bool
        """
        return self._CaEnable

    @CaEnable.setter
    def CaEnable(self, CaEnable):
        self._CaEnable = CaEnable

    @property
    def CreateTime(self):
        r"""监听器实例的创建时间。格式：ISO 8601（例如 2025-01-01T08:30:00+08:00）
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def GzipEnabled(self):
        r"""是否启用 Gzip 压缩。
        :rtype: bool
        """
        return self._GzipEnabled

    @GzipEnabled.setter
    def GzipEnabled(self, GzipEnabled):
        self._GzipEnabled = GzipEnabled

    @property
    def Http2Enable(self):
        r"""是否启用http2。
        :rtype: bool
        """
        return self._Http2Enable

    @Http2Enable.setter
    def Http2Enable(self, Http2Enable):
        self._Http2Enable = Http2Enable

    @property
    def IdleTimeout(self):
        r"""空闲超时时间。
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        r"""监听器名称。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def ListenerPort(self):
        r"""监听器端口。
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""监听器协议。
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def ListenerStatus(self):
        r"""监听器状态。取值:=

- **Active**: 运行中。
- **Provisioning**：创建中。
- **Configuring**：变配中。
- **ProvisionFailed**：创建失败
        :rtype: str
        """
        return self._ListenerStatus

    @ListenerStatus.setter
    def ListenerStatus(self, ListenerStatus):
        self._ListenerStatus = ListenerStatus

    @property
    def ModifyTime(self):
        r"""监听器实例的最后变更时间。格式：ISO 8601（例如 2025-01-01T08:30:00+08:00）
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def RequestTimeout(self):
        r"""请求超时时间。
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TlsSecurityPolicyId(self):
        r"""安全策略 ID。
        :rtype: str
        """
        return self._TlsSecurityPolicyId

    @TlsSecurityPolicyId.setter
    def TlsSecurityPolicyId(self, TlsSecurityPolicyId):
        self._TlsSecurityPolicyId = TlsSecurityPolicyId

    @property
    def XForwardedForConfig(self):
        r"""XForwardedFor配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        return self._XForwardedForConfig

    @XForwardedForConfig.setter
    def XForwardedForConfig(self, XForwardedForConfig):
        self._XForwardedForConfig = XForwardedForConfig


    def _deserialize(self, params):
        self._CaEnable = params.get("CaEnable")
        self._CreateTime = params.get("CreateTime")
        self._GzipEnabled = params.get("GzipEnabled")
        self._Http2Enable = params.get("Http2Enable")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._ListenerStatus = params.get("ListenerStatus")
        self._ModifyTime = params.get("ModifyTime")
        self._RequestTimeout = params.get("RequestTimeout")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TlsSecurityPolicyId = params.get("TlsSecurityPolicyId")
        if params.get("XForwardedForConfig") is not None:
            self._XForwardedForConfig = XForwardedForConfig()
            self._XForwardedForConfig._deserialize(params.get("XForwardedForConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    r"""列表展示的应用型负载均衡实例结构。

    """

    def __init__(self):
        r"""
        :param _AccessLogConfig: 访问日志配置结构。
        :type AccessLogConfig: :class:`tencentcloud.alb.v20251030.models.AccessLogConfig`
        :param _AddressIpVersion: IP 地址版本，取值 IPv4 或 IPv6。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressIpVersion: str
        :param _AddressType: 负载均衡的地址类型。取值：

- **Internet**：负载均衡具有公网IP地址，DNS域名被解析到公网IP，因此可以在公网环境访问。

- **Intranet**：负载均衡只有私网IP地址，DNS域名被解析到私网IP，因此只能被负载均衡所在VPC的内网环境访问。
注意：此字段可能返回 null，表示取不到有效值。
        :type AddressType: str
        :param _CreateTime: 资源创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _DeletionProtection: 删除保护设置信息。
        :type DeletionProtection: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        :param _Domain: DNS域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _LoadBalancerBillingConfig: 负载均衡实例计费配置。
        :type LoadBalancerBillingConfig: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 负载均衡实例名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerName: str
        :param _LoadBalancerOperationLocks: 负载均衡操作锁配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerOperationLocks: list of LoadBalancerOperationLocksItem
        :param _LoadBalancerStatus: 应用型负载均衡实例状态。取值：

- **Provisioning**：创建中。
- **Active**: 运行中。
- **Configuring**: 变配中。
- **Deleting**：删除中。
- **ProvisionFailed**：创建失败。
- **ConfigureFailed**：变配失败。
- **DeletionFailed**：删除失败。
- **Abnormal**：异常状态，具体异常原因参见LoadBalancerOperationLocks字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerStatus: str
        :param _ModificationProtection: 修改保护设置信息。
        :type ModificationProtection: :class:`tencentcloud.alb.v20251030.models.ModificationProtectionInfo`
        :param _Tags: 标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of TagInfo
        :param _VpcId: 私有网络 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        """
        self._AccessLogConfig = None
        self._AddressIpVersion = None
        self._AddressType = None
        self._CreateTime = None
        self._DeletionProtection = None
        self._Domain = None
        self._LoadBalancerBillingConfig = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerOperationLocks = None
        self._LoadBalancerStatus = None
        self._ModificationProtection = None
        self._Tags = None
        self._VpcId = None

    @property
    def AccessLogConfig(self):
        r"""访问日志配置结构。
        :rtype: :class:`tencentcloud.alb.v20251030.models.AccessLogConfig`
        """
        return self._AccessLogConfig

    @AccessLogConfig.setter
    def AccessLogConfig(self, AccessLogConfig):
        self._AccessLogConfig = AccessLogConfig

    @property
    def AddressIpVersion(self):
        r"""IP 地址版本，取值 IPv4 或 IPv6。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddressIpVersion

    @AddressIpVersion.setter
    def AddressIpVersion(self, AddressIpVersion):
        self._AddressIpVersion = AddressIpVersion

    @property
    def AddressType(self):
        r"""负载均衡的地址类型。取值：

- **Internet**：负载均衡具有公网IP地址，DNS域名被解析到公网IP，因此可以在公网环境访问。

- **Intranet**：负载均衡只有私网IP地址，DNS域名被解析到私网IP，因此只能被负载均衡所在VPC的内网环境访问。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def CreateTime(self):
        r"""资源创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeletionProtection(self):
        r"""删除保护设置信息。
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Domain(self):
        r"""DNS域名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerBillingConfig(self):
        r"""负载均衡实例计费配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        """
        return self._LoadBalancerBillingConfig

    @LoadBalancerBillingConfig.setter
    def LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):
        self._LoadBalancerBillingConfig = LoadBalancerBillingConfig

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""负载均衡实例名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerOperationLocks(self):
        r"""负载均衡操作锁配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of LoadBalancerOperationLocksItem
        """
        return self._LoadBalancerOperationLocks

    @LoadBalancerOperationLocks.setter
    def LoadBalancerOperationLocks(self, LoadBalancerOperationLocks):
        self._LoadBalancerOperationLocks = LoadBalancerOperationLocks

    @property
    def LoadBalancerStatus(self):
        r"""应用型负载均衡实例状态。取值：

- **Provisioning**：创建中。
- **Active**: 运行中。
- **Configuring**: 变配中。
- **Deleting**：删除中。
- **ProvisionFailed**：创建失败。
- **ConfigureFailed**：变配失败。
- **DeletionFailed**：删除失败。
- **Abnormal**：异常状态，具体异常原因参见LoadBalancerOperationLocks字段。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LoadBalancerStatus

    @LoadBalancerStatus.setter
    def LoadBalancerStatus(self, LoadBalancerStatus):
        self._LoadBalancerStatus = LoadBalancerStatus

    @property
    def ModificationProtection(self):
        r"""修改保护设置信息。
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModificationProtectionInfo`
        """
        return self._ModificationProtection

    @ModificationProtection.setter
    def ModificationProtection(self, ModificationProtection):
        self._ModificationProtection = ModificationProtection

    @property
    def Tags(self):
        r"""标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VpcId(self):
        r"""私有网络 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        if params.get("AccessLogConfig") is not None:
            self._AccessLogConfig = AccessLogConfig()
            self._AccessLogConfig._deserialize(params.get("AccessLogConfig"))
        self._AddressIpVersion = params.get("AddressIpVersion")
        self._AddressType = params.get("AddressType")
        self._CreateTime = params.get("CreateTime")
        if params.get("DeletionProtection") is not None:
            self._DeletionProtection = DeletionProtectionConfig()
            self._DeletionProtection._deserialize(params.get("DeletionProtection"))
        self._Domain = params.get("Domain")
        if params.get("LoadBalancerBillingConfig") is not None:
            self._LoadBalancerBillingConfig = LoadBalancerBillingConfig()
            self._LoadBalancerBillingConfig._deserialize(params.get("LoadBalancerBillingConfig"))
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("LoadBalancerOperationLocks") is not None:
            self._LoadBalancerOperationLocks = []
            for item in params.get("LoadBalancerOperationLocks"):
                obj = LoadBalancerOperationLocksItem()
                obj._deserialize(item)
                self._LoadBalancerOperationLocks.append(obj)
        self._LoadBalancerStatus = params.get("LoadBalancerStatus")
        if params.get("ModificationProtection") is not None:
            self._ModificationProtection = ModificationProtectionInfo()
            self._ModificationProtection._deserialize(params.get("ModificationProtection"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerAddress(AbstractModel):
    r"""应用型负载均衡可用区子网映射中的 IP 信息数据结构

    """

    def __init__(self):
        r"""
        :param _IPv4Address: IPv4 地址列表
        :type IPv4Address: list of IPAddressInfo
        :param _IPv6Address: IPv6 地址列表
        :type IPv6Address: list of IPAddressInfo
        """
        self._IPv4Address = None
        self._IPv6Address = None

    @property
    def IPv4Address(self):
        r"""IPv4 地址列表
        :rtype: list of IPAddressInfo
        """
        return self._IPv4Address

    @IPv4Address.setter
    def IPv4Address(self, IPv4Address):
        self._IPv4Address = IPv4Address

    @property
    def IPv6Address(self):
        r"""IPv6 地址列表
        :rtype: list of IPAddressInfo
        """
        return self._IPv6Address

    @IPv6Address.setter
    def IPv6Address(self, IPv6Address):
        self._IPv6Address = IPv6Address


    def _deserialize(self, params):
        if params.get("IPv4Address") is not None:
            self._IPv4Address = []
            for item in params.get("IPv4Address"):
                obj = IPAddressInfo()
                obj._deserialize(item)
                self._IPv4Address.append(obj)
        if params.get("IPv6Address") is not None:
            self._IPv6Address = []
            for item in params.get("IPv6Address"):
                obj = IPAddressInfo()
                obj._deserialize(item)
                self._IPv6Address.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerBillingConfig(AbstractModel):
    r"""应用型负载均衡实例计费配置。

    """

    def __init__(self):
        r"""
        :param _ChargeType: 实例的计费类型。

取值**POSTPAID_BY_HOUR**：表示按量计费。
注意：此字段可能返回 null，表示取不到有效值。
        :type ChargeType: str
        :param _BandwidthPackageId: 共享带宽包 ID。
        :type BandwidthPackageId: str
        """
        self._ChargeType = None
        self._BandwidthPackageId = None

    @property
    def ChargeType(self):
        r"""实例的计费类型。

取值**POSTPAID_BY_HOUR**：表示按量计费。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChargeType

    @ChargeType.setter
    def ChargeType(self, ChargeType):
        self._ChargeType = ChargeType

    @property
    def BandwidthPackageId(self):
        r"""共享带宽包 ID。
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId


    def _deserialize(self, params):
        self._ChargeType = params.get("ChargeType")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerDetail(AbstractModel):
    r"""负载均衡详细信息

    """

    def __init__(self):
        r"""
        :param _AccessLogConfig: 访问日志配置。
        :type AccessLogConfig: :class:`tencentcloud.alb.v20251030.models.AccessLogConfig`
        :param _AddressIpVersion: IP 地址版本，取值 IPv4 或 IPv6。
        :type AddressIpVersion: str
        :param _AddressType: 应用型负载均衡实例的网络地址类型。取值：

- **Internet/Public**：负载均衡具有公网IP地址，DNS域名被解析到公网IP，因此可以在公网环境访问。

- **Intranet/Internal**：负载均衡只有私网IP地址，DNS域名被解析到私网IP，因此只能被负载均衡所在VPC的内网环境访问。


        :type AddressType: str
        :param _CreateTime: 资源创建时间，格式为`yyyy-MM-ddTHH:mm:ss±hh:mm`。
        :type CreateTime: str
        :param _DeletionProtection: 删除保护设置信息。
        :type DeletionProtection: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        :param _Domain: DNS域名。
        :type Domain: str
        :param _LoadBalancerBillingConfig: 负载均衡实例付计费配置信息
        :type LoadBalancerBillingConfig: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _LoadBalancerName: 实例名称。

长度为1~80个字符，可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）。
        :type LoadBalancerName: str
        :param _LoadBalancerOperationLocks: 应用型负载均衡操作锁配置。
        :type LoadBalancerOperationLocks: list of LoadBalancerOperationLocksItem
        :param _LoadBalancerStatus: 应用型负载均衡实例状态。取值：

- **Provisioning**：创建中。
- **Active**: 运行中。
- **Configuring**: 变配中。
- **Deleting**：删除中。
- **ProvisionFailed**：创建失败。
- **ConfigureFailed**：变配失败。
- **DeletionFailed**：删除失败。
- **Abnormal**：异常状态，具体异常原因参见LoadBalancerOperationLocks字段。
        :type LoadBalancerStatus: str
        :param _ModificationProtection: 修改保护设置信息。
        :type ModificationProtection: :class:`tencentcloud.alb.v20251030.models.ModificationProtectionInfo`
        :param _SecurityGroupIds: 应用型负载均衡实例绑定的安全组ID集合。
        :type SecurityGroupIds: list of str
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        :param _VpcId: 私有网络 ID。
        :type VpcId: str
        :param _ZoneMappings: 可用区及子网映射列表，最多返回10个可用区。若当前地域支持2个及以上可用区，至少返回2个及以上可用区。
        :type ZoneMappings: list of ZoneMappingInfo
        """
        self._AccessLogConfig = None
        self._AddressIpVersion = None
        self._AddressType = None
        self._CreateTime = None
        self._DeletionProtection = None
        self._Domain = None
        self._LoadBalancerBillingConfig = None
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._LoadBalancerOperationLocks = None
        self._LoadBalancerStatus = None
        self._ModificationProtection = None
        self._SecurityGroupIds = None
        self._Tags = None
        self._VpcId = None
        self._ZoneMappings = None

    @property
    def AccessLogConfig(self):
        r"""访问日志配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.AccessLogConfig`
        """
        return self._AccessLogConfig

    @AccessLogConfig.setter
    def AccessLogConfig(self, AccessLogConfig):
        self._AccessLogConfig = AccessLogConfig

    @property
    def AddressIpVersion(self):
        r"""IP 地址版本，取值 IPv4 或 IPv6。
        :rtype: str
        """
        return self._AddressIpVersion

    @AddressIpVersion.setter
    def AddressIpVersion(self, AddressIpVersion):
        self._AddressIpVersion = AddressIpVersion

    @property
    def AddressType(self):
        r"""应用型负载均衡实例的网络地址类型。取值：

- **Internet/Public**：负载均衡具有公网IP地址，DNS域名被解析到公网IP，因此可以在公网环境访问。

- **Intranet/Internal**：负载均衡只有私网IP地址，DNS域名被解析到私网IP，因此只能被负载均衡所在VPC的内网环境访问。


        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def CreateTime(self):
        r"""资源创建时间，格式为`yyyy-MM-ddTHH:mm:ss±hh:mm`。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DeletionProtection(self):
        r"""删除保护设置信息。
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def Domain(self):
        r"""DNS域名。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LoadBalancerBillingConfig(self):
        r"""负载均衡实例付计费配置信息
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerBillingConfig`
        """
        return self._LoadBalancerBillingConfig

    @LoadBalancerBillingConfig.setter
    def LoadBalancerBillingConfig(self, LoadBalancerBillingConfig):
        self._LoadBalancerBillingConfig = LoadBalancerBillingConfig

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        r"""实例名称。

长度为1~80个字符，可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def LoadBalancerOperationLocks(self):
        r"""应用型负载均衡操作锁配置。
        :rtype: list of LoadBalancerOperationLocksItem
        """
        return self._LoadBalancerOperationLocks

    @LoadBalancerOperationLocks.setter
    def LoadBalancerOperationLocks(self, LoadBalancerOperationLocks):
        self._LoadBalancerOperationLocks = LoadBalancerOperationLocks

    @property
    def LoadBalancerStatus(self):
        r"""应用型负载均衡实例状态。取值：

- **Provisioning**：创建中。
- **Active**: 运行中。
- **Configuring**: 变配中。
- **Deleting**：删除中。
- **ProvisionFailed**：创建失败。
- **ConfigureFailed**：变配失败。
- **DeletionFailed**：删除失败。
- **Abnormal**：异常状态，具体异常原因参见LoadBalancerOperationLocks字段。
        :rtype: str
        """
        return self._LoadBalancerStatus

    @LoadBalancerStatus.setter
    def LoadBalancerStatus(self, LoadBalancerStatus):
        self._LoadBalancerStatus = LoadBalancerStatus

    @property
    def ModificationProtection(self):
        r"""修改保护设置信息。
        :rtype: :class:`tencentcloud.alb.v20251030.models.ModificationProtectionInfo`
        """
        return self._ModificationProtection

    @ModificationProtection.setter
    def ModificationProtection(self, ModificationProtection):
        self._ModificationProtection = ModificationProtection

    @property
    def SecurityGroupIds(self):
        r"""应用型负载均衡实例绑定的安全组ID集合。
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def VpcId(self):
        r"""私有网络 ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def ZoneMappings(self):
        r"""可用区及子网映射列表，最多返回10个可用区。若当前地域支持2个及以上可用区，至少返回2个及以上可用区。
        :rtype: list of ZoneMappingInfo
        """
        return self._ZoneMappings

    @ZoneMappings.setter
    def ZoneMappings(self, ZoneMappings):
        self._ZoneMappings = ZoneMappings


    def _deserialize(self, params):
        if params.get("AccessLogConfig") is not None:
            self._AccessLogConfig = AccessLogConfig()
            self._AccessLogConfig._deserialize(params.get("AccessLogConfig"))
        self._AddressIpVersion = params.get("AddressIpVersion")
        self._AddressType = params.get("AddressType")
        self._CreateTime = params.get("CreateTime")
        if params.get("DeletionProtection") is not None:
            self._DeletionProtection = DeletionProtectionConfig()
            self._DeletionProtection._deserialize(params.get("DeletionProtection"))
        self._Domain = params.get("Domain")
        if params.get("LoadBalancerBillingConfig") is not None:
            self._LoadBalancerBillingConfig = LoadBalancerBillingConfig()
            self._LoadBalancerBillingConfig._deserialize(params.get("LoadBalancerBillingConfig"))
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("LoadBalancerOperationLocks") is not None:
            self._LoadBalancerOperationLocks = []
            for item in params.get("LoadBalancerOperationLocks"):
                obj = LoadBalancerOperationLocksItem()
                obj._deserialize(item)
                self._LoadBalancerOperationLocks.append(obj)
        self._LoadBalancerStatus = params.get("LoadBalancerStatus")
        if params.get("ModificationProtection") is not None:
            self._ModificationProtection = ModificationProtectionInfo()
            self._ModificationProtection._deserialize(params.get("ModificationProtection"))
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._VpcId = params.get("VpcId")
        if params.get("ZoneMappings") is not None:
            self._ZoneMappings = []
            for item in params.get("ZoneMappings"):
                obj = ZoneMappingInfo()
                obj._deserialize(item)
                self._ZoneMappings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerOperationLocksItem(AbstractModel):
    r"""应用型负载均衡操作锁配置。

    """

    def __init__(self):
        r"""
        :param _LockReason: 锁定的原因。在**LoadBalancerStatus**为**Abnormal**时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type LockReason: str
        :param _LockType: 锁定的类型。取值 ：

- **SecurityLocked**：安全锁定。

- **RelatedResourceLocked**：关联锁定。

- **FinancialLocked**：欠费锁定。

- **ResidualLocked**：残留锁定。
注意：此字段可能返回 null，表示取不到有效值。
        :type LockType: str
        """
        self._LockReason = None
        self._LockType = None

    @property
    def LockReason(self):
        r"""锁定的原因。在**LoadBalancerStatus**为**Abnormal**时有效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LockReason

    @LockReason.setter
    def LockReason(self, LockReason):
        self._LockReason = LockReason

    @property
    def LockType(self):
        r"""锁定的类型。取值 ：

- **SecurityLocked**：安全锁定。

- **RelatedResourceLocked**：关联锁定。

- **FinancialLocked**：欠费锁定。

- **ResidualLocked**：残留锁定。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LockType

    @LockType.setter
    def LockType(self, LockType):
        self._LockType = LockType


    def _deserialize(self, params):
        self._LockReason = params.get("LockReason")
        self._LockType = params.get("LockType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModificationProtectionInfo(AbstractModel):
    r"""修改保护状态信息。

    """

    def __init__(self):
        r"""
        :param _ModificationProtectionEnabled: 是否开启修改保护。开启后，可防止实例被意外修改或删除。
- true：开启修改保护
- false：关闭修改保护
        :type ModificationProtectionEnabled: bool
        :param _OperatorUin: 1238716123
        :type OperatorUin: str
        :param _Reason: 开启修改保护的原因说明。
长度为 1~255 个字符，必须是中文和无害字符串中的字符， 可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :type Reason: str
        """
        self._ModificationProtectionEnabled = None
        self._OperatorUin = None
        self._Reason = None

    @property
    def ModificationProtectionEnabled(self):
        r"""是否开启修改保护。开启后，可防止实例被意外修改或删除。
- true：开启修改保护
- false：关闭修改保护
        :rtype: bool
        """
        return self._ModificationProtectionEnabled

    @ModificationProtectionEnabled.setter
    def ModificationProtectionEnabled(self, ModificationProtectionEnabled):
        self._ModificationProtectionEnabled = ModificationProtectionEnabled

    @property
    def OperatorUin(self):
        r"""1238716123
        :rtype: str
        """
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin

    @property
    def Reason(self):
        r"""开启修改保护的原因说明。
长度为 1~255 个字符，必须是中文和无害字符串中的字符， 可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._ModificationProtectionEnabled = params.get("ModificationProtectionEnabled")
        self._OperatorUin = params.get("OperatorUin")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHealthCheckTemplateRequest(AbstractModel):
    r"""ModifyHealthCheckTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _HealthCheckTemplateId: 健康检查模板 ID，格式为 hct- 后接字母数字。
        :type HealthCheckTemplateId: str
        :param _DryRun: 是否预览此次请求。
- **false**（默认）：发送普通请求，直接修改健康检查模板。
- **true**：发送预览请求，检查修改健康检查模板的参数、格式、业务限制等是否符合要求。
        :type DryRun: bool
        :param _HealthCheckCodes: 健康检查状态码。取值：
- 当健康检查协议为**HTTP/HTTPS**时：
	- **http_1xx**
	- **http_2xx**（默认值）
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- 当健康检查协议为**GRPC/GRPCS**时：默认值为**12**，数值范围为**0-99**，输入值可为数值、多个数值或者范围以及相互组合，如：
	- **"20"**
	- **"0-99"**
        :type HealthCheckCodes: list of str
        :param _HealthCheckHealthyThreshold: 判定后端服务健康的阈值，当健康检查连续成功多少次后，后端服务的状态由**不健康**变为**健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :type HealthCheckHealthyThreshold: int
        :param _HealthCheckHost: 健康检查域名。
长度限制为 **1-255** 个字符。
可包含小写字母、数字、短划线（-）和半角句号（.）。

> 仅当 **HealthCheckProtocol** 设置为 **HTTP/HTTPS/GRPC/GRPCS** 时，该参数生效。
        :type HealthCheckHost: str
        :param _HealthCheckHttpVersion: 健康检查 HTTP 协议版本，取值：
- **HTTP1.1**（默认）
- **HTTP1.0** 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :type HealthCheckHttpVersion: str
        :param _HealthCheckInterval: 健康检查的时间间隔。单位：秒。 取值范围：**2**-**300**。 默认值：**5**。
        :type HealthCheckInterval: int
        :param _HealthCheckMethod: 健康检查方法，取值： - **GET** - **HEAD**（默认值） 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :type HealthCheckMethod: str
        :param _HealthCheckPath: 健康检查的转发规则路径。 长度为 **1-80** 个字符，只能使用字母、数字、字符`-/.%?#&=`以及扩展字符`_;~!（)*[]@$^:',+`。 URL 必须以正斜线（/）开头。 
> 仅当**HealthCheckProtocol**为**HTTP/HTTPS/GRPC/GRPCS**时，转发规则路径参数生效。
        :type HealthCheckPath: str
        :param _HealthCheckPort: 健康检查访问后端服务器的端口。  取值范围：**0-65535**。  默认值：**0**，表示后端服务器的端口。
        :type HealthCheckPort: int
        :param _HealthCheckProtocol: 健康检查协议。取值：
- **HTTP**（默认）：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。
- **HTTPS**：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。（数据加密，相比 HTTP 更安全。）
- **TCP**：通过发送 SYN 握手报文来检测服务器端口是否存活。
- **GRPC**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
- **GRPCS**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
        :type HealthCheckProtocol: str
        :param _HealthCheckTemplateName: 健康检查模板名称。长度为 **1-255** 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :type HealthCheckTemplateName: str
        :param _HealthCheckTimeout: 健康检查的响应超时时间。单位：秒。
取值范围：**2**-**60**。
默认值：**2**。
        :type HealthCheckTimeout: int
        :param _HealthCheckUnhealthyThreshold: 判定后端服务不健康的阈值，当健康检查连续失败多少次后，后端服务的状态由**健康**变为**不健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :type HealthCheckUnhealthyThreshold: int
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        """
        self._HealthCheckTemplateId = None
        self._DryRun = None
        self._HealthCheckCodes = None
        self._HealthCheckHealthyThreshold = None
        self._HealthCheckHost = None
        self._HealthCheckHttpVersion = None
        self._HealthCheckInterval = None
        self._HealthCheckMethod = None
        self._HealthCheckPath = None
        self._HealthCheckPort = None
        self._HealthCheckProtocol = None
        self._HealthCheckTemplateName = None
        self._HealthCheckTimeout = None
        self._HealthCheckUnhealthyThreshold = None
        self._Tags = None

    @property
    def HealthCheckTemplateId(self):
        r"""健康检查模板 ID，格式为 hct- 后接字母数字。
        :rtype: str
        """
        return self._HealthCheckTemplateId

    @HealthCheckTemplateId.setter
    def HealthCheckTemplateId(self, HealthCheckTemplateId):
        self._HealthCheckTemplateId = HealthCheckTemplateId

    @property
    def DryRun(self):
        r"""是否预览此次请求。
- **false**（默认）：发送普通请求，直接修改健康检查模板。
- **true**：发送预览请求，检查修改健康检查模板的参数、格式、业务限制等是否符合要求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def HealthCheckCodes(self):
        r"""健康检查状态码。取值：
- 当健康检查协议为**HTTP/HTTPS**时：
	- **http_1xx**
	- **http_2xx**（默认值）
	-  **http_3xx**
	-  **http_4xx**
	-  **http_5xx**
- 当健康检查协议为**GRPC/GRPCS**时：默认值为**12**，数值范围为**0-99**，输入值可为数值、多个数值或者范围以及相互组合，如：
	- **"20"**
	- **"0-99"**
        :rtype: list of str
        """
        return self._HealthCheckCodes

    @HealthCheckCodes.setter
    def HealthCheckCodes(self, HealthCheckCodes):
        self._HealthCheckCodes = HealthCheckCodes

    @property
    def HealthCheckHealthyThreshold(self):
        r"""判定后端服务健康的阈值，当健康检查连续成功多少次后，后端服务的状态由**不健康**变为**健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckHealthyThreshold

    @HealthCheckHealthyThreshold.setter
    def HealthCheckHealthyThreshold(self, HealthCheckHealthyThreshold):
        self._HealthCheckHealthyThreshold = HealthCheckHealthyThreshold

    @property
    def HealthCheckHost(self):
        r"""健康检查域名。
长度限制为 **1-255** 个字符。
可包含小写字母、数字、短划线（-）和半角句号（.）。

> 仅当 **HealthCheckProtocol** 设置为 **HTTP/HTTPS/GRPC/GRPCS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckHost

    @HealthCheckHost.setter
    def HealthCheckHost(self, HealthCheckHost):
        self._HealthCheckHost = HealthCheckHost

    @property
    def HealthCheckHttpVersion(self):
        r"""健康检查 HTTP 协议版本，取值：
- **HTTP1.1**（默认）
- **HTTP1.0** 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckHttpVersion

    @HealthCheckHttpVersion.setter
    def HealthCheckHttpVersion(self, HealthCheckHttpVersion):
        self._HealthCheckHttpVersion = HealthCheckHttpVersion

    @property
    def HealthCheckInterval(self):
        r"""健康检查的时间间隔。单位：秒。 取值范围：**2**-**300**。 默认值：**5**。
        :rtype: int
        """
        return self._HealthCheckInterval

    @HealthCheckInterval.setter
    def HealthCheckInterval(self, HealthCheckInterval):
        self._HealthCheckInterval = HealthCheckInterval

    @property
    def HealthCheckMethod(self):
        r"""健康检查方法，取值： - **GET** - **HEAD**（默认值） 
> 仅当**HealthCheckProtocol**设置为**HTTP** 或 **HTTPS** 时，该参数生效。
        :rtype: str
        """
        return self._HealthCheckMethod

    @HealthCheckMethod.setter
    def HealthCheckMethod(self, HealthCheckMethod):
        self._HealthCheckMethod = HealthCheckMethod

    @property
    def HealthCheckPath(self):
        r"""健康检查的转发规则路径。 长度为 **1-80** 个字符，只能使用字母、数字、字符`-/.%?#&=`以及扩展字符`_;~!（)*[]@$^:',+`。 URL 必须以正斜线（/）开头。 
> 仅当**HealthCheckProtocol**为**HTTP/HTTPS/GRPC/GRPCS**时，转发规则路径参数生效。
        :rtype: str
        """
        return self._HealthCheckPath

    @HealthCheckPath.setter
    def HealthCheckPath(self, HealthCheckPath):
        self._HealthCheckPath = HealthCheckPath

    @property
    def HealthCheckPort(self):
        r"""健康检查访问后端服务器的端口。  取值范围：**0-65535**。  默认值：**0**，表示后端服务器的端口。
        :rtype: int
        """
        return self._HealthCheckPort

    @HealthCheckPort.setter
    def HealthCheckPort(self, HealthCheckPort):
        self._HealthCheckPort = HealthCheckPort

    @property
    def HealthCheckProtocol(self):
        r"""健康检查协议。取值：
- **HTTP**（默认）：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。
- **HTTPS**：通过发送 HEAD 或 GET 请求模拟浏览器的访问行为来检查服务器应用是否健康。（数据加密，相比 HTTP 更安全。）
- **TCP**：通过发送 SYN 握手报文来检测服务器端口是否存活。
- **GRPC**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
- **GRPCS**：通过发送 POST 或 GET 请求来检查服务器应用是否健康。
        :rtype: str
        """
        return self._HealthCheckProtocol

    @HealthCheckProtocol.setter
    def HealthCheckProtocol(self, HealthCheckProtocol):
        self._HealthCheckProtocol = HealthCheckProtocol

    @property
    def HealthCheckTemplateName(self):
        r"""健康检查模板名称。长度为 **1-255** 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :rtype: str
        """
        return self._HealthCheckTemplateName

    @HealthCheckTemplateName.setter
    def HealthCheckTemplateName(self, HealthCheckTemplateName):
        self._HealthCheckTemplateName = HealthCheckTemplateName

    @property
    def HealthCheckTimeout(self):
        r"""健康检查的响应超时时间。单位：秒。
取值范围：**2**-**60**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckTimeout

    @HealthCheckTimeout.setter
    def HealthCheckTimeout(self, HealthCheckTimeout):
        self._HealthCheckTimeout = HealthCheckTimeout

    @property
    def HealthCheckUnhealthyThreshold(self):
        r"""判定后端服务不健康的阈值，当健康检查连续失败多少次后，后端服务的状态由**健康**变为**不健康**。
取值范围：**2**-**10**。
默认值：**2**。
        :rtype: int
        """
        return self._HealthCheckUnhealthyThreshold

    @HealthCheckUnhealthyThreshold.setter
    def HealthCheckUnhealthyThreshold(self, HealthCheckUnhealthyThreshold):
        self._HealthCheckUnhealthyThreshold = HealthCheckUnhealthyThreshold

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._HealthCheckTemplateId = params.get("HealthCheckTemplateId")
        self._DryRun = params.get("DryRun")
        self._HealthCheckCodes = params.get("HealthCheckCodes")
        self._HealthCheckHealthyThreshold = params.get("HealthCheckHealthyThreshold")
        self._HealthCheckHost = params.get("HealthCheckHost")
        self._HealthCheckHttpVersion = params.get("HealthCheckHttpVersion")
        self._HealthCheckInterval = params.get("HealthCheckInterval")
        self._HealthCheckMethod = params.get("HealthCheckMethod")
        self._HealthCheckPath = params.get("HealthCheckPath")
        self._HealthCheckPort = params.get("HealthCheckPort")
        self._HealthCheckProtocol = params.get("HealthCheckProtocol")
        self._HealthCheckTemplateName = params.get("HealthCheckTemplateName")
        self._HealthCheckTimeout = params.get("HealthCheckTimeout")
        self._HealthCheckUnhealthyThreshold = params.get("HealthCheckUnhealthyThreshold")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHealthCheckTemplateResponse(AbstractModel):
    r"""ModifyHealthCheckTemplate返回参数结构体

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


class ModifyListenerAttributesRequest(AbstractModel):
    r"""ModifyListenerAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _CaCertificateIds: 监听器配置的CA证书ID列表。目前仅支持添加1个CA证书。
        :type CaCertificateIds: list of str
        :param _CaEnabled: 是否开启双向认证。
取值：
true：开启。
false（默认值）：不开启。
        :type CaEnabled: bool
        :param _CertificateIds: 服务器证书 ID 列表。
        :type CertificateIds: list of str
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。  

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。
        :type ClientToken: str
        :param _DefaultActions: 默认转发规则动作列表。目前监听器仅支持添加 1 个默认转发规则动作。
        :type DefaultActions: list of DefaultAction
        :param _GzipEnabled: 是否启用 Gzip 压缩。
        :type GzipEnabled: bool
        :param _Http2Enabled: 是否开启HTTP/2特性。只有 HTTPS 协议支持此参数。
        :type Http2Enabled: bool
        :param _IdleTimeout: 指定连接空闲超时时间。单位：秒。
取值范围：1~600。
默认值：15。
如果在设定时间内一直没有访问请求，负载均衡会暂时断开当前连接，下次请求来临时重新建立新的连接。
        :type IdleTimeout: int
        :param _ListenerName: 自定义监听名称。  长度为 1~255 个字符，必须是中文和无害字符串中的字符，  可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :type ListenerName: str
        :param _RequestTimeout: 指定请求超时时间。单位：秒。
取值：1~600。
默认值：60。
如果在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，并给客户端返回HTTP 504错误码。
        :type RequestTimeout: int
        :param _SecurityPolicyId: 安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :type SecurityPolicyId: str
        :param _XForwardedForConfig: XForwardedFor配置。
        :type XForwardedForConfig: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._CaCertificateIds = None
        self._CaEnabled = None
        self._CertificateIds = None
        self._ClientToken = None
        self._DefaultActions = None
        self._GzipEnabled = None
        self._Http2Enabled = None
        self._IdleTimeout = None
        self._ListenerName = None
        self._RequestTimeout = None
        self._SecurityPolicyId = None
        self._XForwardedForConfig = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def CaCertificateIds(self):
        r"""监听器配置的CA证书ID列表。目前仅支持添加1个CA证书。
        :rtype: list of str
        """
        return self._CaCertificateIds

    @CaCertificateIds.setter
    def CaCertificateIds(self, CaCertificateIds):
        self._CaCertificateIds = CaCertificateIds

    @property
    def CaEnabled(self):
        r"""是否开启双向认证。
取值：
true：开启。
false（默认值）：不开启。
        :rtype: bool
        """
        return self._CaEnabled

    @CaEnabled.setter
    def CaEnabled(self, CaEnabled):
        self._CaEnabled = CaEnabled

    @property
    def CertificateIds(self):
        r"""服务器证书 ID 列表。
        :rtype: list of str
        """
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。  

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DefaultActions(self):
        r"""默认转发规则动作列表。目前监听器仅支持添加 1 个默认转发规则动作。
        :rtype: list of DefaultAction
        """
        return self._DefaultActions

    @DefaultActions.setter
    def DefaultActions(self, DefaultActions):
        self._DefaultActions = DefaultActions

    @property
    def GzipEnabled(self):
        r"""是否启用 Gzip 压缩。
        :rtype: bool
        """
        return self._GzipEnabled

    @GzipEnabled.setter
    def GzipEnabled(self, GzipEnabled):
        self._GzipEnabled = GzipEnabled

    @property
    def Http2Enabled(self):
        r"""是否开启HTTP/2特性。只有 HTTPS 协议支持此参数。
        :rtype: bool
        """
        return self._Http2Enabled

    @Http2Enabled.setter
    def Http2Enabled(self, Http2Enabled):
        self._Http2Enabled = Http2Enabled

    @property
    def IdleTimeout(self):
        r"""指定连接空闲超时时间。单位：秒。
取值范围：1~600。
默认值：15。
如果在设定时间内一直没有访问请求，负载均衡会暂时断开当前连接，下次请求来临时重新建立新的连接。
        :rtype: int
        """
        return self._IdleTimeout

    @IdleTimeout.setter
    def IdleTimeout(self, IdleTimeout):
        self._IdleTimeout = IdleTimeout

    @property
    def ListenerName(self):
        r"""自定义监听名称。  长度为 1~255 个字符，必须是中文和无害字符串中的字符，  可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :rtype: str
        """
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def RequestTimeout(self):
        r"""指定请求超时时间。单位：秒。
取值：1~600。
默认值：60。
如果在超时时间内后端服务器一直没有响应，负载均衡将放弃等待，并给客户端返回HTTP 504错误码。
        :rtype: int
        """
        return self._RequestTimeout

    @RequestTimeout.setter
    def RequestTimeout(self, RequestTimeout):
        self._RequestTimeout = RequestTimeout

    @property
    def SecurityPolicyId(self):
        r"""安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def XForwardedForConfig(self):
        r"""XForwardedFor配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.XForwardedForConfig`
        """
        return self._XForwardedForConfig

    @XForwardedForConfig.setter
    def XForwardedForConfig(self, XForwardedForConfig):
        self._XForwardedForConfig = XForwardedForConfig


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._CaCertificateIds = params.get("CaCertificateIds")
        self._CaEnabled = params.get("CaEnabled")
        self._CertificateIds = params.get("CertificateIds")
        self._ClientToken = params.get("ClientToken")
        if params.get("DefaultActions") is not None:
            self._DefaultActions = []
            for item in params.get("DefaultActions"):
                obj = DefaultAction()
                obj._deserialize(item)
                self._DefaultActions.append(obj)
        self._GzipEnabled = params.get("GzipEnabled")
        self._Http2Enabled = params.get("Http2Enabled")
        self._IdleTimeout = params.get("IdleTimeout")
        self._ListenerName = params.get("ListenerName")
        self._RequestTimeout = params.get("RequestTimeout")
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        if params.get("XForwardedForConfig") is not None:
            self._XForwardedForConfig = XForwardedForConfig()
            self._XForwardedForConfig._deserialize(params.get("XForwardedForConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerAttributesResponse(AbstractModel):
    r"""ModifyListenerAttributes返回参数结构体

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


class ModifyLoadBalancerAddressTypeRequest(AbstractModel):
    r"""ModifyLoadBalancerAddressType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AddressType: 目标网络类型。取值：
- **Internet**（公网型）
负载均衡实例分配公网 IP 地址，域名（DNS）解析至公网 IP，可在公网环境中直接访问，适用于对外提供服务的业务场景。
- **Intranet**（内网型）
负载均衡实例仅分配私网 IP 地址，域名（DNS）解析至私网 IP，仅支持在负载均衡实例所属 VPC 内的内网环境访问，适用于内部业务或对安全性要求较高的场景。
        :type AddressType: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _BandwidthPackageId: 共享带宽包 ID。
        :type BandwidthPackageId: str
        :param _DryRun: 是否只预检此次请求。取值：
- **true**：发送检查请求，不会更新实例的网络类型。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码DryRunOperation。
- **false**（默认值）：发送正常请求，通过检查后返回 HTTP 2xx 状态码并直接进行操作。
        :type DryRun: bool
        :param _ZoneMappings: 可用区及子网映射结构体。
若当前地域支持 2 个及以上的可用区，至少需要添加 2 个可用区。
        :type ZoneMappings: list of ZoneMappingsItem
        """
        self._AddressType = None
        self._LoadBalancerId = None
        self._BandwidthPackageId = None
        self._DryRun = None
        self._ZoneMappings = None

    @property
    def AddressType(self):
        r"""目标网络类型。取值：
- **Internet**（公网型）
负载均衡实例分配公网 IP 地址，域名（DNS）解析至公网 IP，可在公网环境中直接访问，适用于对外提供服务的业务场景。
- **Intranet**（内网型）
负载均衡实例仅分配私网 IP 地址，域名（DNS）解析至私网 IP，仅支持在负载均衡实例所属 VPC 内的内网环境访问，适用于内部业务或对安全性要求较高的场景。
        :rtype: str
        """
        return self._AddressType

    @AddressType.setter
    def AddressType(self, AddressType):
        self._AddressType = AddressType

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def BandwidthPackageId(self):
        r"""共享带宽包 ID。
        :rtype: str
        """
        return self._BandwidthPackageId

    @BandwidthPackageId.setter
    def BandwidthPackageId(self, BandwidthPackageId):
        self._BandwidthPackageId = BandwidthPackageId

    @property
    def DryRun(self):
        r"""是否只预检此次请求。取值：
- **true**：发送检查请求，不会更新实例的网络类型。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码DryRunOperation。
- **false**（默认值）：发送正常请求，通过检查后返回 HTTP 2xx 状态码并直接进行操作。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def ZoneMappings(self):
        r"""可用区及子网映射结构体。
若当前地域支持 2 个及以上的可用区，至少需要添加 2 个可用区。
        :rtype: list of ZoneMappingsItem
        """
        return self._ZoneMappings

    @ZoneMappings.setter
    def ZoneMappings(self, ZoneMappings):
        self._ZoneMappings = ZoneMappings


    def _deserialize(self, params):
        self._AddressType = params.get("AddressType")
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._BandwidthPackageId = params.get("BandwidthPackageId")
        self._DryRun = params.get("DryRun")
        if params.get("ZoneMappings") is not None:
            self._ZoneMappings = []
            for item in params.get("ZoneMappings"):
                obj = ZoneMappingsItem()
                obj._deserialize(item)
                self._ZoneMappings.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAddressTypeResponse(AbstractModel):
    r"""ModifyLoadBalancerAddressType返回参数结构体

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


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    r"""ModifyLoadBalancerAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _ClientToken: 客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。

> 若您未指定，则系统自动使用API请求的**RequestId**作为**ClientToken**标识。每次API请求的**RequestId**不一样。
        :type ClientToken: str
        :param _DeletionProtection: 删除保护配置
        :type DeletionProtection: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        :param _DryRun: 是否只预检此次请求，取值：

- **true**：发送检查请求，不会修改应用型负载均衡实例的属性。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。

- **false**（默认值）：发送正常请求，通过检查后返回`HTTP_2xx`状态码并直接进行操作。
        :type DryRun: bool
        :param _LoadBalancerName: 应用型负载均衡实例名称。长度为1~80个字符，可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）。
        :type LoadBalancerName: str
        """
        self._LoadBalancerId = None
        self._ClientToken = None
        self._DeletionProtection = None
        self._DryRun = None
        self._LoadBalancerName = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ClientToken(self):
        r"""客户端Token，用于保证请求的幂等性。

从您的客户端生成一个参数值，确保不同请求间该参数值唯一。ClientToken只支持ASCII字符。

> 若您未指定，则系统自动使用API请求的**RequestId**作为**ClientToken**标识。每次API请求的**RequestId**不一样。
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def DeletionProtection(self):
        r"""删除保护配置
        :rtype: :class:`tencentcloud.alb.v20251030.models.DeletionProtectionConfig`
        """
        return self._DeletionProtection

    @DeletionProtection.setter
    def DeletionProtection(self, DeletionProtection):
        self._DeletionProtection = DeletionProtection

    @property
    def DryRun(self):
        r"""是否只预检此次请求，取值：

- **true**：发送检查请求，不会修改应用型负载均衡实例的属性。检查项包括是否填写了必需参数、请求格式、业务限制。如果检查不通过，则返回对应错误。如果检查通过，则返回错误码`DryRunOperation`。

- **false**（默认值）：发送正常请求，通过检查后返回`HTTP_2xx`状态码并直接进行操作。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def LoadBalancerName(self):
        r"""应用型负载均衡实例名称。长度为1~80个字符，可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）和下划线（_）。
        :rtype: str
        """
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ClientToken = params.get("ClientToken")
        if params.get("DeletionProtection") is not None:
            self._DeletionProtection = DeletionProtectionConfig()
            self._DeletionProtection._deserialize(params.get("DeletionProtection"))
        self._DryRun = params.get("DryRun")
        self._LoadBalancerName = params.get("LoadBalancerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    r"""ModifyLoadBalancerAttributes返回参数结构体

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


class ModifyLoadBalancerModificationProtectionRequest(AbstractModel):
    r"""ModifyLoadBalancerModificationProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _ModificationProtectionEnabled: 是否开启修改保护。开启后，可防止实例被意外修改或删除。\n- true：开启修改保护\n- false：关闭修改保护
        :type ModificationProtectionEnabled: bool
        :param _DryRun: 是否只预检此次请求。取值：
- true：仅执行预检，不实际操作资源。检查参数完整性、请求格式及业务限制，通过返回 DryRunOperation，不通过返回对应错误。
- false（默认）：执行正常请求，检查通过后直接操作资源。
        :type DryRun: bool
        :param _Reason: 开启修改保护的原因说明。
长度为 1~255 个字符，必须是中文和无害字符串中的字符， 可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :type Reason: str
        """
        self._LoadBalancerId = None
        self._ModificationProtectionEnabled = None
        self._DryRun = None
        self._Reason = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def ModificationProtectionEnabled(self):
        r"""是否开启修改保护。开启后，可防止实例被意外修改或删除。\n- true：开启修改保护\n- false：关闭修改保护
        :rtype: bool
        """
        return self._ModificationProtectionEnabled

    @ModificationProtectionEnabled.setter
    def ModificationProtectionEnabled(self, ModificationProtectionEnabled):
        self._ModificationProtectionEnabled = ModificationProtectionEnabled

    @property
    def DryRun(self):
        r"""是否只预检此次请求。取值：
- true：仅执行预检，不实际操作资源。检查参数完整性、请求格式及业务限制，通过返回 DryRunOperation，不通过返回对应错误。
- false（默认）：执行正常请求，检查通过后直接操作资源。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def Reason(self):
        r"""开启修改保护的原因说明。
长度为 1~255 个字符，必须是中文和无害字符串中的字符， 可包含中文、字母、数字、短划线（-）、正斜线（/）、半角句号（.）、下划线（_）。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._ModificationProtectionEnabled = params.get("ModificationProtectionEnabled")
        self._DryRun = params.get("DryRun")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerModificationProtectionResponse(AbstractModel):
    r"""ModifyLoadBalancerModificationProtection返回参数结构体

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


class ModifyRulesAttributesRequest(AbstractModel):
    r"""ModifyRulesAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _Rules: 转发规则列表。
        :type Rules: list of RuleModify
        :param _DryRun: 是否只预检查此次请求。
        :type DryRun: bool
        """
        self._ListenerId = None
        self._LoadBalancerId = None
        self._Rules = None
        self._DryRun = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def Rules(self):
        r"""转发规则列表。
        :rtype: list of RuleModify
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def DryRun(self):
        r"""是否只预检查此次请求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = RuleModify()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRulesAttributesResponse(AbstractModel):
    r"""ModifyRulesAttributes返回参数结构体

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


class ModifySecurityPolicyAttributesRequest(AbstractModel):
    r"""ModifySecurityPolicyAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SecurityPolicyId: <p>安全策略 ID，格式为 tls- 后接 8 位字母数字。</p>
        :type SecurityPolicyId: str
        :param _Ciphers: <p>修改后的加密套件列表。加密套件用于协商客户端与服务端之间的加密算法。</p><p><strong>配置说明：</strong></p><ul><li>加密套件的可选范围取决于所选的 TLS 协议版本（TLSVersions 参数）。</li><li>只要加密套件被任意一个已选 TLS 版本支持，即可添加到列表中。</li><li>若 TLSVersions 包含 TLSv1.3：可不指定 TLSv1.3 专属加密套件（系统将自动补全全部 TLSv1.3 套件）；若指定，则必须包含全部 TLSv1.3 专属加密套件，不支持仅指定部分。</li></ul><p><strong>获取可用加密套件：</strong><br>请调用 <a href="https://cloud.tencent.com/document/api/1822/133718">DescribeSecurityPolicyCapabilities</a> 接口查询各 TLS 版本支持的加密套件列表。</p><p><strong>注意：</strong> 若不传此参数，则保持原有配置不变。</p>
        :type Ciphers: list of str
        :param _DryRun: <p>是否仅执行预检请求。取值：</p><ul><li><strong>true</strong>：仅执行预检请求，不实际修改资源。预检请求将验证参数格式、权限及配置有效性等，帮助您在正式操作前发现潜在问题。</li><li><strong>false</strong>（默认）：执行正常请求，通过预检后将直接修改安全策略。</li></ul>
        :type DryRun: bool
        :param _SecurityPolicyName: <p>修改后的安全策略名称。用于标识和区分不同的安全策略。</p><p><strong>命名规则：</strong></p><ul><li>长度为 2~128 个字符。</li><li>必须以英文字母或中文开头。</li><li>可包含英文字母、中文、数字、半角句号（.）、下划线（_）和短划线（-）。</li></ul><p><strong>注意：</strong> 若不传此参数，则保持原有名称不变。</p>
        :type SecurityPolicyName: str
        :param _TLSVersions: <p>修改后的 TLS 协议版本列表。TLS（Transport Layer Security）协议用于保障客户端与负载均衡之间的通信安全。</p><p><strong>可选值：</strong></p><ul><li><strong>TLSv1.0</strong>：兼容性最好，但安全性较低，不推荐在生产环境使用。</li><li><strong>TLSv1.1</strong>：安全性略优于 TLSv1.0，但仍不推荐。</li><li><strong>TLSv1.2</strong>：目前主流的安全协议版本，兼顾安全性与兼容性。</li><li><strong>TLSv1.3</strong>：最新版本，安全性最高，性能更优，推荐优先使用。</li></ul><p><strong>注意：</strong> </p><ul><li>若不传此参数，则保持原有配置不变。</li><li>修改 TLS 版本时，请同步检查 Ciphers 参数的配置是否兼容。</li></ul>
        :type TLSVersions: list of str
        """
        self._SecurityPolicyId = None
        self._Ciphers = None
        self._DryRun = None
        self._SecurityPolicyName = None
        self._TLSVersions = None

    @property
    def SecurityPolicyId(self):
        r"""<p>安全策略 ID，格式为 tls- 后接 8 位字母数字。</p>
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def Ciphers(self):
        r"""<p>修改后的加密套件列表。加密套件用于协商客户端与服务端之间的加密算法。</p><p><strong>配置说明：</strong></p><ul><li>加密套件的可选范围取决于所选的 TLS 协议版本（TLSVersions 参数）。</li><li>只要加密套件被任意一个已选 TLS 版本支持，即可添加到列表中。</li><li>若 TLSVersions 包含 TLSv1.3：可不指定 TLSv1.3 专属加密套件（系统将自动补全全部 TLSv1.3 套件）；若指定，则必须包含全部 TLSv1.3 专属加密套件，不支持仅指定部分。</li></ul><p><strong>获取可用加密套件：</strong><br>请调用 <a href="https://cloud.tencent.com/document/api/1822/133718">DescribeSecurityPolicyCapabilities</a> 接口查询各 TLS 版本支持的加密套件列表。</p><p><strong>注意：</strong> 若不传此参数，则保持原有配置不变。</p>
        :rtype: list of str
        """
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def DryRun(self):
        r"""<p>是否仅执行预检请求。取值：</p><ul><li><strong>true</strong>：仅执行预检请求，不实际修改资源。预检请求将验证参数格式、权限及配置有效性等，帮助您在正式操作前发现潜在问题。</li><li><strong>false</strong>（默认）：执行正常请求，通过预检后将直接修改安全策略。</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def SecurityPolicyName(self):
        r"""<p>修改后的安全策略名称。用于标识和区分不同的安全策略。</p><p><strong>命名规则：</strong></p><ul><li>长度为 2~128 个字符。</li><li>必须以英文字母或中文开头。</li><li>可包含英文字母、中文、数字、半角句号（.）、下划线（_）和短划线（-）。</li></ul><p><strong>注意：</strong> 若不传此参数，则保持原有名称不变。</p>
        :rtype: str
        """
        return self._SecurityPolicyName

    @SecurityPolicyName.setter
    def SecurityPolicyName(self, SecurityPolicyName):
        self._SecurityPolicyName = SecurityPolicyName

    @property
    def TLSVersions(self):
        r"""<p>修改后的 TLS 协议版本列表。TLS（Transport Layer Security）协议用于保障客户端与负载均衡之间的通信安全。</p><p><strong>可选值：</strong></p><ul><li><strong>TLSv1.0</strong>：兼容性最好，但安全性较低，不推荐在生产环境使用。</li><li><strong>TLSv1.1</strong>：安全性略优于 TLSv1.0，但仍不推荐。</li><li><strong>TLSv1.2</strong>：目前主流的安全协议版本，兼顾安全性与兼容性。</li><li><strong>TLSv1.3</strong>：最新版本，安全性最高，性能更优，推荐优先使用。</li></ul><p><strong>注意：</strong> </p><ul><li>若不传此参数，则保持原有配置不变。</li><li>修改 TLS 版本时，请同步检查 Ciphers 参数的配置是否兼容。</li></ul>
        :rtype: list of str
        """
        return self._TLSVersions

    @TLSVersions.setter
    def TLSVersions(self, TLSVersions):
        self._TLSVersions = TLSVersions


    def _deserialize(self, params):
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        self._Ciphers = params.get("Ciphers")
        self._DryRun = params.get("DryRun")
        self._SecurityPolicyName = params.get("SecurityPolicyName")
        self._TLSVersions = params.get("TLSVersions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityPolicyAttributesResponse(AbstractModel):
    r"""ModifySecurityPolicyAttributes返回参数结构体

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


class ModifyTargetGroupAttributesRequest(AbstractModel):
    r"""ModifyTargetGroupAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DryRun: <p>是否预览此次请求。</p><ul><li><strong>false</strong>（默认）：发送普通请求，直接修改目标组。</li><li><strong>true</strong>：发送预览请求，检查修改目标组的参数、格式、业务限制等是否符合要求。</li></ul>
        :type DryRun: bool
        :param _HealthCheckConfig: <p>健康检查配置。</p>
        :type HealthCheckConfig: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        :param _KeepaliveEnabled: <p>是否开启长连接。</p>
        :type KeepaliveEnabled: bool
        :param _SchedulerAlgorithm: <p>调度算法。取值：</p><ul><li><strong>wrr</strong>：加权轮询，按照权重选择后端服务器，权重越高的服务器被轮询到的概率越高。</li><li><strong>wlc</strong>：加权最小连接数，当不同后端服务器权重值相同时，当前连接数越小的后端服务器被轮询到的概率越高。</li></ul>
        :type SchedulerAlgorithm: str
        :param _StickySessionConfig: <p>会话保持配置。</p>
        :type StickySessionConfig: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        :param _TargetGroupId: <p>目标组 ID，格式为 lbtg- 后接 8 位字母数字。</p>
        :type TargetGroupId: str
        :param _TargetGroupName: <p>目标组名称。长度为 1~255 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。不传目标组名称时默认使用ID作为目标组名称。</p>
        :type TargetGroupName: str
        """
        self._DryRun = None
        self._HealthCheckConfig = None
        self._KeepaliveEnabled = None
        self._SchedulerAlgorithm = None
        self._StickySessionConfig = None
        self._TargetGroupId = None
        self._TargetGroupName = None

    @property
    def DryRun(self):
        r"""<p>是否预览此次请求。</p><ul><li><strong>false</strong>（默认）：发送普通请求，直接修改目标组。</li><li><strong>true</strong>：发送预览请求，检查修改目标组的参数、格式、业务限制等是否符合要求。</li></ul>
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun

    @property
    def HealthCheckConfig(self):
        r"""<p>健康检查配置。</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        """
        return self._HealthCheckConfig

    @HealthCheckConfig.setter
    def HealthCheckConfig(self, HealthCheckConfig):
        self._HealthCheckConfig = HealthCheckConfig

    @property
    def KeepaliveEnabled(self):
        r"""<p>是否开启长连接。</p>
        :rtype: bool
        """
        return self._KeepaliveEnabled

    @KeepaliveEnabled.setter
    def KeepaliveEnabled(self, KeepaliveEnabled):
        self._KeepaliveEnabled = KeepaliveEnabled

    @property
    def SchedulerAlgorithm(self):
        r"""<p>调度算法。取值：</p><ul><li><strong>wrr</strong>：加权轮询，按照权重选择后端服务器，权重越高的服务器被轮询到的概率越高。</li><li><strong>wlc</strong>：加权最小连接数，当不同后端服务器权重值相同时，当前连接数越小的后端服务器被轮询到的概率越高。</li></ul>
        :rtype: str
        """
        return self._SchedulerAlgorithm

    @SchedulerAlgorithm.setter
    def SchedulerAlgorithm(self, SchedulerAlgorithm):
        self._SchedulerAlgorithm = SchedulerAlgorithm

    @property
    def StickySessionConfig(self):
        r"""<p>会话保持配置。</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        """
        return self._StickySessionConfig

    @StickySessionConfig.setter
    def StickySessionConfig(self, StickySessionConfig):
        self._StickySessionConfig = StickySessionConfig

    @property
    def TargetGroupId(self):
        r"""<p>目标组 ID，格式为 lbtg- 后接 8 位字母数字。</p>
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        r"""<p>目标组名称。长度为 1~255 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。不传目标组名称时默认使用ID作为目标组名称。</p>
        :rtype: str
        """
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName


    def _deserialize(self, params):
        self._DryRun = params.get("DryRun")
        if params.get("HealthCheckConfig") is not None:
            self._HealthCheckConfig = HealthCheckConfig()
            self._HealthCheckConfig._deserialize(params.get("HealthCheckConfig"))
        self._KeepaliveEnabled = params.get("KeepaliveEnabled")
        self._SchedulerAlgorithm = params.get("SchedulerAlgorithm")
        if params.get("StickySessionConfig") is not None:
            self._StickySessionConfig = StickySessionConfig()
            self._StickySessionConfig._deserialize(params.get("StickySessionConfig"))
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetGroupAttributesResponse(AbstractModel):
    r"""ModifyTargetGroupAttributes返回参数结构体

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


class ModifyTargetsInTargetGroupRequest(AbstractModel):
    r"""ModifyTargetsInTargetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupId: str
        :param _Targets: 需要修改的后端服务列表。
        :type Targets: list of TargetToModify
        :param _DryRun: 是否预览此次请求。 
- **false**（默认）：发送普通请求，直接修改后端服务信息。 
- **true**：发送预览请求，检查修改后端服务的参数、格式、业务限制等是否符合要求。
        :type DryRun: bool
        """
        self._TargetGroupId = None
        self._Targets = None
        self._DryRun = None

    @property
    def TargetGroupId(self):
        r"""目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Targets(self):
        r"""需要修改的后端服务列表。
        :rtype: list of TargetToModify
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def DryRun(self):
        r"""是否预览此次请求。 
- **false**（默认）：发送普通请求，直接修改后端服务信息。 
- **true**：发送预览请求，检查修改后端服务的参数、格式、业务限制等是否符合要求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetToModify()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetsInTargetGroupResponse(AbstractModel):
    r"""ModifyTargetsInTargetGroup返回参数结构体

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


class NotifyUnbindTargetRequest(AbstractModel):
    r"""NotifyUnbindTarget请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ips: 后端服务的IP列表。
> **VpcId**（**NumericVpcId**）、**Ips**必须同时设置。
        :type Ips: list of str
        :param _NumericVpcId: 后端服务所属VPC的数字ID。
> **VpcId**（**NumericVpcId**）、**Ips**必须同时设置。
        :type NumericVpcId: int
        """
        self._Ips = None
        self._NumericVpcId = None

    @property
    def Ips(self):
        r"""后端服务的IP列表。
> **VpcId**（**NumericVpcId**）、**Ips**必须同时设置。
        :rtype: list of str
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def NumericVpcId(self):
        r"""后端服务所属VPC的数字ID。
> **VpcId**（**NumericVpcId**）、**Ips**必须同时设置。
        :rtype: int
        """
        return self._NumericVpcId

    @NumericVpcId.setter
    def NumericVpcId(self, NumericVpcId):
        self._NumericVpcId = NumericVpcId


    def _deserialize(self, params):
        self._Ips = params.get("Ips")
        self._NumericVpcId = params.get("NumericVpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotifyUnbindTargetResponse(AbstractModel):
    r"""NotifyUnbindTarget返回参数结构体

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


class PostPayPriceInfo(AbstractModel):
    r"""描述了后付费计费项的价格信息

    """

    def __init__(self):
        r"""
        :param _Discount: 折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
        :type Discount: float
        :param _UnitPrice: 单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPrice: float
        :param _UnitPriceDiscount: 折扣单价，单位:元。
注意：此字段可能返回 null，表示取不到有效值。
        :type UnitPriceDiscount: float
        """
        self._Discount = None
        self._UnitPrice = None
        self._UnitPriceDiscount = None

    @property
    def Discount(self):
        r"""折扣，如20.0代表2折。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Discount

    @Discount.setter
    def Discount(self, Discount):
        self._Discount = Discount

    @property
    def UnitPrice(self):
        r"""单价，单位：元。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._UnitPrice

    @UnitPrice.setter
    def UnitPrice(self, UnitPrice):
        self._UnitPrice = UnitPrice

    @property
    def UnitPriceDiscount(self):
        r"""折扣单价，单位:元。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._UnitPriceDiscount

    @UnitPriceDiscount.setter
    def UnitPriceDiscount(self, UnitPriceDiscount):
        self._UnitPriceDiscount = UnitPriceDiscount


    def _deserialize(self, params):
        self._Discount = params.get("Discount")
        self._UnitPrice = params.get("UnitPrice")
        self._UnitPriceDiscount = params.get("UnitPriceDiscount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Price(AbstractModel):
    r"""表示负载均衡的价格

    """

    def __init__(self):
        r"""
        :param _InstancePrice: 描述了实例价格，单位：元/小时。
        :type InstancePrice: :class:`tencentcloud.alb.v20251030.models.PostPayPriceInfo`
        :param _LcuPrice: 描述了lcu价格，单位：元/个。
        :type LcuPrice: :class:`tencentcloud.alb.v20251030.models.PostPayPriceInfo`
        """
        self._InstancePrice = None
        self._LcuPrice = None

    @property
    def InstancePrice(self):
        r"""描述了实例价格，单位：元/小时。
        :rtype: :class:`tencentcloud.alb.v20251030.models.PostPayPriceInfo`
        """
        return self._InstancePrice

    @InstancePrice.setter
    def InstancePrice(self, InstancePrice):
        self._InstancePrice = InstancePrice

    @property
    def LcuPrice(self):
        r"""描述了lcu价格，单位：元/个。
        :rtype: :class:`tencentcloud.alb.v20251030.models.PostPayPriceInfo`
        """
        return self._LcuPrice

    @LcuPrice.setter
    def LcuPrice(self, LcuPrice):
        self._LcuPrice = LcuPrice


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self._InstancePrice = PostPayPriceInfo()
            self._InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("LcuPrice") is not None:
            self._LcuPrice = PostPayPriceInfo()
            self._LcuPrice._deserialize(params.get("LcuPrice"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaInfo(AbstractModel):
    r"""单个配额项的查询结果。每个结果对应一个配额类型；当请求中传入 ResourceIds 时，每个结果还会对应一个具体资源。

    """

    def __init__(self):
        r"""
        :param _Available: 当前剩余可用量，计算方式为 Limit - Used。仅当请求参数 DisplayFields 包含 available 时返回有效值；未请求时不返回或为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Available: int
        :param _Limit: 配额上限值。不同配额类型的单位不同，通常表示资源个数；超时时间类配额表示秒。
        :type Limit: int
        :param _QuotaType: 配额类型，与请求参数 QuotaTypes 中的取值对应。每种配额类型的含义请参考 QuotaTypes 参数说明。
        :type QuotaType: str
        :param _ResourceId: 资源 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _Used: 当前已使用量。仅当请求参数 DisplayFields 包含 used 时返回有效值；未请求时不返回或为空。
注意：此字段可能返回 null，表示取不到有效值。
        :type Used: int
        """
        self._Available = None
        self._Limit = None
        self._QuotaType = None
        self._ResourceId = None
        self._Used = None

    @property
    def Available(self):
        r"""当前剩余可用量，计算方式为 Limit - Used。仅当请求参数 DisplayFields 包含 available 时返回有效值；未请求时不返回或为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Limit(self):
        r"""配额上限值。不同配额类型的单位不同，通常表示资源个数；超时时间类配额表示秒。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def QuotaType(self):
        r"""配额类型，与请求参数 QuotaTypes 中的取值对应。每种配额类型的含义请参考 QuotaTypes 参数说明。
        :rtype: str
        """
        return self._QuotaType

    @QuotaType.setter
    def QuotaType(self, QuotaType):
        self._QuotaType = QuotaType

    @property
    def ResourceId(self):
        r"""资源 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Used(self):
        r"""当前已使用量。仅当请求参数 DisplayFields 包含 used 时返回有效值；未请求时不返回或为空。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used


    def _deserialize(self, params):
        self._Available = params.get("Available")
        self._Limit = params.get("Limit")
        self._QuotaType = params.get("QuotaType")
        self._ResourceId = params.get("ResourceId")
        self._Used = params.get("Used")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RelatedListener(AbstractModel):
    r"""关联监听器信息

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器 ID，格式为 lst- 后接 8 位字母数字。
        :type ListenerId: str
        :param _ListenerPort: 监听器端口。
        :type ListenerPort: int
        :param _ListenerProtocol: 监听器协议。
        :type ListenerProtocol: str
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        """
        self._ListenerId = None
        self._ListenerPort = None
        self._ListenerProtocol = None
        self._LoadBalancerId = None

    @property
    def ListenerId(self):
        r"""监听器 ID，格式为 lst- 后接 8 位字母数字。
        :rtype: str
        """
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerPort(self):
        r"""监听器端口。
        :rtype: int
        """
        return self._ListenerPort

    @ListenerPort.setter
    def ListenerPort(self, ListenerPort):
        self._ListenerPort = ListenerPort

    @property
    def ListenerProtocol(self):
        r"""监听器协议。
        :rtype: str
        """
        return self._ListenerProtocol

    @ListenerProtocol.setter
    def ListenerProtocol(self, ListenerProtocol):
        self._ListenerProtocol = ListenerProtocol

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerPort = params.get("ListenerPort")
        self._ListenerProtocol = params.get("ListenerProtocol")
        self._LoadBalancerId = params.get("LoadBalancerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveHTTPHeaderInfo(AbstractModel):
    r"""删除HTTP Header信息

    """

    def __init__(self):
        r"""
        :param _Key: 要删除的HTTP Header的键，长度1 ~ 40个字符，支持的字符集为：a-z A-Z 0-9 - _ 。
不支持Cookie,Host,Content-Length,Connection,Upgrade,transfer-encoding,keep-alive,te,authority,x-forwarded-for,x-forwarded-proto,x-forwarded-host,x-forwarded-port,server
        :type Key: str
        """
        self._Key = None

    @property
    def Key(self):
        r"""要删除的HTTP Header的键，长度1 ~ 40个字符，支持的字符集为：a-z A-Z 0-9 - _ 。
不支持Cookie,Host,Content-Length,Connection,Upgrade,transfer-encoding,keep-alive,te,authority,x-forwarded-for,x-forwarded-proto,x-forwarded-host,x-forwarded-port,server
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key


    def _deserialize(self, params):
        self._Key = params.get("Key")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveTargetsFromTargetGroupRequest(AbstractModel):
    r"""RemoveTargetsFromTargetGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupId: str
        :param _Targets: 需要从目标组移除的后端服务列表。单次请求最多移除 **50** 个后端服务。
        :type Targets: list of TargetToRemove
        :param _DryRun: 是否预览此次请求。 
- **false**（默认）：发送普通请求，直接移除后端服务。 
- **true**：发送预览请求，检查移除后端服务的参数、格式、业务限制等是否符合要求。
        :type DryRun: bool
        """
        self._TargetGroupId = None
        self._Targets = None
        self._DryRun = None

    @property
    def TargetGroupId(self):
        r"""目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Targets(self):
        r"""需要从目标组移除的后端服务列表。单次请求最多移除 **50** 个后端服务。
        :rtype: list of TargetToRemove
        """
        return self._Targets

    @Targets.setter
    def Targets(self, Targets):
        self._Targets = Targets

    @property
    def DryRun(self):
        r"""是否预览此次请求。 
- **false**（默认）：发送普通请求，直接移除后端服务。 
- **true**：发送预览请求，检查移除后端服务的参数、格式、业务限制等是否符合要求。
        :rtype: bool
        """
        return self._DryRun

    @DryRun.setter
    def DryRun(self, DryRun):
        self._DryRun = DryRun


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("Targets") is not None:
            self._Targets = []
            for item in params.get("Targets"):
                obj = TargetToRemove()
                obj._deserialize(item)
                self._Targets.append(obj)
        self._DryRun = params.get("DryRun")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveTargetsFromTargetGroupResponse(AbstractModel):
    r"""RemoveTargetsFromTargetGroup返回参数结构体

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


class RuleAction(AbstractModel):
    r"""转发规则动作

    """

    def __init__(self):
        r"""
        :param _Order: 转发动作执行顺序，不能重复，按从小到大顺序执行。取值范围：1 ~ 50000。
        :type Order: int
        :param _Type: 转发动作类型。取值：
TargetGroup：转发至目标组。
Redirect：重定向。
FixedResponse：返回固定内容。
Rewrite：重写。
InsertHeader：写入HTTP Header。
RemoveHeader：删除HTTP Header。
转发动作必选包含TargetGroup,Redirect,FixedResponse其中一个，并且执行顺序放在最后。
        :type Type: str
        :param _FixedResponseConfig: 固定响应内容配置。
        :type FixedResponseConfig: :class:`tencentcloud.alb.v20251030.models.FixedResponseInfo`
        :param _InsertHeaderConfig: 插入HTTP Header配置。
        :type InsertHeaderConfig: :class:`tencentcloud.alb.v20251030.models.InsertHTTPHeaderInfo`
        :param _RedirectConfig: 重定向配置。除HttpCode外，其他配置不能都使用默认值。
        :type RedirectConfig: :class:`tencentcloud.alb.v20251030.models.HTTPRedirectInfo`
        :param _RemoveHeaderConfig: 删除HTTP Header配置。
        :type RemoveHeaderConfig: :class:`tencentcloud.alb.v20251030.models.RemoveHTTPHeaderInfo`
        :param _RewriteConfig: 重写配置。
        :type RewriteConfig: :class:`tencentcloud.alb.v20251030.models.HTTPRewriteInfo`
        :param _TargetGroupConfig: 转发目标组配置。
        :type TargetGroupConfig: :class:`tencentcloud.alb.v20251030.models.TargetGroupConfig`
        """
        self._Order = None
        self._Type = None
        self._FixedResponseConfig = None
        self._InsertHeaderConfig = None
        self._RedirectConfig = None
        self._RemoveHeaderConfig = None
        self._RewriteConfig = None
        self._TargetGroupConfig = None

    @property
    def Order(self):
        r"""转发动作执行顺序，不能重复，按从小到大顺序执行。取值范围：1 ~ 50000。
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Type(self):
        r"""转发动作类型。取值：
TargetGroup：转发至目标组。
Redirect：重定向。
FixedResponse：返回固定内容。
Rewrite：重写。
InsertHeader：写入HTTP Header。
RemoveHeader：删除HTTP Header。
转发动作必选包含TargetGroup,Redirect,FixedResponse其中一个，并且执行顺序放在最后。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def FixedResponseConfig(self):
        r"""固定响应内容配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.FixedResponseInfo`
        """
        return self._FixedResponseConfig

    @FixedResponseConfig.setter
    def FixedResponseConfig(self, FixedResponseConfig):
        self._FixedResponseConfig = FixedResponseConfig

    @property
    def InsertHeaderConfig(self):
        r"""插入HTTP Header配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.InsertHTTPHeaderInfo`
        """
        return self._InsertHeaderConfig

    @InsertHeaderConfig.setter
    def InsertHeaderConfig(self, InsertHeaderConfig):
        self._InsertHeaderConfig = InsertHeaderConfig

    @property
    def RedirectConfig(self):
        r"""重定向配置。除HttpCode外，其他配置不能都使用默认值。
        :rtype: :class:`tencentcloud.alb.v20251030.models.HTTPRedirectInfo`
        """
        return self._RedirectConfig

    @RedirectConfig.setter
    def RedirectConfig(self, RedirectConfig):
        self._RedirectConfig = RedirectConfig

    @property
    def RemoveHeaderConfig(self):
        r"""删除HTTP Header配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.RemoveHTTPHeaderInfo`
        """
        return self._RemoveHeaderConfig

    @RemoveHeaderConfig.setter
    def RemoveHeaderConfig(self, RemoveHeaderConfig):
        self._RemoveHeaderConfig = RemoveHeaderConfig

    @property
    def RewriteConfig(self):
        r"""重写配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.HTTPRewriteInfo`
        """
        return self._RewriteConfig

    @RewriteConfig.setter
    def RewriteConfig(self, RewriteConfig):
        self._RewriteConfig = RewriteConfig

    @property
    def TargetGroupConfig(self):
        r"""转发目标组配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.TargetGroupConfig`
        """
        return self._TargetGroupConfig

    @TargetGroupConfig.setter
    def TargetGroupConfig(self, TargetGroupConfig):
        self._TargetGroupConfig = TargetGroupConfig


    def _deserialize(self, params):
        self._Order = params.get("Order")
        self._Type = params.get("Type")
        if params.get("FixedResponseConfig") is not None:
            self._FixedResponseConfig = FixedResponseInfo()
            self._FixedResponseConfig._deserialize(params.get("FixedResponseConfig"))
        if params.get("InsertHeaderConfig") is not None:
            self._InsertHeaderConfig = InsertHTTPHeaderInfo()
            self._InsertHeaderConfig._deserialize(params.get("InsertHeaderConfig"))
        if params.get("RedirectConfig") is not None:
            self._RedirectConfig = HTTPRedirectInfo()
            self._RedirectConfig._deserialize(params.get("RedirectConfig"))
        if params.get("RemoveHeaderConfig") is not None:
            self._RemoveHeaderConfig = RemoveHTTPHeaderInfo()
            self._RemoveHeaderConfig._deserialize(params.get("RemoveHeaderConfig"))
        if params.get("RewriteConfig") is not None:
            self._RewriteConfig = HTTPRewriteInfo()
            self._RewriteConfig._deserialize(params.get("RewriteConfig"))
        if params.get("TargetGroupConfig") is not None:
            self._TargetGroupConfig = TargetGroupConfig()
            self._TargetGroupConfig._deserialize(params.get("TargetGroupConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCondition(AbstractModel):
    r"""转发规则条件

    """

    def __init__(self):
        r"""
        :param _Type: 转发条件类型。取值：
Host：主机。
Path：路径。
Header：HTTP Header字段。
QueryString：HTPP查询字符串。
Method：请求方法。
Cookie：Cookie。
SourceIp：源 IP。
        :type Type: str
        :param _CookieConfig: Cookie配置。
        :type CookieConfig: list of HTTPCookieInfo
        :param _HeaderConfig: HTTP Header配置。
        :type HeaderConfig: :class:`tencentcloud.alb.v20251030.models.HTTPHeaderInfo`
        :param _HostConfig: 主机名。主机配置在一个规则中只能出现一次，长度3 ~ 128个字符，支持精确匹配，正则匹配，通配匹配。
不能以半角句号（.）、下划线（_）开头或结尾。
精确匹配，支持的字符集为：a-z 0-9 . - _ 。
正则匹配，波浪线（~）开头为正则匹配，支持的字符集为：a-z 0-9 . - ? = ~ _ - + \ ^ * ! $ & | ( ) [ ] 。
通配匹配，星号（*）多字符通配，半角问号（?）单字符通配，支持的字符集为：a-z 0-9 . - _ * ?。
        :type HostConfig: list of str
        :param _MethodConfig: 请求方法。取值：HEAD、GET、POST、OPTIONS、PUT、PATCH、DELETE。
        :type MethodConfig: list of str
        :param _PathConfig: 转发路径。长度1 ~ 128个字符，支持精确匹配，正则匹配，通配匹配。
精确匹配，支持的字符集为：a-z A-Z 0-9 . - _ / =  :。
正则匹配，需以 ~ 开头，~ 开头表示区分大小写， ~* 开头表示不区分大小写，支持的字符集为： a-z A-Z 0-9 . - _ / = ?  ~ ^ * $ : ( ) [ ] + |。
通配匹配，* 表示多字符通配，? 表示单字符通配，支持的字符集为：a-z A-Z 0-9 . - _ / =  :。
        :type PathConfig: list of str
        :param _QueryStringConfig: 查询字符串配置。
        :type QueryStringConfig: list of HTTPQueryStringInfo
        :param _SourceIpConfig: 源IP匹配配置。CIDR格式，IP地址x.x.x.x/32，IP网段x.x.x.x/24。
        :type SourceIpConfig: list of str
        """
        self._Type = None
        self._CookieConfig = None
        self._HeaderConfig = None
        self._HostConfig = None
        self._MethodConfig = None
        self._PathConfig = None
        self._QueryStringConfig = None
        self._SourceIpConfig = None

    @property
    def Type(self):
        r"""转发条件类型。取值：
Host：主机。
Path：路径。
Header：HTTP Header字段。
QueryString：HTPP查询字符串。
Method：请求方法。
Cookie：Cookie。
SourceIp：源 IP。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CookieConfig(self):
        r"""Cookie配置。
        :rtype: list of HTTPCookieInfo
        """
        return self._CookieConfig

    @CookieConfig.setter
    def CookieConfig(self, CookieConfig):
        self._CookieConfig = CookieConfig

    @property
    def HeaderConfig(self):
        r"""HTTP Header配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.HTTPHeaderInfo`
        """
        return self._HeaderConfig

    @HeaderConfig.setter
    def HeaderConfig(self, HeaderConfig):
        self._HeaderConfig = HeaderConfig

    @property
    def HostConfig(self):
        r"""主机名。主机配置在一个规则中只能出现一次，长度3 ~ 128个字符，支持精确匹配，正则匹配，通配匹配。
不能以半角句号（.）、下划线（_）开头或结尾。
精确匹配，支持的字符集为：a-z 0-9 . - _ 。
正则匹配，波浪线（~）开头为正则匹配，支持的字符集为：a-z 0-9 . - ? = ~ _ - + \ ^ * ! $ & | ( ) [ ] 。
通配匹配，星号（*）多字符通配，半角问号（?）单字符通配，支持的字符集为：a-z 0-9 . - _ * ?。
        :rtype: list of str
        """
        return self._HostConfig

    @HostConfig.setter
    def HostConfig(self, HostConfig):
        self._HostConfig = HostConfig

    @property
    def MethodConfig(self):
        r"""请求方法。取值：HEAD、GET、POST、OPTIONS、PUT、PATCH、DELETE。
        :rtype: list of str
        """
        return self._MethodConfig

    @MethodConfig.setter
    def MethodConfig(self, MethodConfig):
        self._MethodConfig = MethodConfig

    @property
    def PathConfig(self):
        r"""转发路径。长度1 ~ 128个字符，支持精确匹配，正则匹配，通配匹配。
精确匹配，支持的字符集为：a-z A-Z 0-9 . - _ / =  :。
正则匹配，需以 ~ 开头，~ 开头表示区分大小写， ~* 开头表示不区分大小写，支持的字符集为： a-z A-Z 0-9 . - _ / = ?  ~ ^ * $ : ( ) [ ] + |。
通配匹配，* 表示多字符通配，? 表示单字符通配，支持的字符集为：a-z A-Z 0-9 . - _ / =  :。
        :rtype: list of str
        """
        return self._PathConfig

    @PathConfig.setter
    def PathConfig(self, PathConfig):
        self._PathConfig = PathConfig

    @property
    def QueryStringConfig(self):
        r"""查询字符串配置。
        :rtype: list of HTTPQueryStringInfo
        """
        return self._QueryStringConfig

    @QueryStringConfig.setter
    def QueryStringConfig(self, QueryStringConfig):
        self._QueryStringConfig = QueryStringConfig

    @property
    def SourceIpConfig(self):
        r"""源IP匹配配置。CIDR格式，IP地址x.x.x.x/32，IP网段x.x.x.x/24。
        :rtype: list of str
        """
        return self._SourceIpConfig

    @SourceIpConfig.setter
    def SourceIpConfig(self, SourceIpConfig):
        self._SourceIpConfig = SourceIpConfig


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("CookieConfig") is not None:
            self._CookieConfig = []
            for item in params.get("CookieConfig"):
                obj = HTTPCookieInfo()
                obj._deserialize(item)
                self._CookieConfig.append(obj)
        if params.get("HeaderConfig") is not None:
            self._HeaderConfig = HTTPHeaderInfo()
            self._HeaderConfig._deserialize(params.get("HeaderConfig"))
        self._HostConfig = params.get("HostConfig")
        self._MethodConfig = params.get("MethodConfig")
        self._PathConfig = params.get("PathConfig")
        if params.get("QueryStringConfig") is not None:
            self._QueryStringConfig = []
            for item in params.get("QueryStringConfig"):
                obj = HTTPQueryStringInfo()
                obj._deserialize(item)
                self._QueryStringConfig.append(obj)
        self._SourceIpConfig = params.get("SourceIpConfig")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHealthStatusInfo(AbstractModel):
    r"""规则健康检查状态

    """

    def __init__(self):
        r"""
        :param _IsDefaultRule: 是否为默认转发规则。
        :type IsDefaultRule: str
        :param _RuleId: 转发规则 ID，格式为 rule- 后接 8 位字母数字。
        :type RuleId: str
        :param _TargetGroupHealthInfos: 目标组健康状态。
        :type TargetGroupHealthInfos: list of TargetGroupHealthInfo
        """
        self._IsDefaultRule = None
        self._RuleId = None
        self._TargetGroupHealthInfos = None

    @property
    def IsDefaultRule(self):
        r"""是否为默认转发规则。
        :rtype: str
        """
        return self._IsDefaultRule

    @IsDefaultRule.setter
    def IsDefaultRule(self, IsDefaultRule):
        self._IsDefaultRule = IsDefaultRule

    @property
    def RuleId(self):
        r"""转发规则 ID，格式为 rule- 后接 8 位字母数字。
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def TargetGroupHealthInfos(self):
        r"""目标组健康状态。
        :rtype: list of TargetGroupHealthInfo
        """
        return self._TargetGroupHealthInfos

    @TargetGroupHealthInfos.setter
    def TargetGroupHealthInfos(self, TargetGroupHealthInfos):
        self._TargetGroupHealthInfos = TargetGroupHealthInfos


    def _deserialize(self, params):
        self._IsDefaultRule = params.get("IsDefaultRule")
        self._RuleId = params.get("RuleId")
        if params.get("TargetGroupHealthInfos") is not None:
            self._TargetGroupHealthInfos = []
            for item in params.get("TargetGroupHealthInfos"):
                obj = TargetGroupHealthInfo()
                obj._deserialize(item)
                self._TargetGroupHealthInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInput(AbstractModel):
    r"""转发规则创建信息

    """

    def __init__(self):
        r"""
        :param _Actions: 转发规则动作列表。
        :type Actions: list of RuleAction
        :param _Conditions: 转发规则条件列表。
        :type Conditions: list of RuleCondition
        :param _Priority: 优先级，值越小优先级越高，不能重复，取值范围：1~10000。
        :type Priority: int
        :param _Direction: 转发规则的方向。Request：客户端到负载均衡的请求方向，Response：后端服务器到负载均衡的响应方向。默认Request。
        :type Direction: str
        :param _RuleName: 转发规则名称。长度为 1~255 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :type RuleName: str
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        """
        self._Actions = None
        self._Conditions = None
        self._Priority = None
        self._Direction = None
        self._RuleName = None
        self._Tags = None

    @property
    def Actions(self):
        r"""转发规则动作列表。
        :rtype: list of RuleAction
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Conditions(self):
        r"""转发规则条件列表。
        :rtype: list of RuleCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Priority(self):
        r"""优先级，值越小优先级越高，不能重复，取值范围：1~10000。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Direction(self):
        r"""转发规则的方向。Request：客户端到负载均衡的请求方向，Response：后端服务器到负载均衡的响应方向。默认Request。
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RuleName(self):
        r"""转发规则名称。长度为 1~255 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Priority = params.get("Priority")
        self._Direction = params.get("Direction")
        self._RuleName = params.get("RuleName")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleModify(AbstractModel):
    r"""转发规则修改信息

    """

    def __init__(self):
        r"""
        :param _Actions: 转发规则动作列表。
        :type Actions: list of RuleAction
        :param _Conditions: 转发规则条件列表。
        :type Conditions: list of RuleCondition
        :param _Priority: 优先级，值越小优先级越高，取值范围：1~10000。
        :type Priority: int
        :param _RuleId: 转发规则 ID，格式为 rule- 后接 8 位字母数字。
        :type RuleId: str
        :param _RuleName: 转发规则名称。
        :type RuleName: str
        """
        self._Actions = None
        self._Conditions = None
        self._Priority = None
        self._RuleId = None
        self._RuleName = None

    @property
    def Actions(self):
        r"""转发规则动作列表。
        :rtype: list of RuleAction
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Conditions(self):
        r"""转发规则条件列表。
        :rtype: list of RuleCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Priority(self):
        r"""优先级，值越小优先级越高，取值范围：1~10000。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RuleId(self):
        r"""转发规则 ID，格式为 rule- 后接 8 位字母数字。
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""转发规则名称。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Priority = params.get("Priority")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleOutput(AbstractModel):
    r"""转发规则信息

    """

    def __init__(self):
        r"""
        :param _Actions: 转发规则动作列表。	
        :type Actions: list of RuleAction
        :param _Conditions: 转发规则条件列表。
        :type Conditions: list of RuleCondition
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _Direction: 转发规则的方向。Request：客户端到负载均衡的请求方向，Response：后端服务器到负载均衡的响应方向。
        :type Direction: str
        :param _ModifyTime: 最后修改时间。
        :type ModifyTime: str
        :param _Priority: 优先级，值越小优先级越高，取值范围：1~10000。
        :type Priority: int
        :param _RuleId: 转发规则 ID，格式为 rule- 后接 8 位字母数字。
        :type RuleId: str
        :param _RuleName: 转发规则名称。
        :type RuleName: str
        :param _Status: 转发规则状态，Provisioning：创建中，Active：运行中，Configuring：配置中。
        :type Status: str
        :param _Tags: 标签列表。
        :type Tags: list of TagInfo
        """
        self._Actions = None
        self._Conditions = None
        self._CreateTime = None
        self._Direction = None
        self._ModifyTime = None
        self._Priority = None
        self._RuleId = None
        self._RuleName = None
        self._Status = None
        self._Tags = None

    @property
    def Actions(self):
        r"""转发规则动作列表。	
        :rtype: list of RuleAction
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Conditions(self):
        r"""转发规则条件列表。
        :rtype: list of RuleCondition
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Direction(self):
        r"""转发规则的方向。Request：客户端到负载均衡的请求方向，Response：后端服务器到负载均衡的响应方向。
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def ModifyTime(self):
        r"""最后修改时间。
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Priority(self):
        r"""优先级，值越小优先级越高，取值范围：1~10000。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def RuleId(self):
        r"""转发规则 ID，格式为 rule- 后接 8 位字母数字。
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        r"""转发规则名称。
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Status(self):
        r"""转发规则状态，Provisioning：创建中，Active：运行中，Configuring：配置中。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        r"""标签列表。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        if params.get("Actions") is not None:
            self._Actions = []
            for item in params.get("Actions"):
                obj = RuleAction()
                obj._deserialize(item)
                self._Actions.append(obj)
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = RuleCondition()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._Direction = params.get("Direction")
        self._ModifyTime = params.get("ModifyTime")
        self._Priority = params.get("Priority")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyCapability(AbstractModel):
    r"""不同TLS版本支持的加密套件信息。

    """

    def __init__(self):
        r"""
        :param _Ciphers: 支持的加密套件列表。
        :type Ciphers: list of str
        :param _TLSVersion: 支持的 TLS 协议版本。可选值包括：TLSv1.0、TLSv1.1、TLSv1.2、TLSv1.3。
        :type TLSVersion: str
        """
        self._Ciphers = None
        self._TLSVersion = None

    @property
    def Ciphers(self):
        r"""支持的加密套件列表。
        :rtype: list of str
        """
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def TLSVersion(self):
        r"""支持的 TLS 协议版本。可选值包括：TLSv1.0、TLSv1.1、TLSv1.2、TLSv1.3。
        :rtype: str
        """
        return self._TLSVersion

    @TLSVersion.setter
    def TLSVersion(self, TLSVersion):
        self._TLSVersion = TLSVersion


    def _deserialize(self, params):
        self._Ciphers = params.get("Ciphers")
        self._TLSVersion = params.get("TLSVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyInfo(AbstractModel):
    r"""安全策略信息。

    """

    def __init__(self):
        r"""
        :param _Ciphers: 支持的加密套件列表。
支持的加密套件，具体依赖 TLSVersions 的取值。
Cipher 只要被任何一个传入的 TLSVersions 支持即可。

说明：若选择了 TLSv1.3，那么 Cipher 列表必须包含 TLSv1.3 支持的 Cipher。

请调用 DescribeSecurityPolicyCapabilities 接口获取支持的加密套件列表。
        :type Ciphers: list of str
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _SecurityPolicyId: 安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :type SecurityPolicyId: str
        :param _SecurityPolicyName: 安全策略名称。长度为2~128个英文或中文字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-）。
        :type SecurityPolicyName: str
        :param _Status: 安全策略状态。当前接口最常返回 Active，表示安全策略处于可用状态。
        :type Status: str
        :param _TLSVersions: 支持的 TLS 协议版本列表。可选值包括：TLSv1.0、TLSv1.1、TLSv1.2、TLSv1.3。
        :type TLSVersions: list of str
        :param _Tags: 标签信息。
        :type Tags: list of TagInfo
        """
        self._Ciphers = None
        self._CreateTime = None
        self._SecurityPolicyId = None
        self._SecurityPolicyName = None
        self._Status = None
        self._TLSVersions = None
        self._Tags = None

    @property
    def Ciphers(self):
        r"""支持的加密套件列表。
支持的加密套件，具体依赖 TLSVersions 的取值。
Cipher 只要被任何一个传入的 TLSVersions 支持即可。

说明：若选择了 TLSv1.3，那么 Cipher 列表必须包含 TLSv1.3 支持的 Cipher。

请调用 DescribeSecurityPolicyCapabilities 接口获取支持的加密套件列表。
        :rtype: list of str
        """
        return self._Ciphers

    @Ciphers.setter
    def Ciphers(self, Ciphers):
        self._Ciphers = Ciphers

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SecurityPolicyId(self):
        r"""安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId

    @property
    def SecurityPolicyName(self):
        r"""安全策略名称。长度为2~128个英文或中文字符，必须以字母或中文开头，可包含数字、半角句号（.）、下划线（_）和短划线（-）。
        :rtype: str
        """
        return self._SecurityPolicyName

    @SecurityPolicyName.setter
    def SecurityPolicyName(self, SecurityPolicyName):
        self._SecurityPolicyName = SecurityPolicyName

    @property
    def Status(self):
        r"""安全策略状态。当前接口最常返回 Active，表示安全策略处于可用状态。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TLSVersions(self):
        r"""支持的 TLS 协议版本列表。可选值包括：TLSv1.0、TLSv1.1、TLSv1.2、TLSv1.3。
        :rtype: list of str
        """
        return self._TLSVersions

    @TLSVersions.setter
    def TLSVersions(self, TLSVersions):
        self._TLSVersions = TLSVersions

    @property
    def Tags(self):
        r"""标签信息。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Ciphers = params.get("Ciphers")
        self._CreateTime = params.get("CreateTime")
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        self._SecurityPolicyName = params.get("SecurityPolicyName")
        self._Status = params.get("Status")
        self._TLSVersions = params.get("TLSVersions")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyRelations(AbstractModel):
    r"""安全策略与监听的关联关系列表。

    """

    def __init__(self):
        r"""
        :param _RelatedListeners: 安全策略与监听的关联关系列表。
        :type RelatedListeners: list of RelatedListener
        :param _SecurityPolicyId: 安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :type SecurityPolicyId: str
        """
        self._RelatedListeners = None
        self._SecurityPolicyId = None

    @property
    def RelatedListeners(self):
        r"""安全策略与监听的关联关系列表。
        :rtype: list of RelatedListener
        """
        return self._RelatedListeners

    @RelatedListeners.setter
    def RelatedListeners(self, RelatedListeners):
        self._RelatedListeners = RelatedListeners

    @property
    def SecurityPolicyId(self):
        r"""安全策略 ID，格式为 tls- 后接 8 位字母数字。
        :rtype: str
        """
        return self._SecurityPolicyId

    @SecurityPolicyId.setter
    def SecurityPolicyId(self, SecurityPolicyId):
        self._SecurityPolicyId = SecurityPolicyId


    def _deserialize(self, params):
        if params.get("RelatedListeners") is not None:
            self._RelatedListeners = []
            for item in params.get("RelatedListeners"):
                obj = RelatedListener()
                obj._deserialize(item)
                self._RelatedListeners.append(obj)
        self._SecurityPolicyId = params.get("SecurityPolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    r"""SetLoadBalancerSecurityGroups请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: 负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :type LoadBalancerId: str
        :param _SecurityGroups: 安全组 ID 列表。
        :type SecurityGroups: list of str
        """
        self._LoadBalancerId = None
        self._SecurityGroups = None

    @property
    def LoadBalancerId(self):
        r"""负载均衡实例 ID，格式为 alb- 后接 8 位字母数字。
        :rtype: str
        """
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def SecurityGroups(self):
        r"""安全组 ID 列表。
        :rtype: list of str
        """
        return self._SecurityGroups

    @SecurityGroups.setter
    def SecurityGroups(self, SecurityGroups):
        self._SecurityGroups = SecurityGroups


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    r"""SetLoadBalancerSecurityGroups返回参数结构体

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


class StickySessionConfig(AbstractModel):
    r"""会话保持配置。

    """

    def __init__(self):
        r"""
        :param _StickySessionEnabled: 是否开启会话保持。
- **true**：开启。
- **false**：不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type StickySessionEnabled: bool
        :param _Cookie: 自定义 Cookie 名称。
长度为 1~255 个字符，只能包含英文字母和数字字符，且不能为`tgw_l7_tg_route`，该字段为目标组间会话保持Cookie保留字段。
>仅当 **StickySessionEnabled** 为 **true** 时该参数生效。
        :type Cookie: str
        :param _CookieTimeout: 会话保持时间。
取值范围：**1-86400**，单位：**秒**。
默认值：**1000**。
>仅当 **StickySessionEnabled** 为 **true**时，该参数生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type CookieTimeout: int
        :param _StickySessionType: 会话保持类型（处理Cookie的方式）。
- **Insert**（默认值）：植入 Cookie。 客户端第一次访问后端服务时，应用型负载均衡会在返回请求中植入 Cookie。下次客户端请求时携带该 Cookie，负载均衡将请求转发到上次请求的相同后端服务。
- **Rewrite**：重写 Cookie。 负载均衡会对用户自定义的 Cookie 进行重写，下次客户端请求时携带该 Cookie，负载均衡将请求转发到上次请求的相同后端服务。
>仅当 **StickySessionEnabled** 为 **true** 时该参数生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type StickySessionType: str
        """
        self._StickySessionEnabled = None
        self._Cookie = None
        self._CookieTimeout = None
        self._StickySessionType = None

    @property
    def StickySessionEnabled(self):
        r"""是否开启会话保持。
- **true**：开启。
- **false**：不开启。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._StickySessionEnabled

    @StickySessionEnabled.setter
    def StickySessionEnabled(self, StickySessionEnabled):
        self._StickySessionEnabled = StickySessionEnabled

    @property
    def Cookie(self):
        r"""自定义 Cookie 名称。
长度为 1~255 个字符，只能包含英文字母和数字字符，且不能为`tgw_l7_tg_route`，该字段为目标组间会话保持Cookie保留字段。
>仅当 **StickySessionEnabled** 为 **true** 时该参数生效。
        :rtype: str
        """
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie

    @property
    def CookieTimeout(self):
        r"""会话保持时间。
取值范围：**1-86400**，单位：**秒**。
默认值：**1000**。
>仅当 **StickySessionEnabled** 为 **true**时，该参数生效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CookieTimeout

    @CookieTimeout.setter
    def CookieTimeout(self, CookieTimeout):
        self._CookieTimeout = CookieTimeout

    @property
    def StickySessionType(self):
        r"""会话保持类型（处理Cookie的方式）。
- **Insert**（默认值）：植入 Cookie。 客户端第一次访问后端服务时，应用型负载均衡会在返回请求中植入 Cookie。下次客户端请求时携带该 Cookie，负载均衡将请求转发到上次请求的相同后端服务。
- **Rewrite**：重写 Cookie。 负载均衡会对用户自定义的 Cookie 进行重写，下次客户端请求时携带该 Cookie，负载均衡将请求转发到上次请求的相同后端服务。
>仅当 **StickySessionEnabled** 为 **true** 时该参数生效。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StickySessionType

    @StickySessionType.setter
    def StickySessionType(self, StickySessionType):
        self._StickySessionType = StickySessionType


    def _deserialize(self, params):
        self._StickySessionEnabled = params.get("StickySessionEnabled")
        self._Cookie = params.get("Cookie")
        self._CookieTimeout = params.get("CookieTimeout")
        self._StickySessionType = params.get("StickySessionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    r"""标签信息

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签的键
        :type TagKey: str
        :param _TagValue: 标签的值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""标签的键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""标签的值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupConfig(AbstractModel):
    r"""目标组配置

    """

    def __init__(self):
        r"""
        :param _TargetGroups: 目标组列表。
        :type TargetGroups: list of TargetGroupTuple
        :param _TargetGroupStickySession: 目标组间会话保持
        :type TargetGroupStickySession: :class:`tencentcloud.alb.v20251030.models.TargetGroupStickySession`
        """
        self._TargetGroups = None
        self._TargetGroupStickySession = None

    @property
    def TargetGroups(self):
        r"""目标组列表。
        :rtype: list of TargetGroupTuple
        """
        return self._TargetGroups

    @TargetGroups.setter
    def TargetGroups(self, TargetGroups):
        self._TargetGroups = TargetGroups

    @property
    def TargetGroupStickySession(self):
        r"""目标组间会话保持
        :rtype: :class:`tencentcloud.alb.v20251030.models.TargetGroupStickySession`
        """
        return self._TargetGroupStickySession

    @TargetGroupStickySession.setter
    def TargetGroupStickySession(self, TargetGroupStickySession):
        self._TargetGroupStickySession = TargetGroupStickySession


    def _deserialize(self, params):
        if params.get("TargetGroups") is not None:
            self._TargetGroups = []
            for item in params.get("TargetGroups"):
                obj = TargetGroupTuple()
                obj._deserialize(item)
                self._TargetGroups.append(obj)
        if params.get("TargetGroupStickySession") is not None:
            self._TargetGroupStickySession = TargetGroupStickySession()
            self._TargetGroupStickySession._deserialize(params.get("TargetGroupStickySession"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupHealthInfo(AbstractModel):
    r"""目标组健康检查状态

    """

    def __init__(self):
        r"""
        :param _HealthCheckEnabled: 是否开启健康检查。
        :type HealthCheckEnabled: bool
        :param _TargetGroupId: 目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupId: str
        :param _TargetHealthStatusInfos: 服务健康检查状态列表。
        :type TargetHealthStatusInfos: list of TargetHealthStatusInfo
        :param _Type: 转发动作类型。取值：
TargetGroup：转发至目标组。
Redirect：重定向。
FixedResponse：返回固定内容。
Rewrite：重写。
InsertHeader：写入HTTP Header。
RemoveHeader：删除HTTP Header。
转发动作必选包含TargetGroup,Redirect,FixedResponse其中一个，并且执行顺序放在最后。
        :type Type: str
        """
        self._HealthCheckEnabled = None
        self._TargetGroupId = None
        self._TargetHealthStatusInfos = None
        self._Type = None

    @property
    def HealthCheckEnabled(self):
        r"""是否开启健康检查。
        :rtype: bool
        """
        return self._HealthCheckEnabled

    @HealthCheckEnabled.setter
    def HealthCheckEnabled(self, HealthCheckEnabled):
        self._HealthCheckEnabled = HealthCheckEnabled

    @property
    def TargetGroupId(self):
        r"""目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetHealthStatusInfos(self):
        r"""服务健康检查状态列表。
        :rtype: list of TargetHealthStatusInfo
        """
        return self._TargetHealthStatusInfos

    @TargetHealthStatusInfos.setter
    def TargetHealthStatusInfos(self, TargetHealthStatusInfos):
        self._TargetHealthStatusInfos = TargetHealthStatusInfos

    @property
    def Type(self):
        r"""转发动作类型。取值：
TargetGroup：转发至目标组。
Redirect：重定向。
FixedResponse：返回固定内容。
Rewrite：重写。
InsertHeader：写入HTTP Header。
RemoveHeader：删除HTTP Header。
转发动作必选包含TargetGroup,Redirect,FixedResponse其中一个，并且执行顺序放在最后。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._HealthCheckEnabled = params.get("HealthCheckEnabled")
        self._TargetGroupId = params.get("TargetGroupId")
        if params.get("TargetHealthStatusInfos") is not None:
            self._TargetHealthStatusInfos = []
            for item in params.get("TargetHealthStatusInfos"):
                obj = TargetHealthStatusInfo()
                obj._deserialize(item)
                self._TargetHealthStatusInfos.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupOutput(AbstractModel):
    r"""目标组简要信息出参

    """

    def __init__(self):
        r"""
        :param _CreateTime: 创建时间。
        :type CreateTime: str
        :param _HealthCheckConfig: 健康检查配置。
        :type HealthCheckConfig: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        :param _KeepaliveEnabled: 是否开启长连接。
        :type KeepaliveEnabled: bool
        :param _Protocol: 后端服务协议类型。取值：
- **HTTP**（默认）：支持绑定HTTP、HTTPS的监听器
- **HTTPS**：支持绑定HTTPS类型的监听器
- **GRPC**：支持绑定HTTPS类型的监听器
- **GRPCS**：支持绑定HTTPS类型的监听器
        :type Protocol: str
        :param _RelatedLoadBalancersCount: 目标组关联的负载均衡数量。
        :type RelatedLoadBalancersCount: int
        :param _SchedulerAlgorithm: 调度算法。
        :type SchedulerAlgorithm: str
        :param _StickySessionConfig: 会话保持配置。
        :type StickySessionConfig: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        :param _Tags: 标签。
        :type Tags: list of TagInfo
        :param _TargetGroupId: 目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupId: str
        :param _TargetGroupName: 目标组名称。默认为目标组ID。长度为 **1-255** 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :type TargetGroupName: str
        :param _TargetGroupStatus: 目标组状态。取值：
- **Provisioning**：创建中。
- **ProvisionFailed**：创建失败。
- **Active**: 运行中。
- **Configuring**：配置变更中。
        :type TargetGroupStatus: str
        :param _TargetType: 目标组类型。取值：
- **Instance**：Cvm服务器类型或Eni弹性网卡类型
        :type TargetType: str
        :param _VpcId: 私有网络 ID。
        :type VpcId: str
        """
        self._CreateTime = None
        self._HealthCheckConfig = None
        self._KeepaliveEnabled = None
        self._Protocol = None
        self._RelatedLoadBalancersCount = None
        self._SchedulerAlgorithm = None
        self._StickySessionConfig = None
        self._Tags = None
        self._TargetGroupId = None
        self._TargetGroupName = None
        self._TargetGroupStatus = None
        self._TargetType = None
        self._VpcId = None

    @property
    def CreateTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def HealthCheckConfig(self):
        r"""健康检查配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.HealthCheckConfig`
        """
        return self._HealthCheckConfig

    @HealthCheckConfig.setter
    def HealthCheckConfig(self, HealthCheckConfig):
        self._HealthCheckConfig = HealthCheckConfig

    @property
    def KeepaliveEnabled(self):
        r"""是否开启长连接。
        :rtype: bool
        """
        return self._KeepaliveEnabled

    @KeepaliveEnabled.setter
    def KeepaliveEnabled(self, KeepaliveEnabled):
        self._KeepaliveEnabled = KeepaliveEnabled

    @property
    def Protocol(self):
        r"""后端服务协议类型。取值：
- **HTTP**（默认）：支持绑定HTTP、HTTPS的监听器
- **HTTPS**：支持绑定HTTPS类型的监听器
- **GRPC**：支持绑定HTTPS类型的监听器
- **GRPCS**：支持绑定HTTPS类型的监听器
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RelatedLoadBalancersCount(self):
        r"""目标组关联的负载均衡数量。
        :rtype: int
        """
        return self._RelatedLoadBalancersCount

    @RelatedLoadBalancersCount.setter
    def RelatedLoadBalancersCount(self, RelatedLoadBalancersCount):
        self._RelatedLoadBalancersCount = RelatedLoadBalancersCount

    @property
    def SchedulerAlgorithm(self):
        r"""调度算法。
        :rtype: str
        """
        return self._SchedulerAlgorithm

    @SchedulerAlgorithm.setter
    def SchedulerAlgorithm(self, SchedulerAlgorithm):
        self._SchedulerAlgorithm = SchedulerAlgorithm

    @property
    def StickySessionConfig(self):
        r"""会话保持配置。
        :rtype: :class:`tencentcloud.alb.v20251030.models.StickySessionConfig`
        """
        return self._StickySessionConfig

    @StickySessionConfig.setter
    def StickySessionConfig(self, StickySessionConfig):
        self._StickySessionConfig = StickySessionConfig

    @property
    def Tags(self):
        r"""标签。
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def TargetGroupId(self):
        r"""目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def TargetGroupName(self):
        r"""目标组名称。默认为目标组ID。长度为 **1-255** 个字符，可包含数字、大小写字母、中文、半角句号（.）、下划线（_）和短划线（-）。
        :rtype: str
        """
        return self._TargetGroupName

    @TargetGroupName.setter
    def TargetGroupName(self, TargetGroupName):
        self._TargetGroupName = TargetGroupName

    @property
    def TargetGroupStatus(self):
        r"""目标组状态。取值：
- **Provisioning**：创建中。
- **ProvisionFailed**：创建失败。
- **Active**: 运行中。
- **Configuring**：配置变更中。
        :rtype: str
        """
        return self._TargetGroupStatus

    @TargetGroupStatus.setter
    def TargetGroupStatus(self, TargetGroupStatus):
        self._TargetGroupStatus = TargetGroupStatus

    @property
    def TargetType(self):
        r"""目标组类型。取值：
- **Instance**：Cvm服务器类型或Eni弹性网卡类型
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def VpcId(self):
        r"""私有网络 ID。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId


    def _deserialize(self, params):
        self._CreateTime = params.get("CreateTime")
        if params.get("HealthCheckConfig") is not None:
            self._HealthCheckConfig = HealthCheckConfig()
            self._HealthCheckConfig._deserialize(params.get("HealthCheckConfig"))
        self._KeepaliveEnabled = params.get("KeepaliveEnabled")
        self._Protocol = params.get("Protocol")
        self._RelatedLoadBalancersCount = params.get("RelatedLoadBalancersCount")
        self._SchedulerAlgorithm = params.get("SchedulerAlgorithm")
        if params.get("StickySessionConfig") is not None:
            self._StickySessionConfig = StickySessionConfig()
            self._StickySessionConfig._deserialize(params.get("StickySessionConfig"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._TargetGroupId = params.get("TargetGroupId")
        self._TargetGroupName = params.get("TargetGroupName")
        self._TargetGroupStatus = params.get("TargetGroupStatus")
        self._TargetType = params.get("TargetType")
        self._VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupStickySession(AbstractModel):
    r"""目标组之间会话保持

    """

    def __init__(self):
        r"""
        :param _Enabled: 是否开启会话保持，默认关闭。
        :type Enabled: bool
        :param _Timeout: 超时时间，单位秒，取值范围：1~86400，默认值：1000。
        :type Timeout: int
        """
        self._Enabled = None
        self._Timeout = None

    @property
    def Enabled(self):
        r"""是否开启会话保持，默认关闭。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def Timeout(self):
        r"""超时时间，单位秒，取值范围：1~86400，默认值：1000。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Enabled = params.get("Enabled")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetGroupTuple(AbstractModel):
    r"""目标组基础配置

    """

    def __init__(self):
        r"""
        :param _TargetGroupId: 目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :type TargetGroupId: str
        :param _Weight: 权重，取值范围：[0, 100]，默认为 10。
        :type Weight: int
        """
        self._TargetGroupId = None
        self._Weight = None

    @property
    def TargetGroupId(self):
        r"""目标组 ID，格式为 lbtg- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetGroupId

    @TargetGroupId.setter
    def TargetGroupId(self, TargetGroupId):
        self._TargetGroupId = TargetGroupId

    @property
    def Weight(self):
        r"""权重，取值范围：[0, 100]，默认为 10。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._TargetGroupId = params.get("TargetGroupId")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHealthStatusInfo(AbstractModel):
    r"""服务健康状态信息

    """

    def __init__(self):
        r"""
        :param _Status: 后端服务健康状态。DescribeListenerHealthStatus 仅返回非健康后端时，该值为 UnHealthy。
        :type Status: str
        :param _TargetId: 后端服务实例 ID，CVM 实例格式为 ins- 后接 8 位字母数字。
        :type TargetId: str
        :param _TargetIp: 后端目标服务IP。
        :type TargetIp: str
        :param _TargetPort: 后端服务器端口。
        :type TargetPort: int
        """
        self._Status = None
        self._TargetId = None
        self._TargetIp = None
        self._TargetPort = None

    @property
    def Status(self):
        r"""后端服务健康状态。DescribeListenerHealthStatus 仅返回非健康后端时，该值为 UnHealthy。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TargetId(self):
        r"""后端服务实例 ID，CVM 实例格式为 ins- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetIp(self):
        r"""后端目标服务IP。
        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def TargetPort(self):
        r"""后端服务器端口。
        :rtype: int
        """
        return self._TargetPort

    @TargetPort.setter
    def TargetPort(self, TargetPort):
        self._TargetPort = TargetPort


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._TargetId = params.get("TargetId")
        self._TargetIp = params.get("TargetIp")
        self._TargetPort = params.get("TargetPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetOutput(AbstractModel):
    r"""后端服务输出参数。

    """

    def __init__(self):
        r"""
        :param _EniId: 弹性网卡 ID。
        :type EniId: str
        :param _Port: 后端服务器使用的端口。取值范围：**1 - 65535**。
        :type Port: int
        :param _TargetId: 后端服务实例 ID，CVM 实例格式为 ins- 后接 8 位字母数字。
        :type TargetId: str
        :param _TargetIp: 后端服务IP。**TargetIp**和**TargetId**需要至少传一个。

- 当服务器组为 **Instance** 类型时，该参数为 **Eni** 的主内网 IP 或辅助内网 IP。

        :type TargetIp: str
        :param _TargetName: 后端服务名称。当前只有CVM后端类型后端服务返回有效名称。
        :type TargetName: str
        :param _TargetStatus: 后端服务的状态。取值：
- **Adding**：添加中。
- **Active**：正常可用状态。
- **Configuring**：配置中。
- **Removing**：移除中。
        :type TargetStatus: str
        :param _TargetType: 后端服务类型。
        :type TargetType: str
        :param _Weight: 后端服务的权重，取值范围：**0 - 100**。默认值为**100**。如果设置权重为**0**，则不会将请求转发给该后端服务。
        :type Weight: int
        """
        self._EniId = None
        self._Port = None
        self._TargetId = None
        self._TargetIp = None
        self._TargetName = None
        self._TargetStatus = None
        self._TargetType = None
        self._Weight = None

    @property
    def EniId(self):
        r"""弹性网卡 ID。
        :rtype: str
        """
        return self._EniId

    @EniId.setter
    def EniId(self, EniId):
        self._EniId = EniId

    @property
    def Port(self):
        r"""后端服务器使用的端口。取值范围：**1 - 65535**。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetId(self):
        r"""后端服务实例 ID，CVM 实例格式为 ins- 后接 8 位字母数字。
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetIp(self):
        r"""后端服务IP。**TargetIp**和**TargetId**需要至少传一个。

- 当服务器组为 **Instance** 类型时，该参数为 **Eni** 的主内网 IP 或辅助内网 IP。

        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def TargetName(self):
        r"""后端服务名称。当前只有CVM后端类型后端服务返回有效名称。
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def TargetStatus(self):
        r"""后端服务的状态。取值：
- **Adding**：添加中。
- **Active**：正常可用状态。
- **Configuring**：配置中。
- **Removing**：移除中。
        :rtype: str
        """
        return self._TargetStatus

    @TargetStatus.setter
    def TargetStatus(self, TargetStatus):
        self._TargetStatus = TargetStatus

    @property
    def TargetType(self):
        r"""后端服务类型。
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Weight(self):
        r"""后端服务的权重，取值范围：**0 - 100**。默认值为**100**。如果设置权重为**0**，则不会将请求转发给该后端服务。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._EniId = params.get("EniId")
        self._Port = params.get("Port")
        self._TargetId = params.get("TargetId")
        self._TargetIp = params.get("TargetIp")
        self._TargetName = params.get("TargetName")
        self._TargetStatus = params.get("TargetStatus")
        self._TargetType = params.get("TargetType")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetToAdd(AbstractModel):
    r"""添加至目标组的后端服务

    """

    def __init__(self):
        r"""
        :param _Port: 后端服务器使用的端口。取值范围：**1 - 65535**。

>当目标组的 **targetType** 取值为 **Instance** 时，该参数必传。
        :type Port: int
        :param _TargetIp: 后端服务IP。**TargetIp**和**TargetId**需要至少传一个。

- 当服务器组为 **Instance** 类型时，该参数为 **Eni** 的主内网 IP 或辅助内网 IP。

        :type TargetIp: str
        :param _Weight: 后端服务的权重，取值范围：**0 - 100**。默认值为**10**。如果设置权重为**0**，则不会将请求转发给该后端服务。
        :type Weight: int
        """
        self._Port = None
        self._TargetIp = None
        self._Weight = None

    @property
    def Port(self):
        r"""后端服务器使用的端口。取值范围：**1 - 65535**。

>当目标组的 **targetType** 取值为 **Instance** 时，该参数必传。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetIp(self):
        r"""后端服务IP。**TargetIp**和**TargetId**需要至少传一个。

- 当服务器组为 **Instance** 类型时，该参数为 **Eni** 的主内网 IP 或辅助内网 IP。

        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def Weight(self):
        r"""后端服务的权重，取值范围：**0 - 100**。默认值为**10**。如果设置权重为**0**，则不会将请求转发给该后端服务。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._TargetIp = params.get("TargetIp")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetToModify(AbstractModel):
    r"""需要修改的后端服务。

    """

    def __init__(self):
        r"""
        :param _TargetIp: 后端服务IP。**TargetIp**和**TargetId**需要至少传一个。

- 当服务器组为 **Instance** 类型时，该参数为 **Eni** 的主内网 IP 或辅助内网 IP。

        :type TargetIp: str
        :param _Port: 后端服务器使用的端口。取值范围：**1 - 65535**。

>当目标组的 **targetType** 取值为 **Instance** 时，该参数必传。
        :type Port: int
        :param _Weight: 后端服务的权重，取值范围：**0 - 100**。如果设置权重为**0**，则不会将请求转发给该后端服务。
        :type Weight: int
        """
        self._TargetIp = None
        self._Port = None
        self._Weight = None

    @property
    def TargetIp(self):
        r"""后端服务IP。**TargetIp**和**TargetId**需要至少传一个。

- 当服务器组为 **Instance** 类型时，该参数为 **Eni** 的主内网 IP 或辅助内网 IP。

        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp

    @property
    def Port(self):
        r"""后端服务器使用的端口。取值范围：**1 - 65535**。

>当目标组的 **targetType** 取值为 **Instance** 时，该参数必传。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Weight(self):
        r"""后端服务的权重，取值范围：**0 - 100**。如果设置权重为**0**，则不会将请求转发给该后端服务。
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight


    def _deserialize(self, params):
        self._TargetIp = params.get("TargetIp")
        self._Port = params.get("Port")
        self._Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetToRemove(AbstractModel):
    r"""从目标组移除的后端服务。

    """

    def __init__(self):
        r"""
        :param _Port: 后端服务器使用的端口。取值范围：**1 - 65535**。

>当目标组的 **targetType** 取值为 **Instance** 时，该参数必传。
        :type Port: int
        :param _TargetIp: 后端服务IP。**TargetIp**和**TargetId**需要至少传一个。

- 当服务器组为 **Instance** 类型时，该参数为 **Eni** 的主内网 IP 或辅助内网 IP。

        :type TargetIp: str
        """
        self._Port = None
        self._TargetIp = None

    @property
    def Port(self):
        r"""后端服务器使用的端口。取值范围：**1 - 65535**。

>当目标组的 **targetType** 取值为 **Instance** 时，该参数必传。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def TargetIp(self):
        r"""后端服务IP。**TargetIp**和**TargetId**需要至少传一个。

- 当服务器组为 **Instance** 类型时，该参数为 **Eni** 的主内网 IP 或辅助内网 IP。

        :rtype: str
        """
        return self._TargetIp

    @TargetIp.setter
    def TargetIp(self, TargetIp):
        self._TargetIp = TargetIp


    def _deserialize(self, params):
        self._Port = params.get("Port")
        self._TargetIp = params.get("TargetIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class XForwardedForConfig(AbstractModel):
    r"""转发配置

    """

    def __init__(self):
        r"""
        :param _XForwardedForAlbIdEnabled: 是否通过 ALB-ID 头字段获取负载均衡实例ID。
- **true**：是。
- **false**：否。
        :type XForwardedForAlbIdEnabled: bool
        :param _XForwardedForClientSrcPortEnabled: 是否通过X-Forwarded-Client-srcport头字段获取访问负载均衡实例客户端的端口。
- **true**：是。
- **false**：否。
        :type XForwardedForClientSrcPortEnabled: bool
        :param _XForwardedForHostEnabled: 是否开启通过X-Forwarded-Host头字段获取访问负载均衡实例客户端的域名。
- **true**：是。
- **false**：否。
        :type XForwardedForHostEnabled: bool
        :param _XForwardedForMode: 指定如何处理 X-Forwarded-For（XFF）HTTP 头字段。
- **append**:  附加模式（默认），将客户端的真实 IP 地址附加到 X-Forwarded-For 头的末尾，保留原有的 XFF 链路信息
- **remove**:  删除模式，移除 X-Forwarded-For 头字段，不将该头传递给后端服务器
- **passthrough**: 透传模式，保持 X-Forwarded-For 头不变，直接透传给后端服务器，不做任何修改

        :type XForwardedForMode: str
        :param _XForwardedForPortEnabled: 是否通过X-Forwarded-Port头字段获取负载均衡实例的监听端口。
- **true**：是。
- **false**：否。
        :type XForwardedForPortEnabled: bool
        :param _XForwardedForProtoEnabled: 是否通过X-Forwarded-Proto头字段获取负载均衡实例的监听协议。
- **true**：是。
- **false**：否。

        :type XForwardedForProtoEnabled: bool
        :param _XTencentClientIDNEnabled: 是否通过 X-Tencent-Client-IDN 头访问 客户端证书的颁发者 $ssl_client_i_dn。
- **true**：是。
- **false**：否。

        :type XTencentClientIDNEnabled: bool
        :param _XTencentClientSDNEnabled: 是否通过 X-Tencent-Client-SDN 头访问客户端证书的主题$ssl_client_s_dn。
- **true**：是。
- **false**：否。

        :type XTencentClientSDNEnabled: bool
        :param _XTencentClientSerialEnabled: 是否通过 X-Tencent-Client-Serial 头访问 客户端证书的序列号 $ssl_client_serial。
- **true**：是。
- **false**：否。

        :type XTencentClientSerialEnabled: bool
        :param _XTencentClientVerifyEnabled: 是通过 X-Tencent-Client-Verify 头访问 客户端证书的验证结果 $ssl_client_verify。
- **true**：是。
- **false**：否。

        :type XTencentClientVerifyEnabled: bool
        """
        self._XForwardedForAlbIdEnabled = None
        self._XForwardedForClientSrcPortEnabled = None
        self._XForwardedForHostEnabled = None
        self._XForwardedForMode = None
        self._XForwardedForPortEnabled = None
        self._XForwardedForProtoEnabled = None
        self._XTencentClientIDNEnabled = None
        self._XTencentClientSDNEnabled = None
        self._XTencentClientSerialEnabled = None
        self._XTencentClientVerifyEnabled = None

    @property
    def XForwardedForAlbIdEnabled(self):
        r"""是否通过 ALB-ID 头字段获取负载均衡实例ID。
- **true**：是。
- **false**：否。
        :rtype: bool
        """
        return self._XForwardedForAlbIdEnabled

    @XForwardedForAlbIdEnabled.setter
    def XForwardedForAlbIdEnabled(self, XForwardedForAlbIdEnabled):
        self._XForwardedForAlbIdEnabled = XForwardedForAlbIdEnabled

    @property
    def XForwardedForClientSrcPortEnabled(self):
        r"""是否通过X-Forwarded-Client-srcport头字段获取访问负载均衡实例客户端的端口。
- **true**：是。
- **false**：否。
        :rtype: bool
        """
        return self._XForwardedForClientSrcPortEnabled

    @XForwardedForClientSrcPortEnabled.setter
    def XForwardedForClientSrcPortEnabled(self, XForwardedForClientSrcPortEnabled):
        self._XForwardedForClientSrcPortEnabled = XForwardedForClientSrcPortEnabled

    @property
    def XForwardedForHostEnabled(self):
        r"""是否开启通过X-Forwarded-Host头字段获取访问负载均衡实例客户端的域名。
- **true**：是。
- **false**：否。
        :rtype: bool
        """
        return self._XForwardedForHostEnabled

    @XForwardedForHostEnabled.setter
    def XForwardedForHostEnabled(self, XForwardedForHostEnabled):
        self._XForwardedForHostEnabled = XForwardedForHostEnabled

    @property
    def XForwardedForMode(self):
        r"""指定如何处理 X-Forwarded-For（XFF）HTTP 头字段。
- **append**:  附加模式（默认），将客户端的真实 IP 地址附加到 X-Forwarded-For 头的末尾，保留原有的 XFF 链路信息
- **remove**:  删除模式，移除 X-Forwarded-For 头字段，不将该头传递给后端服务器
- **passthrough**: 透传模式，保持 X-Forwarded-For 头不变，直接透传给后端服务器，不做任何修改

        :rtype: str
        """
        return self._XForwardedForMode

    @XForwardedForMode.setter
    def XForwardedForMode(self, XForwardedForMode):
        self._XForwardedForMode = XForwardedForMode

    @property
    def XForwardedForPortEnabled(self):
        r"""是否通过X-Forwarded-Port头字段获取负载均衡实例的监听端口。
- **true**：是。
- **false**：否。
        :rtype: bool
        """
        return self._XForwardedForPortEnabled

    @XForwardedForPortEnabled.setter
    def XForwardedForPortEnabled(self, XForwardedForPortEnabled):
        self._XForwardedForPortEnabled = XForwardedForPortEnabled

    @property
    def XForwardedForProtoEnabled(self):
        r"""是否通过X-Forwarded-Proto头字段获取负载均衡实例的监听协议。
- **true**：是。
- **false**：否。

        :rtype: bool
        """
        return self._XForwardedForProtoEnabled

    @XForwardedForProtoEnabled.setter
    def XForwardedForProtoEnabled(self, XForwardedForProtoEnabled):
        self._XForwardedForProtoEnabled = XForwardedForProtoEnabled

    @property
    def XTencentClientIDNEnabled(self):
        r"""是否通过 X-Tencent-Client-IDN 头访问 客户端证书的颁发者 $ssl_client_i_dn。
- **true**：是。
- **false**：否。

        :rtype: bool
        """
        return self._XTencentClientIDNEnabled

    @XTencentClientIDNEnabled.setter
    def XTencentClientIDNEnabled(self, XTencentClientIDNEnabled):
        self._XTencentClientIDNEnabled = XTencentClientIDNEnabled

    @property
    def XTencentClientSDNEnabled(self):
        r"""是否通过 X-Tencent-Client-SDN 头访问客户端证书的主题$ssl_client_s_dn。
- **true**：是。
- **false**：否。

        :rtype: bool
        """
        return self._XTencentClientSDNEnabled

    @XTencentClientSDNEnabled.setter
    def XTencentClientSDNEnabled(self, XTencentClientSDNEnabled):
        self._XTencentClientSDNEnabled = XTencentClientSDNEnabled

    @property
    def XTencentClientSerialEnabled(self):
        r"""是否通过 X-Tencent-Client-Serial 头访问 客户端证书的序列号 $ssl_client_serial。
- **true**：是。
- **false**：否。

        :rtype: bool
        """
        return self._XTencentClientSerialEnabled

    @XTencentClientSerialEnabled.setter
    def XTencentClientSerialEnabled(self, XTencentClientSerialEnabled):
        self._XTencentClientSerialEnabled = XTencentClientSerialEnabled

    @property
    def XTencentClientVerifyEnabled(self):
        r"""是通过 X-Tencent-Client-Verify 头访问 客户端证书的验证结果 $ssl_client_verify。
- **true**：是。
- **false**：否。

        :rtype: bool
        """
        return self._XTencentClientVerifyEnabled

    @XTencentClientVerifyEnabled.setter
    def XTencentClientVerifyEnabled(self, XTencentClientVerifyEnabled):
        self._XTencentClientVerifyEnabled = XTencentClientVerifyEnabled


    def _deserialize(self, params):
        self._XForwardedForAlbIdEnabled = params.get("XForwardedForAlbIdEnabled")
        self._XForwardedForClientSrcPortEnabled = params.get("XForwardedForClientSrcPortEnabled")
        self._XForwardedForHostEnabled = params.get("XForwardedForHostEnabled")
        self._XForwardedForMode = params.get("XForwardedForMode")
        self._XForwardedForPortEnabled = params.get("XForwardedForPortEnabled")
        self._XForwardedForProtoEnabled = params.get("XForwardedForProtoEnabled")
        self._XTencentClientIDNEnabled = params.get("XTencentClientIDNEnabled")
        self._XTencentClientSDNEnabled = params.get("XTencentClientSDNEnabled")
        self._XTencentClientSerialEnabled = params.get("XTencentClientSerialEnabled")
        self._XTencentClientVerifyEnabled = params.get("XTencentClientVerifyEnabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Zone(AbstractModel):
    r"""可用区信息

    """

    def __init__(self):
        r"""
        :param _LocalName: 可用区名称
        :type LocalName: str
        :param _ZoneId: 可用区 ID
        :type ZoneId: str
        :param _ZoneStatus: 可用区状态
        :type ZoneStatus: str
        """
        self._LocalName = None
        self._ZoneId = None
        self._ZoneStatus = None

    @property
    def LocalName(self):
        r"""可用区名称
        :rtype: str
        """
        return self._LocalName

    @LocalName.setter
    def LocalName(self, LocalName):
        self._LocalName = LocalName

    @property
    def ZoneId(self):
        r"""可用区 ID
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneStatus(self):
        r"""可用区状态
        :rtype: str
        """
        return self._ZoneStatus

    @ZoneStatus.setter
    def ZoneStatus(self, ZoneStatus):
        self._ZoneStatus = ZoneStatus


    def _deserialize(self, params):
        self._LocalName = params.get("LocalName")
        self._ZoneId = params.get("ZoneId")
        self._ZoneStatus = params.get("ZoneStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneMappingInfo(AbstractModel):
    r"""可用区及子网映射结构体

    """

    def __init__(self):
        r"""
        :param _SubnetId: <p>子网 ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _ZoneId: <p>可用区ID。最多支持添加10个可用区。若当前地域支持2个及以上的可用区，至少需要添加2个可用区。<br>您可以通过调用<a href="https://cloud.tencent.com/document/api/1822/133727">DescribeZones</a>接口获取可用区ID对应的可用区的信息。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _LoadBalancerAddress: <p>负载均衡 VIP/EIP 信息</p>
        :type LoadBalancerAddress: :class:`tencentcloud.alb.v20251030.models.LoadBalancerAddress`
        :param _Status: <p>可用区状态。取值：</p><ul><li><strong>Active</strong>：运行中。</li><li><strong>Stopped</strong>：已停止。</li><li><strong>Shifted</strong>：已移除。</li><li><strong>Starting</strong>：启动中。</li><li><strong>Stopping</strong>：停止中。</li></ul>
        :type Status: str
        """
        self._SubnetId = None
        self._ZoneId = None
        self._LoadBalancerAddress = None
        self._Status = None

    @property
    def SubnetId(self):
        r"""<p>子网 ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ZoneId(self):
        r"""<p>可用区ID。最多支持添加10个可用区。若当前地域支持2个及以上的可用区，至少需要添加2个可用区。<br>您可以通过调用<a href="https://cloud.tencent.com/document/api/1822/133727">DescribeZones</a>接口获取可用区ID对应的可用区的信息。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def LoadBalancerAddress(self):
        r"""<p>负载均衡 VIP/EIP 信息</p>
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerAddress`
        """
        return self._LoadBalancerAddress

    @LoadBalancerAddress.setter
    def LoadBalancerAddress(self, LoadBalancerAddress):
        self._LoadBalancerAddress = LoadBalancerAddress

    @property
    def Status(self):
        r"""<p>可用区状态。取值：</p><ul><li><strong>Active</strong>：运行中。</li><li><strong>Stopped</strong>：已停止。</li><li><strong>Shifted</strong>：已移除。</li><li><strong>Starting</strong>：启动中。</li><li><strong>Stopping</strong>：停止中。</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._ZoneId = params.get("ZoneId")
        if params.get("LoadBalancerAddress") is not None:
            self._LoadBalancerAddress = LoadBalancerAddress()
            self._LoadBalancerAddress._deserialize(params.get("LoadBalancerAddress"))
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneMappingsItem(AbstractModel):
    r"""用于购买或者修改使用的可用区及子网映射结构体

    """

    def __init__(self):
        r"""
        :param _SubnetId: <p>子网 ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _ZoneId: <p>可用区ID。最多支持添加10个可用区。若当前地域支持2个及以上的可用区，至少需要添加2个可用区。<br>您可以通过调用<a href="https://cloud.tencent.com/document/api/1822/133727">DescribeZones</a>接口获取可用区ID对应的可用区的信息。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _LoadBalancerAddress: <p>公网实例绑定的EIP实例ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LoadBalancerAddress: :class:`tencentcloud.alb.v20251030.models.LoadBalancerAddress`
        """
        self._SubnetId = None
        self._ZoneId = None
        self._LoadBalancerAddress = None

    @property
    def SubnetId(self):
        r"""<p>子网 ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def ZoneId(self):
        r"""<p>可用区ID。最多支持添加10个可用区。若当前地域支持2个及以上的可用区，至少需要添加2个可用区。<br>您可以通过调用<a href="https://cloud.tencent.com/document/api/1822/133727">DescribeZones</a>接口获取可用区ID对应的可用区的信息。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def LoadBalancerAddress(self):
        r"""<p>公网实例绑定的EIP实例ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.alb.v20251030.models.LoadBalancerAddress`
        """
        return self._LoadBalancerAddress

    @LoadBalancerAddress.setter
    def LoadBalancerAddress(self, LoadBalancerAddress):
        self._LoadBalancerAddress = LoadBalancerAddress


    def _deserialize(self, params):
        self._SubnetId = params.get("SubnetId")
        self._ZoneId = params.get("ZoneId")
        if params.get("LoadBalancerAddress") is not None:
            self._LoadBalancerAddress = LoadBalancerAddress()
            self._LoadBalancerAddress._deserialize(params.get("LoadBalancerAddress"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        