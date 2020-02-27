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


class ApiKey(AbstractModel):
    """API密钥数据列表

    """

    def __init__(self):
        """
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


class AssumeRoleRequest(AbstractModel):
    """AssumeRole请求参数结构体

    """

    def __init__(self):
        """
        :param RoleArn: 角色的资源描述。例如：qcs::cam::uin/12345678:role/4611686018427397919、qcs::cam::uin/12345678:roleName/testRoleName
        :type RoleArn: str
        :param RoleSessionName: 临时会话名称，由用户自定义名称
        :type RoleSessionName: str
        :param DurationSeconds: 指定临时证书的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 43200 秒
        :type DurationSeconds: int
        :param Policy: 策略描述
注意：
1、policy 需要做 urlencode（如果通过 GET 方法请求云 API，发送请求前，所有参数都需要按照[云 API 规范](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2)再 urlencode 一次）。
2、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。
3、策略中不能包含 principal 元素。
        :type Policy: str
        """
        self.RoleArn = None
        self.RoleSessionName = None
        self.DurationSeconds = None
        self.Policy = None


    def _deserialize(self, params):
        self.RoleArn = params.get("RoleArn")
        self.RoleSessionName = params.get("RoleSessionName")
        self.DurationSeconds = params.get("DurationSeconds")
        self.Policy = params.get("Policy")


class AssumeRoleResponse(AbstractModel):
    """AssumeRole返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param SAMLAssertion: base64 编码的 SAML 断言信息
        :type SAMLAssertion: str
        :param PrincipalArn: 扮演者访问描述名
        :type PrincipalArn: str
        :param RoleArn: 角色访问描述名
        :type RoleArn: str
        :param RoleSessionName: 会话名称
        :type RoleSessionName: str
        :param DurationSeconds: 指定临时证书的有效期，单位：秒，默认 7200 秒，最长可设定有效期为 7200 秒
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


class AssumeRoleWithSAMLResponse(AbstractModel):
    """AssumeRoleWithSAML返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Token: token
        :type Token: str
        :param TmpSecretId: 临时证书密钥ID
        :type TmpSecretId: str
        :param TmpSecretKey: 临时证书密钥Key
        :type TmpSecretKey: str
        """
        self.Token = None
        self.TmpSecretId = None
        self.TmpSecretKey = None


    def _deserialize(self, params):
        self.Token = params.get("Token")
        self.TmpSecretId = params.get("TmpSecretId")
        self.TmpSecretKey = params.get("TmpSecretKey")


class GetFederationTokenRequest(AbstractModel):
    """GetFederationToken请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 您可以自定义调用方英文名称，由字母组成。
        :type Name: str
        :param Policy: 策略描述
注意：
1、policy 需要做 urlencode（如果通过 GET 方法请求云 API，发送请求前，所有参数都需要按照[云 API 规范](https://cloud.tencent.com/document/api/598/33159#1.-.E6.8B.BC.E6.8E.A5.E8.A7.84.E8.8C.83.E8.AF.B7.E6.B1.82.E4.B8.B2)再 urlencode 一次）。
2、策略语法参照[ CAM 策略语法](https://cloud.tencent.com/document/product/598/10603)。
3、策略中不能包含 principal 元素。
        :type Policy: str
        :param DurationSeconds: 指定临时证书的有效期，单位：秒，默认1800秒，最长可设定有效期为7200秒。
        :type DurationSeconds: int
        """
        self.Name = None
        self.Policy = None
        self.DurationSeconds = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Policy = params.get("Policy")
        self.DurationSeconds = params.get("DurationSeconds")


class GetFederationTokenResponse(AbstractModel):
    """GetFederationToken返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param TargetUin: 待查询的账号(不填默认查当前账号)
        :type TargetUin: int
        """
        self.TargetUin = None


    def _deserialize(self, params):
        self.TargetUin = params.get("TargetUin")


class QueryApiKeyResponse(AbstractModel):
    """QueryApiKey返回参数结构体

    """

    def __init__(self):
        """
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