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
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Qos(self):
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Retain(self):
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdateTime(self):
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
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Priority(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyVersion(self):
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Retain(self):
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain

    @property
    def Qos(self):
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Remark(self):
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
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
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
        :param _From: 设备连接时传递jwt的key；username-使用用户名字段传递；password-使用密码字段传递
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def RefreshInterval(self):
        return self._RefreshInterval

    @RefreshInterval.setter
    def RefreshInterval(self, RefreshInterval):
        self._RefreshInterval = RefreshInterval

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def From(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Secret(self):
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Remark(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Topic = params.get("Topic")
        self._RequestId = params.get("RequestId")


class DeleteAuthenticatorRequest(AbstractModel):
    """DeleteAuthenticator请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Type: 认证器类型
        :type Type: str
        """
        self._InstanceId = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Id(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
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
        :param _Type: 认证器类型
        :type Type: str
        """
        self._InstanceId = None
        self._Type = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Type(self):
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
        return self._Authenticators

    @Authenticators.setter
    def Authenticators(self, Authenticators):
        self._Authenticators = Authenticators

    @property
    def RequestId(self):
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
            self._Data = []
            for item in params.get("Data"):
                obj = AuthorizationPolicyItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInstanceListRequest(AbstractModel):
    """DescribeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 查询条件列表
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
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
    def TagFilters(self):
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
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        :param _InstanceType: 实例类型，
EXPERIMENT 体验版
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
        :param _DeviceCertificateProvisionType: 客户端证书注册方式：JITP，API
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
        :param _X509Mode:     TLS,单向认证
    mTLS,双向认证
    BYOC;一机一证
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
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

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
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def TopicNumLimit(self):
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def TpsLimit(self):
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def SkuCode(self):
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def MaxSubscriptionPerClient(self):
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def AuthorizationPolicyLimit(self):
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def ClientNumLimit(self):
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def DeviceCertificateProvisionType(self):
        return self._DeviceCertificateProvisionType

    @DeviceCertificateProvisionType.setter
    def DeviceCertificateProvisionType(self, DeviceCertificateProvisionType):
        self._DeviceCertificateProvisionType = DeviceCertificateProvisionType

    @property
    def AutomaticActivation(self):
        return self._AutomaticActivation

    @AutomaticActivation.setter
    def AutomaticActivation(self, AutomaticActivation):
        self._AutomaticActivation = AutomaticActivation

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def DestroyTime(self):
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def X509Mode(self):
        return self._X509Mode

    @X509Mode.setter
    def X509Mode(self, X509Mode):
        self._X509Mode = X509Mode

    @property
    def MaxCaNum(self):
        return self._MaxCaNum

    @MaxCaNum.setter
    def MaxCaNum(self, MaxCaNum):
        self._MaxCaNum = MaxCaNum

    @property
    def RegistrationCode(self):
        return self._RegistrationCode

    @RegistrationCode.setter
    def RegistrationCode(self, RegistrationCode):
        self._RegistrationCode = RegistrationCode

    @property
    def MaxSubscription(self):
        return self._MaxSubscription

    @MaxSubscription.setter
    def MaxSubscription(self, MaxSubscription):
        self._MaxSubscription = MaxSubscription

    @property
    def RequestId(self):
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


class DescribeTopicListRequest(AbstractModel):
    """DescribeTopicList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Filters: 查询条件列表
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def CreatedTime(self):
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def RequestId(self):
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
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Config(self):
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Remark(self):
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
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def InstanceType(self):
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def InstanceStatus(self):
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

    @property
    def TopicNumLimit(self):
        return self._TopicNumLimit

    @TopicNumLimit.setter
    def TopicNumLimit(self, TopicNumLimit):
        self._TopicNumLimit = TopicNumLimit

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def TopicNum(self):
        return self._TopicNum

    @TopicNum.setter
    def TopicNum(self, TopicNum):
        self._TopicNum = TopicNum

    @property
    def SkuCode(self):
        return self._SkuCode

    @SkuCode.setter
    def SkuCode(self, SkuCode):
        self._SkuCode = SkuCode

    @property
    def TpsLimit(self):
        return self._TpsLimit

    @TpsLimit.setter
    def TpsLimit(self, TpsLimit):
        self._TpsLimit = TpsLimit

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def MaxSubscriptionPerClient(self):
        return self._MaxSubscriptionPerClient

    @MaxSubscriptionPerClient.setter
    def MaxSubscriptionPerClient(self, MaxSubscriptionPerClient):
        self._MaxSubscriptionPerClient = MaxSubscriptionPerClient

    @property
    def ClientNumLimit(self):
        return self._ClientNumLimit

    @ClientNumLimit.setter
    def ClientNumLimit(self, ClientNumLimit):
        self._ClientNumLimit = ClientNumLimit

    @property
    def RenewFlag(self):
        return self._RenewFlag

    @RenewFlag.setter
    def RenewFlag(self, RenewFlag):
        self._RenewFlag = RenewFlag

    @property
    def PayMode(self):
        return self._PayMode

    @PayMode.setter
    def PayMode(self, PayMode):
        self._PayMode = PayMode

    @property
    def ExpiryTime(self):
        return self._ExpiryTime

    @ExpiryTime.setter
    def ExpiryTime(self, ExpiryTime):
        self._ExpiryTime = ExpiryTime

    @property
    def DestroyTime(self):
        return self._DestroyTime

    @DestroyTime.setter
    def DestroyTime(self, DestroyTime):
        self._DestroyTime = DestroyTime

    @property
    def AuthorizationPolicyLimit(self):
        return self._AuthorizationPolicyLimit

    @AuthorizationPolicyLimit.setter
    def AuthorizationPolicyLimit(self, AuthorizationPolicyLimit):
        self._AuthorizationPolicyLimit = AuthorizationPolicyLimit

    @property
    def MaxCaNum(self):
        return self._MaxCaNum

    @MaxCaNum.setter
    def MaxCaNum(self, MaxCaNum):
        self._MaxCaNum = MaxCaNum

    @property
    def MaxSubscription(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
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
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyName(self):
        return self._PolicyName

    @PolicyName.setter
    def PolicyName(self, PolicyName):
        self._PolicyName = PolicyName

    @property
    def PolicyVersion(self):
        return self._PolicyVersion

    @PolicyVersion.setter
    def PolicyVersion(self, PolicyVersion):
        self._PolicyVersion = PolicyVersion

    @property
    def Priority(self):
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority

    @property
    def Effect(self):
        return self._Effect

    @Effect.setter
    def Effect(self, Effect):
        self._Effect = Effect

    @property
    def Actions(self):
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Username(self):
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Retain(self):
        return self._Retain

    @Retain.setter
    def Retain(self, Retain):
        self._Retain = Retain

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Qos(self):
        return self._Qos

    @Qos.setter
    def Qos(self, Qos):
        self._Qos = Qos

    @property
    def Remark(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Endpoint(self):
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RefreshInterval(self):
        return self._RefreshInterval

    @RefreshInterval.setter
    def RefreshInterval(self, RefreshInterval):
        self._RefreshInterval = RefreshInterval

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Remark(self):
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
        :param _From: 设备连接时传递jwt的key；username-使用用户名字段传递；password-使用密码字段传递
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Algorithm(self):
        return self._Algorithm

    @Algorithm.setter
    def Algorithm(self, Algorithm):
        self._Algorithm = Algorithm

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Secret(self):
        return self._Secret

    @Secret.setter
    def Secret(self, Secret):
        self._Secret = Secret

    @property
    def PublicKey(self):
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Remark(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Topic(self):
        return self._Topic

    @Topic.setter
    def Topic(self, Topic):
        self._Topic = Topic

    @property
    def Remark(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceCertificate(self):
        return self._DeviceCertificate

    @DeviceCertificate.setter
    def DeviceCertificate(self, DeviceCertificate):
        self._DeviceCertificate = DeviceCertificate

    @property
    def CaSn(self):
        return self._CaSn

    @CaSn.setter
    def CaSn(self, CaSn):
        self._CaSn = CaSn

    @property
    def ClientId(self):
        return self._ClientId

    @ClientId.setter
    def ClientId(self, ClientId):
        self._ClientId = ClientId

    @property
    def Format(self):
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def Status(self):
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
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


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
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValues(self):
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
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Priorities(self):
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
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")