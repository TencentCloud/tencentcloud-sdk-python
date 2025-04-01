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


class CreateIncrementalMigrationStrategyRequest(AbstractModel):
    """CreateIncrementalMigrationStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAppId: <b>点播[专业版](/document/product/266/115396)[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _BucketId: 策略生效的存储桶 ID。
        :type BucketId: str
        :param _StrategyName: 增量迁移策略名称，名称长度不超过100个字符，允许的字符为：`中文、英文、0-9、_、-`。
        :type StrategyName: str
        :param _OriginType: 源站类型。取值有：
<li>HTTP：HTTP 源。</li>
        :type OriginType: str
        :param _HttpOriginConfig: 增量迁移 HTTP 回源源站配置，当 OriginType 取值 `HTTP` 时必填。
        :type HttpOriginConfig: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginConfig`
        """
        self._SubAppId = None
        self._BucketId = None
        self._StrategyName = None
        self._OriginType = None
        self._HttpOriginConfig = None

    @property
    def SubAppId(self):
        """<b>点播[专业版](/document/product/266/115396)[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def BucketId(self):
        """策略生效的存储桶 ID。
        :rtype: str
        """
        return self._BucketId

    @BucketId.setter
    def BucketId(self, BucketId):
        self._BucketId = BucketId

    @property
    def StrategyName(self):
        """增量迁移策略名称，名称长度不超过100个字符，允许的字符为：`中文、英文、0-9、_、-`。
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def OriginType(self):
        """源站类型。取值有：
<li>HTTP：HTTP 源。</li>
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def HttpOriginConfig(self):
        """增量迁移 HTTP 回源源站配置，当 OriginType 取值 `HTTP` 时必填。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginConfig`
        """
        return self._HttpOriginConfig

    @HttpOriginConfig.setter
    def HttpOriginConfig(self, HttpOriginConfig):
        self._HttpOriginConfig = HttpOriginConfig


    def _deserialize(self, params):
        self._SubAppId = params.get("SubAppId")
        self._BucketId = params.get("BucketId")
        self._StrategyName = params.get("StrategyName")
        self._OriginType = params.get("OriginType")
        if params.get("HttpOriginConfig") is not None:
            self._HttpOriginConfig = IncrementalMigrationHttpOriginConfig()
            self._HttpOriginConfig._deserialize(params.get("HttpOriginConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIncrementalMigrationStrategyResponse(AbstractModel):
    """CreateIncrementalMigrationStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyId: 增量迁移策略 ID。
        :type StrategyId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._StrategyId = None
        self._RequestId = None

    @property
    def StrategyId(self):
        """增量迁移策略 ID。
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

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
        self._StrategyId = params.get("StrategyId")
        self._RequestId = params.get("RequestId")


class CreateStorageCredentialsRequest(AbstractModel):
    """CreateStorageCredentials请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAppId: <b>点播专业版[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _Policy: 按照下方语法组装好策略后，先序列化为字符串，再做 URL Encode，结果作为 Policy 字段入参。服务端会对该字段做 URL Decode，并按解析后的策略授予临时访问凭证权限，请按规范传入参数。
注意： 
1.策略语法参照[访问管理策略](/document/product/598/10603)。
2.策略中不能包含 principal 元素。
3.策略的 action 元素仅支持：<li>name/vod:PutObject;</li><li>name/vod:ListParts;</li><li>name/vod:PostObject;</li><li>name/vod:InitiateMultipartUpload;</li><li>name/vod:UploadPart;</li><li>name/vod:CompleteMultipartUpload;</li><li>name/vod:AbortMultipartUpload;</li><li>name/vod:ListMultipartUploads;</li>4.策略的 resource 元素填写格式为：`qcs::vod:[存储地域]:uid/[账号AppID]:prefix//[点播应用ID]/[存储桶ID]/[存储路径]`，其中存储地域、账号 AppID、点播应用 ID、存储桶 ID 和存储路径要按需填写，其他内容不允许改动，例：`qcs:ap-chongqing:vod::uid/1231456789:prefix//1234567890/2ceds3ew323w3mu/file_path`。

        :type Policy: str
        :param _DurationSeconds: 指定临时证书的有效期，单位：秒。
