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


class CreateLibraryRequest(AbstractModel):
    """CreateLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param Name: 媒体库名称，最多 50 个字符
        :type Name: str
        :param Remark: 备注，最多 250 个字符
        :type Remark: str
        :param BucketName: 存储桶全名，新建后不可更改。当前版本不再支持指定存储桶。
        :type BucketName: str
        :param BucketRegion: 存储桶所在地域，新建后不可更改。当前版本不再支持指定存储桶所在地域。
        :type BucketRegion: str
        :param LibraryExtension: 媒体库配置项，部分参数新建后不可更改
        :type LibraryExtension: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        """
        self.Name = None
        self.Remark = None
        self.BucketName = None
        self.BucketRegion = None
        self.LibraryExtension = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.BucketName = params.get("BucketName")
        self.BucketRegion = params.get("BucketRegion")
        if params.get("LibraryExtension") is not None:
            self.LibraryExtension = LibraryExtension()
            self.LibraryExtension._deserialize(params.get("LibraryExtension"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLibraryResponse(AbstractModel):
    """CreateLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param LibraryId: 媒体库 ID
        :type LibraryId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LibraryId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.RequestId = params.get("RequestId")


class DeleteLibraryRequest(AbstractModel):
    """DeleteLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param LibraryId: 媒体库 ID
        :type LibraryId: str
        """
        self.LibraryId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLibraryResponse(AbstractModel):
    """DeleteLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeLibrariesRequest(AbstractModel):
    """DescribeLibraries请求参数结构体

    """

    def __init__(self):
        r"""
        :param LibraryIds: 按照一个或者多个媒体库 ID 查询，每次请求的上限为 100 个。
        :type LibraryIds: list of str
        :param PageNumber: 页码，整型，配合 PageSize 使用，默认值为 1。
        :type PageNumber: int
        :param PageSize: 每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :type PageSize: int
        """
        self.LibraryIds = None
        self.PageNumber = None
        self.PageSize = None


    def _deserialize(self, params):
        self.LibraryIds = params.get("LibraryIds")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLibrariesResponse(AbstractModel):
    """DescribeLibraries返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 媒体库列表
        :type List: list of Library
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Library()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLibrarySecretRequest(AbstractModel):
    """DescribeLibrarySecret请求参数结构体

    """

    def __init__(self):
        r"""
        :param LibraryId: 媒体库 ID
        :type LibraryId: str
        """
        self.LibraryId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLibrarySecretResponse(AbstractModel):
    """DescribeLibrarySecret返回参数结构体

    """

    def __init__(self):
        r"""
        :param LibraryId: 查询的媒体库 ID
        :type LibraryId: str
        :param LibrarySecret: 查询到的媒体库密钥
        :type LibrarySecret: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LibraryId = None
        self.LibrarySecret = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.LibrarySecret = params.get("LibrarySecret")
        self.RequestId = params.get("RequestId")


class DescribeOfficialInstancesRequest(AbstractModel):
    """DescribeOfficialInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param SuperAdminAccount: 是否查询实例绑定的超级管理员账号，默认值为 false。
        :type SuperAdminAccount: bool
        :param InstanceIds: 按照一个或者多个实例 ID 查询，每次请求的上限为 100 个。
        :type InstanceIds: list of str
        :param PageNumber: 页码，整型，配合 PageSize 使用，默认值为 1。
        :type PageNumber: int
        :param PageSize: 每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :type PageSize: int
        :param OrderBy: 对指定列进行排序
        :type OrderBy: str
        :param OrderByType: 排序方式
        :type OrderByType: str
        :param AutoRenew: 续费管理筛选类型
        :type AutoRenew: int
        :param BindPhone: 超级管理管理员账号是否绑定了手机号
        :type BindPhone: bool
        """
        self.SuperAdminAccount = None
        self.InstanceIds = None
        self.PageNumber = None
        self.PageSize = None
        self.OrderBy = None
        self.OrderByType = None
        self.AutoRenew = None
        self.BindPhone = None


    def _deserialize(self, params):
        self.SuperAdminAccount = params.get("SuperAdminAccount")
        self.InstanceIds = params.get("InstanceIds")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.AutoRenew = params.get("AutoRenew")
        self.BindPhone = params.get("BindPhone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOfficialInstancesResponse(AbstractModel):
    """DescribeOfficialInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 实例列表
        :type List: list of Instance
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = Instance()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeOfficialOverviewRequest(AbstractModel):
    """DescribeOfficialOverview请求参数结构体

    """


class DescribeOfficialOverviewResponse(AbstractModel):
    """DescribeOfficialOverview返回参数结构体

    """

    def __init__(self):
        r"""
        :param Quantity: 云盘实例数量
        :type Quantity: int
        :param Storage: 已经使用的总存储量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Storage: str
        :param UserCount: 已经分配和使用的总用户数
        :type UserCount: int
        :param InternetTraffic: 本月外网下行流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type InternetTraffic: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Quantity = None
        self.Storage = None
        self.UserCount = None
        self.InternetTraffic = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Quantity = params.get("Quantity")
        self.Storage = params.get("Storage")
        self.UserCount = params.get("UserCount")
        self.InternetTraffic = params.get("InternetTraffic")
        self.RequestId = params.get("RequestId")


class DescribeTrafficPackagesRequest(AbstractModel):
    """DescribeTrafficPackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceIds: 按照一个或者多个资源 ID 查询，每次请求的上限为 100 个。
        :type ResourceIds: list of str
        :param PageNumber: 页码，整型，配合 PageSize 使用，默认值为 1。
        :type PageNumber: int
        :param PageSize: 每页数目，整型，配合 PageNumber 使用，默认值为 20，最大值为 100。
        :type PageSize: int
        :param OrderBy: 对指定列进行排序
        :type OrderBy: str
        :param OrderByType: 排序方式
        :type OrderByType: str
        :param Type: 来源类型筛选
        :type Type: int
        """
        self.ResourceIds = None
        self.PageNumber = None
        self.PageSize = None
        self.OrderBy = None
        self.OrderByType = None
        self.Type = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.PageNumber = params.get("PageNumber")
        self.PageSize = params.get("PageSize")
        self.OrderBy = params.get("OrderBy")
        self.OrderByType = params.get("OrderByType")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficPackagesResponse(AbstractModel):
    """DescribeTrafficPackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param List: 流量包列表
        :type List: list of TrafficPackage
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.List = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = TrafficPackage()
                obj._deserialize(item)
                self.List.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """官方云盘实例信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例 ID
        :type InstanceId: str
        :param Domain: 专属域名。如果实例无专属域名，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param EffectiveTime: 生效时间
        :type EffectiveTime: str
        :param ExpireTime: 过期时间。如果为按量计费或永久有效实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param UserLimit: 用户数量。如果为按量计费或不限制用户数量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type UserLimit: int
        :param StorageLimit: 存储容量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。如果为按量计费或不限制存储容量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimit: str
        :param StorageLimitGB: 存储容量，单位为 GB。如果为按量计费或不限制存储容量实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type StorageLimitGB: int
        :param Isolated: 是否过期隔离
        :type Isolated: bool
        :param AutoRenew: 续费标识。0：手动续费；1：自动续费；2：到期不续。
        :type AutoRenew: int
        :param SuperAdminAccount: 超级管理员账号，如果未选择查询实例绑定的超级管理员账号或当前实例未绑定超级管理员账号，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type SuperAdminAccount: str
        """
        self.InstanceId = None
        self.Domain = None
        self.EffectiveTime = None
        self.ExpireTime = None
        self.UserLimit = None
        self.StorageLimit = None
        self.StorageLimitGB = None
        self.Isolated = None
        self.AutoRenew = None
        self.SuperAdminAccount = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Domain = params.get("Domain")
        self.EffectiveTime = params.get("EffectiveTime")
        self.ExpireTime = params.get("ExpireTime")
        self.UserLimit = params.get("UserLimit")
        self.StorageLimit = params.get("StorageLimit")
        self.StorageLimitGB = params.get("StorageLimitGB")
        self.Isolated = params.get("Isolated")
        self.AutoRenew = params.get("AutoRenew")
        self.SuperAdminAccount = params.get("SuperAdminAccount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Library(AbstractModel):
    """PaaS 服务媒体库信息

    """

    def __init__(self):
        r"""
        :param LibraryId: 媒体库 ID
        :type LibraryId: str
        :param Name: 媒体库友好名称
        :type Name: str
        :param Remark: 备注
        :type Remark: str
        :param BucketName: 媒体库绑定的 COS 存储桶
        :type BucketName: str
        :param BucketRegion: 媒体库绑定的 COS 存储桶所在的地域
        :type BucketRegion: str
        :param CreationTime: 媒体库创建时间
        :type CreationTime: str
        :param LibraryExtension: 媒体库配置项
        :type LibraryExtension: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        :param Size: 媒体库用量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Size: str
        :param DirNum: 媒体库目录数，由于数字类型精度限制，该字段为 String 类型。
        :type DirNum: str
        :param FileNum: 媒体库文件数，由于数字类型精度限制，该字段为 String 类型。
        :type FileNum: str
        """
        self.LibraryId = None
        self.Name = None
        self.Remark = None
        self.BucketName = None
        self.BucketRegion = None
        self.CreationTime = None
        self.LibraryExtension = None
        self.Size = None
        self.DirNum = None
        self.FileNum = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        self.BucketName = params.get("BucketName")
        self.BucketRegion = params.get("BucketRegion")
        self.CreationTime = params.get("CreationTime")
        if params.get("LibraryExtension") is not None:
            self.LibraryExtension = LibraryExtension()
            self.LibraryExtension._deserialize(params.get("LibraryExtension"))
        self.Size = params.get("Size")
        self.DirNum = params.get("DirNum")
        self.FileNum = params.get("FileNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LibraryExtension(AbstractModel):
    """媒体库配置项

    """

    def __init__(self):
        r"""
        :param IsFileLibrary: true 为文件类型媒体库，可存储任何类型文件；false 为媒体类型媒体库，仅可存储照片和视频类型文件。默认为 false。在媒体库创建后不能修改。
        :type IsFileLibrary: bool
        :param IsMultiSpace: true 为多租户空间媒体库，可创建多个租户空间；false 为单租户空间媒体库，不能创建租户空间，仅可使用默认的单一租户空间。默认为 false。在媒体库创建后不能修改。
        :type IsMultiSpace: bool
        :param CosStorageClass: 保存至 COS 对象存储的文件的存储类型，仅支持 STANDARD、STANDARD_IA、INTELLIGENT_TIERING、MAZ_STANDARD、MAZ_STANDARD_IA 和 MAZ_INTELLIGENT_TIERING，默认为 STANDARD，当使用多 AZ 存储桶时将自动使用 MAZ_ 开头的用于多 AZ 的存储类型，否则自动使用非 MAZ_ 开头的用于非多 AZ 的存储类型。当指定智能分层存储 INTELLIGENT_TIERING 或 MAZ_INTELLIGENT_TIERING 时，需要事先为存储桶开启智能分层存储，否则将返回失败。在媒体库创建后不能修改。
        :type CosStorageClass: str
        :param UseRecycleBin: 是否开启回收站功能。默认为 false。
        :type UseRecycleBin: bool
        :param AutoRemoveRecycledDays: 当开启回收站时，自动删除回收站项目的天数，不能超过 1095（3 年），指定为 0 则不自动删除，默认为 0。当未开启回收站时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRemoveRecycledDays: int
        :param EnableSearch: 是否启用文件路径搜索功能。默认为 false。
        :type EnableSearch: bool
        :param DenyOnQuotaLessThanUsage: 设置媒体库或租户空间配额且配额小于已使用存储量时，是否拒绝设置请求。默认为 false。
        :type DenyOnQuotaLessThanUsage: bool
        :param EnableFileHistory: 是否开启历史版本。默认为 false。
        :type EnableFileHistory: bool
        :param FileHistoryCount: 当开启历史版本时，指定单个文件保留的历史版本的数量上限，不能超过 999，指定为 0 则不限制，默认为 0。当未开启历史版本时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileHistoryCount: int
        :param FileHistoryExpireDay: 当开启历史版本时，指定历史版本保留的最长天数，不能超过 999，指定为 0 则不限制，默认为 0。当未开启历史版本时，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type FileHistoryExpireDay: int
        :param MaxDirFileNameLength: 目录或文件名的最长长度，不能超过 255，默认为 255。修改该参数不会影响存量目录或文件名，即如果将该字段的值改小，已经存在的长度超过目标值的目录或文件名不会发生变化。
        :type MaxDirFileNameLength: int
        :param IsPublicRead: 是否开启公有读，开启后读操作无需使用访问令牌，默认为 false。仅单租户空间媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsPublicRead: bool
        :param IsMultiAlbum: 媒体类型媒体库是否开启多相簿，开启后可创建一级目录（即相簿）且媒体文件只能保存在各相簿中，否则不能创建相簿且媒体文件只能保存在根目录。默认为 false。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。在媒体库创建后不能修改。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsMultiAlbum: bool
        :param AllowPhoto: 媒体类型媒体库是否允许上传照片，默认为 true。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowPhoto: bool
        :param AllowPhotoExtName: 当媒体类型媒体库允许上传照片时，指定允许的扩展名，默认为空数组，此时将根据文件扩展名对应的 MIME 类型自动判断。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowPhotoExtName: list of str
        :param AllowVideo: 媒体类型媒体库是否允许上传视频，默认为 true。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowVideo: bool
        :param AllowVideoExtName: 当媒体类型媒体库允许上传视频时，指定允许的扩展名，默认为空数组，此时将根据文件扩展名对应的 MIME 类型自动判断。仅单租户空间媒体类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowVideoExtName: list of str
        :param AllowFileExtName: 指定文件类型媒体库允许的文件扩展名，默认为空数组，此时允许上传所有类型文件。仅单租户空间文件类型媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type AllowFileExtName: list of str
        :param RecognizeSensitiveContent: 照片上传时是否进行敏感内容鉴定，默认为 false。仅单租户空间媒体库支持该属性，否则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type RecognizeSensitiveContent: bool
        """
        self.IsFileLibrary = None
        self.IsMultiSpace = None
        self.CosStorageClass = None
        self.UseRecycleBin = None
        self.AutoRemoveRecycledDays = None
        self.EnableSearch = None
        self.DenyOnQuotaLessThanUsage = None
        self.EnableFileHistory = None
        self.FileHistoryCount = None
        self.FileHistoryExpireDay = None
        self.MaxDirFileNameLength = None
        self.IsPublicRead = None
        self.IsMultiAlbum = None
        self.AllowPhoto = None
        self.AllowPhotoExtName = None
        self.AllowVideo = None
        self.AllowVideoExtName = None
        self.AllowFileExtName = None
        self.RecognizeSensitiveContent = None


    def _deserialize(self, params):
        self.IsFileLibrary = params.get("IsFileLibrary")
        self.IsMultiSpace = params.get("IsMultiSpace")
        self.CosStorageClass = params.get("CosStorageClass")
        self.UseRecycleBin = params.get("UseRecycleBin")
        self.AutoRemoveRecycledDays = params.get("AutoRemoveRecycledDays")
        self.EnableSearch = params.get("EnableSearch")
        self.DenyOnQuotaLessThanUsage = params.get("DenyOnQuotaLessThanUsage")
        self.EnableFileHistory = params.get("EnableFileHistory")
        self.FileHistoryCount = params.get("FileHistoryCount")
        self.FileHistoryExpireDay = params.get("FileHistoryExpireDay")
        self.MaxDirFileNameLength = params.get("MaxDirFileNameLength")
        self.IsPublicRead = params.get("IsPublicRead")
        self.IsMultiAlbum = params.get("IsMultiAlbum")
        self.AllowPhoto = params.get("AllowPhoto")
        self.AllowPhotoExtName = params.get("AllowPhotoExtName")
        self.AllowVideo = params.get("AllowVideo")
        self.AllowVideoExtName = params.get("AllowVideoExtName")
        self.AllowFileExtName = params.get("AllowFileExtName")
        self.RecognizeSensitiveContent = params.get("RecognizeSensitiveContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLibraryRequest(AbstractModel):
    """ModifyLibrary请求参数结构体

    """

    def __init__(self):
        r"""
        :param LibraryId: 媒体库 ID
        :type LibraryId: str
        :param Name: 媒体库名称，最多 50 个字符。如不传则不修改。
        :type Name: str
        :param Remark: 备注，最多 250 个字符。如不传则不修改。
        :type Remark: str
        :param LibraryExtension: 媒体库配置项，部分参数在新建后不可更改，且仅修改传入的参数。如不传该参数则不修改任何配置项。
        :type LibraryExtension: :class:`tencentcloud.smh.v20210712.models.LibraryExtension`
        """
        self.LibraryId = None
        self.Name = None
        self.Remark = None
        self.LibraryExtension = None


    def _deserialize(self, params):
        self.LibraryId = params.get("LibraryId")
        self.Name = params.get("Name")
        self.Remark = params.get("Remark")
        if params.get("LibraryExtension") is not None:
            self.LibraryExtension = LibraryExtension()
            self.LibraryExtension._deserialize(params.get("LibraryExtension"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLibraryResponse(AbstractModel):
    """ModifyLibrary返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SendSmsCodeRequest(AbstractModel):
    """SendSmsCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Purpose: 验证码目的，当前支持换绑超级管理员账号， BindSuperAdmin；体验版企业升级，ChannelUpdateVerify等
        :type Purpose: str
        :param PhoneNumber: 将作为超级管理员账号的手机号码
        :type PhoneNumber: str
        :param InstanceId: 官方云盘实例 ID
        :type InstanceId: str
        :param CountryCode: 将作为超级管理员账号的手机号码的国家代码。默认为 +86。
        :type CountryCode: str
        """
        self.Purpose = None
        self.PhoneNumber = None
        self.InstanceId = None
        self.CountryCode = None


    def _deserialize(self, params):
        self.Purpose = params.get("Purpose")
        self.PhoneNumber = params.get("PhoneNumber")
        self.InstanceId = params.get("InstanceId")
        self.CountryCode = params.get("CountryCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendSmsCodeResponse(AbstractModel):
    """SendSmsCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TrafficPackage(AbstractModel):
    """流量资源包信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 流量资源包所抵扣的实例 ID
        :type InstanceId: str
        :param Domain: 专属域名。如果实例无专属域名，则该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Type: 流量资源包来源类型，0 为付费购买，1 为赠送。
        :type Type: int
        :param Size: 总流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Size: str
        :param SizeGB: 总流量，单位为 GB
        :type SizeGB: int
        :param Remain: 剩余流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Remain: str
        :param Used: 已使用流量，单位为 Bytes，由于数字类型精度限制，该字段为 String 类型。
        :type Used: str
        :param UsedPercentage: 已使用百分比，由于数字类型精度限制，该字段为 String 类型。
        :type UsedPercentage: str
        :param EffectiveTime: 生效时间，即流量资源包的订购时间
        :type EffectiveTime: str
        :param ExpireTime: 过期时间，即所抵扣的实例的过期时间。如果流量资源包所抵扣的实例为按量计费或永久有效实例，该属性为 null。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        """
        self.InstanceId = None
        self.Domain = None
        self.Type = None
        self.Size = None
        self.SizeGB = None
        self.Remain = None
        self.Used = None
        self.UsedPercentage = None
        self.EffectiveTime = None
        self.ExpireTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Domain = params.get("Domain")
        self.Type = params.get("Type")
        self.Size = params.get("Size")
        self.SizeGB = params.get("SizeGB")
        self.Remain = params.get("Remain")
        self.Used = params.get("Used")
        self.UsedPercentage = params.get("UsedPercentage")
        self.EffectiveTime = params.get("EffectiveTime")
        self.ExpireTime = params.get("ExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySmsCodeRequest(AbstractModel):
    """VerifySmsCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Purpose: 验证码目的，当前支持换绑超级管理员账号，BindSuperAdmin；体验版企业升级验证ChannelUpdateVerify，等
        :type Purpose: str
        :param PhoneNumber: 将作为超级管理员账号的手机号码
        :type PhoneNumber: str
        :param Code: 短信验证码
        :type Code: str
        :param InstanceId: 官方云盘实例 ID
        :type InstanceId: str
        :param CountryCode: 将作为超级管理员账号的手机号码的国家代码。默认为 +86。
        :type CountryCode: str
        """
        self.Purpose = None
        self.PhoneNumber = None
        self.Code = None
        self.InstanceId = None
        self.CountryCode = None


    def _deserialize(self, params):
        self.Purpose = params.get("Purpose")
        self.PhoneNumber = params.get("PhoneNumber")
        self.Code = params.get("Code")
        self.InstanceId = params.get("InstanceId")
        self.CountryCode = params.get("CountryCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySmsCodeResponse(AbstractModel):
    """VerifySmsCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")