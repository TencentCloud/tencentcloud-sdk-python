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
        


class AcquireSandboxInstanceTokenRequest(AbstractModel):
    r"""AcquireSandboxInstanceToken请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 沙箱实例ID，生成的访问Token将仅可用于访问此沙箱实例
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        r"""沙箱实例ID，生成的访问Token将仅可用于访问此沙箱实例
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
        :param _Token: 访问Token
        :type Token: str
        :param _ExpiresAt: 过期时间
        :type ExpiresAt: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Token = None
        self._ExpiresAt = None
        self._RequestId = None

    @property
    def Token(self):
        r"""访问Token
        :rtype: str
        """
        return self._Token

    @Token.setter
    def Token(self, Token):
        self._Token = Token

    @property
    def ExpiresAt(self):
        r"""过期时间
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


class CreateSandboxToolRequest(AbstractModel):
    r"""CreateSandboxTool请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ToolName: 沙箱工具名称，长度 1-50 字符，支持英文、数字、下划线和连接线。同一 AppId 下沙箱工具名称必须唯一
        :type ToolName: str
        :param _ToolType: 沙箱工具类型，目前支持：browser、code-interpreter
        :type ToolType: str
        :param _NetworkConfiguration: 网络配置
        :type NetworkConfiguration: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        :param _Description: 沙箱工具描述，最大长度 200 字符
        :type Description: str
        :param _DefaultTimeout: 默认超时时间，支持格式：5m、300s、1h 等，不指定则使用系统默认值（5 分钟）。最大 24 小时
        :type DefaultTimeout: str
        :param _Tags: 标签规格，为沙箱工具绑定标签，支持多种资源类型的标签绑定
        :type Tags: list of Tag
        :param _ClientToken: 幂等性 Token，长度不超过 64 字符
        :type ClientToken: str
        """
        self._ToolName = None
        self._ToolType = None
        self._NetworkConfiguration = None
        self._Description = None
        self._DefaultTimeout = None
        self._Tags = None
        self._ClientToken = None

    @property
    def ToolName(self):
        r"""沙箱工具名称，长度 1-50 字符，支持英文、数字、下划线和连接线。同一 AppId 下沙箱工具名称必须唯一
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def ToolType(self):
        r"""沙箱工具类型，目前支持：browser、code-interpreter
        :rtype: str
        """
        return self._ToolType

    @ToolType.setter
    def ToolType(self, ToolType):
        self._ToolType = ToolType

    @property
    def NetworkConfiguration(self):
        r"""网络配置
        :rtype: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        """
        return self._NetworkConfiguration

    @NetworkConfiguration.setter
    def NetworkConfiguration(self, NetworkConfiguration):
        self._NetworkConfiguration = NetworkConfiguration

    @property
    def Description(self):
        r"""沙箱工具描述，最大长度 200 字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DefaultTimeout(self):
        r"""默认超时时间，支持格式：5m、300s、1h 等，不指定则使用系统默认值（5 分钟）。最大 24 小时
        :rtype: str
        """
        return self._DefaultTimeout

    @DefaultTimeout.setter
    def DefaultTimeout(self, DefaultTimeout):
        self._DefaultTimeout = DefaultTimeout

    @property
    def Tags(self):
        r"""标签规格，为沙箱工具绑定标签，支持多种资源类型的标签绑定
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def ClientToken(self):
        r"""幂等性 Token，长度不超过 64 字符
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


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
        :param _ToolId: 创建的沙箱工具 ID
        :type ToolId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ToolId = None
        self._RequestId = None

    @property
    def ToolId(self):
        r"""创建的沙箱工具 ID
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


