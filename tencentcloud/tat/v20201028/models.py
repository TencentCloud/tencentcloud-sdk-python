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


class AutomationAgentInfo(AbstractModel):
    """自动化助手客户端信息

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _Version: Agent 版本号。
        :type Version: str
        :param _LastHeartbeatTime: 上次心跳时间
        :type LastHeartbeatTime: str
        :param _AgentStatus: Agent状态，取值范围：
Online：在线，Offline：离线

        :type AgentStatus: str
        :param _Environment: Agent运行环境，取值范围：Linux：Linux实例Windows：Windows实例
        :type Environment: str
        :param _SupportFeatures: Agent 支持的功能列表。
        :type SupportFeatures: list of str
        """
        self._InstanceId = None
        self._Version = None
        self._LastHeartbeatTime = None
        self._AgentStatus = None
        self._Environment = None
        self._SupportFeatures = None

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Version(self):
        """Agent 版本号。
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def LastHeartbeatTime(self):
        """上次心跳时间
        :rtype: str
        """
        return self._LastHeartbeatTime

    @LastHeartbeatTime.setter
    def LastHeartbeatTime(self, LastHeartbeatTime):
        self._LastHeartbeatTime = LastHeartbeatTime

    @property
    def AgentStatus(self):
        """Agent状态，取值范围：
Online：在线，Offline：离线

        :rtype: str
        """
        return self._AgentStatus

    @AgentStatus.setter
    def AgentStatus(self, AgentStatus):
        self._AgentStatus = AgentStatus

    @property
    def Environment(self):
        """Agent运行环境，取值范围：Linux：Linux实例Windows：Windows实例
        :rtype: str
        """
        return self._Environment

    @Environment.setter
    def Environment(self, Environment):
        self._Environment = Environment

    @property
    def SupportFeatures(self):
        """Agent 支持的功能列表。
        :rtype: list of str
        """
        return self._SupportFeatures

    @SupportFeatures.setter
    def SupportFeatures(self, SupportFeatures):
        self._SupportFeatures = SupportFeatures


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Version = params.get("Version")
        self._LastHeartbeatTime = params.get("LastHeartbeatTime")
        self._AgentStatus = params.get("AgentStatus")
        self._Environment = params.get("Environment")
        self._SupportFeatures = params.get("SupportFeatures")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInvocationRequest(AbstractModel):
    """CancelInvocation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvocationId: 执行活动ID。

