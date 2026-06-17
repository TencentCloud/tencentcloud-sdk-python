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


class ApiKeyDetail(AbstractModel):
    r"""API 密钥详情

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API 密钥 ID。
        :type ApiKeyId: str
        :param _Name: 名称。
        :type Name: str
        :param _ApiKey: API 密钥值。接口返回脱敏值
        :type ApiKey: str
        :param _Remark: 备注。
        :type Remark: str
        :param _Platform: 平台类型。当前支持填值：maas
        :type Platform: str
        :param _Uin: 主账号。
        :type Uin: str
        :param _SubUin: 子账号。
        :type SubUin: str
        :param _Status: 状态。取值：enable（启用）、disable（禁用）。
        :type Status: str
        :param _BindType: 绑定类型。取值：all（全部模型和服务）、model_all_endpoint_custom（全部模型+自定义服务）、model_custom_endpoint_all（自定义模型+全部服务）、model_custom_endpoint_custom（自定义模型+自定义服务）。
        :type BindType: str
        :param _CreateTime: 创建时间。格式：YYYY-MM-DD HH:mm:ss。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。格式：YYYY-MM-DD HH:mm:ss。
        :type UpdateTime: str
        :param _AppId: 应用 ID。
        :type AppId: str
        :param _Editable: 是否可编辑。true 表示可编辑，false 表示不可编辑。
        :type Editable: bool
        :param _BindingItems: 绑定资源列表，区分 endpoint 和 model 类型。
        :type BindingItems: list of BindingItem
        :param _IpWhitelist: IP 白名单列表。支持 IPv4 和 CIDR 格式。空数组表示不限制 IP。
        :type IpWhitelist: list of str
        :param _Creator: 当Platform为maas时该字段为空
        :type Creator: str
        :param _QuotaSet: Token 限额信息多维度列表。未配置限额时不返回该字段。
        :type QuotaSet: list of QuotaInfo
        :param _QuotaStatus: Token 限额状态。空字符串表示未配置任何限额包；active 表示已配置且当前可用；inactive 表示已配置但额度耗尽
        :type QuotaStatus: str
        """
        self._ApiKeyId = None
        self._Name = None
        self._ApiKey = None
        self._Remark = None
        self._Platform = None
        self._Uin = None
        self._SubUin = None
        self._Status = None
        self._BindType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AppId = None
        self._Editable = None
        self._BindingItems = None
        self._IpWhitelist = None
        self._Creator = None
        self._QuotaSet = None
        self._QuotaStatus = None

    @property
    def ApiKeyId(self):
        r"""API 密钥 ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def Name(self):
        r"""名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ApiKey(self):
        r"""API 密钥值。接口返回脱敏值
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Remark(self):
        r"""备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Platform(self):
        r"""平台类型。当前支持填值：maas
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Uin(self):
        r"""主账号。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        r"""子账号。
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def Status(self):
        r"""状态。取值：enable（启用）、disable（禁用）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BindType(self):
        r"""绑定类型。取值：all（全部模型和服务）、model_all_endpoint_custom（全部模型+自定义服务）、model_custom_endpoint_all（自定义模型+全部服务）、model_custom_endpoint_custom（自定义模型+自定义服务）。
        :rtype: str
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def CreateTime(self):
        r"""创建时间。格式：YYYY-MM-DD HH:mm:ss。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间。格式：YYYY-MM-DD HH:mm:ss。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AppId(self):
        r"""应用 ID。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Editable(self):
        r"""是否可编辑。true 表示可编辑，false 表示不可编辑。
        :rtype: bool
        """
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def BindingItems(self):
        r"""绑定资源列表，区分 endpoint 和 model 类型。
        :rtype: list of BindingItem
        """
        return self._BindingItems

    @BindingItems.setter
    def BindingItems(self, BindingItems):
        self._BindingItems = BindingItems

    @property
    def IpWhitelist(self):
        r"""IP 白名单列表。支持 IPv4 和 CIDR 格式。空数组表示不限制 IP。
        :rtype: list of str
        """
        return self._IpWhitelist

    @IpWhitelist.setter
    def IpWhitelist(self, IpWhitelist):
        self._IpWhitelist = IpWhitelist

    @property
    def Creator(self):
        r"""当Platform为maas时该字段为空
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def QuotaSet(self):
        r"""Token 限额信息多维度列表。未配置限额时不返回该字段。
        :rtype: list of QuotaInfo
        """
        return self._QuotaSet

    @QuotaSet.setter
    def QuotaSet(self, QuotaSet):
        self._QuotaSet = QuotaSet

    @property
    def QuotaStatus(self):
        r"""Token 限额状态。空字符串表示未配置任何限额包；active 表示已配置且当前可用；inactive 表示已配置但额度耗尽
        :rtype: str
        """
        return self._QuotaStatus

    @QuotaStatus.setter
    def QuotaStatus(self, QuotaStatus):
        self._QuotaStatus = QuotaStatus


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        self._Name = params.get("Name")
        self._ApiKey = params.get("ApiKey")
        self._Remark = params.get("Remark")
        self._Platform = params.get("Platform")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._Status = params.get("Status")
        self._BindType = params.get("BindType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AppId = params.get("AppId")
        self._Editable = params.get("Editable")
        if params.get("BindingItems") is not None:
            self._BindingItems = []
            for item in params.get("BindingItems"):
                obj = BindingItem()
                obj._deserialize(item)
                self._BindingItems.append(obj)
        self._IpWhitelist = params.get("IpWhitelist")
        self._Creator = params.get("Creator")
        if params.get("QuotaSet") is not None:
            self._QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = QuotaInfo()
                obj._deserialize(item)
                self._QuotaSet.append(obj)
        self._QuotaStatus = params.get("QuotaStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchCreateFailedItem(AbstractModel):
    r"""批量创建失败项

    """

    def __init__(self):
        r"""
        :param _Index: 失败项的序号（从 1 开始，对应后缀编号）。
        :type Index: int
        :param _Name: 失败项的名称。
        :type Name: str
        :param _Reason: 失败原因。
        :type Reason: str
        """
        self._Index = None
        self._Name = None
        self._Reason = None

    @property
    def Index(self):
        r"""失败项的序号（从 1 开始，对应后缀编号）。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Name(self):
        r"""失败项的名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Reason(self):
        r"""失败原因。
        :rtype: str
        """
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Name = params.get("Name")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindingItem(AbstractModel):
    r"""绑定资源项

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源 ID（模型 ID 或服务 ID）。
        :type ResourceId: str
        :param _ResourceType: 资源类型。取值：endpoint（服务）、model（模型）。
        :type ResourceType: str
        :param _Status: 资源状态
        :type Status: str
        """
        self._ResourceId = None
        self._ResourceType = None
        self._Status = None

    @property
    def ResourceId(self):
        r"""资源 ID（模型 ID 或服务 ID）。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceType(self):
        r"""资源类型。取值：endpoint（服务）、model（模型）。
        :rtype: str
        """
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        r"""资源状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateApiKeysResultItem(AbstractModel):
    r"""批量创建成功项

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: APIKey ID。
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""APIKey ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlossaryEntriesRequest(AbstractModel):
    r"""CreateGlossaryEntries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlossaryId: 术语库 ID。可通过 DescribeGlossaries 接口获取。
        :type GlossaryId: str
        :param _Entries: 术语条目列表。单次最多 100 个。
        :type Entries: list of GlossaryEntryInput
        """
        self._GlossaryId = None
        self._Entries = None

    @property
    def GlossaryId(self):
        r"""术语库 ID。可通过 DescribeGlossaries 接口获取。
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Entries(self):
        r"""术语条目列表。单次最多 100 个。
        :rtype: list of GlossaryEntryInput
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = GlossaryEntryInput()
                obj._deserialize(item)
                self._Entries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlossaryEntriesResponse(AbstractModel):
    r"""CreateGlossaryEntries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Entries: 创建成功的术语条目列表。
        :type Entries: list of GlossaryEntryItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Entries = None
        self._RequestId = None

    @property
    def Entries(self):
        r"""创建成功的术语条目列表。
        :rtype: list of GlossaryEntryItem
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries

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
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = GlossaryEntryItem()
                obj._deserialize(item)
                self._Entries.append(obj)
        self._RequestId = params.get("RequestId")


class CreateGlossaryRequest(AbstractModel):
    r"""CreateGlossary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 术语库名称。最大 50 字符。
        :type Name: str
        :param _Source: 源语言代码。最大 16 字符。例如：zh（中文）、en（英文）。
        :type Source: str
        :param _Target: 目标语言代码。最大 16 字符。例如：zh（中文）、en（英文）。
        :type Target: str
        :param _Description: 术语库描述。最大 255 字符。
        :type Description: str
        """
        self._Name = None
        self._Source = None
        self._Target = None
        self._Description = None

    @property
    def Name(self):
        r"""术语库名称。最大 50 字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Source(self):
        r"""源语言代码。最大 16 字符。例如：zh（中文）、en（英文）。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言代码。最大 16 字符。例如：zh（中文）、en（英文）。
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Description(self):
        r"""术语库描述。最大 255 字符。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateGlossaryResponse(AbstractModel):
    r"""CreateGlossary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GlossaryId: 术语库 ID。
        :type GlossaryId: str
        :param _Name: 术语库名称。
        :type Name: str
        :param _CreatedAt: 创建时间。Unix 时间戳（毫秒）。
        :type CreatedAt: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GlossaryId = None
        self._Name = None
        self._CreatedAt = None
        self._RequestId = None

    @property
    def GlossaryId(self):
        r"""术语库 ID。
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Name(self):
        r"""术语库名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreatedAt(self):
        r"""创建时间。Unix 时间戳（毫秒）。
        :rtype: int
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

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
        self._GlossaryId = params.get("GlossaryId")
        self._Name = params.get("Name")
        self._CreatedAt = params.get("CreatedAt")
        self._RequestId = params.get("RequestId")


class CreateTokenPlanApiKeysRequest(AbstractModel):
    r"""CreateTokenPlanApiKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TeamId: 套餐 ID。可通过DescribeTokenPlanList接口获取。
        :type TeamId: str
        :param _ApiKeyName: API Key 名称，最大 128 字符。如果创建 API Key 的数量超过1个，实际名称格式为 {ApiKeyName}-{序号}（如 mykey-1, mykey-2）。
        :type ApiKeyName: str
        :param _Count: 创建数量。取值范围：1 ~ 10。
        :type Count: int
        :param _AllowedModels: 可用模型列表。如果套餐类型为企业版专业套餐，可以指定模型，也可以传入“all”，传入 “all“表示可以使用套餐支持的所有模型，如果要指定具体模型，传入 Model ID，“all“和具体的 Model ID 不能同时传入，如果不传则表示该API Key不支持任何模型，从而影响API Key的正常使用。如果套餐类型为企业版轻享套餐，则无论是否传入该字段，以及该字段传入什么值，都会被强制覆盖为["auto"]。
        :type AllowedModels: list of str
        :param _ExclusiveQuota: 独占额度。不传则为0，代表该 API Key 不被分配任何独占配额。单位说明如下：
- 套餐类型为专业，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type ExclusiveQuota: int
        :param _TotalQuota: 总额度上限。-1 表示不限，必须为 -1 或 >= API Key 当前的 ExclusiveQuota（独占额度）。不传表示不设置上限。单位说明如下：
- 套餐类型为专业，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type TotalQuota: int
        :param _TPM: TPM（Tokens Per Minute）限制。不传使用套餐级别 TPM。必须 >= 0 且 <= 套餐 TPM。
        :type TPM: int
        """
        self._TeamId = None
        self._ApiKeyName = None
        self._Count = None
        self._AllowedModels = None
        self._ExclusiveQuota = None
        self._TotalQuota = None
        self._TPM = None

    @property
    def TeamId(self):
        r"""套餐 ID。可通过DescribeTokenPlanList接口获取。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def ApiKeyName(self):
        r"""API Key 名称，最大 128 字符。如果创建 API Key 的数量超过1个，实际名称格式为 {ApiKeyName}-{序号}（如 mykey-1, mykey-2）。
        :rtype: str
        """
        return self._ApiKeyName

    @ApiKeyName.setter
    def ApiKeyName(self, ApiKeyName):
        self._ApiKeyName = ApiKeyName

    @property
    def Count(self):
        r"""创建数量。取值范围：1 ~ 10。
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def AllowedModels(self):
        r"""可用模型列表。如果套餐类型为企业版专业套餐，可以指定模型，也可以传入“all”，传入 “all“表示可以使用套餐支持的所有模型，如果要指定具体模型，传入 Model ID，“all“和具体的 Model ID 不能同时传入，如果不传则表示该API Key不支持任何模型，从而影响API Key的正常使用。如果套餐类型为企业版轻享套餐，则无论是否传入该字段，以及该字段传入什么值，都会被强制覆盖为["auto"]。
        :rtype: list of str
        """
        return self._AllowedModels

    @AllowedModels.setter
    def AllowedModels(self, AllowedModels):
        self._AllowedModels = AllowedModels

    @property
    def ExclusiveQuota(self):
        r"""独占额度。不传则为0，代表该 API Key 不被分配任何独占配额。单位说明如下：
- 套餐类型为专业，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: int
        """
        return self._ExclusiveQuota

    @ExclusiveQuota.setter
    def ExclusiveQuota(self, ExclusiveQuota):
        self._ExclusiveQuota = ExclusiveQuota

    @property
    def TotalQuota(self):
        r"""总额度上限。-1 表示不限，必须为 -1 或 >= API Key 当前的 ExclusiveQuota（独占额度）。不传表示不设置上限。单位说明如下：
- 套餐类型为专业，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def TPM(self):
        r"""TPM（Tokens Per Minute）限制。不传使用套餐级别 TPM。必须 >= 0 且 <= 套餐 TPM。
        :rtype: int
        """
        return self._TPM

    @TPM.setter
    def TPM(self, TPM):
        self._TPM = TPM


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._ApiKeyName = params.get("ApiKeyName")
        self._Count = params.get("Count")
        self._AllowedModels = params.get("AllowedModels")
        self._ExclusiveQuota = params.get("ExclusiveQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._TPM = params.get("TPM")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTokenPlanApiKeysResponse(AbstractModel):
    r"""CreateTokenPlanApiKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 成功创建的项列表。
        :type Items: list of CreateApiKeysResultItem
        :param _FailedItems: 创建失败的项列表。
        :type FailedItems: list of BatchCreateFailedItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._FailedItems = None
        self._RequestId = None

    @property
    def Items(self):
        r"""成功创建的项列表。
        :rtype: list of CreateApiKeysResultItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def FailedItems(self):
        r"""创建失败的项列表。
        :rtype: list of BatchCreateFailedItem
        """
        return self._FailedItems

    @FailedItems.setter
    def FailedItems(self, FailedItems):
        self._FailedItems = FailedItems

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = CreateApiKeysResultItem()
                obj._deserialize(item)
                self._Items.append(obj)
        if params.get("FailedItems") is not None:
            self._FailedItems = []
            for item in params.get("FailedItems"):
                obj = BatchCreateFailedItem()
                obj._deserialize(item)
                self._FailedItems.append(obj)
        self._RequestId = params.get("RequestId")


class CreateTokenPlanTeamOrderAndBuyRequest(AbstractModel):
    r"""CreateTokenPlanTeamOrderAndBuy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductType: 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）。
        :type ProductType: str
        :param _TeamName: 套餐名称。只能包含中文、字母、数字、下划线、连字符，以中文或者字母开头，以中文或字母或数字结尾，2~50个字符
        :type TeamName: str
        :param _TimeSpan: 购买时长。单位：月。必须大于 0。
        :type TimeSpan: int
        :param _CreditOrToken: 购买的套餐规格。套餐类型为专业套餐（enterprise），单位取值为积分；轻享套餐（enterprise-auto），单位取值为 tokens。
        :type CreditOrToken: int
        :param _EnableAutoRenew: 是否开启自动续费。默认不开启。
        :type EnableAutoRenew: bool
        """
        self._ProductType = None
        self._TeamName = None
        self._TimeSpan = None
        self._CreditOrToken = None
        self._EnableAutoRenew = None

    @property
    def ProductType(self):
        r"""套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）。
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def TeamName(self):
        r"""套餐名称。只能包含中文、字母、数字、下划线、连字符，以中文或者字母开头，以中文或字母或数字结尾，2~50个字符
        :rtype: str
        """
        return self._TeamName

    @TeamName.setter
    def TeamName(self, TeamName):
        self._TeamName = TeamName

    @property
    def TimeSpan(self):
        r"""购买时长。单位：月。必须大于 0。
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan

    @property
    def CreditOrToken(self):
        r"""购买的套餐规格。套餐类型为专业套餐（enterprise），单位取值为积分；轻享套餐（enterprise-auto），单位取值为 tokens。
        :rtype: int
        """
        return self._CreditOrToken

    @CreditOrToken.setter
    def CreditOrToken(self, CreditOrToken):
        self._CreditOrToken = CreditOrToken

    @property
    def EnableAutoRenew(self):
        r"""是否开启自动续费。默认不开启。
        :rtype: bool
        """
        return self._EnableAutoRenew

    @EnableAutoRenew.setter
    def EnableAutoRenew(self, EnableAutoRenew):
        self._EnableAutoRenew = EnableAutoRenew


    def _deserialize(self, params):
        self._ProductType = params.get("ProductType")
        self._TeamName = params.get("TeamName")
        self._TimeSpan = params.get("TimeSpan")
        self._CreditOrToken = params.get("CreditOrToken")
        self._EnableAutoRenew = params.get("EnableAutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTokenPlanTeamOrderAndBuyResponse(AbstractModel):
    r"""CreateTokenPlanTeamOrderAndBuy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BigOrderId: 腾讯云订单 ID。用于关联一次购买操作下的所有子订单。
        :type BigOrderId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BigOrderId = None
        self._RequestId = None

    @property
    def BigOrderId(self):
        r"""腾讯云订单 ID。用于关联一次购买操作下的所有子订单。
        :rtype: str
        """
        return self._BigOrderId

    @BigOrderId.setter
    def BigOrderId(self, BigOrderId):
        self._BigOrderId = BigOrderId

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
        self._BigOrderId = params.get("BigOrderId")
        self._RequestId = params.get("RequestId")


class DeleteGlossaryEntriesRequest(AbstractModel):
    r"""DeleteGlossaryEntries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlossaryId: 术语库 ID。可通过 DescribeGlossaries 接口获取。
        :type GlossaryId: str
        :param _Entries: 待删除的术语条目列表。单次最多 200 个。
        :type Entries: list of DeleteGlossaryEntryInput
        """
        self._GlossaryId = None
        self._Entries = None

    @property
    def GlossaryId(self):
        r"""术语库 ID。可通过 DescribeGlossaries 接口获取。
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Entries(self):
        r"""待删除的术语条目列表。单次最多 200 个。
        :rtype: list of DeleteGlossaryEntryInput
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = DeleteGlossaryEntryInput()
                obj._deserialize(item)
                self._Entries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlossaryEntriesResponse(AbstractModel):
    r"""DeleteGlossaryEntries返回参数结构体

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


class DeleteGlossaryEntryInput(AbstractModel):
    r"""删除术语条目项

    """

    def __init__(self):
        r"""
        :param _EntryId: 术语条目 ID。可通过 DescribeGlossaryEntries 接口获取。
        :type EntryId: str
        """
        self._EntryId = None

    @property
    def EntryId(self):
        r"""术语条目 ID。可通过 DescribeGlossaryEntries 接口获取。
        :rtype: str
        """
        return self._EntryId

    @EntryId.setter
    def EntryId(self, EntryId):
        self._EntryId = EntryId


    def _deserialize(self, params):
        self._EntryId = params.get("EntryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlossaryRequest(AbstractModel):
    r"""DeleteGlossary请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlossaryId: 术语库 ID。可通过 DescribeGlossaries 接口获取。
        :type GlossaryId: str
        """
        self._GlossaryId = None

    @property
    def GlossaryId(self):
        r"""术语库 ID。可通过 DescribeGlossaries 接口获取。
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteGlossaryResponse(AbstractModel):
    r"""DeleteGlossary返回参数结构体

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


class DeleteTokenPlanApiKeyRequest(AbstractModel):
    r"""DeleteTokenPlanApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID。可通过DescribeTokenPlanApiKeyList接口获取。
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID。可通过DescribeTokenPlanApiKeyList接口获取。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTokenPlanApiKeyResponse(AbstractModel):
    r"""DeleteTokenPlanApiKey返回参数结构体

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


class DescribeApiKeyListRequest(AbstractModel):
    r"""DescribeApiKeyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台类型。当前支持填值：maas
        :type Platform: str
        :param _Limit: 返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量，默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件列表。支持的过滤字段：apikeyId（API 密钥 ID）、apiKeyName（名称）、platform（平台类型）、status（状态）、bindType（绑定类型）。
        :type Filters: list of RequestFilter
        :param _Sorts: 排序条件列表。支持的排序字段：apiKeyName
        :type Sorts: list of RequestSort
        """
        self._Platform = None
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Sorts = None

    @property
    def Platform(self):
        r"""平台类型。当前支持填值：maas
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Limit(self):
        r"""返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""过滤条件列表。支持的过滤字段：apikeyId（API 密钥 ID）、apiKeyName（名称）、platform（平台类型）、status（状态）、bindType（绑定类型）。
        :rtype: list of RequestFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sorts(self):
        r"""排序条件列表。支持的排序字段：apiKeyName
        :rtype: list of RequestSort
        """
        return self._Sorts

    @Sorts.setter
    def Sorts(self, Sorts):
        self._Sorts = Sorts


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RequestFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sorts") is not None:
            self._Sorts = []
            for item in params.get("Sorts"):
                obj = RequestSort()
                obj._deserialize(item)
                self._Sorts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeyListResponse(AbstractModel):
    r"""DescribeApiKeyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeySet: API 密钥列表。
        :type ApiKeySet: list of ApiKeyDetail
        :param _TotalCount: 符合条件的 API 密钥总数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApiKeySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApiKeySet(self):
        r"""API 密钥列表。
        :rtype: list of ApiKeyDetail
        """
        return self._ApiKeySet

    @ApiKeySet.setter
    def ApiKeySet(self, ApiKeySet):
        self._ApiKeySet = ApiKeySet

    @property
    def TotalCount(self):
        r"""符合条件的 API 密钥总数。
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
        if params.get("ApiKeySet") is not None:
            self._ApiKeySet = []
            for item in params.get("ApiKeySet"):
                obj = ApiKeyDetail()
                obj._deserialize(item)
                self._ApiKeySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeApiKeyRequest(AbstractModel):
    r"""DescribeApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Platform: 平台类型。当前支持填值：maas
        :type Platform: str
        :param _ApiKeyId: API 密钥 ID，与 ApiKey 至少需传入其一，优先使用 ApiKeyId。
        :type ApiKeyId: str
        :param _ApiKey: API 密钥明文，与 ApiKeyId 至少需传入其一。
        :type ApiKey: str
        """
        self._Platform = None
        self._ApiKeyId = None
        self._ApiKey = None

    @property
    def Platform(self):
        r"""平台类型。当前支持填值：maas
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def ApiKeyId(self):
        r"""API 密钥 ID，与 ApiKey 至少需传入其一，优先使用 ApiKeyId。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def ApiKey(self):
        r"""API 密钥明文，与 ApiKeyId 至少需传入其一。
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey


    def _deserialize(self, params):
        self._Platform = params.get("Platform")
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKey = params.get("ApiKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeApiKeyResponse(AbstractModel):
    r"""DescribeApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API 密钥 ID。
        :type ApiKeyId: str
        :param _Name: 名称。
        :type Name: str
        :param _ApiKey: API 密钥值（明文）。
        :type ApiKey: str
        :param _Remark: 备注。
        :type Remark: str
        :param _Platform: 平台类型。枚举：maas
        :type Platform: str
        :param _Uin: 主账号。
        :type Uin: str
        :param _SubUin: 子账号。
        :type SubUin: str
        :param _Status: 状态。取值：enable（启用）、disable（禁用）。
        :type Status: str
        :param _BindType: 绑定类型。取值：all（全部模型和接入点）、model_all_endpoint_custom（全部模型+自定义接入点）、model_custom_endpoint_all（自定义模型+全部接入点）、model_custom_endpoint_custom（自定义模型+自定义接入点）。
        :type BindType: str
        :param _CreateTime: 创建时间。格式：YYYY-MM-DD HH:mm:ss。
        :type CreateTime: str
        :param _UpdateTime: 更新时间。格式：YYYY-MM-DD HH:mm:ss。
        :type UpdateTime: str
        :param _AppId: 应用 ID。
        :type AppId: str
        :param _Editable: 是否可编辑。true 表示可编辑，false 表示不可编辑。
        :type Editable: bool
        :param _BindingItems: 绑定资源列表，区分 endpoint 和 model 类型。
        :type BindingItems: list of BindingItem
        :param _IpWhitelist: IP 白名单列表。支持 IPv4和 CIDR 格式。空数组表示不限制 IP。
        :type IpWhitelist: list of str
        :param _Creator: 当Platform为maas时该字段为空
        :type Creator: str
        :param _QuotaSet: Token 限额多维度信息。未配置限额时不返回该字段。
        :type QuotaSet: list of QuotaInfo
        :param _QuotaStatus: Token 限额状态。空字符串表示未配置任何限额包；active 表示已配置且当前可用；inactive 表示已配置但额度耗尽
        :type QuotaStatus: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApiKeyId = None
        self._Name = None
        self._ApiKey = None
        self._Remark = None
        self._Platform = None
        self._Uin = None
        self._SubUin = None
        self._Status = None
        self._BindType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._AppId = None
        self._Editable = None
        self._BindingItems = None
        self._IpWhitelist = None
        self._Creator = None
        self._QuotaSet = None
        self._QuotaStatus = None
        self._RequestId = None

    @property
    def ApiKeyId(self):
        r"""API 密钥 ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def Name(self):
        r"""名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ApiKey(self):
        r"""API 密钥值（明文）。
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Remark(self):
        r"""备注。
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def Platform(self):
        r"""平台类型。枚举：maas
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Uin(self):
        r"""主账号。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def SubUin(self):
        r"""子账号。
        :rtype: str
        """
        return self._SubUin

    @SubUin.setter
    def SubUin(self, SubUin):
        self._SubUin = SubUin

    @property
    def Status(self):
        r"""状态。取值：enable（启用）、disable（禁用）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def BindType(self):
        r"""绑定类型。取值：all（全部模型和接入点）、model_all_endpoint_custom（全部模型+自定义接入点）、model_custom_endpoint_all（自定义模型+全部接入点）、model_custom_endpoint_custom（自定义模型+自定义接入点）。
        :rtype: str
        """
        return self._BindType

    @BindType.setter
    def BindType(self, BindType):
        self._BindType = BindType

    @property
    def CreateTime(self):
        r"""创建时间。格式：YYYY-MM-DD HH:mm:ss。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间。格式：YYYY-MM-DD HH:mm:ss。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AppId(self):
        r"""应用 ID。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Editable(self):
        r"""是否可编辑。true 表示可编辑，false 表示不可编辑。
        :rtype: bool
        """
        return self._Editable

    @Editable.setter
    def Editable(self, Editable):
        self._Editable = Editable

    @property
    def BindingItems(self):
        r"""绑定资源列表，区分 endpoint 和 model 类型。
        :rtype: list of BindingItem
        """
        return self._BindingItems

    @BindingItems.setter
    def BindingItems(self, BindingItems):
        self._BindingItems = BindingItems

    @property
    def IpWhitelist(self):
        r"""IP 白名单列表。支持 IPv4和 CIDR 格式。空数组表示不限制 IP。
        :rtype: list of str
        """
        return self._IpWhitelist

    @IpWhitelist.setter
    def IpWhitelist(self, IpWhitelist):
        self._IpWhitelist = IpWhitelist

    @property
    def Creator(self):
        r"""当Platform为maas时该字段为空
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def QuotaSet(self):
        r"""Token 限额多维度信息。未配置限额时不返回该字段。
        :rtype: list of QuotaInfo
        """
        return self._QuotaSet

    @QuotaSet.setter
    def QuotaSet(self, QuotaSet):
        self._QuotaSet = QuotaSet

    @property
    def QuotaStatus(self):
        r"""Token 限额状态。空字符串表示未配置任何限额包；active 表示已配置且当前可用；inactive 表示已配置但额度耗尽
        :rtype: str
        """
        return self._QuotaStatus

    @QuotaStatus.setter
    def QuotaStatus(self, QuotaStatus):
        self._QuotaStatus = QuotaStatus

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
        self._ApiKeyId = params.get("ApiKeyId")
        self._Name = params.get("Name")
        self._ApiKey = params.get("ApiKey")
        self._Remark = params.get("Remark")
        self._Platform = params.get("Platform")
        self._Uin = params.get("Uin")
        self._SubUin = params.get("SubUin")
        self._Status = params.get("Status")
        self._BindType = params.get("BindType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._AppId = params.get("AppId")
        self._Editable = params.get("Editable")
        if params.get("BindingItems") is not None:
            self._BindingItems = []
            for item in params.get("BindingItems"):
                obj = BindingItem()
                obj._deserialize(item)
                self._BindingItems.append(obj)
        self._IpWhitelist = params.get("IpWhitelist")
        self._Creator = params.get("Creator")
        if params.get("QuotaSet") is not None:
            self._QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = QuotaInfo()
                obj._deserialize(item)
                self._QuotaSet.append(obj)
        self._QuotaStatus = params.get("QuotaStatus")
        self._RequestId = params.get("RequestId")


class DescribeGlossariesRequest(AbstractModel):
    r"""DescribeGlossaries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 返回数量。默认为 20，最大值为 100。
        :type Limit: int
        :param _Offset: 偏移量。默认为 0。
        :type Offset: int
        :param _Filters: 过滤条件列表。支持的过滤字段：GlossaryId（术语库 ID）、Name（名称）、Source（源语言代码）、Target（目标语言代码）。
        :type Filters: list of RequestFilter
        :param _Sorts: 排序条件列表。支持的排序字段：CreatedTime（创建时间）、UpdatedTime（更新时间）。
        :type Sorts: list of RequestSort
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None
        self._Sorts = None

    @property
    def Limit(self):
        r"""返回数量。默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量。默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""过滤条件列表。支持的过滤字段：GlossaryId（术语库 ID）、Name（名称）、Source（源语言代码）、Target（目标语言代码）。
        :rtype: list of RequestFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sorts(self):
        r"""排序条件列表。支持的排序字段：CreatedTime（创建时间）、UpdatedTime（更新时间）。
        :rtype: list of RequestSort
        """
        return self._Sorts

    @Sorts.setter
    def Sorts(self, Sorts):
        self._Sorts = Sorts


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RequestFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sorts") is not None:
            self._Sorts = []
            for item in params.get("Sorts"):
                obj = RequestSort()
                obj._deserialize(item)
                self._Sorts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlossariesResponse(AbstractModel):
    r"""DescribeGlossaries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Items: 术语库列表。
        :type Items: list of GlossaryItem
        :param _TotalCount: 符合条件的术语库总数。
        :type TotalCount: int
        :param _Current: 当前页码。
        :type Current: int
        :param _PageSize: 每页大小。
        :type PageSize: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Items = None
        self._TotalCount = None
        self._Current = None
        self._PageSize = None
        self._RequestId = None

    @property
    def Items(self):
        r"""术语库列表。
        :rtype: list of GlossaryItem
        """
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items

    @property
    def TotalCount(self):
        r"""符合条件的术语库总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Current(self):
        r"""当前页码。
        :rtype: int
        """
        return self._Current

    @Current.setter
    def Current(self, Current):
        self._Current = Current

    @property
    def PageSize(self):
        r"""每页大小。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

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
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = GlossaryItem()
                obj._deserialize(item)
                self._Items.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._Current = params.get("Current")
        self._PageSize = params.get("PageSize")
        self._RequestId = params.get("RequestId")


class DescribeGlossaryEntriesRequest(AbstractModel):
    r"""DescribeGlossaryEntries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlossaryId: 术语库 ID。可通过 DescribeGlossaries 接口获取。
        :type GlossaryId: str
        :param _Page: 页码。默认为 1。
        :type Page: int
        :param _PageSize: 每页大小。默认为 20，最大值为 200。
        :type PageSize: int
        """
        self._GlossaryId = None
        self._Page = None
        self._PageSize = None

    @property
    def GlossaryId(self):
        r"""术语库 ID。可通过 DescribeGlossaries 接口获取。
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Page(self):
        r"""页码。默认为 1。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""每页大小。默认为 20，最大值为 200。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGlossaryEntriesResponse(AbstractModel):
    r"""DescribeGlossaryEntries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Entries: 术语条目列表。
        :type Entries: list of GlossaryEntryItem
        :param _Total: 符合条件的术语条目总数。
        :type Total: int
        :param _Page: 当前页码。
        :type Page: int
        :param _PageSize: 每页大小。
        :type PageSize: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Entries = None
        self._Total = None
        self._Page = None
        self._PageSize = None
        self._RequestId = None

    @property
    def Entries(self):
        r"""术语条目列表。
        :rtype: list of GlossaryEntryItem
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries

    @property
    def Total(self):
        r"""符合条件的术语条目总数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Page(self):
        r"""当前页码。
        :rtype: int
        """
        return self._Page

    @Page.setter
    def Page(self, Page):
        self._Page = Page

    @property
    def PageSize(self):
        r"""每页大小。
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

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
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = GlossaryEntryItem()
                obj._deserialize(item)
                self._Entries.append(obj)
        self._Total = params.get("Total")
        self._Page = params.get("Page")
        self._PageSize = params.get("PageSize")
        self._RequestId = params.get("RequestId")


class DescribeModelListRequest(AbstractModel):
    r"""DescribeModelList请求参数结构体

    """


class DescribeModelListResponse(AbstractModel):
    r"""DescribeModelList返回参数结构体

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


class DescribeTokenPlanApiKeyListRequest(AbstractModel):
    r"""DescribeTokenPlanApiKeyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TeamId: 套餐 ID。可通过DescribeTokenPlanList接口获取。
        :type TeamId: str
        :param _Offset: 分页查询偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 分页查询返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Filters: 分页查询过滤条件列表。支持的过滤字段：ApiKeyId （API Key ID）、Name （API Key 名称）、Status （API Key是否可用）、StopReason （API Key停用原因）、UseStatus （API Key用户侧开关）。
        :type Filters: list of RequestFilter
        :param _Sorts: 分页查询排序条件列表。支持的排序字段：CreatedAt（创建时间）、UpdatedAt（更新时间）。默认按 CreatedAt 降序。
        :type Sorts: list of RequestSort
        """
        self._TeamId = None
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sorts = None

    @property
    def TeamId(self):
        r"""套餐 ID。可通过DescribeTokenPlanList接口获取。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Offset(self):
        r"""分页查询偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页查询返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""分页查询过滤条件列表。支持的过滤字段：ApiKeyId （API Key ID）、Name （API Key 名称）、Status （API Key是否可用）、StopReason （API Key停用原因）、UseStatus （API Key用户侧开关）。
        :rtype: list of RequestFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sorts(self):
        r"""分页查询排序条件列表。支持的排序字段：CreatedAt（创建时间）、UpdatedAt（更新时间）。默认按 CreatedAt 降序。
        :rtype: list of RequestSort
        """
        return self._Sorts

    @Sorts.setter
    def Sorts(self, Sorts):
        self._Sorts = Sorts


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RequestFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sorts") is not None:
            self._Sorts = []
            for item in params.get("Sorts"):
                obj = RequestSort()
                obj._deserialize(item)
                self._Sorts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanApiKeyListResponse(AbstractModel):
    r"""DescribeTokenPlanApiKeyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeySet: API Key 列表。
        :type ApiKeySet: list of TokenPlanApiKeyListItem
        :param _TotalCount: API Key总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApiKeySet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def ApiKeySet(self):
        r"""API Key 列表。
        :rtype: list of TokenPlanApiKeyListItem
        """
        return self._ApiKeySet

    @ApiKeySet.setter
    def ApiKeySet(self, ApiKeySet):
        self._ApiKeySet = ApiKeySet

    @property
    def TotalCount(self):
        r"""API Key总数量。
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
        if params.get("ApiKeySet") is not None:
            self._ApiKeySet = []
            for item in params.get("ApiKeySet"):
                obj = TokenPlanApiKeyListItem()
                obj._deserialize(item)
                self._ApiKeySet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanApiKeyRequest(AbstractModel):
    r"""DescribeTokenPlanApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID。可通过DescribeTokenPlanApiKeyList接口获取。
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID。可通过DescribeTokenPlanApiKeyList接口获取。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanApiKeyResponse(AbstractModel):
    r"""DescribeTokenPlanApiKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKey: API Key 详情信息。
        :type ApiKey: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanApiKeyInfo`
        :param _Balance: API Key 额度及用量信息。
        :type Balance: :class:`tencentcloud.tokenhub.v20260322.models.SubPackageBalance`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApiKey = None
        self._Balance = None
        self._RequestId = None

    @property
    def ApiKey(self):
        r"""API Key 详情信息。
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanApiKeyInfo`
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Balance(self):
        r"""API Key 额度及用量信息。
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.SubPackageBalance`
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

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
        if params.get("ApiKey") is not None:
            self._ApiKey = TokenPlanApiKeyInfo()
            self._ApiKey._deserialize(params.get("ApiKey"))
        if params.get("Balance") is not None:
            self._Balance = SubPackageBalance()
            self._Balance._deserialize(params.get("Balance"))
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanApiKeySecretRequest(AbstractModel):
    r"""DescribeTokenPlanApiKeySecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID。可通过DescribeTokenPlanApiKeyList接口获取。
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID。可通过DescribeTokenPlanApiKeyList接口获取。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanApiKeySecretResponse(AbstractModel):
    r"""DescribeTokenPlanApiKeySecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: APIKey ID。
        :type ApiKeyId: str
        :param _ApiKey: APIKey 密钥值（明文）。请妥善保管。
        :type ApiKey: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApiKeyId = None
        self._ApiKey = None
        self._RequestId = None

    @property
    def ApiKeyId(self):
        r"""APIKey ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def ApiKey(self):
        r"""APIKey 密钥值（明文）。请妥善保管。
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

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
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKey = params.get("ApiKey")
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanApiKeyUsageDetailRequest(AbstractModel):
    r"""DescribeTokenPlanApiKeyUsageDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TeamId: 套餐 ID。可通过DescribeTokenPlanList接口获取。
        :type TeamId: str
        :param _From: 起始时间，RFC3339 格式。不传默认为结束时间前 15 分钟。
        :type From: str
        :param _To: 结束时间，RFC3339 格式。不传默认为当前时间。
        :type To: str
        :param _Sort: 排序方式。取值：asc（升序）、desc（降序），默认为 desc。
        :type Sort: str
        :param _Limit: 返回条数，默认为 20，最大值为 100。
        :type Limit: int
        :param _Context: 翻页上下文，首次查询不传，后续传入上次返回的 Context，直到 ListOver 为 true。
        :type Context: str
        :param _ApiKeyId: 按 API Key ID 精确过滤。最大 128 字符。与 ApiKeyName 至少需传入其一，都传时以 ApiKeyId 为准。可通过 DescribeTokenPlanApiKeyList 接口获取。
        :type ApiKeyId: str
        :param _ApiKeyName: 按 API Key 名称模糊过滤。最大 64 字符。与 ApiKeyId 至少需传入其一，都传时以 ApiKeyId 为准。
        :type ApiKeyName: str
        :param _ModelName: 按模型 ID (Model ID) 精确过滤。需要按模型名称过滤时传入该字段。
        :type ModelName: str
        """
        self._TeamId = None
        self._From = None
        self._To = None
        self._Sort = None
        self._Limit = None
        self._Context = None
        self._ApiKeyId = None
        self._ApiKeyName = None
        self._ModelName = None

    @property
    def TeamId(self):
        r"""套餐 ID。可通过DescribeTokenPlanList接口获取。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def From(self):
        r"""起始时间，RFC3339 格式。不传默认为结束时间前 15 分钟。
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def To(self):
        r"""结束时间，RFC3339 格式。不传默认为当前时间。
        :rtype: str
        """
        return self._To

    @To.setter
    def To(self, To):
        self._To = To

    @property
    def Sort(self):
        r"""排序方式。取值：asc（升序）、desc（降序），默认为 desc。
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def Limit(self):
        r"""返回条数，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Context(self):
        r"""翻页上下文，首次查询不传，后续传入上次返回的 Context，直到 ListOver 为 true。
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ApiKeyId(self):
        r"""按 API Key ID 精确过滤。最大 128 字符。与 ApiKeyName 至少需传入其一，都传时以 ApiKeyId 为准。可通过 DescribeTokenPlanApiKeyList 接口获取。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def ApiKeyName(self):
        r"""按 API Key 名称模糊过滤。最大 64 字符。与 ApiKeyId 至少需传入其一，都传时以 ApiKeyId 为准。
        :rtype: str
        """
        return self._ApiKeyName

    @ApiKeyName.setter
    def ApiKeyName(self, ApiKeyName):
        self._ApiKeyName = ApiKeyName

    @property
    def ModelName(self):
        r"""按模型 ID (Model ID) 精确过滤。需要按模型名称过滤时传入该字段。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._From = params.get("From")
        self._To = params.get("To")
        self._Sort = params.get("Sort")
        self._Limit = params.get("Limit")
        self._Context = params.get("Context")
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKeyName = params.get("ApiKeyName")
        self._ModelName = params.get("ModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanApiKeyUsageDetailResponse(AbstractModel):
    r"""DescribeTokenPlanApiKeyUsageDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Context: 翻页上下文，传入下一次请求的 Context 参数继续翻页。
        :type Context: str
        :param _ListOver: 是否已到末尾，为 true 时无需继续翻页。
        :type ListOver: bool
        :param _List: 调用明细列表。
        :type List: list of UsageDetailItem
        :param _ProductType: 	 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）
        :type ProductType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Context = None
        self._ListOver = None
        self._List = None
        self._ProductType = None
        self._RequestId = None

    @property
    def Context(self):
        r"""翻页上下文，传入下一次请求的 Context 参数继续翻页。
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def ListOver(self):
        r"""是否已到末尾，为 true 时无需继续翻页。
        :rtype: bool
        """
        return self._ListOver

    @ListOver.setter
    def ListOver(self, ListOver):
        self._ListOver = ListOver

    @property
    def List(self):
        r"""调用明细列表。
        :rtype: list of UsageDetailItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def ProductType(self):
        r"""	 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

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
        self._Context = params.get("Context")
        self._ListOver = params.get("ListOver")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UsageDetailItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._ProductType = params.get("ProductType")
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanListRequest(AbstractModel):
    r"""DescribeTokenPlanList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询偏移量，默认为 0。
        :type Offset: int
        :param _Limit: 分页查询返回数量，默认为 20，最大值为 100。
        :type Limit: int
        :param _Filters: 分页查询过滤条件列表。支持的过滤字段：TeamId（套餐 ID）、Name（套餐名称）、StopReason（关停原因）、ProductType（套餐类型）。
        :type Filters: list of RequestFilter
        :param _Sorts: 排序条件列表。支持的排序字段：CreatedAt（创建时间）、UpdatedAt（更新时间）。默认按 CreatedAt 降序。
        :type Sorts: list of RequestSort
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sorts = None

    @property
    def Offset(self):
        r"""分页查询偏移量，默认为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""分页查询返回数量，默认为 20，最大值为 100。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        r"""分页查询过滤条件列表。支持的过滤字段：TeamId（套餐 ID）、Name（套餐名称）、StopReason（关停原因）、ProductType（套餐类型）。
        :rtype: list of RequestFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sorts(self):
        r"""排序条件列表。支持的排序字段：CreatedAt（创建时间）、UpdatedAt（更新时间）。默认按 CreatedAt 降序。
        :rtype: list of RequestSort
        """
        return self._Sorts

    @Sorts.setter
    def Sorts(self, Sorts):
        self._Sorts = Sorts


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = RequestFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sorts") is not None:
            self._Sorts = []
            for item in params.get("Sorts"):
                obj = RequestSort()
                obj._deserialize(item)
                self._Sorts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanListResponse(AbstractModel):
    r"""DescribeTokenPlanList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TokenPlanSet: 套餐列表。
        :type TokenPlanSet: list of TokenPlanListItem
        :param _TotalCount: 套餐总数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TokenPlanSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TokenPlanSet(self):
        r"""套餐列表。
        :rtype: list of TokenPlanListItem
        """
        return self._TokenPlanSet

    @TokenPlanSet.setter
    def TokenPlanSet(self, TokenPlanSet):
        self._TokenPlanSet = TokenPlanSet

    @property
    def TotalCount(self):
        r"""套餐总数量。
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
        if params.get("TokenPlanSet") is not None:
            self._TokenPlanSet = []
            for item in params.get("TokenPlanSet"):
                obj = TokenPlanListItem()
                obj._deserialize(item)
                self._TokenPlanSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeTokenPlanRequest(AbstractModel):
    r"""DescribeTokenPlan请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TeamId: 套餐 ID。可通过 DescribeTokenPlanList 接口获取。
        :type TeamId: str
        """
        self._TeamId = None

    @property
    def TeamId(self):
        r"""套餐 ID。可通过 DescribeTokenPlanList 接口获取。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTokenPlanResponse(AbstractModel):
    r"""DescribeTokenPlan返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TeamId: 套餐 ID。
        :type TeamId: str
        :param _Name: 套餐名称。
        :type Name: str
        :param _AppId: 主账号 APP ID。
        :type AppId: str
        :param _Uin: 主账号 UIN。
        :type Uin: str
        :param _Status: 状态。取值：enable（启用）、disable（停用）。
        :type Status: str
        :param _StopReason: 关停原因。取值：取值：NORMAL（套餐正常）、ISOLATED（隔离/欠费）、FROZEN（冻结）、EXHAUSTED（额度耗尽）、DESTROYED（已销毁）。
        :type StopReason: str
        :param _ApiKeyMax: 可创建APIKey 上限。
        :type ApiKeyMax: int
        :param _PrepayResourceID: 云计费预付费资源包 ID。
        :type PrepayResourceID: str
        :param _Creator: 创建人，子账号创建的套餐将展示子账号UIN。
        :type Creator: str
        :param _CreatedAt: 创建时间。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间。
        :type UpdatedAt: str
        :param _PackageInfo: 套餐包基本信息
        :type PackageInfo: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanPackageInfo`
        :param _AutoRenewFlag: 自动续费标识。取值：0（手动续费）、1（自动续费）、2（明确不自动续费）。未绑定预付费资源时不返回。
        :type AutoRenewFlag: int
        :param _ApiKeyCount: 当前已创建的 API Key 数量
        :type ApiKeyCount: int
        :param _TokenSummary: 当前周期 Token 用量明细
        :type TokenSummary: :class:`tencentcloud.tokenhub.v20260322.models.TokenSummary`
        :param _ProductType: 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）
        :type ProductType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TeamId = None
        self._Name = None
        self._AppId = None
        self._Uin = None
        self._Status = None
        self._StopReason = None
        self._ApiKeyMax = None
        self._PrepayResourceID = None
        self._Creator = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._PackageInfo = None
        self._AutoRenewFlag = None
        self._ApiKeyCount = None
        self._TokenSummary = None
        self._ProductType = None
        self._RequestId = None

    @property
    def TeamId(self):
        r"""套餐 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def Name(self):
        r"""套餐名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppId(self):
        r"""主账号 APP ID。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""主账号 UIN。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Status(self):
        r"""状态。取值：enable（启用）、disable（停用）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StopReason(self):
        r"""关停原因。取值：取值：NORMAL（套餐正常）、ISOLATED（隔离/欠费）、FROZEN（冻结）、EXHAUSTED（额度耗尽）、DESTROYED（已销毁）。
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def ApiKeyMax(self):
        r"""可创建APIKey 上限。
        :rtype: int
        """
        return self._ApiKeyMax

    @ApiKeyMax.setter
    def ApiKeyMax(self, ApiKeyMax):
        self._ApiKeyMax = ApiKeyMax

    @property
    def PrepayResourceID(self):
        r"""云计费预付费资源包 ID。
        :rtype: str
        """
        return self._PrepayResourceID

    @PrepayResourceID.setter
    def PrepayResourceID(self, PrepayResourceID):
        self._PrepayResourceID = PrepayResourceID

    @property
    def Creator(self):
        r"""创建人，子账号创建的套餐将展示子账号UIN。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatedAt(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PackageInfo(self):
        r"""套餐包基本信息
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanPackageInfo`
        """
        return self._PackageInfo

    @PackageInfo.setter
    def PackageInfo(self, PackageInfo):
        self._PackageInfo = PackageInfo

    @property
    def AutoRenewFlag(self):
        r"""自动续费标识。取值：0（手动续费）、1（自动续费）、2（明确不自动续费）。未绑定预付费资源时不返回。
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def ApiKeyCount(self):
        r"""当前已创建的 API Key 数量
        :rtype: int
        """
        return self._ApiKeyCount

    @ApiKeyCount.setter
    def ApiKeyCount(self, ApiKeyCount):
        self._ApiKeyCount = ApiKeyCount

    @property
    def TokenSummary(self):
        r"""当前周期 Token 用量明细
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.TokenSummary`
        """
        return self._TokenSummary

    @TokenSummary.setter
    def TokenSummary(self, TokenSummary):
        self._TokenSummary = TokenSummary

    @property
    def ProductType(self):
        r"""套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

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
        self._TeamId = params.get("TeamId")
        self._Name = params.get("Name")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Status = params.get("Status")
        self._StopReason = params.get("StopReason")
        self._ApiKeyMax = params.get("ApiKeyMax")
        self._PrepayResourceID = params.get("PrepayResourceID")
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("PackageInfo") is not None:
            self._PackageInfo = TokenPlanPackageInfo()
            self._PackageInfo._deserialize(params.get("PackageInfo"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._ApiKeyCount = params.get("ApiKeyCount")
        if params.get("TokenSummary") is not None:
            self._TokenSummary = TokenSummary()
            self._TokenSummary._deserialize(params.get("TokenSummary"))
        self._ProductType = params.get("ProductType")
        self._RequestId = params.get("RequestId")


class DescribeUsageRankListRequest(AbstractModel):
    r"""DescribeUsageRankList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Dimension: 统计维度。取值：apikey（按 APIKey 统计）、endpoint（按接入点统计）、model（按模型统计）。
        :type Dimension: str
        :param _StartTime: 起始时间（闭区间），RFC3339 格式。
        :type StartTime: str
        :param _EndTime: 结束时间（开区间），RFC3339 格式。与 StartTime 的跨度最大 90 天。
        :type EndTime: str
        :param _MetricType: 指标族切换字段。本期支持 tokens（累计 Token 用量，statistics=sum）；传其他值将返回 InvalidParameter。空字符串或不传时默认 tokens。接口预留 MetricType 字段以支持后续指标族扩展。
        :type MetricType: str
        :param _Target: 维度过滤值。空字符串表示查询全部对象，非空时仅查询指定单个对象（如指定 APIKey ID）。最大 256 字符。
        :type Target: str
        :param _Period: 统计粒度（秒）。取值：60、300、3600、86400。必须不小于跨度对应下限：跨度 ≤ 1 天 → 60；1 ~ 5 天 → 300；5 ~ 10 天 → 3600；> 10 天 → 86400。仅 ShowAll=false 时使用。
        :type Period: int
        :param _Offset: 翻页起点，从 0 起，默认 0。ShowAll=true 时忽略。页大小固定为 10。
        :type Offset: int
        :param _ShowAll: 是否返回全量结果。
- false（默认）：按 Offset 分页返回 TopList（每页 10 条），每个对象包含
  Series 时序点用于绘制曲线。
- true：忽略 Offset，返回全量对象列表，不返回 Series（CSV 导出场景）。

        :type ShowAll: bool
        """
        self._Dimension = None
        self._StartTime = None
        self._EndTime = None
        self._MetricType = None
        self._Target = None
        self._Period = None
        self._Offset = None
        self._ShowAll = None

    @property
    def Dimension(self):
        r"""统计维度。取值：apikey（按 APIKey 统计）、endpoint（按接入点统计）、model（按模型统计）。
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def StartTime(self):
        r"""起始时间（闭区间），RFC3339 格式。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""结束时间（开区间），RFC3339 格式。与 StartTime 的跨度最大 90 天。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricType(self):
        r"""指标族切换字段。本期支持 tokens（累计 Token 用量，statistics=sum）；传其他值将返回 InvalidParameter。空字符串或不传时默认 tokens。接口预留 MetricType 字段以支持后续指标族扩展。
        :rtype: str
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def Target(self):
        r"""维度过滤值。空字符串表示查询全部对象，非空时仅查询指定单个对象（如指定 APIKey ID）。最大 256 字符。
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def Period(self):
        r"""统计粒度（秒）。取值：60、300、3600、86400。必须不小于跨度对应下限：跨度 ≤ 1 天 → 60；1 ~ 5 天 → 300；5 ~ 10 天 → 3600；> 10 天 → 86400。仅 ShowAll=false 时使用。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Offset(self):
        r"""翻页起点，从 0 起，默认 0。ShowAll=true 时忽略。页大小固定为 10。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ShowAll(self):
        r"""是否返回全量结果。
- false（默认）：按 Offset 分页返回 TopList（每页 10 条），每个对象包含
  Series 时序点用于绘制曲线。
- true：忽略 Offset，返回全量对象列表，不返回 Series（CSV 导出场景）。

        :rtype: bool
        """
        return self._ShowAll

    @ShowAll.setter
    def ShowAll(self, ShowAll):
        self._ShowAll = ShowAll


    def _deserialize(self, params):
        self._Dimension = params.get("Dimension")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricType = params.get("MetricType")
        self._Target = params.get("Target")
        self._Period = params.get("Period")
        self._Offset = params.get("Offset")
        self._ShowAll = params.get("ShowAll")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUsageRankListResponse(AbstractModel):
    r"""DescribeUsageRankList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Dimension: 回填请求的统计维度。
        :type Dimension: str
        :param _MetricType: 回填请求的指标族（本期固定为 tokens）。前端按本字段切换图表渲染逻辑。
        :type MetricType: str
        :param _MetricKeys: 本次响应中 Stats / Series / PageStats / TotalStats 实际包含的 metric key 列表，顺序固定为 [Total, Input, Output]。本期为 [TotalToken, InputTotalToken, OutputTotalToken]。前端可遍历此列表渲染图表，无需硬编码 key 名。
        :type MetricKeys: list of str
        :param _ViewName: 视图（数据来源）
        :type ViewName: str
        :param _Period: 回填请求的统计粒度（秒）。ShowAll=true 时为 0。
        :type Period: int
        :param _StartTime: 回填请求的起始时间。
        :type StartTime: str
        :param _EndTime: 回填请求的结束时间。
        :type EndTime: str
        :param _Total: 全量对象数。
        :type Total: int
        :param _Offset: 回填请求的翻页起点。ShowAll=true 时为 0。
        :type Offset: int
        :param _Limit: 页大小，恒为 10。ShowAll=true 时为 Total。
        :type Limit: int
        :param _Timestamps: Series 数组对应的时间戳序列（Unix 秒）。ShowAll=true 时为空数组。
        :type Timestamps: list of int
        :param _TopList: 对象排行列表，按主指标（`MetricKeys[0]`，本期为 TotalToken）降序排序。ShowAll=false 时为当前页 10 个对象（含 Series）；ShowAll=true 时为全量对象（不含 Series，用于 CSV 导出）。
        :type TopList: list of UsageRankItem
        :param _PageStats: 分页统计结果
        :type PageStats: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        :param _TotalStats: 总统计结果
        :type TotalStats: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Dimension = None
        self._MetricType = None
        self._MetricKeys = None
        self._ViewName = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Total = None
        self._Offset = None
        self._Limit = None
        self._Timestamps = None
        self._TopList = None
        self._PageStats = None
        self._TotalStats = None
        self._RequestId = None

    @property
    def Dimension(self):
        r"""回填请求的统计维度。
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def MetricType(self):
        r"""回填请求的指标族（本期固定为 tokens）。前端按本字段切换图表渲染逻辑。
        :rtype: str
        """
        return self._MetricType

    @MetricType.setter
    def MetricType(self, MetricType):
        self._MetricType = MetricType

    @property
    def MetricKeys(self):
        r"""本次响应中 Stats / Series / PageStats / TotalStats 实际包含的 metric key 列表，顺序固定为 [Total, Input, Output]。本期为 [TotalToken, InputTotalToken, OutputTotalToken]。前端可遍历此列表渲染图表，无需硬编码 key 名。
        :rtype: list of str
        """
        return self._MetricKeys

    @MetricKeys.setter
    def MetricKeys(self, MetricKeys):
        self._MetricKeys = MetricKeys

    @property
    def ViewName(self):
        r"""视图（数据来源）
        :rtype: str
        """
        return self._ViewName

    @ViewName.setter
    def ViewName(self, ViewName):
        self._ViewName = ViewName

    @property
    def Period(self):
        r"""回填请求的统计粒度（秒）。ShowAll=true 时为 0。
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        r"""回填请求的起始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""回填请求的结束时间。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Total(self):
        r"""全量对象数。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Offset(self):
        r"""回填请求的翻页起点。ShowAll=true 时为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""页大小，恒为 10。ShowAll=true 时为 Total。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Timestamps(self):
        r"""Series 数组对应的时间戳序列（Unix 秒）。ShowAll=true 时为空数组。
        :rtype: list of int
        """
        return self._Timestamps

    @Timestamps.setter
    def Timestamps(self, Timestamps):
        self._Timestamps = Timestamps

    @property
    def TopList(self):
        r"""对象排行列表，按主指标（`MetricKeys[0]`，本期为 TotalToken）降序排序。ShowAll=false 时为当前页 10 个对象（含 Series）；ShowAll=true 时为全量对象（不含 Series，用于 CSV 导出）。
        :rtype: list of UsageRankItem
        """
        return self._TopList

    @TopList.setter
    def TopList(self, TopList):
        self._TopList = TopList

    @property
    def PageStats(self):
        r"""分页统计结果
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        """
        return self._PageStats

    @PageStats.setter
    def PageStats(self, PageStats):
        self._PageStats = PageStats

    @property
    def TotalStats(self):
        r"""总统计结果
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        """
        return self._TotalStats

    @TotalStats.setter
    def TotalStats(self, TotalStats):
        self._TotalStats = TotalStats

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
        self._Dimension = params.get("Dimension")
        self._MetricType = params.get("MetricType")
        self._MetricKeys = params.get("MetricKeys")
        self._ViewName = params.get("ViewName")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Total = params.get("Total")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Timestamps = params.get("Timestamps")
        if params.get("TopList") is not None:
            self._TopList = []
            for item in params.get("TopList"):
                obj = UsageRankItem()
                obj._deserialize(item)
                self._TopList.append(obj)
        if params.get("PageStats") is not None:
            self._PageStats = UsageStats()
            self._PageStats._deserialize(params.get("PageStats"))
        if params.get("TotalStats") is not None:
            self._TotalStats = UsageStats()
            self._TotalStats._deserialize(params.get("TotalStats"))
        self._RequestId = params.get("RequestId")


class GlossaryEntryInput(AbstractModel):
    r"""新建术语条目项

    """

    def __init__(self):
        r"""
        :param _SourceTerm: 源语言术语。最大 1000 字符。
        :type SourceTerm: str
        :param _TargetTerm: 目标语言术语。最大 1000 字符。
        :type TargetTerm: str
        """
        self._SourceTerm = None
        self._TargetTerm = None

    @property
    def SourceTerm(self):
        r"""源语言术语。最大 1000 字符。
        :rtype: str
        """
        return self._SourceTerm

    @SourceTerm.setter
    def SourceTerm(self, SourceTerm):
        self._SourceTerm = SourceTerm

    @property
    def TargetTerm(self):
        r"""目标语言术语。最大 1000 字符。
        :rtype: str
        """
        return self._TargetTerm

    @TargetTerm.setter
    def TargetTerm(self, TargetTerm):
        self._TargetTerm = TargetTerm


    def _deserialize(self, params):
        self._SourceTerm = params.get("SourceTerm")
        self._TargetTerm = params.get("TargetTerm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlossaryEntryItem(AbstractModel):
    r"""术语条目详情

    """

    def __init__(self):
        r"""
        :param _EntryId: 术语条目 ID。
        :type EntryId: str
        :param _SourceTerm: 源语言术语。
        :type SourceTerm: str
        :param _TargetTerm: 目标语言术语。
        :type TargetTerm: str
        :param _UpdatedAt: 更新时间。Unix 时间戳（毫秒）。
        :type UpdatedAt: int
        """
        self._EntryId = None
        self._SourceTerm = None
        self._TargetTerm = None
        self._UpdatedAt = None

    @property
    def EntryId(self):
        r"""术语条目 ID。
        :rtype: str
        """
        return self._EntryId

    @EntryId.setter
    def EntryId(self, EntryId):
        self._EntryId = EntryId

    @property
    def SourceTerm(self):
        r"""源语言术语。
        :rtype: str
        """
        return self._SourceTerm

    @SourceTerm.setter
    def SourceTerm(self, SourceTerm):
        self._SourceTerm = SourceTerm

    @property
    def TargetTerm(self):
        r"""目标语言术语。
        :rtype: str
        """
        return self._TargetTerm

    @TargetTerm.setter
    def TargetTerm(self, TargetTerm):
        self._TargetTerm = TargetTerm

    @property
    def UpdatedAt(self):
        r"""更新时间。Unix 时间戳（毫秒）。
        :rtype: int
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._EntryId = params.get("EntryId")
        self._SourceTerm = params.get("SourceTerm")
        self._TargetTerm = params.get("TargetTerm")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GlossaryItem(AbstractModel):
    r"""术语库详情

    """

    def __init__(self):
        r"""
        :param _GlossaryId: 术语库 ID。
        :type GlossaryId: str
        :param _Name: 术语库名称。
        :type Name: str
        :param _Description: 术语库描述。
        :type Description: str
        :param _Source: 源语言代码。
        :type Source: str
        :param _Target: 目标语言代码。
        :type Target: str
        :param _CreatedTime: 创建时间。
        :type CreatedTime: str
        :param _UpdatedTime: 更新时间。
        :type UpdatedTime: str
        """
        self._GlossaryId = None
        self._Name = None
        self._Description = None
        self._Source = None
        self._Target = None
        self._CreatedTime = None
        self._UpdatedTime = None

    @property
    def GlossaryId(self):
        r"""术语库 ID。
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Name(self):
        r"""术语库名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        r"""术语库描述。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Source(self):
        r"""源语言代码。
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Target(self):
        r"""目标语言代码。
        :rtype: str
        """
        return self._Target

    @Target.setter
    def Target(self, Target):
        self._Target = Target

    @property
    def CreatedTime(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def UpdatedTime(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdatedTime

    @UpdatedTime.setter
    def UpdatedTime(self, UpdatedTime):
        self._UpdatedTime = UpdatedTime


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        self._Source = params.get("Source")
        self._Target = params.get("Target")
        self._CreatedTime = params.get("CreatedTime")
        self._UpdatedTime = params.get("UpdatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlossaryEntriesRequest(AbstractModel):
    r"""ModifyGlossaryEntries请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GlossaryId: 术语库 ID。可通过 DescribeGlossaries 接口获取。
        :type GlossaryId: str
        :param _Entries: 术语条目列表。单次最多 200 个。
        :type Entries: list of ModifyGlossaryEntryInput
        """
        self._GlossaryId = None
        self._Entries = None

    @property
    def GlossaryId(self):
        r"""术语库 ID。可通过 DescribeGlossaries 接口获取。
        :rtype: str
        """
        return self._GlossaryId

    @GlossaryId.setter
    def GlossaryId(self, GlossaryId):
        self._GlossaryId = GlossaryId

    @property
    def Entries(self):
        r"""术语条目列表。单次最多 200 个。
        :rtype: list of ModifyGlossaryEntryInput
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries


    def _deserialize(self, params):
        self._GlossaryId = params.get("GlossaryId")
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = ModifyGlossaryEntryInput()
                obj._deserialize(item)
                self._Entries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGlossaryEntriesResponse(AbstractModel):
    r"""ModifyGlossaryEntries返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Entries: 修改后的术语条目列表。
        :type Entries: list of GlossaryEntryItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Entries = None
        self._RequestId = None

    @property
    def Entries(self):
        r"""修改后的术语条目列表。
        :rtype: list of GlossaryEntryItem
        """
        return self._Entries

    @Entries.setter
    def Entries(self, Entries):
        self._Entries = Entries

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
        if params.get("Entries") is not None:
            self._Entries = []
            for item in params.get("Entries"):
                obj = GlossaryEntryItem()
                obj._deserialize(item)
                self._Entries.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyGlossaryEntryInput(AbstractModel):
    r"""修改术语条目项

    """

    def __init__(self):
        r"""
        :param _EntryId: 术语条目 ID。可通过 DescribeGlossaryEntries 接口获取。
        :type EntryId: str
        :param _SourceTerm: 源语言术语。最大 1000 字符。不传则保持不变。
        :type SourceTerm: str
        :param _TargetTerm: 目标语言术语。最大 1000 字符。不传则保持不变。
        :type TargetTerm: str
        """
        self._EntryId = None
        self._SourceTerm = None
        self._TargetTerm = None

    @property
    def EntryId(self):
        r"""术语条目 ID。可通过 DescribeGlossaryEntries 接口获取。
        :rtype: str
        """
        return self._EntryId

    @EntryId.setter
    def EntryId(self, EntryId):
        self._EntryId = EntryId

    @property
    def SourceTerm(self):
        r"""源语言术语。最大 1000 字符。不传则保持不变。
        :rtype: str
        """
        return self._SourceTerm

    @SourceTerm.setter
    def SourceTerm(self, SourceTerm):
        self._SourceTerm = SourceTerm

    @property
    def TargetTerm(self):
        r"""目标语言术语。最大 1000 字符。不传则保持不变。
        :rtype: str
        """
        return self._TargetTerm

    @TargetTerm.setter
    def TargetTerm(self, TargetTerm):
        self._TargetTerm = TargetTerm


    def _deserialize(self, params):
        self._EntryId = params.get("EntryId")
        self._SourceTerm = params.get("SourceTerm")
        self._TargetTerm = params.get("TargetTerm")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenPlanApiKeyRequest(AbstractModel):
    r"""ModifyTokenPlanApiKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID。
        :type ApiKeyId: str
        :param _AllowedModels: 可用模型列表。不传则不修改。

- 如果套餐类型为企业版专业套餐：
1）传入“all“ ：使用套餐支持的所有模型
2）传入 Model ID：指定具体模型。“all“和具体的 Model ID 不能同时传入。

- 如果套餐类型为企业版轻享套餐，不允许传该参数。
        :type AllowedModels: list of str
        :param _ExclusiveQuota: 独占额度，不传则不修改。单位说明：

- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type ExclusiveQuota: int
        :param _TotalQuota: 总额度上限。-1 表示不限，必须为 -1 或 >= API Key 当前的 ExclusiveQuota（独占额度），不传则不修改。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type TotalQuota: int
        :param _UseStatus: 是否启用该 API Key。取值：enable（启用）、disable（停用），不传则不修改。
        :type UseStatus: str
        :param _TPM: TPM（Tokens Per Minute）限制。不传则不修改。必须 >= 0 且 <= 套餐 TPM。
        :type TPM: int
        """
        self._ApiKeyId = None
        self._AllowedModels = None
        self._ExclusiveQuota = None
        self._TotalQuota = None
        self._UseStatus = None
        self._TPM = None

    @property
    def ApiKeyId(self):
        r"""API Key ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def AllowedModels(self):
        r"""可用模型列表。不传则不修改。

- 如果套餐类型为企业版专业套餐：
1）传入“all“ ：使用套餐支持的所有模型
2）传入 Model ID：指定具体模型。“all“和具体的 Model ID 不能同时传入。

- 如果套餐类型为企业版轻享套餐，不允许传该参数。
        :rtype: list of str
        """
        return self._AllowedModels

    @AllowedModels.setter
    def AllowedModels(self, AllowedModels):
        self._AllowedModels = AllowedModels

    @property
    def ExclusiveQuota(self):
        r"""独占额度，不传则不修改。单位说明：

- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: int
        """
        return self._ExclusiveQuota

    @ExclusiveQuota.setter
    def ExclusiveQuota(self, ExclusiveQuota):
        self._ExclusiveQuota = ExclusiveQuota

    @property
    def TotalQuota(self):
        r"""总额度上限。-1 表示不限，必须为 -1 或 >= API Key 当前的 ExclusiveQuota（独占额度），不传则不修改。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def UseStatus(self):
        r"""是否启用该 API Key。取值：enable（启用）、disable（停用），不传则不修改。
        :rtype: str
        """
        return self._UseStatus

    @UseStatus.setter
    def UseStatus(self, UseStatus):
        self._UseStatus = UseStatus

    @property
    def TPM(self):
        r"""TPM（Tokens Per Minute）限制。不传则不修改。必须 >= 0 且 <= 套餐 TPM。
        :rtype: int
        """
        return self._TPM

    @TPM.setter
    def TPM(self, TPM):
        self._TPM = TPM


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        self._AllowedModels = params.get("AllowedModels")
        self._ExclusiveQuota = params.get("ExclusiveQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._UseStatus = params.get("UseStatus")
        self._TPM = params.get("TPM")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenPlanApiKeyResponse(AbstractModel):
    r"""ModifyTokenPlanApiKey返回参数结构体

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


class ModifyTokenPlanApiKeySecretRequest(AbstractModel):
    r"""ModifyTokenPlanApiKeySecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID。可通过DescribeTokenPlanApiKeyList接口获取。
        :type ApiKeyId: str
        """
        self._ApiKeyId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID。可通过DescribeTokenPlanApiKeyList接口获取。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTokenPlanApiKeySecretResponse(AbstractModel):
    r"""ModifyTokenPlanApiKeySecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID。
        :type ApiKeyId: str
        :param _KeyVersion: 重置后的密钥版本号。
        :type KeyVersion: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ApiKeyId = None
        self._KeyVersion = None
        self._RequestId = None

    @property
    def ApiKeyId(self):
        r"""API Key ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def KeyVersion(self):
        r"""重置后的密钥版本号。
        :rtype: int
        """
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

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
        self._ApiKeyId = params.get("ApiKeyId")
        self._KeyVersion = params.get("KeyVersion")
        self._RequestId = params.get("RequestId")


class QuotaInfo(AbstractModel):
    r"""Token 限额信息

    """

    def __init__(self):
        r"""
        :param _PkgId: 限额包 ID。
        :type PkgId: str
        :param _Status: 限额包状态。取值：1（正常）、3（已耗尽）、4（已销毁）。
        :type Status: int
        :param _CycleUnit: 限额周期。取值：d（按日）、m（按月）、lifetime（总额度，不重置）。
        :type CycleUnit: str
        :param _CycleCredits: 维度当期限额总量（Token 数）。使用字符串避免大数精度丢失。
        :type CycleCredits: str
        :param _CycleUsed: 维度当期已使用量（Token 数）。使用字符串避免大数精度丢失。
        :type CycleUsed: str
        :param _StartTime: 限额生效起始时间。
        :type StartTime: str
        :param _ExpireTime: 限额过期时间。
        :type ExpireTime: str
        """
        self._PkgId = None
        self._Status = None
        self._CycleUnit = None
        self._CycleCredits = None
        self._CycleUsed = None
        self._StartTime = None
        self._ExpireTime = None

    @property
    def PkgId(self):
        r"""限额包 ID。
        :rtype: str
        """
        return self._PkgId

    @PkgId.setter
    def PkgId(self, PkgId):
        self._PkgId = PkgId

    @property
    def Status(self):
        r"""限额包状态。取值：1（正常）、3（已耗尽）、4（已销毁）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CycleUnit(self):
        r"""限额周期。取值：d（按日）、m（按月）、lifetime（总额度，不重置）。
        :rtype: str
        """
        return self._CycleUnit

    @CycleUnit.setter
    def CycleUnit(self, CycleUnit):
        self._CycleUnit = CycleUnit

    @property
    def CycleCredits(self):
        r"""维度当期限额总量（Token 数）。使用字符串避免大数精度丢失。
        :rtype: str
        """
        return self._CycleCredits

    @CycleCredits.setter
    def CycleCredits(self, CycleCredits):
        self._CycleCredits = CycleCredits

    @property
    def CycleUsed(self):
        r"""维度当期已使用量（Token 数）。使用字符串避免大数精度丢失。
        :rtype: str
        """
        return self._CycleUsed

    @CycleUsed.setter
    def CycleUsed(self, CycleUsed):
        self._CycleUsed = CycleUsed

    @property
    def StartTime(self):
        r"""限额生效起始时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        r"""限额过期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime


    def _deserialize(self, params):
        self._PkgId = params.get("PkgId")
        self._Status = params.get("Status")
        self._CycleUnit = params.get("CycleUnit")
        self._CycleCredits = params.get("CycleCredits")
        self._CycleUsed = params.get("CycleUsed")
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewTokenPlanTeamOrderRequest(AbstractModel):
    r"""RenewTokenPlanTeamOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TeamId: 套餐 ID。可通过 DescribeTokenPlanList 接口获取。
        :type TeamId: str
        :param _TimeSpan: 续费时长。单位：月。必须大于 0。
        :type TimeSpan: int
        """
        self._TeamId = None
        self._TimeSpan = None

    @property
    def TeamId(self):
        r"""套餐 ID。可通过 DescribeTokenPlanList 接口获取。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def TimeSpan(self):
        r"""续费时长。单位：月。必须大于 0。
        :rtype: int
        """
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewTokenPlanTeamOrderResponse(AbstractModel):
    r"""RenewTokenPlanTeamOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BigOrderId: 腾讯云订单 ID。用于关联一次续费操作下的所有子订单。
        :type BigOrderId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BigOrderId = None
        self._RequestId = None

    @property
    def BigOrderId(self):
        r"""腾讯云订单 ID。用于关联一次续费操作下的所有子订单。
        :rtype: str
        """
        return self._BigOrderId

    @BigOrderId.setter
    def BigOrderId(self, BigOrderId):
        self._BigOrderId = BigOrderId

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
        self._BigOrderId = params.get("BigOrderId")
        self._RequestId = params.get("RequestId")


class RequestFilter(AbstractModel):
    r"""过滤条件

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名称。
        :type Name: str
        :param _Op: 过滤操作符。取值：EXACT（精确匹配）、FUZZY（模糊匹配）、NOT（排除匹配）。
        :type Op: str
        :param _Values: 过滤值列表。最多支持 10 个。
        :type Values: list of str
        """
        self._Name = None
        self._Op = None
        self._Values = None

    @property
    def Name(self):
        r"""过滤字段名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Op(self):
        r"""过滤操作符。取值：EXACT（精确匹配）、FUZZY（模糊匹配）、NOT（排除匹配）。
        :rtype: str
        """
        return self._Op

    @Op.setter
    def Op(self, Op):
        self._Op = Op

    @property
    def Values(self):
        r"""过滤值列表。最多支持 10 个。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Op = params.get("Op")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestSort(AbstractModel):
    r"""排序条件

    """

    def __init__(self):
        r"""
        :param _Name: 排序字段名称。
        :type Name: str
        :param _Order: 排序方向。取值：ASC（升序）、DESC（降序）。
        :type Order: str
        """
        self._Name = None
        self._Order = None

    @property
    def Name(self):
        r"""排序字段名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Order(self):
        r"""排序方向。取值：ASC（升序）、DESC（降序）。
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubPackageBalance(AbstractModel):
    r"""API Key 额度及用量信息

    """

    def __init__(self):
        r"""
        :param _ExclusiveQuota: 独占额度。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type ExclusiveQuota: str
        :param _ExclusiveUsed: 独占额度已用量。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type ExclusiveUsed: str
        :param _ExclusiveRemain: 独占额度剩余量。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type ExclusiveRemain: str
        :param _SharedQuota: 共享额度上限，-1 表示不限。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type SharedQuota: str
        :param _SharedUsed: 共享额度已用量。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type SharedUsed: str
        :param _SharedRemain: 共享额度剩余量。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :type SharedRemain: str
        :param _Status: API Key 额度包状态。取值：0（正常）、1（耗尽）。
        :type Status: int
        """
        self._ExclusiveQuota = None
        self._ExclusiveUsed = None
        self._ExclusiveRemain = None
        self._SharedQuota = None
        self._SharedUsed = None
        self._SharedRemain = None
        self._Status = None

    @property
    def ExclusiveQuota(self):
        r"""独占额度。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: str
        """
        return self._ExclusiveQuota

    @ExclusiveQuota.setter
    def ExclusiveQuota(self, ExclusiveQuota):
        self._ExclusiveQuota = ExclusiveQuota

    @property
    def ExclusiveUsed(self):
        r"""独占额度已用量。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: str
        """
        return self._ExclusiveUsed

    @ExclusiveUsed.setter
    def ExclusiveUsed(self, ExclusiveUsed):
        self._ExclusiveUsed = ExclusiveUsed

    @property
    def ExclusiveRemain(self):
        r"""独占额度剩余量。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: str
        """
        return self._ExclusiveRemain

    @ExclusiveRemain.setter
    def ExclusiveRemain(self, ExclusiveRemain):
        self._ExclusiveRemain = ExclusiveRemain

    @property
    def SharedQuota(self):
        r"""共享额度上限，-1 表示不限。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: str
        """
        return self._SharedQuota

    @SharedQuota.setter
    def SharedQuota(self, SharedQuota):
        self._SharedQuota = SharedQuota

    @property
    def SharedUsed(self):
        r"""共享额度已用量。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: str
        """
        return self._SharedUsed

    @SharedUsed.setter
    def SharedUsed(self, SharedUsed):
        self._SharedUsed = SharedUsed

    @property
    def SharedRemain(self):
        r"""共享额度剩余量。单位说明如下：
- 套餐类型为专业套餐，单位取值为积分；
- 套餐类型为轻享套餐，单位取值为 token。
        :rtype: str
        """
        return self._SharedRemain

    @SharedRemain.setter
    def SharedRemain(self, SharedRemain):
        self._SharedRemain = SharedRemain

    @property
    def Status(self):
        r"""API Key 额度包状态。取值：0（正常）、1（耗尽）。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ExclusiveQuota = params.get("ExclusiveQuota")
        self._ExclusiveUsed = params.get("ExclusiveUsed")
        self._ExclusiveRemain = params.get("ExclusiveRemain")
        self._SharedQuota = params.get("SharedQuota")
        self._SharedUsed = params.get("SharedUsed")
        self._SharedRemain = params.get("SharedRemain")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenPlanApiKeyInfo(AbstractModel):
    r"""Token Plan API Key 详情

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID。
        :type ApiKeyId: str
        :param _ApiKey: API Key 密钥值（脱敏）。
        :type ApiKey: str
        :param _Name: API Key 名称。
        :type Name: str
        :param _TeamId: 所属套餐 ID。
        :type TeamId: str
        :param _AppId: 账号APP ID。
        :type AppId: str
        :param _Uin: 主账号 UIN。
        :type Uin: str
        :param _AllowedModels: API Key 可用模型列表（JSON 数组字符串）。
        :type AllowedModels: str
        :param _Status: API Key 是否可用。取值：enable（启用）、disable（停用）。
        :type Status: str
        :param _StopReason: API Key 停用原因。取值：NORMAL（正常，默认值），QUOTA_EXHAUSTED（API Key额度包耗尽），ABNORMAL（异常，需人工介入）
        :type StopReason: str
        :param _UseStatus: 用户侧开关。取值：enable（启用）、disable（停用）。
        :type UseStatus: str
        :param _KeyVersion: 密钥版本号。
        :type KeyVersion: int
        :param _LastRotatedAt: 最近一次重置时间。（ISO 8601）
        :type LastRotatedAt: str
        :param _Creator: 创建人，如果是子账号创建，则该值为子账号UIN。
        :type Creator: str
        :param _CreatedAt: 创建时间。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间。
        :type UpdatedAt: str
        :param _TPM: TPM 限制（Tokens Per Minute）。
        :type TPM: int
        :param _ProductType: 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）
        :type ProductType: str
        """
        self._ApiKeyId = None
        self._ApiKey = None
        self._Name = None
        self._TeamId = None
        self._AppId = None
        self._Uin = None
        self._AllowedModels = None
        self._Status = None
        self._StopReason = None
        self._UseStatus = None
        self._KeyVersion = None
        self._LastRotatedAt = None
        self._Creator = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._TPM = None
        self._ProductType = None

    @property
    def ApiKeyId(self):
        r"""API Key ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def ApiKey(self):
        r"""API Key 密钥值（脱敏）。
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Name(self):
        r"""API Key 名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TeamId(self):
        r"""所属套餐 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def AppId(self):
        r"""账号APP ID。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""主账号 UIN。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AllowedModels(self):
        r"""API Key 可用模型列表（JSON 数组字符串）。
        :rtype: str
        """
        return self._AllowedModels

    @AllowedModels.setter
    def AllowedModels(self, AllowedModels):
        self._AllowedModels = AllowedModels

    @property
    def Status(self):
        r"""API Key 是否可用。取值：enable（启用）、disable（停用）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StopReason(self):
        r"""API Key 停用原因。取值：NORMAL（正常，默认值），QUOTA_EXHAUSTED（API Key额度包耗尽），ABNORMAL（异常，需人工介入）
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def UseStatus(self):
        r"""用户侧开关。取值：enable（启用）、disable（停用）。
        :rtype: str
        """
        return self._UseStatus

    @UseStatus.setter
    def UseStatus(self, UseStatus):
        self._UseStatus = UseStatus

    @property
    def KeyVersion(self):
        r"""密钥版本号。
        :rtype: int
        """
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

    @property
    def LastRotatedAt(self):
        r"""最近一次重置时间。（ISO 8601）
        :rtype: str
        """
        return self._LastRotatedAt

    @LastRotatedAt.setter
    def LastRotatedAt(self, LastRotatedAt):
        self._LastRotatedAt = LastRotatedAt

    @property
    def Creator(self):
        r"""创建人，如果是子账号创建，则该值为子账号UIN。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatedAt(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def TPM(self):
        r"""TPM 限制（Tokens Per Minute）。
        :rtype: int
        """
        return self._TPM

    @TPM.setter
    def TPM(self, TPM):
        self._TPM = TPM

    @property
    def ProductType(self):
        r"""套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKey = params.get("ApiKey")
        self._Name = params.get("Name")
        self._TeamId = params.get("TeamId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AllowedModels = params.get("AllowedModels")
        self._Status = params.get("Status")
        self._StopReason = params.get("StopReason")
        self._UseStatus = params.get("UseStatus")
        self._KeyVersion = params.get("KeyVersion")
        self._LastRotatedAt = params.get("LastRotatedAt")
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._TPM = params.get("TPM")
        self._ProductType = params.get("ProductType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenPlanApiKeyListItem(AbstractModel):
    r"""Token Plan API Key 列表项

    """

    def __init__(self):
        r"""
        :param _ApiKeyId: API Key ID。
        :type ApiKeyId: str
        :param _ApiKey: API Key 密钥值（脱敏）。
        :type ApiKey: str
        :param _Name: API Key 名称。
        :type Name: str
        :param _TeamId: 所属套餐 ID。
        :type TeamId: str
        :param _AppId: 账号APP ID。
        :type AppId: str
        :param _Uin: 主账号 UIN。最大 128 字符。
        :type Uin: str
        :param _AllowedModels: API Key 可用模型列表（JSON 数组字符串）。
        :type AllowedModels: str
        :param _Status: API Key 是否可用。取值：enable（启用）、disable（停用）。
        :type Status: str
        :param _StopReason: API Key 停用原因。取值：NORMAL（正常，默认值），QUOTA_EXHAUSTED（API Key额度包耗尽），ABNORMAL（异常，需人工介入）
        :type StopReason: str
        :param _UseStatus: 用户侧开关。取值：enable（启用）、disable（停用）。
        :type UseStatus: str
        :param _KeyVersion: 密钥版本号。
        :type KeyVersion: int
        :param _LastRotatedAt: 最近一次重置时间。（ISO 8601）
        :type LastRotatedAt: str
        :param _Creator: 创建人，如果是子账号创建，则该值为子账号UIN。
        :type Creator: str
        :param _CreatedAt: 创建时间。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间。
        :type UpdatedAt: str
        :param _Balance: API Key 额度用量信息
        :type Balance: :class:`tencentcloud.tokenhub.v20260322.models.SubPackageBalance`
        :param _ProductType: 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）。
        :type ProductType: str
        """
        self._ApiKeyId = None
        self._ApiKey = None
        self._Name = None
        self._TeamId = None
        self._AppId = None
        self._Uin = None
        self._AllowedModels = None
        self._Status = None
        self._StopReason = None
        self._UseStatus = None
        self._KeyVersion = None
        self._LastRotatedAt = None
        self._Creator = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Balance = None
        self._ProductType = None

    @property
    def ApiKeyId(self):
        r"""API Key ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def ApiKey(self):
        r"""API Key 密钥值（脱敏）。
        :rtype: str
        """
        return self._ApiKey

    @ApiKey.setter
    def ApiKey(self, ApiKey):
        self._ApiKey = ApiKey

    @property
    def Name(self):
        r"""API Key 名称。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def TeamId(self):
        r"""所属套餐 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def AppId(self):
        r"""账号APP ID。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""主账号 UIN。最大 128 字符。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def AllowedModels(self):
        r"""API Key 可用模型列表（JSON 数组字符串）。
        :rtype: str
        """
        return self._AllowedModels

    @AllowedModels.setter
    def AllowedModels(self, AllowedModels):
        self._AllowedModels = AllowedModels

    @property
    def Status(self):
        r"""API Key 是否可用。取值：enable（启用）、disable（停用）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StopReason(self):
        r"""API Key 停用原因。取值：NORMAL（正常，默认值），QUOTA_EXHAUSTED（API Key额度包耗尽），ABNORMAL（异常，需人工介入）
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def UseStatus(self):
        r"""用户侧开关。取值：enable（启用）、disable（停用）。
        :rtype: str
        """
        return self._UseStatus

    @UseStatus.setter
    def UseStatus(self, UseStatus):
        self._UseStatus = UseStatus

    @property
    def KeyVersion(self):
        r"""密钥版本号。
        :rtype: int
        """
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

    @property
    def LastRotatedAt(self):
        r"""最近一次重置时间。（ISO 8601）
        :rtype: str
        """
        return self._LastRotatedAt

    @LastRotatedAt.setter
    def LastRotatedAt(self, LastRotatedAt):
        self._LastRotatedAt = LastRotatedAt

    @property
    def Creator(self):
        r"""创建人，如果是子账号创建，则该值为子账号UIN。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatedAt(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Balance(self):
        r"""API Key 额度用量信息
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.SubPackageBalance`
        """
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def ProductType(self):
        r"""套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）。
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType


    def _deserialize(self, params):
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKey = params.get("ApiKey")
        self._Name = params.get("Name")
        self._TeamId = params.get("TeamId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._AllowedModels = params.get("AllowedModels")
        self._Status = params.get("Status")
        self._StopReason = params.get("StopReason")
        self._UseStatus = params.get("UseStatus")
        self._KeyVersion = params.get("KeyVersion")
        self._LastRotatedAt = params.get("LastRotatedAt")
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("Balance") is not None:
            self._Balance = SubPackageBalance()
            self._Balance._deserialize(params.get("Balance"))
        self._ProductType = params.get("ProductType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenPlanListItem(AbstractModel):
    r"""Token Plan 套餐列表项

    """

    def __init__(self):
        r"""
        :param _TeamId: 套餐 ID。
        :type TeamId: str
        :param _ProductType: 套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）
        :type ProductType: str
        :param _Name: 套餐名称。最大 128 字符。
        :type Name: str
        :param _AppId: 账号 APP ID。
        :type AppId: str
        :param _Uin: 主账号 UIN。
        :type Uin: str
        :param _Status: 套餐状态。取值：enable（启用）、disable（停用）。
        :type Status: str
        :param _StopReason: 套餐关停原因。取值：NORMAL（正常）、ISOLATED（隔离/欠费）、FROZEN（冻结）、EXHAUSTED（额度耗尽）、DESTROYED（已销毁）
        :type StopReason: str
        :param _ApiKeyMax: 可创建 API Key 上限。
        :type ApiKeyMax: int
        :param _PrepayResourceID: 云计费预付费资源包 ID。
        :type PrepayResourceID: str
        :param _Creator: 创建人。若为子账号创建的套餐，则该值为子账号UIN。
        :type Creator: str
        :param _CreatedAt: 创建时间。
        :type CreatedAt: str
        :param _UpdatedAt: 更新时间。
        :type UpdatedAt: str
        :param _PackageInfo: 套餐包基本信息。
        :type PackageInfo: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanPackageInfo`
        :param _AutoRenewFlag: 是否开启自动续费。取值：0（未开启），1（开启）
        :type AutoRenewFlag: int
        """
        self._TeamId = None
        self._ProductType = None
        self._Name = None
        self._AppId = None
        self._Uin = None
        self._Status = None
        self._StopReason = None
        self._ApiKeyMax = None
        self._PrepayResourceID = None
        self._Creator = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._PackageInfo = None
        self._AutoRenewFlag = None

    @property
    def TeamId(self):
        r"""套餐 ID。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def ProductType(self):
        r"""套餐类型。取值：enterprise（企业版专业套餐）、enterprise-auto（企业版轻享套餐）
        :rtype: str
        """
        return self._ProductType

    @ProductType.setter
    def ProductType(self, ProductType):
        self._ProductType = ProductType

    @property
    def Name(self):
        r"""套餐名称。最大 128 字符。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def AppId(self):
        r"""账号 APP ID。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""主账号 UIN。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Status(self):
        r"""套餐状态。取值：enable（启用）、disable（停用）。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StopReason(self):
        r"""套餐关停原因。取值：NORMAL（正常）、ISOLATED（隔离/欠费）、FROZEN（冻结）、EXHAUSTED（额度耗尽）、DESTROYED（已销毁）
        :rtype: str
        """
        return self._StopReason

    @StopReason.setter
    def StopReason(self, StopReason):
        self._StopReason = StopReason

    @property
    def ApiKeyMax(self):
        r"""可创建 API Key 上限。
        :rtype: int
        """
        return self._ApiKeyMax

    @ApiKeyMax.setter
    def ApiKeyMax(self, ApiKeyMax):
        self._ApiKeyMax = ApiKeyMax

    @property
    def PrepayResourceID(self):
        r"""云计费预付费资源包 ID。
        :rtype: str
        """
        return self._PrepayResourceID

    @PrepayResourceID.setter
    def PrepayResourceID(self, PrepayResourceID):
        self._PrepayResourceID = PrepayResourceID

    @property
    def Creator(self):
        r"""创建人。若为子账号创建的套餐，则该值为子账号UIN。
        :rtype: str
        """
        return self._Creator

    @Creator.setter
    def Creator(self, Creator):
        self._Creator = Creator

    @property
    def CreatedAt(self):
        r"""创建时间。
        :rtype: str
        """
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        r"""更新时间。
        :rtype: str
        """
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def PackageInfo(self):
        r"""套餐包基本信息。
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.TokenPlanPackageInfo`
        """
        return self._PackageInfo

    @PackageInfo.setter
    def PackageInfo(self, PackageInfo):
        self._PackageInfo = PackageInfo

    @property
    def AutoRenewFlag(self):
        r"""是否开启自动续费。取值：0（未开启），1（开启）
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._ProductType = params.get("ProductType")
        self._Name = params.get("Name")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Status = params.get("Status")
        self._StopReason = params.get("StopReason")
        self._ApiKeyMax = params.get("ApiKeyMax")
        self._PrepayResourceID = params.get("PrepayResourceID")
        self._Creator = params.get("Creator")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        if params.get("PackageInfo") is not None:
            self._PackageInfo = TokenPlanPackageInfo()
            self._PackageInfo._deserialize(params.get("PackageInfo"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenPlanPackageInfo(AbstractModel):
    r"""主额度包信息

    """

    def __init__(self):
        r"""
        :param _TotalQuota: 总额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :type TotalQuota: str
        :param _TotalUsed: 总已使用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :type TotalUsed: str
        :param _TotalCycles: 总周期数。
        :type TotalCycles: int
        :param _CycleUnit: 周期单位。取值：month（月）
        :type CycleUnit: str
        :param _StartTime: 套餐包生效时间。
        :type StartTime: str
        :param _ExpireTime: 套餐包到期时间。
        :type ExpireTime: str
        :param _ExclusiveAllocated: 独占池已分配额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :type ExclusiveAllocated: str
        :param _ExclusiveUsed: 独占池已用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :type ExclusiveUsed: str
        :param _SharedPool: 共享池总额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :type SharedPool: str
        :param _SharedUsed: 共享已用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :type SharedUsed: str
        :param _CycleQuota: 当期额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :type CycleQuota: str
        :param _CurrentCycle: 当前周期。
        :type CurrentCycle: int
        :param _RemainCycles: 剩余周期。
        :type RemainCycles: int
        """
        self._TotalQuota = None
        self._TotalUsed = None
        self._TotalCycles = None
        self._CycleUnit = None
        self._StartTime = None
        self._ExpireTime = None
        self._ExclusiveAllocated = None
        self._ExclusiveUsed = None
        self._SharedPool = None
        self._SharedUsed = None
        self._CycleQuota = None
        self._CurrentCycle = None
        self._RemainCycles = None

    @property
    def TotalQuota(self):
        r"""总额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :rtype: str
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def TotalUsed(self):
        r"""总已使用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :rtype: str
        """
        return self._TotalUsed

    @TotalUsed.setter
    def TotalUsed(self, TotalUsed):
        self._TotalUsed = TotalUsed

    @property
    def TotalCycles(self):
        r"""总周期数。
        :rtype: int
        """
        return self._TotalCycles

    @TotalCycles.setter
    def TotalCycles(self, TotalCycles):
        self._TotalCycles = TotalCycles

    @property
    def CycleUnit(self):
        r"""周期单位。取值：month（月）
        :rtype: str
        """
        return self._CycleUnit

    @CycleUnit.setter
    def CycleUnit(self, CycleUnit):
        self._CycleUnit = CycleUnit

    @property
    def StartTime(self):
        r"""套餐包生效时间。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def ExpireTime(self):
        r"""套餐包到期时间。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ExclusiveAllocated(self):
        r"""独占池已分配额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :rtype: str
        """
        return self._ExclusiveAllocated

    @ExclusiveAllocated.setter
    def ExclusiveAllocated(self, ExclusiveAllocated):
        self._ExclusiveAllocated = ExclusiveAllocated

    @property
    def ExclusiveUsed(self):
        r"""独占池已用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :rtype: str
        """
        return self._ExclusiveUsed

    @ExclusiveUsed.setter
    def ExclusiveUsed(self, ExclusiveUsed):
        self._ExclusiveUsed = ExclusiveUsed

    @property
    def SharedPool(self):
        r"""共享池总额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :rtype: str
        """
        return self._SharedPool

    @SharedPool.setter
    def SharedPool(self, SharedPool):
        self._SharedPool = SharedPool

    @property
    def SharedUsed(self):
        r"""共享已用额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :rtype: str
        """
        return self._SharedUsed

    @SharedUsed.setter
    def SharedUsed(self, SharedUsed):
        self._SharedUsed = SharedUsed

    @property
    def CycleQuota(self):
        r"""当期额度。根据套餐类型区分单位：credits（企业版专业套餐），tokens（企业版auto套餐）
        :rtype: str
        """
        return self._CycleQuota

    @CycleQuota.setter
    def CycleQuota(self, CycleQuota):
        self._CycleQuota = CycleQuota

    @property
    def CurrentCycle(self):
        r"""当前周期。
        :rtype: int
        """
        return self._CurrentCycle

    @CurrentCycle.setter
    def CurrentCycle(self, CurrentCycle):
        self._CurrentCycle = CurrentCycle

    @property
    def RemainCycles(self):
        r"""剩余周期。
        :rtype: int
        """
        return self._RemainCycles

    @RemainCycles.setter
    def RemainCycles(self, RemainCycles):
        self._RemainCycles = RemainCycles


    def _deserialize(self, params):
        self._TotalQuota = params.get("TotalQuota")
        self._TotalUsed = params.get("TotalUsed")
        self._TotalCycles = params.get("TotalCycles")
        self._CycleUnit = params.get("CycleUnit")
        self._StartTime = params.get("StartTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ExclusiveAllocated = params.get("ExclusiveAllocated")
        self._ExclusiveUsed = params.get("ExclusiveUsed")
        self._SharedPool = params.get("SharedPool")
        self._SharedUsed = params.get("SharedUsed")
        self._CycleQuota = params.get("CycleQuota")
        self._CurrentCycle = params.get("CurrentCycle")
        self._RemainCycles = params.get("RemainCycles")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenSummary(AbstractModel):
    r"""主包Token总结

    """

    def __init__(self):
        r"""
        :param _CycleSeq: 套餐包当前计费周期序号
        :type CycleSeq: int
        :param _CycleStartTime: 套餐包计费周期开始时间（RFC3339）
        :type CycleStartTime: str
        :param _CycleEndTime: 套餐包当前计费周期结束时间（RFC3339）
        :type CycleEndTime: str
        :param _BillingItems: 按计费项分组的 token 汇总列表
        :type BillingItems: list of TokenSummaryBillingItem
        """
        self._CycleSeq = None
        self._CycleStartTime = None
        self._CycleEndTime = None
        self._BillingItems = None

    @property
    def CycleSeq(self):
        r"""套餐包当前计费周期序号
        :rtype: int
        """
        return self._CycleSeq

    @CycleSeq.setter
    def CycleSeq(self, CycleSeq):
        self._CycleSeq = CycleSeq

    @property
    def CycleStartTime(self):
        r"""套餐包计费周期开始时间（RFC3339）
        :rtype: str
        """
        return self._CycleStartTime

    @CycleStartTime.setter
    def CycleStartTime(self, CycleStartTime):
        self._CycleStartTime = CycleStartTime

    @property
    def CycleEndTime(self):
        r"""套餐包当前计费周期结束时间（RFC3339）
        :rtype: str
        """
        return self._CycleEndTime

    @CycleEndTime.setter
    def CycleEndTime(self, CycleEndTime):
        self._CycleEndTime = CycleEndTime

    @property
    def BillingItems(self):
        r"""按计费项分组的 token 汇总列表
        :rtype: list of TokenSummaryBillingItem
        """
        return self._BillingItems

    @BillingItems.setter
    def BillingItems(self, BillingItems):
        self._BillingItems = BillingItems


    def _deserialize(self, params):
        self._CycleSeq = params.get("CycleSeq")
        self._CycleStartTime = params.get("CycleStartTime")
        self._CycleEndTime = params.get("CycleEndTime")
        if params.get("BillingItems") is not None:
            self._BillingItems = []
            for item in params.get("BillingItems"):
                obj = TokenSummaryBillingItem()
                obj._deserialize(item)
                self._BillingItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TokenSummaryBillingItem(AbstractModel):
    r"""Token 汇总计费项

    """

    def __init__(self):
        r"""
        :param _BillingItem: 计费项。取值：input（输入 Token）、output（输出 Token）、cache（缓存 Token）、call_count（调用次数）。
        :type BillingItem: str
        :param _TotalQty: 该计费项在周期内的原始用量汇总，单位：tokens。
        :type TotalQty: int
        """
        self._BillingItem = None
        self._TotalQty = None

    @property
    def BillingItem(self):
        r"""计费项。取值：input（输入 Token）、output（输出 Token）、cache（缓存 Token）、call_count（调用次数）。
        :rtype: str
        """
        return self._BillingItem

    @BillingItem.setter
    def BillingItem(self, BillingItem):
        self._BillingItem = BillingItem

    @property
    def TotalQty(self):
        r"""该计费项在周期内的原始用量汇总，单位：tokens。
        :rtype: int
        """
        return self._TotalQty

    @TotalQty.setter
    def TotalQty(self, TotalQty):
        self._TotalQty = TotalQty


    def _deserialize(self, params):
        self._BillingItem = params.get("BillingItem")
        self._TotalQty = params.get("TotalQty")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeTokenPlanTeamOrderRequest(AbstractModel):
    r"""UpgradeTokenPlanTeamOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TeamId: 套餐 ID。可通过 DescribeTokenPlanList 接口获取。
        :type TeamId: str
        :param _NewCreditOrToken: 升配后的新规格额度。套餐类型为 enterprise 时表示积分额度，套餐类型为 enterprise-auto 时表示 Token 数。必须大于当前额度。
        :type NewCreditOrToken: int
        """
        self._TeamId = None
        self._NewCreditOrToken = None

    @property
    def TeamId(self):
        r"""套餐 ID。可通过 DescribeTokenPlanList 接口获取。
        :rtype: str
        """
        return self._TeamId

    @TeamId.setter
    def TeamId(self, TeamId):
        self._TeamId = TeamId

    @property
    def NewCreditOrToken(self):
        r"""升配后的新规格额度。套餐类型为 enterprise 时表示积分额度，套餐类型为 enterprise-auto 时表示 Token 数。必须大于当前额度。
        :rtype: int
        """
        return self._NewCreditOrToken

    @NewCreditOrToken.setter
    def NewCreditOrToken(self, NewCreditOrToken):
        self._NewCreditOrToken = NewCreditOrToken


    def _deserialize(self, params):
        self._TeamId = params.get("TeamId")
        self._NewCreditOrToken = params.get("NewCreditOrToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpgradeTokenPlanTeamOrderResponse(AbstractModel):
    r"""UpgradeTokenPlanTeamOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BigOrderId: 腾讯云订单 ID。用于关联一次升配操作下的所有子订单。
        :type BigOrderId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BigOrderId = None
        self._RequestId = None

    @property
    def BigOrderId(self):
        r"""腾讯云订单 ID。用于关联一次升配操作下的所有子订单。
        :rtype: str
        """
        return self._BigOrderId

    @BigOrderId.setter
    def BigOrderId(self, BigOrderId):
        self._BigOrderId = BigOrderId

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
        self._BigOrderId = params.get("BigOrderId")
        self._RequestId = params.get("RequestId")


class UsageDetailItem(AbstractModel):
    r"""Token Plan 企业版套餐调用明细项（字段与 CLS 日志对齐）

    """

    def __init__(self):
        r"""
        :param _Uin: 主账号 UIN。
        :type Uin: str
        :param _ModelName: 模型名称。
        :type ModelName: str
        :param _ApiKeyId: APIKey ID。
        :type ApiKeyId: str
        :param _ApiKeyName: APIKey 名称。
        :type ApiKeyName: str
        :param _RequestId: 请求 ID。
        :type RequestId: str
        :param _RequestTime: 请求时间（RFC3339 格式）。
        :type RequestTime: str
        :param _InputToken: 输入 token 数。
        :type InputToken: int
        :param _CacheToken: 缓存 token 数。
        :type CacheToken: int
        :param _OutputToken: 输出 token 数。
        :type OutputToken: int
        :param _TotalToken: 总 token 数。
        :type TotalToken: int
        :param _InputQuota: 未命中缓存输入消耗额度。单位说明如下：
- 套餐类型为专业套餐（enterprise），单位取值为积分；
- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。
        :type InputQuota: str
        :param _CacheQuota: 缓存消耗额度。单位说明如下：
- 套餐类型为专业套餐（enterprise），单位取值为积分；
- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。
        :type CacheQuota: str
        :param _OutputQuota: 输出消耗额度。单位说明如下：
- 套餐类型为专业套餐（enterprise），单位取值为积分；
- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。
        :type OutputQuota: str
        :param _TotalQuota: 总消耗额度。单位说明如下：
- 套餐类型为专业套餐（enterprise），单位取值为积分；
- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。
        :type TotalQuota: str
        """
        self._Uin = None
        self._ModelName = None
        self._ApiKeyId = None
        self._ApiKeyName = None
        self._RequestId = None
        self._RequestTime = None
        self._InputToken = None
        self._CacheToken = None
        self._OutputToken = None
        self._TotalToken = None
        self._InputQuota = None
        self._CacheQuota = None
        self._OutputQuota = None
        self._TotalQuota = None

    @property
    def Uin(self):
        r"""主账号 UIN。
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def ModelName(self):
        r"""模型名称。
        :rtype: str
        """
        return self._ModelName

    @ModelName.setter
    def ModelName(self, ModelName):
        self._ModelName = ModelName

    @property
    def ApiKeyId(self):
        r"""APIKey ID。
        :rtype: str
        """
        return self._ApiKeyId

    @ApiKeyId.setter
    def ApiKeyId(self, ApiKeyId):
        self._ApiKeyId = ApiKeyId

    @property
    def ApiKeyName(self):
        r"""APIKey 名称。
        :rtype: str
        """
        return self._ApiKeyName

    @ApiKeyName.setter
    def ApiKeyName(self, ApiKeyName):
        self._ApiKeyName = ApiKeyName

    @property
    def RequestId(self):
        r"""请求 ID。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId

    @property
    def RequestTime(self):
        r"""请求时间（RFC3339 格式）。
        :rtype: str
        """
        return self._RequestTime

    @RequestTime.setter
    def RequestTime(self, RequestTime):
        self._RequestTime = RequestTime

    @property
    def InputToken(self):
        r"""输入 token 数。
        :rtype: int
        """
        return self._InputToken

    @InputToken.setter
    def InputToken(self, InputToken):
        self._InputToken = InputToken

    @property
    def CacheToken(self):
        r"""缓存 token 数。
        :rtype: int
        """
        return self._CacheToken

    @CacheToken.setter
    def CacheToken(self, CacheToken):
        self._CacheToken = CacheToken

    @property
    def OutputToken(self):
        r"""输出 token 数。
        :rtype: int
        """
        return self._OutputToken

    @OutputToken.setter
    def OutputToken(self, OutputToken):
        self._OutputToken = OutputToken

    @property
    def TotalToken(self):
        r"""总 token 数。
        :rtype: int
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        self._TotalToken = TotalToken

    @property
    def InputQuota(self):
        r"""未命中缓存输入消耗额度。单位说明如下：
- 套餐类型为专业套餐（enterprise），单位取值为积分；
- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。
        :rtype: str
        """
        return self._InputQuota

    @InputQuota.setter
    def InputQuota(self, InputQuota):
        self._InputQuota = InputQuota

    @property
    def CacheQuota(self):
        r"""缓存消耗额度。单位说明如下：
- 套餐类型为专业套餐（enterprise），单位取值为积分；
- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。
        :rtype: str
        """
        return self._CacheQuota

    @CacheQuota.setter
    def CacheQuota(self, CacheQuota):
        self._CacheQuota = CacheQuota

    @property
    def OutputQuota(self):
        r"""输出消耗额度。单位说明如下：
- 套餐类型为专业套餐（enterprise），单位取值为积分；
- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。
        :rtype: str
        """
        return self._OutputQuota

    @OutputQuota.setter
    def OutputQuota(self, OutputQuota):
        self._OutputQuota = OutputQuota

    @property
    def TotalQuota(self):
        r"""总消耗额度。单位说明如下：
- 套餐类型为专业套餐（enterprise），单位取值为积分；
- 套餐类型轻享套餐（enterprise-auto），单位取值为 token。
        :rtype: str
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._ModelName = params.get("ModelName")
        self._ApiKeyId = params.get("ApiKeyId")
        self._ApiKeyName = params.get("ApiKeyName")
        self._RequestId = params.get("RequestId")
        self._RequestTime = params.get("RequestTime")
        self._InputToken = params.get("InputToken")
        self._CacheToken = params.get("CacheToken")
        self._OutputToken = params.get("OutputToken")
        self._TotalToken = params.get("TotalToken")
        self._InputQuota = params.get("InputQuota")
        self._CacheQuota = params.get("CacheQuota")
        self._OutputQuota = params.get("OutputQuota")
        self._TotalQuota = params.get("TotalQuota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageRankItem(AbstractModel):
    r"""排行列表中的单个对象用量项，含对象标识、时间周期内的统计值（Stats）和时间周期内的时序点列表（Series，仅 ShowAll=false 时返回）。

    """

    def __init__(self):
        r"""
        :param _Rank: 全局排名（从 1 起）。分页场景下仍为全量排序中的位次，非页内序号
        :type Rank: int
        :param _Key: 对象标识。apikey 维度为 APIKey ID；endpoint 维度为接入点；model 维度为模型名。
        :type Key: str
        :param _Name: 对象展示名。apikey 维度返回 APIKey 名称（已删除的 APIKey 仍保留原名）；
endpoint / model 维度等于 Key。
        :type Name: str
        :param _Stats: 时间周期内的统计值
注意：此字段可能返回 null，表示取不到有效值。
        :type Stats: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        :param _Series: 时间周期内的时序点列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Series: :class:`tencentcloud.tokenhub.v20260322.models.UsageSeries`
        """
        self._Rank = None
        self._Key = None
        self._Name = None
        self._Stats = None
        self._Series = None

    @property
    def Rank(self):
        r"""全局排名（从 1 起）。分页场景下仍为全量排序中的位次，非页内序号
        :rtype: int
        """
        return self._Rank

    @Rank.setter
    def Rank(self, Rank):
        self._Rank = Rank

    @property
    def Key(self):
        r"""对象标识。apikey 维度为 APIKey ID；endpoint 维度为接入点；model 维度为模型名。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Name(self):
        r"""对象展示名。apikey 维度返回 APIKey 名称（已删除的 APIKey 仍保留原名）；
endpoint / model 维度等于 Key。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Stats(self):
        r"""时间周期内的统计值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UsageStats`
        """
        return self._Stats

    @Stats.setter
    def Stats(self, Stats):
        self._Stats = Stats

    @property
    def Series(self):
        r"""时间周期内的时序点列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tokenhub.v20260322.models.UsageSeries`
        """
        return self._Series

    @Series.setter
    def Series(self, Series):
        self._Series = Series


    def _deserialize(self, params):
        self._Rank = params.get("Rank")
        self._Key = params.get("Key")
        self._Name = params.get("Name")
        if params.get("Stats") is not None:
            self._Stats = UsageStats()
            self._Stats._deserialize(params.get("Stats"))
        if params.get("Series") is not None:
            self._Series = UsageSeries()
            self._Series._deserialize(params.get("Series"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageSeries(AbstractModel):
    r"""用量时间周期内的时序点列表（按 metric key 索引）。为 JSON 数组的字符串形式,数组长度与响应 Timestamps 一致，无数据点处为 null。具体包含哪些 key 由响应 MetricKeys 决定。

    """

    def __init__(self):
        r"""
        :param _TotalToken: 总 token 数用量时间周期内的 JSON 字符串形式，如 `"[12,null,15]"`。
        :type TotalToken: str
        :param _InputTotalToken: 输入 token 数用量时间周期内的 JSON 字符串形式，如 `"[7,null,9]"`。
        :type InputTotalToken: str
        :param _OutputTotalToken: 输出 token 数用量时间周期内的 JSON 字符串形式，如 `"[5,null,6]"`。
        :type OutputTotalToken: str
        """
        self._TotalToken = None
        self._InputTotalToken = None
        self._OutputTotalToken = None

    @property
    def TotalToken(self):
        r"""总 token 数用量时间周期内的 JSON 字符串形式，如 `"[12,null,15]"`。
        :rtype: str
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        self._TotalToken = TotalToken

    @property
    def InputTotalToken(self):
        r"""输入 token 数用量时间周期内的 JSON 字符串形式，如 `"[7,null,9]"`。
        :rtype: str
        """
        return self._InputTotalToken

    @InputTotalToken.setter
    def InputTotalToken(self, InputTotalToken):
        self._InputTotalToken = InputTotalToken

    @property
    def OutputTotalToken(self):
        r"""输出 token 数用量时间周期内的 JSON 字符串形式，如 `"[5,null,6]"`。
        :rtype: str
        """
        return self._OutputTotalToken

    @OutputTotalToken.setter
    def OutputTotalToken(self, OutputTotalToken):
        self._OutputTotalToken = OutputTotalToken


    def _deserialize(self, params):
        self._TotalToken = params.get("TotalToken")
        self._InputTotalToken = params.get("InputTotalToken")
        self._OutputTotalToken = params.get("OutputTotalToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UsageStats(AbstractModel):
    r"""时间周期内的统计聚合值（按 metric key 索引）。本期返回 tokens 族（statistics=sum）的累计 Token 用量；具体包含哪些 key、顺序如何，参见响应顶层 `MetricKeys` 字段。接口预留 MetricType 字段以支持后续指标族扩展，本期仅支持 tokens。

    """

    def __init__(self):
        r"""
        :param _TotalToken: 时间周期内的累计总 token 数。
        :type TotalToken: int
        :param _InputTotalToken: 时间周期内的累计输入 token 数。
        :type InputTotalToken: int
        :param _OutputTotalToken: 时间周期内的累计输出 token 数。
        :type OutputTotalToken: int
        """
        self._TotalToken = None
        self._InputTotalToken = None
        self._OutputTotalToken = None

    @property
    def TotalToken(self):
        r"""时间周期内的累计总 token 数。
        :rtype: int
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        self._TotalToken = TotalToken

    @property
    def InputTotalToken(self):
        r"""时间周期内的累计输入 token 数。
        :rtype: int
        """
        return self._InputTotalToken

    @InputTotalToken.setter
    def InputTotalToken(self, InputTotalToken):
        self._InputTotalToken = InputTotalToken

    @property
    def OutputTotalToken(self):
        r"""时间周期内的累计输出 token 数。
        :rtype: int
        """
        return self._OutputTotalToken

    @OutputTotalToken.setter
    def OutputTotalToken(self, OutputTotalToken):
        self._OutputTotalToken = OutputTotalToken


    def _deserialize(self, params):
        self._TotalToken = params.get("TotalToken")
        self._InputTotalToken = params.get("InputTotalToken")
        self._OutputTotalToken = params.get("OutputTotalToken")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        