class DescribeSandboxInstanceListRequest(AbstractModel):
    r"""DescribeSandboxInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIds: 沙箱实例ID列表，指定要查询的实例。如果为空则查询所有实例。最大支持100个ID
        :type InstanceIds: list of str
        :param _ToolId: 沙箱工具ID，指定时查询该沙箱模板下的实例，为空则查询所有沙箱模板的实例
        :type ToolId: str
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为20，最大值为100
        :type Limit: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        """
        self._InstanceIds = None
        self._ToolId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def InstanceIds(self):
        r"""沙箱实例ID列表，指定要查询的实例。如果为空则查询所有实例。最大支持100个ID
        :rtype: list of str
        """
        return self._InstanceIds

    @InstanceIds.setter
    def InstanceIds(self, InstanceIds):
        self._InstanceIds = InstanceIds

    @property
    def ToolId(self):
        r"""沙箱工具ID，指定时查询该沙箱模板下的实例，为空则查询所有沙箱模板的实例
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

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
        :param _InstanceSet: 沙箱实例列表
        :type InstanceSet: list of SandboxInstance
        :param _TotalCount: 符合条件的实例总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceSet(self):
        r"""沙箱实例列表
        :rtype: list of SandboxInstance
        """
        return self._InstanceSet

    @InstanceSet.setter
    def InstanceSet(self, InstanceSet):
        self._InstanceSet = InstanceSet

    @property
    def TotalCount(self):
        r"""符合条件的实例总数
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
        if params.get("InstanceSet") is not None:
            self._InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = SandboxInstance()
                obj._deserialize(item)
                self._InstanceSet.append(obj)
        self._TotalCount = params.get("TotalCount")
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
        