可通过 [DescribeInvocations(查询执行活动)](https://cloud.tencent.com/document/api/1340/52679) 接口获取。
        :type InvocationId: str
        :param _InstanceIds: 实例ID列表，上限100。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：
- CVM
- Lighthouse
- TAT 托管实例
        :type InstanceIds: list of str
        """
        self._InvocationId = None
        self._InstanceIds = None

    @property
    def InvocationId(self):
        """执行活动ID。

可通过 [DescribeInvocations(查询执行活动)](https://cloud.tencent.com/document/api/1340/52679) 接口获取。
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InstanceIds(self):
        """实例ID列表，上限100。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：
- CVM
- Lighthouse
- TAT 托管实例
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds


    def _deserialize(self, params):
        self._InvocationId = params.get("InvocationId")
        self._InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelInvocationResponse(AbstractModel):
    """CancelInvocation返回参数结构体

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


class Command(AbstractModel):
    """命令详情。

    """

    def __init__(self):
        r"""
        :param _CommandId: 命令ID。
        :type CommandId: str
        :param _CommandName: 命令名称。
        :type CommandName: str
        :param _Description: 命令描述。
        :type Description: str
        :param _Content: Base64编码后的命令内容。
        :type Content: str
        :param _CommandType: 命令类型。取值为 SHELL、POWERSHELL、BAT 之一。
        :type CommandType: str
        :param _WorkingDirectory: 命令执行路径。
        :type WorkingDirectory: str
        :param _Timeout: 命令超时时间。
        :type Timeout: int
        :param _CreatedTime: 命令创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type CreatedTime: str
        :param _UpdatedTime: 命令更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type UpdatedTime: str
        :param _EnableParameter: 是否启用自定义参数功能。
        :type EnableParameter: bool
        :param _DefaultParameters: 自定义参数的默认取值。
        :type DefaultParameters: str
        :param _DefaultParameterConfs: 自定义参数的默认取值。
        :type DefaultParameterConfs: list of DefaultParameterConf
        :param _Scenes: 命令关联的场景
        :type Scenes: list of str
        :param _FormattedDescription: 命令的结构化描述。公共命令有值，用户命令为空字符串。
        :type FormattedDescription: str
        :param _CreatedBy: 命令创建者。TAT 代表公共命令，USER 代表个人命令。
        :type CreatedBy: str
        :param _Tags: 命令关联的标签列表。
        :type Tags: list of Tag
        :param _Username: 在实例上执行命令的用户名。
        :type Username: str
        :param _OutputCOSBucketUrl: 日志上传的cos bucket 地址。
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: 日志在cos bucket中的目录。
        :type OutputCOSKeyPrefix: str
        """
        self._CommandId = None
        self._CommandName = None
        self._Description = None
        self._Content = None
        self._CommandType = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._EnableParameter = None
        self._DefaultParameters = None
        self._DefaultParameterConfs = None
        self._Scenes = None
        self._FormattedDescription = None
        self._CreatedBy = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandId(self):
        """命令ID。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def CommandName(self):
        """命令名称。
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        """命令描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        """Base64编码后的命令内容。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        """命令类型。取值为 SHELL、POWERSHELL、BAT 之一。
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        """命令执行路径。
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """命令超时时间。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def CreatedTime(self):
        """命令创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """命令更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def EnableParameter(self):
        """是否启用自定义参数功能。
        :rtype: bool
        """
        return self._EnableParameter

    @EnableParameter.setter
    def EnableParameter(self, EnableParameter):
        self._EnableParameter = EnableParameter

    @property
    def DefaultParameters(self):
        """自定义参数的默认取值。
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def DefaultParameterConfs(self):
        """自定义参数的默认取值。
        :rtype: list of DefaultParameterConf
        """
        return self._DefaultParameterConfs

    @DefaultParameterConfs.setter
    def DefaultParameterConfs(self, DefaultParameterConfs):
        self._DefaultParameterConfs = DefaultParameterConfs

    @property
    def Scenes(self):
        """命令关联的场景
        :rtype: list of str
        """
        return self._Scenes

    @Scenes.setter
    def Scenes(self, Scenes):
        self._Scenes = Scenes

    @property
    def FormattedDescription(self):
        """命令的结构化描述。公共命令有值，用户命令为空字符串。
        :rtype: str
        """
        return self._FormattedDescription

    @FormattedDescription.setter
    def FormattedDescription(self, FormattedDescription):
        self._FormattedDescription = FormattedDescription

    @property
    def CreatedBy(self):
        """命令创建者。TAT 代表公共命令，USER 代表个人命令。
        :rtype: str
        """
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def Tags(self):
        """命令关联的标签列表。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        """在实例上执行命令的用户名。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """日志上传的cos bucket 地址。
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """日志在cos bucket中的目录。
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        self._CommandName = params.get("CommandName")
        self._Description = params.get("Description")
        self._Content = params.get("Content")
        self._CommandType = params.get("CommandType")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._EnableParameter = params.get("EnableParameter")
        self._DefaultParameters = params.get("DefaultParameters")
        if params.get("DefaultParameterConfs") is not None:
            self._DefaultParameterConfs = []
            for item in params.get("DefaultParameterConfs"):
                obj = DefaultParameterConf()
                obj._deserialize(item)
                self._DefaultParameterConfs.append(obj)
        self._Scenes = params.get("Scenes")
        self._FormattedDescription = params.get("FormattedDescription")
        self._CreatedBy = params.get("CreatedBy")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommandDocument(AbstractModel):
    """命令执行详情。

    """

    def __init__(self):
        r"""
        :param _Content: Base64 编码后的执行命令。
        :type Content: str
        :param _CommandType: 命令类型。取值为 SHELL、POWERSHELL、BAT 之一。
        :type CommandType: str
        :param _Timeout: 超时时间。单位：秒。
        :type Timeout: int
        :param _WorkingDirectory: 执行路径。
        :type WorkingDirectory: str
        :param _Username: 执行用户。
        :type Username: str
        :param _OutputCOSBucketUrl: 保存输出的 COS Bucket 链接。
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: 保存输出的文件名称前缀。
        :type OutputCOSKeyPrefix: str
        """
        self._Content = None
        self._CommandType = None
        self._Timeout = None
        self._WorkingDirectory = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def Content(self):
        """Base64 编码后的执行命令。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        """命令类型。取值为 SHELL、POWERSHELL、BAT 之一。
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def Timeout(self):
        """超时时间。单位：秒。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def WorkingDirectory(self):
        """执行路径。
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Username(self):
        """执行用户。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """保存输出的 COS Bucket 链接。
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """保存输出的文件名称前缀。
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._CommandType = params.get("CommandType")
        self._Timeout = params.get("Timeout")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandRequest(AbstractModel):
    """CreateCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type CommandName: str
        :param _Content: Base64编码后的命令内容，长度不可超过64KB。
        :type Content: str
        :param _Description: 命令描述。不超过120字符。
        :type Description: str
        :param _CommandType: 命令类型，目前支持取值：SHELL、POWERSHELL、BAT。默认：SHELL。
        :type CommandType: str
        :param _WorkingDirectory: 命令执行路径，对于 SHELL 命令默认为 /root，对于 POWERSHELL 命令默认为 C:\Program Files\qcloud\tat_agent\workdir。
        :type WorkingDirectory: str
        :param _Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。
        :type Timeout: int
        :param _EnableParameter: 是否启用自定义参数功能。
一旦创建，此值不提供修改。
默认值：false。
        :type EnableParameter: bool
        :param _DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果InvokeCommand时未提供参数取值，将使用这里的默认值进行替换。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
仅在 EnableParameter 参数为 true 时，才允许设置此参数。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type DefaultParameters: str
        :param _DefaultParameterConfs: 自定义参数数组。
如果InvokeCommand时未提供参数取值，将使用这里的默认值进行替换。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
仅在 EnableParameter 参数为 true 时，才允许设置此参数。
自定义参数最多20个。
        :type DefaultParameterConfs: list of DefaultParameterConf
        :param _Tags: 为命令关联的标签，列表长度不超过10。
        :type Tags: list of Tag
        :param _Username: 在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。默认情况下，在 Linux 实例中以 root 用户执行命令；在Windows 实例中以 System 用户执行命令。
        :type Username: str
        :param _OutputCOSBucketUrl: 指定日志上传的cos bucket 地址，必须以https开头，如 https://BucketName-123454321.cos.ap-beijing.myqcloud.com。
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: 指定日志在cos bucket中的目录，目录命名有如下规则：
1. 可用数字、中英文和可见字符的组合，长度最多为60。
2. 用 / 分割路径，可快速创建子目录。
3. 不允许连续 / ；不允许以 / 开头；不允许以..作为文件夹名称
        :type OutputCOSKeyPrefix: str
        """
        self._CommandName = None
        self._Content = None
        self._Description = None
        self._CommandType = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._EnableParameter = None
        self._DefaultParameters = None
        self._DefaultParameterConfs = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandName(self):
        """命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Content(self):
        """Base64编码后的命令内容，长度不可超过64KB。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Description(self):
        """命令描述。不超过120字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CommandType(self):
        """命令类型，目前支持取值：SHELL、POWERSHELL、BAT。默认：SHELL。
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        """命令执行路径，对于 SHELL 命令默认为 /root，对于 POWERSHELL 命令默认为 C:\Program Files\qcloud\tat_agent\workdir。
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """命令超时时间，默认60秒。取值范围[1, 86400]。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def EnableParameter(self):
        """是否启用自定义参数功能。
一旦创建，此值不提供修改。
默认值：false。
        :rtype: bool
        """
        return self._EnableParameter

    @EnableParameter.setter
    def EnableParameter(self, EnableParameter):
        self._EnableParameter = EnableParameter

    @property
    def DefaultParameters(self):
        """启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
如果InvokeCommand时未提供参数取值，将使用这里的默认值进行替换。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
仅在 EnableParameter 参数为 true 时，才允许设置此参数。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def DefaultParameterConfs(self):
        """自定义参数数组。
如果InvokeCommand时未提供参数取值，将使用这里的默认值进行替换。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
仅在 EnableParameter 参数为 true 时，才允许设置此参数。
自定义参数最多20个。
        :rtype: list of DefaultParameterConf
        """
        return self._DefaultParameterConfs

    @DefaultParameterConfs.setter
    def DefaultParameterConfs(self, DefaultParameterConfs):
        self._DefaultParameterConfs = DefaultParameterConfs

    @property
    def Tags(self):
        """为命令关联的标签，列表长度不超过10。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        """在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。默认情况下，在 Linux 实例中以 root 用户执行命令；在Windows 实例中以 System 用户执行命令。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """指定日志上传的cos bucket 地址，必须以https开头，如 https://BucketName-123454321.cos.ap-beijing.myqcloud.com。
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """指定日志在cos bucket中的目录，目录命名有如下规则：
1. 可用数字、中英文和可见字符的组合，长度最多为60。
2. 用 / 分割路径，可快速创建子目录。
3. 不允许连续 / ；不允许以 / 开头；不允许以..作为文件夹名称
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._CommandName = params.get("CommandName")
        self._Content = params.get("Content")
        self._Description = params.get("Description")
        self._CommandType = params.get("CommandType")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._EnableParameter = params.get("EnableParameter")
        self._DefaultParameters = params.get("DefaultParameters")
        if params.get("DefaultParameterConfs") is not None:
            self._DefaultParameterConfs = []
            for item in params.get("DefaultParameterConfs"):
                obj = DefaultParameterConf()
                obj._deserialize(item)
                self._DefaultParameterConfs.append(obj)
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCommandResponse(AbstractModel):
    """CreateCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandId: 命令ID。
        :type CommandId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CommandId = None
        self._RequestId = None

    @property
    def CommandId(self):
        """命令ID。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

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
        self._CommandId = params.get("CommandId")
        self._RequestId = params.get("RequestId")


class CreateInvokerRequest(AbstractModel):
    """CreateInvoker请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 执行器名称。
        :type Name: str
        :param _Type: 执行器类型，当前仅支持周期类型执行器，取值：`SCHEDULE` 。
        :type Type: str
        :param _CommandId: 远程命令ID。

可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :type CommandId: str
        :param _InstanceIds: 触发器关联的实例ID。列表上限 100。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：CVM、Lighthouse、TAT 托管实例。

实例需要安装 TAT 客户端, 且客户端为 Online 状态。可通过 [DescribeAutomationAgentStatus(查询客户端状态)](https://cloud.tencent.com/document/api/1340/52682) 接口查询客户端状态。
        :type InstanceIds: list of str
        :param _Username: 命令执行用户。
        :type Username: str
        :param _Parameters: 命令自定义参数。

仅在 CommandId 所指命令的 EnableParameter 为 true 时，才允许设置此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
        :type Parameters: str
        :param _ScheduleSettings: 周期执行器设置。当创建周期执行器时，必须指定此参数。
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        self._Name = None
        self._Type = None
        self._CommandId = None
        self._InstanceIds = None
        self._Username = None
        self._Parameters = None
        self._ScheduleSettings = None

    @property
    def Name(self):
        """执行器名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """执行器类型，当前仅支持周期类型执行器，取值：`SCHEDULE` 。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        """远程命令ID。

可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InstanceIds(self):
        """触发器关联的实例ID。列表上限 100。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：CVM、Lighthouse、TAT 托管实例。

实例需要安装 TAT 客户端, 且客户端为 Online 状态。可通过 [DescribeAutomationAgentStatus(查询客户端状态)](https://cloud.tencent.com/document/api/1340/52682) 接口查询客户端状态。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Username(self):
        """命令执行用户。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        """命令自定义参数。

仅在 CommandId 所指命令的 EnableParameter 为 true 时，才允许设置此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def ScheduleSettings(self):
        """周期执行器设置。当创建周期执行器时，必须指定此参数。
        :rtype: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        return self._ScheduleSettings

    @ScheduleSettings.setter
    def ScheduleSettings(self, ScheduleSettings):
        self._ScheduleSettings = ScheduleSettings


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CommandId = params.get("CommandId")
        self._InstanceIds = params.get("InstanceIds")
        self._Username = params.get("Username")
        self._Parameters = params.get("Parameters")
        if params.get("ScheduleSettings") is not None:
            self._ScheduleSettings = ScheduleSettings()
            self._ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateInvokerResponse(AbstractModel):
    """CreateInvoker返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokerId: 执行器ID。
        :type InvokerId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvokerId = None
        self._RequestId = None

    @property
    def InvokerId(self):
        """执行器ID。
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

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
        self._InvokerId = params.get("InvokerId")
        self._RequestId = params.get("RequestId")


class CreateRegisterCodeRequest(AbstractModel):
    """CreateRegisterCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Description: 注册码描述。最大长度为 128 字符。
        :type Description: str
        :param _InstanceNamePrefix: 注册实例名称前缀。最大长度为 32 字符。
        :type InstanceNamePrefix: str
        :param _RegisterLimit: 该注册码允许注册的实例数目。默认值为 10，最小值为 1，最大值为 10000。
        :type RegisterLimit: int
        :param _EffectiveTime: 该注册码的有效时间，单位为小时。默认值为 4。

- 若传入值小于等于 99999，则以小时为单位设置有效时间。
- 若传入值大于 99999，则设置为长期有效。
        :type EffectiveTime: int
        :param _IpAddressRange: 限制注册码只能从 IpAddressRange 所描述公网出口进行注册。

默认为空，即无任何限制。

取值应为标准 IPv4 或 CIDRv4 格式。例如 192.168.1.1 或 192.168.0.0/16。
        :type IpAddressRange: str
        """
        self._Description = None
        self._InstanceNamePrefix = None
        self._RegisterLimit = None
        self._EffectiveTime = None
        self._IpAddressRange = None

    @property
    def Description(self):
        """注册码描述。最大长度为 128 字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InstanceNamePrefix(self):
        """注册实例名称前缀。最大长度为 32 字符。
        :rtype: str
        """
        return self._InstanceNamePrefix

    @InstanceNamePrefix.setter
    def InstanceNamePrefix(self, InstanceNamePrefix):
        self._InstanceNamePrefix = InstanceNamePrefix

    @property
    def RegisterLimit(self):
        """该注册码允许注册的实例数目。默认值为 10，最小值为 1，最大值为 10000。
        :rtype: int
        """
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def EffectiveTime(self):
        """该注册码的有效时间，单位为小时。默认值为 4。

- 若传入值小于等于 99999，则以小时为单位设置有效时间。
- 若传入值大于 99999，则设置为长期有效。
        :rtype: int
        """
        return self._EffectiveTime

    @EffectiveTime.setter
    def EffectiveTime(self, EffectiveTime):
        self._EffectiveTime = EffectiveTime

    @property
    def IpAddressRange(self):
        """限制注册码只能从 IpAddressRange 所描述公网出口进行注册。

默认为空，即无任何限制。

取值应为标准 IPv4 或 CIDRv4 格式。例如 192.168.1.1 或 192.168.0.0/16。
        :rtype: str
        """
        return self._IpAddressRange

    @IpAddressRange.setter
    def IpAddressRange(self, IpAddressRange):
        self._IpAddressRange = IpAddressRange


    def _deserialize(self, params):
        self._Description = params.get("Description")
        self._InstanceNamePrefix = params.get("InstanceNamePrefix")
        self._RegisterLimit = params.get("RegisterLimit")
        self._EffectiveTime = params.get("EffectiveTime")
        self._IpAddressRange = params.get("IpAddressRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRegisterCodeResponse(AbstractModel):
    """CreateRegisterCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RegisterCodeId: 注册码ID。
        :type RegisterCodeId: str
        :param _RegisterCodeValue: 注册码值。
        :type RegisterCodeValue: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RegisterCodeId = None
        self._RegisterCodeValue = None
        self._RequestId = None

    @property
    def RegisterCodeId(self):
        """注册码ID。
        :rtype: str
        """
        return self._RegisterCodeId

    @RegisterCodeId.setter
    def RegisterCodeId(self, RegisterCodeId):
        self._RegisterCodeId = RegisterCodeId

    @property
    def RegisterCodeValue(self):
        """注册码值。
        :rtype: str
        """
        return self._RegisterCodeValue

    @RegisterCodeValue.setter
    def RegisterCodeValue(self, RegisterCodeValue):
        self._RegisterCodeValue = RegisterCodeValue

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
        self._RegisterCodeId = params.get("RegisterCodeId")
        self._RegisterCodeValue = params.get("RegisterCodeValue")
        self._RequestId = params.get("RequestId")


class DefaultParameterConf(AbstractModel):
    """自定义参数。

    """

    def __init__(self):
        r"""
        :param _ParameterName: 参数名。
        :type ParameterName: str
        :param _ParameterValue: 参数默认值。
        :type ParameterValue: str
        :param _ParameterDescription: 参数描述。
        :type ParameterDescription: str
        """
        self._ParameterName = None
        self._ParameterValue = None
        self._ParameterDescription = None

    @property
    def ParameterName(self):
        """参数名。
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName

    @property
    def ParameterValue(self):
        """参数默认值。
        :rtype: str
        """
        return self._ParameterValue

    @ParameterValue.setter
    def ParameterValue(self, ParameterValue):
        self._ParameterValue = ParameterValue

    @property
    def ParameterDescription(self):
        """参数描述。
        :rtype: str
        """
        return self._ParameterDescription

    @ParameterDescription.setter
    def ParameterDescription(self, ParameterDescription):
        self._ParameterDescription = ParameterDescription


    def _deserialize(self, params):
        self._ParameterName = params.get("ParameterName")
        self._ParameterValue = params.get("ParameterValue")
        self._ParameterDescription = params.get("ParameterDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandRequest(AbstractModel):
    """DeleteCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandId: 待删除的命令 ID。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :type CommandId: str
        """
        self._CommandId = None

    @property
    def CommandId(self):
        """待删除的命令 ID。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandResponse(AbstractModel):
    """DeleteCommand返回参数结构体

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


class DeleteCommandsRequest(AbstractModel):
    """DeleteCommands请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandIds: 待删除的命令 ID。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :type CommandIds: list of str
        """
        self._CommandIds = None

    @property
    def CommandIds(self):
        """待删除的命令 ID。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :rtype: list of str
        """
        return self._CommandIds

    @CommandIds.setter
    def CommandIds(self, CommandIds):
        self._CommandIds = CommandIds


    def _deserialize(self, params):
        self._CommandIds = params.get("CommandIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCommandsResponse(AbstractModel):
    """DeleteCommands返回参数结构体

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


class DeleteInvokerRequest(AbstractModel):
    """DeleteInvoker请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokerId: 待删除的执行器ID。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        """待删除的执行器ID。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteInvokerResponse(AbstractModel):
    """DeleteInvoker返回参数结构体

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


class DeleteRegisterCodesRequest(AbstractModel):
    """DeleteRegisterCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegisterCodeIds: 注册码ID列表。限制输入的注册码ID数量大于0小于100。

可通过 [DescribeRegisterCodes(查询注册码)](https://cloud.tencent.com/document/api/1340/96925) 接口获取。
        :type RegisterCodeIds: list of str
        """
        self._RegisterCodeIds = None

    @property
    def RegisterCodeIds(self):
        """注册码ID列表。限制输入的注册码ID数量大于0小于100。

可通过 [DescribeRegisterCodes(查询注册码)](https://cloud.tencent.com/document/api/1340/96925) 接口获取。
        :rtype: list of str
        """
        return self._RegisterCodeIds

    @RegisterCodeIds.setter
    def RegisterCodeIds(self, RegisterCodeIds):
        self._RegisterCodeIds = RegisterCodeIds


    def _deserialize(self, params):
        self._RegisterCodeIds = params.get("RegisterCodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRegisterCodesResponse(AbstractModel):
    """DeleteRegisterCodes返回参数结构体

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


class DeleteRegisterInstanceRequest(AbstractModel):
    """DeleteRegisterInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 托管实例ID。

可通过 [DescribeRegisterInstances(查询托管实例)](https://cloud.tencent.com/document/api/1340/96924) 接口获取。
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """托管实例ID。

可通过 [DescribeRegisterInstances(查询托管实例)](https://cloud.tencent.com/document/api/1340/96924) 接口获取。
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
        


class DeleteRegisterInstanceResponse(AbstractModel):
    """DeleteRegisterInstance返回参数结构体

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


class DescribeAutomationAgentStatusRequest(AbstractModel):
    """DescribeAutomationAgentStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 待查询的实例ID列表。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：CVM、Lighthouse、TAT 托管实例。

参数不支持同时指定 `InstanceIds ` 和 `Filters ` 。
        :type InstanceIds: list of str
        :param _Filters: - agent-status - String - 是否必填：否 -（过滤条件）按照agent状态过滤，取值：Online 在线，Offline 离线。 
- environment - String - 是否必填：否 -（过滤条件）按照agent运行环境查询，取值：Linux, Windows。
- instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。 可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：CVM、Lighthouse、TAT 托管实例。

参数不支持同时指定 `InstanceIds ` 和 `Filters ` 。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def InstanceIds(self):
        """待查询的实例ID列表。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：CVM、Lighthouse、TAT 托管实例。

参数不支持同时指定 `InstanceIds ` 和 `Filters ` 。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        """- agent-status - String - 是否必填：否 -（过滤条件）按照agent状态过滤，取值：Online 在线，Offline 离线。 
- environment - String - 是否必填：否 -（过滤条件）按照agent运行环境查询，取值：Linux, Windows。
- instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。 可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：CVM、Lighthouse、TAT 托管实例。

参数不支持同时指定 `InstanceIds ` 和 `Filters ` 。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
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
        


class DescribeAutomationAgentStatusResponse(AbstractModel):
    """DescribeAutomationAgentStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AutomationAgentSet: Agent 信息列表。
        :type AutomationAgentSet: list of AutomationAgentInfo
        :param _TotalCount: 符合条件的 Agent 总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AutomationAgentSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def AutomationAgentSet(self):
        """Agent 信息列表。
        :rtype: list of AutomationAgentInfo
        """
        return self._AutomationAgentSet

    @AutomationAgentSet.setter
    def AutomationAgentSet(self, AutomationAgentSet):
        self._AutomationAgentSet = AutomationAgentSet

    @property
    def TotalCount(self):
        """符合条件的 Agent 总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("AutomationAgentSet") is not None:
            self._AutomationAgentSet = []
            for item in params.get("AutomationAgentSet"):
                obj = AutomationAgentInfo()
                obj._deserialize(item)
                self._AutomationAgentSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCommandsRequest(AbstractModel):
    """DescribeCommands请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandIds: 命令ID列表，每次请求的上限为100。参数不支持同时指定 `CommandIds` 和 `Filters` 。
        :type CommandIds: list of str
        :param _Filters: 过滤条件。

- command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。
- command-name - String - 是否必填：否 -（过滤条件）按照命令名称过滤。
- command-type - String - 是否必填：否 -（过滤条件）按照命令类型过滤，取值为 SHELL、POWERSHELL、BAT。
- scene-id - String - 是否必填：否 -（过滤条件）按照场景ID过滤。可通过 [DescribeScenes(查询场景)](https://cloud.tencent.com/document/api/1340/109968) 接口获取场景ID。
- created-by - String - 是否必填：否 -（过滤条件）按照命令创建者过滤，取值为 TAT 或 USER。TAT 代表公共命令，USER 代表由用户创建的命令。
- tag-key - String - 是否必填：否 -（过滤条件）按照标签键进行过滤。
- tag-value - String - 是否必填：否 -（过滤条件）按照标签值进行过滤。
- tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例4

每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `CommandIds` 和 `Filters` 。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._CommandIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def CommandIds(self):
        """命令ID列表，每次请求的上限为100。参数不支持同时指定 `CommandIds` 和 `Filters` 。
        :rtype: list of str
        """
        return self._CommandIds

    @CommandIds.setter
    def CommandIds(self, CommandIds):
        self._CommandIds = CommandIds

    @property
    def Filters(self):
        """过滤条件。

- command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。
- command-name - String - 是否必填：否 -（过滤条件）按照命令名称过滤。
- command-type - String - 是否必填：否 -（过滤条件）按照命令类型过滤，取值为 SHELL、POWERSHELL、BAT。
- scene-id - String - 是否必填：否 -（过滤条件）按照场景ID过滤。可通过 [DescribeScenes(查询场景)](https://cloud.tencent.com/document/api/1340/109968) 接口获取场景ID。
- created-by - String - 是否必填：否 -（过滤条件）按照命令创建者过滤，取值为 TAT 或 USER。TAT 代表公共命令，USER 代表由用户创建的命令。
- tag-key - String - 是否必填：否 -（过滤条件）按照标签键进行过滤。
- tag-value - String - 是否必填：否 -（过滤条件）按照标签值进行过滤。
- tag:tag-key - String - 是否必填：否 -（过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例4

每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `CommandIds` 和 `Filters` 。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._CommandIds = params.get("CommandIds")
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
        


class DescribeCommandsResponse(AbstractModel):
    """DescribeCommands返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的命令总数。
        :type TotalCount: int
        :param _CommandSet: 命令详情列表。
        :type CommandSet: list of Command
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CommandSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的命令总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CommandSet(self):
        """命令详情列表。
        :rtype: list of Command
        """
        return self._CommandSet

    @CommandSet.setter
    def CommandSet(self, CommandSet):
        self._CommandSet = CommandSet

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
        if params.get("CommandSet") is not None:
            self._CommandSet = []
            for item in params.get("CommandSet"):
                obj = Command()
                obj._deserialize(item)
                self._CommandSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvocationTasksRequest(AbstractModel):
    """DescribeInvocationTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvocationTaskIds: 执行任务ID列表，每次请求的上限为100。参数不支持同时指定 `InvocationTaskIds` 和 `Filters`。
        :type InvocationTaskIds: list of str
        :param _Filters: 过滤条件。<br>

- invocation-task-id - String - 是否必填：否 -（过滤条件）按照执行任务ID过滤。
- invocation-id - String - 是否必填：否 -（过滤条件）按照执行活动ID过滤。可通过 [DescribeInvocations(查询执行活动)](https://cloud.tencent.com/document/api/1340/52679) 接口获取。
- instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型： CVM、Lighthouse、TAT 托管实例
- command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。

每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InvocationTaskIds` 和 `Filters` 。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        :param _HideOutput: 是否隐藏命令输出结果，取值范围：

- true：隐藏输出
- false：不隐藏
 
默认为 true。
        :type HideOutput: bool
        """
        self._InvocationTaskIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._HideOutput = None

    @property
    def InvocationTaskIds(self):
        """执行任务ID列表，每次请求的上限为100。参数不支持同时指定 `InvocationTaskIds` 和 `Filters`。
        :rtype: list of str
        """
        return self._InvocationTaskIds

    @InvocationTaskIds.setter
    def InvocationTaskIds(self, InvocationTaskIds):
        self._InvocationTaskIds = InvocationTaskIds

    @property
    def Filters(self):
        """过滤条件。<br>

- invocation-task-id - String - 是否必填：否 -（过滤条件）按照执行任务ID过滤。
- invocation-id - String - 是否必填：否 -（过滤条件）按照执行活动ID过滤。可通过 [DescribeInvocations(查询执行活动)](https://cloud.tencent.com/document/api/1340/52679) 接口获取。
- instance-id - String - 是否必填：否 -（过滤条件）按照实例ID过滤。可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型： CVM、Lighthouse、TAT 托管实例
- command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。

每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InvocationTaskIds` 和 `Filters` 。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def HideOutput(self):
        """是否隐藏命令输出结果，取值范围：

- true：隐藏输出
- false：不隐藏
 
默认为 true。
        :rtype: bool
        """
        return self._HideOutput

    @HideOutput.setter
    def HideOutput(self, HideOutput):
        self._HideOutput = HideOutput


    def _deserialize(self, params):
        self._InvocationTaskIds = params.get("InvocationTaskIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._HideOutput = params.get("HideOutput")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvocationTasksResponse(AbstractModel):
    """DescribeInvocationTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的执行任务总数。
        :type TotalCount: int
        :param _InvocationTaskSet: 执行任务列表。
        :type InvocationTaskSet: list of InvocationTask
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InvocationTaskSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的执行任务总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvocationTaskSet(self):
        """执行任务列表。
        :rtype: list of InvocationTask
        """
        return self._InvocationTaskSet

    @InvocationTaskSet.setter
    def InvocationTaskSet(self, InvocationTaskSet):
        self._InvocationTaskSet = InvocationTaskSet

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
        if params.get("InvocationTaskSet") is not None:
            self._InvocationTaskSet = []
            for item in params.get("InvocationTaskSet"):
                obj = InvocationTask()
                obj._deserialize(item)
                self._InvocationTaskSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvocationsRequest(AbstractModel):
    """DescribeInvocations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvocationIds: 执行活动ID列表，每次请求的上限为100。参数不支持同时指定 `InvocationIds` 和 `Filters`。
        :type InvocationIds: list of str
        :param _Filters: 过滤条件。<br>

<li> invocation-id - String - 是否必填：否 -（过滤条件）按照执行活动ID过滤。</li>
 <li> command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。</li> 
<li> command-created-by - String - 是否必填：否 -（过滤条件）按照执行的命令类型过滤，取值为 TAT 或 USER，TAT 代表公共命令，USER 代表由用户创建的命令。</li>
 <li> instance-kind - String - 是否必填：否 -（过滤条件）按照运行实例类型过滤，取值为 CVM 或 LIGHTHOUSE，CVM 代表实例为云服务器， LIGHTHOUSE 代表实例为轻量应用服务器。</li>
 <br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InvocationIds` 和 `Filters` 。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._InvocationIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def InvocationIds(self):
        """执行活动ID列表，每次请求的上限为100。参数不支持同时指定 `InvocationIds` 和 `Filters`。
        :rtype: list of str
        """
        return self._InvocationIds

    @InvocationIds.setter
    def InvocationIds(self, InvocationIds):
        self._InvocationIds = InvocationIds

    @property
    def Filters(self):
        """过滤条件。<br>

<li> invocation-id - String - 是否必填：否 -（过滤条件）按照执行活动ID过滤。</li>
 <li> command-id - String - 是否必填：否 -（过滤条件）按照命令ID过滤。</li> 
<li> command-created-by - String - 是否必填：否 -（过滤条件）按照执行的命令类型过滤，取值为 TAT 或 USER，TAT 代表公共命令，USER 代表由用户创建的命令。</li>
 <li> instance-kind - String - 是否必填：否 -（过滤条件）按照运行实例类型过滤，取值为 CVM 或 LIGHTHOUSE，CVM 代表实例为云服务器， LIGHTHOUSE 代表实例为轻量应用服务器。</li>
 <br>每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `InvocationIds` 和 `Filters` 。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InvocationIds = params.get("InvocationIds")
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
        


class DescribeInvocationsResponse(AbstractModel):
    """DescribeInvocations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的执行活动总数。
        :type TotalCount: int
        :param _InvocationSet: 执行活动列表。
        :type InvocationSet: list of Invocation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InvocationSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的执行活动总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvocationSet(self):
        """执行活动列表。
        :rtype: list of Invocation
        """
        return self._InvocationSet

    @InvocationSet.setter
    def InvocationSet(self, InvocationSet):
        self._InvocationSet = InvocationSet

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
        if params.get("InvocationSet") is not None:
            self._InvocationSet = []
            for item in params.get("InvocationSet"):
                obj = Invocation()
                obj._deserialize(item)
                self._InvocationSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvokerRecordsRequest(AbstractModel):
    """DescribeInvokerRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokerIds: 执行器ID列表。列表上限 100。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :type InvokerIds: list of str
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._InvokerIds = None
        self._Limit = None
        self._Offset = None

    @property
    def InvokerIds(self):
        """执行器ID列表。列表上限 100。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :rtype: list of str
        """
        return self._InvokerIds

    @InvokerIds.setter
    def InvokerIds(self, InvokerIds):
        self._InvokerIds = InvokerIds

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InvokerIds = params.get("InvokerIds")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInvokerRecordsResponse(AbstractModel):
    """DescribeInvokerRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的历史记录数量。
        :type TotalCount: int
        :param _InvokerRecordSet: 执行器执行历史记录。
        :type InvokerRecordSet: list of InvokerRecord
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InvokerRecordSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的历史记录数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvokerRecordSet(self):
        """执行器执行历史记录。
        :rtype: list of InvokerRecord
        """
        return self._InvokerRecordSet

    @InvokerRecordSet.setter
    def InvokerRecordSet(self, InvokerRecordSet):
        self._InvokerRecordSet = InvokerRecordSet

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
        if params.get("InvokerRecordSet") is not None:
            self._InvokerRecordSet = []
            for item in params.get("InvokerRecordSet"):
                obj = InvokerRecord()
                obj._deserialize(item)
                self._InvokerRecordSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeInvokersRequest(AbstractModel):
    """DescribeInvokers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokerIds: 执行器ID列表。

参数不支持同时指定 `InvokerIds ` 和 `Filters ` 。

        :type InvokerIds: list of str
        :param _Filters: 过滤条件：

- invoker-id - String - 是否必填：否 - （过滤条件）按执行器ID过滤。
- command-id - String - 是否必填：否 - （过滤条件）按命令ID过滤。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
- type - String - 是否必填：否 - （过滤条件）按执行器类型过滤。目前仅支持 SCHEDULE 一种。

参数不支持同时指定 `InvokerIds ` 和 `Filters ` 。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        """
        self._InvokerIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def InvokerIds(self):
        """执行器ID列表。

参数不支持同时指定 `InvokerIds ` 和 `Filters ` 。

        :rtype: list of str
        """
        return self._InvokerIds

    @InvokerIds.setter
    def InvokerIds(self, InvokerIds):
        self._InvokerIds = InvokerIds

    @property
    def Filters(self):
        """过滤条件：

- invoker-id - String - 是否必填：否 - （过滤条件）按执行器ID过滤。
- command-id - String - 是否必填：否 - （过滤条件）按命令ID过滤。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
- type - String - 是否必填：否 - （过滤条件）按执行器类型过滤。目前仅支持 SCHEDULE 一种。

参数不支持同时指定 `InvokerIds ` 和 `Filters ` 。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._InvokerIds = params.get("InvokerIds")
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
        


class DescribeInvokersResponse(AbstractModel):
    """DescribeInvokers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 满足条件的执行器数量。
        :type TotalCount: int
        :param _InvokerSet: 执行器信息。
        :type InvokerSet: list of Invoker
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InvokerSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """满足条件的执行器数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InvokerSet(self):
        """执行器信息。
        :rtype: list of Invoker
        """
        return self._InvokerSet

    @InvokerSet.setter
    def InvokerSet(self, InvokerSet):
        self._InvokerSet = InvokerSet

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
        if params.get("InvokerSet") is not None:
            self._InvokerSet = []
            for item in params.get("InvokerSet"):
                obj = Invoker()
                obj._deserialize(item)
                self._InvokerSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeQuotasRequest(AbstractModel):
    """DescribeQuotas请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceNames: 资源名称

取值为：

- COMMAND：命令
- REGISTER_CODE：托管实例注册码
        :type ResourceNames: list of str
        """
        self._ResourceNames = None

    @property
    def ResourceNames(self):
        """资源名称

取值为：

- COMMAND：命令
- REGISTER_CODE：托管实例注册码
        :rtype: list of str
        """
        return self._ResourceNames

    @ResourceNames.setter
    def ResourceNames(self, ResourceNames):
        self._ResourceNames = ResourceNames


    def _deserialize(self, params):
        self._ResourceNames = params.get("ResourceNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeQuotasResponse(AbstractModel):
    """DescribeQuotas返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GeneralResourceQuotaSet: 资源额度列表
        :type GeneralResourceQuotaSet: list of GeneralResourceQuotaSet
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GeneralResourceQuotaSet = None
        self._RequestId = None

    @property
    def GeneralResourceQuotaSet(self):
        """资源额度列表
        :rtype: list of GeneralResourceQuotaSet
        """
        return self._GeneralResourceQuotaSet

    @GeneralResourceQuotaSet.setter
    def GeneralResourceQuotaSet(self, GeneralResourceQuotaSet):
        self._GeneralResourceQuotaSet = GeneralResourceQuotaSet

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
        if params.get("GeneralResourceQuotaSet") is not None:
            self._GeneralResourceQuotaSet = []
            for item in params.get("GeneralResourceQuotaSet"):
                obj = GeneralResourceQuotaSet()
                obj._deserialize(item)
                self._GeneralResourceQuotaSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegionsRequest(AbstractModel):
    """DescribeRegions请求参数结构体

    """


class DescribeRegionsResponse(AbstractModel):
    """DescribeRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 地域数量
        :type TotalCount: int
        :param _RegionSet: 地域信息列表
        :type RegionSet: list of RegionInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegionSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """地域数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegionSet(self):
        """地域信息列表
        :rtype: list of RegionInfo
        """
        return self._RegionSet

    @RegionSet.setter
    def RegionSet(self, RegionSet):
        self._RegionSet = RegionSet

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
        if params.get("RegionSet") is not None:
            self._RegionSet = []
            for item in params.get("RegionSet"):
                obj = RegionInfo()
                obj._deserialize(item)
                self._RegionSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegisterCodesRequest(AbstractModel):
    """DescribeRegisterCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegisterCodeIds: 注册码ID。
        :type RegisterCodeIds: list of str
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._RegisterCodeIds = None
        self._Offset = None
        self._Limit = None

    @property
    def RegisterCodeIds(self):
        """注册码ID。
        :rtype: list of str
        """
        return self._RegisterCodeIds

    @RegisterCodeIds.setter
    def RegisterCodeIds(self, RegisterCodeIds):
        self._RegisterCodeIds = RegisterCodeIds

    @property
    def Offset(self):
        """偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._RegisterCodeIds = params.get("RegisterCodeIds")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegisterCodesResponse(AbstractModel):
    """DescribeRegisterCodes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 查询到的注册码总数。
        :type TotalCount: int
        :param _RegisterCodeSet: 注册码信息列表。
        :type RegisterCodeSet: list of RegisterCodeInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegisterCodeSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """查询到的注册码总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegisterCodeSet(self):
        """注册码信息列表。
        :rtype: list of RegisterCodeInfo
        """
        return self._RegisterCodeSet

    @RegisterCodeSet.setter
    def RegisterCodeSet(self, RegisterCodeSet):
        self._RegisterCodeSet = RegisterCodeSet

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
        if params.get("RegisterCodeSet") is not None:
            self._RegisterCodeSet = []
            for item in params.get("RegisterCodeSet"):
                obj = RegisterCodeInfo()
                obj._deserialize(item)
                self._RegisterCodeSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRegisterInstancesRequest(AbstractModel):
    """DescribeRegisterInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 托管实例 id。

参数不支持同时指定 `InstanceIds` 和 `Filters` 。

        :type InstanceIds: list of str
        :param _Filters: 过滤器列表。参数不支持同时指定 `InstanceIds` 和 `Filters` 。


- instance-name

按照【托管实例名称】进行过滤。
类型：String
必选：否

- instance-id

按照【托管实例ID】进行过滤。
类型：String
必选：否

- register-code-id

按照【托管实例注册码ID】进行过滤。可通过 [DescribeRegisterCodes(查询注册码)](https://cloud.tencent.com/document/api/1340/96925) 接口获取。
类型：String
必选：否

- sys-name

按照【操作系统类型】进行过滤，取值：Linux | Windows。
类型：String
必选：否

- tag-key

按照【标签键】进行过滤。
类型：String
必选：否

- tag-value

按照【标签值】进行过滤。
类型：String
必选：否

- tag:tag-key

按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
类型：String
必选：否

例如 Filter 为 {"Name": "tag:key1", "Values": ["v1", "v2"] } ，即查询所有标签为 key1:v1 或 key1:v2 的资源。


        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        """
        self._InstanceIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def InstanceIds(self):
        """托管实例 id。

参数不支持同时指定 `InstanceIds` 和 `Filters` 。

        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Filters(self):
        """过滤器列表。参数不支持同时指定 `InstanceIds` 和 `Filters` 。


- instance-name

按照【托管实例名称】进行过滤。
类型：String
必选：否

- instance-id

按照【托管实例ID】进行过滤。
类型：String
必选：否

- register-code-id

按照【托管实例注册码ID】进行过滤。可通过 [DescribeRegisterCodes(查询注册码)](https://cloud.tencent.com/document/api/1340/96925) 接口获取。
类型：String
必选：否

- sys-name

按照【操作系统类型】进行过滤，取值：Linux | Windows。
类型：String
必选：否

- tag-key

按照【标签键】进行过滤。
类型：String
必选：否

- tag-value

按照【标签值】进行过滤。
类型：String
必选：否

- tag:tag-key

按照【标签键值对】进行过滤。 tag-key使用具体的标签键进行替换。
类型：String
必选：否

例如 Filter 为 {"Name": "tag:key1", "Values": ["v1", "v2"] } ，即查询所有标签为 key1:v1 或 key1:v2 的资源。


        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        """偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._InstanceIds = params.get("InstanceIds")
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
        


class DescribeRegisterInstancesResponse(AbstractModel):
    """DescribeRegisterInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 该实例注册过的注册码总数。
        :type TotalCount: int
        :param _RegisterInstanceSet: 被托管的实例信息的列表。
        :type RegisterInstanceSet: list of RegisterInstanceInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RegisterInstanceSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """该实例注册过的注册码总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RegisterInstanceSet(self):
        """被托管的实例信息的列表。
        :rtype: list of RegisterInstanceInfo
        """
        return self._RegisterInstanceSet

    @RegisterInstanceSet.setter
    def RegisterInstanceSet(self, RegisterInstanceSet):
        self._RegisterInstanceSet = RegisterInstanceSet

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
        if params.get("RegisterInstanceSet") is not None:
            self._RegisterInstanceSet = []
            for item in params.get("RegisterInstanceSet"):
                obj = RegisterInstanceInfo()
                obj._deserialize(item)
                self._RegisterInstanceSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScenesRequest(AbstractModel):
    """DescribeScenes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SceneIds: 场景 ID 数组。

参数不支持同时指定 `SceneIds ` 和 `Filters ` 。

        :type SceneIds: list of str
        :param _Filters: 过滤条件。

- scene-id - String - 是否必填：否 -（过滤条件）按照场景 ID 过滤。
- scene-name - String - 是否必填：否 -（过滤条件）按照场景名称过滤。
- created-by - String - 是否必填：否 -（过滤条件）按照场景创建者过滤，目前仅支持 TAT，代表公共场景。

每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `SceneIds` 和 `Filters` 。
        :type Filters: list of Filter
        :param _Limit: 返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Limit: int
        :param _Offset: 偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :type Offset: int
        """
        self._SceneIds = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def SceneIds(self):
        """场景 ID 数组。

参数不支持同时指定 `SceneIds ` 和 `Filters ` 。

        :rtype: list of str
        """
        return self._SceneIds

    @SceneIds.setter
    def SceneIds(self, SceneIds):
        self._SceneIds = SceneIds

    @property
    def Filters(self):
        """过滤条件。

- scene-id - String - 是否必填：否 -（过滤条件）按照场景 ID 过滤。
- scene-name - String - 是否必填：否 -（过滤条件）按照场景名称过滤。
- created-by - String - 是否必填：否 -（过滤条件）按照场景创建者过滤，目前仅支持 TAT，代表公共场景。

每次请求的 `Filters` 的上限为10， `Filter.Values` 的上限为5。参数不支持同时指定 `SceneIds` 和 `Filters` 。
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        """返回数量，默认为20，最大值为100。关于 `Limit` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """偏移量，默认为0。关于 `Offset` 的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/15688)中的相关小节。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._SceneIds = params.get("SceneIds")
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
        


class DescribeScenesResponse(AbstractModel):
    """DescribeScenes返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的场景总数。
        :type TotalCount: int
        :param _SceneSet: 场景详情列表。
        :type SceneSet: list of Scene
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SceneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的场景总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SceneSet(self):
        """场景详情列表。
        :rtype: list of Scene
        """
        return self._SceneSet

    @SceneSet.setter
    def SceneSet(self, SceneSet):
        self._SceneSet = SceneSet

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
        if params.get("SceneSet") is not None:
            self._SceneSet = []
            for item in params.get("SceneSet"):
                obj = Scene()
                obj._deserialize(item)
                self._SceneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DisableInvokerRequest(AbstractModel):
    """DisableInvoker请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokerId: 待停止的执行器ID。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        """待停止的执行器ID。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableInvokerResponse(AbstractModel):
    """DisableInvoker返回参数结构体

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


class DisableRegisterCodesRequest(AbstractModel):
    """DisableRegisterCodes请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RegisterCodeIds: 注册码ID。

可通过 [DescribeRegisterCodes(查询注册码)](https://cloud.tencent.com/document/api/1340/96925) 接口获取。
        :type RegisterCodeIds: list of str
        """
        self._RegisterCodeIds = None

    @property
    def RegisterCodeIds(self):
        """注册码ID。

可通过 [DescribeRegisterCodes(查询注册码)](https://cloud.tencent.com/document/api/1340/96925) 接口获取。
        :rtype: list of str
        """
        return self._RegisterCodeIds

    @RegisterCodeIds.setter
    def RegisterCodeIds(self, RegisterCodeIds):
        self._RegisterCodeIds = RegisterCodeIds


    def _deserialize(self, params):
        self._RegisterCodeIds = params.get("RegisterCodeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRegisterCodesResponse(AbstractModel):
    """DisableRegisterCodes返回参数结构体

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


class EnableInvokerRequest(AbstractModel):
    """EnableInvoker请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokerId: 待启用的执行器ID。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :type InvokerId: str
        """
        self._InvokerId = None

    @property
    def InvokerId(self):
        """待启用的执行器ID。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableInvokerResponse(AbstractModel):
    """EnableInvoker返回参数结构体

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


class Filter(AbstractModel):
    """> 描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等
    > - 若存在多个`Filter`时，`Filter`间的关系为逻辑与（`AND`）关系。
    > - 若同一个`Filter`存在多个`Values`，同一`Filter`下`Values`间的关系为逻辑或（`OR`）关系。
    >
    > 以[DescribeCommands](https://cloud.tencent.com/document/api/1340/52681)接口的`Filters`为例。若我们需要查询命令名称（`command-name`）为 “打印工作目录” ***并且*** 命令类型（`command-type`）为 “POWERSHELL” ***或者*** “BAT” 时，可如下实现：
    ```
    Filters.0.Name=command-name
    &Filters.0.Values.0=打印工作目录

    &Filters.1.Name=command-type
    &Filters.1.Values.0=POWERSHELL
    &Filters.1.Values.1=BAT
    ```

    """

    def __init__(self):
        r"""
        :param _Name: 需要过滤的字段。
        :type Name: str
        :param _Values: 字段的过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """需要过滤的字段。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """字段的过滤值。
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
        


class GeneralResourceQuotaSet(AbstractModel):
    """用户配额信息。

    """

    def __init__(self):
        r"""
        :param _ResourceName: 资源名称

取值为：

- COMMAND：命令
- REGISTER_CODE：托管实例注册码
        :type ResourceName: str
        :param _ResourceQuotaUsed: 已使用额度
        :type ResourceQuotaUsed: int
        :param _ResourceQuotaTotal: 总额度
        :type ResourceQuotaTotal: int
        """
        self._ResourceName = None
        self._ResourceQuotaUsed = None
        self._ResourceQuotaTotal = None

    @property
    def ResourceName(self):
        """资源名称

取值为：

- COMMAND：命令
- REGISTER_CODE：托管实例注册码
        :rtype: str
        """
        return self._ResourceName

    @ResourceName.setter
    def ResourceName(self, ResourceName):
        self._ResourceName = ResourceName

    @property
    def ResourceQuotaUsed(self):
        """已使用额度
        :rtype: int
        """
        return self._ResourceQuotaUsed

    @ResourceQuotaUsed.setter
    def ResourceQuotaUsed(self, ResourceQuotaUsed):
        self._ResourceQuotaUsed = ResourceQuotaUsed

    @property
    def ResourceQuotaTotal(self):
        """总额度
        :rtype: int
        """
        return self._ResourceQuotaTotal

    @ResourceQuotaTotal.setter
    def ResourceQuotaTotal(self, ResourceQuotaTotal):
        self._ResourceQuotaTotal = ResourceQuotaTotal


    def _deserialize(self, params):
        self._ResourceName = params.get("ResourceName")
        self._ResourceQuotaUsed = params.get("ResourceQuotaUsed")
        self._ResourceQuotaTotal = params.get("ResourceQuotaTotal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Invocation(AbstractModel):
    """执行活动详情。

    """

    def __init__(self):
        r"""
        :param _InvocationId: 执行活动ID。
        :type InvocationId: str
        :param _CommandId: 命令ID。
        :type CommandId: str
        :param _InvocationStatus: 执行任务状态。取值范围：

- PENDING：等待下发
- RUNNING：命令运行中
- CANCELLING：取消中
- SUCCESS：命令成功
- TIMEOUT：命令超时
- FAILED：命令失败
- CANCELLED：命令全部取消
- PARTIAL_FAILED：命令部分失败
- PARTIAL_CANCELLED：命令部分取消
        :type InvocationStatus: str
        :param _InvocationTaskBasicInfoSet: 执行任务信息列表。
        :type InvocationTaskBasicInfoSet: list of InvocationTaskBasicInfo
        :param _Description: 执行活动描述。
        :type Description: str
        :param _StartTime: 执行活动开始时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type StartTime: str
        :param _EndTime: 执行活动结束时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type EndTime: str
        :param _CreatedTime: 执行活动创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type CreatedTime: str
        :param _UpdatedTime: 执行活动更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type UpdatedTime: str
        :param _Parameters: 自定义参数取值。
        :type Parameters: str
        :param _DefaultParameters: 自定义参数的默认取值。
        :type DefaultParameters: str
        :param _InstanceKind: 执行命令的实例类型，取值范围：CVM、LIGHTHOUSE。
        :type InstanceKind: str
        :param _Username: 在实例上执行命令时使用的用户名。
        :type Username: str
        :param _InvocationSource: 调用来源。

- USER：来源于用户调用。
- INVOKER：来源于定时执行。
        :type InvocationSource: str
        :param _CommandContent: base64编码的命令内容
        :type CommandContent: str
        :param _CommandType: 命令类型
        :type CommandType: str
        :param _Timeout: 执行命令过期时间， 单位秒
        :type Timeout: int
        :param _WorkingDirectory: 执行命令的工作路径
        :type WorkingDirectory: str
        :param _OutputCOSBucketUrl: 日志上传的cos bucket 地址。
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: 日志在cos bucket中的目录。
        :type OutputCOSKeyPrefix: str
        """
        self._InvocationId = None
        self._CommandId = None
        self._InvocationStatus = None
        self._InvocationTaskBasicInfoSet = None
        self._Description = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._Parameters = None
        self._DefaultParameters = None
        self._InstanceKind = None
        self._Username = None
        self._InvocationSource = None
        self._CommandContent = None
        self._CommandType = None
        self._Timeout = None
        self._WorkingDirectory = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def InvocationId(self):
        """执行活动ID。
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def CommandId(self):
        """命令ID。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InvocationStatus(self):
        """执行任务状态。取值范围：

- PENDING：等待下发
- RUNNING：命令运行中
- CANCELLING：取消中
- SUCCESS：命令成功
- TIMEOUT：命令超时
- FAILED：命令失败
- CANCELLED：命令全部取消
- PARTIAL_FAILED：命令部分失败
- PARTIAL_CANCELLED：命令部分取消
        :rtype: str
        """
        return self._InvocationStatus

    @InvocationStatus.setter
    def InvocationStatus(self, InvocationStatus):
        self._InvocationStatus = InvocationStatus

    @property
    def InvocationTaskBasicInfoSet(self):
        """执行任务信息列表。
        :rtype: list of InvocationTaskBasicInfo
        """
        return self._InvocationTaskBasicInfoSet

    @InvocationTaskBasicInfoSet.setter
    def InvocationTaskBasicInfoSet(self, InvocationTaskBasicInfoSet):
        self._InvocationTaskBasicInfoSet = InvocationTaskBasicInfoSet

    @property
    def Description(self):
        """执行活动描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def StartTime(self):
        """执行活动开始时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """执行活动结束时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        """执行活动创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """执行活动更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Parameters(self):
        """自定义参数取值。
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def DefaultParameters(self):
        """自定义参数的默认取值。
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def InstanceKind(self):
        """执行命令的实例类型，取值范围：CVM、LIGHTHOUSE。
        :rtype: str
        """
        return self._InstanceKind

    @InstanceKind.setter
    def InstanceKind(self, InstanceKind):
        self._InstanceKind = InstanceKind

    @property
    def Username(self):
        """在实例上执行命令时使用的用户名。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def InvocationSource(self):
        """调用来源。

- USER：来源于用户调用。
- INVOKER：来源于定时执行。
        :rtype: str
        """
        return self._InvocationSource

    @InvocationSource.setter
    def InvocationSource(self, InvocationSource):
        self._InvocationSource = InvocationSource

    @property
    def CommandContent(self):
        """base64编码的命令内容
        :rtype: str
        """
        return self._CommandContent

    @CommandContent.setter
    def CommandContent(self, CommandContent):
        self._CommandContent = CommandContent

    @property
    def CommandType(self):
        """命令类型
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def Timeout(self):
        """执行命令过期时间， 单位秒
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def WorkingDirectory(self):
        """执行命令的工作路径
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def OutputCOSBucketUrl(self):
        """日志上传的cos bucket 地址。
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """日志在cos bucket中的目录。
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._InvocationId = params.get("InvocationId")
        self._CommandId = params.get("CommandId")
        self._InvocationStatus = params.get("InvocationStatus")
        if params.get("InvocationTaskBasicInfoSet") is not None:
            self._InvocationTaskBasicInfoSet = []
            for item in params.get("InvocationTaskBasicInfoSet"):
                obj = InvocationTaskBasicInfo()
                obj._deserialize(item)
                self._InvocationTaskBasicInfoSet.append(obj)
        self._Description = params.get("Description")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        self._Parameters = params.get("Parameters")
        self._DefaultParameters = params.get("DefaultParameters")
        self._InstanceKind = params.get("InstanceKind")
        self._Username = params.get("Username")
        self._InvocationSource = params.get("InvocationSource")
        self._CommandContent = params.get("CommandContent")
        self._CommandType = params.get("CommandType")
        self._Timeout = params.get("Timeout")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTask(AbstractModel):
    """执行任务。

    """

    def __init__(self):
        r"""
        :param _InvocationId: 执行活动ID。
        :type InvocationId: str
        :param _InvocationTaskId: 执行任务ID。
        :type InvocationTaskId: str
        :param _CommandId: 命令ID。
        :type CommandId: str
        :param _TaskStatus: 执行任务状态。取值范围：

- PENDING：等待下发
- DELIVERING：下发中
- DELIVER_DELAYED：延时下发
- DELIVER_FAILED：下发失败
- START_FAILED：命令启动失败
- RUNNING：命令运行中
- SUCCESS：命令成功
- FAILED：命令执行失败，执行完退出码不为 0
- TIMEOUT：命令超时
- TASK_TIMEOUT：客户端无响应
- CANCELLING：取消中
- CANCELLED：已取消（命令启动前就被取消）
- TERMINATED：已中止（命令执行期间被取消）
        :type TaskStatus: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        :param _TaskResult: 执行结果。
        :type TaskResult: :class:`tencentcloud.tat.v20201028.models.TaskResult`
        :param _StartTime: 执行任务开始时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTime: str
        :param _EndTime: 执行任务结束时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: str
        :param _CreatedTime: 创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type UpdatedTime: str
        :param _CommandDocument: 执行任务所执行的命令详情。
        :type CommandDocument: :class:`tencentcloud.tat.v20201028.models.CommandDocument`
        :param _ErrorInfo: 执行任务失败时的错误信息。
        :type ErrorInfo: str
        :param _InvocationSource: 调用来源。

- USER：来源于用户调用。
- INVOKER：来源于定时执行。
        :type InvocationSource: str
        """
        self._InvocationId = None
        self._InvocationTaskId = None
        self._CommandId = None
        self._TaskStatus = None
        self._InstanceId = None
        self._TaskResult = None
        self._StartTime = None
        self._EndTime = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._CommandDocument = None
        self._ErrorInfo = None
        self._InvocationSource = None

    @property
    def InvocationId(self):
        """执行活动ID。
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def InvocationTaskId(self):
        """执行任务ID。
        :rtype: str
        """
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def CommandId(self):
        """命令ID。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def TaskStatus(self):
        """执行任务状态。取值范围：

- PENDING：等待下发
- DELIVERING：下发中
- DELIVER_DELAYED：延时下发
- DELIVER_FAILED：下发失败
- START_FAILED：命令启动失败
- RUNNING：命令运行中
- SUCCESS：命令成功
- FAILED：命令执行失败，执行完退出码不为 0
- TIMEOUT：命令超时
- TASK_TIMEOUT：客户端无响应
- CANCELLING：取消中
- CANCELLED：已取消（命令启动前就被取消）
- TERMINATED：已中止（命令执行期间被取消）
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def TaskResult(self):
        """执行结果。
        :rtype: :class:`tencentcloud.tat.v20201028.models.TaskResult`
        """
        return self._TaskResult

    @TaskResult.setter
    def TaskResult(self, TaskResult):
        self._TaskResult = TaskResult

    @property
    def StartTime(self):
        """执行任务开始时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """执行任务结束时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreatedTime(self):
        """创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def CommandDocument(self):
        """执行任务所执行的命令详情。
        :rtype: :class:`tencentcloud.tat.v20201028.models.CommandDocument`
        """
        return self._CommandDocument

    @CommandDocument.setter
    def CommandDocument(self, CommandDocument):
        self._CommandDocument = CommandDocument

    @property
    def ErrorInfo(self):
        """执行任务失败时的错误信息。
        :rtype: str
        """
        return self._ErrorInfo

    @ErrorInfo.setter
    def ErrorInfo(self, ErrorInfo):
        self._ErrorInfo = ErrorInfo

    @property
    def InvocationSource(self):
        """调用来源。

- USER：来源于用户调用。
- INVOKER：来源于定时执行。
        :rtype: str
        """
        return self._InvocationSource

    @InvocationSource.setter
    def InvocationSource(self, InvocationSource):
        self._InvocationSource = InvocationSource


    def _deserialize(self, params):
        self._InvocationId = params.get("InvocationId")
        self._InvocationTaskId = params.get("InvocationTaskId")
        self._CommandId = params.get("CommandId")
        self._TaskStatus = params.get("TaskStatus")
        self._InstanceId = params.get("InstanceId")
        if params.get("TaskResult") is not None:
            self._TaskResult = TaskResult()
            self._TaskResult._deserialize(params.get("TaskResult"))
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        if params.get("CommandDocument") is not None:
            self._CommandDocument = CommandDocument()
            self._CommandDocument._deserialize(params.get("CommandDocument"))
        self._ErrorInfo = params.get("ErrorInfo")
        self._InvocationSource = params.get("InvocationSource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvocationTaskBasicInfo(AbstractModel):
    """执行活动任务简介。

    """

    def __init__(self):
        r"""
        :param _InvocationTaskId: 执行任务ID。
        :type InvocationTaskId: str
        :param _TaskStatus: 执行任务状态。取值范围：

- PENDING：等待下发
- DELIVERING：下发中
- DELIVER_DELAYED：延时下发
- DELIVER_FAILED：下发失败
- START_FAILED：命令启动失败
- RUNNING：命令运行中
- SUCCESS：命令成功
- FAILED：命令执行失败，执行完退出码不为 0
- TIMEOUT：命令超时
- TASK_TIMEOUT：客户端无响应
- CANCELLING：取消中
- CANCELLED：已取消（命令启动前就被取消）
- TERMINATED：已中止（命令执行期间被取消）
        :type TaskStatus: str
        :param _InstanceId: 实例ID。
        :type InstanceId: str
        """
        self._InvocationTaskId = None
        self._TaskStatus = None
        self._InstanceId = None

    @property
    def InvocationTaskId(self):
        """执行任务ID。
        :rtype: str
        """
        return self._InvocationTaskId

    @InvocationTaskId.setter
    def InvocationTaskId(self, InvocationTaskId):
        self._InvocationTaskId = InvocationTaskId

    @property
    def TaskStatus(self):
        """执行任务状态。取值范围：

- PENDING：等待下发
- DELIVERING：下发中
- DELIVER_DELAYED：延时下发
- DELIVER_FAILED：下发失败
- START_FAILED：命令启动失败
- RUNNING：命令运行中
- SUCCESS：命令成功
- FAILED：命令执行失败，执行完退出码不为 0
- TIMEOUT：命令超时
- TASK_TIMEOUT：客户端无响应
- CANCELLING：取消中
- CANCELLED：已取消（命令启动前就被取消）
- TERMINATED：已中止（命令执行期间被取消）
        :rtype: str
        """
        return self._TaskStatus

    @TaskStatus.setter
    def TaskStatus(self, TaskStatus):
        self._TaskStatus = TaskStatus

    @property
    def InstanceId(self):
        """实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InvocationTaskId = params.get("InvocationTaskId")
        self._TaskStatus = params.get("TaskStatus")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCommandRequest(AbstractModel):
    """InvokeCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandId: 待触发的命令ID。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :type CommandId: str
        :param _InstanceIds: 待执行命令的实例ID列表，上限200。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：
- CVM
- Lighthouse
- TAT 托管实例
        :type InstanceIds: list of str
        :param _Parameters: Command 的自定义参数。字段类型为json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
如果未提供该参数取值，将使用 Command 的 DefaultParameters 或 DefaultParameterConfs 进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type Parameters: str
        :param _Username: 在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。若不填，默认以 Command 配置的 Username 执行。
        :type Username: str
        :param _WorkingDirectory: 命令执行路径, 默认以Command配置的WorkingDirectory执行。
        :type WorkingDirectory: str
        :param _Timeout: 命令超时时间，取值范围[1, 86400]。默认以Command配置的Timeout执行。
        :type Timeout: int
        :param _OutputCOSBucketUrl: 指定日志上传的cos bucket 地址，必须以https开头，如 https://BucketName-123454321.cos.ap-beijing.myqcloud.com。
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: 指定日志在cos bucket中的目录，目录命名有如下规则：
1. 可用数字、中英文和可见字符的组合，长度最多为60。
2. 用 / 分割路径，可快速创建子目录。
3. 不允许连续 / ；不允许以 / 开头；不允许以..作为文件夹名称。
        :type OutputCOSKeyPrefix: str
        """
        self._CommandId = None
        self._InstanceIds = None
        self._Parameters = None
        self._Username = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandId(self):
        """待触发的命令ID。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InstanceIds(self):
        """待执行命令的实例ID列表，上限200。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：
- CVM
- Lighthouse
- TAT 托管实例
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Parameters(self):
        """Command 的自定义参数。字段类型为json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
如果未提供该参数取值，将使用 Command 的 DefaultParameters 或 DefaultParameterConfs 进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Username(self):
        """在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。若不填，默认以 Command 配置的 Username 执行。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def WorkingDirectory(self):
        """命令执行路径, 默认以Command配置的WorkingDirectory执行。
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """命令超时时间，取值范围[1, 86400]。默认以Command配置的Timeout执行。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def OutputCOSBucketUrl(self):
        """指定日志上传的cos bucket 地址，必须以https开头，如 https://BucketName-123454321.cos.ap-beijing.myqcloud.com。
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """指定日志在cos bucket中的目录，目录命名有如下规则：
1. 可用数字、中英文和可见字符的组合，长度最多为60。
2. 用 / 分割路径，可快速创建子目录。
3. 不允许连续 / ；不允许以 / 开头；不允许以..作为文件夹名称。
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        self._InstanceIds = params.get("InstanceIds")
        self._Parameters = params.get("Parameters")
        self._Username = params.get("Username")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokeCommandResponse(AbstractModel):
    """InvokeCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InvocationId: 执行活动ID。
        :type InvocationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InvocationId = None
        self._RequestId = None

    @property
    def InvocationId(self):
        """执行活动ID。
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

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
        self._InvocationId = params.get("InvocationId")
        self._RequestId = params.get("RequestId")


class Invoker(AbstractModel):
    """执行器信息。

    """

    def __init__(self):
        r"""
        :param _InvokerId: 执行器ID。
        :type InvokerId: str
        :param _Name: 执行器名称。
        :type Name: str
        :param _Type: 执行器类型。目前仅支持 SCHEDULE 一种。
        :type Type: str
        :param _CommandId: 命令ID。
        :type CommandId: str
        :param _Username: 用户名。
        :type Username: str
        :param _Parameters: 自定义参数。
        :type Parameters: str
        :param _InstanceIds: 实例ID列表。
        :type InstanceIds: list of str
        :param _Enable: 执行器是否启用。
        :type Enable: bool
        :param _ScheduleSettings: 执行器周期计划。周期执行器会返回此字段。
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        :param _CreatedTime: 创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type CreatedTime: str
        :param _UpdatedTime: 修改时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type UpdatedTime: str
        """
        self._InvokerId = None
        self._Name = None
        self._Type = None
        self._CommandId = None
        self._Username = None
        self._Parameters = None
        self._InstanceIds = None
        self._Enable = None
        self._ScheduleSettings = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def InvokerId(self):
        """执行器ID。
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def Name(self):
        """执行器名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """执行器类型。目前仅支持 SCHEDULE 一种。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        """命令ID。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Username(self):
        """用户名。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        """自定义参数。
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def InstanceIds(self):
        """实例ID列表。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def Enable(self):
        """执行器是否启用。
        :rtype: bool
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def ScheduleSettings(self):
        """执行器周期计划。周期执行器会返回此字段。
        :rtype: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        return self._ScheduleSettings

    @ScheduleSettings.setter
    def ScheduleSettings(self, ScheduleSettings):
        self._ScheduleSettings = ScheduleSettings

    @property
    def CreatedTime(self):
        """创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """修改时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CommandId = params.get("CommandId")
        self._Username = params.get("Username")
        self._Parameters = params.get("Parameters")
        self._InstanceIds = params.get("InstanceIds")
        self._Enable = params.get("Enable")
        if params.get("ScheduleSettings") is not None:
            self._ScheduleSettings = ScheduleSettings()
            self._ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InvokerRecord(AbstractModel):
    """执行器执行记录。

    """

    def __init__(self):
        r"""
        :param _InvokerId: 执行器ID。
        :type InvokerId: str
        :param _InvokeTime: 执行时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type InvokeTime: str
        :param _Reason: 执行原因。
        :type Reason: str
        :param _InvocationId: 命令执行ID。
        :type InvocationId: str
        :param _Result: 触发结果。

- PENDING：等待下发
- RUNNING：命令运行中
- CANCELLING：取消中
- SUCCESS：命令成功
- TIMEOUT：命令超时
- FAILED：命令失败
- CANCELLED：命令全部取消
- PARTIAL_FAILED：命令部分失败
- PARTIAL_CANCELLED：命令部分取消
        :type Result: str
        """
        self._InvokerId = None
        self._InvokeTime = None
        self._Reason = None
        self._InvocationId = None
        self._Result = None

    @property
    def InvokerId(self):
        """执行器ID。
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def InvokeTime(self):
        """执行时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._InvokeTime

    @InvokeTime.setter
    def InvokeTime(self, InvokeTime):
        self._InvokeTime = InvokeTime

    @property
    def Reason(self):
        """执行原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason

    @property
    def InvocationId(self):
        """命令执行ID。
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

    @property
    def Result(self):
        """触发结果。

- PENDING：等待下发
- RUNNING：命令运行中
- CANCELLING：取消中
- SUCCESS：命令成功
- TIMEOUT：命令超时
- FAILED：命令失败
- CANCELLED：命令全部取消
- PARTIAL_FAILED：命令部分失败
- PARTIAL_CANCELLED：命令部分取消
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        self._InvokeTime = params.get("InvokeTime")
        self._Reason = params.get("Reason")
        self._InvocationId = params.get("InvocationId")
        self._Result = params.get("Result")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCommandRequest(AbstractModel):
    """ModifyCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandId: 命令ID。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :type CommandId: str
        :param _CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type CommandName: str
        :param _Description: 命令描述。不超过120字符。
        :type Description: str
        :param _Content: Base64编码后的命令内容，长度不可超过64KB。
        :type Content: str
        :param _CommandType: 命令类型，目前支持取值：SHELL、POWERSHELL、BAT。
        :type CommandType: str
        :param _WorkingDirectory: 命令执行路径。
        :type WorkingDirectory: str
        :param _Timeout: 命令超时时间。取值范围[1, 86400]。
        :type Timeout: int
        :param _DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{"varA": "222"}。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
采取整体全覆盖式修改，即修改时必须提供所有新默认值。
仅在命令的 EnableParameter 为 true 时，才允许修改此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type DefaultParameters: str
        :param _DefaultParameterConfs: 自定义参数数组。如果 InvokeCommand 时未提供参数取值，将使用这里的默认值进行替换。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
仅在命令的 EnableParameter 为 true 时，才允许修改此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
自定义参数最多20个。
        :type DefaultParameterConfs: list of DefaultParameterConf
        :param _Username: 在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。
        :type Username: str
        :param _OutputCOSBucketUrl: 指定日志上传的cos bucket 地址，必须以https开头，如 https://BucketName-123454321.cos.ap-beijing.myqcloud.com。
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: 指定日志在cos bucket中的目录，目录命名有如下规则：
1. 可用数字、中英文和可见字符的组合，长度最多为60。
2. 用 / 分割路径，可快速创建子目录。
3. 不允许连续 / ；不允许以 / 开头；不允许以..作为文件夹名称。
        :type OutputCOSKeyPrefix: str
        """
        self._CommandId = None
        self._CommandName = None
        self._Description = None
        self._Content = None
        self._CommandType = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._DefaultParameters = None
        self._DefaultParameterConfs = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def CommandId(self):
        """命令ID。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def CommandName(self):
        """命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        """命令描述。不超过120字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Content(self):
        """Base64编码后的命令内容，长度不可超过64KB。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def CommandType(self):
        """命令类型，目前支持取值：SHELL、POWERSHELL、BAT。
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        """命令执行路径。
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """命令超时时间。取值范围[1, 86400]。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def DefaultParameters(self):
        """启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{"varA": "222"}。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
采取整体全覆盖式修改，即修改时必须提供所有新默认值。
仅在命令的 EnableParameter 为 true 时，才允许修改此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def DefaultParameterConfs(self):
        """自定义参数数组。如果 InvokeCommand 时未提供参数取值，将使用这里的默认值进行替换。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
仅在命令的 EnableParameter 为 true 时，才允许修改此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
自定义参数最多20个。
        :rtype: list of DefaultParameterConf
        """
        return self._DefaultParameterConfs

    @DefaultParameterConfs.setter
    def DefaultParameterConfs(self, DefaultParameterConfs):
        self._DefaultParameterConfs = DefaultParameterConfs

    @property
    def Username(self):
        """在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """指定日志上传的cos bucket 地址，必须以https开头，如 https://BucketName-123454321.cos.ap-beijing.myqcloud.com。
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """指定日志在cos bucket中的目录，目录命名有如下规则：
1. 可用数字、中英文和可见字符的组合，长度最多为60。
2. 用 / 分割路径，可快速创建子目录。
3. 不允许连续 / ；不允许以 / 开头；不允许以..作为文件夹名称。
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._CommandId = params.get("CommandId")
        self._CommandName = params.get("CommandName")
        self._Description = params.get("Description")
        self._Content = params.get("Content")
        self._CommandType = params.get("CommandType")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._DefaultParameters = params.get("DefaultParameters")
        if params.get("DefaultParameterConfs") is not None:
            self._DefaultParameterConfs = []
            for item in params.get("DefaultParameterConfs"):
                obj = DefaultParameterConf()
                obj._deserialize(item)
                self._DefaultParameterConfs.append(obj)
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCommandResponse(AbstractModel):
    """ModifyCommand返回参数结构体

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


class ModifyInvokerRequest(AbstractModel):
    """ModifyInvoker请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InvokerId: 待修改的执行器ID。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :type InvokerId: str
        :param _Name: 待修改的执行器名称。
        :type Name: str
        :param _Type: 执行器类型，当前仅支持周期类型执行器，取值：`SCHEDULE` 。
        :type Type: str
        :param _CommandId: 待修改的命令ID。

可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :type CommandId: str
        :param _Username: 待修改的用户名。
        :type Username: str
        :param _Parameters: 待修改的自定义参数。

仅在 CommandId 所指命令的 EnableParameter 为 true 时，才允许设置此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
        :type Parameters: str
        :param _InstanceIds: 待修改的实例ID列表。列表长度上限100。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：CVM、Lighthouse、TAT 托管实例。

实例需要安装 TAT 客户端, 且客户端为 Online 状态。可通过 [DescribeAutomationAgentStatus(查询客户端状态)](https://cloud.tencent.com/document/api/1340/52682) 接口查询客户端状态。
        :type InstanceIds: list of str
        :param _ScheduleSettings: 待修改的周期执行器设置。
        :type ScheduleSettings: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        self._InvokerId = None
        self._Name = None
        self._Type = None
        self._CommandId = None
        self._Username = None
        self._Parameters = None
        self._InstanceIds = None
        self._ScheduleSettings = None

    @property
    def InvokerId(self):
        """待修改的执行器ID。

可通过 [DescribeInvokers(查询执行器)](https://cloud.tencent.com/document/api/1340/61759) 接口获取。
        :rtype: str
        """
        return self._InvokerId

    @InvokerId.setter
    def InvokerId(self, InvokerId):
        self._InvokerId = InvokerId

    @property
    def Name(self):
        """待修改的执行器名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Type(self):
        """执行器类型，当前仅支持周期类型执行器，取值：`SCHEDULE` 。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CommandId(self):
        """待修改的命令ID。

可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Username(self):
        """待修改的用户名。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def Parameters(self):
        """待修改的自定义参数。

仅在 CommandId 所指命令的 EnableParameter 为 true 时，才允许设置此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def InstanceIds(self):
        """待修改的实例ID列表。列表长度上限100。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：CVM、Lighthouse、TAT 托管实例。

实例需要安装 TAT 客户端, 且客户端为 Online 状态。可通过 [DescribeAutomationAgentStatus(查询客户端状态)](https://cloud.tencent.com/document/api/1340/52682) 接口查询客户端状态。
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ScheduleSettings(self):
        """待修改的周期执行器设置。
        :rtype: :class:`tencentcloud.tat.v20201028.models.ScheduleSettings`
        """
        return self._ScheduleSettings

    @ScheduleSettings.setter
    def ScheduleSettings(self, ScheduleSettings):
        self._ScheduleSettings = ScheduleSettings


    def _deserialize(self, params):
        self._InvokerId = params.get("InvokerId")
        self._Name = params.get("Name")
        self._Type = params.get("Type")
        self._CommandId = params.get("CommandId")
        self._Username = params.get("Username")
        self._Parameters = params.get("Parameters")
        self._InstanceIds = params.get("InstanceIds")
        if params.get("ScheduleSettings") is not None:
            self._ScheduleSettings = ScheduleSettings()
            self._ScheduleSettings._deserialize(params.get("ScheduleSettings"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInvokerResponse(AbstractModel):
    """ModifyInvoker返回参数结构体

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


class ModifyRegisterInstanceRequest(AbstractModel):
    """ModifyRegisterInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 托管实例ID。

可通过 [DescribeRegisterInstances(查询托管实例)](https://cloud.tencent.com/document/api/1340/96924) 接口获取。
        :type InstanceId: str
        :param _InstanceName: 实例名称。有效长度为 1～60 字符。
        :type InstanceName: str
        """
        self._InstanceId = None
        self._InstanceName = None

    @property
    def InstanceId(self):
        """托管实例ID。

可通过 [DescribeRegisterInstances(查询托管实例)](https://cloud.tencent.com/document/api/1340/96924) 接口获取。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """实例名称。有效长度为 1～60 字符。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRegisterInstanceResponse(AbstractModel):
    """ModifyRegisterInstance返回参数结构体

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


class PreviewReplacedCommandContentRequest(AbstractModel):
    """PreviewReplacedCommandContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Parameters: 本次预览采用的自定义参数。字段类型为 json encoded string，如：{"varA": "222"}。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
如果有设置过 DefaultParameters 或 DefaultParameterConfs，会与 Parameters 进行叠加，优先使用 Parameters 的值。

key 为自定义参数名称，value 为该参数的取值。kv 均为字符串型。
自定义参数最多 20 个。
自定义参数名称需符合以下规范：字符数目上限 64，可选范围【a-zA-Z0-9-_】。
如果将预览的 CommandId 设置过 DefaultParameters，本参数可以为空。
        :type Parameters: str
        :param _CommandId: 要进行替换预览的命令。
可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
CommandId 与 Content，必须且只能提供一个。
        :type CommandId: str
        :param _Content: 要预览的命令内容，经 Base64 编码，长度不可超过 64KB。
CommandId 与 Content，必须且只能提供一个。
        :type Content: str
        """
        self._Parameters = None
        self._CommandId = None
        self._Content = None

    @property
    def Parameters(self):
        """本次预览采用的自定义参数。字段类型为 json encoded string，如：{"varA": "222"}。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取命令的 EnableParameter 设置。
如果有设置过 DefaultParameters 或 DefaultParameterConfs，会与 Parameters 进行叠加，优先使用 Parameters 的值。

key 为自定义参数名称，value 为该参数的取值。kv 均为字符串型。
自定义参数最多 20 个。
自定义参数名称需符合以下规范：字符数目上限 64，可选范围【a-zA-Z0-9-_】。
如果将预览的 CommandId 设置过 DefaultParameters，本参数可以为空。
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def CommandId(self):
        """要进行替换预览的命令。
可通过 [DescribeCommands(查询命令详情)](https://cloud.tencent.com/document/api/1340/52681) 接口获取。
CommandId 与 Content，必须且只能提供一个。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def Content(self):
        """要预览的命令内容，经 Base64 编码，长度不可超过 64KB。
CommandId 与 Content，必须且只能提供一个。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Parameters = params.get("Parameters")
        self._CommandId = params.get("CommandId")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreviewReplacedCommandContentResponse(AbstractModel):
    """PreviewReplacedCommandContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReplacedContent: 自定义参数替换后的，经Base64编码的命令内容。
        :type ReplacedContent: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReplacedContent = None
        self._RequestId = None

    @property
    def ReplacedContent(self):
        """自定义参数替换后的，经Base64编码的命令内容。
        :rtype: str
        """
        return self._ReplacedContent

    @ReplacedContent.setter
    def ReplacedContent(self, ReplacedContent):
        self._ReplacedContent = ReplacedContent

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
        self._ReplacedContent = params.get("ReplacedContent")
        self._RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """描述单个地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域名称，例如，ap-guangzhou
        :type Region: str
        :param _RegionName: 地域描述，例如: 广州
        :type RegionName: str
        :param _RegionState: 地域是否可用状态，AVAILABLE 代表可用，UNAVAILABLE 代表不可用。
        :type RegionState: str
        """
        self._Region = None
        self._RegionName = None
        self._RegionState = None

    @property
    def Region(self):
        """地域名称，例如，ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def RegionName(self):
        """地域描述，例如: 广州
        :rtype: str
        """
        return self._RegionName

    @RegionName.setter
    def RegionName(self, RegionName):
        self._RegionName = RegionName

    @property
    def RegionState(self):
        """地域是否可用状态，AVAILABLE 代表可用，UNAVAILABLE 代表不可用。
        :rtype: str
        """
        return self._RegionState

    @RegionState.setter
    def RegionState(self, RegionState):
        self._RegionState = RegionState


    def _deserialize(self, params):
        self._Region = params.get("Region")
        self._RegionName = params.get("RegionName")
        self._RegionState = params.get("RegionState")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterCodeInfo(AbstractModel):
    """注册码信息。

    """

    def __init__(self):
        r"""
        :param _RegisterCodeId: 注册码ID。
        :type RegisterCodeId: str
        :param _Description: 注册码描述。
        :type Description: str
        :param _InstanceNamePrefix: 注册实例名称前缀。
        :type InstanceNamePrefix: str
        :param _RegisterLimit: 该注册码允许注册的实例数目。
        :type RegisterLimit: int
        :param _ExpiredTime: 该注册码的过期时间，按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpiredTime: str
        :param _IpAddressRange: 该注册码限制tat_agent只能从IpAddressRange所描述公网出口进行注册。
        :type IpAddressRange: str
        :param _Enabled: 该注册码是否可用。
        :type Enabled: bool
        :param _RegisteredCount: 该注册码已注册数目。
        :type RegisteredCount: int
        :param _CreatedTime: 注册码创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatedTime: str
        :param _UpdatedTime: 注册码最近一次更新时间，按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdatedTime: str
        """
        self._RegisterCodeId = None
        self._Description = None
        self._InstanceNamePrefix = None
        self._RegisterLimit = None
        self._ExpiredTime = None
        self._IpAddressRange = None
        self._Enabled = None
        self._RegisteredCount = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def RegisterCodeId(self):
        """注册码ID。
        :rtype: str
        """
        return self._RegisterCodeId

    @RegisterCodeId.setter
    def RegisterCodeId(self, RegisterCodeId):
        self._RegisterCodeId = RegisterCodeId

    @property
    def Description(self):
        """注册码描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def InstanceNamePrefix(self):
        """注册实例名称前缀。
        :rtype: str
        """
        return self._InstanceNamePrefix

    @InstanceNamePrefix.setter
    def InstanceNamePrefix(self, InstanceNamePrefix):
        self._InstanceNamePrefix = InstanceNamePrefix

    @property
    def RegisterLimit(self):
        """该注册码允许注册的实例数目。
        :rtype: int
        """
        return self._RegisterLimit

    @RegisterLimit.setter
    def RegisterLimit(self, RegisterLimit):
        self._RegisterLimit = RegisterLimit

    @property
    def ExpiredTime(self):
        """该注册码的过期时间，按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def IpAddressRange(self):
        """该注册码限制tat_agent只能从IpAddressRange所描述公网出口进行注册。
        :rtype: str
        """
        return self._IpAddressRange

    @IpAddressRange.setter
    def IpAddressRange(self, IpAddressRange):
        self._IpAddressRange = IpAddressRange

    @property
    def Enabled(self):
        """该注册码是否可用。
        :rtype: bool
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def RegisteredCount(self):
        """该注册码已注册数目。
        :rtype: int
        """
        return self._RegisteredCount

    @RegisteredCount.setter
    def RegisteredCount(self, RegisteredCount):
        self._RegisteredCount = RegisteredCount

    @property
    def CreatedTime(self):
        """注册码创建时间，按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """注册码最近一次更新时间，按照 ISO8601 标准表示，并且使用 UTC 时间。 
格式为： YYYY-MM-DDThh:mm:ssZ。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._RegisterCodeId = params.get("RegisterCodeId")
        self._Description = params.get("Description")
        self._InstanceNamePrefix = params.get("InstanceNamePrefix")
        self._RegisterLimit = params.get("RegisterLimit")
        self._ExpiredTime = params.get("ExpiredTime")
        self._IpAddressRange = params.get("IpAddressRange")
        self._Enabled = params.get("Enabled")
        self._RegisteredCount = params.get("RegisteredCount")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegisterInstanceInfo(AbstractModel):
    """注册实例信息。

    """

    def __init__(self):
        r"""
        :param _RegisterCodeId: 注册码ID。
        :type RegisterCodeId: str
        :param _InstanceId: 托管实例ID。
        :type InstanceId: str
        :param _InstanceName: 托管实例名。
        :type InstanceName: str
        :param _MachineId: 机器ID。
        :type MachineId: str
        :param _SystemName: 系统名。取值：Linux | Windows。
        :type SystemName: str
        :param _HostName: 主机名。
        :type HostName: str
        :param _LocalIp: 内网IP。
        :type LocalIp: str
        :param _PublicKey: 公钥。
        :type PublicKey: str
        :param _Status: 托管状态。
返回Online表示实例正在托管，返回Offline表示实例未托管。
        :type Status: str
        :param _CreatedTime: 创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type CreatedTime: str
        :param _UpdatedTime: 上次更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type UpdatedTime: str
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._RegisterCodeId = None
        self._InstanceId = None
        self._InstanceName = None
        self._MachineId = None
        self._SystemName = None
        self._HostName = None
        self._LocalIp = None
        self._PublicKey = None
        self._Status = None
        self._CreatedTime = None
        self._UpdatedTime = None
        self._Tags = None

    @property
    def RegisterCodeId(self):
        """注册码ID。
        :rtype: str
        """
        return self._RegisterCodeId

    @RegisterCodeId.setter
    def RegisterCodeId(self, RegisterCodeId):
        self._RegisterCodeId = RegisterCodeId

    @property
    def InstanceId(self):
        """托管实例ID。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """托管实例名。
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def MachineId(self):
        """机器ID。
        :rtype: str
        """
        return self._MachineId

    @MachineId.setter
    def MachineId(self, MachineId):
        self._MachineId = MachineId

    @property
    def SystemName(self):
        """系统名。取值：Linux | Windows。
        :rtype: str
        """
        return self._SystemName

    @SystemName.setter
    def SystemName(self, SystemName):
        self._SystemName = SystemName

    @property
    def HostName(self):
        """主机名。
        :rtype: str
        """
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def LocalIp(self):
        """内网IP。
        :rtype: str
        """
        return self._LocalIp

    @LocalIp.setter
    def LocalIp(self, LocalIp):
        self._LocalIp = LocalIp

    @property
    def PublicKey(self):
        """公钥。
        :rtype: str
        """
        return self._PublicKey

    @PublicKey.setter
    def PublicKey(self, PublicKey):
        self._PublicKey = PublicKey

    @property
    def Status(self):
        """托管状态。
返回Online表示实例正在托管，返回Offline表示实例未托管。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        """创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """上次更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime

    @property
    def Tags(self):
        """标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._RegisterCodeId = params.get("RegisterCodeId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._MachineId = params.get("MachineId")
        self._SystemName = params.get("SystemName")
        self._HostName = params.get("HostName")
        self._LocalIp = params.get("LocalIp")
        self._PublicKey = params.get("PublicKey")
        self._Status = params.get("Status")
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
        


class RunCommandRequest(AbstractModel):
    """RunCommand请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: Base64编码后的命令内容，长度不可超过64KB。
        :type Content: str
        :param _InstanceIds: 待执行命令的实例ID列表，上限200。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：
- CVM
- Lighthouse
- TAT 托管实例
        :type InstanceIds: list of str
        :param _CommandName: 命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :type CommandName: str
        :param _Description: 命令描述。不超过120字符。
        :type Description: str
        :param _CommandType: 命令类型，目前支持取值：SHELL、POWERSHELL、BAT。默认：SHELL。
        :type CommandType: str
        :param _WorkingDirectory: 命令执行路径，对于 SHELL 命令默认为 /root，对于 POWERSHELL 命令默认为 C:\Program Files\qcloud\tat_agent\workdir。
        :type WorkingDirectory: str
        :param _Timeout: 命令超时时间，默认60秒。取值范围[1, 86400]。
        :type Timeout: int
        :param _SaveCommand: 是否保存命令，取值范围：
<li> true：保存</li>
<li> false：不保存</li>
默认为 false。
        :type SaveCommand: bool
        :param _EnableParameter: 是否启用自定义参数功能。
一旦创建，此值不提供修改。
取值范围：
<li> true：启用 </li>
<li> false：不启用 </li>
默认值：false。 
        :type EnableParameter: bool
        :param _DefaultParameters: 启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
如果 Parameters 未提供，将使用这里的默认值进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type DefaultParameters: str
        :param _DefaultParameterConfs: 自定义参数数组。 如果 Parameters 未提供，将使用这里的默认值进行替换。 自定义参数最多20个。
如果 Parameters 未提供，将使用这里的默认值进行替换。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
        :type DefaultParameterConfs: list of DefaultParameterConf
        :param _Parameters: Command 的自定义参数。字段类型为json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。
如果未提供该参数取值，将使用 DefaultParameters 或 DefaultParameterConfs 进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :type Parameters: str
        :param _Tags: 如果保存命令，可为命令设置标签。列表长度不超过10。
        :type Tags: list of Tag
        :param _Username: 在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。默认情况下，在 Linux 实例中以 root 用户执行命令；在Windows 实例中以 System 用户执行命令。
        :type Username: str
        :param _OutputCOSBucketUrl: 指定日志上传的cos bucket 地址，必须以https开头，如 https://BucketName-123454321.cos.ap-beijing.myqcloud.com。
        :type OutputCOSBucketUrl: str
        :param _OutputCOSKeyPrefix: 指定日志在cos bucket中的目录，目录命名有如下规则：
1. 可用数字、中英文和可见字符的组合，长度最多为60。
2. 用 / 分割路径，可快速创建子目录。
3. 不允许连续 / ；不允许以 / 开头；不允许以..作为文件夹名称。
        :type OutputCOSKeyPrefix: str
        """
        self._Content = None
        self._InstanceIds = None
        self._CommandName = None
        self._Description = None
        self._CommandType = None
        self._WorkingDirectory = None
        self._Timeout = None
        self._SaveCommand = None
        self._EnableParameter = None
        self._DefaultParameters = None
        self._DefaultParameterConfs = None
        self._Parameters = None
        self._Tags = None
        self._Username = None
        self._OutputCOSBucketUrl = None
        self._OutputCOSKeyPrefix = None

    @property
    def Content(self):
        """Base64编码后的命令内容，长度不可超过64KB。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def InstanceIds(self):
        """待执行命令的实例ID列表，上限200。

可通过对应云产品的查询实例接口获取实例 ID。目前支持实例类型：
- CVM
- Lighthouse
- TAT 托管实例
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def CommandName(self):
        """命令名称。名称仅支持中文、英文、数字、下划线、分隔符"-"、小数点，最大长度不能超60个字节。
        :rtype: str
        """
        return self._CommandName

    @CommandName.setter
    def CommandName(self, CommandName):
        self._CommandName = CommandName

    @property
    def Description(self):
        """命令描述。不超过120字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def CommandType(self):
        """命令类型，目前支持取值：SHELL、POWERSHELL、BAT。默认：SHELL。
        :rtype: str
        """
        return self._CommandType

    @CommandType.setter
    def CommandType(self, CommandType):
        self._CommandType = CommandType

    @property
    def WorkingDirectory(self):
        """命令执行路径，对于 SHELL 命令默认为 /root，对于 POWERSHELL 命令默认为 C:\Program Files\qcloud\tat_agent\workdir。
        :rtype: str
        """
        return self._WorkingDirectory

    @WorkingDirectory.setter
    def WorkingDirectory(self, WorkingDirectory):
        self._WorkingDirectory = WorkingDirectory

    @property
    def Timeout(self):
        """命令超时时间，默认60秒。取值范围[1, 86400]。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def SaveCommand(self):
        """是否保存命令，取值范围：
<li> true：保存</li>
<li> false：不保存</li>
默认为 false。
        :rtype: bool
        """
        return self._SaveCommand

    @SaveCommand.setter
    def SaveCommand(self, SaveCommand):
        self._SaveCommand = SaveCommand

    @property
    def EnableParameter(self):
        """是否启用自定义参数功能。
一旦创建，此值不提供修改。
取值范围：
<li> true：启用 </li>
<li> false：不启用 </li>
默认值：false。 
        :rtype: bool
        """
        return self._EnableParameter

    @EnableParameter.setter
    def EnableParameter(self, EnableParameter):
        self._EnableParameter = EnableParameter

    @property
    def DefaultParameters(self):
        """启用自定义参数功能时，自定义参数的默认取值。字段类型为json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
如果 Parameters 未提供，将使用这里的默认值进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :rtype: str
        """
        return self._DefaultParameters

    @DefaultParameters.setter
    def DefaultParameters(self, DefaultParameters):
        self._DefaultParameters = DefaultParameters

    @property
    def DefaultParameterConfs(self):
        """自定义参数数组。 如果 Parameters 未提供，将使用这里的默认值进行替换。 自定义参数最多20个。
如果 Parameters 未提供，将使用这里的默认值进行替换。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。
参数不支持同时指定 `DefaultParameters` 和 `DefaultParameterConfs` 。
        :rtype: list of DefaultParameterConf
        """
        return self._DefaultParameterConfs

    @DefaultParameterConfs.setter
    def DefaultParameterConfs(self, DefaultParameterConfs):
        self._DefaultParameterConfs = DefaultParameterConfs

    @property
    def Parameters(self):
        """Command 的自定义参数。字段类型为json encoded string。如：{"varA": "222"}。
key为自定义参数名称，value为该参数的默认取值。kv均为字符串型。
仅在命令的 EnableParameter 为 true 时，才允许设置此参数。
如果未提供该参数取值，将使用 DefaultParameters 或 DefaultParameterConfs 进行替换。
自定义参数最多20个。
自定义参数名称需符合以下规范：字符数目上限64，可选范围【a-zA-Z0-9-_】。
        :rtype: str
        """
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Tags(self):
        """如果保存命令，可为命令设置标签。列表长度不超过10。
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def Username(self):
        """在 CVM 或 Lighthouse 实例中执行命令的用户名称。
使用最小权限执行命令是权限管理的最佳实践，建议您以普通用户身份执行云助手命令。默认情况下，在 Linux 实例中以 root 用户执行命令；在Windows 实例中以 System 用户执行命令。
        :rtype: str
        """
        return self._Username

    @Username.setter
    def Username(self, Username):
        self._Username = Username

    @property
    def OutputCOSBucketUrl(self):
        """指定日志上传的cos bucket 地址，必须以https开头，如 https://BucketName-123454321.cos.ap-beijing.myqcloud.com。
        :rtype: str
        """
        return self._OutputCOSBucketUrl

    @OutputCOSBucketUrl.setter
    def OutputCOSBucketUrl(self, OutputCOSBucketUrl):
        self._OutputCOSBucketUrl = OutputCOSBucketUrl

    @property
    def OutputCOSKeyPrefix(self):
        """指定日志在cos bucket中的目录，目录命名有如下规则：
1. 可用数字、中英文和可见字符的组合，长度最多为60。
2. 用 / 分割路径，可快速创建子目录。
3. 不允许连续 / ；不允许以 / 开头；不允许以..作为文件夹名称。
        :rtype: str
        """
        return self._OutputCOSKeyPrefix

    @OutputCOSKeyPrefix.setter
    def OutputCOSKeyPrefix(self, OutputCOSKeyPrefix):
        self._OutputCOSKeyPrefix = OutputCOSKeyPrefix


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._InstanceIds = params.get("InstanceIds")
        self._CommandName = params.get("CommandName")
        self._Description = params.get("Description")
        self._CommandType = params.get("CommandType")
        self._WorkingDirectory = params.get("WorkingDirectory")
        self._Timeout = params.get("Timeout")
        self._SaveCommand = params.get("SaveCommand")
        self._EnableParameter = params.get("EnableParameter")
        self._DefaultParameters = params.get("DefaultParameters")
        if params.get("DefaultParameterConfs") is not None:
            self._DefaultParameterConfs = []
            for item in params.get("DefaultParameterConfs"):
                obj = DefaultParameterConf()
                obj._deserialize(item)
                self._DefaultParameterConfs.append(obj)
        self._Parameters = params.get("Parameters")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._Username = params.get("Username")
        self._OutputCOSBucketUrl = params.get("OutputCOSBucketUrl")
        self._OutputCOSKeyPrefix = params.get("OutputCOSKeyPrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunCommandResponse(AbstractModel):
    """RunCommand返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CommandId: 命令ID。
        :type CommandId: str
        :param _InvocationId: 执行活动ID。
        :type InvocationId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CommandId = None
        self._InvocationId = None
        self._RequestId = None

    @property
    def CommandId(self):
        """命令ID。
        :rtype: str
        """
        return self._CommandId

    @CommandId.setter
    def CommandId(self, CommandId):
        self._CommandId = CommandId

    @property
    def InvocationId(self):
        """执行活动ID。
        :rtype: str
        """
        return self._InvocationId

    @InvocationId.setter
    def InvocationId(self, InvocationId):
        self._InvocationId = InvocationId

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
        self._CommandId = params.get("CommandId")
        self._InvocationId = params.get("InvocationId")
        self._RequestId = params.get("RequestId")


class Scene(AbstractModel):
    """场景详情。

    """

    def __init__(self):
        r"""
        :param _SceneId: 场景 ID 。
        :type SceneId: str
        :param _SceneName: 场景名称。
        :type SceneName: str
        :param _CreatedBy: 场景创建者。

- TAT：公共场景
        :type CreatedBy: str
        :param _CreatedTime: 创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :type UpdatedTime: str
        """
        self._SceneId = None
        self._SceneName = None
        self._CreatedBy = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def SceneId(self):
        """场景 ID 。
        :rtype: str
        """
        return self._SceneId

    @SceneId.setter
    def SceneId(self, SceneId):
        self._SceneId = SceneId

    @property
    def SceneName(self):
        """场景名称。
        :rtype: str
        """
        return self._SceneName

    @SceneName.setter
    def SceneName(self, SceneName):
        self._SceneName = SceneName

    @property
    def CreatedBy(self):
        """场景创建者。

- TAT：公共场景
        :rtype: str
        """
        return self._CreatedBy

    @CreatedBy.setter
    def CreatedBy(self, CreatedBy):
        self._CreatedBy = CreatedBy

    @property
    def CreatedTime(self):
        """创建时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        """更新时间。格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._SceneId = params.get("SceneId")
        self._SceneName = params.get("SceneName")
        self._CreatedBy = params.get("CreatedBy")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScheduleSettings(AbstractModel):
    """周期执行器设置。

    """

    def __init__(self):
        r"""
        :param _Policy: 执行策略：
- ONCE：单次执行
- RECURRENCE：周期执行

只有在 CreateInvoker 时才必填，ModifyInvoker 时为非必填
        :type Policy: str
        :param _Recurrence: 触发 Crontab 表达式。Policy 为 RECURRENCE 时，需要指定此字段。Crontab 按北京时间解析。
        :type Recurrence: str
        :param _InvokeTime: 执行器下次执行时间。Policy 为 ONCE 时，需要指定此字段。

时间格式为：YYYY-MM-DDThh:mm:ssZ
        :type InvokeTime: str
        """
        self._Policy = None
        self._Recurrence = None
        self._InvokeTime = None

    @property
    def Policy(self):
        """执行策略：
- ONCE：单次执行
- RECURRENCE：周期执行

只有在 CreateInvoker 时才必填，ModifyInvoker 时为非必填
        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def Recurrence(self):
        """触发 Crontab 表达式。Policy 为 RECURRENCE 时，需要指定此字段。Crontab 按北京时间解析。
        :rtype: str
        """
        return self._Recurrence

    @Recurrence.setter
    def Recurrence(self, Recurrence):
        self._Recurrence = Recurrence

    @property
    def InvokeTime(self):
        """执行器下次执行时间。Policy 为 ONCE 时，需要指定此字段。

时间格式为：YYYY-MM-DDThh:mm:ssZ
        :rtype: str
        """
        return self._InvokeTime

    @InvokeTime.setter
    def InvokeTime(self, InvokeTime):
        self._InvokeTime = InvokeTime


    def _deserialize(self, params):
        self._Policy = params.get("Policy")
        self._Recurrence = params.get("Recurrence")
        self._InvokeTime = params.get("InvokeTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签

    """

    def __init__(self):
        r"""
        :param _Key: 标签键。
        :type Key: str
        :param _Value: 标签值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """标签键。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """标签值。
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
        


class TaskResult(AbstractModel):
    """任务结果。

    """

    def __init__(self):
        r"""
        :param _ExitCode: 命令执行ExitCode。
        :type ExitCode: int
        :param _Output: Base64编码后的命令输出。最大长度24KB。
        :type Output: str
        :param _ExecStartTime: 命令执行开始时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecStartTime: str
        :param _ExecEndTime: 命令执行结束时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :type ExecEndTime: str
        :param _Dropped: 命令最终输出被截断的字节数。
        :type Dropped: int
        :param _OutputUrl: 日志在cos中的地址
        :type OutputUrl: str
        :param _OutputUploadCOSErrorInfo: 日志上传cos的错误信息。
        :type OutputUploadCOSErrorInfo: str
        """
        self._ExitCode = None
        self._Output = None
        self._ExecStartTime = None
        self._ExecEndTime = None
        self._Dropped = None
        self._OutputUrl = None
        self._OutputUploadCOSErrorInfo = None

    @property
    def ExitCode(self):
        """命令执行ExitCode。
        :rtype: int
        """
        return self._ExitCode

    @ExitCode.setter
    def ExitCode(self, ExitCode):
        self._ExitCode = ExitCode

    @property
    def Output(self):
        """Base64编码后的命令输出。最大长度24KB。
        :rtype: str
        """
        return self._Output

    @Output.setter
    def Output(self, Output):
        self._Output = Output

    @property
    def ExecStartTime(self):
        """命令执行开始时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecStartTime

    @ExecStartTime.setter
    def ExecStartTime(self, ExecStartTime):
        self._ExecStartTime = ExecStartTime

    @property
    def ExecEndTime(self):
        """命令执行结束时间。格式为：YYYY-MM-DDThh:mm:ssZ
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExecEndTime

    @ExecEndTime.setter
    def ExecEndTime(self, ExecEndTime):
        self._ExecEndTime = ExecEndTime

    @property
    def Dropped(self):
        """命令最终输出被截断的字节数。
        :rtype: int
        """
        return self._Dropped

    @Dropped.setter
    def Dropped(self, Dropped):
        self._Dropped = Dropped

    @property
    def OutputUrl(self):
        """日志在cos中的地址
        :rtype: str
        """
        return self._OutputUrl

    @OutputUrl.setter
    def OutputUrl(self, OutputUrl):
        self._OutputUrl = OutputUrl

    @property
    def OutputUploadCOSErrorInfo(self):
        """日志上传cos的错误信息。
        :rtype: str
        """
        return self._OutputUploadCOSErrorInfo

    @OutputUploadCOSErrorInfo.setter
    def OutputUploadCOSErrorInfo(self, OutputUploadCOSErrorInfo):
        self._OutputUploadCOSErrorInfo = OutputUploadCOSErrorInfo


    def _deserialize(self, params):
        self._ExitCode = params.get("ExitCode")
        self._Output = params.get("Output")
        self._ExecStartTime = params.get("ExecStartTime")
        self._ExecEndTime = params.get("ExecEndTime")
        self._Dropped = params.get("Dropped")
        self._OutputUrl = params.get("OutputUrl")
        self._OutputUploadCOSErrorInfo = params.get("OutputUploadCOSErrorInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        