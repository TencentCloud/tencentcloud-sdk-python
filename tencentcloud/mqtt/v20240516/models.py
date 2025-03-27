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


class ActivateCaCertificateRequest(AbstractModel):
    """ActivateCaCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _CaSn: CA证书的SN序列号，可以从 [DescribeCaCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :type CaSn: str
        """
        self._InstanceId = None
        self._CaSn = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CaSn(self):
        """CA证书的SN序列号，可以从 [DescribeCaCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CaSn = params.get("CaSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateCaCertificateResponse(AbstractModel):
    """ActivateCaCertificate返回参数结构体

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


class ActivateDeviceCertificateRequest(AbstractModel):
    """ActivateDeviceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _DeviceCertificateSn: 设备证书的SN序列号，可以从 [DescribeDeviceCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :type DeviceCertificateSn: str
        """
        self._InstanceId = None
        self._DeviceCertificateSn = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceCertificateSn(self):
        """设备证书的SN序列号，可以从 [DescribeDeviceCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :rtype: str
        """
        return self._DeviceCertificateSn

    @DeviceCertificateSn.setter
    def DeviceCertificateSn(self, DeviceCertificateSn):
        self._DeviceCertificateSn = DeviceCertificateSn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DeviceCertificateSn = params.get("DeviceCertificateSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ActivateDeviceCertificateResponse(AbstractModel):
    """ActivateDeviceCertificate返回参数结构体

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


class ApplyRegistrationCodeRequest(AbstractModel):
    """ApplyRegistrationCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
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
        


class ApplyRegistrationCodeResponse(AbstractModel):
    """ApplyRegistrationCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _RegistrationCode: 注册码
        :type RegistrationCode: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RegistrationCode = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def RegistrationCode(self):
        """注册码
        :rtype: str
        """
        return self._RegistrationCode

    @RegistrationCode.setter
    def RegistrationCode(self, RegistrationCode):
        self._RegistrationCode = RegistrationCode

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
        self._InstanceId = params.get("InstanceId")
        self._RegistrationCode = params.get("RegistrationCode")
        self._RequestId = params.get("RequestId")


class AuthorizationPolicyItem(AbstractModel):
    """AuthorizationPolicyItem

    """

    def __init__(self):
        r"""
        :param _Id: 策略规则ID
        :type Id: int
        :param _InstanceId: MQTT集群ID
        :type InstanceId: str
        :param _PolicyName: 策略规则名
        :type PolicyName: str
        :param _Version: 规则语法版本，当前仅支持1，默认为1
        :type Version: int
        :param _Priority: 策略优先级，优先级ID越小表示策略越优先检查生效。可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :type Priority: int
        :param _Effect: 决策
allow：允许符合该策略的设备的访问请求。
deny：拒绝覆盖该策略的设备的访问请求。
可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :type Effect: str
        :param _Actions: 操作
connect：连接
pub：发布mqtt消息
sub：订阅mqtt消息
可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :type Actions: str
        :param _Resources: 资源，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :type Resources: str
        :param _ClientId: 条件-连接设备ID，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :type ClientId: str
        :param _Username: 条件-用户名，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :type Username: str
        :param _Ip: 条件-客户端IP地址，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :type Ip: str
        :param _Qos: 条件-服务质量，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :type Qos: str
        :param _Retain: 条件-保留消息，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
1：表示匹配retain消息
2：表示匹配非retain消息
3：表示匹配retain和非retain消息
        :type Retain: int
        :param _Remark: 备注，长度不超过128个字符。
        :type Remark: str
        :param _CreatedTime: 创建时间。毫秒级时间戳 。
        :type CreatedTime: int
        :param _UpdateTime: 更新时间。毫秒级时间戳 。
        :type UpdateTime: int
        """
        self._Id = None
        self._InstanceId = None
        self._PolicyName = None
        self._Version = None
        self._Priority = None
        self._Effect = None
        self._Actions = None
        self._Resources = None
        self._ClientId = None
        self._Username = None
        self._Ip = None
        self._Qos = None
        self._Retain = None
        self._Remark = None
        self._CreatedTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        """策略规则ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        """MQTT集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        """策略规则名
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Version(self):
        """规则语法版本，当前仅支持1，默认为1
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Priority(self):
        """策略优先级，优先级ID越小表示策略越优先检查生效。可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Effect(self):
        """决策
allow：允许符合该策略的设备的访问请求。
deny：拒绝覆盖该策略的设备的访问请求。
可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :rtype: str
        """
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect

    @property
    def Actions(self):
        """操作
connect：连接
pub：发布mqtt消息
sub：订阅mqtt消息
可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :rtype: str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Resources(self):
        """资源，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :rtype: str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def ClientId(self):
        """条件-连接设备ID，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Username(self):
        """条件-用户名，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Ip(self):
        """条件-客户端IP地址，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Qos(self):
        """条件-服务质量，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
        :rtype: str
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Retain(self):
        """条件-保留消息，可参考 [数据面授权策略说明](https://cloud.tencent.com/document/product/1778/109715)。
1：表示匹配retain消息
2：表示匹配非retain消息
3：表示匹配retain和非retain消息
        :rtype: int
        """
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain

    @property
    def Remark(self):
        """备注，长度不超过128个字符。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        """创建时间。毫秒级时间戳 。
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """更新时间。毫秒级时间戳 。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._PolicyName = params.get("PolicyName")
        self._Version = params.get("Version")
        self._Priority = params.get("Priority")
        self._Effect = params.get("Effect")
        self._Actions = params.get("Actions")
        self._Resources = params.get("Resources")
        self._ClientId = params.get("ClientId")
        self._Username = params.get("Username")
        self._Ip = params.get("Ip")
        self._Qos = params.get("Qos")
        self._Retain = params.get("Retain")
        self._Remark = params.get("Remark")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthorizationPolicyPriority(AbstractModel):
    """策略规则优先级

    """

    def __init__(self):
        r"""
        :param _Id: 授权策略规则id，可以从 [DescribeAuthorizationPolicies](https://cloud.tencent.com/document/api/1778/111074)接口获得。
        :type Id: int
        :param _Priority: 优先级
        :type Priority: int
        """
        self._Id = None
        self._Priority = None

    @property
    def Id(self):
        """授权策略规则id，可以从 [DescribeAuthorizationPolicies](https://cloud.tencent.com/document/api/1778/111074)接口获得。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Priority(self):
        """优先级
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BodyItem(AbstractModel):
    """HTTP 认证器body

    """

    def __init__(self):
        r"""
        :param _Key: body key
        :type Key: str
        :param _Value: body key
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """body key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """body key
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
        


class CaCertificateItem(AbstractModel):
    """CA证书信息

    """

    def __init__(self):
        r"""
        :param _CaCn: 证书的公用名(Common Name)
        :type CaCn: str
        :param _CaCertificate: 证书内容
        :type CaCertificate: str
        :param _CaSn: 证书序列号
        :type CaSn: str
        :param _Format: 证书格式，当前仅支持 PEM 格式
        :type Format: str
        :param _VerificationCertificate: 验证证书内容
        :type VerificationCertificate: str
        :param _Status: CA证书的状态
    ACTIVE：激活
    INACTIVE：未激活
    REVOKED：吊销
    PENDING_ACTIVATION：注册待激活
        :type Status: str
        :param _LastActivationTime: 上次激活时间，毫秒级时间戳 。
        :type LastActivationTime: int
        :param _CreatedTime: 创建时间，毫秒级时间戳 。
        :type CreatedTime: int
        :param _UpdateTime: 更新时间，毫秒级时间戳 。
        :type UpdateTime: int
        :param _LastInactivationTime: 上次去激活时间，毫秒级时间戳 。
        :type LastInactivationTime: int
        :param _CaIssuerCn: Ca证书颁发者CN
        :type CaIssuerCn: str
        :param _NotBeforeTime: 生效时间，毫秒级时间戳 。
        :type NotBeforeTime: int
        :param _NotAfterTime: 失效时间，毫秒级时间戳 。
        :type NotAfterTime: int
        """
        self._CaCn = None
        self._CaCertificate = None
        self._CaSn = None
        self._Format = None
        self._VerificationCertificate = None
        self._Status = None
        self._LastActivationTime = None
        self._CreatedTime = None
        self._UpdateTime = None
        self._LastInactivationTime = None
        self._CaIssuerCn = None
        self._NotBeforeTime = None
        self._NotAfterTime = None

    @property
    def CaCn(self):
        """证书的公用名(Common Name)
        :rtype: str
        """
        return self._CaCn

    @CaCn.setter
    def CaCn(self, CaCn):
        self._CaCn = CaCn

    @property
    def CaCertificate(self):
        """证书内容
        :rtype: str
        """
        return self._CaCertificate

    @CaCertificate.setter
    def CaCertificate(self, CaCertificate):
        self._CaCertificate = CaCertificate

    @property
    def CaSn(self):
        """证书序列号
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def Format(self):
        """证书格式，当前仅支持 PEM 格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def VerificationCertificate(self):
        """验证证书内容
        :rtype: str
        """
        return self._VerificationCertificate

    @VerificationCertificate.setter
    def VerificationCertificate(self, VerificationCertificate):
        self._VerificationCertificate = VerificationCertificate

    @property
    def Status(self):
        """CA证书的状态
    ACTIVE：激活
    INACTIVE：未激活
    REVOKED：吊销
    PENDING_ACTIVATION：注册待激活
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LastActivationTime(self):
        """上次激活时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._LastActivationTime

    @LastActivationTime.setter
    def LastActivationTime(self, LastActivationTime):
        self._LastActivationTime = LastActivationTime

    @property
    def CreatedTime(self):
        """创建时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """更新时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LastInactivationTime(self):
        """上次去激活时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._LastInactivationTime

    @LastInactivationTime.setter
    def LastInactivationTime(self, LastInactivationTime):
        self._LastInactivationTime = LastInactivationTime

    @property
    def CaIssuerCn(self):
        """Ca证书颁发者CN
        :rtype: str
        """
        return self._CaIssuerCn

    @CaIssuerCn.setter
    def CaIssuerCn(self, CaIssuerCn):
        self._CaIssuerCn = CaIssuerCn

    @property
    def NotBeforeTime(self):
        """生效时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._NotBeforeTime

    @NotBeforeTime.setter
    def NotBeforeTime(self, NotBeforeTime):
        self._NotBeforeTime = NotBeforeTime

    @property
    def NotAfterTime(self):
        """失效时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._NotAfterTime

    @NotAfterTime.setter
    def NotAfterTime(self, NotAfterTime):
        self._NotAfterTime = NotAfterTime


    def _deserialize(self, params):
        self._CaCn = params.get("CaCn")
        self._CaCertificate = params.get("CaCertificate")
        self._CaSn = params.get("CaSn")
        self._Format = params.get("Format")
        self._VerificationCertificate = params.get("VerificationCertificate")
        self._Status = params.get("Status")
        self._LastActivationTime = params.get("LastActivationTime")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdateTime = params.get("UpdateTime")
        self._LastInactivationTime = params.get("LastInactivationTime")
        self._CaIssuerCn = params.get("CaIssuerCn")
        self._NotBeforeTime = params.get("NotBeforeTime")
        self._NotAfterTime = params.get("NotAfterTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuthorizationPolicyRequest(AbstractModel):
    """CreateAuthorizationPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _PolicyName: 策略名称，不能为空，3-64个字符，支持中文、字母、数字、“-”及“_”。
        :type PolicyName: str
        :param _PolicyVersion: 策略版本,默认为1，当前仅支持1
        :type PolicyVersion: int
        :param _Priority: 策略优先级，越小越优先，不能重复
        :type Priority: int
        :param _Effect: 决策：
allow 允许
deny 拒绝
        :type Effect: str
        :param _Actions: 操作
connect：连接
pub：发布
sub：订阅
        :type Actions: str
        :param _Retain: 条件-保留消息
1,匹配保留消息；
2,匹配非保留消息，
3.匹配保留和非保留消息
        :type Retain: int
        :param _Qos: 条件：服务质量
0：最多一次
1：最少一次
2：精确一次
        :type Qos: str
        :param _Resources: 资源，需要匹配的订阅
        :type Resources: str
        :param _Username: 条件-用户名
        :type Username: str
        :param _ClientId: 条件：客户端ID，支持正则
        :type ClientId: str
        :param _Ip: 条件：客户端IP地址，支持IP或者CIDR
        :type Ip: str
        :param _Remark: 备注信息，最长 128 字符
        :type Remark: str
        """
        self._InstanceId = None
        self._PolicyName = None
        self._PolicyVersion = None
        self._Priority = None
        self._Effect = None
        self._Actions = None
        self._Retain = None
        self._Qos = None
        self._Resources = None
        self._Username = None
        self._ClientId = None
        self._Ip = None
        self._Remark = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        """策略名称，不能为空，3-64个字符，支持中文、字母、数字、“-”及“_”。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyVersion(self):
        """策略版本,默认为1，当前仅支持1
        :rtype: int
        """
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion

    @property
    def Priority(self):
        """策略优先级，越小越优先，不能重复
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Effect(self):
        """决策：
allow 允许
deny 拒绝
        :rtype: str
        """
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect

    @property
    def Actions(self):
        """操作
connect：连接
pub：发布
sub：订阅
        :rtype: str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Retain(self):
        """条件-保留消息
1,匹配保留消息；
2,匹配非保留消息，
3.匹配保留和非保留消息
        :rtype: int
        """
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain

    @property
    def Qos(self):
        """条件：服务质量
0：最多一次
1：最少一次
2：精确一次
        :rtype: str
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Resources(self):
        """资源，需要匹配的订阅
        :rtype: str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Username(self):
        """条件-用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def ClientId(self):
        """条件：客户端ID，支持正则
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Ip(self):
        """条件：客户端IP地址，支持IP或者CIDR
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Remark(self):
        """备注信息，最长 128 字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyName = params.get("PolicyName")
        self._PolicyVersion = params.get("PolicyVersion")
        self._Priority = params.get("Priority")
        self._Effect = params.get("Effect")
        self._Actions = params.get("Actions")
        self._Retain = params.get("Retain")
        self._Qos = params.get("Qos")
        self._Resources = params.get("Resources")
        self._Username = params.get("Username")
        self._ClientId = params.get("ClientId")
        self._Ip = params.get("Ip")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAuthorizationPolicyResponse(AbstractModel):
    """CreateAuthorizationPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群Id
        :type InstanceId: str
        :param _Id: 策略id
        :type Id: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Id = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """集群Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Id(self):
        """策略id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
        self._InstanceId = params.get("InstanceId")
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class CreateHttpAuthenticatorRequest(AbstractModel):
    """CreateHttpAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Endpoint: jwks端点
        :type Endpoint: str
        :param _Concurrency: 最大并发连接数，默认8，范围：1-20
        :type Concurrency: int
        :param _Method: 网络请求方法 Get 或 Post，默认post
        :type Method: str
        :param _Status: 认证器是否开启：open-启用；close-关闭
        :type Status: str
        :param _Remark: 说明
        :type Remark: str
        :param _ConnectTimeout: 连接超时时间，单位：秒，范围：1-30
        :type ConnectTimeout: int
        :param _ReadTimeout: 请求超时时间，单位：秒，范围：1-30
        :type ReadTimeout: int
        :param _Header: 转发请求header
        :type Header: list of HeaderItem
        :param _Body: 转发请求body
        :type Body: list of BodyItem
        """
        self._InstanceId = None
        self._Endpoint = None
        self._Concurrency = None
        self._Method = None
        self._Status = None
        self._Remark = None
        self._ConnectTimeout = None
        self._ReadTimeout = None
        self._Header = None
        self._Body = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Endpoint(self):
        """jwks端点
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def Concurrency(self):
        """最大并发连接数，默认8，范围：1-20
        :rtype: int
        """
        return self._Concurrency

    @Concurrency.setter
    def Concurrency(self, Concurrency):
        self._Concurrency = Concurrency

    @property
    def Method(self):
        """网络请求方法 Get 或 Post，默认post
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Status(self):
        """认证器是否开启：open-启用；close-关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        """说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def ConnectTimeout(self):
        """连接超时时间，单位：秒，范围：1-30
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def ReadTimeout(self):
        """请求超时时间，单位：秒，范围：1-30
        :rtype: int
        """
        return self._ReadTimeout

    @ReadTimeout.setter
    def ReadTimeout(self, ReadTimeout):
        self._ReadTimeout = ReadTimeout

    @property
    def Header(self):
        """转发请求header
        :rtype: list of HeaderItem
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Body(self):
        """转发请求body
        :rtype: list of BodyItem
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Endpoint = params.get("Endpoint")
        self._Concurrency = params.get("Concurrency")
        self._Method = params.get("Method")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._ReadTimeout = params.get("ReadTimeout")
        if params.get("Header") is not None:
            self._Header = []
            for item in params.get("Header"):
                obj = HeaderItem()
                obj._deserialize(item)
                self._Header.append(obj)
        if params.get("Body") is not None:
            self._Body = []
            for item in params.get("Body"):
                obj = BodyItem()
                obj._deserialize(item)
                self._Body.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHttpAuthenticatorResponse(AbstractModel):
    """CreateHttpAuthenticator返回参数结构体

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


class CreateInsPublicEndpointRequest(AbstractModel):
    """CreateInsPublicEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Bandwidth: 带宽,单位Mbps
        :type Bandwidth: int
        :param _Rules: 公网访问规则
        :type Rules: list of PublicAccessRule
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._Rules = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        """带宽,单位Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Rules(self):
        """公网访问规则
        :rtype: list of PublicAccessRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInsPublicEndpointResponse(AbstractModel):
    """CreateInsPublicEndpoint返回参数结构体

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


class CreateInstanceRequest(AbstractModel):
    """CreateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型，
BASIC 基础版
PRO  专业版
        :type InstanceType: str
        :param _Name: 实例名称
        :type Name: str
        :param _SkuCode: 商品规格，可用规格可通过接口DescribeProductSKUList查询
        :type SkuCode: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _TagList: 标签列表
        :type TagList: list of Tag
        :param _VpcList: 实例绑定的VPC信息
        :type VpcList: list of VpcInfo
        :param _EnablePublic: 是否开启公网
        :type EnablePublic: bool
        :param _Bandwidth: 公网带宽（单位：兆）
        :type Bandwidth: int
        :param _IpRules: 公网访问白名单
        :type IpRules: list of IpRule
        :param _RenewFlag: 是否自动续费（0: 不自动续费；1: 自动续费）
        :type RenewFlag: int
        :param _TimeSpan: 购买时长（单位：月）
        :type TimeSpan: int
        :param _PayMode: 付费模式（0: 后付费；1: 预付费）
        :type PayMode: int
        """
        self._InstanceType = None
        self._Name = None
        self._SkuCode = None
        self._Remark = None
        self._TagList = None
        self._VpcList = None
        self._EnablePublic = None
        self._Bandwidth = None
        self._IpRules = None
        self._RenewFlag = None
        self._TimeSpan = None
        self._PayMode = None

    @property
    def InstanceType(self):
        """实例类型，
BASIC 基础版
PRO  专业版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def Name(self):
        """实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SkuCode(self):
        """商品规格，可用规格可通过接口DescribeProductSKUList查询
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TagList(self):
        """标签列表
        :rtype: list of Tag
        """
        return self._TagList

    @TagList.setter
    def TagList(self, TagList):
        self._TagList = TagList

    @property
    def VpcList(self):
        """实例绑定的VPC信息
        :rtype: list of VpcInfo
        """
        return self._VpcList

    @VpcList.setter
    def VpcList(self, VpcList):
        self._VpcList = VpcList

    @property
    def EnablePublic(self):
        """是否开启公网
        :rtype: bool
        """
        return self._EnablePublic

    @EnablePublic.setter
    def EnablePublic(self, EnablePublic):
        self._EnablePublic = EnablePublic

    @property
    def Bandwidth(self):
        """公网带宽（单位：兆）
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def IpRules(self):
        """公网访问白名单
        :rtype: list of IpRule
        """
        return self._IpRules

    @IpRules.setter
    def IpRules(self, IpRules):
        self._IpRules = IpRules

    @property
    def RenewFlag(self):
        """是否自动续费（0: 不自动续费；1: 自动续费）
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def TimeSpan(self):
        """购买时长（单位：月）
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def PayMode(self):
        """付费模式（0: 后付费；1: 预付费）
        :rtype: int
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._Name = params.get("Name")
        self._SkuCode = params.get("SkuCode")
        self._Remark = params.get("Remark")
        if params.get("TagList") is not None:
            self._TagList = []
            for item in params.get("TagList"):
                obj = Tag()
                obj._deserialize(item)
                self._TagList.append(obj)
        if params.get("VpcList") is not None:
            self._VpcList = []
            for item in params.get("VpcList"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcList.append(obj)
        self._EnablePublic = params.get("EnablePublic")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("IpRules") is not None:
            self._IpRules = []
            for item in params.get("IpRules"):
                obj = IpRule()
                obj._deserialize(item)
                self._IpRules.append(obj)
        self._RenewFlag = params.get("RenewFlag")
        self._TimeSpan = params.get("TimeSpan")
        self._PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInstanceResponse(AbstractModel):
    """CreateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        self._InstanceId = params.get("InstanceId")
        self._RequestId = params.get("RequestId")


class CreateJWKSAuthenticatorRequest(AbstractModel):
    """CreateJWKSAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Endpoint: jwks端点
        :type Endpoint: str
        :param _RefreshInterval: jwks刷新间隔,单位：秒
        :type RefreshInterval: int
        :param _Text: jwks文本
        :type Text: str
        :param _Status: 认证器是否开启：open-启用；close-关闭
        :type Status: str
        :param _Remark: 说明
        :type Remark: str
        :param _From: 设备连接时传递jwt的key；
username-使用用户名字段传递；
password-使用密码字段传递
        :type From: str
        """
        self._InstanceId = None
        self._Endpoint = None
        self._RefreshInterval = None
        self._Text = None
        self._Status = None
        self._Remark = None
        self._From = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Endpoint(self):
        """jwks端点
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def RefreshInterval(self):
        """jwks刷新间隔,单位：秒
        :rtype: int
        """
        return self._RefreshInterval

    @RefreshInterval.setter
    def RefreshInterval(self, RefreshInterval):
        self._RefreshInterval = RefreshInterval

    @property
    def Text(self):
        """jwks文本
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Status(self):
        """认证器是否开启：open-启用；close-关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        """说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def From(self):
        """设备连接时传递jwt的key；
username-使用用户名字段传递；
password-使用密码字段传递
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Endpoint = params.get("Endpoint")
        self._RefreshInterval = params.get("RefreshInterval")
        self._Text = params.get("Text")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJWKSAuthenticatorResponse(AbstractModel):
    """CreateJWKSAuthenticator返回参数结构体

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


class CreateJWTAuthenticatorRequest(AbstractModel):
    """CreateJWTAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Algorithm: 算法：hmac-based，public-key
        :type Algorithm: str
        :param _From: 设备连接时传递jwt的key；username-使用用户名字段传递；password-使用密码字段传递
        :type From: str
        :param _Secret: 密码
        :type Secret: str
        :param _PublicKey: 公钥
        :type PublicKey: str
        :param _Status: 认证器是否开启：open-启用；close-关闭
        :type Status: str
        :param _Remark: 说明
        :type Remark: str
        """
        self._InstanceId = None
        self._Algorithm = None
        self._From = None
        self._Secret = None
        self._PublicKey = None
        self._Status = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Algorithm(self):
        """算法：hmac-based，public-key
        :rtype: str
        """
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def From(self):
        """设备连接时传递jwt的key；username-使用用户名字段传递；password-使用密码字段传递
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Secret(self):
        """密码
        :rtype: str
        """
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret

    @property
    def PublicKey(self):
        """公钥
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Status(self):
        """认证器是否开启：open-启用；close-关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        """说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Algorithm = params.get("Algorithm")
        self._From = params.get("From")
        self._Secret = params.get("Secret")
        self._PublicKey = params.get("PublicKey")
        self._Status = params.get("Status")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateJWTAuthenticatorResponse(AbstractModel):
    """CreateJWTAuthenticator返回参数结构体

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


class CreateTopicRequest(AbstractModel):
    """CreateTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题，不能为空，只能包含字母、数字、“-”及“_”，3-100 字符。
        :type Topic: str
        :param _Remark: 备注，最长 128 字符
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._Remark = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题，不能为空，只能包含字母、数字、“-”及“_”，3-100 字符。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        """备注，最长 128 字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTopicResponse(AbstractModel):
    """CreateTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Topic = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

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
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._RequestId = params.get("RequestId")


class CreateUserRequest(AbstractModel):
    """CreateUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Username: 用户名，不能为空，只支持数字 大小写字母 分隔符("_","-")，不能超过 32 个字符
        :type Username: str
        :param _Password: 密码，该字段为空时候则后端会默认生成。用户自定义密码时，不能为空，只支持数字 大小写字母 分隔符("_","-")，不能超过 64 个字符。
        :type Password: str
        :param _Remark: 备注，长度不超过128个字符。
        :type Remark: str
        """
        self._InstanceId = None
        self._Username = None
        self._Password = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Username(self):
        """用户名，不能为空，只支持数字 大小写字母 分隔符("_","-")，不能超过 32 个字符
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """密码，该字段为空时候则后端会默认生成。用户自定义密码时，不能为空，只支持数字 大小写字母 分隔符("_","-")，不能超过 64 个字符。
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Remark(self):
        """备注，长度不超过128个字符。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUserResponse(AbstractModel):
    """CreateUser返回参数结构体

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


class DeactivateCaCertificateRequest(AbstractModel):
    """DeactivateCaCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _CaSn: 证书序列号，可以从 [DescribeCaCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :type CaSn: str
        """
        self._InstanceId = None
        self._CaSn = None

    @property
    def InstanceId(self):
        """实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CaSn(self):
        """证书序列号，可以从 [DescribeCaCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CaSn = params.get("CaSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeactivateCaCertificateResponse(AbstractModel):
    """DeactivateCaCertificate返回参数结构体

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


class DeactivateDeviceCertificateRequest(AbstractModel):
    """DeactivateDeviceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _DeviceCertificateSn: 设备证书的SN序列号，可以从 [DescribeDeviceCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、设备证书文件中获得。
        :type DeviceCertificateSn: str
        """
        self._InstanceId = None
        self._DeviceCertificateSn = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceCertificateSn(self):
        """设备证书的SN序列号，可以从 [DescribeDeviceCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、设备证书文件中获得。
        :rtype: str
        """
        return self._DeviceCertificateSn

    @DeviceCertificateSn.setter
    def DeviceCertificateSn(self, DeviceCertificateSn):
        self._DeviceCertificateSn = DeviceCertificateSn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DeviceCertificateSn = params.get("DeviceCertificateSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeactivateDeviceCertificateResponse(AbstractModel):
    """DeactivateDeviceCertificate返回参数结构体

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


class DeleteAuthenticatorRequest(AbstractModel):
    """DeleteAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Type: 认证器类型:
JWT：JWT认证器
JWKS：JWKS认证器
HTTP：HTTP认证器
        :type Type: str
        """
        self._InstanceId = None
        self._Type = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """认证器类型:
JWT：JWT认证器
JWKS：JWKS认证器
HTTP：HTTP认证器
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuthenticatorResponse(AbstractModel):
    """DeleteAuthenticator返回参数结构体

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


class DeleteAuthorizationPolicyRequest(AbstractModel):
    """DeleteAuthorizationPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Id: 授权策略规则id，可以从 [DescribeAuthorizationPolicies](https://cloud.tencent.com/document/api/1778/111074)接口获得。
        :type Id: int
        """
        self._InstanceId = None
        self._Id = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Id(self):
        """授权策略规则id，可以从 [DescribeAuthorizationPolicies](https://cloud.tencent.com/document/api/1778/111074)接口获得。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAuthorizationPolicyResponse(AbstractModel):
    """DeleteAuthorizationPolicy返回参数结构体

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


class DeleteCaCertificateRequest(AbstractModel):
    """DeleteCaCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _CaSn: CA证书序列号，可以从 [DescribeCaCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :type CaSn: str
        """
        self._InstanceId = None
        self._CaSn = None

    @property
    def InstanceId(self):
        """实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CaSn(self):
        """CA证书序列号，可以从 [DescribeCaCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CaSn = params.get("CaSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCaCertificateResponse(AbstractModel):
    """DeleteCaCertificate返回参数结构体

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


class DeleteDeviceCertificateRequest(AbstractModel):
    """DeleteDeviceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _DeviceCertificateSn: 设备证书序列号
        :type DeviceCertificateSn: str
        """
        self._InstanceId = None
        self._DeviceCertificateSn = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceCertificateSn(self):
        """设备证书序列号
        :rtype: str
        """
        return self._DeviceCertificateSn

    @DeviceCertificateSn.setter
    def DeviceCertificateSn(self, DeviceCertificateSn):
        self._DeviceCertificateSn = DeviceCertificateSn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DeviceCertificateSn = params.get("DeviceCertificateSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeviceCertificateResponse(AbstractModel):
    """DeleteDeviceCertificate返回参数结构体

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


class DeleteInsPublicEndpointRequest(AbstractModel):
    """DeleteInsPublicEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
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
        


class DeleteInsPublicEndpointResponse(AbstractModel):
    """DeleteInsPublicEndpoint返回参数结构体

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


class DeleteInstanceRequest(AbstractModel):
    """DeleteInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
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
        


class DeleteInstanceResponse(AbstractModel):
    """DeleteInstance返回参数结构体

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


class DeleteTopicRequest(AbstractModel):
    """DeleteTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTopicResponse(AbstractModel):
    """DeleteTopic返回参数结构体

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


class DeleteUserRequest(AbstractModel):
    """DeleteUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Username: 用户名
        :type Username: str
        """
        self._InstanceId = None
        self._Username = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Username(self):
        """用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Username = params.get("Username")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteUserResponse(AbstractModel):
    """DeleteUser返回参数结构体

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


class DescribeAuthenticatorRequest(AbstractModel):
    """DescribeAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Type: 认证器类型:
JWT：JWT认证器
JWKS：JWKS认证器
HTTP：HTTP认证器
        :type Type: str
        """
        self._InstanceId = None
        self._Type = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
        """认证器类型:
JWT：JWT认证器
JWKS：JWKS认证器
HTTP：HTTP认证器
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuthenticatorResponse(AbstractModel):
    """DescribeAuthenticator返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Authenticators: 集群认证器列表
        :type Authenticators: list of MQTTAuthenticatorItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Authenticators = None
        self._RequestId = None

    @property
    def Authenticators(self):
        """集群认证器列表
        :rtype: list of MQTTAuthenticatorItem
        """
        return self._Authenticators

    @Authenticators.setter
    def Authenticators(self, Authenticators):
        self._Authenticators = Authenticators

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
        if params.get("Authenticators") is not None:
            self._Authenticators = []
            for item in params.get("Authenticators"):
                obj = MQTTAuthenticatorItem()
                obj._deserialize(item)
                self._Authenticators.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuthorizationPoliciesRequest(AbstractModel):
    """DescribeAuthorizationPolicies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
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
        


class DescribeAuthorizationPoliciesResponse(AbstractModel):
    """DescribeAuthorizationPolicies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 规则
        :type Data: list of AuthorizationPolicyItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """规则
        :rtype: list of AuthorizationPolicyItem
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
            self._Data = []
            for item in params.get("Data"):
                obj = AuthorizationPolicyItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCaCertificateRequest(AbstractModel):
    """DescribeCaCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CaSn: CA证书的SN序列号，可以从 [DescribeCaCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :type CaSn: str
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._CaSn = None
        self._InstanceId = None

    @property
    def CaSn(self):
        """CA证书的SN序列号，可以从 [DescribeCaCertificates](https://cloud.tencent.com/document/api/1778/116206)接口、控制台、证书文件中获得。
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._CaSn = params.get("CaSn")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCaCertificateResponse(AbstractModel):
    """DescribeCaCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CreatedTime: 创建时间，毫秒级时间戳 。
        :type CreatedTime: int
        :param _UpdateTime: 上次更新时间，毫秒级时间戳 。
        :type UpdateTime: int
        :param _NotAfterTime: 失效日期，毫秒级时间戳 。
        :type NotAfterTime: int
        :param _LastActivationTime: 上次激活时间，毫秒级时间戳 。
        :type LastActivationTime: int
        :param _LastInactivationTime: 上次吊销时间，毫秒级时间戳 。
        :type LastInactivationTime: int
        :param _Status: CA证书状态
 ACTIVE：激活
INACTIVE：未激活

        :type Status: str
        :param _CaSn: 证书序列号
        :type CaSn: str
        :param _CaCn: 证书的CN（Common Name），证书中用于标识主体的名称，通常是域名或组织名称
        :type CaCn: str
        :param _CaCertificate: 证书内容
        :type CaCertificate: str
        :param _Format: 证书格式，当仅支持PEM格式
        :type Format: str
        :param _CaIssuerCn: Ca证书颁发者CN
        :type CaIssuerCn: str
        :param _NotBeforeTime: 生效开始时间，毫秒级时间戳 。
        :type NotBeforeTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CreatedTime = None
        self._UpdateTime = None
        self._NotAfterTime = None
        self._LastActivationTime = None
        self._LastInactivationTime = None
        self._Status = None
        self._CaSn = None
        self._CaCn = None
        self._CaCertificate = None
        self._Format = None
        self._CaIssuerCn = None
        self._NotBeforeTime = None
        self._RequestId = None

    @property
    def CreatedTime(self):
        """创建时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """上次更新时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def NotAfterTime(self):
        """失效日期，毫秒级时间戳 。
        :rtype: int
        """
        return self._NotAfterTime

    @NotAfterTime.setter
    def NotAfterTime(self, NotAfterTime):
        self._NotAfterTime = NotAfterTime

    @property
    def LastActivationTime(self):
        """上次激活时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._LastActivationTime

    @LastActivationTime.setter
    def LastActivationTime(self, LastActivationTime):
        self._LastActivationTime = LastActivationTime

    @property
    def LastInactivationTime(self):
        """上次吊销时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._LastInactivationTime

    @LastInactivationTime.setter
    def LastInactivationTime(self, LastInactivationTime):
        self._LastInactivationTime = LastInactivationTime

    @property
    def Status(self):
        """CA证书状态
 ACTIVE：激活
INACTIVE：未激活

        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CaSn(self):
        """证书序列号
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def CaCn(self):
        """证书的CN（Common Name），证书中用于标识主体的名称，通常是域名或组织名称
        :rtype: str
        """
        return self._CaCn

    @CaCn.setter
    def CaCn(self, CaCn):
        self._CaCn = CaCn

    @property
    def CaCertificate(self):
        """证书内容
        :rtype: str
        """
        return self._CaCertificate

    @CaCertificate.setter
    def CaCertificate(self, CaCertificate):
        self._CaCertificate = CaCertificate

    @property
    def Format(self):
        """证书格式，当仅支持PEM格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CaIssuerCn(self):
        """Ca证书颁发者CN
        :rtype: str
        """
        return self._CaIssuerCn

    @CaIssuerCn.setter
    def CaIssuerCn(self, CaIssuerCn):
        self._CaIssuerCn = CaIssuerCn

    @property
    def NotBeforeTime(self):
        """生效开始时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._NotBeforeTime

    @NotBeforeTime.setter
    def NotBeforeTime(self, NotBeforeTime):
        self._NotBeforeTime = NotBeforeTime

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
        self._CreatedTime = params.get("CreatedTime")
        self._UpdateTime = params.get("UpdateTime")
        self._NotAfterTime = params.get("NotAfterTime")
        self._LastActivationTime = params.get("LastActivationTime")
        self._LastInactivationTime = params.get("LastInactivationTime")
        self._Status = params.get("Status")
        self._CaSn = params.get("CaSn")
        self._CaCn = params.get("CaCn")
        self._CaCertificate = params.get("CaCertificate")
        self._Format = params.get("Format")
        self._CaIssuerCn = params.get("CaIssuerCn")
        self._NotBeforeTime = params.get("NotBeforeTime")
        self._RequestId = params.get("RequestId")


class DescribeCaCertificatesRequest(AbstractModel):
    """DescribeCaCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
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
        


class DescribeCaCertificatesResponse(AbstractModel):
    """DescribeCaCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: ca证书列表
        :type Data: list of CaCertificateItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """ca证书列表
        :rtype: list of CaCertificateItem
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
            self._Data = []
            for item in params.get("Data"):
                obj = CaCertificateItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeClientListRequest(AbstractModel):
    """DescribeClientList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _ClientId: 客户端ID
        :type ClientId: str
        :param _Number: 客户端数量限制,最大1024，默认1024
        :type Number: str
        """
        self._InstanceId = None
        self._ClientId = None
        self._Number = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ClientId(self):
        """客户端ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Number(self):
        """客户端数量限制,最大1024，默认1024
        :rtype: str
        """
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ClientId = params.get("ClientId")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClientListResponse(AbstractModel):
    """DescribeClientList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Clients: 客户端列表
        :type Clients: list of MQTTClientInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Clients = None
        self._RequestId = None

    @property
    def Clients(self):
        """客户端列表
        :rtype: list of MQTTClientInfo
        """
        return self._Clients

    @Clients.setter
    def Clients(self, Clients):
        self._Clients = Clients

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
        if params.get("Clients") is not None:
            self._Clients = []
            for item in params.get("Clients"):
                obj = MQTTClientInfo()
                obj._deserialize(item)
                self._Clients.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDeviceCertificateRequest(AbstractModel):
    """DescribeDeviceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceCertificateSn: 设备证书的SN序列号，用于唯一标识一个设备证书。
        :type DeviceCertificateSn: str
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._DeviceCertificateSn = None
        self._InstanceId = None

    @property
    def DeviceCertificateSn(self):
        """设备证书的SN序列号，用于唯一标识一个设备证书。
        :rtype: str
        """
        return self._DeviceCertificateSn

    @DeviceCertificateSn.setter
    def DeviceCertificateSn(self, DeviceCertificateSn):
        self._DeviceCertificateSn = DeviceCertificateSn

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._DeviceCertificateSn = params.get("DeviceCertificateSn")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceCertificateResponse(AbstractModel):
    """DescribeDeviceCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CreatedTime: 创建时间，毫秒级时间戳 。
        :type CreatedTime: int
        :param _UpdateTime: 上次更新时间，毫秒级时间戳 。
        :type UpdateTime: int
        :param _NotAfterTime: 证书失效日期，毫秒级时间戳 。
        :type NotAfterTime: int
        :param _LastActivationTime: 上次激活时间，毫秒级时间戳 。
        :type LastActivationTime: int
        :param _LastInactivationTime: 上次取消激活时间，毫秒级时间戳 。
        :type LastInactivationTime: int
        :param _Status: 设备证书的状态
    ACTIVE：激活 
    INACTIVE：未激活
    REVOKED：吊销
    PENDING_ACTIVATION：注册待激活
        :type Status: str
        :param _CaSn: Ca证书序列号
        :type CaSn: str
        :param _DeviceCertificateSn: 设备证书序列号
        :type DeviceCertificateSn: str
        :param _DeviceCertificate: 设备证书内容
        :type DeviceCertificate: str
        :param _DeviceCertificateCn: 设备证书common name
        :type DeviceCertificateCn: str
        :param _Format: 证书格式，当前仅支持PEM格式
        :type Format: str
        :param _ClientId: 客户端id
        :type ClientId: str
        :param _CertificateSource: 证书来源    
API：手动注册   
JITP：自动注册
        :type CertificateSource: str
        :param _NotBeforeTime: 证书生效开始时间，毫秒级时间戳 。
        :type NotBeforeTime: int
        :param _OrganizationalUnit: 组织单位
        :type OrganizationalUnit: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CreatedTime = None
        self._UpdateTime = None
        self._NotAfterTime = None
        self._LastActivationTime = None
        self._LastInactivationTime = None
        self._Status = None
        self._CaSn = None
        self._DeviceCertificateSn = None
        self._DeviceCertificate = None
        self._DeviceCertificateCn = None
        self._Format = None
        self._ClientId = None
        self._CertificateSource = None
        self._NotBeforeTime = None
        self._OrganizationalUnit = None
        self._RequestId = None

    @property
    def CreatedTime(self):
        """创建时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """上次更新时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def NotAfterTime(self):
        """证书失效日期，毫秒级时间戳 。
        :rtype: int
        """
        return self._NotAfterTime

    @NotAfterTime.setter
    def NotAfterTime(self, NotAfterTime):
        self._NotAfterTime = NotAfterTime

    @property
    def LastActivationTime(self):
        """上次激活时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._LastActivationTime

    @LastActivationTime.setter
    def LastActivationTime(self, LastActivationTime):
        self._LastActivationTime = LastActivationTime

    @property
    def LastInactivationTime(self):
        """上次取消激活时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._LastInactivationTime

    @LastInactivationTime.setter
    def LastInactivationTime(self, LastInactivationTime):
        self._LastInactivationTime = LastInactivationTime

    @property
    def Status(self):
        """设备证书的状态
    ACTIVE：激活 
    INACTIVE：未激活
    REVOKED：吊销
    PENDING_ACTIVATION：注册待激活
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CaSn(self):
        """Ca证书序列号
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def DeviceCertificateSn(self):
        """设备证书序列号
        :rtype: str
        """
        return self._DeviceCertificateSn

    @DeviceCertificateSn.setter
    def DeviceCertificateSn(self, DeviceCertificateSn):
        self._DeviceCertificateSn = DeviceCertificateSn

    @property
    def DeviceCertificate(self):
        """设备证书内容
        :rtype: str
        """
        return self._DeviceCertificate

    @DeviceCertificate.setter
    def DeviceCertificate(self, DeviceCertificate):
        self._DeviceCertificate = DeviceCertificate

    @property
    def DeviceCertificateCn(self):
        """设备证书common name
        :rtype: str
        """
        return self._DeviceCertificateCn

    @DeviceCertificateCn.setter
    def DeviceCertificateCn(self, DeviceCertificateCn):
        self._DeviceCertificateCn = DeviceCertificateCn

    @property
    def Format(self):
        """证书格式，当前仅支持PEM格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def ClientId(self):
        """客户端id
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def CertificateSource(self):
        """证书来源    
API：手动注册   
JITP：自动注册
        :rtype: str
        """
        return self._CertificateSource

    @CertificateSource.setter
    def CertificateSource(self, CertificateSource):
        self._CertificateSource = CertificateSource

    @property
    def NotBeforeTime(self):
        """证书生效开始时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._NotBeforeTime

    @NotBeforeTime.setter
    def NotBeforeTime(self, NotBeforeTime):
        self._NotBeforeTime = NotBeforeTime

    @property
    def OrganizationalUnit(self):
        """组织单位
        :rtype: str
        """
        return self._OrganizationalUnit

    @OrganizationalUnit.setter
    def OrganizationalUnit(self, OrganizationalUnit):
        self._OrganizationalUnit = OrganizationalUnit

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
        self._CreatedTime = params.get("CreatedTime")
        self._UpdateTime = params.get("UpdateTime")
        self._NotAfterTime = params.get("NotAfterTime")
        self._LastActivationTime = params.get("LastActivationTime")
        self._LastInactivationTime = params.get("LastInactivationTime")
        self._Status = params.get("Status")
        self._CaSn = params.get("CaSn")
        self._DeviceCertificateSn = params.get("DeviceCertificateSn")
        self._DeviceCertificate = params.get("DeviceCertificate")
        self._DeviceCertificateCn = params.get("DeviceCertificateCn")
        self._Format = params.get("Format")
        self._ClientId = params.get("ClientId")
        self._CertificateSource = params.get("CertificateSource")
        self._NotBeforeTime = params.get("NotBeforeTime")
        self._OrganizationalUnit = params.get("OrganizationalUnit")
        self._RequestId = params.get("RequestId")


class DescribeDeviceCertificatesRequest(AbstractModel):
    """DescribeDeviceCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Filters: 支持搜索参数
ClientId：客户端id，根据实际业务使用获取
CaSn：所属的CA证书SN序列号 可以从 [查询集群CA证书列表](https://cloud.tencent.com/document/api/1778/116206) 或者实际业务使用获取
DeviceCertificateSn：设备证书SN序列号 可从[查询设备证书详情](https://cloud.tencent.com/document/api/1778/113748) 获取
DeviceCertificateCn：设备证书CN 可从[查询设备证书详情](https://cloud.tencent.com/document/api/1778/113748) 获取
OrganizationalUnit：证书OU
NotAfterEnd：过期时间小于等于指定时间的证书
NotAfterStart：过期时间大于等于指定时间的证书
Status：设备证书状态     ACTIVE（激活）； INACTIVE（未激活）REVOKED（吊销）；PENDING_ACTIVATION（注册待激活）

        :type Filters: list of Filter
        :param _Limit: 分页limit，默认20，最大100
        :type Limit: int
        :param _Offset: 分页偏移量，默认0
        :type Offset: int
        :param _OrderBy: 排序规则
    CREATE_TIME_DESC, 创建时间降序
    CREATE_TIME_ASC,创建时间升序
    UPDATE_TIME_DESC,更新时间降序
    UPDATE_TIME_ASC,更新时间升序
        :type OrderBy: str
        """
        self._InstanceId = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._OrderBy = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        """支持搜索参数
ClientId：客户端id，根据实际业务使用获取
CaSn：所属的CA证书SN序列号 可以从 [查询集群CA证书列表](https://cloud.tencent.com/document/api/1778/116206) 或者实际业务使用获取
DeviceCertificateSn：设备证书SN序列号 可从[查询设备证书详情](https://cloud.tencent.com/document/api/1778/113748) 获取
DeviceCertificateCn：设备证书CN 可从[查询设备证书详情](https://cloud.tencent.com/document/api/1778/113748) 获取
OrganizationalUnit：证书OU
NotAfterEnd：过期时间小于等于指定时间的证书
NotAfterStart：过期时间大于等于指定时间的证书
Status：设备证书状态     ACTIVE（激活）； INACTIVE（未激活）REVOKED（吊销）；PENDING_ACTIVATION（注册待激活）

        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """分页limit，默认20，最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """排序规则
    CREATE_TIME_DESC, 创建时间降序
    CREATE_TIME_ASC,创建时间升序
    UPDATE_TIME_DESC,更新时间降序
    UPDATE_TIME_ASC,更新时间升序
        :rtype: str
        """
        return self._OrderBy

    @OrderBy.setter
    def OrderBy(self, OrderBy):
        self._OrderBy = OrderBy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeviceCertificatesResponse(AbstractModel):
    """DescribeDeviceCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Data: 设备证书列表
        :type Data: list of DeviceCertificateItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """设备证书列表
        :rtype: list of DeviceCertificateItem
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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DeviceCertificateItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInsPublicEndpointsRequest(AbstractModel):
    """DescribeInsPublicEndpoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
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
        


class DescribeInsPublicEndpointsResponse(AbstractModel):
    """DescribeInsPublicEndpoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoints: 接入点
        :type Endpoints: list of MQTTEndpointItem
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _Bandwidth: 带宽，单位Mbps
        :type Bandwidth: int
        :param _Rules: 公网访问规则
        :type Rules: list of PublicAccessRule
        :param _Status: 公网状态：
    NORMAL-正常
    CLOSING-关闭中
    MODIFYING-修改中
    CREATING-开启中
    CLOSE-关闭
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoints = None
        self._InstanceId = None
        self._Bandwidth = None
        self._Rules = None
        self._Status = None
        self._RequestId = None

    @property
    def Endpoints(self):
        """接入点
        :rtype: list of MQTTEndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        """带宽，单位Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Rules(self):
        """公网访问规则
        :rtype: list of PublicAccessRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Status(self):
        """公网状态：
    NORMAL-正常
    CLOSING-关闭中
    MODIFYING-修改中
    CREATING-开启中
    CLOSE-关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

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
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = MQTTEndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeInsVPCEndpointsRequest(AbstractModel):
    """DescribeInsVPCEndpoints请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
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
        


class DescribeInsVPCEndpointsResponse(AbstractModel):
    """DescribeInsVPCEndpoints返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Endpoints: 接入点
        :type Endpoints: list of MQTTEndpointItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Endpoints = None
        self._RequestId = None

    @property
    def Endpoints(self):
        """接入点
        :rtype: list of MQTTEndpointItem
        """
        return self._Endpoints

    @Endpoints.setter
    def Endpoints(self, Endpoints):
        self._Endpoints = Endpoints

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
        if params.get("Endpoints") is not None:
            self._Endpoints = []
            for item in params.get("Endpoints"):
                obj = MQTTEndpointItem()
                obj._deserialize(item)
                self._Endpoints.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件列表,支持以下字段
InstanceName：集群名模糊搜索
InstanceId：集群id精确搜索
InstanceStatus：集群状态搜索（RUNNING-运行中，CREATING-创建中，MODIFYING-变配中，DELETING-删除中）
        :type Filters: list of Filter
        :param _Offset: 查询起始位置，默认0
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20，最大100
        :type Limit: int
        :param _TagFilters: 标签过滤器
        :type TagFilters: list of TagFilter
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._TagFilters = None

    @property
    def Filters(self):
        """查询条件列表,支持以下字段
InstanceName：集群名模糊搜索
InstanceId：集群id精确搜索
InstanceStatus：集群状态搜索（RUNNING-运行中，CREATING-创建中，MODIFYING-变配中，DELETING-删除中）
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """查询起始位置，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询结果限制数量，默认20，最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TagFilters(self):
        """标签过滤器
        :rtype: list of TagFilter
        """
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceListResponse(AbstractModel):
    """DescribeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 实例列表
        :type Data: list of MQTTInstanceItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """实例列表
        :rtype: list of MQTTInstanceItem
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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTInstanceItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceRequest(AbstractModel):
    """DescribeInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)
        :rtype: str
        """
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
        


class DescribeInstanceResponse(AbstractModel):
    """DescribeInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 实例类型
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :type InstanceType: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _TopicNumLimit: 实例最大主题数量
        :type TopicNumLimit: int
        :param _TpsLimit: TPS限流值
        :type TpsLimit: int
        :param _CreatedTime: 创建时间，秒为单位
        :type CreatedTime: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _InstanceStatus: 实例状态， RUNNING, 运行中 MAINTAINING，维护中 ABNORMAL，异常 OVERDUE，欠费 DESTROYED，已删除 CREATING，创建中 MODIFYING，变配中 CREATE_FAILURE，创建失败 MODIFY_FAILURE，变配失败 DELETING，删除中
        :type InstanceStatus: str
        :param _SkuCode: 实例规格
        :type SkuCode: str
        :param _MaxSubscriptionPerClient: 单客户端最大订阅数
        :type MaxSubscriptionPerClient: int
        :param _AuthorizationPolicyLimit: 授权规则条数
        :type AuthorizationPolicyLimit: int
        :param _ClientNumLimit: 客户端数量上限
        :type ClientNumLimit: int
        :param _DeviceCertificateProvisionType: 客户端证书注册方式：
JITP：自动注册
API：通过API手动注册
        :type DeviceCertificateProvisionType: str
        :param _AutomaticActivation: 自动注册设备证书时是否自动激活
        :type AutomaticActivation: bool
        :param _RenewFlag: 是否自动续费。仅包年包月集群生效。 1:自动续费 0:非自动续费
        :type RenewFlag: int
        :param _PayMode: 计费模式， POSTPAID，按量计费 PREPAID，包年包月
        :type PayMode: str
        :param _ExpiryTime: 到期时间，毫秒级时间戳
        :type ExpiryTime: int
        :param _DestroyTime: 预销毁时间，毫秒级时间戳
        :type DestroyTime: int
        :param _X509Mode: TLS,单向认证    mTLS,双向认证    BYOC;一机一证
        :type X509Mode: str
        :param _MaxCaNum: 最大Ca配额
        :type MaxCaNum: int
        :param _RegistrationCode: 证书注册码
        :type RegistrationCode: str
        :param _MaxSubscription: 集群最大订阅数
        :type MaxSubscription: int
        :param _AuthorizationPolicy: 授权策略开关
        :type AuthorizationPolicy: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceType = None
        self._InstanceId = None
        self._InstanceName = None
        self._TopicNum = None
        self._TopicNumLimit = None
        self._TpsLimit = None
        self._CreatedTime = None
        self._Remark = None
        self._InstanceStatus = None
        self._SkuCode = None
        self._MaxSubscriptionPerClient = None
        self._AuthorizationPolicyLimit = None
        self._ClientNumLimit = None
        self._DeviceCertificateProvisionType = None
        self._AutomaticActivation = None
        self._RenewFlag = None
        self._PayMode = None
        self._ExpiryTime = None
        self._DestroyTime = None
        self._X509Mode = None
        self._MaxCaNum = None
        self._RegistrationCode = None
        self._MaxSubscription = None
        self._AuthorizationPolicy = None
        self._RequestId = None

    @property
    def InstanceType(self):
        """实例类型
BASIC 基础版
PRO  专业版
PLATINUM 铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def TopicNum(self):
        """主题数量
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def TopicNumLimit(self):
        """实例最大主题数量
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def TpsLimit(self):
        """TPS限流值
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreatedTime(self):
        """创建时间，秒为单位
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceStatus(self):
        """实例状态， RUNNING, 运行中 MAINTAINING，维护中 ABNORMAL，异常 OVERDUE，欠费 DESTROYED，已删除 CREATING，创建中 MODIFYING，变配中 CREATE_FAILURE，创建失败 MODIFY_FAILURE，变配失败 DELETING，删除中
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SkuCode(self):
        """实例规格
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def MaxSubscriptionPerClient(self):
        """单客户端最大订阅数
        :rtype: int
        """
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def AuthorizationPolicyLimit(self):
        """授权规则条数
        :rtype: int
        """
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def ClientNumLimit(self):
        """客户端数量上限
        :rtype: int
        """
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def DeviceCertificateProvisionType(self):
        """客户端证书注册方式：
JITP：自动注册
API：通过API手动注册
        :rtype: str
        """
        return self._DeviceCertificateProvisionType

    @DeviceCertificateProvisionType.setter
    def DeviceCertificateProvisionType(self, DeviceCertificateProvisionType):
        self._DeviceCertificateProvisionType = DeviceCertificateProvisionType

    @property
    def AutomaticActivation(self):
        """自动注册设备证书时是否自动激活
        :rtype: bool
        """
        return self._AutomaticActivation

    @AutomaticActivation.setter
    def AutomaticActivation(self, AutomaticActivation):
        self._AutomaticActivation = AutomaticActivation

    @property
    def RenewFlag(self):
        """是否自动续费。仅包年包月集群生效。 1:自动续费 0:非自动续费
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        """计费模式， POSTPAID，按量计费 PREPAID，包年包月
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        """到期时间，毫秒级时间戳
        :rtype: int
        """
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def DestroyTime(self):
        """预销毁时间，毫秒级时间戳
        :rtype: int
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def X509Mode(self):
        """TLS,单向认证    mTLS,双向认证    BYOC;一机一证
        :rtype: str
        """
        return self._X509Mode

    @X509Mode.setter
    def X509Mode(self, X509Mode):
        self._X509Mode = X509Mode

    @property
    def MaxCaNum(self):
        """最大Ca配额
        :rtype: int
        """
        return self._MaxCaNum

    @MaxCaNum.setter
    def MaxCaNum(self, MaxCaNum):
        self._MaxCaNum = MaxCaNum

    @property
    def RegistrationCode(self):
        """证书注册码
        :rtype: str
        """
        return self._RegistrationCode

    @RegistrationCode.setter
    def RegistrationCode(self, RegistrationCode):
        self._RegistrationCode = RegistrationCode

    @property
    def MaxSubscription(self):
        """集群最大订阅数
        :rtype: int
        """
        return self._MaxSubscription

    @MaxSubscription.setter
    def MaxSubscription(self, MaxSubscription):
        self._MaxSubscription = MaxSubscription

    @property
    def AuthorizationPolicy(self):
        """授权策略开关
        :rtype: bool
        """
        return self._AuthorizationPolicy

    @AuthorizationPolicy.setter
    def AuthorizationPolicy(self, AuthorizationPolicy):
        self._AuthorizationPolicy = AuthorizationPolicy

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
        self._InstanceType = params.get("InstanceType")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._TopicNum = params.get("TopicNum")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._TpsLimit = params.get("TpsLimit")
        self._CreatedTime = params.get("CreatedTime")
        self._Remark = params.get("Remark")
        self._InstanceStatus = params.get("InstanceStatus")
        self._SkuCode = params.get("SkuCode")
        self._MaxSubscriptionPerClient = params.get("MaxSubscriptionPerClient")
        self._AuthorizationPolicyLimit = params.get("AuthorizationPolicyLimit")
        self._ClientNumLimit = params.get("ClientNumLimit")
        self._DeviceCertificateProvisionType = params.get("DeviceCertificateProvisionType")
        self._AutomaticActivation = params.get("AutomaticActivation")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._ExpiryTime = params.get("ExpiryTime")
        self._DestroyTime = params.get("DestroyTime")
        self._X509Mode = params.get("X509Mode")
        self._MaxCaNum = params.get("MaxCaNum")
        self._RegistrationCode = params.get("RegistrationCode")
        self._MaxSubscription = params.get("MaxSubscription")
        self._AuthorizationPolicy = params.get("AuthorizationPolicy")
        self._RequestId = params.get("RequestId")


class DescribeMessageListRequest(AbstractModel):
    """DescribeMessageList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 要查询的一级Topic，可从 [查询MQTT主题列表](https://cloud.tencent.com/document/product/1778/111082) 获取。
        :type Topic: str
        :param _StartTime: 开始时间，毫秒级时间戳 。
        :type StartTime: int
        :param _EndTime: 结束时间，毫秒级时间戳 。
        :type EndTime: int
        :param _TaskRequestId: 请求任务id，用于相同查询参数下查询加速，第一次查询时无需传递，第一次查询会根据本次查询参数生成查询任务ID，保留查询条件，查询下一页消息时可传递第一次查询返回的任务ID。
        :type TaskRequestId: str
        :param _Offset: 查询起始位置，默认0
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20，最大50
        :type Limit: int
        """
        self._InstanceId = None
        self._Topic = None
        self._StartTime = None
        self._EndTime = None
        self._TaskRequestId = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """要查询的一级Topic，可从 [查询MQTT主题列表](https://cloud.tencent.com/document/product/1778/111082) 获取。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def StartTime(self):
        """开始时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskRequestId(self):
        """请求任务id，用于相同查询参数下查询加速，第一次查询时无需传递，第一次查询会根据本次查询参数生成查询任务ID，保留查询条件，查询下一页消息时可传递第一次查询返回的任务ID。
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

    @property
    def Offset(self):
        """查询起始位置，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询结果限制数量，默认20，最大50
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskRequestId = params.get("TaskRequestId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMessageListResponse(AbstractModel):
    """DescribeMessageList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 消息记录列表
        :type Data: list of MQTTMessageItem
        :param _TaskRequestId: 请求任务id
        :type TaskRequestId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._TaskRequestId = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """消息记录列表
        :rtype: list of MQTTMessageItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TaskRequestId(self):
        """请求任务id
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTMessageItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TaskRequestId = params.get("TaskRequestId")
        self._RequestId = params.get("RequestId")


class DescribeProductSKUListRequest(AbstractModel):
    """DescribeProductSKUList请求参数结构体

    """


class DescribeProductSKUListResponse(AbstractModel):
    """DescribeProductSKUList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _MQTTProductSkuList: mqtt商品配置信息
        :type MQTTProductSkuList: list of ProductSkuItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._MQTTProductSkuList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MQTTProductSkuList(self):
        """mqtt商品配置信息
        :rtype: list of ProductSkuItem
        """
        return self._MQTTProductSkuList

    @MQTTProductSkuList.setter
    def MQTTProductSkuList(self, MQTTProductSkuList):
        self._MQTTProductSkuList = MQTTProductSkuList

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
        self._TotalCount = params.get("TotalCount")
        if params.get("MQTTProductSkuList") is not None:
            self._MQTTProductSkuList = []
            for item in params.get("MQTTProductSkuList"):
                obj = ProductSkuItem()
                obj._deserialize(item)
                self._MQTTProductSkuList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSharedSubscriptionLagRequest(AbstractModel):
    """DescribeSharedSubscriptionLag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id	
        :type InstanceId: str
        :param _SharedSubscription: 共享订阅表达式
        :type SharedSubscription: str
        """
        self._InstanceId = None
        self._SharedSubscription = None

    @property
    def InstanceId(self):
        """集群id	
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SharedSubscription(self):
        """共享订阅表达式
        :rtype: str
        """
        return self._SharedSubscription

    @SharedSubscription.setter
    def SharedSubscription(self, SharedSubscription):
        self._SharedSubscription = SharedSubscription


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SharedSubscription = params.get("SharedSubscription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSharedSubscriptionLagResponse(AbstractModel):
    """DescribeSharedSubscriptionLag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Lag: 堆积值
        :type Lag: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Lag = None
        self._RequestId = None

    @property
    def Lag(self):
        """堆积值
        :rtype: int
        """
        return self._Lag

    @Lag.setter
    def Lag(self, Lag):
        self._Lag = Lag

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
        self._Lag = params.get("Lag")
        self._RequestId = params.get("RequestId")


class DescribeTopicListRequest(AbstractModel):
    """DescribeTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Filters: 查询条件列表:
支持TopicName模糊查询
        :type Filters: list of Filter
        :param _Offset: 查询起始位置，默认0。
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认20，最大20
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        """查询条件列表:
支持TopicName模糊查询
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """查询起始位置，默认0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询结果限制数量，默认20，最大20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicListResponse(AbstractModel):
    """DescribeTopicList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 主题列表
        :type Data: list of MQTTTopicItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """主题列表
        :rtype: list of MQTTTopicItem
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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTTopicItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopicRequest(AbstractModel):
    """DescribeTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        """
        self._InstanceId = None
        self._Topic = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopicResponse(AbstractModel):
    """DescribeTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Remark: 备注
        :type Remark: str
        :param _CreatedTime: 创建时间，秒为单位
        :type CreatedTime: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceId = None
        self._Topic = None
        self._Remark = None
        self._CreatedTime = None
        self._RequestId = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        """创建时间，秒为单位
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

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
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        self._CreatedTime = params.get("CreatedTime")
        self._RequestId = params.get("RequestId")


class DescribeUserListRequest(AbstractModel):
    """DescribeUserList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Filters: 查询条件列表支持字段
Username：按照【用户名】进行过滤，支持模糊过滤，类型：String
        :type Filters: list of Filter
        :param _Offset: 查询起始位置，默认值0
        :type Offset: int
        :param _Limit: 查询结果限制数量，默认值20，最大值100
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceId(self):
        """实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        """查询条件列表支持字段
Username：按照【用户名】进行过滤，支持模糊过滤，类型：String
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """查询起始位置，默认值0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询结果限制数量，默认值20，最大值100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUserListResponse(AbstractModel):
    """DescribeUserList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询总数
        :type TotalCount: int
        :param _Data: 角色信息列表
        :type Data: list of MQTTUserItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Data = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Data(self):
        """角色信息列表
        :rtype: list of MQTTUserItem
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
        self._TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MQTTUserItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DeviceCertificateItem(AbstractModel):
    """设备证书信息

    """

    def __init__(self):
        r"""
        :param _ClientId: 客户端id
        :type ClientId: str
        :param _DeviceCertificate: 设备证书
        :type DeviceCertificate: str
        :param _DeviceCertificateSn: 设备证书SN序列号，用于唯一标识一个设备证书
        :type DeviceCertificateSn: str
        :param _DeviceCertificateCn: 设备证书Cn
        :type DeviceCertificateCn: str
        :param _CaSn: 签发该证书的CA证书的序列号
        :type CaSn: str
        :param _Format: 证书格式，当前仅支持PEM
        :type Format: str
        :param _Status: 设备证书状态
    ACTIVE：激活
    INACTIVE：未激活
    REVOKED：吊销
    PENDING_ACTIVATION：注册待激活
        :type Status: str
        :param _OrganizationalUnit: 组织单位
        :type OrganizationalUnit: str
        :param _LastActivationTime: 上次激活时间，毫秒级时间戳 。
        :type LastActivationTime: int
        :param _LastInactivationTime: 上次取消激活时间，毫秒级时间戳 。
        :type LastInactivationTime: int
        :param _CreatedTime: 创建时间，毫秒级时间戳 。
        :type CreatedTime: int
        :param _UpdateTime: 更新时间，毫秒级时间戳 。
        :type UpdateTime: int
        :param _CertificateSource: 证书来源：
API, 手动注册   
JITP 自动注册
        :type CertificateSource: str
        :param _NotAfterTime: 证书失效日期，毫秒级时间戳 。
        :type NotAfterTime: int
        :param _NotBeforeTime: 证书生效开始日期，毫秒级时间戳 。
        :type NotBeforeTime: int
        """
        self._ClientId = None
        self._DeviceCertificate = None
        self._DeviceCertificateSn = None
        self._DeviceCertificateCn = None
        self._CaSn = None
        self._Format = None
        self._Status = None
        self._OrganizationalUnit = None
        self._LastActivationTime = None
        self._LastInactivationTime = None
        self._CreatedTime = None
        self._UpdateTime = None
        self._CertificateSource = None
        self._NotAfterTime = None
        self._NotBeforeTime = None

    @property
    def ClientId(self):
        """客户端id
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def DeviceCertificate(self):
        """设备证书
        :rtype: str
        """
        return self._DeviceCertificate

    @DeviceCertificate.setter
    def DeviceCertificate(self, DeviceCertificate):
        self._DeviceCertificate = DeviceCertificate

    @property
    def DeviceCertificateSn(self):
        """设备证书SN序列号，用于唯一标识一个设备证书
        :rtype: str
        """
        return self._DeviceCertificateSn

    @DeviceCertificateSn.setter
    def DeviceCertificateSn(self, DeviceCertificateSn):
        self._DeviceCertificateSn = DeviceCertificateSn

    @property
    def DeviceCertificateCn(self):
        """设备证书Cn
        :rtype: str
        """
        return self._DeviceCertificateCn

    @DeviceCertificateCn.setter
    def DeviceCertificateCn(self, DeviceCertificateCn):
        self._DeviceCertificateCn = DeviceCertificateCn

    @property
    def CaSn(self):
        """签发该证书的CA证书的序列号
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def Format(self):
        """证书格式，当前仅支持PEM
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Status(self):
        """设备证书状态
    ACTIVE：激活
    INACTIVE：未激活
    REVOKED：吊销
    PENDING_ACTIVATION：注册待激活
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def OrganizationalUnit(self):
        """组织单位
        :rtype: str
        """
        return self._OrganizationalUnit

    @OrganizationalUnit.setter
    def OrganizationalUnit(self, OrganizationalUnit):
        self._OrganizationalUnit = OrganizationalUnit

    @property
    def LastActivationTime(self):
        """上次激活时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._LastActivationTime

    @LastActivationTime.setter
    def LastActivationTime(self, LastActivationTime):
        self._LastActivationTime = LastActivationTime

    @property
    def LastInactivationTime(self):
        """上次取消激活时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._LastInactivationTime

    @LastInactivationTime.setter
    def LastInactivationTime(self, LastInactivationTime):
        self._LastInactivationTime = LastInactivationTime

    @property
    def CreatedTime(self):
        """创建时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """更新时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CertificateSource(self):
        """证书来源：
API, 手动注册   
JITP 自动注册
        :rtype: str
        """
        return self._CertificateSource

    @CertificateSource.setter
    def CertificateSource(self, CertificateSource):
        self._CertificateSource = CertificateSource

    @property
    def NotAfterTime(self):
        """证书失效日期，毫秒级时间戳 。
        :rtype: int
        """
        return self._NotAfterTime

    @NotAfterTime.setter
    def NotAfterTime(self, NotAfterTime):
        self._NotAfterTime = NotAfterTime

    @property
    def NotBeforeTime(self):
        """证书生效开始日期，毫秒级时间戳 。
        :rtype: int
        """
        return self._NotBeforeTime

    @NotBeforeTime.setter
    def NotBeforeTime(self, NotBeforeTime):
        self._NotBeforeTime = NotBeforeTime


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._DeviceCertificate = params.get("DeviceCertificate")
        self._DeviceCertificateSn = params.get("DeviceCertificateSn")
        self._DeviceCertificateCn = params.get("DeviceCertificateCn")
        self._CaSn = params.get("CaSn")
        self._Format = params.get("Format")
        self._Status = params.get("Status")
        self._OrganizationalUnit = params.get("OrganizationalUnit")
        self._LastActivationTime = params.get("LastActivationTime")
        self._LastInactivationTime = params.get("LastInactivationTime")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CertificateSource = params.get("CertificateSource")
        self._NotAfterTime = params.get("NotAfterTime")
        self._NotBeforeTime = params.get("NotBeforeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """查询过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 过滤条件名
        :type Name: str
        :param _Values: 过滤条件的值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """过滤条件名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """过滤条件的值
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
        


class HeaderItem(AbstractModel):
    """HTTP 认证器header

    """

    def __init__(self):
        r"""
        :param _Key: header key
        :type Key: str
        :param _Value: header value
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """header key
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """header value
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
        


class IpRule(AbstractModel):
    """IP规则

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _Allow: 是否允许放行
        :type Allow: bool
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._Ip = None
        self._Allow = None
        self._Remark = None

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Allow(self):
        """是否允许放行
        :rtype: bool
        """
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Allow = params.get("Allow")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTAuthenticatorItem(AbstractModel):
    """MQTT认证器信息

    """

    def __init__(self):
        r"""
        :param _Type: 认证器类型
JWT：JWT认证器
JWKS：JWKS认证器
HTTP：HTTP认证器
        :type Type: str
        :param _Config: JWT认证器字段说明
from（认证字段）
    password：从password字段获取认证字段
    username：从username字段获取认证字段
secret（签名方式）
    hmac-based：hmac-based签名方式
    public-key：public-key签名方式
secret（密钥），hmac-based需要配置密钥
public-key（公钥），public-key签名方式需要配置
样例：{"from":"password","secret":"secret282698","algorithm":"hmac-based"}

JWKS认证器字段说明
endpoint（接入点）：公钥获取服务器接入地址
refreshInterval（认证内容）：公钥集合刷新周期
from（认证字段）
    password：从password字段获取认证字段
    username：从username字段获取认证字段
text：公钥集合
样例：{"endpoint":"127.0.0.1","refreshInterval":60,"from":"password"}

HTTP认证器
headers（请求头）：标准请求头和自定义请求头
endpoint（接入点）：认证服务器接入点
method（http请求方法）：POST/GET
readTimeout（读超时时间）：读取认证服务器数据超时时间，单位秒
connectTimeout（连接超时时间）：连接认证服务器超时时间，单位秒
body（请求体）：http请求体
concurrency（并发数）：最大并发请求数量
样例：{"headers":[{"key":"Content-type","value":"application/json"},{"key":"username","value":"${Username}"}],"endpoint":"https://127.0.0.1:443","method":"POST","readTimeout":10,"connectTimeout":10,"body":[{"key":"client-id","value":"${ClientId}"}],"concurrency":8}
参考 [认证管理概述](https://cloud.tencent.com/document/product/1778/114813)
        :type Config: str
        :param _Status: 认证器状态
open：认证器打开
close：认证器关闭
        :type Status: str
        :param _CreateTime: 创建时间，毫秒级时间戳 。
        :type CreateTime: int
        :param _Remark: 说明，最长 128 字符。
        :type Remark: str
        """
        self._Type = None
        self._Config = None
        self._Status = None
        self._CreateTime = None
        self._Remark = None

    @property
    def Type(self):
        """认证器类型
JWT：JWT认证器
JWKS：JWKS认证器
HTTP：HTTP认证器
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Config(self):
        """JWT认证器字段说明
from（认证字段）
    password：从password字段获取认证字段
    username：从username字段获取认证字段
secret（签名方式）
    hmac-based：hmac-based签名方式
    public-key：public-key签名方式
secret（密钥），hmac-based需要配置密钥
public-key（公钥），public-key签名方式需要配置
样例：{"from":"password","secret":"secret282698","algorithm":"hmac-based"}

JWKS认证器字段说明
endpoint（接入点）：公钥获取服务器接入地址
refreshInterval（认证内容）：公钥集合刷新周期
from（认证字段）
    password：从password字段获取认证字段
    username：从username字段获取认证字段
text：公钥集合
样例：{"endpoint":"127.0.0.1","refreshInterval":60,"from":"password"}

HTTP认证器
headers（请求头）：标准请求头和自定义请求头
endpoint（接入点）：认证服务器接入点
method（http请求方法）：POST/GET
readTimeout（读超时时间）：读取认证服务器数据超时时间，单位秒
connectTimeout（连接超时时间）：连接认证服务器超时时间，单位秒
body（请求体）：http请求体
concurrency（并发数）：最大并发请求数量
样例：{"headers":[{"key":"Content-type","value":"application/json"},{"key":"username","value":"${Username}"}],"endpoint":"https://127.0.0.1:443","method":"POST","readTimeout":10,"connectTimeout":10,"body":[{"key":"client-id","value":"${ClientId}"}],"concurrency":8}
参考 [认证管理概述](https://cloud.tencent.com/document/product/1778/114813)
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Status(self):
        """认证器状态
open：认证器打开
close：认证器关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        """说明，最长 128 字符。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Config = params.get("Config")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTClientInfo(AbstractModel):
    """MQTT客户端信息

    """

    def __init__(self):
        r"""
        :param _ClientId: 客户端ID
        :type ClientId: str
        :param _ClientAddress: 客户端网络地址
        :type ClientAddress: str
        :param _ProtocolVersion: MQTT 协议版本
3：表示MQTT 3.1版本
4：表示 MQTT 3.1.1
5：表示MQTT 5.0协议
        :type ProtocolVersion: int
        :param _Keepalive: 保持连接时间，单位：秒
        :type Keepalive: int
        :param _ConnectionStatus: 连接状态，CONNECTED 已连接，DISCONNECTED 未连接
        :type ConnectionStatus: str
        :param _CreateTime: 客户端创建时间，毫秒级时间戳 。
        :type CreateTime: int
        :param _ConnectTime: 上次建立连接时间，毫秒级时间戳 。
        :type ConnectTime: int
        :param _DisconnectTime: 上次断开连接时间，仅对持久会话（cleanSession=false）并且客户端当前未连接时有意义，毫秒级时间戳 。
        :type DisconnectTime: int
        :param _MQTTClientSubscriptions: 客户端的订阅列表
        :type MQTTClientSubscriptions: list of MQTTClientSubscription
        """
        self._ClientId = None
        self._ClientAddress = None
        self._ProtocolVersion = None
        self._Keepalive = None
        self._ConnectionStatus = None
        self._CreateTime = None
        self._ConnectTime = None
        self._DisconnectTime = None
        self._MQTTClientSubscriptions = None

    @property
    def ClientId(self):
        """客户端ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def ClientAddress(self):
        """客户端网络地址
        :rtype: str
        """
        return self._ClientAddress

    @ClientAddress.setter
    def ClientAddress(self, ClientAddress):
        self._ClientAddress = ClientAddress

    @property
    def ProtocolVersion(self):
        """MQTT 协议版本
3：表示MQTT 3.1版本
4：表示 MQTT 3.1.1
5：表示MQTT 5.0协议
        :rtype: int
        """
        return self._ProtocolVersion

    @ProtocolVersion.setter
    def ProtocolVersion(self, ProtocolVersion):
        self._ProtocolVersion = ProtocolVersion

    @property
    def Keepalive(self):
        """保持连接时间，单位：秒
        :rtype: int
        """
        return self._Keepalive

    @Keepalive.setter
    def Keepalive(self, Keepalive):
        self._Keepalive = Keepalive

    @property
    def ConnectionStatus(self):
        """连接状态，CONNECTED 已连接，DISCONNECTED 未连接
        :rtype: str
        """
        return self._ConnectionStatus

    @ConnectionStatus.setter
    def ConnectionStatus(self, ConnectionStatus):
        self._ConnectionStatus = ConnectionStatus

    @property
    def CreateTime(self):
        """客户端创建时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ConnectTime(self):
        """上次建立连接时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._ConnectTime

    @ConnectTime.setter
    def ConnectTime(self, ConnectTime):
        self._ConnectTime = ConnectTime

    @property
    def DisconnectTime(self):
        """上次断开连接时间，仅对持久会话（cleanSession=false）并且客户端当前未连接时有意义，毫秒级时间戳 。
        :rtype: int
        """
        return self._DisconnectTime

    @DisconnectTime.setter
    def DisconnectTime(self, DisconnectTime):
        self._DisconnectTime = DisconnectTime

    @property
    def MQTTClientSubscriptions(self):
        """客户端的订阅列表
        :rtype: list of MQTTClientSubscription
        """
        return self._MQTTClientSubscriptions

    @MQTTClientSubscriptions.setter
    def MQTTClientSubscriptions(self, MQTTClientSubscriptions):
        self._MQTTClientSubscriptions = MQTTClientSubscriptions


    def _deserialize(self, params):
        self._ClientId = params.get("ClientId")
        self._ClientAddress = params.get("ClientAddress")
        self._ProtocolVersion = params.get("ProtocolVersion")
        self._Keepalive = params.get("Keepalive")
        self._ConnectionStatus = params.get("ConnectionStatus")
        self._CreateTime = params.get("CreateTime")
        self._ConnectTime = params.get("ConnectTime")
        self._DisconnectTime = params.get("DisconnectTime")
        if params.get("MQTTClientSubscriptions") is not None:
            self._MQTTClientSubscriptions = []
            for item in params.get("MQTTClientSubscriptions"):
                obj = MQTTClientSubscription()
                obj._deserialize(item)
                self._MQTTClientSubscriptions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTClientSubscription(AbstractModel):
    """MQTT 订阅关系

    """

    def __init__(self):
        r"""
        :param _TopicFilter: topic 订阅
        :type TopicFilter: str
        :param _Qos: 服务质量等级
0: 至多一次
1: 至少一次
2: 恰好一次
        :type Qos: int
        :param _Lag: 堆积数量
        :type Lag: int
        :param _Inflight: 投递未确认数量
        :type Inflight: int
        """
        self._TopicFilter = None
        self._Qos = None
        self._Lag = None
        self._Inflight = None

    @property
    def TopicFilter(self):
        """topic 订阅
        :rtype: str
        """
        return self._TopicFilter

    @TopicFilter.setter
    def TopicFilter(self, TopicFilter):
        self._TopicFilter = TopicFilter

    @property
    def Qos(self):
        """服务质量等级
0: 至多一次
1: 至少一次
2: 恰好一次
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Lag(self):
        """堆积数量
        :rtype: int
        """
        return self._Lag

    @Lag.setter
    def Lag(self, Lag):
        self._Lag = Lag

    @property
    def Inflight(self):
        """投递未确认数量
        :rtype: int
        """
        return self._Inflight

    @Inflight.setter
    def Inflight(self, Inflight):
        self._Inflight = Inflight


    def _deserialize(self, params):
        self._TopicFilter = params.get("TopicFilter")
        self._Qos = params.get("Qos")
        self._Lag = params.get("Lag")
        self._Inflight = params.get("Inflight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTEndpointItem(AbstractModel):
    """MQTTEndpoint

    """

    def __init__(self):
        r"""
        :param _Type: 类型
        :type Type: str
        :param _Url: 接入点
        :type Url: str
        :param _VpcId: vpc信息
        :type VpcId: str
        :param _SubnetId: 子网信息
        :type SubnetId: str
        :param _Host: 主机
        :type Host: str
        :param _Port: 端口
        :type Port: int
        :param _Ip: 接入点ip
        :type Ip: str
        """
        self._Type = None
        self._Url = None
        self._VpcId = None
        self._SubnetId = None
        self._Host = None
        self._Port = None
        self._Ip = None

    @property
    def Type(self):
        """类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        """接入点
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def VpcId(self):
        """vpc信息
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网信息
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Host(self):
        """主机
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        """端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Ip(self):
        """接入点ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Url = params.get("Url")
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        self._Host = params.get("Host")
        self._Port = params.get("Port")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTInstanceItem(AbstractModel):
    """MQTT 实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _Version: 实例版本
        :type Version: str
        :param _InstanceType: 实例类型
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :type InstanceType: str
        :param _InstanceStatus: 实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :type InstanceStatus: str
        :param _TopicNumLimit: 实例主题数上限
        :type TopicNumLimit: int
        :param _Remark: 备注信息
        :type Remark: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _SkuCode: 商品规格
        :type SkuCode: str
        :param _TpsLimit: 弹性TPS限流值
        :type TpsLimit: int
        :param _CreateTime: 创建时间，毫秒级时间戳
        :type CreateTime: int
        :param _MaxSubscriptionPerClient: 单客户端最大订阅数量
        :type MaxSubscriptionPerClient: int
        :param _ClientNumLimit: 客户端连接数上线
        :type ClientNumLimit: int
        :param _RenewFlag: 是否自动续费。仅包年包月集群生效。
1:自动续费
0:非自动续费
        :type RenewFlag: int
        :param _PayMode: 计费模式， POSTPAID，按量计费 PREPAID，包年包月
        :type PayMode: str
        :param _ExpiryTime: 到期时间，毫秒级时间戳
        :type ExpiryTime: int
        :param _DestroyTime: 预销毁时间，毫秒级时间戳
        :type DestroyTime: int
        :param _AuthorizationPolicyLimit: 授权规则条数限制
        :type AuthorizationPolicyLimit: int
        :param _MaxCaNum: 最大ca配额
        :type MaxCaNum: int
        :param _MaxSubscription: 最大订阅数
        :type MaxSubscription: int
        """
        self._InstanceId = None
        self._InstanceName = None
        self._Version = None
        self._InstanceType = None
        self._InstanceStatus = None
        self._TopicNumLimit = None
        self._Remark = None
        self._TopicNum = None
        self._SkuCode = None
        self._TpsLimit = None
        self._CreateTime = None
        self._MaxSubscriptionPerClient = None
        self._ClientNumLimit = None
        self._RenewFlag = None
        self._PayMode = None
        self._ExpiryTime = None
        self._DestroyTime = None
        self._AuthorizationPolicyLimit = None
        self._MaxCaNum = None
        self._MaxSubscription = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def Version(self):
        """实例版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def InstanceType(self):
        """实例类型
BASIC，基础版
PRO，专业版
PLATINUM，铂金版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        """实例状态，
RUNNING, 运行中
MAINTAINING，维护中
ABNORMAL，异常
OVERDUE，欠费
DESTROYED，已删除
CREATING，创建中
MODIFYING，变配中
CREATE_FAILURE，创建失败
MODIFY_FAILURE，变配失败
DELETING，删除中
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TopicNumLimit(self):
        """实例主题数上限
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicNum(self):
        """主题数量
        :rtype: int
        """
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def SkuCode(self):
        """商品规格
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def TpsLimit(self):
        """弹性TPS限流值
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreateTime(self):
        """创建时间，毫秒级时间戳
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MaxSubscriptionPerClient(self):
        """单客户端最大订阅数量
        :rtype: int
        """
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def ClientNumLimit(self):
        """客户端连接数上线
        :rtype: int
        """
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def RenewFlag(self):
        """是否自动续费。仅包年包月集群生效。
1:自动续费
0:非自动续费
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        """计费模式， POSTPAID，按量计费 PREPAID，包年包月
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        """到期时间，毫秒级时间戳
        :rtype: int
        """
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def DestroyTime(self):
        """预销毁时间，毫秒级时间戳
        :rtype: int
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def AuthorizationPolicyLimit(self):
        """授权规则条数限制
        :rtype: int
        """
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def MaxCaNum(self):
        """最大ca配额
        :rtype: int
        """
        return self._MaxCaNum

    @MaxCaNum.setter
    def MaxCaNum(self, MaxCaNum):
        self._MaxCaNum = MaxCaNum

    @property
    def MaxSubscription(self):
        """最大订阅数
        :rtype: int
        """
        return self._MaxSubscription

    @MaxSubscription.setter
    def MaxSubscription(self, MaxSubscription):
        self._MaxSubscription = MaxSubscription


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._Version = params.get("Version")
        self._InstanceType = params.get("InstanceType")
        self._InstanceStatus = params.get("InstanceStatus")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._Remark = params.get("Remark")
        self._TopicNum = params.get("TopicNum")
        self._SkuCode = params.get("SkuCode")
        self._TpsLimit = params.get("TpsLimit")
        self._CreateTime = params.get("CreateTime")
        self._MaxSubscriptionPerClient = params.get("MaxSubscriptionPerClient")
        self._ClientNumLimit = params.get("ClientNumLimit")
        self._RenewFlag = params.get("RenewFlag")
        self._PayMode = params.get("PayMode")
        self._ExpiryTime = params.get("ExpiryTime")
        self._DestroyTime = params.get("DestroyTime")
        self._AuthorizationPolicyLimit = params.get("AuthorizationPolicyLimit")
        self._MaxCaNum = params.get("MaxCaNum")
        self._MaxSubscription = params.get("MaxSubscription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTMessageItem(AbstractModel):
    """消息记录

    """

    def __init__(self):
        r"""
        :param _MsgId: 消息ID
        :type MsgId: str
        :param _Tags: 消息tag
        :type Tags: str
        :param _Keys: 消息key
        :type Keys: str
        :param _ProducerAddr: 客户端地址	
        :type ProducerAddr: str
        :param _ProduceTime: 消息发送时间，格式 日期时间：YYYY-MM-DD hh:mm:ss
        :type ProduceTime: str
        :param _DeadLetterResendTimes: 死信重发次数	
        :type DeadLetterResendTimes: int
        :param _DeadLetterResendSuccessTimes: 死信重发成功次数
        :type DeadLetterResendSuccessTimes: int
        :param _SubTopic: 子topic
        :type SubTopic: str
        :param _Qos: 消息质量等级
0：至多一次
1：至少一次
2：精确一次
        :type Qos: str
        """
        self._MsgId = None
        self._Tags = None
        self._Keys = None
        self._ProducerAddr = None
        self._ProduceTime = None
        self._DeadLetterResendTimes = None
        self._DeadLetterResendSuccessTimes = None
        self._SubTopic = None
        self._Qos = None

    @property
    def MsgId(self):
        """消息ID
        :rtype: str
        """
        return self._MsgId

    @MsgId.setter
    def MsgId(self, MsgId):
        self._MsgId = MsgId

    @property
    def Tags(self):
        """消息tag
        :rtype: str
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Keys(self):
        """消息key
        :rtype: str
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def ProducerAddr(self):
        """客户端地址	
        :rtype: str
        """
        return self._ProducerAddr

    @ProducerAddr.setter
    def ProducerAddr(self, ProducerAddr):
        self._ProducerAddr = ProducerAddr

    @property
    def ProduceTime(self):
        """消息发送时间，格式 日期时间：YYYY-MM-DD hh:mm:ss
        :rtype: str
        """
        return self._ProduceTime

    @ProduceTime.setter
    def ProduceTime(self, ProduceTime):
        self._ProduceTime = ProduceTime

    @property
    def DeadLetterResendTimes(self):
        """死信重发次数	
        :rtype: int
        """
        return self._DeadLetterResendTimes

    @DeadLetterResendTimes.setter
    def DeadLetterResendTimes(self, DeadLetterResendTimes):
        self._DeadLetterResendTimes = DeadLetterResendTimes

    @property
    def DeadLetterResendSuccessTimes(self):
        """死信重发成功次数
        :rtype: int
        """
        return self._DeadLetterResendSuccessTimes

    @DeadLetterResendSuccessTimes.setter
    def DeadLetterResendSuccessTimes(self, DeadLetterResendSuccessTimes):
        self._DeadLetterResendSuccessTimes = DeadLetterResendSuccessTimes

    @property
    def SubTopic(self):
        """子topic
        :rtype: str
        """
        return self._SubTopic

    @SubTopic.setter
    def SubTopic(self, SubTopic):
        self._SubTopic = SubTopic

    @property
    def Qos(self):
        """消息质量等级
0：至多一次
1：至少一次
2：精确一次
        :rtype: str
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos


    def _deserialize(self, params):
        self._MsgId = params.get("MsgId")
        self._Tags = params.get("Tags")
        self._Keys = params.get("Keys")
        self._ProducerAddr = params.get("ProducerAddr")
        self._ProduceTime = params.get("ProduceTime")
        self._DeadLetterResendTimes = params.get("DeadLetterResendTimes")
        self._DeadLetterResendSuccessTimes = params.get("DeadLetterResendSuccessTimes")
        self._SubTopic = params.get("SubTopic")
        self._Qos = params.get("Qos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTTopicItem(AbstractModel):
    """MQTT 主题详情

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例 ID
        :type InstanceId: str
        :param _Topic: 主题名称
        :type Topic: str
        :param _Remark: 主题描述
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例 ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题名称
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        """主题描述
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MQTTUserItem(AbstractModel):
    """MQTT集群用户信息

    """

    def __init__(self):
        r"""
        :param _Username: 用户名
        :type Username: str
        :param _Password: 密码
        :type Password: str
        :param _Remark: 备注信息
        :type Remark: str
        :param _CreatedTime: 创建时间，毫秒级时间戳 。
        :type CreatedTime: int
        :param _ModifiedTime: 修改时间，毫秒级时间戳 。
        :type ModifiedTime: int
        """
        self._Username = None
        self._Password = None
        self._Remark = None
        self._CreatedTime = None
        self._ModifiedTime = None

    @property
    def Username(self):
        """用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Password(self):
        """密码
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        """创建时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        """修改时间，毫秒级时间戳 。
        :rtype: int
        """
        return self._ModifiedTime

    @ModifiedTime.setter
    def ModifiedTime(self, ModifiedTime):
        self._ModifiedTime = ModifiedTime


    def _deserialize(self, params):
        self._Username = params.get("Username")
        self._Password = params.get("Password")
        self._Remark = params.get("Remark")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifiedTime = params.get("ModifiedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuthorizationPolicyRequest(AbstractModel):
    """ModifyAuthorizationPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 策略
        :type Id: int
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _PolicyName: 策略名称
        :type PolicyName: str
        :param _PolicyVersion: 策略版本
        :type PolicyVersion: int
        :param _Priority: 策略优先级，越小越优先
        :type Priority: int
        :param _Effect: allow、deny
        :type Effect: str
        :param _Actions: connect、pub、sub
        :type Actions: str
        :param _Resources: 资源
        :type Resources: str
        :param _Username: 用户名
        :type Username: str
        :param _Retain: 1.匹配保留消息；2.匹配非保留消息；3.匹配所有消息
        :type Retain: int
        :param _ClientId: 客户端
        :type ClientId: str
        :param _Ip: IP
        :type Ip: str
        :param _Qos: 0、1、2
        :type Qos: str
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._Id = None
        self._InstanceId = None
        self._PolicyName = None
        self._PolicyVersion = None
        self._Priority = None
        self._Effect = None
        self._Actions = None
        self._Resources = None
        self._Username = None
        self._Retain = None
        self._ClientId = None
        self._Ip = None
        self._Qos = None
        self._Remark = None

    @property
    def Id(self):
        """策略
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        """策略名称
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyVersion(self):
        """策略版本
        :rtype: int
        """
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion

    @property
    def Priority(self):
        """策略优先级，越小越优先
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Effect(self):
        """allow、deny
        :rtype: str
        """
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect

    @property
    def Actions(self):
        """connect、pub、sub
        :rtype: str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Resources(self):
        """资源
        :rtype: str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Username(self):
        """用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Retain(self):
        """1.匹配保留消息；2.匹配非保留消息；3.匹配所有消息
        :rtype: int
        """
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain

    @property
    def ClientId(self):
        """客户端
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Ip(self):
        """IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Qos(self):
        """0、1、2
        :rtype: str
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._InstanceId = params.get("InstanceId")
        self._PolicyName = params.get("PolicyName")
        self._PolicyVersion = params.get("PolicyVersion")
        self._Priority = params.get("Priority")
        self._Effect = params.get("Effect")
        self._Actions = params.get("Actions")
        self._Resources = params.get("Resources")
        self._Username = params.get("Username")
        self._Retain = params.get("Retain")
        self._ClientId = params.get("ClientId")
        self._Ip = params.get("Ip")
        self._Qos = params.get("Qos")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAuthorizationPolicyResponse(AbstractModel):
    """ModifyAuthorizationPolicy返回参数结构体

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


class ModifyHttpAuthenticatorRequest(AbstractModel):
    """ModifyHttpAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Endpoint: 端点
        :type Endpoint: str
        :param _Status: 认证器状态：open-启用；close-关闭
        :type Status: str
        :param _Concurrency: 最大并发连接数，默认8，范围：1-20
        :type Concurrency: int
        :param _ConnectTimeout: 连接超时时间，单位：秒，范围：1-30
        :type ConnectTimeout: int
        :param _ReadTimeout: 请求超时时间，单位：秒，范围：1-30
        :type ReadTimeout: int
        :param _Remark: 说明
        :type Remark: str
        :param _Method: 请求方法，GET 或者 POST
        :type Method: str
        :param _Header: 请求header
        :type Header: list of HeaderItem
        :param _Body: 请求body
        :type Body: list of BodyItem
        """
        self._InstanceId = None
        self._Endpoint = None
        self._Status = None
        self._Concurrency = None
        self._ConnectTimeout = None
        self._ReadTimeout = None
        self._Remark = None
        self._Method = None
        self._Header = None
        self._Body = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Endpoint(self):
        """端点
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def Status(self):
        """认证器状态：open-启用；close-关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Concurrency(self):
        """最大并发连接数，默认8，范围：1-20
        :rtype: int
        """
        return self._Concurrency

    @Concurrency.setter
    def Concurrency(self, Concurrency):
        self._Concurrency = Concurrency

    @property
    def ConnectTimeout(self):
        """连接超时时间，单位：秒，范围：1-30
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def ReadTimeout(self):
        """请求超时时间，单位：秒，范围：1-30
        :rtype: int
        """
        return self._ReadTimeout

    @ReadTimeout.setter
    def ReadTimeout(self, ReadTimeout):
        self._ReadTimeout = ReadTimeout

    @property
    def Remark(self):
        """说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Method(self):
        """请求方法，GET 或者 POST
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def Header(self):
        """请求header
        :rtype: list of HeaderItem
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def Body(self):
        """请求body
        :rtype: list of BodyItem
        """
        return self._Body

    @Body.setter
    def Body(self, Body):
        self._Body = Body


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Endpoint = params.get("Endpoint")
        self._Status = params.get("Status")
        self._Concurrency = params.get("Concurrency")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._ReadTimeout = params.get("ReadTimeout")
        self._Remark = params.get("Remark")
        self._Method = params.get("Method")
        if params.get("Header") is not None:
            self._Header = []
            for item in params.get("Header"):
                obj = HeaderItem()
                obj._deserialize(item)
                self._Header.append(obj)
        if params.get("Body") is not None:
            self._Body = []
            for item in params.get("Body"):
                obj = BodyItem()
                obj._deserialize(item)
                self._Body.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHttpAuthenticatorResponse(AbstractModel):
    """ModifyHttpAuthenticator返回参数结构体

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


class ModifyInsPublicEndpointRequest(AbstractModel):
    """ModifyInsPublicEndpoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Bandwidth: 带宽，单位：Mbps
        :type Bandwidth: int
        :param _Rules: 公网访问规则
        :type Rules: list of PublicAccessRule
        """
        self._InstanceId = None
        self._Bandwidth = None
        self._Rules = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Bandwidth(self):
        """带宽，单位：Mbps
        :rtype: int
        """
        return self._Bandwidth

    @Bandwidth.setter
    def Bandwidth(self, Bandwidth):
        self._Bandwidth = Bandwidth

    @property
    def Rules(self):
        """公网访问规则
        :rtype: list of PublicAccessRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Bandwidth = params.get("Bandwidth")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PublicAccessRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInsPublicEndpointResponse(AbstractModel):
    """ModifyInsPublicEndpoint返回参数结构体

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


class ModifyInstanceCertBindingRequest(AbstractModel):
    """ModifyInstanceCertBinding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _SSLServerCertId: 服务端证书id
        :type SSLServerCertId: str
        :param _SSLCaCertId: CA证书id
        :type SSLCaCertId: str
        :param _X509Mode: 加密通信方式
TLS：单向证书认证
mTLS：双向证书认证
BYOC：一设备一证书认证
        :type X509Mode: str
        :param _DeviceCertificateProvisionType: 设备证书注册类型：
JITP，自动注册；
MANUAL 手动注册
        :type DeviceCertificateProvisionType: str
        :param _AutomaticActivation: 是否自动激活，默认为false
        :type AutomaticActivation: bool
        """
        self._InstanceId = None
        self._SSLServerCertId = None
        self._SSLCaCertId = None
        self._X509Mode = None
        self._DeviceCertificateProvisionType = None
        self._AutomaticActivation = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def SSLServerCertId(self):
        """服务端证书id
        :rtype: str
        """
        return self._SSLServerCertId

    @SSLServerCertId.setter
    def SSLServerCertId(self, SSLServerCertId):
        self._SSLServerCertId = SSLServerCertId

    @property
    def SSLCaCertId(self):
        """CA证书id
        :rtype: str
        """
        return self._SSLCaCertId

    @SSLCaCertId.setter
    def SSLCaCertId(self, SSLCaCertId):
        self._SSLCaCertId = SSLCaCertId

    @property
    def X509Mode(self):
        """加密通信方式
TLS：单向证书认证
mTLS：双向证书认证
BYOC：一设备一证书认证
        :rtype: str
        """
        return self._X509Mode

    @X509Mode.setter
    def X509Mode(self, X509Mode):
        self._X509Mode = X509Mode

    @property
    def DeviceCertificateProvisionType(self):
        """设备证书注册类型：
JITP，自动注册；
MANUAL 手动注册
        :rtype: str
        """
        return self._DeviceCertificateProvisionType

    @DeviceCertificateProvisionType.setter
    def DeviceCertificateProvisionType(self, DeviceCertificateProvisionType):
        self._DeviceCertificateProvisionType = DeviceCertificateProvisionType

    @property
    def AutomaticActivation(self):
        """是否自动激活，默认为false
        :rtype: bool
        """
        return self._AutomaticActivation

    @AutomaticActivation.setter
    def AutomaticActivation(self, AutomaticActivation):
        self._AutomaticActivation = AutomaticActivation


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._SSLServerCertId = params.get("SSLServerCertId")
        self._SSLCaCertId = params.get("SSLCaCertId")
        self._X509Mode = params.get("X509Mode")
        self._DeviceCertificateProvisionType = params.get("DeviceCertificateProvisionType")
        self._AutomaticActivation = params.get("AutomaticActivation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceCertBindingResponse(AbstractModel):
    """ModifyInstanceCertBinding返回参数结构体

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


class ModifyInstanceRequest(AbstractModel):
    """ModifyInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Name: 要修改实例名称，不能为空, 3-64个字符，只能包含数字、字母、“-”和“_”。
        :type Name: str
        :param _Remark: 要修改的备注信息，最多64个字符。
        :type Remark: str
        :param _SkuCode: 需要变更的配置规格
基础版和增强版集群不能升配到铂金版规格，铂金版集群不能降配至基础版和增强版规格。
        :type SkuCode: str
        :param _DeviceCertificateProvisionType: 客户端证书注册方式：
JITP：自动注册
API：手动通过API注册
        :type DeviceCertificateProvisionType: str
        :param _AutomaticActivation: 自动注册证书是否自动激活
        :type AutomaticActivation: bool
        :param _AuthorizationPolicy: 授权策略开关
        :type AuthorizationPolicy: bool
        """
        self._InstanceId = None
        self._Name = None
        self._Remark = None
        self._SkuCode = None
        self._DeviceCertificateProvisionType = None
        self._AutomaticActivation = None
        self._AuthorizationPolicy = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Name(self):
        """要修改实例名称，不能为空, 3-64个字符，只能包含数字、字母、“-”和“_”。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """要修改的备注信息，最多64个字符。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SkuCode(self):
        """需要变更的配置规格
基础版和增强版集群不能升配到铂金版规格，铂金版集群不能降配至基础版和增强版规格。
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def DeviceCertificateProvisionType(self):
        """客户端证书注册方式：
JITP：自动注册
API：手动通过API注册
        :rtype: str
        """
        return self._DeviceCertificateProvisionType

    @DeviceCertificateProvisionType.setter
    def DeviceCertificateProvisionType(self, DeviceCertificateProvisionType):
        self._DeviceCertificateProvisionType = DeviceCertificateProvisionType

    @property
    def AutomaticActivation(self):
        """自动注册证书是否自动激活
        :rtype: bool
        """
        return self._AutomaticActivation

    @AutomaticActivation.setter
    def AutomaticActivation(self, AutomaticActivation):
        self._AutomaticActivation = AutomaticActivation

    @property
    def AuthorizationPolicy(self):
        """授权策略开关
        :rtype: bool
        """
        return self._AuthorizationPolicy

    @AuthorizationPolicy.setter
    def AuthorizationPolicy(self, AuthorizationPolicy):
        self._AuthorizationPolicy = AuthorizationPolicy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._SkuCode = params.get("SkuCode")
        self._DeviceCertificateProvisionType = params.get("DeviceCertificateProvisionType")
        self._AutomaticActivation = params.get("AutomaticActivation")
        self._AuthorizationPolicy = params.get("AuthorizationPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstanceResponse(AbstractModel):
    """ModifyInstance返回参数结构体

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


class ModifyJWKSAuthenticatorRequest(AbstractModel):
    """ModifyJWKSAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Endpoint: 端点
        :type Endpoint: str
        :param _Status: 认证器状态：open-启用；close-关闭
        :type Status: str
        :param _RefreshInterval: 刷新时间
        :type RefreshInterval: int
        :param _Text: JSKS文本
        :type Text: str
        :param _From: 设备连接时传递jwt的key；username-使用用户名字段传递；password-使用密码字段传递
        :type From: str
        :param _Remark: 说明
        :type Remark: str
        """
        self._InstanceId = None
        self._Endpoint = None
        self._Status = None
        self._RefreshInterval = None
        self._Text = None
        self._From = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Endpoint(self):
        """端点
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def Status(self):
        """认证器状态：open-启用；close-关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RefreshInterval(self):
        """刷新时间
        :rtype: int
        """
        return self._RefreshInterval

    @RefreshInterval.setter
    def RefreshInterval(self, RefreshInterval):
        self._RefreshInterval = RefreshInterval

    @property
    def Text(self):
        """JSKS文本
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def From(self):
        """设备连接时传递jwt的key；username-使用用户名字段传递；password-使用密码字段传递
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Remark(self):
        """说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Endpoint = params.get("Endpoint")
        self._Status = params.get("Status")
        self._RefreshInterval = params.get("RefreshInterval")
        self._Text = params.get("Text")
        self._From = params.get("From")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyJWKSAuthenticatorResponse(AbstractModel):
    """ModifyJWKSAuthenticator返回参数结构体

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


class ModifyJWTAuthenticatorRequest(AbstractModel):
    """ModifyJWTAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Algorithm: 算法：hmac-based，public-key
        :type Algorithm: str
        :param _From: 设备连接时传递jwt的key；
username-使用用户名字段传递；
password-使用密码字段传递
        :type From: str
        :param _Secret: 密码
        :type Secret: str
        :param _PublicKey: 公钥
        :type PublicKey: str
        :param _Text: JSKS文本
        :type Text: str
        :param _Remark: 说明
        :type Remark: str
        """
        self._InstanceId = None
        self._Algorithm = None
        self._From = None
        self._Secret = None
        self._PublicKey = None
        self._Text = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Algorithm(self):
        """算法：hmac-based，public-key
        :rtype: str
        """
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def From(self):
        """设备连接时传递jwt的key；
username-使用用户名字段传递；
password-使用密码字段传递
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Secret(self):
        """密码
        :rtype: str
        """
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret

    @property
    def PublicKey(self):
        """公钥
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Text(self):
        """JSKS文本
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Remark(self):
        """说明
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Algorithm = params.get("Algorithm")
        self._From = params.get("From")
        self._Secret = params.get("Secret")
        self._PublicKey = params.get("PublicKey")
        self._Text = params.get("Text")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyJWTAuthenticatorResponse(AbstractModel):
    """ModifyJWTAuthenticator返回参数结构体

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


class ModifyTopicRequest(AbstractModel):
    """ModifyTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Topic: 主题，不能为空，只能包含字母、数字、“-”及“_”，3-100 字符。
        :type Topic: str
        :param _Remark: 备注信息，最长 128 字符
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
        self._Remark = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        """主题，不能为空，只能包含字母、数字、“-”及“_”，3-100 字符。
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        """备注信息，最长 128 字符
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTopicResponse(AbstractModel):
    """ModifyTopic返回参数结构体

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


class ModifyUserRequest(AbstractModel):
    """ModifyUser请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Username: 用户名
        :type Username: str
        :param _Remark: 备注，长度不超过128个字符。
        :type Remark: str
        """
        self._InstanceId = None
        self._Username = None
        self._Remark = None

    @property
    def InstanceId(self):
        """实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Username(self):
        """用户名
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Remark(self):
        """备注，长度不超过128个字符。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Username = params.get("Username")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUserResponse(AbstractModel):
    """ModifyUser返回参数结构体

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


class PriceTag(AbstractModel):
    """价格标签信息

    """

    def __init__(self):
        r"""
        :param _Name: 计价名称
        :type Name: str
        :param _Category: 计价类别
        :type Category: str
        :param _Code: 计费项标签
        :type Code: str
        :param _Step: 步长
        :type Step: int
        """
        self._Name = None
        self._Category = None
        self._Code = None
        self._Step = None

    @property
    def Name(self):
        """计价名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Category(self):
        """计价类别
        :rtype: str
        """
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category

    @property
    def Code(self):
        """计费项标签
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Step(self):
        """步长
        :rtype: int
        """
        return self._Step

    @Step.setter
    def Step(self, Step):
        self._Step = Step


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Category = params.get("Category")
        self._Code = params.get("Code")
        self._Step = params.get("Step")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProductSkuItem(AbstractModel):
    """MQTT ProductSkuItem

    """

    def __init__(self):
        r"""
        :param _InstanceType: 规格类型
BASIC：基础版
PRO ：专业版
        :type InstanceType: str
        :param _SkuCode: 规格代码
        :type SkuCode: str
        :param _OnSale: 是否售卖
        :type OnSale: bool
        :param _TopicNumLimit: topic num限制
        :type TopicNumLimit: int
        :param _TpsLimit: tps
        :type TpsLimit: int
        :param _ClientNumLimit: 客户端连接数
        :type ClientNumLimit: int
        :param _MaxSubscriptionPerClient: 单客户端最大订阅数
        :type MaxSubscriptionPerClient: int
        :param _AuthorizationPolicyLimit: 授权规则条数
        :type AuthorizationPolicyLimit: int
        :param _PriceTags: 计费项信息
        :type PriceTags: list of PriceTag
        """
        self._InstanceType = None
        self._SkuCode = None
        self._OnSale = None
        self._TopicNumLimit = None
        self._TpsLimit = None
        self._ClientNumLimit = None
        self._MaxSubscriptionPerClient = None
        self._AuthorizationPolicyLimit = None
        self._PriceTags = None

    @property
    def InstanceType(self):
        """规格类型
BASIC：基础版
PRO ：专业版
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SkuCode(self):
        """规格代码
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def OnSale(self):
        """是否售卖
        :rtype: bool
        """
        return self._OnSale

    @OnSale.setter
    def OnSale(self, OnSale):
        self._OnSale = OnSale

    @property
    def TopicNumLimit(self):
        """topic num限制
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def TpsLimit(self):
        """tps
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ClientNumLimit(self):
        """客户端连接数
        :rtype: int
        """
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def MaxSubscriptionPerClient(self):
        """单客户端最大订阅数
        :rtype: int
        """
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def AuthorizationPolicyLimit(self):
        """授权规则条数
        :rtype: int
        """
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def PriceTags(self):
        """计费项信息
        :rtype: list of PriceTag
        """
        return self._PriceTags

    @PriceTags.setter
    def PriceTags(self, PriceTags):
        self._PriceTags = PriceTags


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._SkuCode = params.get("SkuCode")
        self._OnSale = params.get("OnSale")
        self._TopicNumLimit = params.get("TopicNumLimit")
        self._TpsLimit = params.get("TpsLimit")
        self._ClientNumLimit = params.get("ClientNumLimit")
        self._MaxSubscriptionPerClient = params.get("MaxSubscriptionPerClient")
        self._AuthorizationPolicyLimit = params.get("AuthorizationPolicyLimit")
        if params.get("PriceTags") is not None:
            self._PriceTags = []
            for item in params.get("PriceTags"):
                obj = PriceTag()
                obj._deserialize(item)
                self._PriceTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicAccessRule(AbstractModel):
    """公网访问安全规则

    """

    def __init__(self):
        r"""
        :param _IpRule: ip网段信息
        :type IpRule: str
        :param _Allow: 允许或者拒绝
        :type Allow: bool
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._IpRule = None
        self._Allow = None
        self._Remark = None

    @property
    def IpRule(self):
        """ip网段信息
        :rtype: str
        """
        return self._IpRule

    @IpRule.setter
    def IpRule(self, IpRule):
        self._IpRule = IpRule

    @property
    def Allow(self):
        """允许或者拒绝
        :rtype: bool
        """
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def Remark(self):
        """备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark


    def _deserialize(self, params):
        self._IpRule = params.get("IpRule")
        self._Allow = params.get("Allow")
        self._Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMessageRequest(AbstractModel):
    """PublishMessage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Payload: 消息负载 Payload，是消息的实际内容，需要按 encoding 指定的编码方式进行编码
        :type Payload: str
        :param _TargetTopic: 消息目的主题，该参数与 TargetClientId 二选一
        :type TargetTopic: str
        :param _TargetClientId: 消息目的客户端 ID，该参数与 TargetTopic 二选一
        :type TargetClientId: str
        :param _Encoding: 消息 payload 编码，可选 plain 或 base64，默认为 plain（即不编码）
        :type Encoding: str
        :param _Qos: 消息的服务质量等级，默认为 1
QoS 0（至多一次）消息发送后，不保证接收方一定收到，也不要求接收方确认。
QoS 1（至少一次）消息至少被接收方成功接收一次，但可能重复。
QoS 2（恰好一次）消息确保被接收方接收且仅接收一次，无重复。
        :type Qos: int
        :param _Retain: 是否为保留消息，默认为 false，且仅支持发布到主题的消息设置为 true
        :type Retain: bool
        """
        self._InstanceId = None
        self._Payload = None
        self._TargetTopic = None
        self._TargetClientId = None
        self._Encoding = None
        self._Qos = None
        self._Retain = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Payload(self):
        """消息负载 Payload，是消息的实际内容，需要按 encoding 指定的编码方式进行编码
        :rtype: str
        """
        return self._Payload

    @Payload.setter
    def Payload(self, Payload):
        self._Payload = Payload

    @property
    def TargetTopic(self):
        """消息目的主题，该参数与 TargetClientId 二选一
        :rtype: str
        """
        return self._TargetTopic

    @TargetTopic.setter
    def TargetTopic(self, TargetTopic):
        self._TargetTopic = TargetTopic

    @property
    def TargetClientId(self):
        """消息目的客户端 ID，该参数与 TargetTopic 二选一
        :rtype: str
        """
        return self._TargetClientId

    @TargetClientId.setter
    def TargetClientId(self, TargetClientId):
        self._TargetClientId = TargetClientId

    @property
    def Encoding(self):
        """消息 payload 编码，可选 plain 或 base64，默认为 plain（即不编码）
        :rtype: str
        """
        return self._Encoding

    @Encoding.setter
    def Encoding(self, Encoding):
        self._Encoding = Encoding

    @property
    def Qos(self):
        """消息的服务质量等级，默认为 1
QoS 0（至多一次）消息发送后，不保证接收方一定收到，也不要求接收方确认。
QoS 1（至少一次）消息至少被接收方成功接收一次，但可能重复。
QoS 2（恰好一次）消息确保被接收方接收且仅接收一次，无重复。
        :rtype: int
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Retain(self):
        """是否为保留消息，默认为 false，且仅支持发布到主题的消息设置为 true
        :rtype: bool
        """
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Payload = params.get("Payload")
        self._TargetTopic = params.get("TargetTopic")
        self._TargetClientId = params.get("TargetClientId")
        self._Encoding = params.get("Encoding")
        self._Qos = params.get("Qos")
        self._Retain = params.get("Retain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublishMessageResponse(AbstractModel):
    """PublishMessage返回参数结构体

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


class RegisterCaCertificateRequest(AbstractModel):
    """RegisterCaCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _CaCertificate: CA证书内容，自签CA可参考 [自定义 X.509 证书实现 “一机一证”](https://cloud.tencent.com/document/product/1778/114817) 签发自签CA
        :type CaCertificate: str
        :param _VerificationCertificate: 验证证书内容，可参考 [自定义 X.509 证书实现 “一机一证”](https://cloud.tencent.com/document/product/1778/114817) 手动注册CA证书章节
        :type VerificationCertificate: str
        :param _Format: 证书格式，不传默认PEM格式，当前仅支持PEM格式
        :type Format: str
        :param _Status: 证书状态，不传默认ACTIVE状态
    ACTIVE：激活
    INACTIVE：未激活
        :type Status: str
        """
        self._InstanceId = None
        self._CaCertificate = None
        self._VerificationCertificate = None
        self._Format = None
        self._Status = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CaCertificate(self):
        """CA证书内容，自签CA可参考 [自定义 X.509 证书实现 “一机一证”](https://cloud.tencent.com/document/product/1778/114817) 签发自签CA
        :rtype: str
        """
        return self._CaCertificate

    @CaCertificate.setter
    def CaCertificate(self, CaCertificate):
        self._CaCertificate = CaCertificate

    @property
    def VerificationCertificate(self):
        """验证证书内容，可参考 [自定义 X.509 证书实现 “一机一证”](https://cloud.tencent.com/document/product/1778/114817) 手动注册CA证书章节
        :rtype: str
        """
        return self._VerificationCertificate

    @VerificationCertificate.setter
    def VerificationCertificate(self, VerificationCertificate):
        self._VerificationCertificate = VerificationCertificate

    @property
    def Format(self):
        """证书格式，不传默认PEM格式，当前仅支持PEM格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Status(self):
        """证书状态，不传默认ACTIVE状态
    ACTIVE：激活
    INACTIVE：未激活
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._CaCertificate = params.get("CaCertificate")
        self._VerificationCertificate = params.get("VerificationCertificate")
        self._Format = params.get("Format")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCaCertificateResponse(AbstractModel):
    """RegisterCaCertificate返回参数结构体

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


class RegisterDeviceCertificateRequest(AbstractModel):
    """RegisterDeviceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _DeviceCertificate: 设备证书内容，可参考 [使用 CA 证书生成服务端/客户端证书](https://cloud.tencent.com/document/product/1778/114817#aab79cc8-a148-412e-beb8-9c9e158eb944) 生成
        :type DeviceCertificate: str
        :param _CaSn: 关联的CA证书SN
        :type CaSn: str
        :param _ClientId: 客户端ID，需要关联该证书的客户端ID。根据实际业务使用填写
        :type ClientId: str
        :param _Format: 证书格式，默认为PEM，当前仅支持PEM格式
        :type Format: str
        :param _Status:  客户端证书状态，默认激活状态（ACTIVE）
ACTIVE：激活     
INACTIVE：未激活     
REVOKED：吊销 
PENDING_ACTIVATION：注册待激活
        :type Status: str
        """
        self._InstanceId = None
        self._DeviceCertificate = None
        self._CaSn = None
        self._ClientId = None
        self._Format = None
        self._Status = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceCertificate(self):
        """设备证书内容，可参考 [使用 CA 证书生成服务端/客户端证书](https://cloud.tencent.com/document/product/1778/114817#aab79cc8-a148-412e-beb8-9c9e158eb944) 生成
        :rtype: str
        """
        return self._DeviceCertificate

    @DeviceCertificate.setter
    def DeviceCertificate(self, DeviceCertificate):
        self._DeviceCertificate = DeviceCertificate

    @property
    def CaSn(self):
        """关联的CA证书SN
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def ClientId(self):
        """客户端ID，需要关联该证书的客户端ID。根据实际业务使用填写
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Format(self):
        """证书格式，默认为PEM，当前仅支持PEM格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Status(self):
        """ 客户端证书状态，默认激活状态（ACTIVE）
ACTIVE：激活     
INACTIVE：未激活     
REVOKED：吊销 
PENDING_ACTIVATION：注册待激活
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DeviceCertificate = params.get("DeviceCertificate")
        self._CaSn = params.get("CaSn")
        self._ClientId = params.get("ClientId")
        self._Format = params.get("Format")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterDeviceCertificateResponse(AbstractModel):
    """RegisterDeviceCertificate返回参数结构体

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


class RevokedDeviceCertificateRequest(AbstractModel):
    """RevokedDeviceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _DeviceCertificateSn: 设备证书序列号
        :type DeviceCertificateSn: str
        """
        self._InstanceId = None
        self._DeviceCertificateSn = None

    @property
    def InstanceId(self):
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceCertificateSn(self):
        """设备证书序列号
        :rtype: str
        """
        return self._DeviceCertificateSn

    @DeviceCertificateSn.setter
    def DeviceCertificateSn(self, DeviceCertificateSn):
        self._DeviceCertificateSn = DeviceCertificateSn


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._DeviceCertificateSn = params.get("DeviceCertificateSn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokedDeviceCertificateResponse(AbstractModel):
    """RevokedDeviceCertificate返回参数结构体

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


class Tag(AbstractModel):
    """标签数据

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签名称
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签名称
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
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
        


class TagFilter(AbstractModel):
    """标签过滤器

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键名称
        :type TagKey: str
        :param _TagValues: 标签键名称
        :type TagValues: list of str
        """
        self._TagKey = None
        self._TagValues = None

    @property
    def TagKey(self):
        """标签键名称
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValues(self):
        """标签键名称
        :rtype: list of str
        """
        return self._TagValues

    @TagValues.setter
    def TagValues(self, TagValues):
        self._TagValues = TagValues


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValues = params.get("TagValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuthorizationPolicyPriorityRequest(AbstractModel):
    """UpdateAuthorizationPolicyPriority请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :type InstanceId: str
        :param _Priorities: 策略ID和优先级
        :type Priorities: list of AuthorizationPolicyPriority
        """
        self._InstanceId = None
        self._Priorities = None

    @property
    def InstanceId(self):
        """腾讯云MQTT实例ID，从 [DescribeInstanceList](https://cloud.tencent.com/document/api/1778/111029)接口或控制台获得。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Priorities(self):
        """策略ID和优先级
        :rtype: list of AuthorizationPolicyPriority
        """
        return self._Priorities

    @Priorities.setter
    def Priorities(self, Priorities):
        self._Priorities = Priorities


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("Priorities") is not None:
            self._Priorities = []
            for item in params.get("Priorities"):
                obj = AuthorizationPolicyPriority()
                obj._deserialize(item)
                self._Priorities.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateAuthorizationPolicyPriorityResponse(AbstractModel):
    """UpdateAuthorizationPolicyPriority返回参数结构体

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


class VpcInfo(AbstractModel):
    """VPC信息

    """

    def __init__(self):
        r"""
        :param _VpcId: VPC ID
        :type VpcId: str
        :param _SubnetId: 子网ID
        :type SubnetId: str
        """
        self._VpcId = None
        self._SubnetId = None

    @property
    def VpcId(self):
        """VPC ID
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网ID
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        