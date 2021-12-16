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


class ApiKey(AbstractModel):
    """API密钥数据列表

    """

    def __init__(self):
        r"""
        :param SecretId: 密钥ID
        :type SecretId: str
        :param CreateTime: 创建时间(时间戳)
        :type CreateTime: int
        :param Status: 状态(2:有效, 3:禁用, 4:已删除)
        :type Status: int
        """
        self.SecretId = None
        self.CreateTime = None
        self.Status = None


    def _deserialize(self, params):
        self.SecretId = params.get("SecretId")
        self.CreateTime = params.get("CreateTime")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleRequest(AbstractModel):
    """AssumeRole请求参数结构体

    """

    def __init__(self):
        r"""
        :param RoleArn: 角色的资源描述，可在[访问管理](https://console.cloud.tencent.com/cam/role)，点击角色名获取。
普通角色：
qcs::cam::uin/12345678:role/4611686018427397919、qcs::cam::uin/12345678:roleName/testRoleName
服务角色：
qcs::cam::uin/12345678:role/tencentcloudServiceRole/4611686018427397920、qcs::cam::uin/12345678:role/tencentcloudServiceRoleName/testServiceRoleName
        :type RoleArn: str
        :param RoleSessionName: 临时会话名称，由用户自定义名称。
长度在2到128之间，可包含大小写字符，数字以及特殊字符：=,.@_-。 正则为：[\w+=,.@_-]*
        :type RoleSessionName: str
        :param DurationSeconds: 指定临时证书的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :type DurationSeconds: int
        :param Policy: 策略描述
注意：
1、policy 需要做 urlencode（如果通过 GET 方法请求云 API，发送请求前，所有参数都需要按照[云 API 规范](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2)再 urlencode 一次）。
2、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。
3、策略中不能包含 principal 元素。
        :type Policy: str
        :param ExternalId: 角色外部ID，可在[访问管理](https://console.cloud.tencent.com/cam/role)，点击角色名获取。
长度在2到128之间，可包含大小写字符，数字以及特殊字符：=,.@:/-。 正则为：[\w+=,.@:\/-]*
        :type ExternalId: str
        """
        self.RoleArn = None
        self.RoleSessionName = None
        self.DurationSeconds = None
        self.Policy = None
        self.ExternalId = None


    def _deserialize(self, params):
        self.RoleArn = params.get("RoleArn")
        self.RoleSessionName = params.get("RoleSessionName")
        self.DurationSeconds = params.get("DurationSeconds")
        self.Policy = params.get("Policy")
        self.ExternalId = params.get("ExternalId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleResponse(AbstractModel):
    """AssumeRole返回参数结构体

    """

    def __init__(self):
        r"""
        :param Credentials: 临时安全证书
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param ExpiredTime: 证书无效的时间，返回 Unix 时间戳，精确到秒
        :type ExpiredTime: int
        :param Expiration: 证书无效的时间，以 iso8601 格式的 UTC 时间表示
        :type Expiration: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Credentials = None
        self.ExpiredTime = None
        self.Expiration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.ExpiredTime = params.get("ExpiredTime")
        self.Expiration = params.get("Expiration")
        self.RequestId = params.get("RequestId")


class AssumeRoleWithSAMLRequest(AbstractModel):
    """AssumeRoleWithSAML请求参数结构体

    """

    def __init__(self):
        r"""
        :param SAMLAssertion: base64 编码的 SAML 断言信息
        :type SAMLAssertion: str
        :param PrincipalArn: 扮演者访问描述名
        :type PrincipalArn: str
        :param RoleArn: 角色访问描述名
        :type RoleArn: str
        :param RoleSessionName: 会话名称
        :type RoleSessionName: str
        :param DurationSeconds: 指定临时证书的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :type DurationSeconds: int
        """
        self.SAMLAssertion = None
        self.PrincipalArn = None
        self.RoleArn = None
        self.RoleSessionName = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.SAMLAssertion = params.get("SAMLAssertion")
        self.PrincipalArn = params.get("PrincipalArn")
        self.RoleArn = params.get("RoleArn")
        self.RoleSessionName = params.get("RoleSessionName")
        self.DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssumeRoleWithSAMLResponse(AbstractModel):
    """AssumeRoleWithSAML返回参数结构体

    """

    def __init__(self):
        r"""
        :param Credentials: 对象里面包含 Token，TmpSecretId，TmpSecretKey 三元组
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param ExpiredTime: 证书无效的时间，返回 Unix 时间戳，精确到秒
        :type ExpiredTime: int
        :param Expiration: 证书无效的时间，以 ISO8601 格式的 UTC 时间表示
        :type Expiration: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Credentials = None
        self.ExpiredTime = None
        self.Expiration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.ExpiredTime = params.get("ExpiredTime")
        self.Expiration = params.get("Expiration")
        self.RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """临时证书

    """

    def __init__(self):
        r"""
        :param Token: token。token长度和绑定的策略有关，最长不超过4096字节。
        :type Token: str
        :param TmpSecretId: 临时证书密钥ID。最长不超过1024字节。
        :type TmpSecretId: str
        :param TmpSecretKey: 临时证书密钥Key。最长不超过1024字节。
        :type TmpSecretKey: str
        """
        self.Token = None
        self.TmpSecretId = None
        self.TmpSecretKey = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCallerIdentityRequest(AbstractModel):
    """GetCallerIdentity请求参数结构体

    """


class GetCallerIdentityResponse(AbstractModel):
    """GetCallerIdentity返回参数结构体

    """

    def __init__(self):
        r"""
        :param Arn: 当前调用者ARN。
        :type Arn: str
        :param AccountId: 当前调用者所属主账号Uin。
        :type AccountId: str
        :param UserId: 身份标识。
1. 调用者是云账号时，返回的是当前账号Uin
2. 调用者是角色时，返回的是roleId:roleSessionName
3. 调用者是联合身份时，返回的是uin:federatedUserName
        :type UserId: str
        :param PrincipalId: 密钥所属账号Uin。
1. 调用者是云账号，返回的当前账号Uin
2, 调用者是角色，返回的申请角色密钥的账号Uin
        :type PrincipalId: str
        :param Type: 身份类型。
        :type Type: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Arn = None
        self.AccountId = None
        self.UserId = None
        self.PrincipalId = None
        self.Type = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Arn = params.get("Arn")
        self.AccountId = params.get("AccountId")
        self.UserId = params.get("UserId")
        self.PrincipalId = params.get("PrincipalId")
        self.Type = params.get("Type")
        self.RequestId = params.get("RequestId")


class GetFederationTokenRequest(AbstractModel):
    """GetFederationToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 您可以自定义调用方英文名称，由字母组成。
        :type Name: str
        :param Policy: 授予该临时证书权限的CAM策略
注意：
1、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。
2、策略中不能包含 principal 元素。
3、该参数需要做urlencode。
        :type Policy: str
        :param DurationSeconds: 指定临时证书的有效期，单位：秒，默认1800秒，主账号最长可设定有效期为7200秒，子账号最长可设定有效期为129600秒。
        :type DurationSeconds: int
        """
        self.Name = None
        self.Policy = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Policy = params.get("Policy")
        self.DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetFederationTokenResponse(AbstractModel):
    """GetFederationToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param Credentials: 临时证书
        :type Credentials: :class:`tencentcloud.sts.v20180813.models.Credentials`
        :param ExpiredTime: 临时证书有效的时间，返回 Unix 时间戳，精确到秒
        :type ExpiredTime: int
        :param Expiration: 证书有效的时间，以 iso8601 格式的 UTC 时间表示
注意：此字段可能返回 null，表示取不到有效值。
        :type Expiration: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Credentials = None
        self.ExpiredTime = None
        self.Expiration = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Credentials") is not None:
            self.Credentials = Credentials()
            self.Credentials._deserialize(params.get("Credentials"))
        self.ExpiredTime = params.get("ExpiredTime")
        self.Expiration = params.get("Expiration")
        self.RequestId = params.get("RequestId")


class QueryApiKeyRequest(AbstractModel):
    """QueryApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param TargetUin: 待查询的账号(不填默认查当前账号)
        :type TargetUin: int
        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryApiKeyResponse(AbstractModel):
    """QueryApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param IdKeys: 密钥ID列表
        :type IdKeys: list of ApiKey
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IdKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("IdKeys") is not None:
            self.IdKeys = []
            for item in params.get("IdKeys"):
                obj = ApiKey()
                obj._deserialize(item)
                self.IdKeys.append(obj)
        self.RequestId = params.get("RequestId")