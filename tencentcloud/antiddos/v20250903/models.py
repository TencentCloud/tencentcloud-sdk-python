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


class AbnormalConnectCondition(AbstractModel):
    r"""连接异常条件。

    """

    def __init__(self):
        r"""
        :param _SynRatioThreshold: <p>SYN占比阈值（百分比）， 0为不检查。 同一连接中，SYN 包占比超过配置占比时，将被视为异常连接处置。</p><p>取值范围：[0, 100]</p>
        :type SynRatioThreshold: int
        :param _SynCountThreshold: <p>SYN占比阈值（百分比）， 0为不检查。 同一连接中，SYN 包占比超过配置占比时，将被视为异常连接处置。</p><p>取值范围：[0, 65535]</p>
        :type SynCountThreshold: int
        :param _ConnectTimeout: <p>连接超时（秒），0为不检查。 连接超过配置时间内未收到数据时，将被视为异常连接处置。</p><p>取值范围：[0, 65535]</p>
        :type ConnectTimeout: int
        :param _EmptyConnection: <p>是否开启空连接防护。 同一客户端对应了较大数量的空连接时，将被视为异常连接处置。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :type EmptyConnection: str
        """
        self._SynRatioThreshold = None
        self._SynCountThreshold = None
        self._ConnectTimeout = None
        self._EmptyConnection = None

    @property
    def SynRatioThreshold(self):
        r"""<p>SYN占比阈值（百分比）， 0为不检查。 同一连接中，SYN 包占比超过配置占比时，将被视为异常连接处置。</p><p>取值范围：[0, 100]</p>
        :rtype: int
        """
        return self._SynRatioThreshold

    @SynRatioThreshold.setter
    def SynRatioThreshold(self, SynRatioThreshold):
        self._SynRatioThreshold = SynRatioThreshold

    @property
    def SynCountThreshold(self):
        r"""<p>SYN占比阈值（百分比）， 0为不检查。 同一连接中，SYN 包占比超过配置占比时，将被视为异常连接处置。</p><p>取值范围：[0, 65535]</p>
        :rtype: int
        """
        return self._SynCountThreshold

    @SynCountThreshold.setter
    def SynCountThreshold(self, SynCountThreshold):
        self._SynCountThreshold = SynCountThreshold

    @property
    def ConnectTimeout(self):
        r"""<p>连接超时（秒），0为不检查。 连接超过配置时间内未收到数据时，将被视为异常连接处置。</p><p>取值范围：[0, 65535]</p>
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def EmptyConnection(self):
        r"""<p>是否开启空连接防护。 同一客户端对应了较大数量的空连接时，将被视为异常连接处置。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :rtype: str
        """
        return self._EmptyConnection

    @EmptyConnection.setter
    def EmptyConnection(self, EmptyConnection):
        self._EmptyConnection = EmptyConnection


    def _deserialize(self, params):
        self._SynRatioThreshold = params.get("SynRatioThreshold")
        self._SynCountThreshold = params.get("SynCountThreshold")
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._EmptyConnection = params.get("EmptyConnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AbnormalConnectionLimit(AbstractModel):
    r"""异常连接防护配置。

    """

    def __init__(self):
        r"""
        :param _AbnormalConnectThreshold: <p>异常连接数限制，限制同一时间单个源 IP 异常连接数量， 0为不启用, 范围: 0-4294967295。</p><p>取值范围：[0, 4294967295]</p>
        :type AbnormalConnectThreshold: int
        :param _AbnormalConnectCondition: <p>异常连接判定条件。满足任意条件则计为一次异常统计。</p>
        :type AbnormalConnectCondition: :class:`tencentcloud.antiddos.v20250903.models.AbnormalConnectCondition`
        """
        self._AbnormalConnectThreshold = None
        self._AbnormalConnectCondition = None

    @property
    def AbnormalConnectThreshold(self):
        r"""<p>异常连接数限制，限制同一时间单个源 IP 异常连接数量， 0为不启用, 范围: 0-4294967295。</p><p>取值范围：[0, 4294967295]</p>
        :rtype: int
        """
        return self._AbnormalConnectThreshold

    @AbnormalConnectThreshold.setter
    def AbnormalConnectThreshold(self, AbnormalConnectThreshold):
        self._AbnormalConnectThreshold = AbnormalConnectThreshold

    @property
    def AbnormalConnectCondition(self):
        r"""<p>异常连接判定条件。满足任意条件则计为一次异常统计。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.AbnormalConnectCondition`
        """
        return self._AbnormalConnectCondition

    @AbnormalConnectCondition.setter
    def AbnormalConnectCondition(self, AbnormalConnectCondition):
        self._AbnormalConnectCondition = AbnormalConnectCondition


    def _deserialize(self, params):
        self._AbnormalConnectThreshold = params.get("AbnormalConnectThreshold")
        if params.get("AbnormalConnectCondition") is not None:
            self._AbnormalConnectCondition = AbnormalConnectCondition()
            self._AbnormalConnectCondition._deserialize(params.get("AbnormalConnectCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectionProtectionConfig(AbstractModel):
    r"""连接类攻击防护配置。

    """

    def __init__(self):
        r"""
        :param _SourceIPNewConnectionLimit: <p>源 IP 每秒新建连接数限制，为 0 为不限制（关闭），大于 0 开启限制。命中后限制新建连接。</p><p>取值范围：[0, 4294967295]</p>
        :type SourceIPNewConnectionLimit: int
        :param _SourceIPConcurrentConnectionLimit: <p>源 IP 并发连接数限制，为 0 不限制（关闭），大于 0 开启限制。命中后限制新建连接。</p><p>取值范围：[0, 4294967295]</p>
        :type SourceIPConcurrentConnectionLimit: int
        :param _DestinationIPNewConnectionLimit: <p>目的 IP 每秒新建连接数限制，为 0 不限制（关闭），大于 0 开启限制。命中后限制新建连接。</p><p>取值范围：[0, 4294967295]</p>
        :type DestinationIPNewConnectionLimit: int
        :param _DestinationIPConcurrentConnectionLimit: <p>目的 IP 并发连接数限制，为 0 不限制（关闭）， 大于 0 开启限制。命中后限制新建连接。</p><p>取值范围：[0, 4294967295]</p>
        :type DestinationIPConcurrentConnectionLimit: int
        :param _AbnormalConnectionLimit: <p>源 IP 异常连接限制。</p>
        :type AbnormalConnectionLimit: :class:`tencentcloud.antiddos.v20250903.models.AbnormalConnectionLimit`
        """
        self._SourceIPNewConnectionLimit = None
        self._SourceIPConcurrentConnectionLimit = None
        self._DestinationIPNewConnectionLimit = None
        self._DestinationIPConcurrentConnectionLimit = None
        self._AbnormalConnectionLimit = None

    @property
    def SourceIPNewConnectionLimit(self):
        r"""<p>源 IP 每秒新建连接数限制，为 0 为不限制（关闭），大于 0 开启限制。命中后限制新建连接。</p><p>取值范围：[0, 4294967295]</p>
        :rtype: int
        """
        return self._SourceIPNewConnectionLimit

    @SourceIPNewConnectionLimit.setter
    def SourceIPNewConnectionLimit(self, SourceIPNewConnectionLimit):
        self._SourceIPNewConnectionLimit = SourceIPNewConnectionLimit

    @property
    def SourceIPConcurrentConnectionLimit(self):
        r"""<p>源 IP 并发连接数限制，为 0 不限制（关闭），大于 0 开启限制。命中后限制新建连接。</p><p>取值范围：[0, 4294967295]</p>
        :rtype: int
        """
        return self._SourceIPConcurrentConnectionLimit

    @SourceIPConcurrentConnectionLimit.setter
    def SourceIPConcurrentConnectionLimit(self, SourceIPConcurrentConnectionLimit):
        self._SourceIPConcurrentConnectionLimit = SourceIPConcurrentConnectionLimit

    @property
    def DestinationIPNewConnectionLimit(self):
        r"""<p>目的 IP 每秒新建连接数限制，为 0 不限制（关闭），大于 0 开启限制。命中后限制新建连接。</p><p>取值范围：[0, 4294967295]</p>
        :rtype: int
        """
        return self._DestinationIPNewConnectionLimit

    @DestinationIPNewConnectionLimit.setter
    def DestinationIPNewConnectionLimit(self, DestinationIPNewConnectionLimit):
        self._DestinationIPNewConnectionLimit = DestinationIPNewConnectionLimit

    @property
    def DestinationIPConcurrentConnectionLimit(self):
        r"""<p>目的 IP 并发连接数限制，为 0 不限制（关闭）， 大于 0 开启限制。命中后限制新建连接。</p><p>取值范围：[0, 4294967295]</p>
        :rtype: int
        """
        return self._DestinationIPConcurrentConnectionLimit

    @DestinationIPConcurrentConnectionLimit.setter
    def DestinationIPConcurrentConnectionLimit(self, DestinationIPConcurrentConnectionLimit):
        self._DestinationIPConcurrentConnectionLimit = DestinationIPConcurrentConnectionLimit

    @property
    def AbnormalConnectionLimit(self):
        r"""<p>源 IP 异常连接限制。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.AbnormalConnectionLimit`
        """
        return self._AbnormalConnectionLimit

    @AbnormalConnectionLimit.setter
    def AbnormalConnectionLimit(self, AbnormalConnectionLimit):
        self._AbnormalConnectionLimit = AbnormalConnectionLimit


    def _deserialize(self, params):
        self._SourceIPNewConnectionLimit = params.get("SourceIPNewConnectionLimit")
        self._SourceIPConcurrentConnectionLimit = params.get("SourceIPConcurrentConnectionLimit")
        self._DestinationIPNewConnectionLimit = params.get("DestinationIPNewConnectionLimit")
        self._DestinationIPConcurrentConnectionLimit = params.get("DestinationIPConcurrentConnectionLimit")
        if params.get("AbnormalConnectionLimit") is not None:
            self._AbnormalConnectionLimit = AbnormalConnectionLimit()
            self._AbnormalConnectionLimit._deserialize(params.get("AbnormalConnectionLimit"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProtectionRequest(AbstractModel):
    r"""CreateProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: <p>防护实例名称。</p><p>入参限制：防护实例名称最多 60 个字符，同一主账号下不可重名。</p>
        :type Name: str
        :param _ProtectionLevel: <p>防护实例的防护级别。</p><p>枚举值：</p><ul><li>advanced： 增强防护；</li><li>ultimate： 卓越防护，仅在当前主账号已订阅任意扩展包时可用。</li></ul><p>不同订阅套餐版本下可用的防护级别不同，可接入的防护资源类型与防护容量也相应不同，具体请参见 <a href="https://cloud.tencent.com/document/product/297/137986">DDoS 防护容量说明</a>。</p>
        :type ProtectionLevel: str
        :param _Tags: <p>标签。用于对防护实例进行分权限管控与分账。<p>需要先前往 <a href="https://console.cloud.tencent.com/tag/taglist">标签控制台</a> 创建对应标签，方可在此处传入标签键与标签值。</p></p>
        :type Tags: list of TagInfo
        """
        self._Name = None
        self._ProtectionLevel = None
        self._Tags = None

    @property
    def Name(self):
        r"""<p>防护实例名称。</p><p>入参限制：防护实例名称最多 60 个字符，同一主账号下不可重名。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProtectionLevel(self):
        r"""<p>防护实例的防护级别。</p><p>枚举值：</p><ul><li>advanced： 增强防护；</li><li>ultimate： 卓越防护，仅在当前主账号已订阅任意扩展包时可用。</li></ul><p>不同订阅套餐版本下可用的防护级别不同，可接入的防护资源类型与防护容量也相应不同，具体请参见 <a href="https://cloud.tencent.com/document/product/297/137986">DDoS 防护容量说明</a>。</p>
        :rtype: str
        """
        return self._ProtectionLevel

    @ProtectionLevel.setter
    def ProtectionLevel(self, ProtectionLevel):
        self._ProtectionLevel = ProtectionLevel

    @property
    def Tags(self):
        r"""<p>标签。用于对防护实例进行分权限管控与分账。<p>需要先前往 <a href="https://console.cloud.tencent.com/tag/taglist">标签控制台</a> 创建对应标签，方可在此处传入标签键与标签值。</p></p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._ProtectionLevel = params.get("ProtectionLevel")
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
        


class CreateProtectionResponse(AbstractModel):
    r"""CreateProtection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectionId: <p>防护实例 ID。</p>
        :type ProtectionId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProtectionId = None
        self._RequestId = None

    @property
    def ProtectionId(self):
        r"""<p>防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId

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
        self._ProtectionId = params.get("ProtectionId")
        self._RequestId = params.get("RequestId")


class DDoSBlockRecord(AbstractModel):
    r"""封堵记录

    """

    def __init__(self):
        r"""
        :param _Resource: <p>被封堵的资源，公网 IP，示例如下：</p><ul><li> 公网 IP：117.175.94.231。</li></ul>
        :type Resource: str
        :param _BlockTime: <p>被封堵的时间。</p>
        :type BlockTime: str
        :param _Status: <p>封堵解封状态。</p><p>枚举值：</p><ul><li>Blocked：已封堵；</li><li>Unblocking：解封中；</li><li>Unblocked：已解封。</li></ul>
        :type Status: str
        """
        self._Resource = None
        self._BlockTime = None
        self._Status = None

    @property
    def Resource(self):
        r"""<p>被封堵的资源，公网 IP，示例如下：</p><ul><li> 公网 IP：117.175.94.231。</li></ul>
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def BlockTime(self):
        r"""<p>被封堵的时间。</p>
        :rtype: str
        """
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime

    @property
    def Status(self):
        r"""<p>封堵解封状态。</p><p>枚举值：</p><ul><li>Blocked：已封堵；</li><li>Unblocking：解封中；</li><li>Unblocked：已解封。</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._BlockTime = params.get("BlockTime")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSUnblockQuota(AbstractModel):
    r"""当前账号剩余解封配额。付费订阅 DDoS 高防产品的账号，将根据产品规格获得解封次数配额，配额按日或按月周期提供。

    - 按日提供的解封配额在每天 00:00（UTC+8）重置，当天未使用的配额不会累计到次日。
    - 按月提供的解封配额每月首日00:00（UTC+8）重置重置，当月未使用的配额不会累计到次日。

    """

    def __init__(self):
        r"""
        :param _TotalQuota: <p>解封次数配额总数。</p>
        :type TotalQuota: int
        :param _UsedQuota: <p>已使用的配额总数。</p>
        :type UsedQuota: int
        :param _QuotaStartTime: <p>配额生效的起始时间。</p>
        :type QuotaStartTime: str
        :param _QuotaEndTime: <p>配额生效的结束时间。</p>
        :type QuotaEndTime: str
        """
        self._TotalQuota = None
        self._UsedQuota = None
        self._QuotaStartTime = None
        self._QuotaEndTime = None

    @property
    def TotalQuota(self):
        r"""<p>解封次数配额总数。</p>
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def UsedQuota(self):
        r"""<p>已使用的配额总数。</p>
        :rtype: int
        """
        return self._UsedQuota

    @UsedQuota.setter
    def UsedQuota(self, UsedQuota):
        self._UsedQuota = UsedQuota

    @property
    def QuotaStartTime(self):
        r"""<p>配额生效的起始时间。</p>
        :rtype: str
        """
        return self._QuotaStartTime

    @QuotaStartTime.setter
    def QuotaStartTime(self, QuotaStartTime):
        self._QuotaStartTime = QuotaStartTime

    @property
    def QuotaEndTime(self):
        r"""<p>配额生效的结束时间。</p>
        :rtype: str
        """
        return self._QuotaEndTime

    @QuotaEndTime.setter
    def QuotaEndTime(self, QuotaEndTime):
        self._QuotaEndTime = QuotaEndTime


    def _deserialize(self, params):
        self._TotalQuota = params.get("TotalQuota")
        self._UsedQuota = params.get("UsedQuota")
        self._QuotaStartTime = params.get("QuotaStartTime")
        self._QuotaEndTime = params.get("QuotaEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultProtectionConfig(AbstractModel):
    r"""DDoS 默认防护配置，用于设置清洗策略的灵敏度等级。

    """

    def __init__(self):
        r"""
        :param _SensitivityLevel: <p>DDoS 防护等级配置，决定清洗策略的灵敏度。</p><p>枚举值：</p><ul><li>high： 高灵敏度。清洗策略相对严格，建议在正常模式出现攻击透传时使用。</li><li>medium： 适中灵敏度（默认）。清洗策略适配绝大多数业务，可有效防护常见攻击。</li><li>low： 宽松灵敏度。清洗策略相对宽松，仅对具有明确攻击特征的攻击包进行防护。</li></ul><p>详见 <a href="https://cloud.tencent.com/document/product/297/139103">各个防护等级防护策略</a> 说明。</p>
        :type SensitivityLevel: str
        """
        self._SensitivityLevel = None

    @property
    def SensitivityLevel(self):
        r"""<p>DDoS 防护等级配置，决定清洗策略的灵敏度。</p><p>枚举值：</p><ul><li>high： 高灵敏度。清洗策略相对严格，建议在正常模式出现攻击透传时使用。</li><li>medium： 适中灵敏度（默认）。清洗策略适配绝大多数业务，可有效防护常见攻击。</li><li>low： 宽松灵敏度。清洗策略相对宽松，仅对具有明确攻击特征的攻击包进行防护。</li></ul><p>详见 <a href="https://cloud.tencent.com/document/product/297/139103">各个防护等级防护策略</a> 说明。</p>
        :rtype: str
        """
        return self._SensitivityLevel

    @SensitivityLevel.setter
    def SensitivityLevel(self, SensitivityLevel):
        self._SensitivityLevel = SensitivityLevel


    def _deserialize(self, params):
        self._SensitivityLevel = params.get("SensitivityLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProtectionRequest(AbstractModel):
    r"""DeleteProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectionId: <p>防护实例 ID。</p>
        :type ProtectionId: str
        """
        self._ProtectionId = None

    @property
    def ProtectionId(self):
        r"""<p>防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId


    def _deserialize(self, params):
        self._ProtectionId = params.get("ProtectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProtectionResponse(AbstractModel):
    r"""DeleteProtection返回参数结构体

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


class DescribeDDoSBlockRecordsRequest(AbstractModel):
    r"""DescribeDDoSBlockRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: <p>查询的起始时间。最高支持近一年的数据查询。</p><p>参数格式：2026-02-04T11:30:00+08:00。</p>
        :type StartTime: str
        :param _EndTime: <p>查询的结束时间。查询时间范围（EndTime - StartTime）需小于等于 31 天。</p><p>参数格式：2026-03-04T11:30:00+08:00。</p>
        :type EndTime: str
        :param _Filters: <p>过滤条件，Filters.Values 的上限为 20。该参数不填写时，返回当前 appid 下所有被封堵过的资源列表。详细的过滤条件如下：</p><ul><li> Resource：可按照被封堵的 IP 或者被封堵的资源六段式进行过滤；</li><li> Status：可按照被封堵的资源状态进行过滤。</li></ul><p>当 Filters.Name 取值为 Status 时，Filters.Values 取值有：</p><ul><li>Blocked：已封堵；</li><li>Unblocking：解封中；</li><li>Unblocked：已解封。</li></ul>
        :type Filters: list of Filter
        :param _Limit: <p>分页查询限制数，最大值为 100。</p><p>默认值：20</p>
        :type Limit: int
        :param _Offset: <p>分页查询偏移量。</p><p>默认值：0</p>
        :type Offset: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def StartTime(self):
        r"""<p>查询的起始时间。最高支持近一年的数据查询。</p><p>参数格式：2026-02-04T11:30:00+08:00。</p>
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""<p>查询的结束时间。查询时间范围（EndTime - StartTime）需小于等于 31 天。</p><p>参数格式：2026-03-04T11:30:00+08:00。</p>
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Filters(self):
        r"""<p>过滤条件，Filters.Values 的上限为 20。该参数不填写时，返回当前 appid 下所有被封堵过的资源列表。详细的过滤条件如下：</p><ul><li> Resource：可按照被封堵的 IP 或者被封堵的资源六段式进行过滤；</li><li> Status：可按照被封堵的资源状态进行过滤。</li></ul><p>当 Filters.Name 取值为 Status 时，Filters.Values 取值有：</p><ul><li>Blocked：已封堵；</li><li>Unblocking：解封中；</li><li>Unblocked：已解封。</li></ul>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""<p>分页查询限制数，最大值为 100。</p><p>默认值：20</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""<p>分页查询偏移量。</p><p>默认值：0</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlockRecordsResponse(AbstractModel):
    r"""DescribeDDoSBlockRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>封堵解封记录总数。</p>
        :type TotalCount: int
        :param _BlockRecords: <p>封堵解封记录。</p>
        :type BlockRecords: list of DDoSBlockRecord
        :param _UnblockQuotaInfo: <p>解封次数配额信息。</p>
        :type UnblockQuotaInfo: :class:`tencentcloud.antiddos.v20250903.models.DDoSUnblockQuota`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._BlockRecords = None
        self._UnblockQuotaInfo = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>封堵解封记录总数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def BlockRecords(self):
        r"""<p>封堵解封记录。</p>
        :rtype: list of DDoSBlockRecord
        """
        return self._BlockRecords

    @BlockRecords.setter
    def BlockRecords(self, BlockRecords):
        self._BlockRecords = BlockRecords

    @property
    def UnblockQuotaInfo(self):
        r"""<p>解封次数配额信息。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DDoSUnblockQuota`
        """
        return self._UnblockQuotaInfo

    @UnblockQuotaInfo.setter
    def UnblockQuotaInfo(self, UnblockQuotaInfo):
        self._UnblockQuotaInfo = UnblockQuotaInfo

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
        if params.get("BlockRecords") is not None:
            self._BlockRecords = []
            for item in params.get("BlockRecords"):
                obj = DDoSBlockRecord()
                obj._deserialize(item)
                self._BlockRecords.append(obj)
        if params.get("UnblockQuotaInfo") is not None:
            self._UnblockQuotaInfo = DDoSUnblockQuota()
            self._UnblockQuotaInfo._deserialize(params.get("UnblockQuotaInfo"))
        self._RequestId = params.get("RequestId")


class DescribeDDoSProtectionPolicyRequest(AbstractModel):
    r"""DescribeDDoSProtectionPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectionId: <p>防护实例 ID。</p>
        :type ProtectionId: str
        """
        self._ProtectionId = None

    @property
    def ProtectionId(self):
        r"""<p>防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId


    def _deserialize(self, params):
        self._ProtectionId = params.get("ProtectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSProtectionPolicyResponse(AbstractModel):
    r"""DescribeDDoSProtectionPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectionPolicy: <p>DDoS 防护策略。</p>
        :type ProtectionPolicy: :class:`tencentcloud.antiddos.v20250903.models.ProtectionPolicy`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProtectionPolicy = None
        self._RequestId = None

    @property
    def ProtectionPolicy(self):
        r"""<p>DDoS 防护策略。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.ProtectionPolicy`
        """
        return self._ProtectionPolicy

    @ProtectionPolicy.setter
    def ProtectionPolicy(self, ProtectionPolicy):
        self._ProtectionPolicy = ProtectionPolicy

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
        if params.get("ProtectionPolicy") is not None:
            self._ProtectionPolicy = ProtectionPolicy()
            self._ProtectionPolicy._deserialize(params.get("ProtectionPolicy"))
        self._RequestId = params.get("RequestId")


class DescribeProtectionResourcesRequest(AbstractModel):
    r"""DescribeProtectionResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectionId: <p>防护实例 ID。</p>
        :type ProtectionId: str
        :param _Offset: <p>分页查询偏移量。默认值：0。</p>
        :type Offset: int
        :param _Limit: <p>分页查询限制数目。默认值：20，最大值：100。</p>
        :type Limit: int
        :param _Filters: <p>过滤条件。<p><code>Filters</code> 数组的元素个数上限为 20。不填写该参数时，返回防护实例下的全部防护资源。</p><p>支持的过滤字段：</p><ul><li><code>ResourceType</code>：按防护资源类型过滤。可选项：<ul><li><code>cvm</code>：云服务器。</li><li><code>lighthouse</code>：轻量应用服务器。</li><li><code>clb</code>：负载均衡。</li><li><code>eip</code>：弹性公网 IP。</li><li><code>waf</code>：Web 应用防火墙。</li><li><code>teo_l7_domain</code>：EdgeOne 域名。</li><li><code>teo_l4_proxy</code>：EdgeOne 四层代理。</li></ul></li></ul></p>
        :type Filters: list of ProtectionFilter
        """
        self._ProtectionId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def ProtectionId(self):
        r"""<p>防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId

    @property
    def Offset(self):
        r"""<p>分页查询偏移量。默认值：0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>分页查询限制数目。默认值：20，最大值：100。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""<p>过滤条件。<p><code>Filters</code> 数组的元素个数上限为 20。不填写该参数时，返回防护实例下的全部防护资源。</p><p>支持的过滤字段：</p><ul><li><code>ResourceType</code>：按防护资源类型过滤。可选项：<ul><li><code>cvm</code>：云服务器。</li><li><code>lighthouse</code>：轻量应用服务器。</li><li><code>clb</code>：负载均衡。</li><li><code>eip</code>：弹性公网 IP。</li><li><code>waf</code>：Web 应用防火墙。</li><li><code>teo_l7_domain</code>：EdgeOne 域名。</li><li><code>teo_l4_proxy</code>：EdgeOne 四层代理。</li></ul></li></ul></p>
        :rtype: list of ProtectionFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._ProtectionId = params.get("ProtectionId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ProtectionFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProtectionResourcesResponse(AbstractModel):
    r"""DescribeProtectionResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>符合条件的防护资源总数。</p>
        :type TotalCount: int
        :param _ResourceInfos: <p>防护资源详细信息列表。</p>
        :type ResourceInfos: list of ResourceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._ResourceInfos = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>符合条件的防护资源总数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def ResourceInfos(self):
        r"""<p>防护资源详细信息列表。</p>
        :rtype: list of ResourceInfo
        """
        return self._ResourceInfos

    @ResourceInfos.setter
    def ResourceInfos(self, ResourceInfos):
        self._ResourceInfos = ResourceInfos

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
        if params.get("ResourceInfos") is not None:
            self._ResourceInfos = []
            for item in params.get("ResourceInfos"):
                obj = ResourceInfo()
                obj._deserialize(item)
                self._ResourceInfos.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeProtectionsRequest(AbstractModel):
    r"""DescribeProtections请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: <p>过滤条件。<p><code>Filters</code> 数组的元素个数上限为 20。不填写该参数时，返回当前账号下有权限的全部防护实例。</p><p>支持的过滤字段：</p><ul><li><code>Name</code>：按防护实例名称过滤。</li><li><code>ProtectionId</code>：按防护实例 ID 过滤。</li><li><code>ProtectionLevel</code>：按防护实例级别过滤。可选项：<ul><li><code>advanced</code>：增强防护。</li><li><code>ultimate</code>：卓越防护。</li></ul></li><li><code>Status</code>：按防护实例状态过滤。可选项：<ul><li><code>protecting</code>：防护中。</li><li><code>processing</code>：变更中。</li><li><code>disabling</code>：隔离中或删除中。</li><li><code>disabled</code>：已隔离。</li></ul></li><li><code>TagKey</code>：按标签键过滤。</li><li><code>TagValue</code>：按标签值过滤。</li></ul><p>模糊查询时支持过滤字段名包括 <code>Name</code>、<code>ProtectionId</code>、<code>ProtectionLevel</code>、<code>Status</code>、<code>TagKey</code>、<code>TagValue</code>。</p></p>
        :type Filters: list of ProtectionFilter
        :param _Offset: <p>分页查询偏移量。默认值：0。</p>
        :type Offset: int
        :param _Limit: <p>分页查询限制数目。默认值：20，最大值：100。</p>
        :type Limit: int
        """
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def Filters(self):
        r"""<p>过滤条件。<p><code>Filters</code> 数组的元素个数上限为 20。不填写该参数时，返回当前账号下有权限的全部防护实例。</p><p>支持的过滤字段：</p><ul><li><code>Name</code>：按防护实例名称过滤。</li><li><code>ProtectionId</code>：按防护实例 ID 过滤。</li><li><code>ProtectionLevel</code>：按防护实例级别过滤。可选项：<ul><li><code>advanced</code>：增强防护。</li><li><code>ultimate</code>：卓越防护。</li></ul></li><li><code>Status</code>：按防护实例状态过滤。可选项：<ul><li><code>protecting</code>：防护中。</li><li><code>processing</code>：变更中。</li><li><code>disabling</code>：隔离中或删除中。</li><li><code>disabled</code>：已隔离。</li></ul></li><li><code>TagKey</code>：按标签键过滤。</li><li><code>TagValue</code>：按标签值过滤。</li></ul><p>模糊查询时支持过滤字段名包括 <code>Name</code>、<code>ProtectionId</code>、<code>ProtectionLevel</code>、<code>Status</code>、<code>TagKey</code>、<code>TagValue</code>。</p></p>
        :rtype: list of ProtectionFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""<p>分页查询偏移量。默认值：0。</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""<p>分页查询限制数目。默认值：20，最大值：100。</p>
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ProtectionFilter()
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
        


class DescribeProtectionsResponse(AbstractModel):
    r"""DescribeProtections返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: <p>符合条件的防护实例个数。</p>
        :type TotalCount: int
        :param _Protections: <p>防护实例详细信息列表。</p>
        :type Protections: list of ProtectionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Protections = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""<p>符合条件的防护实例个数。</p>
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Protections(self):
        r"""<p>防护实例详细信息列表。</p>
        :rtype: list of ProtectionInfo
        """
        return self._Protections

    @Protections.setter
    def Protections(self, Protections):
        self._Protections = Protections

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
        if params.get("Protections") is not None:
            self._Protections = []
            for item in params.get("Protections"):
                obj = ProtectionInfo()
                obj._deserialize(item)
                self._Protections.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceProtectionsRequest(AbstractModel):
    r"""DescribeResourceProtections请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Resources: <p>防护资源，须采用资源六段式格式。具体格式如下：<ul><li>云服务器：<code>qcs::cvm:${region}:uin/${uin}:instance/${InstanceId}</code></li><li>轻量应用服务器：<code>qcs::lighthouse:${region}:uin/${uin}:instance/${InstanceId}</code></li><li>负载均衡：<code>qcs::clb:${region}:uin/${uin}:clb/${LoadBalancerId}</code></li><li>弹性公网 IP：<code>qcs::cvm:${region}:uin/${uin}:eip/${AddressId}</code></li><li>Web 应用防火墙：<code>qcs::waf:${region}:uin/${uin}:waf/${InstanceId}</code></li><li>EdgeOne 域名：<code>qcs::teo::uin/${uin}:zone/${ZoneId}/Domain/${Domain}</code></li><li>EdgeOne 四层代理：<code>qcs::teo::uin/${uin}:zone/${ZoneId}/L4Proxy/${InstanceId}</code></li></ul></p><p>取值参考：<a href="https://cloud.tencent.com/document/product/598/67350">支持 CAM 的业务接口</a></p>
        :type Resources: list of str
        """
        self._Resources = None

    @property
    def Resources(self):
        r"""<p>防护资源，须采用资源六段式格式。具体格式如下：<ul><li>云服务器：<code>qcs::cvm:${region}:uin/${uin}:instance/${InstanceId}</code></li><li>轻量应用服务器：<code>qcs::lighthouse:${region}:uin/${uin}:instance/${InstanceId}</code></li><li>负载均衡：<code>qcs::clb:${region}:uin/${uin}:clb/${LoadBalancerId}</code></li><li>弹性公网 IP：<code>qcs::cvm:${region}:uin/${uin}:eip/${AddressId}</code></li><li>Web 应用防火墙：<code>qcs::waf:${region}:uin/${uin}:waf/${InstanceId}</code></li><li>EdgeOne 域名：<code>qcs::teo::uin/${uin}:zone/${ZoneId}/Domain/${Domain}</code></li><li>EdgeOne 四层代理：<code>qcs::teo::uin/${uin}:zone/${ZoneId}/L4Proxy/${InstanceId}</code></li></ul></p><p>取值参考：<a href="https://cloud.tencent.com/document/product/598/67350">支持 CAM 的业务接口</a></p>
        :rtype: list of str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        self._Resources = params.get("Resources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceProtectionsResponse(AbstractModel):
    r"""DescribeResourceProtections返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceProtections: <p>防护资源对应的防护实例列表。资源未绑定任何防护实例时，返回空数组。</p>
        :type ResourceProtections: list of ResourceProtection
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResourceProtections = None
        self._RequestId = None

    @property
    def ResourceProtections(self):
        r"""<p>防护资源对应的防护实例列表。资源未绑定任何防护实例时，返回空数组。</p>
        :rtype: list of ResourceProtection
        """
        return self._ResourceProtections

    @ResourceProtections.setter
    def ResourceProtections(self, ResourceProtections):
        self._ResourceProtections = ResourceProtections

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
        if params.get("ResourceProtections") is not None:
            self._ResourceProtections = []
            for item in params.get("ResourceProtections"):
                obj = ResourceProtection()
                obj._deserialize(item)
                self._ResourceProtections.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    r"""描述键值对过滤器，用于条件过滤查询。例如过滤 ID、名称、状态等。 若存在多个 Filter 时，Filter 间的关系为逻辑与（AND）关系。 若同一个 Filter 存在多个 Values，同一 Filter 下 Values 间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: <p>需要过滤的字段；具体可选择值请查看对应的引用接口。</p>
        :type Name: str
        :param _Values: <p>字段的过滤值。</p>
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        r"""<p>需要过滤的字段；具体可选择值请查看对应的引用接口。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>字段的过滤值。</p>
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
        


class GeoBlockingConfig(AbstractModel):
    r"""区域封禁配置。

    """

    def __init__(self):
        r"""
        :param _GeoCode: <p>封禁地域列表。采用<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"> ISO 3166-1 alpha-2 </a>标准的两字代码。</p>
        :type GeoCode: list of str
        """
        self._GeoCode = None

    @property
    def GeoCode(self):
        r"""<p>封禁地域列表。采用<a href="https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"> ISO 3166-1 alpha-2 </a>标准的两字代码。</p>
        :rtype: list of str
        """
        return self._GeoCode

    @GeoCode.setter
    def GeoCode(self, GeoCode):
        self._GeoCode = GeoCode


    def _deserialize(self, params):
        self._GeoCode = params.get("GeoCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPACLRule(AbstractModel):
    r"""IP 黑白名单规则。

    """

    def __init__(self):
        r"""
        :param _Action: <p>处置方式。</p><p>枚举值：</p><ul><li>drop： 黑名单（拦截）。</li><li>allow： 白名单（放行）。</li></ul>
        :type Action: str
        :param _IPs: <p>IP 列表。</p><p>参数格式：支持 IPv4、IPv6 和 CIDR 格式。</p>
        :type IPs: list of str
        """
        self._Action = None
        self._IPs = None

    @property
    def Action(self):
        r"""<p>处置方式。</p><p>枚举值：</p><ul><li>drop： 黑名单（拦截）。</li><li>allow： 白名单（放行）。</li></ul>
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def IPs(self):
        r"""<p>IP 列表。</p><p>参数格式：支持 IPv4、IPv6 和 CIDR 格式。</p>
        :rtype: list of str
        """
        return self._IPs

    @IPs.setter
    def IPs(self, IPs):
        self._IPs = IPs


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._IPs = params.get("IPs")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPACLRules(AbstractModel):
    r"""IP 黑白名单规则列表。

    """

    def __init__(self):
        r"""
        :param _Rules: <p>IP 黑白名单规则列表。</p>
        :type Rules: list of IPACLRule
        """
        self._Rules = None

    @property
    def Rules(self):
        r"""<p>IP 黑白名单规则列表。</p>
        :rtype: list of IPACLRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = IPACLRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSProtectionPolicyRequest(AbstractModel):
    r"""ModifyDDoSProtectionPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectionId: <p>防护实例 ID。</p>
        :type ProtectionId: str
        :param _ProtectionPolicy: <p>防护策略。</p><p>支持部分修改：对于 <code>ProtectionPolicy</code> 下的各子策略，入参未传入的子策略保持原值不变。</p>
        :type ProtectionPolicy: :class:`tencentcloud.antiddos.v20250903.models.ProtectionPolicy`
        """
        self._ProtectionId = None
        self._ProtectionPolicy = None

    @property
    def ProtectionId(self):
        r"""<p>防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId

    @property
    def ProtectionPolicy(self):
        r"""<p>防护策略。</p><p>支持部分修改：对于 <code>ProtectionPolicy</code> 下的各子策略，入参未传入的子策略保持原值不变。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.ProtectionPolicy`
        """
        return self._ProtectionPolicy

    @ProtectionPolicy.setter
    def ProtectionPolicy(self, ProtectionPolicy):
        self._ProtectionPolicy = ProtectionPolicy


    def _deserialize(self, params):
        self._ProtectionId = params.get("ProtectionId")
        if params.get("ProtectionPolicy") is not None:
            self._ProtectionPolicy = ProtectionPolicy()
            self._ProtectionPolicy._deserialize(params.get("ProtectionPolicy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSProtectionPolicyResponse(AbstractModel):
    r"""ModifyDDoSProtectionPolicy返回参数结构体

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


class ModifyProtectionRequest(AbstractModel):
    r"""ModifyProtection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectionId: <p>防护实例 ID。</p>
        :type ProtectionId: str
        :param _Name: <p>防护实例名称。</p><p>入参限制：防护实例名称最多 60 个字符，同一主账号下不可重名。</p>
        :type Name: str
        """
        self._ProtectionId = None
        self._Name = None

    @property
    def ProtectionId(self):
        r"""<p>防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId

    @property
    def Name(self):
        r"""<p>防护实例名称。</p><p>入参限制：防护实例名称最多 60 个字符，同一主账号下不可重名。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._ProtectionId = params.get("ProtectionId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProtectionResourceRequest(AbstractModel):
    r"""ModifyProtectionResource请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProtectionId: <p>防护实例 ID。</p>
        :type ProtectionId: str
        :param _Mode: <p>操作类型。</p><p>枚举值：</p><ul><li>APPEND： 向防护实例中添加新的防护资源；</li><li>UPDATE： 替换防护实例中的全部防护资源；</li><li>REMOVE： 从防护实例中移除指定的防护资源。</li></ul><p>默认值：APPEND</p>
        :type Mode: str
        :param _Resources: <p>防护资源，须采用资源六段式格式。具体格式如下：<ul><li>云服务器：<code>qcs::cvm:${region}:uin/${uin}:instance/${InstanceId}</code></li><li>轻量应用服务器：<code>qcs::lighthouse:${region}:uin/${uin}:instance/${InstanceId}</code></li><li>负载均衡：<code>qcs::clb:${region}:uin/${uin}:clb/${LoadBalancerId}</code></li><li>弹性公网 IP：<code>qcs::cvm:${region}:uin/${uin}:eip/${AddressId}</code></li><li>Web 应用防火墙：<code>qcs::waf:${region}:uin/${uin}:waf/${InstanceId}</code></li><li>EdgeOne 域名：<code>qcs::teo::uin/${uin}:zone/${ZoneId}/Domain/${Domain}</code></li><li>EdgeOne 四层代理：<code>qcs::teo::uin/${uin}:zone/${ZoneId}/L4Proxy/${InstanceId}</code></li></ul></p><p>取值参考：<a href="https://cloud.tencent.com/document/product/598/67350">支持 CAM 的业务接口</a></p>
        :type Resources: list of str
        :param _ConflictStrategy: <p>冲突策略。</p><p>枚举值：</p><ul><li>REJECT： 若任一防护资源已存在于其他防护实例，则拒绝本次操作。</li><li>FORCE： 若任一防护资源已存在于其他防护实例，则强制将其添加至当前实例。</li></ul><p>默认值：REJECT</p>
        :type ConflictStrategy: str
        """
        self._ProtectionId = None
        self._Mode = None
        self._Resources = None
        self._ConflictStrategy = None

    @property
    def ProtectionId(self):
        r"""<p>防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId

    @property
    def Mode(self):
        r"""<p>操作类型。</p><p>枚举值：</p><ul><li>APPEND： 向防护实例中添加新的防护资源；</li><li>UPDATE： 替换防护实例中的全部防护资源；</li><li>REMOVE： 从防护实例中移除指定的防护资源。</li></ul><p>默认值：APPEND</p>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Resources(self):
        r"""<p>防护资源，须采用资源六段式格式。具体格式如下：<ul><li>云服务器：<code>qcs::cvm:${region}:uin/${uin}:instance/${InstanceId}</code></li><li>轻量应用服务器：<code>qcs::lighthouse:${region}:uin/${uin}:instance/${InstanceId}</code></li><li>负载均衡：<code>qcs::clb:${region}:uin/${uin}:clb/${LoadBalancerId}</code></li><li>弹性公网 IP：<code>qcs::cvm:${region}:uin/${uin}:eip/${AddressId}</code></li><li>Web 应用防火墙：<code>qcs::waf:${region}:uin/${uin}:waf/${InstanceId}</code></li><li>EdgeOne 域名：<code>qcs::teo::uin/${uin}:zone/${ZoneId}/Domain/${Domain}</code></li><li>EdgeOne 四层代理：<code>qcs::teo::uin/${uin}:zone/${ZoneId}/L4Proxy/${InstanceId}</code></li></ul></p><p>取值参考：<a href="https://cloud.tencent.com/document/product/598/67350">支持 CAM 的业务接口</a></p>
        :rtype: list of str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources

    @property
    def ConflictStrategy(self):
        r"""<p>冲突策略。</p><p>枚举值：</p><ul><li>REJECT： 若任一防护资源已存在于其他防护实例，则拒绝本次操作。</li><li>FORCE： 若任一防护资源已存在于其他防护实例，则强制将其添加至当前实例。</li></ul><p>默认值：REJECT</p>
        :rtype: str
        """
        return self._ConflictStrategy

    @ConflictStrategy.setter
    def ConflictStrategy(self, ConflictStrategy):
        self._ConflictStrategy = ConflictStrategy


    def _deserialize(self, params):
        self._ProtectionId = params.get("ProtectionId")
        self._Mode = params.get("Mode")
        self._Resources = params.get("Resources")
        self._ConflictStrategy = params.get("ConflictStrategy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProtectionResourceResponse(AbstractModel):
    r"""ModifyProtectionResource返回参数结构体

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


class ModifyProtectionResponse(AbstractModel):
    r"""ModifyProtection返回参数结构体

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


class PacketFilterCondition(AbstractModel):
    r"""报文匹配条件。

    """

    def __init__(self):
        r"""
        :param _MatchBegin: <p>报文匹配的起始位置。</p><p>枚举值：</p><ul><li>ip_header： 从 IP 头部开始匹配。</li><li>transport_header： 从 TCP/UDP 头部开始匹配。</li><li>payload： 从应用层载荷开始匹配。</li></ul>
        :type MatchBegin: str
        :param _Content: <p>报文匹配内容。</p>
        :type Content: :class:`tencentcloud.antiddos.v20250903.models.PacketMatchContent`
        """
        self._MatchBegin = None
        self._Content = None

    @property
    def MatchBegin(self):
        r"""<p>报文匹配的起始位置。</p><p>枚举值：</p><ul><li>ip_header： 从 IP 头部开始匹配。</li><li>transport_header： 从 TCP/UDP 头部开始匹配。</li><li>payload： 从应用层载荷开始匹配。</li></ul>
        :rtype: str
        """
        return self._MatchBegin

    @MatchBegin.setter
    def MatchBegin(self, MatchBegin):
        self._MatchBegin = MatchBegin

    @property
    def Content(self):
        r"""<p>报文匹配内容。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.PacketMatchContent`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._MatchBegin = params.get("MatchBegin")
        if params.get("Content") is not None:
            self._Content = PacketMatchContent()
            self._Content._deserialize(params.get("Content"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketFilterRule(AbstractModel):
    r"""特征过滤规则。

    """

    def __init__(self):
        r"""
        :param _Action: <p>匹配后执行的动作。</p><p>枚举值：</p><ul><li>drop： 丢弃。</li><li>allow： 放行。</li><li>drop_and_block： 丢弃并拉黑。</li><li>forward： 继续防护，即继续执行下一个防护子策略，而非特征过滤内的其他规则。</li></ul>
        :type Action: str
        :param _Protocol: <p>协议类型。</p><p>枚举值：</p><ul><li>tcp： TCP 协议。</li><li>udp： UDP 协议。</li><li>all： 所有协议。</li></ul>
        :type Protocol: str
        :param _PacketSizeRange: <p>报文长度范围。</p>
        :type PacketSizeRange: :class:`tencentcloud.antiddos.v20250903.models.SizeRange`
        :param _SourcePortRange: <p>源端口范围。</p>
        :type SourcePortRange: :class:`tencentcloud.antiddos.v20250903.models.PortRange`
        :param _DestinationPortRange: <p>目的端口范围。</p>
        :type DestinationPortRange: :class:`tencentcloud.antiddos.v20250903.models.PortRange`
        :param _PacketFilterConditions: <p>报文匹配条件列表。</p>
        :type PacketFilterConditions: list of PacketFilterCondition
        """
        self._Action = None
        self._Protocol = None
        self._PacketSizeRange = None
        self._SourcePortRange = None
        self._DestinationPortRange = None
        self._PacketFilterConditions = None

    @property
    def Action(self):
        r"""<p>匹配后执行的动作。</p><p>枚举值：</p><ul><li>drop： 丢弃。</li><li>allow： 放行。</li><li>drop_and_block： 丢弃并拉黑。</li><li>forward： 继续防护，即继续执行下一个防护子策略，而非特征过滤内的其他规则。</li></ul>
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Protocol(self):
        r"""<p>协议类型。</p><p>枚举值：</p><ul><li>tcp： TCP 协议。</li><li>udp： UDP 协议。</li><li>all： 所有协议。</li></ul>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def PacketSizeRange(self):
        r"""<p>报文长度范围。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.SizeRange`
        """
        return self._PacketSizeRange

    @PacketSizeRange.setter
    def PacketSizeRange(self, PacketSizeRange):
        self._PacketSizeRange = PacketSizeRange

    @property
    def SourcePortRange(self):
        r"""<p>源端口范围。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.PortRange`
        """
        return self._SourcePortRange

    @SourcePortRange.setter
    def SourcePortRange(self, SourcePortRange):
        self._SourcePortRange = SourcePortRange

    @property
    def DestinationPortRange(self):
        r"""<p>目的端口范围。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.PortRange`
        """
        return self._DestinationPortRange

    @DestinationPortRange.setter
    def DestinationPortRange(self, DestinationPortRange):
        self._DestinationPortRange = DestinationPortRange

    @property
    def PacketFilterConditions(self):
        r"""<p>报文匹配条件列表。</p>
        :rtype: list of PacketFilterCondition
        """
        return self._PacketFilterConditions

    @PacketFilterConditions.setter
    def PacketFilterConditions(self, PacketFilterConditions):
        self._PacketFilterConditions = PacketFilterConditions


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Protocol = params.get("Protocol")
        if params.get("PacketSizeRange") is not None:
            self._PacketSizeRange = SizeRange()
            self._PacketSizeRange._deserialize(params.get("PacketSizeRange"))
        if params.get("SourcePortRange") is not None:
            self._SourcePortRange = PortRange()
            self._SourcePortRange._deserialize(params.get("SourcePortRange"))
        if params.get("DestinationPortRange") is not None:
            self._DestinationPortRange = PortRange()
            self._DestinationPortRange._deserialize(params.get("DestinationPortRange"))
        if params.get("PacketFilterConditions") is not None:
            self._PacketFilterConditions = []
            for item in params.get("PacketFilterConditions"):
                obj = PacketFilterCondition()
                obj._deserialize(item)
                self._PacketFilterConditions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketFilterRules(AbstractModel):
    r"""特征过滤规则列表。

    """

    def __init__(self):
        r"""
        :param _Rules: <p>特征过滤规则列表。</p>
        :type Rules: list of PacketFilterRule
        """
        self._Rules = None

    @property
    def Rules(self):
        r"""<p>特征过滤规则列表。</p>
        :rtype: list of PacketFilterRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PacketFilterRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketMatchContent(AbstractModel):
    r"""报文匹配内容。

    """

    def __init__(self):
        r"""
        :param _Type: <p>匹配值 Value 的格式类型。</p><p>枚举值：</p><ul><li>string： 明文字符串。</li><li>hex： 十六进制字符串。</li></ul>
        :type Type: str
        :param _Value: <p>匹配值。Type=string 时为明文字符串，例如 <code>GET /index</code>；Type=hex 时为十六进制字符串，例如 <code>0x7e2f68656c6c6f</code>。</p>
        :type Value: str
        :param _Offset: <p>匹配起始偏移量，从匹配起始位置（MatchBegin）开始计算。</p><p>取值范围：[0, 1500]</p><p>单位：字节</p>
        :type Offset: int
        :param _Depth: <p>检查深度，即从 Offset 开始的最大检查字节数。</p><p>取值范围：[0, 1500]</p><p>单位：字节</p>
        :type Depth: int
        """
        self._Type = None
        self._Value = None
        self._Offset = None
        self._Depth = None

    @property
    def Type(self):
        r"""<p>匹配值 Value 的格式类型。</p><p>枚举值：</p><ul><li>string： 明文字符串。</li><li>hex： 十六进制字符串。</li></ul>
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        r"""<p>匹配值。Type=string 时为明文字符串，例如 <code>GET /index</code>；Type=hex 时为十六进制字符串，例如 <code>0x7e2f68656c6c6f</code>。</p>
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Offset(self):
        r"""<p>匹配起始偏移量，从匹配起始位置（MatchBegin）开始计算。</p><p>取值范围：[0, 1500]</p><p>单位：字节</p>
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Depth(self):
        r"""<p>检查深度，即从 Offset 开始的最大检查字节数。</p><p>取值范围：[0, 1500]</p><p>单位：字节</p>
        :rtype: int
        """
        return self._Depth

    @Depth.setter
    def Depth(self, Depth):
        self._Depth = Depth


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        self._Offset = params.get("Offset")
        self._Depth = params.get("Depth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortACLRule(AbstractModel):
    r"""端口过滤规则。

    """

    def __init__(self):
        r"""
        :param _SourcePortRange: <p>源端口范围。</p>
        :type SourcePortRange: :class:`tencentcloud.antiddos.v20250903.models.PortRange`
        :param _DestinationPortRange: <p>目的端口范围。</p>
        :type DestinationPortRange: :class:`tencentcloud.antiddos.v20250903.models.PortRange`
        :param _Protocol: <p>协议类型。</p><p>枚举值：</p><ul><li>all ： 所有协议。</li><li>tcp： TCP 协议。</li><li>udp： UDP 协议。</li></ul>
        :type Protocol: str
        :param _Action: <p>处置动作。</p><p>枚举值：</p><ul><li>drop： 丢弃。</li><li>allow： 放行。</li><li>forward： 继续防护，即继续执行下一个防护子策略模块，而非端口过滤内的其他规则。</li></ul>
        :type Action: str
        """
        self._SourcePortRange = None
        self._DestinationPortRange = None
        self._Protocol = None
        self._Action = None

    @property
    def SourcePortRange(self):
        r"""<p>源端口范围。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.PortRange`
        """
        return self._SourcePortRange

    @SourcePortRange.setter
    def SourcePortRange(self, SourcePortRange):
        self._SourcePortRange = SourcePortRange

    @property
    def DestinationPortRange(self):
        r"""<p>目的端口范围。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.PortRange`
        """
        return self._DestinationPortRange

    @DestinationPortRange.setter
    def DestinationPortRange(self, DestinationPortRange):
        self._DestinationPortRange = DestinationPortRange

    @property
    def Protocol(self):
        r"""<p>协议类型。</p><p>枚举值：</p><ul><li>all ： 所有协议。</li><li>tcp： TCP 协议。</li><li>udp： UDP 协议。</li></ul>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Action(self):
        r"""<p>处置动作。</p><p>枚举值：</p><ul><li>drop： 丢弃。</li><li>allow： 放行。</li><li>forward： 继续防护，即继续执行下一个防护子策略模块，而非端口过滤内的其他规则。</li></ul>
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action


    def _deserialize(self, params):
        if params.get("SourcePortRange") is not None:
            self._SourcePortRange = PortRange()
            self._SourcePortRange._deserialize(params.get("SourcePortRange"))
        if params.get("DestinationPortRange") is not None:
            self._DestinationPortRange = PortRange()
            self._DestinationPortRange._deserialize(params.get("DestinationPortRange"))
        self._Protocol = params.get("Protocol")
        self._Action = params.get("Action")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortACLRules(AbstractModel):
    r"""端口过滤规则列表。

    """

    def __init__(self):
        r"""
        :param _Rules: <p>端口过滤规则列表。</p>
        :type Rules: list of PortACLRule
        """
        self._Rules = None

    @property
    def Rules(self):
        r"""<p>端口过滤规则列表。</p>
        :rtype: list of PortACLRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = PortACLRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortRange(AbstractModel):
    r"""端口范围。

    """

    def __init__(self):
        r"""
        :param _FromPort: <p>起始端口。</p><p>取值范围：[1, 65535]</p><p>与 <code>ToPort</code> 相同时表示单个端口。</p>
        :type FromPort: int
        :param _ToPort: <p>结束端口</p><p>取值范围：[1, 65535]</p>
        :type ToPort: int
        """
        self._FromPort = None
        self._ToPort = None

    @property
    def FromPort(self):
        r"""<p>起始端口。</p><p>取值范围：[1, 65535]</p><p>与 <code>ToPort</code> 相同时表示单个端口。</p>
        :rtype: int
        """
        return self._FromPort

    @FromPort.setter
    def FromPort(self, FromPort):
        self._FromPort = FromPort

    @property
    def ToPort(self):
        r"""<p>结束端口</p><p>取值范围：[1, 65535]</p>
        :rtype: int
        """
        return self._ToPort

    @ToPort.setter
    def ToPort(self, ToPort):
        self._ToPort = ToPort


    def _deserialize(self, params):
        self._FromPort = params.get("FromPort")
        self._ToPort = params.get("ToPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectionFilter(AbstractModel):
    r"""用于按指定字段过滤查询结果，例如按防护实例 ID、名称、状态等过滤。多个 Filter 之间为逻辑与（AND）关系；同一 Filter 的多个 Values 之间为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: <p>需要过滤的字段名。</p>
        :type Name: str
        :param _Values: <p>对应字段的过滤值。</p>
        :type Values: list of str
        :param _Fuzzy: <p>是否启用模糊查询。</p>
        :type Fuzzy: bool
        """
        self._Name = None
        self._Values = None
        self._Fuzzy = None

    @property
    def Name(self):
        r"""<p>需要过滤的字段名。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>对应字段的过滤值。</p>
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def Fuzzy(self):
        r"""<p>是否启用模糊查询。</p>
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectionInfo(AbstractModel):
    r"""DDoS 防护实例信息。

    """

    def __init__(self):
        r"""
        :param _ProtectionId: <p>防护实例 ID。</p>
        :type ProtectionId: str
        :param _Name: <p>防护实例名称。</p>
        :type Name: str
        :param _ProtectionLevel: <p>防护实例的防护级别。</p><p>枚举值：</p><ul><li>advanced： 增强防护；</li><li>ultimate： 卓越防护。</li></ul>
        :type ProtectionLevel: str
        :param _Status: <p>防护实例状态。</p><p>枚举值：</p><ul><li>protecting： 防护中；</li><li>processing： 变更中；</li><li>disabling： 停用中；</li><li>disabled： 已停用。</li></ul>
        :type Status: str
        :param _Tags: <p>资源标签列表。</p>
        :type Tags: list of TagInfo
        :param _ResourceCount: <p>防护实例中的防护资源数量。</p>
        :type ResourceCount: int
        """
        self._ProtectionId = None
        self._Name = None
        self._ProtectionLevel = None
        self._Status = None
        self._Tags = None
        self._ResourceCount = None

    @property
    def ProtectionId(self):
        r"""<p>防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId

    @property
    def Name(self):
        r"""<p>防护实例名称。</p>
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ProtectionLevel(self):
        r"""<p>防护实例的防护级别。</p><p>枚举值：</p><ul><li>advanced： 增强防护；</li><li>ultimate： 卓越防护。</li></ul>
        :rtype: str
        """
        return self._ProtectionLevel

    @ProtectionLevel.setter
    def ProtectionLevel(self, ProtectionLevel):
        self._ProtectionLevel = ProtectionLevel

    @property
    def Status(self):
        r"""<p>防护实例状态。</p><p>枚举值：</p><ul><li>protecting： 防护中；</li><li>processing： 变更中；</li><li>disabling： 停用中；</li><li>disabled： 已停用。</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Tags(self):
        r"""<p>资源标签列表。</p>
        :rtype: list of TagInfo
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ResourceCount(self):
        r"""<p>防护实例中的防护资源数量。</p>
        :rtype: int
        """
        return self._ResourceCount

    @ResourceCount.setter
    def ResourceCount(self, ResourceCount):
        self._ResourceCount = ResourceCount


    def _deserialize(self, params):
        self._ProtectionId = params.get("ProtectionId")
        self._Name = params.get("Name")
        self._ProtectionLevel = params.get("ProtectionLevel")
        self._Status = params.get("Status")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._ResourceCount = params.get("ResourceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectionPolicy(AbstractModel):
    r"""防护实例的 L3/4 DDoS 防护策略。

    """

    def __init__(self):
        r"""
        :param _DefaultProtection: <p>默认防护配置。</p>
        :type DefaultProtection: :class:`tencentcloud.antiddos.v20250903.models.DefaultProtectionConfig`
        :param _IPACLRules: <p>IP 黑白名单规则列表。</p>
        :type IPACLRules: :class:`tencentcloud.antiddos.v20250903.models.IPACLRules`
        :param _PortACLRules: <p>端口过滤规则列表。</p>
        :type PortACLRules: :class:`tencentcloud.antiddos.v20250903.models.PortACLRules`
        :param _SpeedLimitRules: <p>限速规则列表。</p>
        :type SpeedLimitRules: :class:`tencentcloud.antiddos.v20250903.models.SpeedLimitRules`
        :param _PacketFilterRules: <p>包特征过滤规则列表。</p>
        :type PacketFilterRules: :class:`tencentcloud.antiddos.v20250903.models.PacketFilterRules`
        :param _GeoBlocking: <p>区域封禁配置。</p>
        :type GeoBlocking: :class:`tencentcloud.antiddos.v20250903.models.GeoBlockingConfig`
        :param _ProtocolBlocking: <p>协议封禁配置。</p>
        :type ProtocolBlocking: :class:`tencentcloud.antiddos.v20250903.models.ProtocolBlockingConfig`
        :param _ConnectionProtection: <p>连接类攻击防护配置。</p>
        :type ConnectionProtection: :class:`tencentcloud.antiddos.v20250903.models.ConnectionProtectionConfig`
        :param _TrafficSignature: <p>流量签名配置。</p>
        :type TrafficSignature: :class:`tencentcloud.antiddos.v20250903.models.TrafficSignatureConfig`
        """
        self._DefaultProtection = None
        self._IPACLRules = None
        self._PortACLRules = None
        self._SpeedLimitRules = None
        self._PacketFilterRules = None
        self._GeoBlocking = None
        self._ProtocolBlocking = None
        self._ConnectionProtection = None
        self._TrafficSignature = None

    @property
    def DefaultProtection(self):
        r"""<p>默认防护配置。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.DefaultProtectionConfig`
        """
        return self._DefaultProtection

    @DefaultProtection.setter
    def DefaultProtection(self, DefaultProtection):
        self._DefaultProtection = DefaultProtection

    @property
    def IPACLRules(self):
        r"""<p>IP 黑白名单规则列表。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.IPACLRules`
        """
        return self._IPACLRules

    @IPACLRules.setter
    def IPACLRules(self, IPACLRules):
        self._IPACLRules = IPACLRules

    @property
    def PortACLRules(self):
        r"""<p>端口过滤规则列表。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.PortACLRules`
        """
        return self._PortACLRules

    @PortACLRules.setter
    def PortACLRules(self, PortACLRules):
        self._PortACLRules = PortACLRules

    @property
    def SpeedLimitRules(self):
        r"""<p>限速规则列表。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.SpeedLimitRules`
        """
        return self._SpeedLimitRules

    @SpeedLimitRules.setter
    def SpeedLimitRules(self, SpeedLimitRules):
        self._SpeedLimitRules = SpeedLimitRules

    @property
    def PacketFilterRules(self):
        r"""<p>包特征过滤规则列表。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.PacketFilterRules`
        """
        return self._PacketFilterRules

    @PacketFilterRules.setter
    def PacketFilterRules(self, PacketFilterRules):
        self._PacketFilterRules = PacketFilterRules

    @property
    def GeoBlocking(self):
        r"""<p>区域封禁配置。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.GeoBlockingConfig`
        """
        return self._GeoBlocking

    @GeoBlocking.setter
    def GeoBlocking(self, GeoBlocking):
        self._GeoBlocking = GeoBlocking

    @property
    def ProtocolBlocking(self):
        r"""<p>协议封禁配置。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.ProtocolBlockingConfig`
        """
        return self._ProtocolBlocking

    @ProtocolBlocking.setter
    def ProtocolBlocking(self, ProtocolBlocking):
        self._ProtocolBlocking = ProtocolBlocking

    @property
    def ConnectionProtection(self):
        r"""<p>连接类攻击防护配置。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.ConnectionProtectionConfig`
        """
        return self._ConnectionProtection

    @ConnectionProtection.setter
    def ConnectionProtection(self, ConnectionProtection):
        self._ConnectionProtection = ConnectionProtection

    @property
    def TrafficSignature(self):
        r"""<p>流量签名配置。</p>
        :rtype: :class:`tencentcloud.antiddos.v20250903.models.TrafficSignatureConfig`
        """
        return self._TrafficSignature

    @TrafficSignature.setter
    def TrafficSignature(self, TrafficSignature):
        self._TrafficSignature = TrafficSignature


    def _deserialize(self, params):
        if params.get("DefaultProtection") is not None:
            self._DefaultProtection = DefaultProtectionConfig()
            self._DefaultProtection._deserialize(params.get("DefaultProtection"))
        if params.get("IPACLRules") is not None:
            self._IPACLRules = IPACLRules()
            self._IPACLRules._deserialize(params.get("IPACLRules"))
        if params.get("PortACLRules") is not None:
            self._PortACLRules = PortACLRules()
            self._PortACLRules._deserialize(params.get("PortACLRules"))
        if params.get("SpeedLimitRules") is not None:
            self._SpeedLimitRules = SpeedLimitRules()
            self._SpeedLimitRules._deserialize(params.get("SpeedLimitRules"))
        if params.get("PacketFilterRules") is not None:
            self._PacketFilterRules = PacketFilterRules()
            self._PacketFilterRules._deserialize(params.get("PacketFilterRules"))
        if params.get("GeoBlocking") is not None:
            self._GeoBlocking = GeoBlockingConfig()
            self._GeoBlocking._deserialize(params.get("GeoBlocking"))
        if params.get("ProtocolBlocking") is not None:
            self._ProtocolBlocking = ProtocolBlockingConfig()
            self._ProtocolBlocking._deserialize(params.get("ProtocolBlocking"))
        if params.get("ConnectionProtection") is not None:
            self._ConnectionProtection = ConnectionProtectionConfig()
            self._ConnectionProtection._deserialize(params.get("ConnectionProtection"))
        if params.get("TrafficSignature") is not None:
            self._TrafficSignature = TrafficSignatureConfig()
            self._TrafficSignature._deserialize(params.get("TrafficSignature"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolBlockingConfig(AbstractModel):
    r"""协议封禁配置。

    """

    def __init__(self):
        r"""
        :param _TCPProtocol: <p>TCP 协议封禁。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :type TCPProtocol: str
        :param _UDPProtocol: <p>UDP 协议封禁。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :type UDPProtocol: str
        :param _ICMPProtocol: <p>ICMP 协议封禁。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :type ICMPProtocol: str
        :param _OtherProtocol: <p>其它协议封禁（除 TCP/UDP/ICMP 外的协议）。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :type OtherProtocol: str
        """
        self._TCPProtocol = None
        self._UDPProtocol = None
        self._ICMPProtocol = None
        self._OtherProtocol = None

    @property
    def TCPProtocol(self):
        r"""<p>TCP 协议封禁。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :rtype: str
        """
        return self._TCPProtocol

    @TCPProtocol.setter
    def TCPProtocol(self, TCPProtocol):
        self._TCPProtocol = TCPProtocol

    @property
    def UDPProtocol(self):
        r"""<p>UDP 协议封禁。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :rtype: str
        """
        return self._UDPProtocol

    @UDPProtocol.setter
    def UDPProtocol(self, UDPProtocol):
        self._UDPProtocol = UDPProtocol

    @property
    def ICMPProtocol(self):
        r"""<p>ICMP 协议封禁。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :rtype: str
        """
        return self._ICMPProtocol

    @ICMPProtocol.setter
    def ICMPProtocol(self, ICMPProtocol):
        self._ICMPProtocol = ICMPProtocol

    @property
    def OtherProtocol(self):
        r"""<p>其它协议封禁（除 TCP/UDP/ICMP 外的协议）。</p><p>枚举值：</p><ul><li>on： 开启</li><li>off： 关闭</li></ul>
        :rtype: str
        """
        return self._OtherProtocol

    @OtherProtocol.setter
    def OtherProtocol(self, OtherProtocol):
        self._OtherProtocol = OtherProtocol


    def _deserialize(self, params):
        self._TCPProtocol = params.get("TCPProtocol")
        self._UDPProtocol = params.get("UDPProtocol")
        self._ICMPProtocol = params.get("ICMPProtocol")
        self._OtherProtocol = params.get("OtherProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceInfo(AbstractModel):
    r"""防护资源的详细信息。

    """

    def __init__(self):
        r"""
        :param _Resource: <p>防护资源的资源六段式标识。</p>
        :type Resource: str
        :param _ResourceType: <p>防护资源类型。</p><p>枚举值：</p><ul><li>cvm： 云服务器</li><li>lighthouse： 轻量应用服务器</li><li>clb： 负载均衡</li><li>eip： 弹性公网 IP</li><li>waf： Web 应用防火墙</li><li>teo_l7_domain： EdgeOne 域名</li><li>teo_l4_proxy： EdgeOne 四层代理</li></ul>
        :type ResourceType: str
        :param _Status: <p>防护资源的防护状态。</p><p>枚举值：</p><ul><li>protecting： 防护中</li><li>processing： 防护变更中</li><li>disabling： 防护停用中</li><li>disabled： 防护已停用</li><li>process_failed： 防护变更失败</li><li>disabled_failed： 防护停用失败</li></ul>
        :type Status: str
        :param _Region: <p>防护资源所属地域，例如 <code>ap-beijing</code>。</p><p>资源类型为 EdgeOne 时，Region 取以下枚举值：</p><ul><li>global：全球可用区。</li><li>mainland：中国大陆可用区。</li><li>overseas：全球可用区（中国大陆除外）。</li></ul>
        :type Region: str
        :param _PublicAddresses: <p>公网访问地址。</p><ul><li>资源类型是以公网 IP 提供接入的云资产时，返回对应的公网 IP。</li><li>资源类型是以域名提供接入的云资产时，返回对应域名，例如 <a href="https://cloud.tencent.com/document/product/214/86948">域名化负载均衡实例</a>。</li><li>资源类型为 EdgeOne 四层代理或七层域名时，不返回该字段。</li></ul>
        :type PublicAddresses: list of str
        """
        self._Resource = None
        self._ResourceType = None
        self._Status = None
        self._Region = None
        self._PublicAddresses = None

    @property
    def Resource(self):
        r"""<p>防护资源的资源六段式标识。</p>
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ResourceType(self):
        r"""<p>防护资源类型。</p><p>枚举值：</p><ul><li>cvm： 云服务器</li><li>lighthouse： 轻量应用服务器</li><li>clb： 负载均衡</li><li>eip： 弹性公网 IP</li><li>waf： Web 应用防火墙</li><li>teo_l7_domain： EdgeOne 域名</li><li>teo_l4_proxy： EdgeOne 四层代理</li></ul>
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        r"""<p>防护资源的防护状态。</p><p>枚举值：</p><ul><li>protecting： 防护中</li><li>processing： 防护变更中</li><li>disabling： 防护停用中</li><li>disabled： 防护已停用</li><li>process_failed： 防护变更失败</li><li>disabled_failed： 防护停用失败</li></ul>
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Region(self):
        r"""<p>防护资源所属地域，例如 <code>ap-beijing</code>。</p><p>资源类型为 EdgeOne 时，Region 取以下枚举值：</p><ul><li>global：全球可用区。</li><li>mainland：中国大陆可用区。</li><li>overseas：全球可用区（中国大陆除外）。</li></ul>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def PublicAddresses(self):
        r"""<p>公网访问地址。</p><ul><li>资源类型是以公网 IP 提供接入的云资产时，返回对应的公网 IP。</li><li>资源类型是以域名提供接入的云资产时，返回对应域名，例如 <a href="https://cloud.tencent.com/document/product/214/86948">域名化负载均衡实例</a>。</li><li>资源类型为 EdgeOne 四层代理或七层域名时，不返回该字段。</li></ul>
        :rtype: list of str
        """
        return self._PublicAddresses

    @PublicAddresses.setter
    def PublicAddresses(self, PublicAddresses):
        self._PublicAddresses = PublicAddresses


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        self._Region = params.get("Region")
        self._PublicAddresses = params.get("PublicAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceProtection(AbstractModel):
    r"""防护资源及其绑定的防护实例。

    """

    def __init__(self):
        r"""
        :param _Resource: <p>防护资源的资源六段式标识。</p>
        :type Resource: str
        :param _ProtectionId: <p>该资源绑定的防护实例 ID。</p>
        :type ProtectionId: str
        """
        self._Resource = None
        self._ProtectionId = None

    @property
    def Resource(self):
        r"""<p>防护资源的资源六段式标识。</p>
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ProtectionId(self):
        r"""<p>该资源绑定的防护实例 ID。</p>
        :rtype: str
        """
        return self._ProtectionId

    @ProtectionId.setter
    def ProtectionId(self, ProtectionId):
        self._ProtectionId = ProtectionId


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._ProtectionId = params.get("ProtectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SizeRange(AbstractModel):
    r"""数值范围。

    """

    def __init__(self):
        r"""
        :param _Min: <p>最小值。</p><p>与 <code>Max</code> 相等时表示单个值。</p>
        :type Min: int
        :param _Max: <p>最大值。</p>
        :type Max: int
        """
        self._Min = None
        self._Max = None

    @property
    def Min(self):
        r"""<p>最小值。</p><p>与 <code>Max</code> 相等时表示单个值。</p>
        :rtype: int
        """
        return self._Min

    @Min.setter
    def Min(self, Min):
        self._Min = Min

    @property
    def Max(self):
        r"""<p>最大值。</p>
        :rtype: int
        """
        return self._Max

    @Max.setter
    def Max(self, Max):
        self._Max = Max


    def _deserialize(self, params):
        self._Min = params.get("Min")
        self._Max = params.get("Max")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedLimitRule(AbstractModel):
    r"""端口限速规则。

    """

    def __init__(self):
        r"""
        :param _IPProtocolNumbers: <p>IP 协议号。取值参考 <a href="https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers">IP 协议号列表</a> 。</p><p>参数格式：0-255 范围的数字。支持单个 IP 协议号和 IP 协议号范围。</p><p><code>0-255</code> 表示全部协议。</p>
        :type IPProtocolNumbers: list of str
        :param _DestinationPortRanges: <p>目的端口范围列表。</p>
        :type DestinationPortRanges: list of PortRange
        :param _Mode: <p>限速统计维度。</p><p>枚举值：</p><ul><li>destination_ip： 按目的 IP 维度统计。</li><li>source_destination_ip： 按源 IP + 目的 IP 维度统计。</li></ul>
        :type Mode: str
        :param _BandwidthLimit: <p>流量带宽限制。</p><p>取值范围：[0, 4294967295]</p><p>单位：bps</p><p>为 0 时表示不限制。BandwidthLimit 和 PacketRateLimit 至少需要设置一个大于 0 的值。</p>
        :type BandwidthLimit: int
        :param _PacketRateLimit: <p>包速率限制。</p><p>取值范围：[0, 4294967295]</p><p>单位：pps</p><p>为 0 时表示不限制。BandwidthLimit 和 PacketRateLimit 至少需要设置一个大于 0 的值。</p>
        :type PacketRateLimit: int
        """
        self._IPProtocolNumbers = None
        self._DestinationPortRanges = None
        self._Mode = None
        self._BandwidthLimit = None
        self._PacketRateLimit = None

    @property
    def IPProtocolNumbers(self):
        r"""<p>IP 协议号。取值参考 <a href="https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers">IP 协议号列表</a> 。</p><p>参数格式：0-255 范围的数字。支持单个 IP 协议号和 IP 协议号范围。</p><p><code>0-255</code> 表示全部协议。</p>
        :rtype: list of str
        """
        return self._IPProtocolNumbers

    @IPProtocolNumbers.setter
    def IPProtocolNumbers(self, IPProtocolNumbers):
        self._IPProtocolNumbers = IPProtocolNumbers

    @property
    def DestinationPortRanges(self):
        r"""<p>目的端口范围列表。</p>
        :rtype: list of PortRange
        """
        return self._DestinationPortRanges

    @DestinationPortRanges.setter
    def DestinationPortRanges(self, DestinationPortRanges):
        self._DestinationPortRanges = DestinationPortRanges

    @property
    def Mode(self):
        r"""<p>限速统计维度。</p><p>枚举值：</p><ul><li>destination_ip： 按目的 IP 维度统计。</li><li>source_destination_ip： 按源 IP + 目的 IP 维度统计。</li></ul>
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def BandwidthLimit(self):
        r"""<p>流量带宽限制。</p><p>取值范围：[0, 4294967295]</p><p>单位：bps</p><p>为 0 时表示不限制。BandwidthLimit 和 PacketRateLimit 至少需要设置一个大于 0 的值。</p>
        :rtype: int
        """
        return self._BandwidthLimit

    @BandwidthLimit.setter
    def BandwidthLimit(self, BandwidthLimit):
        self._BandwidthLimit = BandwidthLimit

    @property
    def PacketRateLimit(self):
        r"""<p>包速率限制。</p><p>取值范围：[0, 4294967295]</p><p>单位：pps</p><p>为 0 时表示不限制。BandwidthLimit 和 PacketRateLimit 至少需要设置一个大于 0 的值。</p>
        :rtype: int
        """
        return self._PacketRateLimit

    @PacketRateLimit.setter
    def PacketRateLimit(self, PacketRateLimit):
        self._PacketRateLimit = PacketRateLimit


    def _deserialize(self, params):
        self._IPProtocolNumbers = params.get("IPProtocolNumbers")
        if params.get("DestinationPortRanges") is not None:
            self._DestinationPortRanges = []
            for item in params.get("DestinationPortRanges"):
                obj = PortRange()
                obj._deserialize(item)
                self._DestinationPortRanges.append(obj)
        self._Mode = params.get("Mode")
        self._BandwidthLimit = params.get("BandwidthLimit")
        self._PacketRateLimit = params.get("PacketRateLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedLimitRules(AbstractModel):
    r"""端口限速规则列表。

    """

    def __init__(self):
        r"""
        :param _Rules: <p>端口限速规则列表。</p>
        :type Rules: list of SpeedLimitRule
        """
        self._Rules = None

    @property
    def Rules(self):
        r"""<p>端口限速规则列表。</p>
        :rtype: list of SpeedLimitRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = SpeedLimitRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    r"""标签配置。

    """

    def __init__(self):
        r"""
        :param _TagKey: <p>标签键。</p>
        :type TagKey: str
        :param _TagValue: <p>标签值。</p>
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        r"""<p>标签键。</p>
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        r"""<p>标签值。</p>
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
        


class TrafficSignatureConfig(AbstractModel):
    r"""流量签名校验配置。

    """

    def __init__(self):
        r"""
        :param _Switch: <p>流量签名配置开关。</p>
        :type Switch: str
        :param _TrafficSignatureKeys: <p>流量签名密钥。</p>
        :type TrafficSignatureKeys: list of str
        :param _UdpCheckPortRanges: <p>UDP 协议校验的端口范围，支持输入多个端口或端口范围。</p>
        :type UdpCheckPortRanges: list of PortRange
        :param _TcpCheckPortRanges: <p>TCP 协议校验的端口范围，支持输入多个端口或端口范围。</p>
        :type TcpCheckPortRanges: list of PortRange
        :param _UdpTrafficSignatureOffset: <p>UDP 协议下签名在数据包负载中的起始偏移位置，支持 0 至 100 字节偏移量。默认为0。</p>
        :type UdpTrafficSignatureOffset: int
        :param _TcpTrafficSignatureOffset: <p>TCP 协议下签名在数据包负载中的起始偏移位置，支持 0 至 100 字节偏移量。默认为0</p>
        :type TcpTrafficSignatureOffset: int
        """
        self._Switch = None
        self._TrafficSignatureKeys = None
        self._UdpCheckPortRanges = None
        self._TcpCheckPortRanges = None
        self._UdpTrafficSignatureOffset = None
        self._TcpTrafficSignatureOffset = None

    @property
    def Switch(self):
        r"""<p>流量签名配置开关。</p>
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def TrafficSignatureKeys(self):
        r"""<p>流量签名密钥。</p>
        :rtype: list of str
        """
        return self._TrafficSignatureKeys

    @TrafficSignatureKeys.setter
    def TrafficSignatureKeys(self, TrafficSignatureKeys):
        self._TrafficSignatureKeys = TrafficSignatureKeys

    @property
    def UdpCheckPortRanges(self):
        r"""<p>UDP 协议校验的端口范围，支持输入多个端口或端口范围。</p>
        :rtype: list of PortRange
        """
        return self._UdpCheckPortRanges

    @UdpCheckPortRanges.setter
    def UdpCheckPortRanges(self, UdpCheckPortRanges):
        self._UdpCheckPortRanges = UdpCheckPortRanges

    @property
    def TcpCheckPortRanges(self):
        r"""<p>TCP 协议校验的端口范围，支持输入多个端口或端口范围。</p>
        :rtype: list of PortRange
        """
        return self._TcpCheckPortRanges

    @TcpCheckPortRanges.setter
    def TcpCheckPortRanges(self, TcpCheckPortRanges):
        self._TcpCheckPortRanges = TcpCheckPortRanges

    @property
    def UdpTrafficSignatureOffset(self):
        r"""<p>UDP 协议下签名在数据包负载中的起始偏移位置，支持 0 至 100 字节偏移量。默认为0。</p>
        :rtype: int
        """
        return self._UdpTrafficSignatureOffset

    @UdpTrafficSignatureOffset.setter
    def UdpTrafficSignatureOffset(self, UdpTrafficSignatureOffset):
        self._UdpTrafficSignatureOffset = UdpTrafficSignatureOffset

    @property
    def TcpTrafficSignatureOffset(self):
        r"""<p>TCP 协议下签名在数据包负载中的起始偏移位置，支持 0 至 100 字节偏移量。默认为0</p>
        :rtype: int
        """
        return self._TcpTrafficSignatureOffset

    @TcpTrafficSignatureOffset.setter
    def TcpTrafficSignatureOffset(self, TcpTrafficSignatureOffset):
        self._TcpTrafficSignatureOffset = TcpTrafficSignatureOffset


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._TrafficSignatureKeys = params.get("TrafficSignatureKeys")
        if params.get("UdpCheckPortRanges") is not None:
            self._UdpCheckPortRanges = []
            for item in params.get("UdpCheckPortRanges"):
                obj = PortRange()
                obj._deserialize(item)
                self._UdpCheckPortRanges.append(obj)
        if params.get("TcpCheckPortRanges") is not None:
            self._TcpCheckPortRanges = []
            for item in params.get("TcpCheckPortRanges"):
                obj = PortRange()
                obj._deserialize(item)
                self._TcpCheckPortRanges.append(obj)
        self._UdpTrafficSignatureOffset = params.get("UdpTrafficSignatureOffset")
        self._TcpTrafficSignatureOffset = params.get("TcpTrafficSignatureOffset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnblockResourcesRequest(AbstractModel):
    r"""UnblockResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Resources: <p>申请解封的资源列表。支持按照公网 IP 解封；可通过 DescribeDDoSBlockRecords 接口获取被封堵的资源详情。参数示例如下：</p><ul><li>公网 IP：117.175.94.230。</li></ul><p>入参限制：列表长度最大限制 10。</p>
        :type Resources: list of str
        """
        self._Resources = None

    @property
    def Resources(self):
        r"""<p>申请解封的资源列表。支持按照公网 IP 解封；可通过 DescribeDDoSBlockRecords 接口获取被封堵的资源详情。参数示例如下：</p><ul><li>公网 IP：117.175.94.230。</li></ul><p>入参限制：列表长度最大限制 10。</p>
        :rtype: list of str
        """
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        self._Resources = params.get("Resources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnblockResourcesResponse(AbstractModel):
    r"""UnblockResources返回参数结构体

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