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
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _CaSn: 证书序列号
        :type CaSn: str
        """
        self._InstanceId = None
        self._CaSn = None

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
    def CaSn(self):
        """证书序列号
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
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群id
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
        :param _Id: 规则ID
        :type Id: int
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _PolicyName: 规则名
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyName: str
        :param _Version: 规则语法版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: int
        :param _Priority: 越小越优先
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        :param _Effect: allow/deny
注意：此字段可能返回 null，表示取不到有效值。
        :type Effect: str
        :param _Actions: connect、pub、sub
注意：此字段可能返回 null，表示取不到有效值。
        :type Actions: str
        :param _Resources: 资源
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: str
        :param _ClientId: client
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        :param _Username: 用户
注意：此字段可能返回 null，表示取不到有效值。
        :type Username: str
        :param _Ip: IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Qos: 0，1，2
注意：此字段可能返回 null，表示取不到有效值。
        :type Qos: str
        :param _Retain: 1：表示匹配retain消息
2：表示匹配非retain消息
3：表示匹配retain和非retain消息
注意：此字段可能返回 null，表示取不到有效值。
        :type Retain: int
        :param _Remark: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _CreatedTime: 1713164969433
        :type CreatedTime: int
        :param _UpdateTime: 1713164969433
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
        """规则ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

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
    def PolicyName(self):
        """规则名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Version(self):
        """规则语法版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Priority(self):
        """越小越优先
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Effect(self):
        """allow/deny
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect

    @property
    def Actions(self):
        """connect、pub、sub
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Resources(self):
        """资源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def ClientId(self):
        """client
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Username(self):
        """用户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Ip(self):
        """IP地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Qos(self):
        """0，1，2
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Retain(self):
        """1：表示匹配retain消息
2：表示匹配非retain消息
3：表示匹配retain和非retain消息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain

    @property
    def Remark(self):
        """描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        """1713164969433
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """1713164969433
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
        :param _Id: 策略id
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Priority: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        """
        self._Id = None
        self._Priority = None

    @property
    def Id(self):
        """策略id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Priority(self):
        """优先级
注意：此字段可能返回 null，表示取不到有效值。
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
        


class CaCertificateItem(AbstractModel):
    """CA证书信息

    """

    def __init__(self):
        r"""
        :param _CaCn: common name
        :type CaCn: str
        :param _CaCertificate: 证书内容
        :type CaCertificate: str
        :param _CaSn: 证书序列号
        :type CaSn: str
        :param _Format: 证书格式
        :type Format: str
        :param _VerificationCertificate: 验证证书内容
        :type VerificationCertificate: str
        :param _Status: ca状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _LastActivationTime: 上次激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastActivationTime: int
        :param _CreatedTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: int
        :param _UpdateTime: 预销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _LastInactivationTime: 上次去激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastInactivationTime: int
        :param _CaIssuerCn: Ca证书颁发者CN
注意：此字段可能返回 null，表示取不到有效值。
        :type CaIssuerCn: str
        :param _NotBeforeTime: 生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type NotBeforeTime: int
        :param _NotAfterTime: 失效时间
注意：此字段可能返回 null，表示取不到有效值。
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
        """common name
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
        """证书格式
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
        """ca状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LastActivationTime(self):
        """上次激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastActivationTime

    @LastActivationTime.setter
    def LastActivationTime(self, LastActivationTime):
        self._LastActivationTime = LastActivationTime

    @property
    def CreatedTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """预销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def LastInactivationTime(self):
        """上次去激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastInactivationTime

    @LastInactivationTime.setter
    def LastInactivationTime(self, LastInactivationTime):
        self._LastInactivationTime = LastInactivationTime

    @property
    def CaIssuerCn(self):
        """Ca证书颁发者CN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CaIssuerCn

    @CaIssuerCn.setter
    def CaIssuerCn(self, CaIssuerCn):
        self._CaIssuerCn = CaIssuerCn

    @property
    def NotBeforeTime(self):
        """生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NotBeforeTime

    @NotBeforeTime.setter
    def NotBeforeTime(self, NotBeforeTime):
        self._NotBeforeTime = NotBeforeTime

    @property
    def NotAfterTime(self):
        """失效时间
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _Retain: 1,匹配保留消息；2,匹配非保留消息，3.匹配所有消息
        :type Retain: int
        :param _Qos: 0、1、2
        :type Qos: str
        :param _Resources: 资源
        :type Resources: str
        :param _Username: 用户名
        :type Username: str
        :param _ClientId: 客户端
        :type ClientId: str
        :param _Ip: IP地址
        :type Ip: str
        :param _Remark: 备注信息
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
    def Retain(self):
        """1,匹配保留消息；2,匹配非保留消息，3.匹配所有消息
        :rtype: int
        """
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain

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
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
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
    def Topic(self):
        """主题
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Username: 用户名
        :type Username: str
        :param _Password: 密码，该字段为空时候则后端会默认生成
        :type Password: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._Username = None
        self._Password = None
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
        """密码，该字段为空时候则后端会默认生成
        :rtype: str
        """
        return self._Password

    @Password.setter
    def Password(self, Password):
        self._Password = Password

    @property
    def Remark(self):
        """备注
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
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _CaSn: 证书序列号
        :type CaSn: str
        """
        self._InstanceId = None
        self._CaSn = None

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
    def CaSn(self):
        """证书序列号
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Type: 认证器类型:
JWT：JWT认证器
JWKS：JWKS认证器
BYOC：一端一证认证器
        :type Type: str
        """
        self._InstanceId = None
        self._Type = None

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
    def Type(self):
        """认证器类型:
JWT：JWT认证器
JWKS：JWKS认证器
BYOC：一端一证认证器
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Id: 策略规则id
        :type Id: int
        """
        self._InstanceId = None
        self._Id = None

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
    def Id(self):
        """策略规则id
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
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _CaSn: 证书序列号
        :type CaSn: str
        """
        self._InstanceId = None
        self._CaSn = None

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
    def CaSn(self):
        """证书序列号
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Type: 认证器类型: JWT：JWT认证器 JWKS：JWKS认证器 HTTP:HTTP认证器
        :type Type: str
        """
        self._InstanceId = None
        self._Type = None

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
    def Type(self):
        """认证器类型: JWT：JWT认证器 JWKS：JWKS认证器 HTTP:HTTP认证器
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
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群ID
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
        :param _CaSn: ca证书sn
        :type CaSn: str
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._CaSn = None
        self._InstanceId = None

    @property
    def CaSn(self):
        """ca证书sn
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def InstanceId(self):
        """集群id
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
        :param _CreatedTime: 创建时间
        :type CreatedTime: int
        :param _UpdateTime: 上次更新时间
        :type UpdateTime: int
        :param _NotAfterTime: 失效日期
        :type NotAfterTime: int
        :param _LastActivationTime: 上次激活时间
        :type LastActivationTime: int
        :param _LastInactivationTime: 上次吊销时间
        :type LastInactivationTime: int
        :param _Status: 证书状态
        :type Status: str
        :param _CaSn: 证书序列号
        :type CaSn: str
        :param _CaCn: common name
        :type CaCn: str
        :param _CaCertificate: 证书内容
        :type CaCertificate: str
        :param _Format: 证书格式
        :type Format: str
        :param _CaIssuerCn: Ca证书颁发者CN
注意：此字段可能返回 null，表示取不到有效值。
        :type CaIssuerCn: str
        :param _NotBeforeTime: 生效开始时间
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
        """创建时间
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """上次更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def NotAfterTime(self):
        """失效日期
        :rtype: int
        """
        return self._NotAfterTime

    @NotAfterTime.setter
    def NotAfterTime(self, NotAfterTime):
        self._NotAfterTime = NotAfterTime

    @property
    def LastActivationTime(self):
        """上次激活时间
        :rtype: int
        """
        return self._LastActivationTime

    @LastActivationTime.setter
    def LastActivationTime(self, LastActivationTime):
        self._LastActivationTime = LastActivationTime

    @property
    def LastInactivationTime(self):
        """上次吊销时间
        :rtype: int
        """
        return self._LastInactivationTime

    @LastInactivationTime.setter
    def LastInactivationTime(self, LastInactivationTime):
        self._LastInactivationTime = LastInactivationTime

    @property
    def Status(self):
        """证书状态
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
        """common name
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
        """证书格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def CaIssuerCn(self):
        """Ca证书颁发者CN
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CaIssuerCn

    @CaIssuerCn.setter
    def CaIssuerCn(self, CaIssuerCn):
        self._CaIssuerCn = CaIssuerCn

    @property
    def NotBeforeTime(self):
        """生效开始时间
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
        :param _InstanceId: 集群ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """集群ID
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