class NetworkConfiguration(AbstractModel):
    r"""沙箱网络配置

    """

    def __init__(self):
        r"""
        :param _NetworkMode: 网络模式（当前支持 PUBLIC）
        :type NetworkMode: str
        """
        self._NetworkMode = None

    @property
    def NetworkMode(self):
        r"""网络模式（当前支持 PUBLIC）
        :rtype: str
        """
        return self._NetworkMode

    @NetworkMode.setter
    def NetworkMode(self, NetworkMode):
        self._NetworkMode = NetworkMode


    def _deserialize(self, params):
        self._NetworkMode = params.get("NetworkMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SandboxInstance(AbstractModel):
    r"""沙箱实例结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 沙箱实例唯一标识符
        :type InstanceId: str
        :param _ToolId: 所属沙箱工具 ID
        :type ToolId: str
        :param _ToolName: 所属沙箱工具名称
        :type ToolName: str
        :param _Status: 实例状态：STARTING（启动中）、RUNNING（运行中）、STOPPING（停止中）、STOPPED（已停止）、STOP_FAILED（停止失败）、FAILED（失败状态）
        :type Status: str
        :param _TimeoutSeconds: 超时时间（秒），null 表示无超时设置
        :type TimeoutSeconds: int
        :param _ExpiresAt: 过期时间（ISO 8601 格式），null 表示无过期时间
        :type ExpiresAt: str
        :param _StopReason: 停止原因：manual（手动）、timeout（超时）、error（错误）、system（系统），仅在状态为 STOPPED、STOP_FAILED 或 FAILED 时有值。当 provider 停止失败时，状态为 STOP_FAILED，原因为 error
        :type StopReason: str
        :param _CreateTime: 创建时间（ISO 8601 格式）
        :type CreateTime: str
        :param _UpdateTime: 更新时间（ISO 8601 格式）
        :type UpdateTime: str
        """
        self._InstanceId = None
        self._ToolId = None
        self._ToolName = None
        self._Status = None
        self._TimeoutSeconds = None
        self._ExpiresAt = None
        self._StopReason = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def InstanceId(self):
        r"""沙箱实例唯一标识符
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ToolId(self):
        r"""所属沙箱工具 ID
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""所属沙箱工具名称
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def Status(self):
        r"""实例状态：STARTING（启动中）、RUNNING（运行中）、STOPPING（停止中）、STOPPED（已停止）、STOP_FAILED（停止失败）、FAILED（失败状态）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TimeoutSeconds(self):
        r"""超时时间（秒），null 表示无超时设置
        :rtype: int
        """
        return self._TimeoutSeconds

    @TimeoutSeconds.setter
    def TimeoutSeconds(self, TimeoutSeconds):
        self._TimeoutSeconds = TimeoutSeconds

    @property
    def ExpiresAt(self):
        r"""过期时间（ISO 8601 格式），null 表示无过期时间
        :rtype: str
        """
        return self._ExpiresAt

    @ExpiresAt.setter
    def ExpiresAt(self, ExpiresAt):
        self._ExpiresAt = ExpiresAt

    @property
    def StopReason(self):
        r"""停止原因：manual（手动）、timeout（超时）、error（错误）、system（系统），仅在状态为 STOPPED、STOP_FAILED 或 FAILED 时有值。当 provider 停止失败时，状态为 STOP_FAILED，原因为 error
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def CreateTime(self):
        r"""创建时间（ISO 8601 格式）
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间（ISO 8601 格式）
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._Status = params.get("Status")
        self._TimeoutSeconds = params.get("TimeoutSeconds")
        self._ExpiresAt = params.get("ExpiresAt")
        self._StopReason = params.get("StopReason")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
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
        :param _ToolId: 沙箱工具唯一标识符
        :type ToolId: str
        :param _ToolName: 沙箱工具名称，长度 1-50 字符，支持中英文、数字、下划线。同一 AppId 下沙箱工具名称必须唯一
        :type ToolName: str
        :param _ToolType: 沙箱工具类型，取值：browser（浏览器工具）、code-interpreter（代码解释器工具）、computer（计算机控制工具）、mobile（移动设备工具）
        :type ToolType: str
        :param _Status: 沙箱工具状态，取值：CREATING（创建中）、ACTIVE（可用）、DELETING（删除中）、FAILED（失败）
        :type Status: str
        :param _Description: 沙箱工具描述信息，最大长度 200 字符
        :type Description: str
        :param _DefaultTimeoutSeconds: 默认超时时间，支持格式：5m、300s、1h 等，不指定则使用系统默认值（5 分钟）。最大 24 小时
        :type DefaultTimeoutSeconds: int
        :param _NetworkConfiguration: 网络配置
        :type NetworkConfiguration: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        :param _Tags: 标签规格，包含资源标签绑定关系。用于为沙箱工具绑定标签，支持多种资源类型的标签绑定
        :type Tags: list of Tag
        :param _CreateTime: 沙箱工具创建时间，格式：ISO8601
        :type CreateTime: str
        :param _UpdateTime: 沙箱工具更新时间，格式：ISO8601
        :type UpdateTime: str
        """
        self._ToolId = None
        self._ToolName = None
        self._ToolType = None
        self._Status = None
        self._Description = None
        self._DefaultTimeoutSeconds = None
        self._NetworkConfiguration = None
        self._Tags = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def ToolId(self):
        r"""沙箱工具唯一标识符
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""沙箱工具名称，长度 1-50 字符，支持中英文、数字、下划线。同一 AppId 下沙箱工具名称必须唯一
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def ToolType(self):
        r"""沙箱工具类型，取值：browser（浏览器工具）、code-interpreter（代码解释器工具）、computer（计算机控制工具）、mobile（移动设备工具）
        :rtype: str
        """
        return self._ToolType

    @ToolType.setter
    def ToolType(self, ToolType):
        self._ToolType = ToolType

    @property
    def Status(self):
        r"""沙箱工具状态，取值：CREATING（创建中）、ACTIVE（可用）、DELETING（删除中）、FAILED（失败）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Description(self):
        r"""沙箱工具描述信息，最大长度 200 字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def DefaultTimeoutSeconds(self):
        r"""默认超时时间，支持格式：5m、300s、1h 等，不指定则使用系统默认值（5 分钟）。最大 24 小时
        :rtype: int
        """
        return self._DefaultTimeoutSeconds

    @DefaultTimeoutSeconds.setter
    def DefaultTimeoutSeconds(self, DefaultTimeoutSeconds):
        self._DefaultTimeoutSeconds = DefaultTimeoutSeconds

    @property
    def NetworkConfiguration(self):
        r"""网络配置
        :rtype: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        """
        return self._NetworkConfiguration

    @NetworkConfiguration.setter
    def NetworkConfiguration(self, NetworkConfiguration):
        self._NetworkConfiguration = NetworkConfiguration

    @property
    def Tags(self):
        r"""标签规格，包含资源标签绑定关系。用于为沙箱工具绑定标签，支持多种资源类型的标签绑定
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CreateTime(self):
        r"""沙箱工具创建时间，格式：ISO8601
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""沙箱工具更新时间，格式：ISO8601
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._ToolType = params.get("ToolType")
        self._Status = params.get("Status")
        self._Description = params.get("Description")
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
        :param _ToolId: 沙箱工具 ID，与 ToolName 至少有一个要填
        :type ToolId: str
        :param _ToolName: 沙箱工具名称，与 ToolId 至少有一个要填
        :type ToolName: str
        :param _Timeout: 超时时间，超过这个时间就自动回收实例。支持格式：5m、300s、1h 等，默认 5m。最小 30s，最大 24h
        :type Timeout: str
        :param _ClientToken: 幂等性 Token，长度不超过 64 字符
        :type ClientToken: str
        """
        self._ToolId = None
        self._ToolName = None
        self._Timeout = None
        self._ClientToken = None

    @property
    def ToolId(self):
        r"""沙箱工具 ID，与 ToolName 至少有一个要填
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def ToolName(self):
        r"""沙箱工具名称，与 ToolId 至少有一个要填
        :rtype: str
        """
        return self._ToolName

    @ToolName.setter
    def ToolName(self, ToolName):
        self._ToolName = ToolName

    @property
    def Timeout(self):
        r"""超时时间，超过这个时间就自动回收实例。支持格式：5m、300s、1h 等，默认 5m。最小 30s，最大 24h
        :rtype: str
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout

    @property
    def ClientToken(self):
        r"""幂等性 Token，长度不超过 64 字符
        :rtype: str
        """
        return self._ClientToken

    @ClientToken.setter
    def ClientToken(self, ClientToken):
        self._ClientToken = ClientToken


    def _deserialize(self, params):
        self._ToolId = params.get("ToolId")
        self._ToolName = params.get("ToolName")
        self._Timeout = params.get("Timeout")
        self._ClientToken = params.get("ClientToken")
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
        :param _Instance: 创建的沙箱实例完整信息
        :type Instance: :class:`tencentcloud.ags.v20250920.models.SandboxInstance`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Instance = None
        self._RequestId = None

    @property
    def Instance(self):
        r"""创建的沙箱实例完整信息
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
        


class UpdateSandboxInstanceRequest(AbstractModel):
    r"""UpdateSandboxInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 沙箱实例ID
        :type InstanceId: str
        :param _Timeout: 新的超时时间（从设置时开始重新计算超时），支持格式：5m、300s、1h等。最小30s，最大24h。如果不指定则保持原有超时设置
        :type Timeout: str
        """
        self._InstanceId = None
        self._Timeout = None

    @property
    def InstanceId(self):
        r"""沙箱实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Timeout(self):
        r"""新的超时时间（从设置时开始重新计算超时），支持格式：5m、300s、1h等。最小30s，最大24h。如果不指定则保持原有超时设置
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
        :param _ToolId: 沙箱工具ID
        :type ToolId: str
        :param _Description: 沙箱工具描述，最大长度200字符
        :type Description: str
        :param _NetworkConfiguration: 网络配置
        :type NetworkConfiguration: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        :param _Tags: 标签
        :type Tags: list of Tag
        """
        self._ToolId = None
        self._Description = None
        self._NetworkConfiguration = None
        self._Tags = None

    @property
    def ToolId(self):
        r"""沙箱工具ID
        :rtype: str
        """
        return self._ToolId

    @ToolId.setter
    def ToolId(self, ToolId):
        self._ToolId = ToolId

    @property
    def Description(self):
        r"""沙箱工具描述，最大长度200字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def NetworkConfiguration(self):
        r"""网络配置
        :rtype: :class:`tencentcloud.ags.v20250920.models.NetworkConfiguration`
        """
        return self._NetworkConfiguration

    @NetworkConfiguration.setter
    def NetworkConfiguration(self, NetworkConfiguration):
        self._NetworkConfiguration = NetworkConfiguration

    @property
    def Tags(self):
        r"""标签
        :rtype: list of Tag
        """
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


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