默认 1800 秒，最大 129600 秒。
        :type DurationSeconds: int
        """
        self._SubAppId = None
        self._Policy = None
        self._DurationSeconds = None

    @property
    def SubAppId(self):
        """<b>点播专业版[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def Policy(self):
        """按照下方语法组装好策略后，先序列化为字符串，再做 URL Encode，结果作为 Policy 字段入参。服务端会对该字段做 URL Decode，并按解析后的策略授予临时访问凭证权限，请按规范传入参数。
注意： 
1.策略语法参照[访问管理策略](/document/product/598/10603)。
2.策略中不能包含 principal 元素。
3.策略的 action 元素仅支持：<li>name/vod:PutObject;</li><li>name/vod:ListParts;</li><li>name/vod:PostObject;</li><li>name/vod:InitiateMultipartUpload;</li><li>name/vod:UploadPart;</li><li>name/vod:CompleteMultipartUpload;</li><li>name/vod:AbortMultipartUpload;</li><li>name/vod:ListMultipartUploads;</li>4.策略的 resource 元素填写格式为：`qcs::vod:[存储地域]:uid/[账号AppID]:prefix//[点播应用ID]/[存储桶ID]/[存储路径]`，其中存储地域、账号 AppID、点播应用 ID、存储桶 ID 和存储路径要按需填写，其他内容不允许改动，例：`qcs:ap-chongqing:vod::uid/1231456789:prefix//1234567890/2ceds3ew323w3mu/file_path`。

        :rtype: str
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def DurationSeconds(self):
        """指定临时证书的有效期，单位：秒。
默认 1800 秒，最大 129600 秒。
        :rtype: int
        """
        return self._DurationSeconds

    @DurationSeconds.setter
    def DurationSeconds(self, DurationSeconds):
        self._DurationSeconds = DurationSeconds


    def _deserialize(self, params):
        self._SubAppId = params.get("SubAppId")
        self._Policy = params.get("Policy")
        self._DurationSeconds = params.get("DurationSeconds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStorageCredentialsResponse(AbstractModel):
    """CreateStorageCredentials返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Credentials: 临时访问凭证。
        :type Credentials: :class:`tencentcloud.vod.v20240718.models.Credentials`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Credentials = None
        self._RequestId = None

    @property
    def Credentials(self):
        """临时访问凭证。
        :rtype: :class:`tencentcloud.vod.v20240718.models.Credentials`
        """
        return self._Credentials

    @Credentials.setter
    def Credentials(self, Credentials):
        self._Credentials = Credentials

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
        if params.get("Credentials") is not None:
            self._Credentials = Credentials()
            self._Credentials._deserialize(params.get("Credentials"))
        self._RequestId = params.get("RequestId")


class CreateStorageRequest(AbstractModel):
    """CreateStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAppId: <b>点播专业版[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _StorageRegion: 存储地域，必须是系统支持地域。
通过 [DescribeStorageRegions](https://cloud.tencent.com/document/product/266/72480) 接口可以查询到所有存储地域及已经开通存储桶的地域。
        :type StorageRegion: str
        :param _StorageName: 存储名称。
<li>仅支持小写英文字母、数字、中划线 “-” 及其组合；</li>
<li>存储命名不能以 “-” 开头或结尾；</li>
<li>存储命名最大长度为 64 字符。</li>
        :type StorageName: str
        """
        self._SubAppId = None
        self._StorageRegion = None
        self._StorageName = None

    @property
    def SubAppId(self):
        """<b>点播专业版[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def StorageRegion(self):
        """存储地域，必须是系统支持地域。
通过 [DescribeStorageRegions](https://cloud.tencent.com/document/product/266/72480) 接口可以查询到所有存储地域及已经开通存储桶的地域。
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def StorageName(self):
        """存储名称。
<li>仅支持小写英文字母、数字、中划线 “-” 及其组合；</li>
<li>存储命名不能以 “-” 开头或结尾；</li>
<li>存储命名最大长度为 64 字符。</li>
        :rtype: str
        """
        return self._StorageName

    @StorageName.setter
    def StorageName(self, StorageName):
        self._StorageName = StorageName


    def _deserialize(self, params):
        self._SubAppId = params.get("SubAppId")
        self._StorageRegion = params.get("StorageRegion")
        self._StorageName = params.get("StorageName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStorageResponse(AbstractModel):
    """CreateStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BucketId: 存储桶 ID。
        :type BucketId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BucketId = None
        self._RequestId = None

    @property
    def BucketId(self):
        """存储桶 ID。
        :rtype: str
        """
        return self._BucketId

    @BucketId.setter
    def BucketId(self, BucketId):
        self._BucketId = BucketId

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
        self._BucketId = params.get("BucketId")
        self._RequestId = params.get("RequestId")


class Credentials(AbstractModel):
    """临时访问凭证。

    """

    def __init__(self):
        r"""
        :param _AccessKeyId: 访问凭证 ID。
        :type AccessKeyId: str
        :param _SecretAccessKey: 访问凭证 Key。
        :type SecretAccessKey: str
        :param _SessionToken: 访问凭证 Token，长度和绑定的策略有关，最长不超过 4096 字节。
        :type SessionToken: str
        :param _Expiration: 访问凭证的过期时间。
        :type Expiration: str
        """
        self._AccessKeyId = None
        self._SecretAccessKey = None
        self._SessionToken = None
        self._Expiration = None

    @property
    def AccessKeyId(self):
        """访问凭证 ID。
        :rtype: str
        """
        return self._AccessKeyId

    @AccessKeyId.setter
    def AccessKeyId(self, AccessKeyId):
        self._AccessKeyId = AccessKeyId

    @property
    def SecretAccessKey(self):
        """访问凭证 Key。
        :rtype: str
        """
        return self._SecretAccessKey

    @SecretAccessKey.setter
    def SecretAccessKey(self, SecretAccessKey):
        self._SecretAccessKey = SecretAccessKey

    @property
    def SessionToken(self):
        """访问凭证 Token，长度和绑定的策略有关，最长不超过 4096 字节。
        :rtype: str
        """
        return self._SessionToken

    @SessionToken.setter
    def SessionToken(self, SessionToken):
        self._SessionToken = SessionToken

    @property
    def Expiration(self):
        """访问凭证的过期时间。
        :rtype: str
        """
        return self._Expiration

    @Expiration.setter
    def Expiration(self, Expiration):
        self._Expiration = Expiration


    def _deserialize(self, params):
        self._AccessKeyId = params.get("AccessKeyId")
        self._SecretAccessKey = params.get("SecretAccessKey")
        self._SessionToken = params.get("SessionToken")
        self._Expiration = params.get("Expiration")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIncrementalMigrationStrategyRequest(AbstractModel):
    """DeleteIncrementalMigrationStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAppId: <b>点播[专业版](/document/product/266/115396)[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _BucketId: 策略生效的存储桶 ID。
        :type BucketId: str
        :param _StrategyId: 增量迁移策略 ID。
        :type StrategyId: str
        """
        self._SubAppId = None
        self._BucketId = None
        self._StrategyId = None

    @property
    def SubAppId(self):
        """<b>点播[专业版](/document/product/266/115396)[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def BucketId(self):
        """策略生效的存储桶 ID。
        :rtype: str
        """
        return self._BucketId

    @BucketId.setter
    def BucketId(self, BucketId):
        self._BucketId = BucketId

    @property
    def StrategyId(self):
        """增量迁移策略 ID。
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._SubAppId = params.get("SubAppId")
        self._BucketId = params.get("BucketId")
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIncrementalMigrationStrategyResponse(AbstractModel):
    """DeleteIncrementalMigrationStrategy返回参数结构体

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


class DescribeIncrementalMigrationStrategyInfosRequest(AbstractModel):
    """DescribeIncrementalMigrationStrategyInfos请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAppId: <b>点播[专业版](/document/product/266/115396)[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _Filters: 过滤条件，Filters.Values 的上限为 `20`；若 Filters 长度为 `0` 则查询时无过滤条件限制。 详细的过滤条件如下： <li>BucketId<br>   按照【<strong>存储桶 ID</strong>】进行过滤<br>   类型：String<br>   必选：否<br></li><li>StrategyId<br>   按照【<strong>策略 ID</strong>】进行过滤。<br>   类型：String<br>   必选：否</li> 
        :type Filters: list of Filter
        :param _SortBy: 返回结果的排序。 SortBy.Field 取值有：<li>UpdateTime：创建时间。</li>若不填，SortBy.Field 默认值为 `UpdateTime`，SortBy.Order 默认值为 `Desc`。
        :type SortBy: :class:`tencentcloud.vod.v20240718.models.SortBy`
        :param _Offset: 分页返回的起始偏移量，默认值为 `0`。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值为 `20`，最大值为 `100`。
        :type Limit: int
        """
        self._SubAppId = None
        self._Filters = None
        self._SortBy = None
        self._Offset = None
        self._Limit = None

    @property
    def SubAppId(self):
        """<b>点播[专业版](/document/product/266/115396)[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def Filters(self):
        """过滤条件，Filters.Values 的上限为 `20`；若 Filters 长度为 `0` 则查询时无过滤条件限制。 详细的过滤条件如下： <li>BucketId<br>   按照【<strong>存储桶 ID</strong>】进行过滤<br>   类型：String<br>   必选：否<br></li><li>StrategyId<br>   按照【<strong>策略 ID</strong>】进行过滤。<br>   类型：String<br>   必选：否</li> 
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        """返回结果的排序。 SortBy.Field 取值有：<li>UpdateTime：创建时间。</li>若不填，SortBy.Field 默认值为 `UpdateTime`，SortBy.Order 默认值为 `Desc`。
        :rtype: :class:`tencentcloud.vod.v20240718.models.SortBy`
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Offset(self):
        """分页返回的起始偏移量，默认值为 `0`。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页返回的记录条数，默认值为 `20`，最大值为 `100`。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SubAppId = params.get("SubAppId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortBy") is not None:
            self._SortBy = SortBy()
            self._SortBy._deserialize(params.get("SortBy"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIncrementalMigrationStrategyInfosResponse(AbstractModel):
    """DescribeIncrementalMigrationStrategyInfos返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数。
        :type TotalCount: int
        :param _StrategyInfoSet: 策略信息集合。
        :type StrategyInfoSet: list of IncrementalMigrationStrategyInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._StrategyInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StrategyInfoSet(self):
        """策略信息集合。
        :rtype: list of IncrementalMigrationStrategyInfo
        """
        return self._StrategyInfoSet

    @StrategyInfoSet.setter
    def StrategyInfoSet(self, StrategyInfoSet):
        self._StrategyInfoSet = StrategyInfoSet

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
        if params.get("StrategyInfoSet") is not None:
            self._StrategyInfoSet = []
            for item in params.get("StrategyInfoSet"):
                obj = IncrementalMigrationStrategyInfo()
                obj._deserialize(item)
                self._StrategyInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStorageRequest(AbstractModel):
    """DescribeStorage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAppId: <b>点播专业版[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _Filters: 过滤条件，Filters.Values 的上限为 20；若 Filters 长度为 0 则分页查询子应用 SubAppId 下的存储信息。 详细的过滤条件如下：
<li>BucketId<br>   按照【<strong>存储桶 ID</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
<li>StorageName<br>   按照【<strong>存储名称</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
        :type Filters: list of Filter
        :param _SortBy: 返回结果的排序。 SortBy.Field 取值有：
<li>CreateTime：创建时间。</li>若不填，SortBy.Field 默认值为 CreateTime，SortBy.Order 默认值为 Asc。
        :type SortBy: :class:`tencentcloud.vod.v20240718.models.SortBy`
        :param _Offset: 分页返回的起始偏移量，默认值为 0。
        :type Offset: int
        :param _Limit: 分页返回的记录条数，默认值为 20，最大值为 1000。
        :type Limit: int
        """
        self._SubAppId = None
        self._Filters = None
        self._SortBy = None
        self._Offset = None
        self._Limit = None

    @property
    def SubAppId(self):
        """<b>点播专业版[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def Filters(self):
        """过滤条件，Filters.Values 的上限为 20；若 Filters 长度为 0 则分页查询子应用 SubAppId 下的存储信息。 详细的过滤条件如下：
<li>BucketId<br>   按照【<strong>存储桶 ID</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
<li>StorageName<br>   按照【<strong>存储名称</strong>】进行过滤。<br>   类型：String<br>   必选：否</li>
        :rtype: list of Filter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def SortBy(self):
        """返回结果的排序。 SortBy.Field 取值有：
<li>CreateTime：创建时间。</li>若不填，SortBy.Field 默认值为 CreateTime，SortBy.Order 默认值为 Asc。
        :rtype: :class:`tencentcloud.vod.v20240718.models.SortBy`
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def Offset(self):
        """分页返回的起始偏移量，默认值为 0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页返回的记录条数，默认值为 20，最大值为 1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._SubAppId = params.get("SubAppId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("SortBy") is not None:
            self._SortBy = SortBy()
            self._SortBy._deserialize(params.get("SortBy"))
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStorageResponse(AbstractModel):
    """DescribeStorage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 符合条件的存储数量。
        :type TotalCount: int
        :param _StorageInfoSet: 符合条件的存储信息列表。
        :type StorageInfoSet: list of StorageInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._StorageInfoSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """符合条件的存储数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def StorageInfoSet(self):
        """符合条件的存储信息列表。
        :rtype: list of StorageInfo
        """
        return self._StorageInfoSet

    @StorageInfoSet.setter
    def StorageInfoSet(self, StorageInfoSet):
        self._StorageInfoSet = StorageInfoSet

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
        if params.get("StorageInfoSet") is not None:
            self._StorageInfoSet = []
            for item in params.get("StorageInfoSet"):
                obj = StorageInfo()
                obj._deserialize(item)
                self._StorageInfoSet.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """键值对过滤器，用于条件过滤查询。例如过滤 ID、名称或状态等。
    若存在多个 Filter 时，Filter 间的关系为逻辑与（AND）关系。
    若同一个 Filter 存在多个 Values，同一 Filter 下 Values 间的关系为逻辑或（OR）关系。

    过滤器筛选字段均为精确匹配。

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
        


class IncrementalMigrationHttpEndpointInfo(AbstractModel):
    """增量迁移源站地址信息。

    """

    def __init__(self):
        r"""
        :param _Endpoint: 地址信息，支持域名或 IP 地址。
        :type Endpoint: str
        :param _StandbyEndpointSet: 备份地址信息。
        :type StandbyEndpointSet: list of str
        """
        self._Endpoint = None
        self._StandbyEndpointSet = None

    @property
    def Endpoint(self):
        """地址信息，支持域名或 IP 地址。
        :rtype: str
        """
        return self._Endpoint

    @Endpoint.setter
    def Endpoint(self, Endpoint):
        self._Endpoint = Endpoint

    @property
    def StandbyEndpointSet(self):
        """备份地址信息。
        :rtype: list of str
        """
        return self._StandbyEndpointSet

    @StandbyEndpointSet.setter
    def StandbyEndpointSet(self, StandbyEndpointSet):
        self._StandbyEndpointSet = StandbyEndpointSet


    def _deserialize(self, params):
        self._Endpoint = params.get("Endpoint")
        self._StandbyEndpointSet = params.get("StandbyEndpointSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationHttpHeader(AbstractModel):
    """增量迁移回源 HTTP Header。

    """

    def __init__(self):
        r"""
        :param _Key: Header 键。
        :type Key: str
        :param _Value: Header 值。
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """Header 键。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """Header 值。
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
        


class IncrementalMigrationHttpHeaderInfo(AbstractModel):
    """增量迁移回源 HTTP Header 信息。

    """

    def __init__(self):
        r"""
        :param _HeaderFollowMode: Http Header 透传模式。取值有：
<li>FOLLOW_ALL：透传所有头部信息；</li>
<li>FOLLOW_PART：透传部分头部信息；</li>
<li>IGNORE_PART：忽略部分头部信息。</li>参数必填。
        :type HeaderFollowMode: str
        :param _FollowHttpHeaderKeySet: 需透传 Header Key 集合，仅当 HeaderFollowMode 取值 `FOLLOW_PART` 时需要填充。
        :type FollowHttpHeaderKeySet: list of str
        :param _NewHttpHeaderSet: 新增 Header 键值对集合。
        :type NewHttpHeaderSet: list of IncrementalMigrationHttpHeader
        """
        self._HeaderFollowMode = None
        self._FollowHttpHeaderKeySet = None
        self._NewHttpHeaderSet = None

    @property
    def HeaderFollowMode(self):
        """Http Header 透传模式。取值有：
<li>FOLLOW_ALL：透传所有头部信息；</li>
<li>FOLLOW_PART：透传部分头部信息；</li>
<li>IGNORE_PART：忽略部分头部信息。</li>参数必填。
        :rtype: str
        """
        return self._HeaderFollowMode

    @HeaderFollowMode.setter
    def HeaderFollowMode(self, HeaderFollowMode):
        self._HeaderFollowMode = HeaderFollowMode

    @property
    def FollowHttpHeaderKeySet(self):
        """需透传 Header Key 集合，仅当 HeaderFollowMode 取值 `FOLLOW_PART` 时需要填充。
        :rtype: list of str
        """
        return self._FollowHttpHeaderKeySet

    @FollowHttpHeaderKeySet.setter
    def FollowHttpHeaderKeySet(self, FollowHttpHeaderKeySet):
        self._FollowHttpHeaderKeySet = FollowHttpHeaderKeySet

    @property
    def NewHttpHeaderSet(self):
        """新增 Header 键值对集合。
        :rtype: list of IncrementalMigrationHttpHeader
        """
        return self._NewHttpHeaderSet

    @NewHttpHeaderSet.setter
    def NewHttpHeaderSet(self, NewHttpHeaderSet):
        self._NewHttpHeaderSet = NewHttpHeaderSet


    def _deserialize(self, params):
        self._HeaderFollowMode = params.get("HeaderFollowMode")
        self._FollowHttpHeaderKeySet = params.get("FollowHttpHeaderKeySet")
        if params.get("NewHttpHeaderSet") is not None:
            self._NewHttpHeaderSet = []
            for item in params.get("NewHttpHeaderSet"):
                obj = IncrementalMigrationHttpHeader()
                obj._deserialize(item)
                self._NewHttpHeaderSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationHttpOriginCondition(AbstractModel):
    """增量迁移回源条件。

    """

    def __init__(self):
        r"""
        :param _HttpStatusCode: 触发回源条件的 HTTP Code。若不填充，默认取值 `404`。
        :type HttpStatusCode: int
        :param _Prefix: 触发回源条件的对象键前缀。
        :type Prefix: str
        """
        self._HttpStatusCode = None
        self._Prefix = None

    @property
    def HttpStatusCode(self):
        """触发回源条件的 HTTP Code。若不填充，默认取值 `404`。
        :rtype: int
        """
        return self._HttpStatusCode

    @HttpStatusCode.setter
    def HttpStatusCode(self, HttpStatusCode):
        self._HttpStatusCode = HttpStatusCode

    @property
    def Prefix(self):
        """触发回源条件的对象键前缀。
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix


    def _deserialize(self, params):
        self._HttpStatusCode = params.get("HttpStatusCode")
        self._Prefix = params.get("Prefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationHttpOriginConfig(AbstractModel):
    """增量迁移回源源站配置。

    """

    def __init__(self):
        r"""
        :param _OriginInfo: 回源源站信息。
        :type OriginInfo: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginInfo`
        :param _OriginParameter: 回源参数。
        :type OriginParameter: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginParameter`
        :param _Mode: 回源模式。取值有：
<li>SYNC：同步回源；</li>
<li>ASYNC：异步回源。</li>若不填，默认取 `SYNC` 同步回源。
        :type Mode: str
        :param _OriginCondition: 回源条件。
        :type OriginCondition: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginCondition`
        """
        self._OriginInfo = None
        self._OriginParameter = None
        self._Mode = None
        self._OriginCondition = None

    @property
    def OriginInfo(self):
        """回源源站信息。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginInfo`
        """
        return self._OriginInfo

    @OriginInfo.setter
    def OriginInfo(self, OriginInfo):
        self._OriginInfo = OriginInfo

    @property
    def OriginParameter(self):
        """回源参数。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginParameter`
        """
        return self._OriginParameter

    @OriginParameter.setter
    def OriginParameter(self, OriginParameter):
        self._OriginParameter = OriginParameter

    @property
    def Mode(self):
        """回源模式。取值有：
<li>SYNC：同步回源；</li>
<li>ASYNC：异步回源。</li>若不填，默认取 `SYNC` 同步回源。
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def OriginCondition(self):
        """回源条件。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginCondition`
        """
        return self._OriginCondition

    @OriginCondition.setter
    def OriginCondition(self, OriginCondition):
        self._OriginCondition = OriginCondition


    def _deserialize(self, params):
        if params.get("OriginInfo") is not None:
            self._OriginInfo = IncrementalMigrationHttpOriginInfo()
            self._OriginInfo._deserialize(params.get("OriginInfo"))
        if params.get("OriginParameter") is not None:
            self._OriginParameter = IncrementalMigrationHttpOriginParameter()
            self._OriginParameter._deserialize(params.get("OriginParameter"))
        self._Mode = params.get("Mode")
        if params.get("OriginCondition") is not None:
            self._OriginCondition = IncrementalMigrationHttpOriginCondition()
            self._OriginCondition._deserialize(params.get("OriginCondition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationHttpOriginInfo(AbstractModel):
    """增量迁移源站信息。

    """

    def __init__(self):
        r"""
        :param _EndpointInfo: 增量迁移源站地址信息。
        :type EndpointInfo: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpEndpointInfo`
        :param _FileInfo: 增量迁移源站文件信息。
        :type FileInfo: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationOriginFileInfo`
        """
        self._EndpointInfo = None
        self._FileInfo = None

    @property
    def EndpointInfo(self):
        """增量迁移源站地址信息。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpEndpointInfo`
        """
        return self._EndpointInfo

    @EndpointInfo.setter
    def EndpointInfo(self, EndpointInfo):
        self._EndpointInfo = EndpointInfo

    @property
    def FileInfo(self):
        """增量迁移源站文件信息。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationOriginFileInfo`
        """
        return self._FileInfo

    @FileInfo.setter
    def FileInfo(self, FileInfo):
        self._FileInfo = FileInfo


    def _deserialize(self, params):
        if params.get("EndpointInfo") is not None:
            self._EndpointInfo = IncrementalMigrationHttpEndpointInfo()
            self._EndpointInfo._deserialize(params.get("EndpointInfo"))
        if params.get("FileInfo") is not None:
            self._FileInfo = IncrementalMigrationOriginFileInfo()
            self._FileInfo._deserialize(params.get("FileInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationHttpOriginParameter(AbstractModel):
    """增量迁移回源参数。

    """

    def __init__(self):
        r"""
        :param _HttpHeaderInfo: HTTP 头部透传信息。
        :type HttpHeaderInfo: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpHeaderInfo`
        :param _Protocol: 回源协议。取值有：
<li>HTTP：强制 HTTP；</li>
<li>HTTPS：强制 HTTPS；</li>
<li>FOLLOW：跟随请求协议。</li>若不填，默认取值 `FOLLOW`。
        :type Protocol: str
        :param _QueryStringFollowMode: 请求参数透传模式。取值有：
<li>FOLLOW：全部透传；</li>
<li>IGNORE：忽略，全部不透传。</li> 默认取值 `FOLLOW`。
        :type QueryStringFollowMode: str
        :param _HttpRedirectCode: 重定向的 HTTP Code，目前仅支持 `301`，`302` 和 `307`。默认取值 `302`。
        :type HttpRedirectCode: int
        :param _OriginRedirectionFollowMode: 源站重定向跟随模式。取值有：
<li>FOLLOW：跟随源站重定向；</li>
<li>IGNORE：忽略源站重定向。</li> 默认取值 `FOLLOW` 跟随源站重定向，即源站返回 `3xx` 时，会默认跟随至对应源站拉取数据。
        :type OriginRedirectionFollowMode: str
        """
        self._HttpHeaderInfo = None
        self._Protocol = None
        self._QueryStringFollowMode = None
        self._HttpRedirectCode = None
        self._OriginRedirectionFollowMode = None

    @property
    def HttpHeaderInfo(self):
        """HTTP 头部透传信息。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpHeaderInfo`
        """
        return self._HttpHeaderInfo

    @HttpHeaderInfo.setter
    def HttpHeaderInfo(self, HttpHeaderInfo):
        self._HttpHeaderInfo = HttpHeaderInfo

    @property
    def Protocol(self):
        """回源协议。取值有：
<li>HTTP：强制 HTTP；</li>
<li>HTTPS：强制 HTTPS；</li>
<li>FOLLOW：跟随请求协议。</li>若不填，默认取值 `FOLLOW`。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def QueryStringFollowMode(self):
        """请求参数透传模式。取值有：
<li>FOLLOW：全部透传；</li>
<li>IGNORE：忽略，全部不透传。</li> 默认取值 `FOLLOW`。
        :rtype: str
        """
        return self._QueryStringFollowMode

    @QueryStringFollowMode.setter
    def QueryStringFollowMode(self, QueryStringFollowMode):
        self._QueryStringFollowMode = QueryStringFollowMode

    @property
    def HttpRedirectCode(self):
        """重定向的 HTTP Code，目前仅支持 `301`，`302` 和 `307`。默认取值 `302`。
        :rtype: int
        """
        return self._HttpRedirectCode

    @HttpRedirectCode.setter
    def HttpRedirectCode(self, HttpRedirectCode):
        self._HttpRedirectCode = HttpRedirectCode

    @property
    def OriginRedirectionFollowMode(self):
        """源站重定向跟随模式。取值有：
<li>FOLLOW：跟随源站重定向；</li>
<li>IGNORE：忽略源站重定向。</li> 默认取值 `FOLLOW` 跟随源站重定向，即源站返回 `3xx` 时，会默认跟随至对应源站拉取数据。
        :rtype: str
        """
        return self._OriginRedirectionFollowMode

    @OriginRedirectionFollowMode.setter
    def OriginRedirectionFollowMode(self, OriginRedirectionFollowMode):
        self._OriginRedirectionFollowMode = OriginRedirectionFollowMode


    def _deserialize(self, params):
        if params.get("HttpHeaderInfo") is not None:
            self._HttpHeaderInfo = IncrementalMigrationHttpHeaderInfo()
            self._HttpHeaderInfo._deserialize(params.get("HttpHeaderInfo"))
        self._Protocol = params.get("Protocol")
        self._QueryStringFollowMode = params.get("QueryStringFollowMode")
        self._HttpRedirectCode = params.get("HttpRedirectCode")
        self._OriginRedirectionFollowMode = params.get("OriginRedirectionFollowMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationOriginFileInfo(AbstractModel):
    """增量迁移源站文件信息。

    """

    def __init__(self):
        r"""
        :param _PrefixConfig: 文件前缀配置。
        :type PrefixConfig: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationOriginPrefixConfig`
        :param _SuffixConfig: 文件后缀配置。
        :type SuffixConfig: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationOriginSuffixConfig`
        :param _FixedFileConfig: 固定文件配置。
        :type FixedFileConfig: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationOriginFixedFileConfig`
        """
        self._PrefixConfig = None
        self._SuffixConfig = None
        self._FixedFileConfig = None

    @property
    def PrefixConfig(self):
        """文件前缀配置。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationOriginPrefixConfig`
        """
        return self._PrefixConfig

    @PrefixConfig.setter
    def PrefixConfig(self, PrefixConfig):
        self._PrefixConfig = PrefixConfig

    @property
    def SuffixConfig(self):
        """文件后缀配置。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationOriginSuffixConfig`
        """
        return self._SuffixConfig

    @SuffixConfig.setter
    def SuffixConfig(self, SuffixConfig):
        self._SuffixConfig = SuffixConfig

    @property
    def FixedFileConfig(self):
        """固定文件配置。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationOriginFixedFileConfig`
        """
        return self._FixedFileConfig

    @FixedFileConfig.setter
    def FixedFileConfig(self, FixedFileConfig):
        self._FixedFileConfig = FixedFileConfig


    def _deserialize(self, params):
        if params.get("PrefixConfig") is not None:
            self._PrefixConfig = IncrementalMigrationOriginPrefixConfig()
            self._PrefixConfig._deserialize(params.get("PrefixConfig"))
        if params.get("SuffixConfig") is not None:
            self._SuffixConfig = IncrementalMigrationOriginSuffixConfig()
            self._SuffixConfig._deserialize(params.get("SuffixConfig"))
        if params.get("FixedFileConfig") is not None:
            self._FixedFileConfig = IncrementalMigrationOriginFixedFileConfig()
            self._FixedFileConfig._deserialize(params.get("FixedFileConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationOriginFixedFileConfig(AbstractModel):
    """增量迁移源站固定文件路径配置。

    """

    def __init__(self):
        r"""
        :param _FixedFilePath: 固定文件路径；如填充 `example/test.png`，则回源地址为： `http(s)://<回源域名>/example/test.png`。
        :type FixedFilePath: str
        """
        self._FixedFilePath = None

    @property
    def FixedFilePath(self):
        """固定文件路径；如填充 `example/test.png`，则回源地址为： `http(s)://<回源域名>/example/test.png`。
        :rtype: str
        """
        return self._FixedFilePath

    @FixedFilePath.setter
    def FixedFilePath(self, FixedFilePath):
        self._FixedFilePath = FixedFilePath


    def _deserialize(self, params):
        self._FixedFilePath = params.get("FixedFilePath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationOriginPrefixConfig(AbstractModel):
    """增量迁移源站地址前缀配置。

    """

    def __init__(self):
        r"""
        :param _Prefix: 源站地址前缀，如填充 `test/`，则回源地址为 `http(s)://<回源域名>/test/<文件名>`。
        :type Prefix: str
        """
        self._Prefix = None

    @property
    def Prefix(self):
        """源站地址前缀，如填充 `test/`，则回源地址为 `http(s)://<回源域名>/test/<文件名>`。
        :rtype: str
        """
        return self._Prefix

    @Prefix.setter
    def Prefix(self, Prefix):
        self._Prefix = Prefix


    def _deserialize(self, params):
        self._Prefix = params.get("Prefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationOriginSuffixConfig(AbstractModel):
    """增量迁移源站文件后缀配置。

    """

    def __init__(self):
        r"""
        :param _Suffix: 文件后缀；如填充 `.ts` ，则回源地址为：`http(s)://<回源域名>/<文件名>.ts`。
        :type Suffix: str
        """
        self._Suffix = None

    @property
    def Suffix(self):
        """文件后缀；如填充 `.ts` ，则回源地址为：`http(s)://<回源域名>/<文件名>.ts`。
        :rtype: str
        """
        return self._Suffix

    @Suffix.setter
    def Suffix(self, Suffix):
        self._Suffix = Suffix


    def _deserialize(self, params):
        self._Suffix = params.get("Suffix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IncrementalMigrationStrategyInfo(AbstractModel):
    """增量迁移策略信息。

    """

    def __init__(self):
        r"""
        :param _StrategyId: 策略 ID。
        :type StrategyId: str
        :param _StrategyName: 策略名称。
        :type StrategyName: str
        :param _SubAppId: <b>策略生效的点播专业版[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _BucketId: 策略生效的存储桶 ID。
        :type BucketId: str
        :param _OriginType: 源站类型。取值有：<li>HTTP：HTTP 源。</li>
        :type OriginType: str
        :param _HttpOriginConfig: 回源源站配置。
        :type HttpOriginConfig: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginConfig`
        """
        self._StrategyId = None
        self._StrategyName = None
        self._SubAppId = None
        self._BucketId = None
        self._OriginType = None
        self._HttpOriginConfig = None

    @property
    def StrategyId(self):
        """策略 ID。
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        """策略名称。
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def SubAppId(self):
        """<b>策略生效的点播专业版[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def BucketId(self):
        """策略生效的存储桶 ID。
        :rtype: str
        """
        return self._BucketId

    @BucketId.setter
    def BucketId(self, BucketId):
        self._BucketId = BucketId

    @property
    def OriginType(self):
        """源站类型。取值有：<li>HTTP：HTTP 源。</li>
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def HttpOriginConfig(self):
        """回源源站配置。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginConfig`
        """
        return self._HttpOriginConfig

    @HttpOriginConfig.setter
    def HttpOriginConfig(self, HttpOriginConfig):
        self._HttpOriginConfig = HttpOriginConfig


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._SubAppId = params.get("SubAppId")
        self._BucketId = params.get("BucketId")
        self._OriginType = params.get("OriginType")
        if params.get("HttpOriginConfig") is not None:
            self._HttpOriginConfig = IncrementalMigrationHttpOriginConfig()
            self._HttpOriginConfig._deserialize(params.get("HttpOriginConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIncrementalMigrationStrategyRequest(AbstractModel):
    """ModifyIncrementalMigrationStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SubAppId: <b>点播[专业版](/document/product/266/115396)[应用](/document/product/266/14574) ID。</b>
        :type SubAppId: int
        :param _BucketId: 策略生效的存储桶 ID。
        :type BucketId: str
        :param _StrategyId: 增量迁移策略 ID。
        :type StrategyId: str
        :param _StrategyName: 策略名称。若不填充或填充空字符串，则不修改。
        :type StrategyName: str
        :param _OriginType: 源站类型。取值有：<li>HTTP：HTTP 源。</li>若不填或填充空字符串，则不修改。
        :type OriginType: str
        :param _HttpOriginConfig: HTTP 回源源站配置，若不填则默认不修改。
        :type HttpOriginConfig: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginConfig`
        """
        self._SubAppId = None
        self._BucketId = None
        self._StrategyId = None
        self._StrategyName = None
        self._OriginType = None
        self._HttpOriginConfig = None

    @property
    def SubAppId(self):
        """<b>点播[专业版](/document/product/266/115396)[应用](/document/product/266/14574) ID。</b>
        :rtype: int
        """
        return self._SubAppId

    @SubAppId.setter
    def SubAppId(self, SubAppId):
        self._SubAppId = SubAppId

    @property
    def BucketId(self):
        """策略生效的存储桶 ID。
        :rtype: str
        """
        return self._BucketId

    @BucketId.setter
    def BucketId(self, BucketId):
        self._BucketId = BucketId

    @property
    def StrategyId(self):
        """增量迁移策略 ID。
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def StrategyName(self):
        """策略名称。若不填充或填充空字符串，则不修改。
        :rtype: str
        """
        return self._StrategyName

    @StrategyName.setter
    def StrategyName(self, StrategyName):
        self._StrategyName = StrategyName

    @property
    def OriginType(self):
        """源站类型。取值有：<li>HTTP：HTTP 源。</li>若不填或填充空字符串，则不修改。
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def HttpOriginConfig(self):
        """HTTP 回源源站配置，若不填则默认不修改。
        :rtype: :class:`tencentcloud.vod.v20240718.models.IncrementalMigrationHttpOriginConfig`
        """
        return self._HttpOriginConfig

    @HttpOriginConfig.setter
    def HttpOriginConfig(self, HttpOriginConfig):
        self._HttpOriginConfig = HttpOriginConfig


    def _deserialize(self, params):
        self._SubAppId = params.get("SubAppId")
        self._BucketId = params.get("BucketId")
        self._StrategyId = params.get("StrategyId")
        self._StrategyName = params.get("StrategyName")
        self._OriginType = params.get("OriginType")
        if params.get("HttpOriginConfig") is not None:
            self._HttpOriginConfig = IncrementalMigrationHttpOriginConfig()
            self._HttpOriginConfig._deserialize(params.get("HttpOriginConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIncrementalMigrationStrategyResponse(AbstractModel):
    """ModifyIncrementalMigrationStrategy返回参数结构体

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


class SortBy(AbstractModel):
    """排序依据。

    """

    def __init__(self):
        r"""
        :param _Field: 排序字段。
        :type Field: str
        :param _Order: 排序方式，可选值有：
<li>Asc: 升序；</li>
<li>Desc: 降序。</li>
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        """排序字段。
        :rtype: str
        """
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        """排序方式，可选值有：
<li>Asc: 升序；</li>
<li>Desc: 降序。</li>
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StorageInfo(AbstractModel):
    """专业版应用的存储信息。

    """

    def __init__(self):
        r"""
        :param _BucketId: 存储桶 ID。
        :type BucketId: str
        :param _StorageName: 存储名称。
        :type StorageName: str
        :param _StorageRegion: 存储所在区域。
        :type StorageRegion: str
        :param _InternetAccessDomainStatus: 存储公网源站访问域名的状态，取值有：
<li>ONLINE：已生效；</li>
<li>DEPLOYING： 部署中。</li>
        :type InternetAccessDomainStatus: str
        :param _InternetAccessDomain: 存储公网源站访问域名。
        :type InternetAccessDomain: str
        :param _CreateTime: 存储的创建时间。
        :type CreateTime: str
        """
        self._BucketId = None
        self._StorageName = None
        self._StorageRegion = None
        self._InternetAccessDomainStatus = None
        self._InternetAccessDomain = None
        self._CreateTime = None

    @property
    def BucketId(self):
        """存储桶 ID。
        :rtype: str
        """
        return self._BucketId

    @BucketId.setter
    def BucketId(self, BucketId):
        self._BucketId = BucketId

    @property
    def StorageName(self):
        """存储名称。
        :rtype: str
        """
        return self._StorageName

    @StorageName.setter
    def StorageName(self, StorageName):
        self._StorageName = StorageName

    @property
    def StorageRegion(self):
        """存储所在区域。
        :rtype: str
        """
        return self._StorageRegion

    @StorageRegion.setter
    def StorageRegion(self, StorageRegion):
        self._StorageRegion = StorageRegion

    @property
    def InternetAccessDomainStatus(self):
        """存储公网源站访问域名的状态，取值有：
<li>ONLINE：已生效；</li>
<li>DEPLOYING： 部署中。</li>
        :rtype: str
        """
        return self._InternetAccessDomainStatus

    @InternetAccessDomainStatus.setter
    def InternetAccessDomainStatus(self, InternetAccessDomainStatus):
        self._InternetAccessDomainStatus = InternetAccessDomainStatus

    @property
    def InternetAccessDomain(self):
        """存储公网源站访问域名。
        :rtype: str
        """
        return self._InternetAccessDomain

    @InternetAccessDomain.setter
    def InternetAccessDomain(self, InternetAccessDomain):
        self._InternetAccessDomain = InternetAccessDomain

    @property
    def CreateTime(self):
        """存储的创建时间。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._BucketId = params.get("BucketId")
        self._StorageName = params.get("StorageName")
        self._StorageRegion = params.get("StorageRegion")
        self._InternetAccessDomainStatus = params.get("InternetAccessDomainStatus")
        self._InternetAccessDomain = params.get("InternetAccessDomain")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        