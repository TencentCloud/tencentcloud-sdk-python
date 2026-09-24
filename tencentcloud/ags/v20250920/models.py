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


class APIKeyInfo(AbstractModel):
    r"""API密钥简略信息

    """

    def __init__(self):
        r"""
        :param _Name: API密钥名称
        :type Name: str
        :param _KeyId: API密钥ID
        :type KeyId: str
        :param _Status: 密钥状态。可以为API_KEY_STATUS_ACTIVE，或API_KEY_STATUS_INACTIVE
        :type Status: str
        :param _MaskedKey: 隐藏部分字符的API密钥，方便用户辨认
        :type MaskedKey: str
        :param _CreatedAt: API密钥创建时间
        :type CreatedAt: str
        """
        self._Name = None
        self._KeyId = None
        self._Status = None
        self._MaskedKey = None
        self._CreatedAt = None

    @property
    def Name(self):
        r"""API密钥名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def KeyId(self):
        r"""API密钥ID
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def Status(self):
        r"""密钥状态。可以为API_KEY_STATUS_ACTIVE，或API_KEY_STATUS_INACTIVE
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def MaskedKey(self):
        r"""隐藏部分字符的API密钥，方便用户辨认
        :rtype: str
        """
        return self._MaskedKey

    @MaskedKey.setter
    def MaskedKey(self, MaskedKey):
        self._MaskedKey = MaskedKey

    @property
    def CreatedAt(self):
        r"""API密钥创建时间
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._KeyId = params.get("KeyId")
        self._Status = params.get("Status")
        self._MaskedKey = params.get("MaskedKey")
        self._CreatedAt = params.get("CreatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountQuotaOverview(AbstractModel):
    r"""主账号配额总览

    """

    def __init__(self):
        r"""
        :param _Quota: <p>主账号各资源维度的配额上限</p>
        :type Quota: :class:`tencentcloud.ags.v20250920.models.QuotaResourceInfo`
        :param _Usage: <p>主账号各资源维度的当前用量</p>
        :type Usage: :class:`tencentcloud.ags.v20250920.models.QuotaResourceInfo`
        """
        self._Quota = None
        self._Usage = None

    @property
    def Quota(self):
        r"""<p>主账号各资源维度的配额上限</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.QuotaResourceInfo`
        """
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota

    @property
    def Usage(self):
        r"""<p>主账号各资源维度的当前用量</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.QuotaResourceInfo`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage


    def _deserialize(self, params):
        if params.get("Quota") is not None:
            self._Quota = QuotaResourceInfo()
            self._Quota._deserialize(params.get("Quota"))
        if params.get("Usage") is not None:
            self._Usage = QuotaResourceInfo()
            self._Usage._deserialize(params.get("Usage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcquireDeploymentTokenRequest(AbstractModel):
    r"""AcquireDeploymentToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>目标 ACTIVE Deployment 的稳定 ID。</p>
        :type DeploymentId: str
        """
        self._DeploymentId = None

    @property
    def DeploymentId(self):
        r"""<p>目标 ACTIVE Deployment 的稳定 ID。</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcquireDeploymentTokenResponse(AbstractModel):
    r"""AcquireDeploymentToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: <p>只用于目标 Deployment 数据面入口的短期 bearer Token，格式为 dpt_ 加非空、无 padding 的 Base64URL opaque 后缀。</p>
        :type Token: str
        :param _ExpiresAt: <p>Token 的绝对过期时间，UTC、秒精度 RFC3339 格式。</p>
        :type ExpiresAt: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._ExpiresAt = None
        self._RequestId = None

    @property
    def Token(self):
        r"""<p>只用于目标 Deployment 数据面入口的短期 bearer Token，格式为 dpt_ 加非空、无 padding 的 Base64URL opaque 后缀。</p>
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiresAt(self):
        r"""<p>Token 的绝对过期时间，UTC、秒精度 RFC3339 格式。</p>
        :rtype: str
        """
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

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
        self._Token = params.get("Token")
        self._ExpiresAt = params.get("ExpiresAt")
        self._RequestId = params.get("RequestId")


class AcquireSandboxInstanceTokenRequest(AbstractModel):
    r"""AcquireSandboxInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>沙箱实例ID，生成的访问Token将仅可用于访问此沙箱实例</p>
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""<p>沙箱实例ID，生成的访问Token将仅可用于访问此沙箱实例</p>
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
        


class AcquireSandboxInstanceTokenResponse(AbstractModel):
    r"""AcquireSandboxInstanceToken返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Token: <p>访问Token</p>
        :type Token: str
        :param _ExpiresAt: <p>过期时间</p>
        :type ExpiresAt: str
        :param _TrafficToken: <p>除管控面envd端口(49983)以外端口的访问Token</p>
        :type TrafficToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._ExpiresAt = None
        self._TrafficToken = None
        self._RequestId = None

    @property
    def Token(self):
        r"""<p>访问Token</p>
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiresAt(self):
        r"""<p>过期时间</p>
        :rtype: str
        """
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def TrafficToken(self):
        r"""<p>除管控面envd端口(49983)以外端口的访问Token</p>
        :rtype: str
        """
        return self._TrafficToken

    @TrafficToken.setter
    def TrafficToken(self, TrafficToken):
        self._TrafficToken = TrafficToken

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
        self._Token = params.get("Token")
        self._ExpiresAt = params.get("ExpiresAt")
        self._TrafficToken = params.get("TrafficToken")
        self._RequestId = params.get("RequestId")


class AffinityConfiguration(AbstractModel):
    r"""Deployment 对 Sandbox Instance 的亲和配置。

    """

    def __init__(self):
        r"""
        :param _Mode: <p>Affinity 模式。</p><p>枚举值：</p><ul><li>BEST_EFFORT：优先复用原 Instance，不可用时允许改选。</li><li>STRICT：只复用原 Instance，不可用时失败且不改选。</li><li>EXCLUSIVE：一个 Affinity ID 独占一个 Instance，不能迁移。</li></ul><p>缺失或空字符串表示关闭 Affinity。</p>
        :type Mode: str
        :param _HeaderName: <p>请求和响应使用的 Affinity Header 名称。必须符合 HTTP field-name token 语法，长度为 1..128 个 ASCII 字节，且不能使用平台保留 Header。</p>
        :type HeaderName: str
        """
        self._Mode = None
        self._HeaderName = None

    @property
    def Mode(self):
        r"""<p>Affinity 模式。</p><p>枚举值：</p><ul><li>BEST_EFFORT：优先复用原 Instance，不可用时允许改选。</li><li>STRICT：只复用原 Instance，不可用时失败且不改选。</li><li>EXCLUSIVE：一个 Affinity ID 独占一个 Instance，不能迁移。</li></ul><p>缺失或空字符串表示关闭 Affinity。</p>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def HeaderName(self):
        r"""<p>请求和响应使用的 Affinity Header 名称。必须符合 HTTP field-name token 语法，长度为 1..128 个 ASCII 字节，且不能使用平台保留 Header。</p>
        :rtype: str
        """
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._HeaderName = params.get("HeaderName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AgentBucketStorageSource(AbstractModel):
    r"""用于记录 Agent Bucket 的 Storage Source

    """

    def __init__(self):
        r"""
        :param _LibraryId: <p>用于传入 AgentBucket 的 LibraryID</p>
        :type LibraryId: str
        :param _SpaceId: <p>用于传入 AgentBucket 的 spaceId</p>
        :type SpaceId: str
        :param _AccessDomain: <p>用于传入 AgentBucket 的 AccessDomain</p>
        :type AccessDomain: str
        """
        self._LibraryId = None
        self._SpaceId = None
        self._AccessDomain = None

    @property
    def LibraryId(self):
        r"""<p>用于传入 AgentBucket 的 LibraryID</p>
        :rtype: str
        """
        return self._LibraryId

    @LibraryId.setter
    def LibraryId(self, LibraryId):
        self._LibraryId = LibraryId

    @property
    def SpaceId(self):
        r"""<p>用于传入 AgentBucket 的 spaceId</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def AccessDomain(self):
        r"""<p>用于传入 AgentBucket 的 AccessDomain</p>
        :rtype: str
        """
        return self._AccessDomain

    @AccessDomain.setter
    def AccessDomain(self, AccessDomain):
        self._AccessDomain = AccessDomain


    def _deserialize(self, params):
        self._LibraryId = params.get("LibraryId")
        self._SpaceId = params.get("SpaceId")
        self._AccessDomain = params.get("AccessDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppendEventRequest(AbstractModel):
    r"""AppendEvent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>会话所属空间 ID。</p>
        :type SpaceId: str
        :param _UserId: <p>用户 ID。可通过调用方业务系统接口获取。</p>
        :type UserId: str
        :param _SessionId: <p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :type SessionId: str
        :param _Event: <p>事件内容。</p>
        :type Event: :class:`tencentcloud.ags.v20250920.models.EventInfo`
        :param _AgentId: <p>Agent ID。可选。</p>
        :type AgentId: str
        """
        self._SpaceId = None
        self._UserId = None
        self._SessionId = None
        self._Event = None
        self._AgentId = None

    @property
    def SpaceId(self):
        r"""<p>会话所属空间 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def UserId(self):
        r"""<p>用户 ID。可通过调用方业务系统接口获取。</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SessionId(self):
        r"""<p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Event(self):
        r"""<p>事件内容。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.EventInfo`
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

    @property
    def AgentId(self):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        r"""<p>Agent ID。可选。</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        self._AgentId = AgentId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._UserId = params.get("UserId")
        self._SessionId = params.get("SessionId")
        if params.get("Event") is not None:
            self._Event = EventInfo()
            self._Event._deserialize(params.get("Event"))
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AppendEventResponse(AbstractModel):
    r"""AppendEvent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Event: <p>事件信息。</p>
        :type Event: :class:`tencentcloud.ags.v20250920.models.EventInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Event = None
        self._RequestId = None

    @property
    def Event(self):
        r"""<p>事件信息。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.EventInfo`
        """
        return self._Event

    @Event.setter
    def Event(self, Event):
        self._Event = Event

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
        if params.get("Event") is not None:
            self._Event = EventInfo()
            self._Event._deserialize(params.get("Event"))
        self._RequestId = params.get("RequestId")


class ApproveRegistryRecordRequest(AbstractModel):
    r"""ApproveRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>Version ID。</p>
        :type VersionId: str
        :param _Comment: <p>动作留言；非空。</p>
        :type Comment: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._Comment = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>Version ID。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Comment(self):
        r"""<p>动作留言；非空。</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApproveRegistryRecordResponse(AbstractModel):
    r"""ApproveRegistryRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: <p>更新后的 Version。</p>
        :type Version: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._RequestId = None

    @property
    def Version(self):
        r"""<p>更新后的 Version。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

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
        if params.get("Version") is not None:
            self._Version = CloudRecordVersion()
            self._Version._deserialize(params.get("Version"))
        self._RequestId = params.get("RequestId")


class CLSConfig(AbstractModel):
    r"""沙箱工具日志推送CLS相关配置

    """

    def __init__(self):
        r"""
        :param _TopicId: 沙箱工具日志推送所使用的CLS日志主题ID
        :type TopicId: str
        """
        self._TopicId = None

    @property
    def TopicId(self):
        r"""沙箱工具日志推送所使用的CLS日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelRegistryRecordRequest(AbstractModel):
    r"""CancelRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>Version ID。</p>
        :type VersionId: str
        :param _Comment: <p>动作留言；非空。</p>
        :type Comment: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._Comment = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>Version ID。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Comment(self):
        r"""<p>动作留言；非空。</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelRegistryRecordResponse(AbstractModel):
    r"""CancelRegistryRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: <p>更新后的 Version。</p>
        :type Version: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._RequestId = None

    @property
    def Version(self):
        r"""<p>更新后的 Version。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

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
        if params.get("Version") is not None:
            self._Version = CloudRecordVersion()
            self._Version._deserialize(params.get("Version"))
        self._RequestId = params.get("RequestId")


class CfsStorageSource(AbstractModel):
    r"""文件存储配置

    """

    def __init__(self):
        r"""
        :param _FileSystemId: CFS资源ID
        :type FileSystemId: str
        :param _Path: CFS挂载路径
        :type Path: str
        """
        self._FileSystemId = None
        self._Path = None

    @property
    def FileSystemId(self):
        r"""CFS资源ID
        :rtype: str
        """
        return self._FileSystemId

    @FileSystemId.setter
    def FileSystemId(self, FileSystemId):
        self._FileSystemId = FileSystemId

    @property
    def Path(self):
        r"""CFS挂载路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._FileSystemId = params.get("FileSystemId")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudAgentSourceInput(AbstractModel):
    r"""Agent Record 内容来源。Type 判别 MANUAL 与 URL_IMPORT。

    """

    def __init__(self):
        r"""
        :param _Type: <p>来源类型。MANUAL：直接提交 Agent Descriptors JSON 文本；URL_IMPORT：从远端 Agent Card / AGUI 端点导入。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Descriptors: <p>Type=MANUAL 时必填；值为通用 JSON object 文本；A2A 标准校验或 AGUI/CUSTOM 规则由后端执行。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Descriptors: str
        :param _EndpointURL: <p>A2A：Agent Card URL；AGUI：Runtime Endpoint URL。Type=URL_IMPORT 时必填，HTTPS。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EndpointURL: str
        """
        self._Type = None
        self._Descriptors = None
        self._EndpointURL = None

    @property
    def Type(self):
        r"""<p>来源类型。MANUAL：直接提交 Agent Descriptors JSON 文本；URL_IMPORT：从远端 Agent Card / AGUI 端点导入。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Descriptors(self):
        r"""<p>Type=MANUAL 时必填；值为通用 JSON object 文本；A2A 标准校验或 AGUI/CUSTOM 规则由后端执行。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Descriptors

    @Descriptors.setter
    def Descriptors(self, Descriptors):
        self._Descriptors = Descriptors

    @property
    def EndpointURL(self):
        r"""<p>A2A：Agent Card URL；AGUI：Runtime Endpoint URL。Type=URL_IMPORT 时必填，HTTPS。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndpointURL

    @EndpointURL.setter
    def EndpointURL(self, EndpointURL):
        self._EndpointURL = EndpointURL


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Descriptors = params.get("Descriptors")
        self._EndpointURL = params.get("EndpointURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudAuditLog(AbstractModel):
    r"""审计日志条目。记录 Registry / Record / Version 维度的动作。

    """

    def __init__(self):
        r"""
        :param _AuditLogId: <p>审计日志 ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AuditLogId: str
        :param _RegistryId: <p>所属 Registry ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: str
        :param _Actor: <p>动作发起者（主账号 UIN 或子账号 UIN）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Actor: str
        :param _Action: <p>Action 名称，等同 X-TC-Action。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _Details: <p>动作脱敏摘要对象；使用云 API 字段命名，字段随 Action 而变；不包含凭据、预签名 URL 或完整 Descriptor。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Details: str
        :param _CreateTime: <p>动作发生时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _RecordId: <p>关联 Record ID；仅 Record / Version 相关动作。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _VersionId: <p>关联 Version ID；仅 Version 相关动作。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        """
        self._AuditLogId = None
        self._RegistryId = None
        self._Actor = None
        self._Action = None
        self._Details = None
        self._CreateTime = None
        self._RecordId = None
        self._VersionId = None

    @property
    def AuditLogId(self):
        r"""<p>审计日志 ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AuditLogId

    @AuditLogId.setter
    def AuditLogId(self, AuditLogId):
        self._AuditLogId = AuditLogId

    @property
    def RegistryId(self):
        r"""<p>所属 Registry ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Actor(self):
        r"""<p>动作发起者（主账号 UIN 或子账号 UIN）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Actor

    @Actor.setter
    def Actor(self, Actor):
        self._Actor = Actor

    @property
    def Action(self):
        r"""<p>Action 名称，等同 X-TC-Action。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Details(self):
        r"""<p>动作脱敏摘要对象；使用云 API 字段命名，字段随 Action 而变；不包含凭据、预签名 URL 或完整 Descriptor。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Details

    @Details.setter
    def Details(self, Details):
        self._Details = Details

    @property
    def CreateTime(self):
        r"""<p>动作发生时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RecordId(self):
        r"""<p>关联 Record ID；仅 Record / Version 相关动作。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>关联 Version ID；仅 Version 相关动作。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._AuditLogId = params.get("AuditLogId")
        self._RegistryId = params.get("RegistryId")
        self._Actor = params.get("Actor")
        self._Action = params.get("Action")
        self._Details = params.get("Details")
        self._CreateTime = params.get("CreateTime")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudFilter(AbstractModel):
    r"""通用过滤条件。Name 为字段名，Values 为字段候选值；字段间 AND、Values 内 OR。

    """

    def __init__(self):
        r"""
        :param _Name: <p>过滤字段名。DescribeRegistryList 支持 <code>name</code> / <code>search</code>（模糊搜索）与 <code>archived</code> / <code>status</code>（true / false / all）；DescribeRegistryRecordList 支持 <code>name</code> / <code>search</code>（模糊）、<code>descriptor-type</code>、<code>lifecycle-status</code>（精确）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Values: <p>过滤字段候选值列表；至少 1 项。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>过滤字段名。DescribeRegistryList 支持 <code>name</code> / <code>search</code>（模糊搜索）与 <code>archived</code> / <code>status</code>（true / false / all）；DescribeRegistryRecordList 支持 <code>name</code> / <code>search</code>（模糊）、<code>descriptor-type</code>、<code>lifecycle-status</code>（精确）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>过滤字段候选值列表；至少 1 项。</p>
注意：此字段可能返回 null，表示取不到有效值。
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
        


class CloudMCPSourceInput(AbstractModel):
    r"""MCP Record 内容来源。Type 判别 MANUAL 与 URL_IMPORT。

    """

    def __init__(self):
        r"""
        :param _Type: <p>来源类型。MANUAL：直接提交 MCP Descriptors JSON 文本；URL_IMPORT：从远端 MCP server.json URL 导入。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Descriptors: <p>Type=MANUAL 时必填；值为完整 MCP server.json 对象的 JSON 文本；完整 MCP 2025-12-11 标准校验由后端执行。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Descriptors: str
        :param _EndpointURL: <p>远端 MCP server.json URL；HTTPS。Type=URL_IMPORT 时必填。Version 从远端 initialize.serverInfo.version 观测获得，无需请求参数。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EndpointURL: str
        """
        self._Type = None
        self._Descriptors = None
        self._EndpointURL = None

    @property
    def Type(self):
        r"""<p>来源类型。MANUAL：直接提交 MCP Descriptors JSON 文本；URL_IMPORT：从远端 MCP server.json URL 导入。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Descriptors(self):
        r"""<p>Type=MANUAL 时必填；值为完整 MCP server.json 对象的 JSON 文本；完整 MCP 2025-12-11 标准校验由后端执行。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Descriptors

    @Descriptors.setter
    def Descriptors(self, Descriptors):
        self._Descriptors = Descriptors

    @property
    def EndpointURL(self):
        r"""<p>远端 MCP server.json URL；HTTPS。Type=URL_IMPORT 时必填。Version 从远端 initialize.serverInfo.version 观测获得，无需请求参数。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndpointURL

    @EndpointURL.setter
    def EndpointURL(self, EndpointURL):
        self._EndpointURL = EndpointURL


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Descriptors = params.get("Descriptors")
        self._EndpointURL = params.get("EndpointURL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudRecord(AbstractModel):
    r"""Registry Record 对象。Record 只保存元数据；协议描述符与内容状态请通过 Version 相关接口获取。

    """

    def __init__(self):
        r"""
        :param _RecordId: <p>Record ID；格式 <code>rec-</code> + 8 位小写字母/数字。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _RegistryId: <p>所属 Registry ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: str
        :param _Name: <p>Record 名称；同一 Registry 内可重复。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>描述。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _DescriptorType: <p>协议描述符类型；创建后不可变。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptorType: str
        :param _LifecycleStatus: <p>生命周期状态。ACTIVE：可用；DELETED：软删除墓碑，不再参与常规查询、下发或版本配额。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LifecycleStatus: str
        :param _AppId: <p>所属租户 AppId。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _CreatorUin: <p>创建者主账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param _CreatorSubAccountUin: <p>创建者子账号 UIN；主账号直接创建时为空。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorSubAccountUin: str
        :param _CreateTime: <p>创建时间，ISO 8601 UTC。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: <p>最近一次更新时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _VersionCount: <p>Record 下未删除 Version 数量。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionCount: int
        :param _LabelSet: <p>Record 下所有 Label Name（含未绑定 Label），包括系统 Label（stable / latest）和自定义 Label。仅名称，不含 VersionId、更新时间或操作者。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelSet: list of str
        """
        self._RecordId = None
        self._RegistryId = None
        self._Name = None
        self._Description = None
        self._DescriptorType = None
        self._LifecycleStatus = None
        self._AppId = None
        self._CreatorUin = None
        self._CreatorSubAccountUin = None
        self._CreateTime = None
        self._UpdateTime = None
        self._VersionCount = None
        self._LabelSet = None

    @property
    def RecordId(self):
        r"""<p>Record ID；格式 <code>rec-</code> + 8 位小写字母/数字。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RegistryId(self):
        r"""<p>所属 Registry ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        r"""<p>Record 名称；同一 Registry 内可重复。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>描述。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DescriptorType(self):
        r"""<p>协议描述符类型；创建后不可变。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DescriptorType

    @DescriptorType.setter
    def DescriptorType(self, DescriptorType):
        self._DescriptorType = DescriptorType

    @property
    def LifecycleStatus(self):
        r"""<p>生命周期状态。ACTIVE：可用；DELETED：软删除墓碑，不再参与常规查询、下发或版本配额。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LifecycleStatus

    @LifecycleStatus.setter
    def LifecycleStatus(self, LifecycleStatus):
        self._LifecycleStatus = LifecycleStatus

    @property
    def AppId(self):
        r"""<p>所属租户 AppId。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CreatorUin(self):
        r"""<p>创建者主账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def CreatorSubAccountUin(self):
        r"""<p>创建者子账号 UIN；主账号直接创建时为空。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorSubAccountUin

    @CreatorSubAccountUin.setter
    def CreatorSubAccountUin(self, CreatorSubAccountUin):
        self._CreatorSubAccountUin = CreatorSubAccountUin

    @property
    def CreateTime(self):
        r"""<p>创建时间，ISO 8601 UTC。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>最近一次更新时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def VersionCount(self):
        r"""<p>Record 下未删除 Version 数量。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VersionCount

    @VersionCount.setter
    def VersionCount(self, VersionCount):
        self._VersionCount = VersionCount

    @property
    def LabelSet(self):
        r"""<p>Record 下所有 Label Name（含未绑定 Label），包括系统 Label（stable / latest）和自定义 Label。仅名称，不含 VersionId、更新时间或操作者。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LabelSet

    @LabelSet.setter
    def LabelSet(self, LabelSet):
        self._LabelSet = LabelSet


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._DescriptorType = params.get("DescriptorType")
        self._LifecycleStatus = params.get("LifecycleStatus")
        self._AppId = params.get("AppId")
        self._CreatorUin = params.get("CreatorUin")
        self._CreatorSubAccountUin = params.get("CreatorSubAccountUin")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._VersionCount = params.get("VersionCount")
        self._LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudRecordLabelMutation(AbstractModel):
    r"""Record Label 变更操作项。Operation=SET 时可携带 VersionId；DELETE 时禁止 VersionId。

    """

    def __init__(self):
        r"""
        :param _Operation: <p>操作类型。SET：创建或移动 Label；DELETE：删除自定义 Label（stable/latest 保留 Label 禁止删除）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Operation: str
        :param _Name: <p>Label 名称，长度 1..63，格式 ^[a-z][a-z0-9._-]{0,62}$，按小写规范化。stable、latest 为系统保留 Label。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _VersionId: <p>目标 Version ID。SET 时可选：省略表示未绑定（自定义 Label 允许，stable 禁止）；DELETE 时禁止携带。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _Reason: <p>变更原因，最大 1024 字符，可选。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        """
        self._Operation = None
        self._Name = None
        self._VersionId = None
        self._Reason = None

    @property
    def Operation(self):
        r"""<p>操作类型。SET：创建或移动 Label；DELETE：删除自定义 Label（stable/latest 保留 Label 禁止删除）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Operation

    @Operation.setter
    def Operation(self, Operation):
        self._Operation = Operation

    @property
    def Name(self):
        r"""<p>Label 名称，长度 1..63，格式 ^[a-z][a-z0-9._-]{0,62}$，按小写规范化。stable、latest 为系统保留 Label。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VersionId(self):
        r"""<p>目标 Version ID。SET 时可选：省略表示未绑定（自定义 Label 允许，stable 禁止）；DELETE 时禁止携带。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Reason(self):
        r"""<p>变更原因，最大 1024 字符，可选。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Operation = params.get("Operation")
        self._Name = params.get("Name")
        self._VersionId = params.get("VersionId")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudRecordVersion(AbstractModel):
    r"""Record 的一个不可变 Version 快照；记录了描述符、来源配置与审批状态。

    """

    def __init__(self):
        r"""
        :param _VersionId: <p>Version ID；格式 <code>rv-</code> + 8 位小写字母/数字。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionId: str
        :param _RecordId: <p>所属 Record ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _Revision: <p>Version 递增序号（1 起）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Revision: int
        :param _Status: <p>Version 状态。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _ApprovalMode: <p>审批模式；创建时锁定，后续变更 Registry 审批模式不影响本 Version。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ApprovalMode: str
        :param _AppId: <p>所属租户 AppId。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _CreatorUin: <p>创建者主账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param _CreateTime: <p>创建时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: <p>最近一次更新时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _VersionName: <p>Version 别名（可选）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type VersionName: str
        :param _Descriptors: <p>协议描述符对象。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Descriptors: str
        :param _SourceType: <p>内容来源。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param _SourceConfig: <p>规范化来源配置对象。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceConfig: str
        :param _ContentStatus: <p>内容状态。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentStatus: str
        :param _ContentSHA256: <p>READY 内容 SHA-256。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentSHA256: str
        :param _ContentSizeBytes: <p>READY 内容字节数。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentSizeBytes: int
        :param _ConfigSHA256: <p>配置内容规范化后的 SHA-256（用于幂等去重）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigSHA256: str
        :param _CreatorSubAccountUin: <p>创建者子账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorSubAccountUin: str
        :param _ApprovalActions: <p>Version 历次审批动作。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ApprovalActions: list of CloudVersionApprovalAction
        :param _ContentReadyTime: <p>TAR 内容成功校验、完成物化并进入 READY 的时间；MANUAL / URL_IMPORT 或尚未 READY 的 TAR_PACKAGE 均为空。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentReadyTime: str
        :param _ChangeLog: <p>本次 Version 的变更原因，最大 4096 字符；不可修改。Revision 1 或未填写时返回空字符串。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ChangeLog: str
        :param _LabelSet: <p>当前绑定该 Version 的 Label Name 列表（例如 stable / latest 或自定义 Label 名称）。未绑定 Label 不在此返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelSet: list of str
        """
        self._VersionId = None
        self._RecordId = None
        self._Revision = None
        self._Status = None
        self._ApprovalMode = None
        self._AppId = None
        self._CreatorUin = None
        self._CreateTime = None
        self._UpdateTime = None
        self._VersionName = None
        self._Descriptors = None
        self._SourceType = None
        self._SourceConfig = None
        self._ContentStatus = None
        self._ContentSHA256 = None
        self._ContentSizeBytes = None
        self._ConfigSHA256 = None
        self._CreatorSubAccountUin = None
        self._ApprovalActions = None
        self._ContentReadyTime = None
        self._ChangeLog = None
        self._LabelSet = None

    @property
    def VersionId(self):
        r"""<p>Version ID；格式 <code>rv-</code> + 8 位小写字母/数字。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def RecordId(self):
        r"""<p>所属 Record ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Revision(self):
        r"""<p>Version 递增序号（1 起）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Revision

    @Revision.setter
    def Revision(self, Revision):
        self._Revision = Revision

    @property
    def Status(self):
        r"""<p>Version 状态。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ApprovalMode(self):
        r"""<p>审批模式；创建时锁定，后续变更 Registry 审批模式不影响本 Version。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApprovalMode

    @ApprovalMode.setter
    def ApprovalMode(self, ApprovalMode):
        self._ApprovalMode = ApprovalMode

    @property
    def AppId(self):
        r"""<p>所属租户 AppId。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CreatorUin(self):
        r"""<p>创建者主账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def CreateTime(self):
        r"""<p>创建时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>最近一次更新时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def VersionName(self):
        r"""<p>Version 别名（可选）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def Descriptors(self):
        r"""<p>协议描述符对象。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Descriptors

    @Descriptors.setter
    def Descriptors(self, Descriptors):
        self._Descriptors = Descriptors

    @property
    def SourceType(self):
        r"""<p>内容来源。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceConfig(self):
        r"""<p>规范化来源配置对象。（JSON 字符串形式）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceConfig

    @SourceConfig.setter
    def SourceConfig(self, SourceConfig):
        self._SourceConfig = SourceConfig

    @property
    def ContentStatus(self):
        r"""<p>内容状态。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContentStatus

    @ContentStatus.setter
    def ContentStatus(self, ContentStatus):
        self._ContentStatus = ContentStatus

    @property
    def ContentSHA256(self):
        r"""<p>READY 内容 SHA-256。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContentSHA256

    @ContentSHA256.setter
    def ContentSHA256(self, ContentSHA256):
        self._ContentSHA256 = ContentSHA256

    @property
    def ContentSizeBytes(self):
        r"""<p>READY 内容字节数。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ContentSizeBytes

    @ContentSizeBytes.setter
    def ContentSizeBytes(self, ContentSizeBytes):
        self._ContentSizeBytes = ContentSizeBytes

    @property
    def ConfigSHA256(self):
        r"""<p>配置内容规范化后的 SHA-256（用于幂等去重）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ConfigSHA256

    @ConfigSHA256.setter
    def ConfigSHA256(self, ConfigSHA256):
        self._ConfigSHA256 = ConfigSHA256

    @property
    def CreatorSubAccountUin(self):
        r"""<p>创建者子账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorSubAccountUin

    @CreatorSubAccountUin.setter
    def CreatorSubAccountUin(self, CreatorSubAccountUin):
        self._CreatorSubAccountUin = CreatorSubAccountUin

    @property
    def ApprovalActions(self):
        r"""<p>Version 历次审批动作。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CloudVersionApprovalAction
        """
        return self._ApprovalActions

    @ApprovalActions.setter
    def ApprovalActions(self, ApprovalActions):
        self._ApprovalActions = ApprovalActions

    @property
    def ContentReadyTime(self):
        r"""<p>TAR 内容成功校验、完成物化并进入 READY 的时间；MANUAL / URL_IMPORT 或尚未 READY 的 TAR_PACKAGE 均为空。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContentReadyTime

    @ContentReadyTime.setter
    def ContentReadyTime(self, ContentReadyTime):
        self._ContentReadyTime = ContentReadyTime

    @property
    def ChangeLog(self):
        r"""<p>本次 Version 的变更原因，最大 4096 字符；不可修改。Revision 1 或未填写时返回空字符串。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ChangeLog

    @ChangeLog.setter
    def ChangeLog(self, ChangeLog):
        self._ChangeLog = ChangeLog

    @property
    def LabelSet(self):
        r"""<p>当前绑定该 Version 的 Label Name 列表（例如 stable / latest 或自定义 Label 名称）。未绑定 Label 不在此返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LabelSet

    @LabelSet.setter
    def LabelSet(self, LabelSet):
        self._LabelSet = LabelSet


    def _deserialize(self, params):
        self._VersionId = params.get("VersionId")
        self._RecordId = params.get("RecordId")
        self._Revision = params.get("Revision")
        self._Status = params.get("Status")
        self._ApprovalMode = params.get("ApprovalMode")
        self._AppId = params.get("AppId")
        self._CreatorUin = params.get("CreatorUin")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._VersionName = params.get("VersionName")
        self._Descriptors = params.get("Descriptors")
        self._SourceType = params.get("SourceType")
        self._SourceConfig = params.get("SourceConfig")
        self._ContentStatus = params.get("ContentStatus")
        self._ContentSHA256 = params.get("ContentSHA256")
        self._ContentSizeBytes = params.get("ContentSizeBytes")
        self._ConfigSHA256 = params.get("ConfigSHA256")
        self._CreatorSubAccountUin = params.get("CreatorSubAccountUin")
        if params.get("ApprovalActions") is not None:
            self._ApprovalActions = []
            for item in params.get("ApprovalActions"):
                obj = CloudVersionApprovalAction()
                obj._deserialize(item)
                self._ApprovalActions.append(obj)
        self._ContentReadyTime = params.get("ContentReadyTime")
        self._ChangeLog = params.get("ChangeLog")
        self._LabelSet = params.get("LabelSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudRegistry(AbstractModel):
    r"""Registry 对象。包含注册中心的基本信息与 Record 计数。

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>Registry ID；格式 <code>reg-</code> + 8 位小写字母/数字。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RegistryId: str
        :param _Name: <p>Registry 同一 AppId + Region 唯一名称。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Description: <p>描述。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ApprovalMode: <p>审批模式；AUTO 自动通过，MANUAL 需人工审批；创建时确定，不可修改。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ApprovalMode: str
        :param _Region: <p>Registry 所在腾讯云地域，如 <code>ap-guangzhou</code>。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Status: <p>Registry 状态。ACTIVE / ARCHIVED。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _CreateTime: <p>创建时间，ISO 8601 UTC，如 <code>2026-08-11T10:00:00Z</code>。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: <p>最近一次更新时间，ISO 8601 UTC。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _RecordCount: <p>Registry 下 Record 总数。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordCount: int
        :param _Tags: <p>权威读取的腾讯云自定义标签，按 Key、Value 稳定排序；无标签时固定返回空数组，不返回 null。</p>
        :type Tags: list of CloudTag
        :param _PublishedRecordCount: <p>Stable Label 已绑定的 Record 数量。Approved Version 数量和可对外消费的 Record 数量已不再等价。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type PublishedRecordCount: int
        :param _AppId: <p>所属租户 AppId。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: int
        :param _CreatorUin: <p>创建者主账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: str
        :param _CreatorSubAccountUin: <p>创建者子账号 UIN；主账号直接创建时为空字符串。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorSubAccountUin: str
        """
        self._RegistryId = None
        self._Name = None
        self._Description = None
        self._ApprovalMode = None
        self._Region = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RecordCount = None
        self._Tags = None
        self._PublishedRecordCount = None
        self._AppId = None
        self._CreatorUin = None
        self._CreatorSubAccountUin = None

    @property
    def RegistryId(self):
        r"""<p>Registry ID；格式 <code>reg-</code> + 8 位小写字母/数字。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        r"""<p>Registry 同一 AppId + Region 唯一名称。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>描述。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ApprovalMode(self):
        r"""<p>审批模式；AUTO 自动通过，MANUAL 需人工审批；创建时确定，不可修改。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ApprovalMode

    @ApprovalMode.setter
    def ApprovalMode(self, ApprovalMode):
        self._ApprovalMode = ApprovalMode

    @property
    def Region(self):
        r"""<p>Registry 所在腾讯云地域，如 <code>ap-guangzhou</code>。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        r"""<p>Registry 状态。ACTIVE / ARCHIVED。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        r"""<p>创建时间，ISO 8601 UTC，如 <code>2026-08-11T10:00:00Z</code>。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>最近一次更新时间，ISO 8601 UTC。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RecordCount(self):
        r"""<p>Registry 下 Record 总数。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def Tags(self):
        r"""<p>权威读取的腾讯云自定义标签，按 Key、Value 稳定排序；无标签时固定返回空数组，不返回 null。</p>
        :rtype: list of CloudTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def PublishedRecordCount(self):
        r"""<p>Stable Label 已绑定的 Record 数量。Approved Version 数量和可对外消费的 Record 数量已不再等价。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PublishedRecordCount

    @PublishedRecordCount.setter
    def PublishedRecordCount(self, PublishedRecordCount):
        self._PublishedRecordCount = PublishedRecordCount

    @property
    def AppId(self):
        r"""<p>所属租户 AppId。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def CreatorUin(self):
        r"""<p>创建者主账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def CreatorSubAccountUin(self):
        r"""<p>创建者子账号 UIN；主账号直接创建时为空字符串。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatorSubAccountUin

    @CreatorSubAccountUin.setter
    def CreatorSubAccountUin(self, CreatorSubAccountUin):
        self._CreatorSubAccountUin = CreatorSubAccountUin


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ApprovalMode = params.get("ApprovalMode")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RecordCount = params.get("RecordCount")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = CloudTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._PublishedRecordCount = params.get("PublishedRecordCount")
        self._AppId = params.get("AppId")
        self._CreatorUin = params.get("CreatorUin")
        self._CreatorSubAccountUin = params.get("CreatorSubAccountUin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudSkillSourceInput(AbstractModel):
    r"""AGENT_SKILLS 内容来源。Type 判别 MANUAL 与 TAR_PACKAGE 两种模式。

    """

    def __init__(self):
        r"""
        :param _Type: <p>来源类型。MANUAL：直接提交 SKILL.md 文本；TAR_PACKAGE：由服务端签发 COS PUT 预签名 URL，客户端上传后由服务端异步校验。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _SkillMd: <p>SKILL.md 原文；Type=MANUAL 时必填非空；Type=TAR_PACKAGE 时不得提供。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SkillMd: str
        """
        self._Type = None
        self._SkillMd = None

    @property
    def Type(self):
        r"""<p>来源类型。MANUAL：直接提交 SKILL.md 文本；TAR_PACKAGE：由服务端签发 COS PUT 预签名 URL，客户端上传后由服务端异步校验。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SkillMd(self):
        r"""<p>SKILL.md 原文；Type=MANUAL 时必填非空；Type=TAR_PACKAGE 时不得提供。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SkillMd

    @SkillMd.setter
    def SkillMd(self, SkillMd):
        self._SkillMd = SkillMd


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._SkillMd = params.get("SkillMd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudTag(AbstractModel):
    r"""腾讯云自定义标签。

    """

    def __init__(self):
        r"""
        :param _Key: <p>自定义标签键；不可使用 qcs:、project 或项目预留前缀，且不可包含首尾空格。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Value: <p>自定义标签值，不可包含首尾空格。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""<p>自定义标签键；不可使用 qcs:、project 或项目预留前缀，且不可包含首尾空格。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""<p>自定义标签值，不可包含首尾空格。</p>
注意：此字段可能返回 null，表示取不到有效值。
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
        


class CloudVersionApprovalAction(AbstractModel):
    r"""Version 一次审批动作条目。

    """

    def __init__(self):
        r"""
        :param _ActionId: <p>动作 ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionId: str
        :param _ActionType: <p>动作类型。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ActionType: str
        :param _ActorType: <p>动作发起者类型。USER 用户；SYSTEM 系统自动通过。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ActorType: str
        :param _ActorUin: <p>发起者主账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ActorUin: str
        :param _ActorSubAccountUin: <p>发起者子账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ActorSubAccountUin: str
        :param _Comment: <p>动作留言。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Comment: str
        :param _CreateTime: <p>发生时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _RequestId: <p>对应云 API 请求的 RequestId。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestId: str
        """
        self._ActionId = None
        self._ActionType = None
        self._ActorType = None
        self._ActorUin = None
        self._ActorSubAccountUin = None
        self._Comment = None
        self._CreateTime = None
        self._RequestId = None

    @property
    def ActionId(self):
        r"""<p>动作 ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActionId

    @ActionId.setter
    def ActionId(self, ActionId):
        self._ActionId = ActionId

    @property
    def ActionType(self):
        r"""<p>动作类型。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ActorType(self):
        r"""<p>动作发起者类型。USER 用户；SYSTEM 系统自动通过。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActorType

    @ActorType.setter
    def ActorType(self, ActorType):
        self._ActorType = ActorType

    @property
    def ActorUin(self):
        r"""<p>发起者主账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActorUin

    @ActorUin.setter
    def ActorUin(self, ActorUin):
        self._ActorUin = ActorUin

    @property
    def ActorSubAccountUin(self):
        r"""<p>发起者子账号 UIN。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ActorSubAccountUin

    @ActorSubAccountUin.setter
    def ActorSubAccountUin(self, ActorSubAccountUin):
        self._ActorSubAccountUin = ActorSubAccountUin

    @property
    def Comment(self):
        r"""<p>动作留言。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment

    @property
    def CreateTime(self):
        r"""<p>发生时间。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def RequestId(self):
        r"""<p>对应云 API 请求的 RequestId。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ActionId = params.get("ActionId")
        self._ActionType = params.get("ActionType")
        self._ActorType = params.get("ActorType")
        self._ActorUin = params.get("ActorUin")
        self._ActorSubAccountUin = params.get("ActorSubAccountUin")
        self._Comment = params.get("Comment")
        self._CreateTime = params.get("CreateTime")
        self._RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComputerConfiguration(AbstractModel):
    r"""桌面电脑环境类沙箱配置

    """

    def __init__(self):
        r"""
        :param _WAAConfiguration: <p>waa沙箱工具配置</p>
        :type WAAConfiguration: :class:`tencentcloud.ags.v20250920.models.WAAConfiguration`
        :param _OSWorldConfiguration: <p>配置内置 OSWorld</p>
        :type OSWorldConfiguration: :class:`tencentcloud.ags.v20250920.models.OSWorldConfiguration`
        """
        self._WAAConfiguration = None
        self._OSWorldConfiguration = None

    @property
    def WAAConfiguration(self):
        r"""<p>waa沙箱工具配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.WAAConfiguration`
        """
        return self._WAAConfiguration

    @WAAConfiguration.setter
    def WAAConfiguration(self, WAAConfiguration):
        self._WAAConfiguration = WAAConfiguration

    @property
    def OSWorldConfiguration(self):
        r"""<p>配置内置 OSWorld</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.OSWorldConfiguration`
        """
        return self._OSWorldConfiguration

    @OSWorldConfiguration.setter
    def OSWorldConfiguration(self, OSWorldConfiguration):
        self._OSWorldConfiguration = OSWorldConfiguration


    def _deserialize(self, params):
        if params.get("WAAConfiguration") is not None:
            self._WAAConfiguration = WAAConfiguration()
            self._WAAConfiguration._deserialize(params.get("WAAConfiguration"))
        if params.get("OSWorldConfiguration") is not None:
            self._OSWorldConfiguration = OSWorldConfiguration()
            self._OSWorldConfiguration._deserialize(params.get("OSWorldConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CosStorageSource(AbstractModel):
    r"""沙箱实例对象存储挂载配置

    """

    def __init__(self):
        r"""
        :param _Endpoint: 对象存储访问域名
        :type Endpoint: str
        :param _BucketName: 对象存储桶名称
        :type BucketName: str
        :param _BucketPath: 对象存储桶路径，必须为以/起始的绝对路径
        :type BucketPath: str
        """
        self._Endpoint = None
        self._BucketName = None
        self._BucketPath = None

    @property
    def Endpoint(self):
        r"""对象存储访问域名
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def BucketName(self):
        r"""对象存储桶名称
        :rtype: str
        """
        return self._BucketName

    @BucketName.setter
    def BucketName(self, BucketName):
        self._BucketName = BucketName

    @property
    def BucketPath(self):
        r"""对象存储桶路径，必须为以/起始的绝对路径
        :rtype: str
        """
        return self._BucketPath

    @BucketPath.setter
    def BucketPath(self, BucketPath):
        self._BucketPath = BucketPath


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._BucketName = params.get("BucketName")
        self._BucketPath = params.get("BucketPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIKeyRequest(AbstractModel):
    r"""CreateAPIKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: API密钥名称，方便用户记忆
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        r"""API密钥名称，方便用户记忆
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAPIKeyResponse(AbstractModel):
    r"""CreateAPIKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 用户传入的API密钥名称，方便用户记忆
        :type Name: str
        :param _APIKey: 生成的API密钥，仅返回此一次，后续无法获取
        :type APIKey: str
        :param _KeyId: API密钥ID
        :type KeyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Name = None
        self._APIKey = None
        self._KeyId = None
        self._RequestId = None

    @property
    def Name(self):
        r"""用户传入的API密钥名称，方便用户记忆
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def APIKey(self):
        r"""生成的API密钥，仅返回此一次，后续无法获取
        :rtype: str
        """
        return self._APIKey

    @APIKey.setter
    def APIKey(self, APIKey):
        self._APIKey = APIKey

    @property
    def KeyId(self):
        r"""API密钥ID
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

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
        self._Name = params.get("Name")
        self._APIKey = params.get("APIKey")
        self._KeyId = params.get("KeyId")
        self._RequestId = params.get("RequestId")


class CreateDeploymentRequest(AbstractModel):
    r"""CreateDeployment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeploymentName: <p>唯一的 Deployment 名称，必须符合 DNS-1123 命名规范，创建后不可修改。</p>
        :type DeploymentName: str
        :param _ToolId: <p>用于关联 Sandbox Tool 的标识，格式为 sdt- 加 8 位小写 base36 字符。</p>
        :type ToolId: str
        :param _ScalingConfiguration: <p>伸缩配置；省略的成员由服务端补全默认值。</p>
        :type ScalingConfiguration: :class:`tencentcloud.ags.v20250920.models.ScalingConfiguration`
        :param _LifecycleConfiguration: <p>空闲生命周期配置；省略的成员由服务端补全默认值。</p>
        :type LifecycleConfiguration: :class:`tencentcloud.ags.v20250920.models.LifecycleConfiguration`
        :param _AffinityConfiguration: <p>Affinity 配置；省略或空 Mode 表示不启用。</p>
        :type AffinityConfiguration: :class:`tencentcloud.ags.v20250920.models.AffinityConfiguration`
        :param _Tags: <p>标签</p>
        :type Tags: list of Tag
        """
        self._DeploymentName = None
        self._ToolId = None
        self._ScalingConfiguration = None
        self._LifecycleConfiguration = None
        self._AffinityConfiguration = None
        self._Tags = None

    @property
    def DeploymentName(self):
        r"""<p>唯一的 Deployment 名称，必须符合 DNS-1123 命名规范，创建后不可修改。</p>
        :rtype: str
        """
        return self._DeploymentName

    @DeploymentName.setter
    def DeploymentName(self, DeploymentName):
        self._DeploymentName = DeploymentName

    @property
    def ToolId(self):
        r"""<p>用于关联 Sandbox Tool 的标识，格式为 sdt- 加 8 位小写 base36 字符。</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ScalingConfiguration(self):
        r"""<p>伸缩配置；省略的成员由服务端补全默认值。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ScalingConfiguration`
        """
        return self._ScalingConfiguration

    @ScalingConfiguration.setter
    def ScalingConfiguration(self, ScalingConfiguration):
        self._ScalingConfiguration = ScalingConfiguration

    @property
    def LifecycleConfiguration(self):
        r"""<p>空闲生命周期配置；省略的成员由服务端补全默认值。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.LifecycleConfiguration`
        """
        return self._LifecycleConfiguration

    @LifecycleConfiguration.setter
    def LifecycleConfiguration(self, LifecycleConfiguration):
        self._LifecycleConfiguration = LifecycleConfiguration

    @property
    def AffinityConfiguration(self):
        r"""<p>Affinity 配置；省略或空 Mode 表示不启用。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.AffinityConfiguration`
        """
        return self._AffinityConfiguration

    @AffinityConfiguration.setter
    def AffinityConfiguration(self, AffinityConfiguration):
        self._AffinityConfiguration = AffinityConfiguration

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DeploymentName = params.get("DeploymentName")
        self._ToolId = params.get("ToolId")
        if params.get("ScalingConfiguration") is not None:
            self._ScalingConfiguration = ScalingConfiguration()
            self._ScalingConfiguration._deserialize(params.get("ScalingConfiguration"))
        if params.get("LifecycleConfiguration") is not None:
            self._LifecycleConfiguration = LifecycleConfiguration()
            self._LifecycleConfiguration._deserialize(params.get("LifecycleConfiguration"))
        if params.get("AffinityConfiguration") is not None:
            self._AffinityConfiguration = AffinityConfiguration()
            self._AffinityConfiguration._deserialize(params.get("AffinityConfiguration"))
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
        


class CreateDeploymentResponse(AbstractModel):
    r"""CreateDeployment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Deployment: <p>已创建并完成默认值物化的 Deployment。</p>
        :type Deployment: :class:`tencentcloud.ags.v20250920.models.Deployment`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Deployment = None
        self._RequestId = None

    @property
    def Deployment(self):
        r"""<p>已创建并完成默认值物化的 Deployment。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.Deployment`
        """
        return self._Deployment

    @Deployment.setter
    def Deployment(self, Deployment):
        self._Deployment = Deployment

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
        if params.get("Deployment") is not None:
            self._Deployment = Deployment()
            self._Deployment._deserialize(params.get("Deployment"))
        self._RequestId = params.get("RequestId")


class CreatePreCacheImageTaskRequest(AbstractModel):
    r"""CreatePreCacheImageTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: <p>镜像地址</p>
        :type Image: str
        :param _ImageRegistryType: <p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>、<code>custom</code></p><p>枚举值：</p><ul><li>enterprise： tcr 企业容器镜像服务</li><li>personal： ccr 个人容器镜像服务</li></ul>
        :type ImageRegistryType: str
        """
        self._Image = None
        self._ImageRegistryType = None

    @property
    def Image(self):
        r"""<p>镜像地址</p>
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ImageRegistryType(self):
        r"""<p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>、<code>custom</code></p><p>枚举值：</p><ul><li>enterprise： tcr 企业容器镜像服务</li><li>personal： ccr 个人容器镜像服务</li></ul>
        :rtype: str
        """
        return self._ImageRegistryType

    @ImageRegistryType.setter
    def ImageRegistryType(self, ImageRegistryType):
        self._ImageRegistryType = ImageRegistryType


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._ImageRegistryType = params.get("ImageRegistryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePreCacheImageTaskResponse(AbstractModel):
    r"""CreatePreCacheImageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: <p>镜像地址</p>
        :type Image: str
        :param _ImageDigest: <p>镜像 Digest</p>
        :type ImageDigest: str
        :param _ImageRegistryType: <p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>。</p>
        :type ImageRegistryType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Image = None
        self._ImageDigest = None
        self._ImageRegistryType = None
        self._RequestId = None

    @property
    def Image(self):
        r"""<p>镜像地址</p>
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ImageDigest(self):
        r"""<p>镜像 Digest</p>
        :rtype: str
        """
        return self._ImageDigest

    @ImageDigest.setter
    def ImageDigest(self, ImageDigest):
        self._ImageDigest = ImageDigest

    @property
    def ImageRegistryType(self):
        r"""<p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>。</p>
        :rtype: str
        """
        return self._ImageRegistryType

    @ImageRegistryType.setter
    def ImageRegistryType(self, ImageRegistryType):
        self._ImageRegistryType = ImageRegistryType

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
        self._Image = params.get("Image")
        self._ImageDigest = params.get("ImageDigest")
        self._ImageRegistryType = params.get("ImageRegistryType")
        self._RequestId = params.get("RequestId")


class CreateRegistryRecordRequest(AbstractModel):
    r"""CreateRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>所属 Registry ID。</p>
        :type RegistryId: str
        :param _Name: <p>Record 名称，长度 1..255，同一租户、Registry 内按规范化 Name 唯一（大小写不敏感）；软删除后允许复用。</p>
        :type Name: str
        :param _DescriptorType: <p>协议描述符类型。MCP / A2A / AGUI / CUSTOM / AGENT_SKILLS。Record 创建后不可修改。</p>
        :type DescriptorType: str
        :param _Description: <p>Record 描述，最大 4096 字符，可选，默认空。</p>
        :type Description: str
        :param _VersionName: <p>Revision 1 的展示名称，可选。</p>
        :type VersionName: str
        :param _MCPSource: <p>DescriptorType=MCP 时必填，其他类型禁止。</p>
        :type MCPSource: :class:`tencentcloud.ags.v20250920.models.CloudMCPSourceInput`
        :param _AgentSource: <p>DescriptorType=A2A 或 AGUI 时必填，其他类型禁止。</p>
        :type AgentSource: :class:`tencentcloud.ags.v20250920.models.CloudAgentSourceInput`
        :param _SkillSource: <p>DescriptorType=AGENT_SKILLS 时必填，其他类型禁止。</p>
        :type SkillSource: :class:`tencentcloud.ags.v20250920.models.CloudSkillSourceInput`
        :param _CustomDescriptors: <p>DescriptorType=CUSTOM 时必填，其他类型禁止。内容必须是 JSON object 字符串；服务端解析后写入 CloudRecordVersion.Descriptors，Version 的 SourceType 固定为 MANUAL、SourceConfig 固定为空对象。</p>
        :type CustomDescriptors: str
        """
        self._RegistryId = None
        self._Name = None
        self._DescriptorType = None
        self._Description = None
        self._VersionName = None
        self._MCPSource = None
        self._AgentSource = None
        self._SkillSource = None
        self._CustomDescriptors = None

    @property
    def RegistryId(self):
        r"""<p>所属 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Name(self):
        r"""<p>Record 名称，长度 1..255，同一租户、Registry 内按规范化 Name 唯一（大小写不敏感）；软删除后允许复用。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def DescriptorType(self):
        r"""<p>协议描述符类型。MCP / A2A / AGUI / CUSTOM / AGENT_SKILLS。Record 创建后不可修改。</p>
        :rtype: str
        """
        return self._DescriptorType

    @DescriptorType.setter
    def DescriptorType(self, DescriptorType):
        self._DescriptorType = DescriptorType

    @property
    def Description(self):
        r"""<p>Record 描述，最大 4096 字符，可选，默认空。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VersionName(self):
        r"""<p>Revision 1 的展示名称，可选。</p>
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def MCPSource(self):
        r"""<p>DescriptorType=MCP 时必填，其他类型禁止。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudMCPSourceInput`
        """
        return self._MCPSource

    @MCPSource.setter
    def MCPSource(self, MCPSource):
        self._MCPSource = MCPSource

    @property
    def AgentSource(self):
        r"""<p>DescriptorType=A2A 或 AGUI 时必填，其他类型禁止。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudAgentSourceInput`
        """
        return self._AgentSource

    @AgentSource.setter
    def AgentSource(self, AgentSource):
        self._AgentSource = AgentSource

    @property
    def SkillSource(self):
        r"""<p>DescriptorType=AGENT_SKILLS 时必填，其他类型禁止。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudSkillSourceInput`
        """
        return self._SkillSource

    @SkillSource.setter
    def SkillSource(self, SkillSource):
        self._SkillSource = SkillSource

    @property
    def CustomDescriptors(self):
        r"""<p>DescriptorType=CUSTOM 时必填，其他类型禁止。内容必须是 JSON object 字符串；服务端解析后写入 CloudRecordVersion.Descriptors，Version 的 SourceType 固定为 MANUAL、SourceConfig 固定为空对象。</p>
        :rtype: str
        """
        return self._CustomDescriptors

    @CustomDescriptors.setter
    def CustomDescriptors(self, CustomDescriptors):
        self._CustomDescriptors = CustomDescriptors


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Name = params.get("Name")
        self._DescriptorType = params.get("DescriptorType")
        self._Description = params.get("Description")
        self._VersionName = params.get("VersionName")
        if params.get("MCPSource") is not None:
            self._MCPSource = CloudMCPSourceInput()
            self._MCPSource._deserialize(params.get("MCPSource"))
        if params.get("AgentSource") is not None:
            self._AgentSource = CloudAgentSourceInput()
            self._AgentSource._deserialize(params.get("AgentSource"))
        if params.get("SkillSource") is not None:
            self._SkillSource = CloudSkillSourceInput()
            self._SkillSource._deserialize(params.get("SkillSource"))
        self._CustomDescriptors = params.get("CustomDescriptors")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRegistryRecordResponse(AbstractModel):
    r"""CreateRegistryRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: <p>新 Record ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordId: str
        :param _Record: <p>新建的 Record 详情。</p>
        :type Record: :class:`tencentcloud.ags.v20250920.models.CloudRecord`
        :param _Version: <p>本次创建的 Revision 1 Version 详情。</p>
        :type Version: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        :param _UploadURL: <p>SkillSource.Type=TAR_PACKAGE 时返回：TAR 包上传预签名 URL。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadURL: str
        :param _ExpireTime: <p>SkillSource.Type=TAR_PACKAGE 时返回：UploadURL 过期时间，ISO 8601 UTC。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _ContentStatus: <p>SkillSource.Type=TAR_PACKAGE 时返回：Version 内容当前状态（UPLOADING 等）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordId = None
        self._Record = None
        self._Version = None
        self._UploadURL = None
        self._ExpireTime = None
        self._ContentStatus = None
        self._RequestId = None

    @property
    def RecordId(self):
        r"""<p>新 Record ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Record(self):
        r"""<p>新建的 Record 详情。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecord`
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def Version(self):
        r"""<p>本次创建的 Revision 1 Version 详情。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UploadURL(self):
        r"""<p>SkillSource.Type=TAR_PACKAGE 时返回：TAR 包上传预签名 URL。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UploadURL

    @UploadURL.setter
    def UploadURL(self, UploadURL):
        self._UploadURL = UploadURL

    @property
    def ExpireTime(self):
        r"""<p>SkillSource.Type=TAR_PACKAGE 时返回：UploadURL 过期时间，ISO 8601 UTC。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ContentStatus(self):
        r"""<p>SkillSource.Type=TAR_PACKAGE 时返回：Version 内容当前状态（UPLOADING 等）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContentStatus

    @ContentStatus.setter
    def ContentStatus(self, ContentStatus):
        self._ContentStatus = ContentStatus

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
        self._RecordId = params.get("RecordId")
        if params.get("Record") is not None:
            self._Record = CloudRecord()
            self._Record._deserialize(params.get("Record"))
        if params.get("Version") is not None:
            self._Version = CloudRecordVersion()
            self._Version._deserialize(params.get("Version"))
        self._UploadURL = params.get("UploadURL")
        self._ExpireTime = params.get("ExpireTime")
        self._ContentStatus = params.get("ContentStatus")
        self._RequestId = params.get("RequestId")


class CreateRegistryRequest(AbstractModel):
    r"""CreateRegistry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>同一 AppId + Region 唯一、长度 1–255</p>
        :type Name: str
        :param _Description: <p>描述文本；最长 4096。</p>
        :type Description: str
        :param _ApprovalMode: <p>审批模式；创建时确定，创建后不可修改；省略时默认为 AUTO，枚举值区分大小写。</p>
        :type ApprovalMode: str
        :param _Tags: <p>创建时绑定的腾讯云自定义标签；Key 不可重复；最多 10 个。</p>
        :type Tags: list of CloudTag
        """
        self._Name = None
        self._Description = None
        self._ApprovalMode = None
        self._Tags = None

    @property
    def Name(self):
        r"""<p>同一 AppId + Region 唯一、长度 1–255</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>描述文本；最长 4096。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ApprovalMode(self):
        r"""<p>审批模式；创建时确定，创建后不可修改；省略时默认为 AUTO，枚举值区分大小写。</p>
        :rtype: str
        """
        return self._ApprovalMode

    @ApprovalMode.setter
    def ApprovalMode(self, ApprovalMode):
        self._ApprovalMode = ApprovalMode

    @property
    def Tags(self):
        r"""<p>创建时绑定的腾讯云自定义标签；Key 不可重复；最多 10 个。</p>
        :rtype: list of CloudTag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._ApprovalMode = params.get("ApprovalMode")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = CloudTag()
                obj._deserialize(item)
                self._Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRegistryResponse(AbstractModel):
    r"""CreateRegistry返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>创建成功的 Registry ID。</p>
        :type RegistryId: str
        :param _Registry: <p>Registry 详细信息。</p>
        :type Registry: :class:`tencentcloud.ags.v20250920.models.CloudRegistry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistryId = None
        self._Registry = None
        self._RequestId = None

    @property
    def RegistryId(self):
        r"""<p>创建成功的 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Registry(self):
        r"""<p>Registry 详细信息。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRegistry`
        """
        return self._Registry

    @Registry.setter
    def Registry(self, Registry):
        self._Registry = Registry

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
        self._RegistryId = params.get("RegistryId")
        if params.get("Registry") is not None:
            self._Registry = CloudRegistry()
            self._Registry._deserialize(params.get("Registry"))
        self._RequestId = params.get("RequestId")


class CreateSandboxToolRequest(AbstractModel):
    r"""CreateSandboxTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ToolName: <p>沙箱工具名称，长度 1-50 字符，支持英文、数字、下划线和连接线。同一 AppId 下沙箱工具名称必须唯一</p>
        :type ToolName: str
        :param _ToolType: <p>沙箱工具类型，目前支持：browser、code-interpreter、custom等</p><p>枚举值：</p><ul><li>browser： browser</li><li>code-interpreter： code-interpreter</li><li>mobile： mobile</li><li>osworld： osworld</li><li>custom： custom</li><li>swebench： swebench</li><li>aio： aio</li><li>android-world： android-world</li><li>waa： waa</li></ul>
        :type ToolType: str
        :param _NetworkConfiguration: <p>网络配置</p>
        :type NetworkConfiguration: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        :param _Description: <p>沙箱工具描述，最大长度 200 字符</p>
        :type Description: str
        :param _DefaultTimeout: <p>默认超时时间，支持格式：5m、300s、1h 等，不指定则使用系统默认值（5 分钟）。最大 24 小时</p>
        :type DefaultTimeout: str
        :param _Tags: <p>标签规格，为沙箱工具绑定标签，支持多种资源类型的标签绑定</p>
        :type Tags: list of Tag
        :param _ClientToken: <p>幂等性 Token，长度不超过 64 字符</p>
        :type ClientToken: str
        :param _RoleArn: <p>角色ARN</p>
        :type RoleArn: str
        :param _StorageMounts: <p>沙箱工具存储配置</p>
        :type StorageMounts: list of StorageMount
        :param _CustomConfiguration: <p>沙箱工具自定义配置</p>
        :type CustomConfiguration: :class:`tencentcloud.ags.v20250920.models.CustomConfiguration`
        :param _ComputerConfiguration: <p>桌面电脑环境类沙箱配置</p>
        :type ComputerConfiguration: :class:`tencentcloud.ags.v20250920.models.ComputerConfiguration`
        :param _LogConfiguration: <p>沙箱工具日志推送相关配置</p>
        :type LogConfiguration: :class:`tencentcloud.ags.v20250920.models.LogConfiguration`
        :param _Persistent: <p>常驻沙箱标识</p>
        :type Persistent: bool
        """
        self._ToolName = None
        self._ToolType = None
        self._NetworkConfiguration = None
        self._Description = None
        self._DefaultTimeout = None
        self._Tags = None
        self._ClientToken = None
        self._RoleArn = None
        self._StorageMounts = None
        self._CustomConfiguration = None
        self._ComputerConfiguration = None
        self._LogConfiguration = None
        self._Persistent = None

    @property
    def ToolName(self):
        r"""<p>沙箱工具名称，长度 1-50 字符，支持英文、数字、下划线和连接线。同一 AppId 下沙箱工具名称必须唯一</p>
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def ToolType(self):
        r"""<p>沙箱工具类型，目前支持：browser、code-interpreter、custom等</p><p>枚举值：</p><ul><li>browser： browser</li><li>code-interpreter： code-interpreter</li><li>mobile： mobile</li><li>osworld： osworld</li><li>custom： custom</li><li>swebench： swebench</li><li>aio： aio</li><li>android-world： android-world</li><li>waa： waa</li></ul>
        :rtype: str
        """
        return self._ToolType

    @ToolType.setter
    def ToolType(self, ToolType):
        self._ToolType = ToolType

    @property
    def NetworkConfiguration(self):
        r"""<p>网络配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        """
        return self._NetworkConfiguration

    @NetworkConfiguration.setter
    def NetworkConfiguration(self, NetworkConfiguration):
        self._NetworkConfiguration = NetworkConfiguration

    @property
    def Description(self):
        r"""<p>沙箱工具描述，最大长度 200 字符</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DefaultTimeout(self):
        r"""<p>默认超时时间，支持格式：5m、300s、1h 等，不指定则使用系统默认值（5 分钟）。最大 24 小时</p>
        :rtype: str
        """
        return self._DefaultTimeout

    @DefaultTimeout.setter
    def DefaultTimeout(self, DefaultTimeout):
        self._DefaultTimeout = DefaultTimeout

    @property
    def Tags(self):
        r"""<p>标签规格，为沙箱工具绑定标签，支持多种资源类型的标签绑定</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ClientToken(self):
        r"""<p>幂等性 Token，长度不超过 64 字符</p>
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def RoleArn(self):
        r"""<p>角色ARN</p>
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def StorageMounts(self):
        r"""<p>沙箱工具存储配置</p>
        :rtype: list of StorageMount
        """
        return self._StorageMounts

    @StorageMounts.setter
    def StorageMounts(self, StorageMounts):
        self._StorageMounts = StorageMounts

    @property
    def CustomConfiguration(self):
        r"""<p>沙箱工具自定义配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CustomConfiguration`
        """
        return self._CustomConfiguration

    @CustomConfiguration.setter
    def CustomConfiguration(self, CustomConfiguration):
        self._CustomConfiguration = CustomConfiguration

    @property
    def ComputerConfiguration(self):
        r"""<p>桌面电脑环境类沙箱配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ComputerConfiguration`
        """
        return self._ComputerConfiguration

    @ComputerConfiguration.setter
    def ComputerConfiguration(self, ComputerConfiguration):
        self._ComputerConfiguration = ComputerConfiguration

    @property
    def LogConfiguration(self):
        r"""<p>沙箱工具日志推送相关配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.LogConfiguration`
        """
        return self._LogConfiguration

    @LogConfiguration.setter
    def LogConfiguration(self, LogConfiguration):
        self._LogConfiguration = LogConfiguration

    @property
    def Persistent(self):
        r"""<p>常驻沙箱标识</p>
        :rtype: bool
        """
        return self._Persistent

    @Persistent.setter
    def Persistent(self, Persistent):
        self._Persistent = Persistent


    def _deserialize(self, params):
        self._ToolName = params.get("ToolName")
        self._ToolType = params.get("ToolType")
        if params.get("NetworkConfiguration") is not None:
            self._NetworkConfiguration = NetworkConfiguration()
            self._NetworkConfiguration._deserialize(params.get("NetworkConfiguration"))
        self._Description = params.get("Description")
        self._DefaultTimeout = params.get("DefaultTimeout")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ClientToken = params.get("ClientToken")
        self._RoleArn = params.get("RoleArn")
        if params.get("StorageMounts") is not None:
            self._StorageMounts = []
            for item in params.get("StorageMounts"):
                obj = StorageMount()
                obj._deserialize(item)
                self._StorageMounts.append(obj)
        if params.get("CustomConfiguration") is not None:
            self._CustomConfiguration = CustomConfiguration()
            self._CustomConfiguration._deserialize(params.get("CustomConfiguration"))
        if params.get("ComputerConfiguration") is not None:
            self._ComputerConfiguration = ComputerConfiguration()
            self._ComputerConfiguration._deserialize(params.get("ComputerConfiguration"))
        if params.get("LogConfiguration") is not None:
            self._LogConfiguration = LogConfiguration()
            self._LogConfiguration._deserialize(params.get("LogConfiguration"))
        self._Persistent = params.get("Persistent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSandboxToolResponse(AbstractModel):
    r"""CreateSandboxTool返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ToolId: <p>创建的沙箱工具 ID</p>
        :type ToolId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ToolId = None
        self._RequestId = None

    @property
    def ToolId(self):
        r"""<p>创建的沙箱工具 ID</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

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
        self._ToolId = params.get("ToolId")
        self._RequestId = params.get("RequestId")


class CreateSessionRequest(AbstractModel):
    r"""CreateSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>会话所属空间 ID。</p>
        :type SpaceId: str
        :param _UserId: <p>用户 ID。可通过调用方业务系统接口获取。</p>
        :type UserId: str
        :param _AgentId: <p>Agent ID。可选。</p>
        :type AgentId: str
        :param _SessionId: <p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :type SessionId: str
        :param _Title: <p>会话标题，最大长度 256 字符。</p>
        :type Title: str
        :param _State: <p>初始会话状态。</p>
        :type State: :class:`tencentcloud.ags.v20250920.models.SessionState`
        :param _Metadata: <p>创建会话时设置的初始元数据，以键值对数组形式表示。每个元素包含 Metadata 名称和对应值。</p><p>入参限制：本参数可选，最多支持 64 项。Name 不能为空或重复，最大长度为 253 字节；Value 最大长度为 1024 字节，允许为空字符串。Metadata 序列化后的总大小不能超过 64 KiB。</p>
        :type Metadata: list of MetadataVar
        """
        self._SpaceId = None
        self._UserId = None
        self._AgentId = None
        self._SessionId = None
        self._Title = None
        self._State = None
        self._Metadata = None

    @property
    def SpaceId(self):
        r"""<p>会话所属空间 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def UserId(self):
        r"""<p>用户 ID。可通过调用方业务系统接口获取。</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def AgentId(self):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        r"""<p>Agent ID。可选。</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        self._AgentId = AgentId

    @property
    def SessionId(self):
        r"""<p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Title(self):
        r"""<p>会话标题，最大长度 256 字符。</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def State(self):
        r"""<p>初始会话状态。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SessionState`
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Metadata(self):
        r"""<p>创建会话时设置的初始元数据，以键值对数组形式表示。每个元素包含 Metadata 名称和对应值。</p><p>入参限制：本参数可选，最多支持 64 项。Name 不能为空或重复，最大长度为 253 字节；Value 最大长度为 1024 字节，允许为空字符串。Metadata 序列化后的总大小不能超过 64 KiB。</p>
        :rtype: list of MetadataVar
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._UserId = params.get("UserId")
        self._AgentId = params.get("AgentId")
        self._SessionId = params.get("SessionId")
        self._Title = params.get("Title")
        if params.get("State") is not None:
            self._State = SessionState()
            self._State._deserialize(params.get("State"))
        if params.get("Metadata") is not None:
            self._Metadata = []
            for item in params.get("Metadata"):
                obj = MetadataVar()
                obj._deserialize(item)
                self._Metadata.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSessionResponse(AbstractModel):
    r"""CreateSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Session: <p>会话信息。</p>
        :type Session: :class:`tencentcloud.ags.v20250920.models.SessionInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        r"""<p>会话信息。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SessionInfo`
        """
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

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
        if params.get("Session") is not None:
            self._Session = SessionInfo()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class CreateSessionSpaceRequest(AbstractModel):
    r"""CreateSessionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>会话空间名称，用于标识会话空间的业务用途。</p><p>入参限制：必填；去除首尾空白后不能为空；最大长度为 128 个字符。</p><p>建议名称包含业务和环境信息，便于识别和管理。</p>
        :type Name: str
        :param _Description: <p>会话空间描述，用于补充说明会话空间的业务用途。</p><p>入参限制：选填；最大长度为 512 个字符。</p><p>未传入时创建为空描述。</p>
        :type Description: str
        :param _Tags: <p>创建 SessionSpace 时为资源绑定标签。</p>
        :type Tags: list of Tag
        """
        self._Name = None
        self._Description = None
        self._Tags = None

    @property
    def Name(self):
        r"""<p>会话空间名称，用于标识会话空间的业务用途。</p><p>入参限制：必填；去除首尾空白后不能为空；最大长度为 128 个字符。</p><p>建议名称包含业务和环境信息，便于识别和管理。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>会话空间描述，用于补充说明会话空间的业务用途。</p><p>入参限制：选填；最大长度为 512 个字符。</p><p>未传入时创建为空描述。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Tags(self):
        r"""<p>创建 SessionSpace 时为资源绑定标签。</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
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
        


class CreateSessionSpaceResponse(AbstractModel):
    r"""CreateSessionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionSpace: <p>创建成功后的会话空间完整信息。</p><p>接口成功时一定返回；接口失败时返回 Error，不会返回该字段。</p>
        :type SessionSpace: :class:`tencentcloud.ags.v20250920.models.SessionSpaceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionSpace = None
        self._RequestId = None

    @property
    def SessionSpace(self):
        r"""<p>创建成功后的会话空间完整信息。</p><p>接口成功时一定返回；接口失败时返回 Error，不会返回该字段。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SessionSpaceInfo`
        """
        return self._SessionSpace

    @SessionSpace.setter
    def SessionSpace(self, SessionSpace):
        self._SessionSpace = SessionSpace

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
        if params.get("SessionSpace") is not None:
            self._SessionSpace = SessionSpaceInfo()
            self._SessionSpace._deserialize(params.get("SessionSpace"))
        self._RequestId = params.get("RequestId")


class CustomConfiguration(AbstractModel):
    r"""沙箱自定义配置

    """

    def __init__(self):
        r"""
        :param _Image: <p>镜像地址</p>
        :type Image: str
        :param _ImageRegistryType: <p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>、<code>custom</code></p><p>枚举值：</p><ul><li>enterprise： tcr 企业容器镜像服务</li><li>personal： ccr 个人容器镜像服务</li></ul>
        :type ImageRegistryType: str
        :param _Command: <p>启动命令</p>
        :type Command: list of str
        :param _Args: <p>启动参数</p>
        :type Args: list of str
        :param _Env: <p>环境变量</p>
        :type Env: list of EnvVar
        :param _Ports: <p>端口配置</p>
        :type Ports: list of PortConfiguration
        :param _Resources: <p>资源配置</p>
        :type Resources: :class:`tencentcloud.ags.v20250920.models.ResourceConfiguration`
        :param _Probe: <p>探针配置</p>
        :type Probe: :class:`tencentcloud.ags.v20250920.models.ProbeConfiguration`
        :param _DNSConfig: <p>沙箱 DNS 配置</p>
        :type DNSConfig: :class:`tencentcloud.ags.v20250920.models.DNSConfig`
        """
        self._Image = None
        self._ImageRegistryType = None
        self._Command = None
        self._Args = None
        self._Env = None
        self._Ports = None
        self._Resources = None
        self._Probe = None
        self._DNSConfig = None

    @property
    def Image(self):
        r"""<p>镜像地址</p>
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ImageRegistryType(self):
        r"""<p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>、<code>custom</code></p><p>枚举值：</p><ul><li>enterprise： tcr 企业容器镜像服务</li><li>personal： ccr 个人容器镜像服务</li></ul>
        :rtype: str
        """
        return self._ImageRegistryType

    @ImageRegistryType.setter
    def ImageRegistryType(self, ImageRegistryType):
        self._ImageRegistryType = ImageRegistryType

    @property
    def Command(self):
        r"""<p>启动命令</p>
        :rtype: list of str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Args(self):
        r"""<p>启动参数</p>
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def Env(self):
        r"""<p>环境变量</p>
        :rtype: list of EnvVar
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Ports(self):
        r"""<p>端口配置</p>
        :rtype: list of PortConfiguration
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Resources(self):
        r"""<p>资源配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ResourceConfiguration`
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Probe(self):
        r"""<p>探针配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ProbeConfiguration`
        """
        return self._Probe

    @Probe.setter
    def Probe(self, Probe):
        self._Probe = Probe

    @property
    def DNSConfig(self):
        r"""<p>沙箱 DNS 配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.DNSConfig`
        """
        return self._DNSConfig

    @DNSConfig.setter
    def DNSConfig(self, DNSConfig):
        self._DNSConfig = DNSConfig


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._ImageRegistryType = params.get("ImageRegistryType")
        self._Command = params.get("Command")
        self._Args = params.get("Args")
        if params.get("Env") is not None:
            self._Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self._Env.append(obj)
        if params.get("Ports") is not None:
            self._Ports = []
            for item in params.get("Ports"):
                obj = PortConfiguration()
                obj._deserialize(item)
                self._Ports.append(obj)
        if params.get("Resources") is not None:
            self._Resources = ResourceConfiguration()
            self._Resources._deserialize(params.get("Resources"))
        if params.get("Probe") is not None:
            self._Probe = ProbeConfiguration()
            self._Probe._deserialize(params.get("Probe"))
        if params.get("DNSConfig") is not None:
            self._DNSConfig = DNSConfig()
            self._DNSConfig._deserialize(params.get("DNSConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomConfigurationDetail(AbstractModel):
    r"""沙箱自定义配置详细信息

    """

    def __init__(self):
        r"""
        :param _Image: <p>镜像地址</p>
        :type Image: str
        :param _ImageRegistryType: <p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>、<code>custom</code>。</p><p>枚举值：</p><ul><li>enterprise： TCR 企业容器镜像服务</li><li>personal： CCR 个人容器镜像服务</li></ul>
        :type ImageRegistryType: str
        :param _ImageDigest: <p>镜像 Digest</p>
        :type ImageDigest: str
        :param _Command: <p>启动命令</p>
        :type Command: list of str
        :param _Args: <p>启动参数</p>
        :type Args: list of str
        :param _Env: <p>环境变量</p>
        :type Env: list of EnvVar
        :param _Ports: <p>端口配置</p>
        :type Ports: list of PortConfiguration
        :param _Resources: <p>资源配置</p>
        :type Resources: :class:`tencentcloud.ags.v20250920.models.ResourceConfiguration`
        :param _Probe: <p>探针配置</p>
        :type Probe: :class:`tencentcloud.ags.v20250920.models.ProbeConfiguration`
        :param _DNSConfig: <p>沙箱 DNS 配置</p>
        :type DNSConfig: :class:`tencentcloud.ags.v20250920.models.DNSConfig`
        """
        self._Image = None
        self._ImageRegistryType = None
        self._ImageDigest = None
        self._Command = None
        self._Args = None
        self._Env = None
        self._Ports = None
        self._Resources = None
        self._Probe = None
        self._DNSConfig = None

    @property
    def Image(self):
        r"""<p>镜像地址</p>
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ImageRegistryType(self):
        r"""<p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>、<code>custom</code>。</p><p>枚举值：</p><ul><li>enterprise： TCR 企业容器镜像服务</li><li>personal： CCR 个人容器镜像服务</li></ul>
        :rtype: str
        """
        return self._ImageRegistryType

    @ImageRegistryType.setter
    def ImageRegistryType(self, ImageRegistryType):
        self._ImageRegistryType = ImageRegistryType

    @property
    def ImageDigest(self):
        r"""<p>镜像 Digest</p>
        :rtype: str
        """
        return self._ImageDigest

    @ImageDigest.setter
    def ImageDigest(self, ImageDigest):
        self._ImageDigest = ImageDigest

    @property
    def Command(self):
        r"""<p>启动命令</p>
        :rtype: list of str
        """
        return self._Command

    @Command.setter
    def Command(self, Command):
        self._Command = Command

    @property
    def Args(self):
        r"""<p>启动参数</p>
        :rtype: list of str
        """
        return self._Args

    @Args.setter
    def Args(self, Args):
        self._Args = Args

    @property
    def Env(self):
        r"""<p>环境变量</p>
        :rtype: list of EnvVar
        """
        return self._Env

    @Env.setter
    def Env(self, Env):
        self._Env = Env

    @property
    def Ports(self):
        r"""<p>端口配置</p>
        :rtype: list of PortConfiguration
        """
        return self._Ports

    @Ports.setter
    def Ports(self, Ports):
        self._Ports = Ports

    @property
    def Resources(self):
        r"""<p>资源配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ResourceConfiguration`
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def Probe(self):
        r"""<p>探针配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ProbeConfiguration`
        """
        return self._Probe

    @Probe.setter
    def Probe(self, Probe):
        self._Probe = Probe

    @property
    def DNSConfig(self):
        r"""<p>沙箱 DNS 配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.DNSConfig`
        """
        return self._DNSConfig

    @DNSConfig.setter
    def DNSConfig(self, DNSConfig):
        self._DNSConfig = DNSConfig


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._ImageRegistryType = params.get("ImageRegistryType")
        self._ImageDigest = params.get("ImageDigest")
        self._Command = params.get("Command")
        self._Args = params.get("Args")
        if params.get("Env") is not None:
            self._Env = []
            for item in params.get("Env"):
                obj = EnvVar()
                obj._deserialize(item)
                self._Env.append(obj)
        if params.get("Ports") is not None:
            self._Ports = []
            for item in params.get("Ports"):
                obj = PortConfiguration()
                obj._deserialize(item)
                self._Ports.append(obj)
        if params.get("Resources") is not None:
            self._Resources = ResourceConfiguration()
            self._Resources._deserialize(params.get("Resources"))
        if params.get("Probe") is not None:
            self._Probe = ProbeConfiguration()
            self._Probe._deserialize(params.get("Probe"))
        if params.get("DNSConfig") is not None:
            self._DNSConfig = DNSConfig()
            self._DNSConfig._deserialize(params.get("DNSConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DNSConfig(AbstractModel):
    r"""沙箱自定义 dns 配置

    """

    def __init__(self):
        r"""
        :param _Servers: <p>DNS 服务器地址</p><p>参数格式：需要有效 IP 地址</p><p>默认值：10.0.0.1</p>
        :type Servers: list of str
        :param _Searches: <p>搜索域(对应 resolv.conf 的 search 指令)</p>
        :type Searches: list of str
        :param _Options: <p>配置项(对应  resolv.conf 选项)</p>
        :type Options: list of str
        """
        self._Servers = None
        self._Searches = None
        self._Options = None

    @property
    def Servers(self):
        r"""<p>DNS 服务器地址</p><p>参数格式：需要有效 IP 地址</p><p>默认值：10.0.0.1</p>
        :rtype: list of str
        """
        return self._Servers

    @Servers.setter
    def Servers(self, Servers):
        self._Servers = Servers

    @property
    def Searches(self):
        r"""<p>搜索域(对应 resolv.conf 的 search 指令)</p>
        :rtype: list of str
        """
        return self._Searches

    @Searches.setter
    def Searches(self, Searches):
        self._Searches = Searches

    @property
    def Options(self):
        r"""<p>配置项(对应  resolv.conf 选项)</p>
        :rtype: list of str
        """
        return self._Options

    @Options.setter
    def Options(self, Options):
        self._Options = Options


    def _deserialize(self, params):
        self._Servers = params.get("Servers")
        self._Searches = params.get("Searches")
        self._Options = params.get("Options")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAPIKeyRequest(AbstractModel):
    r"""DeleteAPIKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyId: 需要删除的API密钥ID
        :type KeyId: str
        """
        self._KeyId = None

    @property
    def KeyId(self):
        r"""需要删除的API密钥ID
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAPIKeyResponse(AbstractModel):
    r"""DeleteAPIKey返回参数结构体

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


class DeleteDeploymentRequest(AbstractModel):
    r"""DeleteDeployment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>待删除的 Deployment ID。</p>
        :type DeploymentId: str
        """
        self._DeploymentId = None

    @property
    def DeploymentId(self):
        r"""<p>待删除的 Deployment ID。</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDeploymentResponse(AbstractModel):
    r"""DeleteDeployment返回参数结构体

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


class DeleteRegistryRecordRequest(AbstractModel):
    r"""DeleteRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>可选。传入时只删除 Record 下指定 Version（软删除）；省略时删除整个 Record。显式传入空字符串或 null 返回 InvalidParameter.VersionId，不得回退为删除整个 Record。</p>
        :type VersionId: str
        :param _Reason: <p>删除原因，最大 1024 字符。删除单个 Version 时必填；删除整个 Record 时可选。</p>
        :type Reason: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._Reason = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>可选。传入时只删除 Record 下指定 Version（软删除）；省略时删除整个 Record。显式传入空字符串或 null 返回 InvalidParameter.VersionId，不得回退为删除整个 Record。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Reason(self):
        r"""<p>删除原因，最大 1024 字符。删除单个 Version 时必填；删除整个 Record 时可选。</p>
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRegistryRecordResponse(AbstractModel):
    r"""DeleteRegistryRecord返回参数结构体

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


class DeleteRegistryRequest(AbstractModel):
    r"""DeleteRegistry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>Registry ID。</p>
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        r"""<p>Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRegistryResponse(AbstractModel):
    r"""DeleteRegistry返回参数结构体

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


class DeleteSandboxToolRequest(AbstractModel):
    r"""DeleteSandboxTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ToolId: 沙箱工具ID
        :type ToolId: str
        """
        self._ToolId = None

    @property
    def ToolId(self):
        r"""沙箱工具ID
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId


    def _deserialize(self, params):
        self._ToolId = params.get("ToolId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSandboxToolResponse(AbstractModel):
    r"""DeleteSandboxTool返回参数结构体

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


class DeleteSessionRequest(AbstractModel):
    r"""DeleteSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>会话所属空间 ID。</p>
        :type SpaceId: str
        :param _UserId: <p>用户 ID。可通过调用方业务系统接口获取。</p>
        :type UserId: str
        :param _SessionId: <p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :type SessionId: str
        :param _AgentId: <p>Agent ID。可选。</p>
        :type AgentId: str
        """
        self._SpaceId = None
        self._UserId = None
        self._SessionId = None
        self._AgentId = None

    @property
    def SpaceId(self):
        r"""<p>会话所属空间 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def UserId(self):
        r"""<p>用户 ID。可通过调用方业务系统接口获取。</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SessionId(self):
        r"""<p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AgentId(self):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        r"""<p>Agent ID。可选。</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        self._AgentId = AgentId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._UserId = params.get("UserId")
        self._SessionId = params.get("SessionId")
        self._AgentId = params.get("AgentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSessionResponse(AbstractModel):
    r"""DeleteSession返回参数结构体

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


class DeleteSessionSpaceRequest(AbstractModel):
    r"""DeleteSessionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>需要删除的会话空间唯一标识。</p>
        :type SpaceId: str
        """
        self._SpaceId = None

    @property
    def SpaceId(self):
        r"""<p>需要删除的会话空间唯一标识。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSessionSpaceResponse(AbstractModel):
    r"""DeleteSessionSpace返回参数结构体

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


class Deployment(AbstractModel):
    r"""Deployment 稳定访问入口定义

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>Deployment 稳定 ID，格式为 dpl- 加 8 位小写 base36 字符。</p>
        :type DeploymentId: str
        :param _DeploymentName: <p>唯一且创建后不可修改的名称，必须符合 DNS-1123 命名规范。</p>
        :type DeploymentName: str
        :param _ToolId: <p>用于关联 Sandbox Tool 的标识，格式为 sdt- 加 8 位小写 base36 字符。</p>
        :type ToolId: str
        :param _ScalingConfiguration: <p>完整的活跃容量配置。</p>
        :type ScalingConfiguration: :class:`tencentcloud.ags.v20250920.models.ScalingConfiguration`
        :param _LifecycleConfiguration: <p>完整的空闲生命周期配置。</p>
        :type LifecycleConfiguration: :class:`tencentcloud.ags.v20250920.models.LifecycleConfiguration`
        :param _AffinityConfiguration: <p>可选 Affinity 配置；未启用时省略。</p>
        :type AffinityConfiguration: :class:`tencentcloud.ags.v20250920.models.AffinityConfiguration`
        :param _Status: <p>Deployment 控制面状态。</p><p>枚举值：</p><ul><li>ACTIVE：入口可用。</li><li>DELETING：入口已关闭并正在异步删除。</li><li>DELETE_FAILED：最近一次异步删除失败，可再次调用 DeleteDeployment。</li></ul>
        :type Status: str
        :param _StatusReason: <p>DELETE_FAILED 状态下 1..1024 个 UTF-8 字节的安全失败摘要，格式为 {Code}[.{SubCode}]: {Message}；其他状态省略。</p>
        :type StatusReason: str
        :param _CreatedTime: <p>创建时间，UTC、秒精度 RFC3339 格式。</p>
        :type CreatedTime: str
        :param _UpdatedTime: <p>最近一次成功公共配置写入或 Deployment 状态迁移时间，UTC、秒精度 RFC3339 格式。</p>
        :type UpdatedTime: str
        :param _Tags: <p>标签</p>
        :type Tags: list of Tag
        """
        self._DeploymentId = None
        self._DeploymentName = None
        self._ToolId = None
        self._ScalingConfiguration = None
        self._LifecycleConfiguration = None
        self._AffinityConfiguration = None
        self._Status = None
        self._StatusReason = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._Tags = None

    @property
    def DeploymentId(self):
        r"""<p>Deployment 稳定 ID，格式为 dpl- 加 8 位小写 base36 字符。</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId

    @property
    def DeploymentName(self):
        r"""<p>唯一且创建后不可修改的名称，必须符合 DNS-1123 命名规范。</p>
        :rtype: str
        """
        return self._DeploymentName

    @DeploymentName.setter
    def DeploymentName(self, DeploymentName):
        self._DeploymentName = DeploymentName

    @property
    def ToolId(self):
        r"""<p>用于关联 Sandbox Tool 的标识，格式为 sdt- 加 8 位小写 base36 字符。</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ScalingConfiguration(self):
        r"""<p>完整的活跃容量配置。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ScalingConfiguration`
        """
        return self._ScalingConfiguration

    @ScalingConfiguration.setter
    def ScalingConfiguration(self, ScalingConfiguration):
        self._ScalingConfiguration = ScalingConfiguration

    @property
    def LifecycleConfiguration(self):
        r"""<p>完整的空闲生命周期配置。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.LifecycleConfiguration`
        """
        return self._LifecycleConfiguration

    @LifecycleConfiguration.setter
    def LifecycleConfiguration(self, LifecycleConfiguration):
        self._LifecycleConfiguration = LifecycleConfiguration

    @property
    def AffinityConfiguration(self):
        r"""<p>可选 Affinity 配置；未启用时省略。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.AffinityConfiguration`
        """
        return self._AffinityConfiguration

    @AffinityConfiguration.setter
    def AffinityConfiguration(self, AffinityConfiguration):
        self._AffinityConfiguration = AffinityConfiguration

    @property
    def Status(self):
        r"""<p>Deployment 控制面状态。</p><p>枚举值：</p><ul><li>ACTIVE：入口可用。</li><li>DELETING：入口已关闭并正在异步删除。</li><li>DELETE_FAILED：最近一次异步删除失败，可再次调用 DeleteDeployment。</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusReason(self):
        r"""<p>DELETE_FAILED 状态下 1..1024 个 UTF-8 字节的安全失败摘要，格式为 {Code}[.{SubCode}]: {Message}；其他状态省略。</p>
        :rtype: str
        """
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason

    @property
    def CreatedTime(self):
        r"""<p>创建时间，UTC、秒精度 RFC3339 格式。</p>
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""<p>最近一次成功公共配置写入或 Deployment 状态迁移时间，UTC、秒精度 RFC3339 格式。</p>
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        self._DeploymentName = params.get("DeploymentName")
        self._ToolId = params.get("ToolId")
        if params.get("ScalingConfiguration") is not None:
            self._ScalingConfiguration = ScalingConfiguration()
            self._ScalingConfiguration._deserialize(params.get("ScalingConfiguration"))
        if params.get("LifecycleConfiguration") is not None:
            self._LifecycleConfiguration = LifecycleConfiguration()
            self._LifecycleConfiguration._deserialize(params.get("LifecycleConfiguration"))
        if params.get("AffinityConfiguration") is not None:
            self._AffinityConfiguration = AffinityConfiguration()
            self._AffinityConfiguration._deserialize(params.get("AffinityConfiguration"))
        self._Status = params.get("Status")
        self._StatusReason = params.get("StatusReason")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
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
        


class DescribeAPIKeyListRequest(AbstractModel):
    r"""DescribeAPIKeyList请求参数结构体

    """


class DescribeAPIKeyListResponse(AbstractModel):
    r"""DescribeAPIKeyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _APIKeySet: API密钥简略信息列表。
        :type APIKeySet: list of APIKeyInfo
        :param _TotalCount: 列表中API密钥数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._APIKeySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def APIKeySet(self):
        r"""API密钥简略信息列表。
        :rtype: list of APIKeyInfo
        """
        return self._APIKeySet

    @APIKeySet.setter
    def APIKeySet(self, APIKeySet):
        self._APIKeySet = APIKeySet

    @property
    def TotalCount(self):
        r"""列表中API密钥数量
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
        if params.get("APIKeySet") is not None:
            self._APIKeySet = []
            for item in params.get("APIKeySet"):
                obj = APIKeyInfo()
                obj._deserialize(item)
                self._APIKeySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDeploymentListRequest(AbstractModel):
    r"""DescribeDeploymentList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: <p>分页偏移量，默认 0，必须大于等于 0。</p>
        :type Offset: int
        :param _Limit: <p>分页返回数量，默认 20，范围 1..200。</p>
        :type Limit: int
        :param _Filters: <p>查询过滤条件。</p><p>Filter.Name 枚举值：</p><ul><li>deployment-id：按 DeploymentId 精确匹配</li><li>deployment-name：按 DeploymentName 精确匹配</li><li>deployment-name-like：按 DeploymentName 进行普通文本包含匹配，%、_ 等字符没有通配语义</li><li>tool-id：按 ToolId 精确匹配</li><li>status：按 Deployment 状态精确匹配，支持 ACTIVE、DELETING、DELETE_FAILED</li></ul><p>所有匹配均区分大小写。不同 Filter 之间为 AND，同一 Filter 的 Values 之间为 OR。</p>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""<p>分页偏移量，默认 0，必须大于等于 0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>分页返回数量，默认 20，范围 1..200。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>查询过滤条件。</p><p>Filter.Name 枚举值：</p><ul><li>deployment-id：按 DeploymentId 精确匹配</li><li>deployment-name：按 DeploymentName 精确匹配</li><li>deployment-name-like：按 DeploymentName 进行普通文本包含匹配，%、_ 等字符没有通配语义</li><li>tool-id：按 ToolId 精确匹配</li><li>status：按 Deployment 状态精确匹配，支持 ACTIVE、DELETING、DELETE_FAILED</li></ul><p>所有匹配均区分大小写。不同 Filter 之间为 AND，同一 Filter 的 Values 之间为 OR。</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeDeploymentListResponse(AbstractModel):
    r"""DescribeDeploymentList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeploymentSet: <p>当前页完整 Deployment；无匹配时为空数组。</p>
        :type DeploymentSet: list of Deployment
        :param _TotalCount: <p>应用 Filters 后、分页前的结果总数。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeploymentSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DeploymentSet(self):
        r"""<p>当前页完整 Deployment；无匹配时为空数组。</p>
        :rtype: list of Deployment
        """
        return self._DeploymentSet

    @DeploymentSet.setter
    def DeploymentSet(self, DeploymentSet):
        self._DeploymentSet = DeploymentSet

    @property
    def TotalCount(self):
        r"""<p>应用 Filters 后、分页前的结果总数。</p>
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
        if params.get("DeploymentSet") is not None:
            self._DeploymentSet = []
            for item in params.get("DeploymentSet"):
                obj = Deployment()
                obj._deserialize(item)
                self._DeploymentSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDeploymentRequest(AbstractModel):
    r"""DescribeDeployment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>待查询的 Deployment ID。</p>
        :type DeploymentId: str
        """
        self._DeploymentId = None

    @property
    def DeploymentId(self):
        r"""<p>待查询的 Deployment ID。</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeploymentResponse(AbstractModel):
    r"""DescribeDeployment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Deployment: <p>完整 Deployment。</p>
        :type Deployment: :class:`tencentcloud.ags.v20250920.models.Deployment`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Deployment = None
        self._RequestId = None

    @property
    def Deployment(self):
        r"""<p>完整 Deployment。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.Deployment`
        """
        return self._Deployment

    @Deployment.setter
    def Deployment(self, Deployment):
        self._Deployment = Deployment

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
        if params.get("Deployment") is not None:
            self._Deployment = Deployment()
            self._Deployment._deserialize(params.get("Deployment"))
        self._RequestId = params.get("RequestId")


class DescribeEventsRequest(AbstractModel):
    r"""DescribeEvents请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>会话所属空间 ID。</p>
        :type SpaceId: str
        :param _UserId: <p>用户 ID。可通过调用方业务系统接口获取。</p>
        :type UserId: str
        :param _SessionId: <p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :type SessionId: str
        :param _AgentId: <p>Agent ID。可选。</p>
        :type AgentId: str
        :param _Author: <p>事件作者。取值示例：user、assistant、tool。</p>
        :type Author: str
        :param _AfterTimestamp: <p>起始时间，仅返回该时间之后的事件，使用 RFC3339 格式，最大长度 64 字符。</p>
        :type AfterTimestamp: str
        :param _Offset: <p>分页偏移量，默认为 0。</p>
        :type Offset: int
        :param _Limit: <p>返回数量，默认为 50，最大值为 200。</p>
        :type Limit: int
        """
        self._SpaceId = None
        self._UserId = None
        self._SessionId = None
        self._AgentId = None
        self._Author = None
        self._AfterTimestamp = None
        self._Offset = None
        self._Limit = None

    @property
    def SpaceId(self):
        r"""<p>会话所属空间 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def UserId(self):
        r"""<p>用户 ID。可通过调用方业务系统接口获取。</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SessionId(self):
        r"""<p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AgentId(self):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        r"""<p>Agent ID。可选。</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        self._AgentId = AgentId

    @property
    def Author(self):
        r"""<p>事件作者。取值示例：user、assistant、tool。</p>
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def AfterTimestamp(self):
        r"""<p>起始时间，仅返回该时间之后的事件，使用 RFC3339 格式，最大长度 64 字符。</p>
        :rtype: str
        """
        return self._AfterTimestamp

    @AfterTimestamp.setter
    def AfterTimestamp(self, AfterTimestamp):
        self._AfterTimestamp = AfterTimestamp

    @property
    def Offset(self):
        r"""<p>分页偏移量，默认为 0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量，默认为 50，最大值为 200。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._UserId = params.get("UserId")
        self._SessionId = params.get("SessionId")
        self._AgentId = params.get("AgentId")
        self._Author = params.get("Author")
        self._AfterTimestamp = params.get("AfterTimestamp")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventsResponse(AbstractModel):
    r"""DescribeEvents返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Events: <p>事件列表。</p>
        :type Events: list of EventInfo
        :param _TotalCount: <p>符合条件的事件总数。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Events = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Events(self):
        r"""<p>事件列表。</p>
        :rtype: list of EventInfo
        """
        return self._Events

    @Events.setter
    def Events(self, Events):
        self._Events = Events

    @property
    def TotalCount(self):
        r"""<p>符合条件的事件总数。</p>
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
        if params.get("Events") is not None:
            self._Events = []
            for item in params.get("Events"):
                obj = EventInfo()
                obj._deserialize(item)
                self._Events.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePreCacheImageTaskRequest(AbstractModel):
    r"""DescribePreCacheImageTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: <p>镜像地址</p>
        :type Image: str
        :param _ImageDigest: <p>镜像 Digest</p>
        :type ImageDigest: str
        :param _ImageRegistryType: <p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>、<code>custom</code> 。</p><p>枚举值：</p><ul><li>enterprise： tcr 企业容器镜像服务</li><li>personal： ccr 个人容器镜像服务</li></ul>
        :type ImageRegistryType: str
        """
        self._Image = None
        self._ImageDigest = None
        self._ImageRegistryType = None

    @property
    def Image(self):
        r"""<p>镜像地址</p>
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ImageDigest(self):
        r"""<p>镜像 Digest</p>
        :rtype: str
        """
        return self._ImageDigest

    @ImageDigest.setter
    def ImageDigest(self, ImageDigest):
        self._ImageDigest = ImageDigest

    @property
    def ImageRegistryType(self):
        r"""<p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>、<code>custom</code> 。</p><p>枚举值：</p><ul><li>enterprise： tcr 企业容器镜像服务</li><li>personal： ccr 个人容器镜像服务</li></ul>
        :rtype: str
        """
        return self._ImageRegistryType

    @ImageRegistryType.setter
    def ImageRegistryType(self, ImageRegistryType):
        self._ImageRegistryType = ImageRegistryType


    def _deserialize(self, params):
        self._Image = params.get("Image")
        self._ImageDigest = params.get("ImageDigest")
        self._ImageRegistryType = params.get("ImageRegistryType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePreCacheImageTaskResponse(AbstractModel):
    r"""DescribePreCacheImageTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Image: <p>镜像地址</p>
        :type Image: str
        :param _ImageDigest: <p>镜像 Digest</p>
        :type ImageDigest: str
        :param _ImageRegistryType: <p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>。</p>
        :type ImageRegistryType: str
        :param _Status: <p>镜像预热状态</p>
        :type Status: str
        :param _Message: <p>镜像预热状态描述</p>
        :type Message: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Image = None
        self._ImageDigest = None
        self._ImageRegistryType = None
        self._Status = None
        self._Message = None
        self._RequestId = None

    @property
    def Image(self):
        r"""<p>镜像地址</p>
        :rtype: str
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def ImageDigest(self):
        r"""<p>镜像 Digest</p>
        :rtype: str
        """
        return self._ImageDigest

    @ImageDigest.setter
    def ImageDigest(self, ImageDigest):
        self._ImageDigest = ImageDigest

    @property
    def ImageRegistryType(self):
        r"""<p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>。</p>
        :rtype: str
        """
        return self._ImageRegistryType

    @ImageRegistryType.setter
    def ImageRegistryType(self, ImageRegistryType):
        self._ImageRegistryType = ImageRegistryType

    @property
    def Status(self):
        r"""<p>镜像预热状态</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Message(self):
        r"""<p>镜像预热状态描述</p>
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

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
        self._Image = params.get("Image")
        self._ImageDigest = params.get("ImageDigest")
        self._ImageRegistryType = params.get("ImageRegistryType")
        self._Status = params.get("Status")
        self._Message = params.get("Message")
        self._RequestId = params.get("RequestId")


class DescribeQuotaOverviewRequest(AbstractModel):
    r"""DescribeQuotaOverview请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: <p>分页偏移量，从 0 开始，默认值为 0，必须大于等于 0。</p><p>单位：偏移量</p>
        :type Offset: int
        :param _Limit: <p>每页返回的配额组数量</p><p>单位：个</p>
        :type Limit: int
        :param _Filters: <p>配额组过滤条件</p>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""<p>分页偏移量，从 0 开始，默认值为 0，必须大于等于 0。</p><p>单位：偏移量</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>每页返回的配额组数量</p><p>单位：个</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>配额组过滤条件</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeQuotaOverviewResponse(AbstractModel):
    r"""DescribeQuotaOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountQuotaOverview: <p>主账号配额上限及全账号当前用量</p>
        :type AccountQuotaOverview: :class:`tencentcloud.ags.v20250920.models.AccountQuotaOverview`
        :param _QuotaGroupSet: <p>当前分页下的配额组配额与用量列表。没有数据时返回空数组。</p>
        :type QuotaGroupSet: list of QuotaGroupOverview
        :param _TotalCount: <p>满足过滤条件的配额组总数，不受当前分页大小影响。</p><p>单位：个</p>
        :type TotalCount: int
        :param _DataTime: <p>本次查询完成时间，格式为 RFC3339</p>
        :type DataTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountQuotaOverview = None
        self._QuotaGroupSet = None
        self._TotalCount = None
        self._DataTime = None
        self._RequestId = None

    @property
    def AccountQuotaOverview(self):
        r"""<p>主账号配额上限及全账号当前用量</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.AccountQuotaOverview`
        """
        return self._AccountQuotaOverview

    @AccountQuotaOverview.setter
    def AccountQuotaOverview(self, AccountQuotaOverview):
        self._AccountQuotaOverview = AccountQuotaOverview

    @property
    def QuotaGroupSet(self):
        r"""<p>当前分页下的配额组配额与用量列表。没有数据时返回空数组。</p>
        :rtype: list of QuotaGroupOverview
        """
        return self._QuotaGroupSet

    @QuotaGroupSet.setter
    def QuotaGroupSet(self, QuotaGroupSet):
        self._QuotaGroupSet = QuotaGroupSet

    @property
    def TotalCount(self):
        r"""<p>满足过滤条件的配额组总数，不受当前分页大小影响。</p><p>单位：个</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataTime(self):
        r"""<p>本次查询完成时间，格式为 RFC3339</p>
        :rtype: str
        """
        return self._DataTime

    @DataTime.setter
    def DataTime(self, DataTime):
        self._DataTime = DataTime

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
        if params.get("AccountQuotaOverview") is not None:
            self._AccountQuotaOverview = AccountQuotaOverview()
            self._AccountQuotaOverview._deserialize(params.get("AccountQuotaOverview"))
        if params.get("QuotaGroupSet") is not None:
            self._QuotaGroupSet = []
            for item in params.get("QuotaGroupSet"):
                obj = QuotaGroupOverview()
                obj._deserialize(item)
                self._QuotaGroupSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._DataTime = params.get("DataTime")
        self._RequestId = params.get("RequestId")


class DescribeRegistryAuditLogListRequest(AbstractModel):
    r"""DescribeRegistryAuditLogList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>Version ID；仅过滤 Version 维度动作，可选。</p>
        :type VersionId: str
        :param _ActionFilter: <p>Action 精确过滤（如 <code>record.version.create</code>），可选。</p>
        :type ActionFilter: str
        :param _Actor: <p>发起者过滤（主账号 UIN 或子账号 UIN），可选。</p>
        :type Actor: str
        :param _StartTime: <p>起始时间；ISO 8601，可选。</p>
        :type StartTime: str
        :param _EndTime: <p>结束时间；ISO 8601，可选。</p>
        :type EndTime: str
        :param _Offset: <p>分页起始偏移，默认 0。</p>
        :type Offset: int
        :param _Limit: <p>分页条数，默认 20，最大 100。</p>
        :type Limit: int
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._ActionFilter = None
        self._Actor = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>Version ID；仅过滤 Version 维度动作，可选。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def ActionFilter(self):
        r"""<p>Action 精确过滤（如 <code>record.version.create</code>），可选。</p>
        :rtype: str
        """
        return self._ActionFilter

    @ActionFilter.setter
    def ActionFilter(self, ActionFilter):
        self._ActionFilter = ActionFilter

    @property
    def Actor(self):
        r"""<p>发起者过滤（主账号 UIN 或子账号 UIN），可选。</p>
        :rtype: str
        """
        return self._Actor

    @Actor.setter
    def Actor(self, Actor):
        self._Actor = Actor

    @property
    def StartTime(self):
        r"""<p>起始时间；ISO 8601，可选。</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>结束时间；ISO 8601，可选。</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        r"""<p>分页起始偏移，默认 0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>分页条数，默认 20，最大 100。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._ActionFilter = params.get("ActionFilter")
        self._Actor = params.get("Actor")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegistryAuditLogListResponse(AbstractModel):
    r"""DescribeRegistryAuditLogList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AuditLogSet: <p>Record 维度的审计日志。</p>
        :type AuditLogSet: list of CloudAuditLog
        :param _TotalCount: <p>符合条件的总数。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AuditLogSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AuditLogSet(self):
        r"""<p>Record 维度的审计日志。</p>
        :rtype: list of CloudAuditLog
        """
        return self._AuditLogSet

    @AuditLogSet.setter
    def AuditLogSet(self, AuditLogSet):
        self._AuditLogSet = AuditLogSet

    @property
    def TotalCount(self):
        r"""<p>符合条件的总数。</p>
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
        if params.get("AuditLogSet") is not None:
            self._AuditLogSet = []
            for item in params.get("AuditLogSet"):
                obj = CloudAuditLog()
                obj._deserialize(item)
                self._AuditLogSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRegistryListRequest(AbstractModel):
    r"""DescribeRegistryList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: <p>分页起始偏移，默认 0。</p>
        :type Offset: int
        :param _Limit: <p>分页条数，默认 20，最大 100。</p>
        :type Limit: int
        :param _Filters: <p>过滤条件。Name 支持：<code>name</code>/<code>search</code>（模糊）、<code>archived</code>/<code>status</code>（true/false/all）、<code>tag-key</code> 和 <code>tag:&lt;key&gt;</code>；最多 6 个标签过滤组，每个标签过滤组最多 10 个 Values，同 Key 多值为 OR，不同 Key 为 AND。</p>
        :type Filters: list of CloudFilter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""<p>分页起始偏移，默认 0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>分页条数，默认 20，最大 100。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤条件。Name 支持：<code>name</code>/<code>search</code>（模糊）、<code>archived</code>/<code>status</code>（true/false/all）、<code>tag-key</code> 和 <code>tag:&lt;key&gt;</code>；最多 6 个标签过滤组，每个标签过滤组最多 10 个 Values，同 Key 多值为 OR，不同 Key 为 AND。</p>
        :rtype: list of CloudFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CloudFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegistryListResponse(AbstractModel):
    r"""DescribeRegistryList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistrySet: <p>Registry 对象数组。</p>
        :type RegistrySet: list of CloudRegistry
        :param _TotalCount: <p>符合条件的总数。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegistrySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RegistrySet(self):
        r"""<p>Registry 对象数组。</p>
        :rtype: list of CloudRegistry
        """
        return self._RegistrySet

    @RegistrySet.setter
    def RegistrySet(self, RegistrySet):
        self._RegistrySet = RegistrySet

    @property
    def TotalCount(self):
        r"""<p>符合条件的总数。</p>
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
        if params.get("RegistrySet") is not None:
            self._RegistrySet = []
            for item in params.get("RegistrySet"):
                obj = CloudRegistry()
                obj._deserialize(item)
                self._RegistrySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRegistryRecordListRequest(AbstractModel):
    r"""DescribeRegistryRecordList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _Offset: <p>分页起始偏移，默认 0。</p>
        :type Offset: int
        :param _Limit: <p>分页条数，默认 20，最大 100。</p>
        :type Limit: int
        :param _Filters: <p>过滤条件。支持 Filter.Name：<code>name</code>/<code>search</code>（按 Record Name 模糊搜索）；其他名称返回 <code>InvalidParameter.Filters.Name</code>。</p>
        :type Filters: list of CloudFilter
        """
        self._RegistryId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Offset(self):
        r"""<p>分页起始偏移，默认 0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>分页条数，默认 20，最大 100。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤条件。支持 Filter.Name：<code>name</code>/<code>search</code>（按 Record Name 模糊搜索）；其他名称返回 <code>InvalidParameter.Filters.Name</code>。</p>
        :rtype: list of CloudFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CloudFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegistryRecordListResponse(AbstractModel):
    r"""DescribeRegistryRecordList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordSet: <p>Record 对象数组。</p>
        :type RecordSet: list of CloudRecord
        :param _TotalCount: <p>符合条件的总数。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def RecordSet(self):
        r"""<p>Record 对象数组。</p>
        :rtype: list of CloudRecord
        """
        return self._RecordSet

    @RecordSet.setter
    def RecordSet(self, RecordSet):
        self._RecordSet = RecordSet

    @property
    def TotalCount(self):
        r"""<p>符合条件的总数。</p>
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
        if params.get("RecordSet") is not None:
            self._RecordSet = []
            for item in params.get("RecordSet"):
                obj = CloudRecord()
                obj._deserialize(item)
                self._RecordSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRegistryRecordRequest(AbstractModel):
    r"""DescribeRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>Version ID，与 Label 互斥。指定时返回该 Version；均省略时等价于 Label=stable。</p>
        :type VersionId: str
        :param _Label: <p>Label 名称，与 VersionId 互斥。指定时返回 Label 当前指向的 Version；均省略时等价于 stable。</p>
        :type Label: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._Label = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>Version ID，与 Label 互斥。指定时返回该 Version；均省略时等价于 Label=stable。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Label(self):
        r"""<p>Label 名称，与 VersionId 互斥。指定时返回 Label 当前指向的 Version；均省略时等价于 stable。</p>
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegistryRecordResponse(AbstractModel):
    r"""DescribeRegistryRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Record: <p>Record 元数据和全部 Label。</p>
        :type Record: :class:`tencentcloud.ags.v20250920.models.CloudRecord`
        :param _Version: <p>根据 VersionId / Label 解析得到的完整 Version。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        :param _ResolvedBy: <p>解析方式：DEFAULT_STABLE / LABEL / VERSION_ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResolvedBy: str
        :param _ResolvedLabel: <p>通过 Label 解析（ResolvedBy=LABEL 或 DEFAULT_STABLE）时返回该 Label 名称，例如 stable。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResolvedLabel: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Record = None
        self._Version = None
        self._ResolvedBy = None
        self._ResolvedLabel = None
        self._RequestId = None

    @property
    def Record(self):
        r"""<p>Record 元数据和全部 Label。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecord`
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def Version(self):
        r"""<p>根据 VersionId / Label 解析得到的完整 Version。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def ResolvedBy(self):
        r"""<p>解析方式：DEFAULT_STABLE / LABEL / VERSION_ID。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResolvedBy

    @ResolvedBy.setter
    def ResolvedBy(self, ResolvedBy):
        self._ResolvedBy = ResolvedBy

    @property
    def ResolvedLabel(self):
        r"""<p>通过 Label 解析（ResolvedBy=LABEL 或 DEFAULT_STABLE）时返回该 Label 名称，例如 stable。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResolvedLabel

    @ResolvedLabel.setter
    def ResolvedLabel(self, ResolvedLabel):
        self._ResolvedLabel = ResolvedLabel

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
        if params.get("Record") is not None:
            self._Record = CloudRecord()
            self._Record._deserialize(params.get("Record"))
        if params.get("Version") is not None:
            self._Version = CloudRecordVersion()
            self._Version._deserialize(params.get("Version"))
        self._ResolvedBy = params.get("ResolvedBy")
        self._ResolvedLabel = params.get("ResolvedLabel")
        self._RequestId = params.get("RequestId")


class DescribeRegistryRecordVersionListRequest(AbstractModel):
    r"""DescribeRegistryRecordVersionList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _Offset: <p>分页起始偏移，默认 0。</p>
        :type Offset: int
        :param _Limit: <p>分页条数，默认 20，最大 100。</p>
        :type Limit: int
        :param _Filters: <p>过滤条件。支持：status（按 Version 状态：PREPARING/PENDING_APPROVAL/APPROVED/REJECTED/CANCELED，多值 OR）、source_type（按内容来源：MANUAL/URL_IMPORT/TAR_PACKAGE，多值 OR）。</p>
        :type Filters: list of CloudFilter
        """
        self._RegistryId = None
        self._RecordId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Offset(self):
        r"""<p>分页起始偏移，默认 0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>分页条数，默认 20，最大 100。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤条件。支持：status（按 Version 状态：PREPARING/PENDING_APPROVAL/APPROVED/REJECTED/CANCELED，多值 OR）、source_type（按内容来源：MANUAL/URL_IMPORT/TAR_PACKAGE，多值 OR）。</p>
        :rtype: list of CloudFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CloudFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegistryRecordVersionListResponse(AbstractModel):
    r"""DescribeRegistryRecordVersionList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _VersionSet: <p>Version 对象数组。</p>
        :type VersionSet: list of CloudRecordVersion
        :param _TotalCount: <p>符合条件的总数。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._VersionSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def VersionSet(self):
        r"""<p>Version 对象数组。</p>
        :rtype: list of CloudRecordVersion
        """
        return self._VersionSet

    @VersionSet.setter
    def VersionSet(self, VersionSet):
        self._VersionSet = VersionSet

    @property
    def TotalCount(self):
        r"""<p>符合条件的总数。</p>
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
        if params.get("VersionSet") is not None:
            self._VersionSet = []
            for item in params.get("VersionSet"):
                obj = CloudRecordVersion()
                obj._deserialize(item)
                self._VersionSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeRegistryRequest(AbstractModel):
    r"""DescribeRegistry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>Registry ID。</p>
        :type RegistryId: str
        """
        self._RegistryId = None

    @property
    def RegistryId(self):
        r"""<p>Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegistryResponse(AbstractModel):
    r"""DescribeRegistry返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Registry: <p>Registry 详情。</p>
        :type Registry: :class:`tencentcloud.ags.v20250920.models.CloudRegistry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Registry = None
        self._RequestId = None

    @property
    def Registry(self):
        r"""<p>Registry 详情。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRegistry`
        """
        return self._Registry

    @Registry.setter
    def Registry(self, Registry):
        self._Registry = Registry

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
        if params.get("Registry") is not None:
            self._Registry = CloudRegistry()
            self._Registry._deserialize(params.get("Registry"))
        self._RequestId = params.get("RequestId")


class DescribeSandboxInstanceListRequest(AbstractModel):
    r"""DescribeSandboxInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: <p>沙箱实例ID列表，指定要查询的实例。如果为空则查询所有实例。最大支持100个ID</p>
        :type InstanceIds: list of str
        :param _ToolId: <p>沙箱工具ID，指定时查询该沙箱模板下的实例，为空则查询所有沙箱模板的实例</p>
        :type ToolId: str
        :param _Offset: <p>偏移量，默认为0</p>
        :type Offset: int
        :param _Limit: <p>返回数量，默认为20，最大值为100</p>
        :type Limit: int
        :param _Filters: <p>过滤条件</p>
        :type Filters: list of Filter
        :param _MaxResults: <p>每次调用返回的最大结果数。如果查询返回的时候有NextToken返回，您可以使用NextToken值获取更多页结果， 当NextToke返回空或者返回的结果数量小于MaxResults时，表示没有更多数据了。允许的最大页面大小为 100。</p>
        :type MaxResults: int
        :param _NextToken: <p>如果NextToken返回非空字符串 ，表示还有更多可用结果。 NextToken是每个页面唯一的分页令牌。使用返回的令牌再次调用以检索下一页。需要保持所有其他参数不变。每个分页令牌在 24 小时后过期。</p>
        :type NextToken: str
        :param _NeedTotalCount: <p>是否返回符合当前查询条件的沙箱实例总数，仅在使用 MaxResults/NextToken 分页时生效。设置为 true 时，首次请求（NextToken 为空）计算并返回精确的 TotalCount；后续使用 NextToken 翻页时返回首次请求计算的 TotalCount，分页期间该值保持不变。重新发起不带 NextToken 的请求时将重新计算。使用 NextToken 翻页时，本参数及其他查询参数必须与首次请求保持一致。默认值为 false，此时 TotalCount 返回 0。</p>
        :type NeedTotalCount: bool
        """
        self._InstanceIds = None
        self._ToolId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._MaxResults = None
        self._NextToken = None
        self._NeedTotalCount = None

    @property
    def InstanceIds(self):
        r"""<p>沙箱实例ID列表，指定要查询的实例。如果为空则查询所有实例。最大支持100个ID</p>
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ToolId(self):
        r"""<p>沙箱工具ID，指定时查询该沙箱模板下的实例，为空则查询所有沙箱模板的实例</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def Offset(self):
        r"""<p>偏移量，默认为0</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量，默认为20，最大值为100</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤条件</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def MaxResults(self):
        r"""<p>每次调用返回的最大结果数。如果查询返回的时候有NextToken返回，您可以使用NextToken值获取更多页结果， 当NextToke返回空或者返回的结果数量小于MaxResults时，表示没有更多数据了。允许的最大页面大小为 100。</p>
        :rtype: int
        """
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def NextToken(self):
        r"""<p>如果NextToken返回非空字符串 ，表示还有更多可用结果。 NextToken是每个页面唯一的分页令牌。使用返回的令牌再次调用以检索下一页。需要保持所有其他参数不变。每个分页令牌在 24 小时后过期。</p>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

    @property
    def NeedTotalCount(self):
        r"""<p>是否返回符合当前查询条件的沙箱实例总数，仅在使用 MaxResults/NextToken 分页时生效。设置为 true 时，首次请求（NextToken 为空）计算并返回精确的 TotalCount；后续使用 NextToken 翻页时返回首次请求计算的 TotalCount，分页期间该值保持不变。重新发起不带 NextToken 的请求时将重新计算。使用 NextToken 翻页时，本参数及其他查询参数必须与首次请求保持一致。默认值为 false，此时 TotalCount 返回 0。</p>
        :rtype: bool
        """
        return self._NeedTotalCount

    @NeedTotalCount.setter
    def NeedTotalCount(self, NeedTotalCount):
        self._NeedTotalCount = NeedTotalCount


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
        self._ToolId = params.get("ToolId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._MaxResults = params.get("MaxResults")
        self._NextToken = params.get("NextToken")
        self._NeedTotalCount = params.get("NeedTotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSandboxInstanceListResponse(AbstractModel):
    r"""DescribeSandboxInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceSet: <p>沙箱实例列表</p>
        :type InstanceSet: list of SandboxInstance
        :param _TotalCount: <p>符合条件的实例总数</p>
        :type TotalCount: int
        :param _NextToken: <p>如果NextToken返回非空字符串 ，表示还有更多可用结果。 NextToken是每个页面唯一的分页令牌。使用返回的令牌再次调用以检索下一页。需要保持所有其他参数不变。每个分页令牌在 24 小时后过期。</p>
        :type NextToken: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._NextToken = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        r"""<p>沙箱实例列表</p>
        :rtype: list of SandboxInstance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TotalCount(self):
        r"""<p>符合条件的实例总数</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def NextToken(self):
        r"""<p>如果NextToken返回非空字符串 ，表示还有更多可用结果。 NextToken是每个页面唯一的分页令牌。使用返回的令牌再次调用以检索下一页。需要保持所有其他参数不变。每个分页令牌在 24 小时后过期。</p>
        :rtype: str
        """
        return self._NextToken

    @NextToken.setter
    def NextToken(self, NextToken):
        self._NextToken = NextToken

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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = SandboxInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._NextToken = params.get("NextToken")
        self._RequestId = params.get("RequestId")


class DescribeSandboxToolListRequest(AbstractModel):
    r"""DescribeSandboxToolList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ToolIds: 沙箱工具ID列表，指定要查询的工具。如果为空则查询所有工具。最大支持100个ID
        :type ToolIds: list of str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._ToolIds = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ToolIds(self):
        r"""沙箱工具ID列表，指定要查询的工具。如果为空则查询所有工具。最大支持100个ID
        :rtype: list of str
        """
        return self._ToolIds

    @ToolIds.setter
    def ToolIds(self, ToolIds):
        self._ToolIds = ToolIds

    @property
    def Offset(self):
        r"""偏移量，默认为0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""返回数量，默认为20，最大值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ToolIds = params.get("ToolIds")
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
        


class DescribeSandboxToolListResponse(AbstractModel):
    r"""DescribeSandboxToolList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SandboxToolSet: 沙箱工具列表
        :type SandboxToolSet: list of SandboxTool
        :param _TotalCount: 符合条件的沙箱工具总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SandboxToolSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SandboxToolSet(self):
        r"""沙箱工具列表
        :rtype: list of SandboxTool
        """
        return self._SandboxToolSet

    @SandboxToolSet.setter
    def SandboxToolSet(self, SandboxToolSet):
        self._SandboxToolSet = SandboxToolSet

    @property
    def TotalCount(self):
        r"""符合条件的沙箱工具总数
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
        if params.get("SandboxToolSet") is not None:
            self._SandboxToolSet = []
            for item in params.get("SandboxToolSet"):
                obj = SandboxTool()
                obj._deserialize(item)
                self._SandboxToolSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSessionRequest(AbstractModel):
    r"""DescribeSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>会话所属空间 ID。</p>
        :type SpaceId: str
        :param _UserId: <p>用户 ID。可通过调用方业务系统接口获取。</p>
        :type UserId: str
        :param _SessionId: <p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :type SessionId: str
        :param _AgentId: <p>Agent ID。可选。</p>
        :type AgentId: str
        :param _NumRecentEvents: <p>返回最近事件数量，默认为 0，最大值为 200。</p>
        :type NumRecentEvents: int
        :param _AfterTimestamp: <p>事件起始时间，RFC3339 格式，最大长度 64 字符。</p>
        :type AfterTimestamp: str
        """
        self._SpaceId = None
        self._UserId = None
        self._SessionId = None
        self._AgentId = None
        self._NumRecentEvents = None
        self._AfterTimestamp = None

    @property
    def SpaceId(self):
        r"""<p>会话所属空间 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def UserId(self):
        r"""<p>用户 ID。可通过调用方业务系统接口获取。</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SessionId(self):
        r"""<p>会话 ID。可通过 CreateSession 或 DescribeSessions 接口获取。</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def AgentId(self):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        r"""<p>Agent ID。可选。</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        self._AgentId = AgentId

    @property
    def NumRecentEvents(self):
        r"""<p>返回最近事件数量，默认为 0，最大值为 200。</p>
        :rtype: int
        """
        return self._NumRecentEvents

    @NumRecentEvents.setter
    def NumRecentEvents(self, NumRecentEvents):
        self._NumRecentEvents = NumRecentEvents

    @property
    def AfterTimestamp(self):
        r"""<p>事件起始时间，RFC3339 格式，最大长度 64 字符。</p>
        :rtype: str
        """
        return self._AfterTimestamp

    @AfterTimestamp.setter
    def AfterTimestamp(self, AfterTimestamp):
        self._AfterTimestamp = AfterTimestamp


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._UserId = params.get("UserId")
        self._SessionId = params.get("SessionId")
        self._AgentId = params.get("AgentId")
        self._NumRecentEvents = params.get("NumRecentEvents")
        self._AfterTimestamp = params.get("AfterTimestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionResponse(AbstractModel):
    r"""DescribeSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Session: <p>会话信息。</p>
        :type Session: :class:`tencentcloud.ags.v20250920.models.SessionInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        r"""<p>会话信息。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SessionInfo`
        """
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

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
        if params.get("Session") is not None:
            self._Session = SessionInfo()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class DescribeSessionSpaceRequest(AbstractModel):
    r"""DescribeSessionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>需要查询的会话空间唯一标识。</p><p>入参限制：必填，不能为空。</p><p>可通过 CreateSessionSpace 或 DescribeSessionSpaces 获取，不应自行构造。</p>
        :type SpaceId: str
        """
        self._SpaceId = None

    @property
    def SpaceId(self):
        r"""<p>需要查询的会话空间唯一标识。</p><p>入参限制：必填，不能为空。</p><p>可通过 CreateSessionSpace 或 DescribeSessionSpaces 获取，不应自行构造。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSessionSpaceResponse(AbstractModel):
    r"""DescribeSessionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionSpace: <p>查询到的会话空间信息。</p>
        :type SessionSpace: :class:`tencentcloud.ags.v20250920.models.SessionSpaceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionSpace = None
        self._RequestId = None

    @property
    def SessionSpace(self):
        r"""<p>查询到的会话空间信息。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SessionSpaceInfo`
        """
        return self._SessionSpace

    @SessionSpace.setter
    def SessionSpace(self, SessionSpace):
        self._SessionSpace = SessionSpace

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
        if params.get("SessionSpace") is not None:
            self._SessionSpace = SessionSpaceInfo()
            self._SessionSpace._deserialize(params.get("SessionSpace"))
        self._RequestId = params.get("RequestId")


class DescribeSessionSpacesRequest(AbstractModel):
    r"""DescribeSessionSpaces请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: <p>分页查询的起始偏移量。</p>
        :type Offset: int
        :param _Limit: <p>单次分页查询返回的会话空间数量。</p>
        :type Limit: int
        :param _Filters: <p>会话空间筛选条件列表，支持按空间 ID 精确匹配、名称精确或模糊匹配、描述模糊匹配。同一 Filter 内多个 Values 之间为 OR，不同 Filter 之间为 AND。不传或传空数组时不增加筛选限制。</p><p>入参限制：Filter.Name 支持 space-id、name、name-like、description-like，不可重复。name 与 name-like 不可同时提供。Values 不可为空数组，筛选值不可为空或纯空白。匹配区分大小写，包含匹配中的 %、_ 按普通字符处理，不具有通配含义。</p><p>例如 Name 为 name-like，Values 为 [&quot;客服&quot;,&quot;测试&quot;]，表示查询名称包含“客服”或“测试”的会话空间。</p>
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        r"""<p>分页查询的起始偏移量。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>单次分页查询返回的会话空间数量。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>会话空间筛选条件列表，支持按空间 ID 精确匹配、名称精确或模糊匹配、描述模糊匹配。同一 Filter 内多个 Values 之间为 OR，不同 Filter 之间为 AND。不传或传空数组时不增加筛选限制。</p><p>入参限制：Filter.Name 支持 space-id、name、name-like、description-like，不可重复。name 与 name-like 不可同时提供。Values 不可为空数组，筛选值不可为空或纯空白。匹配区分大小写，包含匹配中的 %、_ 按普通字符处理，不具有通配含义。</p><p>例如 Name 为 name-like，Values 为 [&quot;客服&quot;,&quot;测试&quot;]，表示查询名称包含“客服”或“测试”的会话空间。</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
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
        


class DescribeSessionSpacesResponse(AbstractModel):
    r"""DescribeSessionSpaces返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionSpaces: <p>会话空间列表。</p>
        :type SessionSpaces: list of SessionSpaceInfo
        :param _TotalCount: <p>满足查询条件的会话空间总数。</p>
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionSpaces = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def SessionSpaces(self):
        r"""<p>会话空间列表。</p>
        :rtype: list of SessionSpaceInfo
        """
        return self._SessionSpaces

    @SessionSpaces.setter
    def SessionSpaces(self, SessionSpaces):
        self._SessionSpaces = SessionSpaces

    @property
    def TotalCount(self):
        r"""<p>满足查询条件的会话空间总数。</p>
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
        if params.get("SessionSpaces") is not None:
            self._SessionSpaces = []
            for item in params.get("SessionSpaces"):
                obj = SessionSpaceInfo()
                obj._deserialize(item)
                self._SessionSpaces.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSessionsRequest(AbstractModel):
    r"""DescribeSessions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>查询的会话空间 ID。</p>
        :type SpaceId: str
        :param _AgentIds: <p>Agent ID 列表，最多支持 100 个。</p>
        :type AgentIds: list of str
        :param _UserIds: <p>用户 ID 列表，最多支持 100 个。</p>
        :type UserIds: list of str
        :param _Offset: <p>分页偏移量，默认为 0。</p>
        :type Offset: int
        :param _Limit: <p>返回数量，默认为 20，最大值为 100。</p>
        :type Limit: int
        :param _SessionIds: <p>会话 ID 列表，最多支持 100 个。</p>
        :type SessionIds: list of str
        :param _Filters: <p>会话筛选条件列表，支持 Metadata 精确匹配、标题精确匹配和标题模糊匹配。同一 Filter 内多个 Values 之间为 OR，不同 Filter 之间为 AND。不传或传空数组时不增加筛选限制。</p><p>入参限制：最多传入 10 个 Filter，每个 Filter 最多支持 100 个 Values。Filter.Name 不可重复，支持 metadata:MetadataKey、title、title-like；title 与 title-like 不可同时提供。标题筛选值不可为空或纯空白。匹配区分大小写，标题包含匹配中的 %、_ 按普通字符处理，不具有通配含义。</p><p>例如 Name 为 title-like，Values 为 [&quot;客服&quot;,&quot;测试&quot;]，表示查询标题包含“客服”或“测试”的会话。Name 为 metadata:env，Values 为 [&quot;dev&quot;,&quot;test&quot;]，表示按 Metadata env 的值精确筛选。标题条件与 Metadata、SessionIds、UserIds 筛选条件可组合使用，条件之间为 AND。筛选在分页前执行，TotalCount 为符合条件的会话总数。</p>
        :type Filters: list of Filter
        """
        self._SpaceId = None
        self._AgentIds = None
        self._UserIds = None
        self._Offset = None
        self._Limit = None
        self._SessionIds = None
        self._Filters = None

    @property
    def SpaceId(self):
        r"""<p>查询的会话空间 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def AgentIds(self):
        warnings.warn("parameter `AgentIds` is deprecated", DeprecationWarning) 

        r"""<p>Agent ID 列表，最多支持 100 个。</p>
        :rtype: list of str
        """
        return self._AgentIds

    @AgentIds.setter
    def AgentIds(self, AgentIds):
        warnings.warn("parameter `AgentIds` is deprecated", DeprecationWarning) 

        self._AgentIds = AgentIds

    @property
    def UserIds(self):
        r"""<p>用户 ID 列表，最多支持 100 个。</p>
        :rtype: list of str
        """
        return self._UserIds

    @UserIds.setter
    def UserIds(self, UserIds):
        self._UserIds = UserIds

    @property
    def Offset(self):
        r"""<p>分页偏移量，默认为 0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>返回数量，默认为 20，最大值为 100。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SessionIds(self):
        r"""<p>会话 ID 列表，最多支持 100 个。</p>
        :rtype: list of str
        """
        return self._SessionIds

    @SessionIds.setter
    def SessionIds(self, SessionIds):
        self._SessionIds = SessionIds

    @property
    def Filters(self):
        r"""<p>会话筛选条件列表，支持 Metadata 精确匹配、标题精确匹配和标题模糊匹配。同一 Filter 内多个 Values 之间为 OR，不同 Filter 之间为 AND。不传或传空数组时不增加筛选限制。</p><p>入参限制：最多传入 10 个 Filter，每个 Filter 最多支持 100 个 Values。Filter.Name 不可重复，支持 metadata:MetadataKey、title、title-like；title 与 title-like 不可同时提供。标题筛选值不可为空或纯空白。匹配区分大小写，标题包含匹配中的 %、_ 按普通字符处理，不具有通配含义。</p><p>例如 Name 为 title-like，Values 为 [&quot;客服&quot;,&quot;测试&quot;]，表示查询标题包含“客服”或“测试”的会话。Name 为 metadata:env，Values 为 [&quot;dev&quot;,&quot;test&quot;]，表示按 Metadata env 的值精确筛选。标题条件与 Metadata、SessionIds、UserIds 筛选条件可组合使用，条件之间为 AND。筛选在分页前执行，TotalCount 为符合条件的会话总数。</p>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._AgentIds = params.get("AgentIds")
        self._UserIds = params.get("UserIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SessionIds = params.get("SessionIds")
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
        


class DescribeSessionsResponse(AbstractModel):
    r"""DescribeSessions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>符合条件的会话总数。</p>
        :type TotalCount: int
        :param _Sessions: <p>会话列表。</p>
        :type Sessions: list of SessionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Sessions = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>符合条件的会话总数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Sessions(self):
        r"""<p>会话列表。</p>
        :rtype: list of SessionInfo
        """
        return self._Sessions

    @Sessions.setter
    def Sessions(self, Sessions):
        self._Sessions = Sessions

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
        if params.get("Sessions") is not None:
            self._Sessions = []
            for item in params.get("Sessions"):
                obj = SessionInfo()
                obj._deserialize(item)
                self._Sessions.append(obj)
        self._RequestId = params.get("RequestId")


class EnvVar(AbstractModel):
    r"""环境变量

    """

    def __init__(self):
        r"""
        :param _Name: 环境变量名
        :type Name: str
        :param _Value: 环境变量值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""环境变量名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""环境变量值
        :rtype: str
        """
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
        


class EventActionsInfo(AbstractModel):
    r"""Agent 状态切换事件信息

    """

    def __init__(self):
        r"""
        :param _StateDelta: 状态增量，JSON 字符串，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type StateDelta: str
        """
        self._StateDelta = None

    @property
    def StateDelta(self):
        r"""状态增量，JSON 字符串，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StateDelta

    @StateDelta.setter
    def StateDelta(self, StateDelta):
        self._StateDelta = StateDelta


    def _deserialize(self, params):
        self._StateDelta = params.get("StateDelta")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventContentInfo(AbstractModel):
    r"""事件内容信息

    """

    def __init__(self):
        r"""
        :param _Role: 角色，最大长度 64 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _Parts: 内容片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Parts: list of EventPartInfo
        """
        self._Role = None
        self._Parts = None

    @property
    def Role(self):
        r"""角色，最大长度 64 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Parts(self):
        r"""内容片段列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of EventPartInfo
        """
        return self._Parts

    @Parts.setter
    def Parts(self, Parts):
        self._Parts = Parts


    def _deserialize(self, params):
        self._Role = params.get("Role")
        if params.get("Parts") is not None:
            self._Parts = []
            for item in params.get("Parts"):
                obj = EventPartInfo()
                obj._deserialize(item)
                self._Parts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventInfo(AbstractModel):
    r"""事件信息

    """

    def __init__(self):
        r"""
        :param _EventId: <p>事件 ID。为空时由服务生成。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type EventId: str
        :param _InvocationId: <p>调用 ID，最大长度 128 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type InvocationId: str
        :param _Author: <p>事件作者，最大长度 128 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Author: str
        :param _Content: <p>事件内容。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: :class:`tencentcloud.ags.v20250920.models.EventContentInfo`
        :param _Actions: <p>事件动作信息。StateDelta 为 JSON 对象字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Actions: :class:`tencentcloud.ags.v20250920.models.EventActionsInfo`
        :param _Metadata: <p>事件元数据。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Metadata: str
        :param _Extensions: <p>事件扩展信息 JSON 对象字符串，最大长度 8192 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Extensions: str
        :param _ErrorCode: <p>错误码，最大长度 128 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param _ErrorMessage: <p>错误信息，最大长度 2048 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _Timestamp: <p>事件时间。</p>
        :type Timestamp: str
        """
        self._EventId = None
        self._InvocationId = None
        self._Author = None
        self._Content = None
        self._Actions = None
        self._Metadata = None
        self._Extensions = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._Timestamp = None

    @property
    def EventId(self):
        r"""<p>事件 ID。为空时由服务生成。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EventId

    @EventId.setter
    def EventId(self, EventId):
        self._EventId = EventId

    @property
    def InvocationId(self):
        r"""<p>调用 ID，最大长度 128 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def Author(self):
        r"""<p>事件作者，最大长度 128 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Author

    @Author.setter
    def Author(self, Author):
        self._Author = Author

    @property
    def Content(self):
        r"""<p>事件内容。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ags.v20250920.models.EventContentInfo`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Actions(self):
        r"""<p>事件动作信息。StateDelta 为 JSON 对象字符串</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ags.v20250920.models.EventActionsInfo`
        """
        return self._Actions

    @Actions.setter
    def Actions(self, Actions):
        self._Actions = Actions

    @property
    def Metadata(self):
        r"""<p>事件元数据。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def Extensions(self):
        r"""<p>事件扩展信息 JSON 对象字符串，最大长度 8192 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Extensions

    @Extensions.setter
    def Extensions(self, Extensions):
        self._Extensions = Extensions

    @property
    def ErrorCode(self):
        r"""<p>错误码，最大长度 128 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>错误信息，最大长度 2048 字符。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def Timestamp(self):
        r"""<p>事件时间。</p>
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp


    def _deserialize(self, params):
        self._EventId = params.get("EventId")
        self._InvocationId = params.get("InvocationId")
        self._Author = params.get("Author")
        if params.get("Content") is not None:
            self._Content = EventContentInfo()
            self._Content._deserialize(params.get("Content"))
        if params.get("Actions") is not None:
            self._Actions = EventActionsInfo()
            self._Actions._deserialize(params.get("Actions"))
        self._Metadata = params.get("Metadata")
        self._Extensions = params.get("Extensions")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._Timestamp = params.get("Timestamp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventPartInfo(AbstractModel):
    r"""多模态内容片段信息

    """

    def __init__(self):
        r"""
        :param _Text: 文本内容，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _Thought: 是否为思考内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Thought: bool
        :param _FunctionCall: 工具调用信息，JSON 字符串，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionCall: str
        :param _FunctionResponse: 工具返回信息，JSON 字符串，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type FunctionResponse: str
        :param _InlineData: 内联数据。
注意：此字段可能返回 null，表示取不到有效值。
        :type InlineData: :class:`tencentcloud.ags.v20250920.models.InlineDataInfo`
        """
        self._Text = None
        self._Thought = None
        self._FunctionCall = None
        self._FunctionResponse = None
        self._InlineData = None

    @property
    def Text(self):
        r"""文本内容，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Thought(self):
        r"""是否为思考内容。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Thought

    @Thought.setter
    def Thought(self, Thought):
        self._Thought = Thought

    @property
    def FunctionCall(self):
        r"""工具调用信息，JSON 字符串，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FunctionCall

    @FunctionCall.setter
    def FunctionCall(self, FunctionCall):
        self._FunctionCall = FunctionCall

    @property
    def FunctionResponse(self):
        r"""工具返回信息，JSON 字符串，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FunctionResponse

    @FunctionResponse.setter
    def FunctionResponse(self, FunctionResponse):
        self._FunctionResponse = FunctionResponse

    @property
    def InlineData(self):
        r"""内联数据。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ags.v20250920.models.InlineDataInfo`
        """
        return self._InlineData

    @InlineData.setter
    def InlineData(self, InlineData):
        self._InlineData = InlineData


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Thought = params.get("Thought")
        self._FunctionCall = params.get("FunctionCall")
        self._FunctionResponse = params.get("FunctionResponse")
        if params.get("InlineData") is not None:
            self._InlineData = InlineDataInfo()
            self._InlineData._deserialize(params.get("InlineData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    r"""过滤列表规则

    """

    def __init__(self):
        r"""
        :param _Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param _Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
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
        


class GetSkillPackageDownloadURLRequest(AbstractModel):
    r"""GetSkillPackageDownloadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID；必须 AGENT_SKILLS 且 ContentStatus=READY。</p>
        :type RecordId: str
        :param _VersionId: <p>可选。指定要下载的 Version；与 Label 互斥；均省略时使用 Stable。</p>
        :type VersionId: str
        :param _Label: <p>可选。指定要下载的 Label 目标；与 VersionId 互斥；均省略时使用 Stable。</p>
        :type Label: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._Label = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID；必须 AGENT_SKILLS 且 ContentStatus=READY。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>可选。指定要下载的 Version；与 Label 互斥；均省略时使用 Stable。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Label(self):
        r"""<p>可选。指定要下载的 Label 目标；与 VersionId 互斥；均省略时使用 Stable。</p>
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSkillPackageDownloadURLResponse(AbstractModel):
    r"""GetSkillPackageDownloadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DownloadURL: <p>COS GET 预签名 URL；带 response-content-disposition；默认 TTL 5 分钟；bearer 凭证禁止持久化。</p>
        :type DownloadURL: str
        :param _ExpireTime: <p>URL 过期时间。</p>
        :type ExpireTime: str
        :param _SHA256: <p>服务端记录的 SHA-256；下载后应本地自检。</p>
        :type SHA256: str
        :param _ResolvedVersionId: <p>解析出的 Version ID（Stable Version）。</p>
        :type ResolvedVersionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DownloadURL = None
        self._ExpireTime = None
        self._SHA256 = None
        self._ResolvedVersionId = None
        self._RequestId = None

    @property
    def DownloadURL(self):
        r"""<p>COS GET 预签名 URL；带 response-content-disposition；默认 TTL 5 分钟；bearer 凭证禁止持久化。</p>
        :rtype: str
        """
        return self._DownloadURL

    @DownloadURL.setter
    def DownloadURL(self, DownloadURL):
        self._DownloadURL = DownloadURL

    @property
    def ExpireTime(self):
        r"""<p>URL 过期时间。</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SHA256(self):
        r"""<p>服务端记录的 SHA-256；下载后应本地自检。</p>
        :rtype: str
        """
        return self._SHA256

    @SHA256.setter
    def SHA256(self, SHA256):
        self._SHA256 = SHA256

    @property
    def ResolvedVersionId(self):
        r"""<p>解析出的 Version ID（Stable Version）。</p>
        :rtype: str
        """
        return self._ResolvedVersionId

    @ResolvedVersionId.setter
    def ResolvedVersionId(self, ResolvedVersionId):
        self._ResolvedVersionId = ResolvedVersionId

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
        self._DownloadURL = params.get("DownloadURL")
        self._ExpireTime = params.get("ExpireTime")
        self._SHA256 = params.get("SHA256")
        self._ResolvedVersionId = params.get("ResolvedVersionId")
        self._RequestId = params.get("RequestId")


class GetSkillPackageUploadURLRequest(AbstractModel):
    r"""GetSkillPackageUploadURL请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>Version ID；格式 <code>rv-</code> + 8 位小写字母/数字。</p>
        :type VersionId: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>Version ID；格式 <code>rv-</code> + 8 位小写字母/数字。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSkillPackageUploadURLResponse(AbstractModel):
    r"""GetSkillPackageUploadURL返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: <p>Version 详情（Revision 不变）。</p>
        :type Version: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        :param _UploadURL: <p>新的 COS PUT 预签名 URL。</p>
        :type UploadURL: str
        :param _ContentStatus: <p>重试后的内容状态。</p>
        :type ContentStatus: str
        :param _ExpireTime: <p>UploadURL 过期时间。</p>
        :type ExpireTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._UploadURL = None
        self._ContentStatus = None
        self._ExpireTime = None
        self._RequestId = None

    @property
    def Version(self):
        r"""<p>Version 详情（Revision 不变）。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UploadURL(self):
        r"""<p>新的 COS PUT 预签名 URL。</p>
        :rtype: str
        """
        return self._UploadURL

    @UploadURL.setter
    def UploadURL(self, UploadURL):
        self._UploadURL = UploadURL

    @property
    def ContentStatus(self):
        r"""<p>重试后的内容状态。</p>
        :rtype: str
        """
        return self._ContentStatus

    @ContentStatus.setter
    def ContentStatus(self, ContentStatus):
        self._ContentStatus = ContentStatus

    @property
    def ExpireTime(self):
        r"""<p>UploadURL 过期时间。</p>
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

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
        if params.get("Version") is not None:
            self._Version = CloudRecordVersion()
            self._Version._deserialize(params.get("Version"))
        self._UploadURL = params.get("UploadURL")
        self._ContentStatus = params.get("ContentStatus")
        self._ExpireTime = params.get("ExpireTime")
        self._RequestId = params.get("RequestId")


class HttpGetAction(AbstractModel):
    r"""HTTP GET 探测动作配置

    """

    def __init__(self):
        r"""
        :param _Path: 路径
        :type Path: str
        :param _Port: 端口
        :type Port: int
        :param _Scheme: 协议
        :type Scheme: str
        """
        self._Path = None
        self._Port = None
        self._Scheme = None

    @property
    def Path(self):
        r"""路径
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Port(self):
        r"""端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Scheme(self):
        r"""协议
        :rtype: str
        """
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme


    def _deserialize(self, params):
        self._Path = params.get("Path")
        self._Port = params.get("Port")
        self._Scheme = params.get("Scheme")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageStorageSource(AbstractModel):
    r"""镜像卷挂载源配置

    """

    def __init__(self):
        r"""
        :param _Reference: <p>镜像地址</p>
        :type Reference: str
        :param _ImageRegistryType: <p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>。</p>
        :type ImageRegistryType: str
        :param _SubPath: <p>镜像内部的路径</p>
        :type SubPath: str
        :param _Digest: <p>镜像 Digest，请求时无需传入</p>
        :type Digest: str
        """
        self._Reference = None
        self._ImageRegistryType = None
        self._SubPath = None
        self._Digest = None

    @property
    def Reference(self):
        r"""<p>镜像地址</p>
        :rtype: str
        """
        return self._Reference

    @Reference.setter
    def Reference(self, Reference):
        self._Reference = Reference

    @property
    def ImageRegistryType(self):
        r"""<p>镜像仓库类型：<code>enterprise</code>、<code>personal</code>。</p>
        :rtype: str
        """
        return self._ImageRegistryType

    @ImageRegistryType.setter
    def ImageRegistryType(self, ImageRegistryType):
        self._ImageRegistryType = ImageRegistryType

    @property
    def SubPath(self):
        r"""<p>镜像内部的路径</p>
        :rtype: str
        """
        return self._SubPath

    @SubPath.setter
    def SubPath(self, SubPath):
        self._SubPath = SubPath

    @property
    def Digest(self):
        r"""<p>镜像 Digest，请求时无需传入</p>
        :rtype: str
        """
        return self._Digest

    @Digest.setter
    def Digest(self, Digest):
        self._Digest = Digest


    def _deserialize(self, params):
        self._Reference = params.get("Reference")
        self._ImageRegistryType = params.get("ImageRegistryType")
        self._SubPath = params.get("SubPath")
        self._Digest = params.get("Digest")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InlineDataInfo(AbstractModel):
    r"""文件内容数据信息

    """

    def __init__(self):
        r"""
        :param _MimeType: 媒体类型，最大长度 128 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type MimeType: str
        :param _Data: Base64 编码数据，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: str
        """
        self._MimeType = None
        self._Data = None

    @property
    def MimeType(self):
        r"""媒体类型，最大长度 128 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MimeType

    @MimeType.setter
    def MimeType(self, MimeType):
        self._MimeType = MimeType

    @property
    def Data(self):
        r"""Base64 编码数据，最大长度 8192 字符。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data


    def _deserialize(self, params):
        self._MimeType = params.get("MimeType")
        self._Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LifecycleConfiguration(AbstractModel):
    r"""Deployment 管理的 Sandbox Instance 的空闲生命周期配置

    """

    def __init__(self):
        r"""
        :param _IdleTimeoutSeconds: <p>Sandbox Instance 没有活跃 Deployment 请求或连接后进入 IdleAction 的秒数，必须大于等于 30。</p>
        :type IdleTimeoutSeconds: int
        :param _IdleAction: <p>空闲处理动作。</p><p>枚举值：</p><ul><li>STOP：停止并释放 Sandbox Instance。</li><li>PAUSE：暂停并保留 Sandbox Instance 状态。</li></ul>
        :type IdleAction: str
        """
        self._IdleTimeoutSeconds = None
        self._IdleAction = None

    @property
    def IdleTimeoutSeconds(self):
        r"""<p>Sandbox Instance 没有活跃 Deployment 请求或连接后进入 IdleAction 的秒数，必须大于等于 30。</p>
        :rtype: int
        """
        return self._IdleTimeoutSeconds

    @IdleTimeoutSeconds.setter
    def IdleTimeoutSeconds(self, IdleTimeoutSeconds):
        self._IdleTimeoutSeconds = IdleTimeoutSeconds

    @property
    def IdleAction(self):
        r"""<p>空闲处理动作。</p><p>枚举值：</p><ul><li>STOP：停止并释放 Sandbox Instance。</li><li>PAUSE：暂停并保留 Sandbox Instance 状态。</li></ul>
        :rtype: str
        """
        return self._IdleAction

    @IdleAction.setter
    def IdleAction(self, IdleAction):
        self._IdleAction = IdleAction


    def _deserialize(self, params):
        self._IdleTimeoutSeconds = params.get("IdleTimeoutSeconds")
        self._IdleAction = params.get("IdleAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogConfiguration(AbstractModel):
    r"""沙箱工具日志采集相关配置

    """

    def __init__(self):
        r"""
        :param _CLSConfig: <p>日志推送CLS的配置。</p>
        :type CLSConfig: :class:`tencentcloud.ags.v20250920.models.CLSConfig`
        :param _LogSources: <p>日志源配置</p>
        :type LogSources: :class:`tencentcloud.ags.v20250920.models.LogSources`
        """
        self._CLSConfig = None
        self._LogSources = None

    @property
    def CLSConfig(self):
        r"""<p>日志推送CLS的配置。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CLSConfig`
        """
        return self._CLSConfig

    @CLSConfig.setter
    def CLSConfig(self, CLSConfig):
        self._CLSConfig = CLSConfig

    @property
    def LogSources(self):
        r"""<p>日志源配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.LogSources`
        """
        return self._LogSources

    @LogSources.setter
    def LogSources(self, LogSources):
        self._LogSources = LogSources


    def _deserialize(self, params):
        if params.get("CLSConfig") is not None:
            self._CLSConfig = CLSConfig()
            self._CLSConfig._deserialize(params.get("CLSConfig"))
        if params.get("LogSources") is not None:
            self._LogSources = LogSources()
            self._LogSources._deserialize(params.get("LogSources"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogSources(AbstractModel):
    r"""日志源配置

    """

    def __init__(self):
        r"""
        :param _Files: <p>需要采集的日志文件路径，必须是 /logs/ 目录下的文件，不支持子目录，最大支持 10 个文件。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Files: list of str
        """
        self._Files = None

    @property
    def Files(self):
        r"""<p>需要采集的日志文件路径，必须是 /logs/ 目录下的文件，不支持子目录，最大支持 10 个文件。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Files

    @Files.setter
    def Files(self, Files):
        self._Files = Files


    def _deserialize(self, params):
        self._Files = params.get("Files")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetadataVar(AbstractModel):
    r"""metadata 项

    """

    def __init__(self):
        r"""
        :param _Name: <p>元数据名</p>
        :type Name: str
        :param _Value: <p>元数据值</p>
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        r"""<p>元数据名</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        r"""<p>元数据值</p>
        :rtype: str
        """
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
        


class ModifyDeploymentRequest(AbstractModel):
    r"""ModifyDeployment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeploymentId: <p>待修改的 Deployment ID。</p>
        :type DeploymentId: str
        :param _ScalingConfiguration: <p>完整替换伸缩配置；提供时必须包含全部三个成员。</p>
        :type ScalingConfiguration: :class:`tencentcloud.ags.v20250920.models.ScalingConfiguration`
        :param _LifecycleConfiguration: <p>完整替换生命周期配置；提供时必须包含全部两个成员。</p>
        :type LifecycleConfiguration: :class:`tencentcloud.ags.v20250920.models.LifecycleConfiguration`
        :param _Tags: <p>标签</p>
        :type Tags: list of Tag
        """
        self._DeploymentId = None
        self._ScalingConfiguration = None
        self._LifecycleConfiguration = None
        self._Tags = None

    @property
    def DeploymentId(self):
        r"""<p>待修改的 Deployment ID。</p>
        :rtype: str
        """
        return self._DeploymentId

    @DeploymentId.setter
    def DeploymentId(self, DeploymentId):
        self._DeploymentId = DeploymentId

    @property
    def ScalingConfiguration(self):
        r"""<p>完整替换伸缩配置；提供时必须包含全部三个成员。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ScalingConfiguration`
        """
        return self._ScalingConfiguration

    @ScalingConfiguration.setter
    def ScalingConfiguration(self, ScalingConfiguration):
        self._ScalingConfiguration = ScalingConfiguration

    @property
    def LifecycleConfiguration(self):
        r"""<p>完整替换生命周期配置；提供时必须包含全部两个成员。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.LifecycleConfiguration`
        """
        return self._LifecycleConfiguration

    @LifecycleConfiguration.setter
    def LifecycleConfiguration(self, LifecycleConfiguration):
        self._LifecycleConfiguration = LifecycleConfiguration

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._DeploymentId = params.get("DeploymentId")
        if params.get("ScalingConfiguration") is not None:
            self._ScalingConfiguration = ScalingConfiguration()
            self._ScalingConfiguration._deserialize(params.get("ScalingConfiguration"))
        if params.get("LifecycleConfiguration") is not None:
            self._LifecycleConfiguration = LifecycleConfiguration()
            self._LifecycleConfiguration._deserialize(params.get("LifecycleConfiguration"))
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
        


class ModifyDeploymentResponse(AbstractModel):
    r"""ModifyDeployment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Deployment: <p>修改后的完整 Deployment。</p>
        :type Deployment: :class:`tencentcloud.ags.v20250920.models.Deployment`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Deployment = None
        self._RequestId = None

    @property
    def Deployment(self):
        r"""<p>修改后的完整 Deployment。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.Deployment`
        """
        return self._Deployment

    @Deployment.setter
    def Deployment(self, Deployment):
        self._Deployment = Deployment

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
        if params.get("Deployment") is not None:
            self._Deployment = Deployment()
            self._Deployment._deserialize(params.get("Deployment"))
        self._RequestId = params.get("RequestId")


class ModifySessionRequest(AbstractModel):
    r"""ModifySession请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>会话所属的 SessionSpace ID。</p>
        :type SpaceId: str
        :param _UserId: <p>会话所属的用户 ID。</p>
        :type UserId: str
        :param _SessionId: <p>待修改的会话 ID。</p>
        :type SessionId: str
        :param _Title: <p>修改后的会话标题。</p><p>入参限制：本参数可选，最大长度为 255 个字符。</p><p>不传表示保持原会话标题不变，传空字符串表示清空会话标题。Title 与 Metadata 至少传入一项。</p>
        :type Title: str
        :param _Metadata: <p>修改后的完整会话元数据，以键值对数组形式表示。</p><p>入参限制：本参数可选，最多支持 64 项。Name 不能为空或重复，最大长度为 253 字节；Value 最大长度为 1024 字节，允许为空字符串。Metadata 序列化后的总大小不能超过 64 KiB。</p><p>不传表示保持原 Metadata 不变；传空数组表示清空全部 Metadata；传非空数组表示使用传入内容全量覆盖原 Metadata。Metadata 与 Title 至少传入一项。</p>
        :type Metadata: list of MetadataVar
        """
        self._SpaceId = None
        self._UserId = None
        self._SessionId = None
        self._Title = None
        self._Metadata = None

    @property
    def SpaceId(self):
        r"""<p>会话所属的 SessionSpace ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def UserId(self):
        r"""<p>会话所属的用户 ID。</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def SessionId(self):
        r"""<p>待修改的会话 ID。</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Title(self):
        r"""<p>修改后的会话标题。</p><p>入参限制：本参数可选，最大长度为 255 个字符。</p><p>不传表示保持原会话标题不变，传空字符串表示清空会话标题。Title 与 Metadata 至少传入一项。</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Metadata(self):
        r"""<p>修改后的完整会话元数据，以键值对数组形式表示。</p><p>入参限制：本参数可选，最多支持 64 项。Name 不能为空或重复，最大长度为 253 字节；Value 最大长度为 1024 字节，允许为空字符串。Metadata 序列化后的总大小不能超过 64 KiB。</p><p>不传表示保持原 Metadata 不变；传空数组表示清空全部 Metadata；传非空数组表示使用传入内容全量覆盖原 Metadata。Metadata 与 Title 至少传入一项。</p>
        :rtype: list of MetadataVar
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._UserId = params.get("UserId")
        self._SessionId = params.get("SessionId")
        self._Title = params.get("Title")
        if params.get("Metadata") is not None:
            self._Metadata = []
            for item in params.get("Metadata"):
                obj = MetadataVar()
                obj._deserialize(item)
                self._Metadata.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySessionResponse(AbstractModel):
    r"""ModifySession返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Session: <p>修改后的完整会话信息。</p>
        :type Session: :class:`tencentcloud.ags.v20250920.models.SessionInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Session = None
        self._RequestId = None

    @property
    def Session(self):
        r"""<p>修改后的完整会话信息。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SessionInfo`
        """
        return self._Session

    @Session.setter
    def Session(self, Session):
        self._Session = Session

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
        if params.get("Session") is not None:
            self._Session = SessionInfo()
            self._Session._deserialize(params.get("Session"))
        self._RequestId = params.get("RequestId")


class ModifySessionSpaceRequest(AbstractModel):
    r"""ModifySessionSpace请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>需要修改的会话空间唯一标识。</p>
        :type SpaceId: str
        :param _Name: <p>修改后的会话空间名称。</p>
        :type Name: str
        :param _Description: <p>修改后的会话空间描述。</p>
        :type Description: str
        """
        self._SpaceId = None
        self._Name = None
        self._Description = None

    @property
    def SpaceId(self):
        r"""<p>需要修改的会话空间唯一标识。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Name(self):
        r"""<p>修改后的会话空间名称。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>修改后的会话空间描述。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySessionSpaceResponse(AbstractModel):
    r"""ModifySessionSpace返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionSpace: <p>修改后的会话空间信息。</p>
        :type SessionSpace: :class:`tencentcloud.ags.v20250920.models.SessionSpaceInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SessionSpace = None
        self._RequestId = None

    @property
    def SessionSpace(self):
        r"""<p>修改后的会话空间信息。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SessionSpaceInfo`
        """
        return self._SessionSpace

    @SessionSpace.setter
    def SessionSpace(self, SessionSpace):
        self._SessionSpace = SessionSpace

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
        if params.get("SessionSpace") is not None:
            self._SessionSpace = SessionSpaceInfo()
            self._SessionSpace._deserialize(params.get("SessionSpace"))
        self._RequestId = params.get("RequestId")


class MountOption(AbstractModel):
    r"""沙箱实例存储挂载配置可选项，用于覆盖沙箱工具的存储配置的部分选项，并提供子路径挂载配置。

    """

    def __init__(self):
        r"""
        :param _Name: 指定沙箱工具中的存储配置名称
        :type Name: str
        :param _MountPath: 沙箱实例本地挂载路径（可选），默认继承工具中的存储配置
        :type MountPath: str
        :param _SubPath: 沙箱实例存储挂载子路径（可选）
        :type SubPath: str
        :param _ReadOnly: 沙箱实例存储挂载读写权限（可选），默认继承工具存储配置
        :type ReadOnly: bool
        """
        self._Name = None
        self._MountPath = None
        self._SubPath = None
        self._ReadOnly = None

    @property
    def Name(self):
        r"""指定沙箱工具中的存储配置名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MountPath(self):
        r"""沙箱实例本地挂载路径（可选），默认继承工具中的存储配置
        :rtype: str
        """
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath

    @property
    def SubPath(self):
        r"""沙箱实例存储挂载子路径（可选）
        :rtype: str
        """
        return self._SubPath

    @SubPath.setter
    def SubPath(self, SubPath):
        self._SubPath = SubPath

    @property
    def ReadOnly(self):
        r"""沙箱实例存储挂载读写权限（可选），默认继承工具存储配置
        :rtype: bool
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._MountPath = params.get("MountPath")
        self._SubPath = params.get("SubPath")
        self._ReadOnly = params.get("ReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkConfiguration(AbstractModel):
    r"""沙箱网络配置

    """

    def __init__(self):
        r"""
        :param _NetworkMode: 网络模式（当前支持 PUBLIC, VPC, SANDBOX）
        :type NetworkMode: str
        :param _VpcConfig: VPC网络相关配置
        :type VpcConfig: :class:`tencentcloud.ags.v20250920.models.VPCConfig`
        """
        self._NetworkMode = None
        self._VpcConfig = None

    @property
    def NetworkMode(self):
        r"""网络模式（当前支持 PUBLIC, VPC, SANDBOX）
        :rtype: str
        """
        return self._NetworkMode

    @NetworkMode.setter
    def NetworkMode(self, NetworkMode):
        self._NetworkMode = NetworkMode

    @property
    def VpcConfig(self):
        r"""VPC网络相关配置
        :rtype: :class:`tencentcloud.ags.v20250920.models.VPCConfig`
        """
        return self._VpcConfig

    @VpcConfig.setter
    def VpcConfig(self, VpcConfig):
        self._VpcConfig = VpcConfig


    def _deserialize(self, params):
        self._NetworkMode = params.get("NetworkMode")
        if params.get("VpcConfig") is not None:
            self._VpcConfig = VPCConfig()
            self._VpcConfig._deserialize(params.get("VpcConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OSWorldConfiguration(AbstractModel):
    r"""OSWorld 内置版本配置

    """

    def __init__(self):
        r"""
        :param _Version: <p>指定内置 OSWorld 版本</p><p>枚举值：</p><ul><li>osworld1： osworld v1</li><li>osworld2： osworld v2</li></ul><p>默认值：osworld1</p>
        :type Version: str
        """
        self._Version = None

    @property
    def Version(self):
        r"""<p>指定内置 OSWorld 版本</p><p>枚举值：</p><ul><li>osworld1： osworld v1</li><li>osworld2： osworld v2</li></ul><p>默认值：osworld1</p>
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseSandboxInstanceRequest(AbstractModel):
    r"""PauseSandboxInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>沙箱实例ID</p>
        :type InstanceId: str
        :param _Memory: <p>可选。带内存暂停，恢复后保留进程和内存状态。true=带内存；false=仅磁盘；不传=系统默认（当前默认 true，带内存）。</p>
        :type Memory: bool
        """
        self._InstanceId = None
        self._Memory = None

    @property
    def InstanceId(self):
        r"""<p>沙箱实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Memory(self):
        r"""<p>可选。带内存暂停，恢复后保留进程和内存状态。true=带内存；false=仅磁盘；不传=系统默认（当前默认 true，带内存）。</p>
        :rtype: bool
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Memory = params.get("Memory")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PauseSandboxInstanceResponse(AbstractModel):
    r"""PauseSandboxInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceStatus: <p>目标沙箱实例当前的状态</p><p>枚举值：</p><ul><li>PAUSING： 正在暂停中</li><li>PAUSED： 已暂停</li><li>PAUSE_FAILED： 暂停失败</li></ul>
        :type InstanceStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceStatus = None
        self._RequestId = None

    @property
    def InstanceStatus(self):
        r"""<p>目标沙箱实例当前的状态</p><p>枚举值：</p><ul><li>PAUSING： 正在暂停中</li><li>PAUSED： 已暂停</li><li>PAUSE_FAILED： 暂停失败</li></ul>
        :rtype: str
        """
        return self._InstanceStatus

    @InstanceStatus.setter
    def InstanceStatus(self, InstanceStatus):
        self._InstanceStatus = InstanceStatus

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
        self._InstanceStatus = params.get("InstanceStatus")
        self._RequestId = params.get("RequestId")


class PortConfiguration(AbstractModel):
    r"""端口配置

    """

    def __init__(self):
        r"""
        :param _Name: 端口名
        :type Name: str
        :param _Port: 端口
        :type Port: int
        :param _Protocol: 协议
        :type Protocol: str
        """
        self._Name = None
        self._Port = None
        self._Protocol = None

    @property
    def Name(self):
        r"""端口名
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Port(self):
        r"""端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        r"""协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewRegistryRecordRequest(AbstractModel):
    r"""PreviewRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>可选。指定要预览的目标 Version；与 Label 互斥；均省略时使用 Stable。</p>
        :type VersionId: str
        :param _Label: <p>可选。指定要预览的目标 Label；与 VersionId 互斥；均省略时使用 Stable。</p>
        :type Label: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._Label = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>可选。指定要预览的目标 Version；与 Label 互斥；均省略时使用 Stable。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Label(self):
        r"""<p>可选。指定要预览的目标 Label；与 VersionId 互斥；均省略时使用 Stable。</p>
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._Label = params.get("Label")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewRegistryRecordResponse(AbstractModel):
    r"""PreviewRegistryRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PreviewResult: <p>只读元数据预览结果对象（JSON 字符串形式）。字段：StatusCode（远端 HTTP 状态码，必返）、Body（远端响应体截断字符串，必返）、HasUpdate（Boolean，必返；远端内容按 Sync 相同的规范化规则处理后是否与请求 Version 配置不同；Error 非空时固定返回 false，此时不表示远端没有变化）、Error（调用错误信息，可选）。</p>
        :type PreviewResult: str
        :param _ResolvedVersionId: <p>实际预览的 Version ID（由 VersionId / Label 解析得到）。</p>
        :type ResolvedVersionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PreviewResult = None
        self._ResolvedVersionId = None
        self._RequestId = None

    @property
    def PreviewResult(self):
        r"""<p>只读元数据预览结果对象（JSON 字符串形式）。字段：StatusCode（远端 HTTP 状态码，必返）、Body（远端响应体截断字符串，必返）、HasUpdate（Boolean，必返；远端内容按 Sync 相同的规范化规则处理后是否与请求 Version 配置不同；Error 非空时固定返回 false，此时不表示远端没有变化）、Error（调用错误信息，可选）。</p>
        :rtype: str
        """
        return self._PreviewResult

    @PreviewResult.setter
    def PreviewResult(self, PreviewResult):
        self._PreviewResult = PreviewResult

    @property
    def ResolvedVersionId(self):
        r"""<p>实际预览的 Version ID（由 VersionId / Label 解析得到）。</p>
        :rtype: str
        """
        return self._ResolvedVersionId

    @ResolvedVersionId.setter
    def ResolvedVersionId(self, ResolvedVersionId):
        self._ResolvedVersionId = ResolvedVersionId

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
        self._PreviewResult = params.get("PreviewResult")
        self._ResolvedVersionId = params.get("ResolvedVersionId")
        self._RequestId = params.get("RequestId")


class ProbeConfiguration(AbstractModel):
    r"""健康检查探针配置

    """

    def __init__(self):
        r"""
        :param _HttpGet: HTTP GET 探测配置
        :type HttpGet: :class:`tencentcloud.ags.v20250920.models.HttpGetAction`
        :param _ReadyTimeoutMs: 健康检查就绪超时
        :type ReadyTimeoutMs: int
        :param _ProbeTimeoutMs: 健康检查单次探测超时
        :type ProbeTimeoutMs: int
        :param _ProbePeriodMs: 健康检查间隔
        :type ProbePeriodMs: int
        :param _SuccessThreshold: 健康检查成功阈值
        :type SuccessThreshold: int
        :param _FailureThreshold: 健康检查失败阈值
        :type FailureThreshold: int
        """
        self._HttpGet = None
        self._ReadyTimeoutMs = None
        self._ProbeTimeoutMs = None
        self._ProbePeriodMs = None
        self._SuccessThreshold = None
        self._FailureThreshold = None

    @property
    def HttpGet(self):
        r"""HTTP GET 探测配置
        :rtype: :class:`tencentcloud.ags.v20250920.models.HttpGetAction`
        """
        return self._HttpGet

    @HttpGet.setter
    def HttpGet(self, HttpGet):
        self._HttpGet = HttpGet

    @property
    def ReadyTimeoutMs(self):
        r"""健康检查就绪超时
        :rtype: int
        """
        return self._ReadyTimeoutMs

    @ReadyTimeoutMs.setter
    def ReadyTimeoutMs(self, ReadyTimeoutMs):
        self._ReadyTimeoutMs = ReadyTimeoutMs

    @property
    def ProbeTimeoutMs(self):
        r"""健康检查单次探测超时
        :rtype: int
        """
        return self._ProbeTimeoutMs

    @ProbeTimeoutMs.setter
    def ProbeTimeoutMs(self, ProbeTimeoutMs):
        self._ProbeTimeoutMs = ProbeTimeoutMs

    @property
    def ProbePeriodMs(self):
        r"""健康检查间隔
        :rtype: int
        """
        return self._ProbePeriodMs

    @ProbePeriodMs.setter
    def ProbePeriodMs(self, ProbePeriodMs):
        self._ProbePeriodMs = ProbePeriodMs

    @property
    def SuccessThreshold(self):
        r"""健康检查成功阈值
        :rtype: int
        """
        return self._SuccessThreshold

    @SuccessThreshold.setter
    def SuccessThreshold(self, SuccessThreshold):
        self._SuccessThreshold = SuccessThreshold

    @property
    def FailureThreshold(self):
        r"""健康检查失败阈值
        :rtype: int
        """
        return self._FailureThreshold

    @FailureThreshold.setter
    def FailureThreshold(self, FailureThreshold):
        self._FailureThreshold = FailureThreshold


    def _deserialize(self, params):
        if params.get("HttpGet") is not None:
            self._HttpGet = HttpGetAction()
            self._HttpGet._deserialize(params.get("HttpGet"))
        self._ReadyTimeoutMs = params.get("ReadyTimeoutMs")
        self._ProbeTimeoutMs = params.get("ProbeTimeoutMs")
        self._ProbePeriodMs = params.get("ProbePeriodMs")
        self._SuccessThreshold = params.get("SuccessThreshold")
        self._FailureThreshold = params.get("FailureThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaGroupOverview(AbstractModel):
    r"""配额组资源信息

    """

    def __init__(self):
        r"""
        :param _Tag: <p>配额组关联的标签键值</p>
        :type Tag: :class:`tencentcloud.ags.v20250920.models.Tag`
        :param _Name: <p>配额组名称</p>
        :type Name: str
        :param _Quota: <p>配额组各资源维度的配额上限</p>
        :type Quota: :class:`tencentcloud.ags.v20250920.models.QuotaResourceInfo`
        :param _Usage: <p>配额组各资源维度的当前用量</p>
        :type Usage: :class:`tencentcloud.ags.v20250920.models.QuotaResourceInfo`
        :param _CreateTime: <p>创建时间</p><p>参数格式：RFC3339 格式</p>
        :type CreateTime: str
        :param _UpdateTime: <p>最后更新时间</p><p>参数格式：RFC3339 格式</p>
        :type UpdateTime: str
        """
        self._Tag = None
        self._Name = None
        self._Quota = None
        self._Usage = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Tag(self):
        r"""<p>配额组关联的标签键值</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.Tag`
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Name(self):
        r"""<p>配额组名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Quota(self):
        r"""<p>配额组各资源维度的配额上限</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.QuotaResourceInfo`
        """
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota

    @property
    def Usage(self):
        r"""<p>配额组各资源维度的当前用量</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.QuotaResourceInfo`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def CreateTime(self):
        r"""<p>创建时间</p><p>参数格式：RFC3339 格式</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>最后更新时间</p><p>参数格式：RFC3339 格式</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        if params.get("Tag") is not None:
            self._Tag = Tag()
            self._Tag._deserialize(params.get("Tag"))
        self._Name = params.get("Name")
        if params.get("Quota") is not None:
            self._Quota = QuotaResourceInfo()
            self._Quota._deserialize(params.get("Quota"))
        if params.get("Usage") is not None:
            self._Usage = QuotaResourceInfo()
            self._Usage._deserialize(params.get("Usage"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QuotaResourceInfo(AbstractModel):
    r"""主账号资源信息

    """

    def __init__(self):
        r"""
        :param _SandboxTools: <p>沙箱工具配额或当前用量</p><p>单位：个</p>
        :type SandboxTools: int
        :param _SandboxInstances: <p>沙箱实例配额或当前用量</p><p>单位：个</p>
        :type SandboxInstances: int
        :param _PausedInstances: <p>暂停实例配额或当前用量</p><p>单位：个</p>
        :type PausedInstances: int
        :param _CPUCores: <p>暂停实例配额或当前用量。目前只在主账号中返回</p><p>单位：核</p>
        :type CPUCores: float
        :param _MemoryGiB: <p>内存配额或当前用量</p><p>单位：GiB</p>
        :type MemoryGiB: float
        """
        self._SandboxTools = None
        self._SandboxInstances = None
        self._PausedInstances = None
        self._CPUCores = None
        self._MemoryGiB = None

    @property
    def SandboxTools(self):
        r"""<p>沙箱工具配额或当前用量</p><p>单位：个</p>
        :rtype: int
        """
        return self._SandboxTools

    @SandboxTools.setter
    def SandboxTools(self, SandboxTools):
        self._SandboxTools = SandboxTools

    @property
    def SandboxInstances(self):
        r"""<p>沙箱实例配额或当前用量</p><p>单位：个</p>
        :rtype: int
        """
        return self._SandboxInstances

    @SandboxInstances.setter
    def SandboxInstances(self, SandboxInstances):
        self._SandboxInstances = SandboxInstances

    @property
    def PausedInstances(self):
        r"""<p>暂停实例配额或当前用量</p><p>单位：个</p>
        :rtype: int
        """
        return self._PausedInstances

    @PausedInstances.setter
    def PausedInstances(self, PausedInstances):
        self._PausedInstances = PausedInstances

    @property
    def CPUCores(self):
        r"""<p>暂停实例配额或当前用量。目前只在主账号中返回</p><p>单位：核</p>
        :rtype: float
        """
        return self._CPUCores

    @CPUCores.setter
    def CPUCores(self, CPUCores):
        self._CPUCores = CPUCores

    @property
    def MemoryGiB(self):
        r"""<p>内存配额或当前用量</p><p>单位：GiB</p>
        :rtype: float
        """
        return self._MemoryGiB

    @MemoryGiB.setter
    def MemoryGiB(self, MemoryGiB):
        self._MemoryGiB = MemoryGiB


    def _deserialize(self, params):
        self._SandboxTools = params.get("SandboxTools")
        self._SandboxInstances = params.get("SandboxInstances")
        self._PausedInstances = params.get("PausedInstances")
        self._CPUCores = params.get("CPUCores")
        self._MemoryGiB = params.get("MemoryGiB")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectRegistryRecordRequest(AbstractModel):
    r"""RejectRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>Version ID。</p>
        :type VersionId: str
        :param _Comment: <p>动作留言；非空。</p>
        :type Comment: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._Comment = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>Version ID。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Comment(self):
        r"""<p>动作留言；非空。</p>
        :rtype: str
        """
        return self._Comment

    @Comment.setter
    def Comment(self, Comment):
        self._Comment = Comment


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectRegistryRecordResponse(AbstractModel):
    r"""RejectRegistryRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Version: <p>更新后的 Version。</p>
        :type Version: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Version = None
        self._RequestId = None

    @property
    def Version(self):
        r"""<p>更新后的 Version。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

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
        if params.get("Version") is not None:
            self._Version = CloudRecordVersion()
            self._Version._deserialize(params.get("Version"))
        self._RequestId = params.get("RequestId")


class ResourceConfiguration(AbstractModel):
    r"""资源配置

    """

    def __init__(self):
        r"""
        :param _CPU: <p>cpu 资源量</p>
        :type CPU: str
        :param _Memory: <p>内存资源量</p>
        :type Memory: str
        :param _Storage: <p>自定义磁盘大小</p><p>枚举值：</p><ul><li>1Gi： 1Gi</li><li>5Gi： 5Gi</li><li>10Gi： 10Gi</li><li>20Gi： 20Gi</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :type Storage: str
        """
        self._CPU = None
        self._Memory = None
        self._Storage = None

    @property
    def CPU(self):
        r"""<p>cpu 资源量</p>
        :rtype: str
        """
        return self._CPU

    @CPU.setter
    def CPU(self, CPU):
        self._CPU = CPU

    @property
    def Memory(self):
        r"""<p>内存资源量</p>
        :rtype: str
        """
        return self._Memory

    @Memory.setter
    def Memory(self, Memory):
        self._Memory = Memory

    @property
    def Storage(self):
        r"""<p>自定义磁盘大小</p><p>枚举值：</p><ul><li>1Gi： 1Gi</li><li>5Gi： 5Gi</li><li>10Gi： 10Gi</li><li>20Gi： 20Gi</li></ul>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Storage

    @Storage.setter
    def Storage(self, Storage):
        self._Storage = Storage


    def _deserialize(self, params):
        self._CPU = params.get("CPU")
        self._Memory = params.get("Memory")
        self._Storage = params.get("Storage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeSandboxInstanceRequest(AbstractModel):
    r"""ResumeSandboxInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>沙箱实例ID</p>
        :type InstanceId: str
        :param _Timeout: <p>超时时间，超过这个时间就自动回收实例。支持格式：5m、300s、1h 等，默认 5m。最小 30s，最大 24h</p>
        :type Timeout: str
        """
        self._InstanceId = None
        self._Timeout = None

    @property
    def InstanceId(self):
        r"""<p>沙箱实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Timeout(self):
        r"""<p>超时时间，超过这个时间就自动回收实例。支持格式：5m、300s、1h 等，默认 5m。最小 30s，最大 24h</p>
        :rtype: str
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResumeSandboxInstanceResponse(AbstractModel):
    r"""ResumeSandboxInstance返回参数结构体

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


class SandboxInstance(AbstractModel):
    r"""沙箱实例结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>沙箱实例唯一标识符</p>
        :type InstanceId: str
        :param _ToolId: <p>所属沙箱工具 ID</p>
        :type ToolId: str
        :param _ToolName: <p>所属沙箱工具名称</p>
        :type ToolName: str
        :param _Status: <p>实例状态：STARTING（启动中）、RUNNING（运行中）、STOPPING（停止中）、STOPPED（已停止）、STOP_FAILED（停止失败）、FAILED（失败状态）</p>
        :type Status: str
        :param _Persistent: <p>是否常驻实例</p>
        :type Persistent: bool
        :param _TimeoutSeconds: <p>超时时间（秒），null 表示无超时设置</p>
        :type TimeoutSeconds: int
        :param _ExpiresAt: <p>过期时间（ISO 8601 格式），null 表示无过期时间</p>
        :type ExpiresAt: str
        :param _StopReason: <p>停止原因：manual（手动）、timeout（超时）、error（错误）、system（系统），仅在状态为 STOPPED、STOP_FAILED 或 FAILED 时有值。当 provider 停止失败时，状态为 STOP_FAILED，原因为 error</p>
        :type StopReason: str
        :param _CreateTime: <p>创建时间（ISO 8601 格式）</p>
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间（ISO 8601 格式）</p>
        :type UpdateTime: str
        :param _MountOptions: <p>存储挂载选项</p>
        :type MountOptions: list of MountOption
        :param _CustomConfiguration: <p>沙箱实例自定义配置</p>
        :type CustomConfiguration: :class:`tencentcloud.ags.v20250920.models.CustomConfigurationDetail`
        :param _ComputerConfiguration: <p>桌面电脑环境类沙箱配置</p>
        :type ComputerConfiguration: :class:`tencentcloud.ags.v20250920.models.ComputerConfiguration`
        :param _NetworkMode: <p>网络模式</p><p>枚举值：</p><ul><li>PUBLIC： 公网访问</li><li>SANDBOX： 无网络</li><li>INTERNAL_SERVICE： 腾讯云内部公共服务</li></ul><p>可以覆盖工具级别的网络配置。但如果一个工具本身就不支持 VPC 网络，那么即便在实例设置里选了 VPC 模式，也是无效的</p>
        :type NetworkMode: str
        :param _Metadata: <p>沙箱实例元数据</p>
        :type Metadata: list of MetadataVar
        :param _AuthMode: <p>沙箱访问认证模式</p><p>枚举值：</p><ul><li>DEFAULT： 默认，即 TOKEN 认证</li><li>TOKEN： Token认证，即所有端口访问都需携带TOKEN</li><li>NONE： 免认证，即所有端口访问无需携带TOKEN</li><li>PUBLIC： 公开模式，即ENVD管理端口（49983）访问需携带TOKEN，其他端口无需携带TOKEN</li></ul><p>默认值：DEFAULT</p>
        :type AuthMode: str
        """
        self._InstanceId = None
        self._ToolId = None
        self._ToolName = None
        self._Status = None
        self._Persistent = None
        self._TimeoutSeconds = None
        self._ExpiresAt = None
        self._StopReason = None
        self._CreateTime = None
        self._UpdateTime = None
        self._MountOptions = None
        self._CustomConfiguration = None
        self._ComputerConfiguration = None
        self._NetworkMode = None
        self._Metadata = None
        self._AuthMode = None

    @property
    def InstanceId(self):
        r"""<p>沙箱实例唯一标识符</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ToolId(self):
        r"""<p>所属沙箱工具 ID</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""<p>所属沙箱工具名称</p>
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def Status(self):
        r"""<p>实例状态：STARTING（启动中）、RUNNING（运行中）、STOPPING（停止中）、STOPPED（已停止）、STOP_FAILED（停止失败）、FAILED（失败状态）</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Persistent(self):
        r"""<p>是否常驻实例</p>
        :rtype: bool
        """
        return self._Persistent

    @Persistent.setter
    def Persistent(self, Persistent):
        self._Persistent = Persistent

    @property
    def TimeoutSeconds(self):
        r"""<p>超时时间（秒），null 表示无超时设置</p>
        :rtype: int
        """
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def ExpiresAt(self):
        r"""<p>过期时间（ISO 8601 格式），null 表示无过期时间</p>
        :rtype: str
        """
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def StopReason(self):
        r"""<p>停止原因：manual（手动）、timeout（超时）、error（错误）、system（系统），仅在状态为 STOPPED、STOP_FAILED 或 FAILED 时有值。当 provider 停止失败时，状态为 STOP_FAILED，原因为 error</p>
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def CreateTime(self):
        r"""<p>创建时间（ISO 8601 格式）</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间（ISO 8601 格式）</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def MountOptions(self):
        r"""<p>存储挂载选项</p>
        :rtype: list of MountOption
        """
        return self._MountOptions

    @MountOptions.setter
    def MountOptions(self, MountOptions):
        self._MountOptions = MountOptions

    @property
    def CustomConfiguration(self):
        r"""<p>沙箱实例自定义配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CustomConfigurationDetail`
        """
        return self._CustomConfiguration

    @CustomConfiguration.setter
    def CustomConfiguration(self, CustomConfiguration):
        self._CustomConfiguration = CustomConfiguration

    @property
    def ComputerConfiguration(self):
        r"""<p>桌面电脑环境类沙箱配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ComputerConfiguration`
        """
        return self._ComputerConfiguration

    @ComputerConfiguration.setter
    def ComputerConfiguration(self, ComputerConfiguration):
        self._ComputerConfiguration = ComputerConfiguration

    @property
    def NetworkMode(self):
        r"""<p>网络模式</p><p>枚举值：</p><ul><li>PUBLIC： 公网访问</li><li>SANDBOX： 无网络</li><li>INTERNAL_SERVICE： 腾讯云内部公共服务</li></ul><p>可以覆盖工具级别的网络配置。但如果一个工具本身就不支持 VPC 网络，那么即便在实例设置里选了 VPC 模式，也是无效的</p>
        :rtype: str
        """
        return self._NetworkMode

    @NetworkMode.setter
    def NetworkMode(self, NetworkMode):
        self._NetworkMode = NetworkMode

    @property
    def Metadata(self):
        r"""<p>沙箱实例元数据</p>
        :rtype: list of MetadataVar
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def AuthMode(self):
        r"""<p>沙箱访问认证模式</p><p>枚举值：</p><ul><li>DEFAULT： 默认，即 TOKEN 认证</li><li>TOKEN： Token认证，即所有端口访问都需携带TOKEN</li><li>NONE： 免认证，即所有端口访问无需携带TOKEN</li><li>PUBLIC： 公开模式，即ENVD管理端口（49983）访问需携带TOKEN，其他端口无需携带TOKEN</li></ul><p>默认值：DEFAULT</p>
        :rtype: str
        """
        return self._AuthMode

    @AuthMode.setter
    def AuthMode(self, AuthMode):
        self._AuthMode = AuthMode


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._Status = params.get("Status")
        self._Persistent = params.get("Persistent")
        self._TimeoutSeconds = params.get("TimeoutSeconds")
        self._ExpiresAt = params.get("ExpiresAt")
        self._StopReason = params.get("StopReason")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("MountOptions") is not None:
            self._MountOptions = []
            for item in params.get("MountOptions"):
                obj = MountOption()
                obj._deserialize(item)
                self._MountOptions.append(obj)
        if params.get("CustomConfiguration") is not None:
            self._CustomConfiguration = CustomConfigurationDetail()
            self._CustomConfiguration._deserialize(params.get("CustomConfiguration"))
        if params.get("ComputerConfiguration") is not None:
            self._ComputerConfiguration = ComputerConfiguration()
            self._ComputerConfiguration._deserialize(params.get("ComputerConfiguration"))
        self._NetworkMode = params.get("NetworkMode")
        if params.get("Metadata") is not None:
            self._Metadata = []
            for item in params.get("Metadata"):
                obj = MetadataVar()
                obj._deserialize(item)
                self._Metadata.append(obj)
        self._AuthMode = params.get("AuthMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SandboxTool(AbstractModel):
    r"""沙箱工具结构体

    """

    def __init__(self):
        r"""
        :param _ToolId: <p>沙箱工具唯一标识符</p>
        :type ToolId: str
        :param _ToolName: <p>沙箱工具名称，长度 1-50 字符，支持中英文、数字、下划线。同一 AppId 下沙箱工具名称必须唯一</p>
        :type ToolName: str
        :param _ToolType: <p>沙箱工具类型，取值：browser（浏览器工具）、code-interpreter（代码解释器工具）、computer（计算机控制工具）、mobile（移动设备工具）</p>
        :type ToolType: str
        :param _Status: <p>沙箱工具状态，取值：CREATING（创建中）、ACTIVE（可用）、DELETING（删除中）、FAILED（失败）</p>
        :type Status: str
        :param _Description: <p>沙箱工具描述信息，最大长度 200 字符</p>
        :type Description: str
        :param _Persistent: <p>是否常驻沙箱</p>
        :type Persistent: bool
        :param _DefaultTimeoutSeconds: <p>默认超时时间，支持格式：5m、300s、1h 等，不指定则使用系统默认值（5 分钟）。最大 24 小时</p>
        :type DefaultTimeoutSeconds: int
        :param _NetworkConfiguration: <p>网络配置</p>
        :type NetworkConfiguration: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        :param _Tags: <p>标签规格，包含资源标签绑定关系。用于为沙箱工具绑定标签，支持多种资源类型的标签绑定</p>
        :type Tags: list of Tag
        :param _CreateTime: <p>沙箱工具创建时间，格式：ISO8601</p>
        :type CreateTime: str
        :param _UpdateTime: <p>沙箱工具更新时间，格式：ISO8601</p>
        :type UpdateTime: str
        :param _RoleArn: <p>沙箱工具绑定角色ARN</p>
        :type RoleArn: str
        :param _StorageMounts: <p>沙箱工具中实例存储挂载配置</p>
        :type StorageMounts: list of StorageMount
        :param _CustomConfiguration: <p>沙箱工具自定义配置</p>
        :type CustomConfiguration: :class:`tencentcloud.ags.v20250920.models.CustomConfigurationDetail`
        :param _LogConfiguration: <p>沙箱工具日志推送相关配置</p>
        :type LogConfiguration: :class:`tencentcloud.ags.v20250920.models.LogConfiguration`
        :param _ComputerConfiguration: <p>桌面电脑环境类沙箱配置</p>
        :type ComputerConfiguration: :class:`tencentcloud.ags.v20250920.models.ComputerConfiguration`
        :param _StatusReason: <p>用于说明沙箱工具处于该状态的原因</p>
        :type StatusReason: str
        """
        self._ToolId = None
        self._ToolName = None
        self._ToolType = None
        self._Status = None
        self._Description = None
        self._Persistent = None
        self._DefaultTimeoutSeconds = None
        self._NetworkConfiguration = None
        self._Tags = None
        self._CreateTime = None
        self._UpdateTime = None
        self._RoleArn = None
        self._StorageMounts = None
        self._CustomConfiguration = None
        self._LogConfiguration = None
        self._ComputerConfiguration = None
        self._StatusReason = None

    @property
    def ToolId(self):
        r"""<p>沙箱工具唯一标识符</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""<p>沙箱工具名称，长度 1-50 字符，支持中英文、数字、下划线。同一 AppId 下沙箱工具名称必须唯一</p>
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def ToolType(self):
        r"""<p>沙箱工具类型，取值：browser（浏览器工具）、code-interpreter（代码解释器工具）、computer（计算机控制工具）、mobile（移动设备工具）</p>
        :rtype: str
        """
        return self._ToolType

    @ToolType.setter
    def ToolType(self, ToolType):
        self._ToolType = ToolType

    @property
    def Status(self):
        r"""<p>沙箱工具状态，取值：CREATING（创建中）、ACTIVE（可用）、DELETING（删除中）、FAILED（失败）</p>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        r"""<p>沙箱工具描述信息，最大长度 200 字符</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Persistent(self):
        r"""<p>是否常驻沙箱</p>
        :rtype: bool
        """
        return self._Persistent

    @Persistent.setter
    def Persistent(self, Persistent):
        self._Persistent = Persistent

    @property
    def DefaultTimeoutSeconds(self):
        r"""<p>默认超时时间，支持格式：5m、300s、1h 等，不指定则使用系统默认值（5 分钟）。最大 24 小时</p>
        :rtype: int
        """
        return self._DefaultTimeoutSeconds

    @DefaultTimeoutSeconds.setter
    def DefaultTimeoutSeconds(self, DefaultTimeoutSeconds):
        self._DefaultTimeoutSeconds = DefaultTimeoutSeconds

    @property
    def NetworkConfiguration(self):
        r"""<p>网络配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        """
        return self._NetworkConfiguration

    @NetworkConfiguration.setter
    def NetworkConfiguration(self, NetworkConfiguration):
        self._NetworkConfiguration = NetworkConfiguration

    @property
    def Tags(self):
        r"""<p>标签规格，包含资源标签绑定关系。用于为沙箱工具绑定标签，支持多种资源类型的标签绑定</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        r"""<p>沙箱工具创建时间，格式：ISO8601</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>沙箱工具更新时间，格式：ISO8601</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RoleArn(self):
        r"""<p>沙箱工具绑定角色ARN</p>
        :rtype: str
        """
        return self._RoleArn

    @RoleArn.setter
    def RoleArn(self, RoleArn):
        self._RoleArn = RoleArn

    @property
    def StorageMounts(self):
        r"""<p>沙箱工具中实例存储挂载配置</p>
        :rtype: list of StorageMount
        """
        return self._StorageMounts

    @StorageMounts.setter
    def StorageMounts(self, StorageMounts):
        self._StorageMounts = StorageMounts

    @property
    def CustomConfiguration(self):
        r"""<p>沙箱工具自定义配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CustomConfigurationDetail`
        """
        return self._CustomConfiguration

    @CustomConfiguration.setter
    def CustomConfiguration(self, CustomConfiguration):
        self._CustomConfiguration = CustomConfiguration

    @property
    def LogConfiguration(self):
        r"""<p>沙箱工具日志推送相关配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.LogConfiguration`
        """
        return self._LogConfiguration

    @LogConfiguration.setter
    def LogConfiguration(self, LogConfiguration):
        self._LogConfiguration = LogConfiguration

    @property
    def ComputerConfiguration(self):
        r"""<p>桌面电脑环境类沙箱配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ComputerConfiguration`
        """
        return self._ComputerConfiguration

    @ComputerConfiguration.setter
    def ComputerConfiguration(self, ComputerConfiguration):
        self._ComputerConfiguration = ComputerConfiguration

    @property
    def StatusReason(self):
        r"""<p>用于说明沙箱工具处于该状态的原因</p>
        :rtype: str
        """
        return self._StatusReason

    @StatusReason.setter
    def StatusReason(self, StatusReason):
        self._StatusReason = StatusReason


    def _deserialize(self, params):
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._ToolType = params.get("ToolType")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
        self._Persistent = params.get("Persistent")
        self._DefaultTimeoutSeconds = params.get("DefaultTimeoutSeconds")
        if params.get("NetworkConfiguration") is not None:
            self._NetworkConfiguration = NetworkConfiguration()
            self._NetworkConfiguration._deserialize(params.get("NetworkConfiguration"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._RoleArn = params.get("RoleArn")
        if params.get("StorageMounts") is not None:
            self._StorageMounts = []
            for item in params.get("StorageMounts"):
                obj = StorageMount()
                obj._deserialize(item)
                self._StorageMounts.append(obj)
        if params.get("CustomConfiguration") is not None:
            self._CustomConfiguration = CustomConfigurationDetail()
            self._CustomConfiguration._deserialize(params.get("CustomConfiguration"))
        if params.get("LogConfiguration") is not None:
            self._LogConfiguration = LogConfiguration()
            self._LogConfiguration._deserialize(params.get("LogConfiguration"))
        if params.get("ComputerConfiguration") is not None:
            self._ComputerConfiguration = ComputerConfiguration()
            self._ComputerConfiguration._deserialize(params.get("ComputerConfiguration"))
        self._StatusReason = params.get("StatusReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScalingConfiguration(AbstractModel):
    r"""Deployment 活跃容量配置

    """

    def __init__(self):
        r"""
        :param _MinInstanceCount: <p>活跃 Sandbox Instance 下限，必须大于等于 0。</p>
        :type MinInstanceCount: int
        :param _MaxInstanceCount: <p>活跃 Sandbox Instance 上限，必须大于等于 1，并且不小于 MinInstanceCount。</p>
        :type MaxInstanceCount: int
        :param _MaxInstanceRequestConcurrency: <p>每个活跃 Sandbox Instance 同时持有的 Deployment 请求或连接 Lease 上限，必须大于等于 1。</p>
        :type MaxInstanceRequestConcurrency: int
        """
        self._MinInstanceCount = None
        self._MaxInstanceCount = None
        self._MaxInstanceRequestConcurrency = None

    @property
    def MinInstanceCount(self):
        r"""<p>活跃 Sandbox Instance 下限，必须大于等于 0。</p>
        :rtype: int
        """
        return self._MinInstanceCount

    @MinInstanceCount.setter
    def MinInstanceCount(self, MinInstanceCount):
        self._MinInstanceCount = MinInstanceCount

    @property
    def MaxInstanceCount(self):
        r"""<p>活跃 Sandbox Instance 上限，必须大于等于 1，并且不小于 MinInstanceCount。</p>
        :rtype: int
        """
        return self._MaxInstanceCount

    @MaxInstanceCount.setter
    def MaxInstanceCount(self, MaxInstanceCount):
        self._MaxInstanceCount = MaxInstanceCount

    @property
    def MaxInstanceRequestConcurrency(self):
        r"""<p>每个活跃 Sandbox Instance 同时持有的 Deployment 请求或连接 Lease 上限，必须大于等于 1。</p>
        :rtype: int
        """
        return self._MaxInstanceRequestConcurrency

    @MaxInstanceRequestConcurrency.setter
    def MaxInstanceRequestConcurrency(self, MaxInstanceRequestConcurrency):
        self._MaxInstanceRequestConcurrency = MaxInstanceRequestConcurrency


    def _deserialize(self, params):
        self._MinInstanceCount = params.get("MinInstanceCount")
        self._MaxInstanceCount = params.get("MaxInstanceCount")
        self._MaxInstanceRequestConcurrency = params.get("MaxInstanceRequestConcurrency")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionInfo(AbstractModel):
    r"""会话信息

    """

    def __init__(self):
        r"""
        :param _SessionId: <p>会话 ID。</p>
        :type SessionId: str
        :param _SpaceId: <p>会话所属空间 ID。</p>
        :type SpaceId: str
        :param _State: <p>Session 快照状态</p>
        :type State: :class:`tencentcloud.ags.v20250920.models.SessionState`
        :param _Metadata: <p>会话元数据，以键值对数组形式表示。每个元素包含 Metadata 名称和对应值，最多支持 64 项。</p>
        :type Metadata: list of MetadataVar
        :param _AgentId: <p>Agent ID。</p>
        :type AgentId: str
        :param _UserId: <p>用户 ID。</p>
        :type UserId: str
        :param _Title: <p>会话标题。</p>
        :type Title: str
        :param _EventCount: <p>事件数量。</p>
        :type EventCount: int
        :param _CreateTime: <p>创建时间。</p>
        :type CreateTime: str
        :param _UpdateTime: <p>更新时间。</p>
        :type UpdateTime: str
        """
        self._SessionId = None
        self._SpaceId = None
        self._State = None
        self._Metadata = None
        self._AgentId = None
        self._UserId = None
        self._Title = None
        self._EventCount = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def SessionId(self):
        r"""<p>会话 ID。</p>
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def SpaceId(self):
        r"""<p>会话所属空间 ID。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def State(self):
        r"""<p>Session 快照状态</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SessionState`
        """
        return self._State

    @State.setter
    def State(self, State):
        self._State = State

    @property
    def Metadata(self):
        r"""<p>会话元数据，以键值对数组形式表示。每个元素包含 Metadata 名称和对应值，最多支持 64 项。</p>
        :rtype: list of MetadataVar
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def AgentId(self):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        r"""<p>Agent ID。</p>
        :rtype: str
        """
        return self._AgentId

    @AgentId.setter
    def AgentId(self, AgentId):
        warnings.warn("parameter `AgentId` is deprecated", DeprecationWarning) 

        self._AgentId = AgentId

    @property
    def UserId(self):
        r"""<p>用户 ID。</p>
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def Title(self):
        r"""<p>会话标题。</p>
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def EventCount(self):
        r"""<p>事件数量。</p>
        :rtype: int
        """
        return self._EventCount

    @EventCount.setter
    def EventCount(self, EventCount):
        self._EventCount = EventCount

    @property
    def CreateTime(self):
        r"""<p>创建时间。</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>更新时间。</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._SpaceId = params.get("SpaceId")
        if params.get("State") is not None:
            self._State = SessionState()
            self._State._deserialize(params.get("State"))
        if params.get("Metadata") is not None:
            self._Metadata = []
            for item in params.get("Metadata"):
                obj = MetadataVar()
                obj._deserialize(item)
                self._Metadata.append(obj)
        self._AgentId = params.get("AgentId")
        self._UserId = params.get("UserId")
        self._Title = params.get("Title")
        self._EventCount = params.get("EventCount")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionSpaceInfo(AbstractModel):
    r"""描述会话空间的完整信息。会话空间是用户状态、会话和事件的上级资源及隔离边界，同一个会话只能属于一个会话空间。

    """

    def __init__(self):
        r"""
        :param _SpaceId: <p>会话空间唯一标识，由服务端生成，最大长度为 128 个字符。调用方不应自行构造或解析。</p>
        :type SpaceId: str
        :param _Name: <p>会话空间名称，用于标识会话空间的业务用途，最大长度为 128 个字符。</p>
        :type Name: str
        :param _Description: <p>会话空间描述，用于说明业务用途和使用范围，最大长度为 512 个字符。为空时该字段可能不返回</p>
        :type Description: str
        :param _Status: <p>会话空间当前状态。</p><p>枚举值：</p><ul><li>Active： 正常可用</li><li>Deleting： 正在删除</li></ul>
        :type Status: str
        :param _Default: <p>是否为系统默认会话空间。true 表示默认会话空间，false 表示普通会话空间。默认会话空间不允许删除。</p>
        :type Default: bool
        :param _CreateTime: <p>会话空间创建时间，采用 ISO 8601/RFC 3339 格式。</p>
        :type CreateTime: str
        :param _UpdateTime: <p>会话空间最后更新时间，采用 ISO 8601/RFC 3339 格式。</p>
        :type UpdateTime: str
        """
        self._SpaceId = None
        self._Name = None
        self._Description = None
        self._Status = None
        self._Default = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def SpaceId(self):
        r"""<p>会话空间唯一标识，由服务端生成，最大长度为 128 个字符。调用方不应自行构造或解析。</p>
        :rtype: str
        """
        return self._SpaceId

    @SpaceId.setter
    def SpaceId(self, SpaceId):
        self._SpaceId = SpaceId

    @property
    def Name(self):
        r"""<p>会话空间名称，用于标识会话空间的业务用途，最大长度为 128 个字符。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""<p>会话空间描述，用于说明业务用途和使用范围，最大长度为 512 个字符。为空时该字段可能不返回</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Status(self):
        r"""<p>会话空间当前状态。</p><p>枚举值：</p><ul><li>Active： 正常可用</li><li>Deleting： 正在删除</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Default(self):
        r"""<p>是否为系统默认会话空间。true 表示默认会话空间，false 表示普通会话空间。默认会话空间不允许删除。</p>
        :rtype: bool
        """
        return self._Default

    @Default.setter
    def Default(self, Default):
        self._Default = Default

    @property
    def CreateTime(self):
        r"""<p>会话空间创建时间，采用 ISO 8601/RFC 3339 格式。</p>
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""<p>会话空间最后更新时间，采用 ISO 8601/RFC 3339 格式。</p>
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._SpaceId = params.get("SpaceId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Status = params.get("Status")
        self._Default = params.get("Default")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SessionState(AbstractModel):
    r"""Session 快照状态

    """

    def __init__(self):
        r"""
        :param _CustomState: <p>自定义状态 JSON 对象字符串</p>
        :type CustomState: str
        """
        self._CustomState = None

    @property
    def CustomState(self):
        r"""<p>自定义状态 JSON 对象字符串</p>
        :rtype: str
        """
        return self._CustomState

    @CustomState.setter
    def CustomState(self, CustomState):
        self._CustomState = CustomState


    def _deserialize(self, params):
        self._CustomState = params.get("CustomState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSandboxInstanceRequest(AbstractModel):
    r"""StartSandboxInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ToolId: <p>沙箱工具 ID，与 ToolName 至少有一个要填</p>
        :type ToolId: str
        :param _ToolName: <p>沙箱工具名称，与 ToolId 至少有一个要填</p>
        :type ToolName: str
        :param _Timeout: <p>超时时间，超过这个时间就自动回收实例。支持格式：5m、300s、1h 等，默认 5m。最小 30s，最大 24h</p>
        :type Timeout: str
        :param _ClientToken: <p>幂等性 Token，长度不超过 64 字符</p>
        :type ClientToken: str
        :param _MountOptions: <p>沙箱实例存储挂载配置</p>
        :type MountOptions: list of MountOption
        :param _CustomConfiguration: <p>沙箱实例自定义配置</p>
        :type CustomConfiguration: :class:`tencentcloud.ags.v20250920.models.CustomConfiguration`
        :param _AuthMode: <p>沙箱访问认证模式</p><p>枚举值：</p><ul><li>DEFAULT： 默认，即TOKEN认证</li><li>TOKEN： Token认证，即所有端口访问都需携带Token</li><li>NONE： 免认证，即所有端口访问无需携带Token</li><li>PUBLIC： 公开模式，即ENVD管理端口（49983）访问需携带Token，其他端口无需携带Token</li></ul><p>默认值：DEFAULT</p>
        :type AuthMode: str
        :param _Metadata: <p>沙箱元数据</p>
        :type Metadata: list of MetadataVar
        """
        self._ToolId = None
        self._ToolName = None
        self._Timeout = None
        self._ClientToken = None
        self._MountOptions = None
        self._CustomConfiguration = None
        self._AuthMode = None
        self._Metadata = None

    @property
    def ToolId(self):
        r"""<p>沙箱工具 ID，与 ToolName 至少有一个要填</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""<p>沙箱工具名称，与 ToolId 至少有一个要填</p>
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def Timeout(self):
        r"""<p>超时时间，超过这个时间就自动回收实例。支持格式：5m、300s、1h 等，默认 5m。最小 30s，最大 24h</p>
        :rtype: str
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def ClientToken(self):
        r"""<p>幂等性 Token，长度不超过 64 字符</p>
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken

    @property
    def MountOptions(self):
        r"""<p>沙箱实例存储挂载配置</p>
        :rtype: list of MountOption
        """
        return self._MountOptions

    @MountOptions.setter
    def MountOptions(self, MountOptions):
        self._MountOptions = MountOptions

    @property
    def CustomConfiguration(self):
        r"""<p>沙箱实例自定义配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CustomConfiguration`
        """
        return self._CustomConfiguration

    @CustomConfiguration.setter
    def CustomConfiguration(self, CustomConfiguration):
        self._CustomConfiguration = CustomConfiguration

    @property
    def AuthMode(self):
        r"""<p>沙箱访问认证模式</p><p>枚举值：</p><ul><li>DEFAULT： 默认，即TOKEN认证</li><li>TOKEN： Token认证，即所有端口访问都需携带Token</li><li>NONE： 免认证，即所有端口访问无需携带Token</li><li>PUBLIC： 公开模式，即ENVD管理端口（49983）访问需携带Token，其他端口无需携带Token</li></ul><p>默认值：DEFAULT</p>
        :rtype: str
        """
        return self._AuthMode

    @AuthMode.setter
    def AuthMode(self, AuthMode):
        self._AuthMode = AuthMode

    @property
    def Metadata(self):
        r"""<p>沙箱元数据</p>
        :rtype: list of MetadataVar
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._Timeout = params.get("Timeout")
        self._ClientToken = params.get("ClientToken")
        if params.get("MountOptions") is not None:
            self._MountOptions = []
            for item in params.get("MountOptions"):
                obj = MountOption()
                obj._deserialize(item)
                self._MountOptions.append(obj)
        if params.get("CustomConfiguration") is not None:
            self._CustomConfiguration = CustomConfiguration()
            self._CustomConfiguration._deserialize(params.get("CustomConfiguration"))
        self._AuthMode = params.get("AuthMode")
        if params.get("Metadata") is not None:
            self._Metadata = []
            for item in params.get("Metadata"):
                obj = MetadataVar()
                obj._deserialize(item)
                self._Metadata.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartSandboxInstanceResponse(AbstractModel):
    r"""StartSandboxInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Instance: <p>创建的沙箱实例完整信息</p>
        :type Instance: :class:`tencentcloud.ags.v20250920.models.SandboxInstance`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instance = None
        self._RequestId = None

    @property
    def Instance(self):
        r"""<p>创建的沙箱实例完整信息</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.SandboxInstance`
        """
        return self._Instance

    @Instance.setter
    def Instance(self, Instance):
        self._Instance = Instance

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
        if params.get("Instance") is not None:
            self._Instance = SandboxInstance()
            self._Instance._deserialize(params.get("Instance"))
        self._RequestId = params.get("RequestId")


class StopSandboxInstanceRequest(AbstractModel):
    r"""StopSandboxInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 沙箱实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""沙箱实例ID
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
        


class StopSandboxInstanceResponse(AbstractModel):
    r"""StopSandboxInstance返回参数结构体

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


class StorageMount(AbstractModel):
    r"""沙箱工具中实例存储挂载配置

    """

    def __init__(self):
        r"""
        :param _Name: <p>存储挂载配置名称</p>
        :type Name: str
        :param _StorageSource: <p>存储配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageSource: :class:`tencentcloud.ags.v20250920.models.StorageSource`
        :param _MountPath: <p>沙箱实例本地挂载路径</p>
        :type MountPath: str
        :param _ReadOnly: <p>存储挂载读写权限配置，默认为false</p>
        :type ReadOnly: bool
        """
        self._Name = None
        self._StorageSource = None
        self._MountPath = None
        self._ReadOnly = None

    @property
    def Name(self):
        r"""<p>存储挂载配置名称</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def StorageSource(self):
        r"""<p>存储配置</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.ags.v20250920.models.StorageSource`
        """
        return self._StorageSource

    @StorageSource.setter
    def StorageSource(self, StorageSource):
        self._StorageSource = StorageSource

    @property
    def MountPath(self):
        r"""<p>沙箱实例本地挂载路径</p>
        :rtype: str
        """
        return self._MountPath

    @MountPath.setter
    def MountPath(self, MountPath):
        self._MountPath = MountPath

    @property
    def ReadOnly(self):
        r"""<p>存储挂载读写权限配置，默认为false</p>
        :rtype: bool
        """
        return self._ReadOnly

    @ReadOnly.setter
    def ReadOnly(self, ReadOnly):
        self._ReadOnly = ReadOnly


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("StorageSource") is not None:
            self._StorageSource = StorageSource()
            self._StorageSource._deserialize(params.get("StorageSource"))
        self._MountPath = params.get("MountPath")
        self._ReadOnly = params.get("ReadOnly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageSource(AbstractModel):
    r"""挂载存储配置

    """

    def __init__(self):
        r"""
        :param _Cos: <p>对象存储桶配置</p>
        :type Cos: :class:`tencentcloud.ags.v20250920.models.CosStorageSource`
        :param _Image: <p>镜像卷配置</p>
        :type Image: :class:`tencentcloud.ags.v20250920.models.ImageStorageSource`
        :param _Cfs: <p>文件存储配置</p>
        :type Cfs: :class:`tencentcloud.ags.v20250920.models.CfsStorageSource`
        :param _AgentBucket: <p>AgentBucket 存储配置</p>
        :type AgentBucket: :class:`tencentcloud.ags.v20250920.models.AgentBucketStorageSource`
        """
        self._Cos = None
        self._Image = None
        self._Cfs = None
        self._AgentBucket = None

    @property
    def Cos(self):
        r"""<p>对象存储桶配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CosStorageSource`
        """
        return self._Cos

    @Cos.setter
    def Cos(self, Cos):
        self._Cos = Cos

    @property
    def Image(self):
        r"""<p>镜像卷配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ImageStorageSource`
        """
        return self._Image

    @Image.setter
    def Image(self, Image):
        self._Image = Image

    @property
    def Cfs(self):
        r"""<p>文件存储配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CfsStorageSource`
        """
        return self._Cfs

    @Cfs.setter
    def Cfs(self, Cfs):
        self._Cfs = Cfs

    @property
    def AgentBucket(self):
        r"""<p>AgentBucket 存储配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.AgentBucketStorageSource`
        """
        return self._AgentBucket

    @AgentBucket.setter
    def AgentBucket(self, AgentBucket):
        self._AgentBucket = AgentBucket


    def _deserialize(self, params):
        if params.get("Cos") is not None:
            self._Cos = CosStorageSource()
            self._Cos._deserialize(params.get("Cos"))
        if params.get("Image") is not None:
            self._Image = ImageStorageSource()
            self._Image._deserialize(params.get("Image"))
        if params.get("Cfs") is not None:
            self._Cfs = CfsStorageSource()
            self._Cfs._deserialize(params.get("Cfs"))
        if params.get("AgentBucket") is not None:
            self._AgentBucket = AgentBucketStorageSource()
            self._AgentBucket._deserialize(params.get("AgentBucket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncRegistryRecordRequest(AbstractModel):
    r"""SyncRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>父 Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _VersionId: <p>可选。指定要同步的目标 Version；与 Label 互斥；均省略时使用 Stable。</p>
        :type VersionId: str
        :param _Label: <p>可选。指定要同步的目标 Label；与 VersionId 互斥；均省略时使用 Stable。Label 在请求开始时只解析一次。</p>
        :type Label: str
        :param _ChangeLog: <p>可选，最大 4096 字符。若同步创建新 Version，将写入新 Version 的 ChangeLog；省略时保存为空。</p>
        :type ChangeLog: str
        """
        self._RegistryId = None
        self._RecordId = None
        self._VersionId = None
        self._Label = None
        self._ChangeLog = None

    @property
    def RegistryId(self):
        r"""<p>父 Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def VersionId(self):
        r"""<p>可选。指定要同步的目标 Version；与 Label 互斥；均省略时使用 Stable。</p>
        :rtype: str
        """
        return self._VersionId

    @VersionId.setter
    def VersionId(self, VersionId):
        self._VersionId = VersionId

    @property
    def Label(self):
        r"""<p>可选。指定要同步的目标 Label；与 VersionId 互斥；均省略时使用 Stable。Label 在请求开始时只解析一次。</p>
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def ChangeLog(self):
        r"""<p>可选，最大 4096 字符。若同步创建新 Version，将写入新 Version 的 ChangeLog；省略时保存为空。</p>
        :rtype: str
        """
        return self._ChangeLog

    @ChangeLog.setter
    def ChangeLog(self, ChangeLog):
        self._ChangeLog = ChangeLog


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._VersionId = params.get("VersionId")
        self._Label = params.get("Label")
        self._ChangeLog = params.get("ChangeLog")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SyncRegistryRecordResponse(AbstractModel):
    r"""SyncRegistryRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SyncStatus: <p>同步结果：UNCHANGED（远端无变化）/ VERSION_CREATED（远端有变化，已生成新 Version）/ FAILED（同步失败）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type SyncStatus: str
        :param _ResolvedVersionId: <p>作为同步来源解析出的 Version ID（可能由 Label 解析而来）；不为空。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ResolvedVersionId: str
        :param _CreatedVersion: <p>SyncStatus=VERSION_CREATED 时返回：本次新建的 Version。</p>
        :type CreatedVersion: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        :param _Record: <p>SyncStatus=VERSION_CREATED 时返回：同步后的最新 Record。</p>
        :type Record: :class:`tencentcloud.ags.v20250920.models.CloudRecord`
        :param _LastSyncTime: <p>最后一次同步时间，ISO 8601 UTC。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type LastSyncTime: str
        :param _ErrorCode: <p>失败错误码；SyncStatus=FAILED 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorCode: str
        :param _ErrorMessage: <p>失败错误信息；SyncStatus=FAILED 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SyncStatus = None
        self._ResolvedVersionId = None
        self._CreatedVersion = None
        self._Record = None
        self._LastSyncTime = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def SyncStatus(self):
        r"""<p>同步结果：UNCHANGED（远端无变化）/ VERSION_CREATED（远端有变化，已生成新 Version）/ FAILED（同步失败）。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SyncStatus

    @SyncStatus.setter
    def SyncStatus(self, SyncStatus):
        self._SyncStatus = SyncStatus

    @property
    def ResolvedVersionId(self):
        r"""<p>作为同步来源解析出的 Version ID（可能由 Label 解析而来）；不为空。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResolvedVersionId

    @ResolvedVersionId.setter
    def ResolvedVersionId(self, ResolvedVersionId):
        self._ResolvedVersionId = ResolvedVersionId

    @property
    def CreatedVersion(self):
        r"""<p>SyncStatus=VERSION_CREATED 时返回：本次新建的 Version。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        """
        return self._CreatedVersion

    @CreatedVersion.setter
    def CreatedVersion(self, CreatedVersion):
        self._CreatedVersion = CreatedVersion

    @property
    def Record(self):
        r"""<p>SyncStatus=VERSION_CREATED 时返回：同步后的最新 Record。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecord`
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def LastSyncTime(self):
        r"""<p>最后一次同步时间，ISO 8601 UTC。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastSyncTime

    @LastSyncTime.setter
    def LastSyncTime(self, LastSyncTime):
        self._LastSyncTime = LastSyncTime

    @property
    def ErrorCode(self):
        r"""<p>失败错误码；SyncStatus=FAILED 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""<p>失败错误信息；SyncStatus=FAILED 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

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
        self._SyncStatus = params.get("SyncStatus")
        self._ResolvedVersionId = params.get("ResolvedVersionId")
        if params.get("CreatedVersion") is not None:
            self._CreatedVersion = CloudRecordVersion()
            self._CreatedVersion._deserialize(params.get("CreatedVersion"))
        if params.get("Record") is not None:
            self._Record = CloudRecord()
            self._Record._deserialize(params.get("Record"))
        self._LastSyncTime = params.get("LastSyncTime")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")


class Tag(AbstractModel):
    r"""标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签键
        :type Key: str
        :param _Value: 标签值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        r"""标签键
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        r"""标签值
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
        


class UpdateRegistryRecordRequest(AbstractModel):
    r"""UpdateRegistryRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>Registry ID。</p>
        :type RegistryId: str
        :param _RecordId: <p>Record ID。</p>
        :type RecordId: str
        :param _Description: <p>Record 描述，可选。Record 更新模式下允许，允许空字符串清空；Version 创建模式禁止。</p>
        :type Description: str
        :param _VersionName: <p>新 Version 的展示名，可选。仅 Version 创建模式允许。</p>
        :type VersionName: str
        :param _ChangeLog: <p>新 Version 的变更原因，最大 4096 字符，可选。仅 Version 创建模式允许。</p>
        :type ChangeLog: str
        :param _MCPSource: <p>Version 创建模式：现有 Record 的 DescriptorType=MCP 时可提交。</p>
        :type MCPSource: :class:`tencentcloud.ags.v20250920.models.CloudMCPSourceInput`
        :param _AgentSource: <p>Version 创建模式：现有 Record 的 DescriptorType=A2A 或 AGUI 时可提交。</p>
        :type AgentSource: :class:`tencentcloud.ags.v20250920.models.CloudAgentSourceInput`
        :param _SkillSource: <p>Version 创建模式：现有 Record 的 DescriptorType=AGENT_SKILLS 时可提交。</p>
        :type SkillSource: :class:`tencentcloud.ags.v20250920.models.CloudSkillSourceInput`
        :param _CustomDescriptors: <p>Version 创建模式：现有 Record 的 DescriptorType=CUSTOM 时可提交，必须是 JSON object 字符串。</p>
        :type CustomDescriptors: str
        :param _LabelMutations: <p>Record 更新模式：Label 变更列表，最多 32 条，同一次请求中 Label Name 不可重复。</p>
        :type LabelMutations: list of CloudRecordLabelMutation
        """
        self._RegistryId = None
        self._RecordId = None
        self._Description = None
        self._VersionName = None
        self._ChangeLog = None
        self._MCPSource = None
        self._AgentSource = None
        self._SkillSource = None
        self._CustomDescriptors = None
        self._LabelMutations = None

    @property
    def RegistryId(self):
        r"""<p>Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def RecordId(self):
        r"""<p>Record ID。</p>
        :rtype: str
        """
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def Description(self):
        r"""<p>Record 描述，可选。Record 更新模式下允许，允许空字符串清空；Version 创建模式禁止。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def VersionName(self):
        r"""<p>新 Version 的展示名，可选。仅 Version 创建模式允许。</p>
        :rtype: str
        """
        return self._VersionName

    @VersionName.setter
    def VersionName(self, VersionName):
        self._VersionName = VersionName

    @property
    def ChangeLog(self):
        r"""<p>新 Version 的变更原因，最大 4096 字符，可选。仅 Version 创建模式允许。</p>
        :rtype: str
        """
        return self._ChangeLog

    @ChangeLog.setter
    def ChangeLog(self, ChangeLog):
        self._ChangeLog = ChangeLog

    @property
    def MCPSource(self):
        r"""<p>Version 创建模式：现有 Record 的 DescriptorType=MCP 时可提交。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudMCPSourceInput`
        """
        return self._MCPSource

    @MCPSource.setter
    def MCPSource(self, MCPSource):
        self._MCPSource = MCPSource

    @property
    def AgentSource(self):
        r"""<p>Version 创建模式：现有 Record 的 DescriptorType=A2A 或 AGUI 时可提交。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudAgentSourceInput`
        """
        return self._AgentSource

    @AgentSource.setter
    def AgentSource(self, AgentSource):
        self._AgentSource = AgentSource

    @property
    def SkillSource(self):
        r"""<p>Version 创建模式：现有 Record 的 DescriptorType=AGENT_SKILLS 时可提交。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudSkillSourceInput`
        """
        return self._SkillSource

    @SkillSource.setter
    def SkillSource(self, SkillSource):
        self._SkillSource = SkillSource

    @property
    def CustomDescriptors(self):
        r"""<p>Version 创建模式：现有 Record 的 DescriptorType=CUSTOM 时可提交，必须是 JSON object 字符串。</p>
        :rtype: str
        """
        return self._CustomDescriptors

    @CustomDescriptors.setter
    def CustomDescriptors(self, CustomDescriptors):
        self._CustomDescriptors = CustomDescriptors

    @property
    def LabelMutations(self):
        r"""<p>Record 更新模式：Label 变更列表，最多 32 条，同一次请求中 Label Name 不可重复。</p>
        :rtype: list of CloudRecordLabelMutation
        """
        return self._LabelMutations

    @LabelMutations.setter
    def LabelMutations(self, LabelMutations):
        self._LabelMutations = LabelMutations


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._RecordId = params.get("RecordId")
        self._Description = params.get("Description")
        self._VersionName = params.get("VersionName")
        self._ChangeLog = params.get("ChangeLog")
        if params.get("MCPSource") is not None:
            self._MCPSource = CloudMCPSourceInput()
            self._MCPSource._deserialize(params.get("MCPSource"))
        if params.get("AgentSource") is not None:
            self._AgentSource = CloudAgentSourceInput()
            self._AgentSource._deserialize(params.get("AgentSource"))
        if params.get("SkillSource") is not None:
            self._SkillSource = CloudSkillSourceInput()
            self._SkillSource._deserialize(params.get("SkillSource"))
        self._CustomDescriptors = params.get("CustomDescriptors")
        if params.get("LabelMutations") is not None:
            self._LabelMutations = []
            for item in params.get("LabelMutations"):
                obj = CloudRecordLabelMutation()
                obj._deserialize(item)
                self._LabelMutations.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRegistryRecordResponse(AbstractModel):
    r"""UpdateRegistryRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Record: <p>更新后的 Record。</p>
        :type Record: :class:`tencentcloud.ags.v20250920.models.CloudRecord`
        :param _Version: <p>Version 创建模式返回：本次创建的新 Version。</p>
        :type Version: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        :param _UploadURL: <p>Version 创建模式且 SkillSource.Type=TAR_PACKAGE 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type UploadURL: str
        :param _ExpireTime: <p>Version 创建模式且 SkillSource.Type=TAR_PACKAGE 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _ContentStatus: <p>Version 创建模式且 SkillSource.Type=TAR_PACKAGE 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Record = None
        self._Version = None
        self._UploadURL = None
        self._ExpireTime = None
        self._ContentStatus = None
        self._RequestId = None

    @property
    def Record(self):
        r"""<p>更新后的 Record。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecord`
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def Version(self):
        r"""<p>Version 创建模式返回：本次创建的新 Version。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRecordVersion`
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def UploadURL(self):
        r"""<p>Version 创建模式且 SkillSource.Type=TAR_PACKAGE 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UploadURL

    @UploadURL.setter
    def UploadURL(self, UploadURL):
        self._UploadURL = UploadURL

    @property
    def ExpireTime(self):
        r"""<p>Version 创建模式且 SkillSource.Type=TAR_PACKAGE 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ContentStatus(self):
        r"""<p>Version 创建模式且 SkillSource.Type=TAR_PACKAGE 时返回。</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ContentStatus

    @ContentStatus.setter
    def ContentStatus(self, ContentStatus):
        self._ContentStatus = ContentStatus

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
        if params.get("Record") is not None:
            self._Record = CloudRecord()
            self._Record._deserialize(params.get("Record"))
        if params.get("Version") is not None:
            self._Version = CloudRecordVersion()
            self._Version._deserialize(params.get("Version"))
        self._UploadURL = params.get("UploadURL")
        self._ExpireTime = params.get("ExpireTime")
        self._ContentStatus = params.get("ContentStatus")
        self._RequestId = params.get("RequestId")


class UpdateRegistryRequest(AbstractModel):
    r"""UpdateRegistry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegistryId: <p>Registry ID。</p>
        :type RegistryId: str
        :param _Description: <p>新的描述；必填；最长 4096。</p>
        :type Description: str
        """
        self._RegistryId = None
        self._Description = None

    @property
    def RegistryId(self):
        r"""<p>Registry ID。</p>
        :rtype: str
        """
        return self._RegistryId

    @RegistryId.setter
    def RegistryId(self, RegistryId):
        self._RegistryId = RegistryId

    @property
    def Description(self):
        r"""<p>新的描述；必填；最长 4096。</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._RegistryId = params.get("RegistryId")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRegistryResponse(AbstractModel):
    r"""UpdateRegistry返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Registry: <p>更新后的 Registry 详情。</p>
        :type Registry: :class:`tencentcloud.ags.v20250920.models.CloudRegistry`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Registry = None
        self._RequestId = None

    @property
    def Registry(self):
        r"""<p>更新后的 Registry 详情。</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CloudRegistry`
        """
        return self._Registry

    @Registry.setter
    def Registry(self, Registry):
        self._Registry = Registry

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
        if params.get("Registry") is not None:
            self._Registry = CloudRegistry()
            self._Registry._deserialize(params.get("Registry"))
        self._RequestId = params.get("RequestId")


class UpdateSandboxInstanceRequest(AbstractModel):
    r"""UpdateSandboxInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: <p>沙箱实例ID</p>
        :type InstanceId: str
        :param _Timeout: <p>新的超时时间（从设置时开始重新计算超时），支持格式：5m、300s、1h等。最小30s，最大24h。如果不指定则保持原有超时设置</p>
        :type Timeout: str
        :param _Metadata: <p>沙箱实例元数据</p>
        :type Metadata: list of MetadataVar
        """
        self._InstanceId = None
        self._Timeout = None
        self._Metadata = None

    @property
    def InstanceId(self):
        r"""<p>沙箱实例ID</p>
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Timeout(self):
        r"""<p>新的超时时间（从设置时开始重新计算超时），支持格式：5m、300s、1h等。最小30s，最大24h。如果不指定则保持原有超时设置</p>
        :rtype: str
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def Metadata(self):
        r"""<p>沙箱实例元数据</p>
        :rtype: list of MetadataVar
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Timeout = params.get("Timeout")
        if params.get("Metadata") is not None:
            self._Metadata = []
            for item in params.get("Metadata"):
                obj = MetadataVar()
                obj._deserialize(item)
                self._Metadata.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSandboxInstanceResponse(AbstractModel):
    r"""UpdateSandboxInstance返回参数结构体

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


class UpdateSandboxToolRequest(AbstractModel):
    r"""UpdateSandboxTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ToolId: <p>沙箱工具ID</p>
        :type ToolId: str
        :param _Description: <p>沙箱工具描述，最大长度200字符</p>
        :type Description: str
        :param _NetworkConfiguration: <p>网络配置</p>
        :type NetworkConfiguration: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        :param _Tags: <p>标签</p>
        :type Tags: list of Tag
        :param _CustomConfiguration: <p>沙箱工具自定义配置</p>
        :type CustomConfiguration: :class:`tencentcloud.ags.v20250920.models.CustomConfiguration`
        :param _ComputerConfiguration: <p>桌面电脑环境类沙箱配置</p>
        :type ComputerConfiguration: :class:`tencentcloud.ags.v20250920.models.ComputerConfiguration`
        """
        self._ToolId = None
        self._Description = None
        self._NetworkConfiguration = None
        self._Tags = None
        self._CustomConfiguration = None
        self._ComputerConfiguration = None

    @property
    def ToolId(self):
        r"""<p>沙箱工具ID</p>
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def Description(self):
        r"""<p>沙箱工具描述，最大长度200字符</p>
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NetworkConfiguration(self):
        r"""<p>网络配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        """
        return self._NetworkConfiguration

    @NetworkConfiguration.setter
    def NetworkConfiguration(self, NetworkConfiguration):
        self._NetworkConfiguration = NetworkConfiguration

    @property
    def Tags(self):
        r"""<p>标签</p>
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CustomConfiguration(self):
        r"""<p>沙箱工具自定义配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.CustomConfiguration`
        """
        return self._CustomConfiguration

    @CustomConfiguration.setter
    def CustomConfiguration(self, CustomConfiguration):
        self._CustomConfiguration = CustomConfiguration

    @property
    def ComputerConfiguration(self):
        r"""<p>桌面电脑环境类沙箱配置</p>
        :rtype: :class:`tencentcloud.ags.v20250920.models.ComputerConfiguration`
        """
        return self._ComputerConfiguration

    @ComputerConfiguration.setter
    def ComputerConfiguration(self, ComputerConfiguration):
        self._ComputerConfiguration = ComputerConfiguration


    def _deserialize(self, params):
        self._ToolId = params.get("ToolId")
        self._Description = params.get("Description")
        if params.get("NetworkConfiguration") is not None:
            self._NetworkConfiguration = NetworkConfiguration()
            self._NetworkConfiguration._deserialize(params.get("NetworkConfiguration"))
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("CustomConfiguration") is not None:
            self._CustomConfiguration = CustomConfiguration()
            self._CustomConfiguration._deserialize(params.get("CustomConfiguration"))
        if params.get("ComputerConfiguration") is not None:
            self._ComputerConfiguration = ComputerConfiguration()
            self._ComputerConfiguration._deserialize(params.get("ComputerConfiguration"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateSandboxToolResponse(AbstractModel):
    r"""UpdateSandboxTool返回参数结构体

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


class VPCConfig(AbstractModel):
    r"""沙箱工具VPC相关配置

    """

    def __init__(self):
        r"""
        :param _SubnetIds: <p>VPC子网ID列表</p>
        :type SubnetIds: list of str
        :param _SecurityGroupIds: <p>安全组ID列表</p>
        :type SecurityGroupIds: list of str
        """
        self._SubnetIds = None
        self._SecurityGroupIds = None

    @property
    def SubnetIds(self):
        r"""<p>VPC子网ID列表</p>
        :rtype: list of str
        """
        return self._SubnetIds

    @SubnetIds.setter
    def SubnetIds(self, SubnetIds):
        self._SubnetIds = SubnetIds

    @property
    def SecurityGroupIds(self):
        r"""<p>安全组ID列表</p>
        :rtype: list of str
        """
        return self._SecurityGroupIds

    @SecurityGroupIds.setter
    def SecurityGroupIds(self, SecurityGroupIds):
        self._SecurityGroupIds = SecurityGroupIds


    def _deserialize(self, params):
        self._SubnetIds = params.get("SubnetIds")
        self._SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WAAConfiguration(AbstractModel):
    r"""waa自定义配置项

    """

    def __init__(self):
        r"""
        :param _ImageId: <p>自定义waa镜像ID</p>
        :type ImageId: str
        """
        self._ImageId = None

    @property
    def ImageId(self):
        r"""<p>自定义waa镜像ID</p>
        :rtype: str
        """
        return self._ImageId

    @ImageId.setter
    def ImageId(self, ImageId):
        self._ImageId = ImageId


    def _deserialize(self, params):
        self._ImageId = params.get("ImageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        