class DescribeDeviceCertificateRequest(AbstractModel):
    """DescribeDeviceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeviceCertificateSn: 设备证书sn
        :type DeviceCertificateSn: str
        :param _InstanceId: 集群id
        :type InstanceId: str
        """
        self._DeviceCertificateSn = None
        self._InstanceId = None

    @property
    def DeviceCertificateSn(self):
        """设备证书sn
        :rtype: str
        """
        return self._DeviceCertificateSn

    @DeviceCertificateSn.setter
    def DeviceCertificateSn(self, DeviceCertificateSn):
        self._DeviceCertificateSn = DeviceCertificateSn

    @property
    def InstanceId(self):
        """集群id
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
        :param _CreatedTime: 创建时间
        :type CreatedTime: int
        :param _UpdateTime: 上次更新时间
        :type UpdateTime: int
        :param _NotAfterTime: 证书失效日期
        :type NotAfterTime: int
        :param _LastActivationTime: 上次激活时间
        :type LastActivationTime: int
        :param _LastInactivationTime: 上次取消激活时间
        :type LastInactivationTime: int
        :param _Status: 证书状态
        :type Status: str
        :param _CaSn: Ca证书序列号
        :type CaSn: str
        :param _DeviceCertificateSn: 设备证书序列号
        :type DeviceCertificateSn: str
        :param _DeviceCertificate: 设备证书内容
        :type DeviceCertificate: str
        :param _DeviceCertificateCn: 设备证书common name
        :type DeviceCertificateCn: str
        :param _Format: 证书格式
        :type Format: str
        :param _ClientId: 客户端id
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        :param _CertificateSource:     API, 手动注册   
    JITP 自动注册
        :type CertificateSource: str
        :param _NotBeforeTime: 证书生效开始时间
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
        self._DeviceCertificateSn = None
        self._DeviceCertificate = None
        self._DeviceCertificateCn = None
        self._Format = None
        self._ClientId = None
        self._CertificateSource = None
        self._NotBeforeTime = None
        self._RequestId = None

    @property
    def CreatedTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """上次更新时间
        :rtype: int
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def NotAfterTime(self):
        """证书失效日期
        :rtype: int
        """
        return self._NotAfterTime

    @NotAfterTime.setter
    def NotAfterTime(self, NotAfterTime):
        self._NotAfterTime = NotAfterTime

    @property
    def LastActivationTime(self):
        """上次激活时间
        :rtype: int
        """
        return self._LastActivationTime

    @LastActivationTime.setter
    def LastActivationTime(self, LastActivationTime):
        self._LastActivationTime = LastActivationTime

    @property
    def LastInactivationTime(self):
        """上次取消激活时间
        :rtype: int
        """
        return self._LastInactivationTime

    @LastInactivationTime.setter
    def LastInactivationTime(self, LastInactivationTime):
        self._LastInactivationTime = LastInactivationTime

    @property
    def Status(self):
        """证书状态
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
        """证书格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def ClientId(self):
        """客户端id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def CertificateSource(self):
        """    API, 手动注册   
    JITP 自动注册
        :rtype: str
        """
        return self._CertificateSource

    @CertificateSource.setter
    def CertificateSource(self, CertificateSource):
        self._CertificateSource = CertificateSource

    @property
    def NotBeforeTime(self):
        """证书生效开始时间
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
        self._DeviceCertificateSn = params.get("DeviceCertificateSn")
        self._DeviceCertificate = params.get("DeviceCertificate")
        self._DeviceCertificateCn = params.get("DeviceCertificateCn")
        self._Format = params.get("Format")
        self._ClientId = params.get("ClientId")
        self._CertificateSource = params.get("CertificateSource")
        self._NotBeforeTime = params.get("NotBeforeTime")
        self._RequestId = params.get("RequestId")


class DescribeDeviceCertificatesRequest(AbstractModel):
    """DescribeDeviceCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 集群ID
        :type InstanceId: str
        :param _Filters: 过滤器支持ClientId、CaSn、DeviceCertificateSn、Status搜索
        :type Filters: list of Filter
        :param _Limit: 分页limit
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _OrderBy: CREATE_TIME_DESC, 创建时间降序
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
        """集群ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        """过滤器支持ClientId、CaSn、DeviceCertificateSn、Status搜索
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """分页limit
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OrderBy(self):
        """CREATE_TIME_DESC, 创建时间降序
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
        :param _Data: 设备证书
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
        """设备证书
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
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
        :param _Bandwidth: 带宽
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
        """带宽
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


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件列表,支持以下子弹
InstanceName：集群名模糊搜索
InstanceId：集群id精确搜索
InstanceStatus：集群状态搜索
        :type Filters: list of Filter
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
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
        """查询条件列表,支持以下子弹
InstanceName：集群名模糊搜索
InstanceId：集群id精确搜索
InstanceStatus：集群状态搜索
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询结果限制数量
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """实例ID
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
        :param _InstanceStatus: 实例状态
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
        :param _RenewFlag: 是否自动续费
        :type RenewFlag: int
        :param _PayMode: 计费模式， POSTPAID，按量计费 PREPAID，包年包月
        :type PayMode: str
        :param _ExpiryTime: 到期时间，秒为单位
        :type ExpiryTime: int
        :param _DestroyTime: 预销毁时间
        :type DestroyTime: int
        :param _X509Mode: TLS,单向认证    mTLS,双向认证    BYOC;一机一证
        :type X509Mode: str
        :param _MaxCaNum: 最大Ca配额
        :type MaxCaNum: int
        :param _RegistrationCode: 证书注册码
        :type RegistrationCode: str
        :param _MaxSubscription: 集群最大订阅数
        :type MaxSubscription: int
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
        self._RequestId = None

    @property
    def InstanceType(self):
        """实例类型
BASIC 基础版
PRO  专业版
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
        """实例状态
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
        """是否自动续费
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
        """到期时间，秒为单位
        :rtype: int
        """
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def DestroyTime(self):
        """预销毁时间
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _MQTTProductSkuList: mqtt商品配置信息
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def MQTTProductSkuList(self):
        """mqtt商品配置信息
注意：此字段可能返回 null，表示取不到有效值。
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


class DescribeTopicListRequest(AbstractModel):
    """DescribeTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Filters: 查询条件列表:
支持TopicName模糊查询
        :type Filters: list of Filter
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

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
        """查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询结果限制数量
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Filters: 查询条件列表支持字段
Username：Username模糊查询
        :type Filters: list of Filter
        :param _Offset: 查询起始位置
        :type Offset: int
        :param _Limit: 查询结果限制数量
        :type Limit: int
        """
        self._InstanceId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

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
    def Filters(self):
        """查询条件列表支持字段
Username：Username模糊查询
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """查询起始位置
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """查询结果限制数量
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientId: str
        :param _DeviceCertificate: 设备证书
        :type DeviceCertificate: str
        :param _DeviceCertificateSn: 设备证书Sn
        :type DeviceCertificateSn: str
        :param _DeviceCertificateCn: 设备证书Cn
        :type DeviceCertificateCn: str
        :param _CaSn: 签发ca的序列号
        :type CaSn: str
        :param _Format: 证书格式
        :type Format: str
        :param _Status: 证书状态
    ACTIVE,//激活
    INACTIVE,//未激活
    REVOKED,//吊销
    PENDING_ACTIVATION,//注册待激活
        :type Status: str
        :param _LastActivationTime: 上次激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastActivationTime: int
        :param _LastInactivationTime: 上次取消激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastInactivationTime: int
        :param _CreatedTime: 创建时间
        :type CreatedTime: int
        :param _UpdateTime: 预销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: int
        :param _CertificateSource: 证书来源：
API, 手动注册   
JITP 自动注册
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateSource: str
        :param _NotAfterTime: 证书失效日期
注意：此字段可能返回 null，表示取不到有效值。
        :type NotAfterTime: int
        :param _NotBeforeTime: 证书生效开始日期
注意：此字段可能返回 null，表示取不到有效值。
        :type NotBeforeTime: int
        """
        self._ClientId = None
        self._DeviceCertificate = None
        self._DeviceCertificateSn = None
        self._DeviceCertificateCn = None
        self._CaSn = None
        self._Format = None
        self._Status = None
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
注意：此字段可能返回 null，表示取不到有效值。
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
        """设备证书Sn
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
        """签发ca的序列号
        :rtype: str
        """
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def Format(self):
        """证书格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Status(self):
        """证书状态
    ACTIVE,//激活
    INACTIVE,//未激活
    REVOKED,//吊销
    PENDING_ACTIVATION,//注册待激活
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def LastActivationTime(self):
        """上次激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastActivationTime

    @LastActivationTime.setter
    def LastActivationTime(self, LastActivationTime):
        self._LastActivationTime = LastActivationTime

    @property
    def LastInactivationTime(self):
        """上次取消激活时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._LastInactivationTime

    @LastInactivationTime.setter
    def LastInactivationTime(self, LastInactivationTime):
        self._LastInactivationTime = LastInactivationTime

    @property
    def CreatedTime(self):
        """创建时间
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
        """预销毁时间
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertificateSource

    @CertificateSource.setter
    def CertificateSource(self, CertificateSource):
        self._CertificateSource = CertificateSource

    @property
    def NotAfterTime(self):
        """证书失效日期
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NotAfterTime

    @NotAfterTime.setter
    def NotAfterTime(self, NotAfterTime):
        self._NotAfterTime = NotAfterTime

    @property
    def NotBeforeTime(self):
        """证书生效开始日期
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _Type: 认证器类型: JWT：JWT认证器 JWKS：JWKS认证器 BYOC：一端一证认证器
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Config: 认证器配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Config: str
        :param _Status: 认证器状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _Remark: 说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._Type = None
        self._Config = None
        self._Status = None
        self._CreateTime = None
        self._Remark = None

    @property
    def Type(self):
        """认证器类型: JWT：JWT认证器 JWKS：JWKS认证器 BYOC：一端一证认证器
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Config(self):
        """认证器配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Status(self):
        """认证器状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
        """说明
注意：此字段可能返回 null，表示取不到有效值。
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
        


class MQTTEndpointItem(AbstractModel):
    """MQTTEndpoint

    """

    def __init__(self):
        r"""
        :param _Type: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Url: 接入点
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _VpcId: vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcId: str
        :param _SubnetId: 子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SubnetId: str
        :param _Host: 主机
注意：此字段可能返回 null，表示取不到有效值。
        :type Host: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Ip: 接入点ip
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Url(self):
        """接入点
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def VpcId(self):
        """vpc信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def SubnetId(self):
        """子网信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SubnetId

    @SubnetId.setter
    def SubnetId(self, SubnetId):
        self._SubnetId = SubnetId

    @property
    def Host(self):
        """主机
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def Port(self):
        """端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Ip(self):
        """接入点ip
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _InstanceType: 实例类型，
EXPERIMENT，体验版
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
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _TopicNum: 主题数量
        :type TopicNum: int
        :param _SkuCode: 商品规格
        :type SkuCode: str
        :param _TpsLimit: 弹性TPS限流值
注意：此字段可能返回 null，表示取不到有效值。
        :type TpsLimit: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param _MaxSubscriptionPerClient: 单客户端最大订阅数量
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSubscriptionPerClient: int
        :param _ClientNumLimit: 客户端连接数上线
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientNumLimit: int
        :param _RenewFlag: 是否自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewFlag: int
        :param _PayMode: 计费模式， POSTPAID，按量计费 PREPAID，包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :type PayMode: str
        :param _ExpiryTime: 到期时间，秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiryTime: int
        :param _DestroyTime: 预销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :type DestroyTime: int
        :param _AuthorizationPolicyLimit: 授权规则条数限制
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationPolicyLimit: int
        :param _MaxCaNum: 最大ca配额
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxCaNum: int
        :param _MaxSubscription: 最大订阅数
注意：此字段可能返回 null，表示取不到有效值。
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
        """实例类型，
EXPERIMENT，体验版
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MaxSubscriptionPerClient(self):
        """单客户端最大订阅数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def ClientNumLimit(self):
        """客户端连接数上线
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def RenewFlag(self):
        """是否自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        """计费模式， POSTPAID，按量计费 PREPAID，包年包月
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        """到期时间，秒为单位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def DestroyTime(self):
        """预销毁时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def AuthorizationPolicyLimit(self):
        """授权规则条数限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def MaxCaNum(self):
        """最大ca配额
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxCaNum

    @MaxCaNum.setter
    def MaxCaNum(self, MaxCaNum):
        self._MaxCaNum = MaxCaNum

    @property
    def MaxSubscription(self):
        """最大订阅数
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _CreatedTime: 创建时间，秒为单位
        :type CreatedTime: int
        :param _ModifiedTime: 修改时间，秒为单位
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
        """创建时间，秒为单位
        :rtype: int
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifiedTime(self):
        """修改时间，秒为单位
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Name: 要修改实例名称
        :type Name: str
        :param _Remark: 要修改的备注信息
        :type Remark: str
        :param _SkuCode: 要变更的配置规格
        :type SkuCode: str
        :param _DeviceCertificateProvisionType: 客户端证书注册方式：
JITP：自动注册
API：手动通过API注册
        :type DeviceCertificateProvisionType: str
        :param _AutomaticActivation: 自动注册证书是否自动激活
        :type AutomaticActivation: bool
        """
        self._InstanceId = None
        self._Name = None
        self._Remark = None
        self._SkuCode = None
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
    def Name(self):
        """要修改实例名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Remark(self):
        """要修改的备注信息
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def SkuCode(self):
        """要变更的配置规格
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


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Name = params.get("Name")
        self._Remark = params.get("Remark")
        self._SkuCode = params.get("SkuCode")
        self._DeviceCertificateProvisionType = params.get("DeviceCertificateProvisionType")
        self._AutomaticActivation = params.get("AutomaticActivation")
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Topic: 主题
        :type Topic: str
        :param _Remark: 备注信息
        :type Remark: str
        """
        self._InstanceId = None
        self._Topic = None
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
    def Topic(self):
        """主题
        :rtype: str
        """
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Username: 用户名
        :type Username: str
        :param _Remark: 备注
        :type Remark: str
        """
        self._InstanceId = None
        self._Username = None
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
        """备注
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceType: str
        :param _SkuCode: 规格代码
注意：此字段可能返回 null，表示取不到有效值。
        :type SkuCode: str
        :param _OnSale: 是否售卖
注意：此字段可能返回 null，表示取不到有效值。
        :type OnSale: bool
        :param _TopicNumLimit: topic num限制
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicNumLimit: int
        :param _TpsLimit: tps
注意：此字段可能返回 null，表示取不到有效值。
        :type TpsLimit: int
        :param _ClientNumLimit: 客户端连接数
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientNumLimit: int
        :param _MaxSubscriptionPerClient: 单客户端最大订阅数
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxSubscriptionPerClient: int
        :param _AuthorizationPolicyLimit: 授权规则条数
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthorizationPolicyLimit: int
        :param _PriceTags: 计费项信息
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def SkuCode(self):
        """规格代码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def OnSale(self):
        """是否售卖
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._OnSale

    @OnSale.setter
    def OnSale(self, OnSale):
        self._OnSale = OnSale

    @property
    def TopicNumLimit(self):
        """topic num限制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def TpsLimit(self):
        """tps
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def ClientNumLimit(self):
        """客户端连接数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def MaxSubscriptionPerClient(self):
        """单客户端最大订阅数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def AuthorizationPolicyLimit(self):
        """授权规则条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def PriceTags(self):
        """计费项信息
注意：此字段可能返回 null，表示取不到有效值。
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
注意：此字段可能返回 null，表示取不到有效值。
        :type IpRule: str
        :param _Allow: 允许或者拒绝
注意：此字段可能返回 null，表示取不到有效值。
        :type Allow: bool
        :param _Remark: 备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self._IpRule = None
        self._Allow = None
        self._Remark = None

    @property
    def IpRule(self):
        """ip网段信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IpRule

    @IpRule.setter
    def IpRule(self, IpRule):
        self._IpRule = IpRule

    @property
    def Allow(self):
        """允许或者拒绝
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Allow

    @Allow.setter
    def Allow(self, Allow):
        self._Allow = Allow

    @property
    def Remark(self):
        """备注信息
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Payload: 消息 payload，需要按 encoding 指定的编码方式进行编码
        :type Payload: str
        :param _TargetTopic: 消息目的主题，该参数与 TargetClientId 二选一
        :type TargetTopic: str
        :param _TargetClientId: 消息目的客户端 ID，该参数与 TargetTopic 二选一
        :type TargetClientId: str
        :param _Encoding: 消息 payload 编码，可选 plain 或 base64，默认为 plain（即不编码）
        :type Encoding: str
        :param _Qos: 消息的服务质量等级，默认为 1
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
        """实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Payload(self):
        """消息 payload，需要按 encoding 指定的编码方式进行编码
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
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _CaCertificate: CA证书
        :type CaCertificate: str
        :param _VerificationCertificate: 验证证书
        :type VerificationCertificate: str
        :param _Format: 证书格式，不传默认PEM格式
        :type Format: str
        :param _Status: 证书状态，不传默认ACTIVE状态
    ACTIVE,//激活
    INACTIVE,//未激活
    REVOKED,//吊销
    PENDING_ACTIVATION,//注册待激活
        :type Status: str
        """
        self._InstanceId = None
        self._CaCertificate = None
        self._VerificationCertificate = None
        self._Format = None
        self._Status = None

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
    def CaCertificate(self):
        """CA证书
        :rtype: str
        """
        return self._CaCertificate

    @CaCertificate.setter
    def CaCertificate(self, CaCertificate):
        self._CaCertificate = CaCertificate

    @property
    def VerificationCertificate(self):
        """验证证书
        :rtype: str
        """
        return self._VerificationCertificate

    @VerificationCertificate.setter
    def VerificationCertificate(self, VerificationCertificate):
        self._VerificationCertificate = VerificationCertificate

    @property
    def Format(self):
        """证书格式，不传默认PEM格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Status(self):
        """证书状态，不传默认ACTIVE状态
    ACTIVE,//激活
    INACTIVE,//未激活
    REVOKED,//吊销
    PENDING_ACTIVATION,//注册待激活
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
        :param _InstanceId: 集群id
        :type InstanceId: str
        :param _DeviceCertificate: 设备证书
        :type DeviceCertificate: str
        :param _CaSn: 关联的CA证书SN
        :type CaSn: str
        :param _ClientId: 客户端ID
        :type ClientId: str
        :param _Format: 证书格式
        :type Format: str
        :param _Status:     ACTIVE,//激活     INACTIVE,//未激活     REVOKED,//吊销     PENDING_ACTIVATION,//注册待激活
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
        """集群id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

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
        """客户端ID
        :rtype: str
        """
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Format(self):
        """证书格式
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Status(self):
        """    ACTIVE,//激活     INACTIVE,//未激活     REVOKED,//吊销     PENDING_ACTIVATION,//注册待激活
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
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
注意：此字段可能返回 null，表示取不到有效值。
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
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Priorities: 策略ID和优先级
        :type Priorities: list of AuthorizationPolicyPriority
        """
        self._InstanceId = None
        self._Priorities = None

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
        