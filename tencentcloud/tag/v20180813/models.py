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


class AddResourceTagRequest(AbstractModel):
    """AddResourceTag请求参数结构体

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        :param Resource: [ 资源六段式描述 ](https://cloud.tencent.com/document/product/598/10606)
        :type Resource: str
        """
        self.TagKey = None
        self.TagValue = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Resource = params.get("Resource")


class AddResourceTagResponse(AbstractModel):
    """AddResourceTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachResourcesTagRequest(AbstractModel):
    """AttachResourcesTag请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceType: 资源所属业务名称（资源六段式中的第三段）
        :type ServiceType: str
        :param ResourceIds: 资源ID数组，资源个数最多为50
        :type ResourceIds: list of str
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        :param ResourceRegion: 资源所在地域，不区分地域的资源不需要传入该字段，区分地域的资源必填
        :type ResourceRegion: str
        :param ResourcePrefix: 资源前缀（资源六段式中最后一段"/"前面的部分），cos存储桶不需要传入该字段，其他云资源必填
        :type ResourcePrefix: str
        """
        self.ServiceType = None
        self.ResourceIds = None
        self.TagKey = None
        self.TagValue = None
        self.ResourceRegion = None
        self.ResourcePrefix = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourcePrefix = params.get("ResourcePrefix")


class AttachResourcesTagResponse(AbstractModel):
    """AttachResourcesTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagRequest(AbstractModel):
    """CreateTag请求参数结构体

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class CreateTagResponse(AbstractModel):
    """CreateTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteResourceTagRequest(AbstractModel):
    """DeleteResourceTag请求参数结构体

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param Resource: [ 资源六段式描述 ](https://cloud.tencent.com/document/product/598/10606)
        :type Resource: str
        """
        self.TagKey = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.Resource = params.get("Resource")


class DeleteResourceTagResponse(AbstractModel):
    """DeleteResourceTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagRequest(AbstractModel):
    """DeleteTag请求参数结构体

    """

    def __init__(self):
        """
        :param TagKey: 需要删除的标签键
        :type TagKey: str
        :param TagValue: 需要删除的标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class DeleteTagResponse(AbstractModel):
    """DeleteTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsRequest(AbstractModel):
    """DescribeResourceTagsByResourceIds请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceType: 业务类型
        :type ServiceType: str
        :param ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param ResourceIds: 资源ID数组，大小不超过50
        :type ResourceIds: list of str
        :param ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        """
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceIds = None
        self.ResourceRegion = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceIds = params.get("ResourceIds")
        self.ResourceRegion = params.get("ResourceRegion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeResourceTagsByResourceIdsResponse(AbstractModel):
    """DescribeResourceTagsByResourceIds返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Tags: 标签列表
        :type Tags: list of TagResource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsSeqRequest(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceType: 业务类型
        :type ServiceType: str
        :param ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param ResourceIds: 资源唯一标记
        :type ResourceIds: list of str
        :param ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        """
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceIds = None
        self.ResourceRegion = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceIds = params.get("ResourceIds")
        self.ResourceRegion = params.get("ResourceRegion")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeResourceTagsByResourceIdsSeqResponse(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Tags: 标签列表
        :type Tags: list of TagResource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByTagKeysRequest(AbstractModel):
    """DescribeResourceTagsByTagKeys请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceType: 业务类型
        :type ServiceType: str
        :param ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param ResourceIds: 资源唯一标识
        :type ResourceIds: list of str
        :param TagKeys: 资源标签键
        :type TagKeys: list of str
        :param Limit: 每页大小，默认为 400
        :type Limit: int
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        """
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceRegion = None
        self.ResourceIds = None
        self.TagKeys = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKeys = params.get("TagKeys")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")


class DescribeResourceTagsByTagKeysResponse(AbstractModel):
    """DescribeResourceTagsByTagKeys返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Rows: 资源标签
        :type Rows: list of ResourceIdTag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = ResourceIdTag()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    """DescribeResourceTags请求参数结构体

    """

    def __init__(self):
        """
        :param CreateUin: 创建者uin
        :type CreateUin: int
        :param ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param ServiceType: 业务类型
        :type ServiceType: str
        :param ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param ResourceId: 资源唯一标识。只输入ResourceId进行查询可能会查询较慢，或者无法匹配到结果，建议在输入ResourceId的同时也输入ServiceType、ResourcePrefix和ResourceRegion（不区分地域的资源可忽略该参数）
        :type ResourceId: str
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        :param CosResourceId: 是否是cos的资源（0或者1），输入的ResourceId为cos资源时必填
        :type CosResourceId: int
        """
        self.CreateUin = None
        self.ResourceRegion = None
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.Offset = None
        self.Limit = None
        self.CosResourceId = None


    def _deserialize(self, params):
        self.CreateUin = params.get("CreateUin")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CosResourceId = params.get("CosResourceId")


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param Rows: 资源标签
        :type Rows: list of TagResource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = TagResource()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourcesByTagsRequest(AbstractModel):
    """DescribeResourcesByTags请求参数结构体

    """

    def __init__(self):
        """
        :param TagFilters: 标签过滤数组
        :type TagFilters: list of TagFilter
        :param CreateUin: 创建标签者uin
        :type CreateUin: int
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        :param ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param ResourceId: 资源唯一标记
        :type ResourceId: str
        :param ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param ServiceType: 业务类型
        :type ServiceType: str
        """
        self.TagFilters = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.ResourceRegion = None
        self.ServiceType = None


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")


class DescribeResourcesByTagsResponse(AbstractModel):
    """DescribeResourcesByTags返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param Rows: 资源标签
        :type Rows: list of ResourceTag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourcesByTagsUnionRequest(AbstractModel):
    """DescribeResourcesByTagsUnion请求参数结构体

    """

    def __init__(self):
        """
        :param TagFilters: 标签过滤数组
        :type TagFilters: list of TagFilter
        :param CreateUin: 创建标签者uin
        :type CreateUin: int
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        :param ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param ResourceId: 资源唯一标记
        :type ResourceId: str
        :param ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param ServiceType: 业务类型
        :type ServiceType: str
        """
        self.TagFilters = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.ResourceRegion = None
        self.ServiceType = None


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")


class DescribeResourcesByTagsUnionResponse(AbstractModel):
    """DescribeResourcesByTagsUnion返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Rows: 资源标签
        :type Rows: list of ResourceTag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Rows = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self.Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self.Rows.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagKeysRequest(AbstractModel):
    """DescribeTagKeys请求参数结构体

    """

    def __init__(self):
        """
        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        :param ShowProject: 是否展现项目
        :type ShowProject: int
        """
        self.CreateUin = None
        self.Offset = None
        self.Limit = None
        self.ShowProject = None


    def _deserialize(self, params):
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ShowProject = params.get("ShowProject")


class DescribeTagKeysResponse(AbstractModel):
    """DescribeTagKeys返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Tags: 标签列表
        :type Tags: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Tags = params.get("Tags")
        self.RequestId = params.get("RequestId")


class DescribeTagValuesRequest(AbstractModel):
    """DescribeTagValues请求参数结构体

    """

    def __init__(self):
        """
        :param TagKeys: 标签键列表
        :type TagKeys: list of str
        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        """
        self.TagKeys = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TagKeys = params.get("TagKeys")
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTagValuesResponse(AbstractModel):
    """DescribeTagValues返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagValuesSeqRequest(AbstractModel):
    """DescribeTagValuesSeq请求参数结构体

    """

    def __init__(self):
        """
        :param TagKeys: 标签键列表
        :type TagKeys: list of str
        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        """
        self.TagKeys = None
        self.CreateUin = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.TagKeys = params.get("TagKeys")
        self.CreateUin = params.get("CreateUin")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeTagValuesSeqResponse(AbstractModel):
    """DescribeTagValuesSeq返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Tags: 标签列表
        :type Tags: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags请求参数结构体

    """

    def __init__(self):
        """
        :param TagKey: 标签键,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签
        :type TagKey: str
        :param TagValue: 标签值,与标签键同时存在或同时不存在，不存在时表示查询该用户所有标签
        :type TagValue: str
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param TagKeys: 标签键数组,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签,当与TagKey同时传递时只取本值
        :type TagKeys: list of str
        :param ShowProject: 是否展现项目标签
        :type ShowProject: int
        """
        self.TagKey = None
        self.TagValue = None
        self.Offset = None
        self.Limit = None
        self.CreateUin = None
        self.TagKeys = None
        self.ShowProject = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreateUin = params.get("CreateUin")
        self.TagKeys = params.get("TagKeys")
        self.ShowProject = params.get("ShowProject")


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Tags: 标签列表
        :type Tags: list of TagWithDelete
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTagsSeqRequest(AbstractModel):
    """DescribeTagsSeq请求参数结构体

    """

    def __init__(self):
        """
        :param TagKey: 标签键,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签
        :type TagKey: str
        :param TagValue: 标签值,与标签键同时存在或同时不存在，不存在时表示查询该用户所有标签
        :type TagValue: str
        :param Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param Limit: 每页大小，默认为 15
        :type Limit: int
        :param CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param TagKeys: 标签键数组,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签,当与TagKey同时传递时只取本值
        :type TagKeys: list of str
        :param ShowProject: 是否展现项目标签
        :type ShowProject: int
        """
        self.TagKey = None
        self.TagValue = None
        self.Offset = None
        self.Limit = None
        self.CreateUin = None
        self.TagKeys = None
        self.ShowProject = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CreateUin = params.get("CreateUin")
        self.TagKeys = params.get("TagKeys")
        self.ShowProject = params.get("ShowProject")


class DescribeTagsSeqResponse(AbstractModel):
    """DescribeTagsSeq返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 结果总数
        :type TotalCount: int
        :param Offset: 数据位移偏量
        :type Offset: int
        :param Limit: 每页大小
        :type Limit: int
        :param Tags: 标签列表
        :type Tags: list of TagWithDelete
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Offset = None
        self.Limit = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class DetachResourcesTagRequest(AbstractModel):
    """DetachResourcesTag请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceType: 资源所属业务名称（资源六段式中的第三段）
        :type ServiceType: str
        :param ResourceIds: 资源ID数组，资源个数最多为50
        :type ResourceIds: list of str
        :param TagKey: 需要解绑的标签键
        :type TagKey: str
        :param ResourceRegion: 资源所在地域，不区分地域的资源不需要传入该字段，区分地域的资源必填
        :type ResourceRegion: str
        :param ResourcePrefix: 资源前缀（资源六段式中最后一段"/"前面的部分），cos存储桶不需要传入该字段，其他云资源必填
        :type ResourcePrefix: str
        """
        self.ServiceType = None
        self.ResourceIds = None
        self.TagKey = None
        self.ResourceRegion = None
        self.ResourcePrefix = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKey = params.get("TagKey")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourcePrefix = params.get("ResourcePrefix")


class DetachResourcesTagResponse(AbstractModel):
    """DetachResourcesTag返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags请求参数结构体

    """

    def __init__(self):
        """
        :param Resource: [ 资源六段式描述 ](https://cloud.tencent.com/document/product/598/10606)
        :type Resource: str
        :param ReplaceTags: 需要增加或修改的标签集合。如果Resource描述的资源未关联输入的标签键，则增加关联；若已关联，则将该资源关联的键对应的标签值修改为输入值。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键。可以不传该参数，但不能是空数组。
        :type ReplaceTags: list of Tag
        :param DeleteTags: 需要解关联的标签集合。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键。可以不传该参数，但不能是空数组。
        :type DeleteTags: list of TagKeyObject
        """
        self.Resource = None
        self.ReplaceTags = None
        self.DeleteTags = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("ReplaceTags") is not None:
            self.ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = Tag()
                obj._deserialize(item)
                self.ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self.DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagKeyObject()
                obj._deserialize(item)
                self.DeleteTags.append(obj)


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyResourcesTagValueRequest(AbstractModel):
    """ModifyResourcesTagValue请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceType: 资源所属业务名称（资源六段式中的第三段）
        :type ServiceType: str
        :param ResourceIds: 资源ID数组，资源个数最多为50
        :type ResourceIds: list of str
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        :param ResourceRegion: 资源所在地域，不区分地域的资源不需要传入该字段，区分地域的资源必填
        :type ResourceRegion: str
        :param ResourcePrefix: 资源前缀（资源六段式中最后一段"/"前面的部分），cos存储桶不需要传入该字段，其他云资源必填
        :type ResourcePrefix: str
        """
        self.ServiceType = None
        self.ResourceIds = None
        self.TagKey = None
        self.TagValue = None
        self.ResourceRegion = None
        self.ResourcePrefix = None


    def _deserialize(self, params):
        self.ServiceType = params.get("ServiceType")
        self.ResourceIds = params.get("ResourceIds")
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceRegion = params.get("ResourceRegion")
        self.ResourcePrefix = params.get("ResourcePrefix")


class ModifyResourcesTagValueResponse(AbstractModel):
    """ModifyResourcesTagValue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResourceIdTag(AbstractModel):
    """资源标签键值

    """

    def __init__(self):
        """
        :param ResourceId: 资源唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param TagKeyValues: 标签键值对
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKeyValues: list of Tag
        """
        self.ResourceId = None
        self.TagKeyValues = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        if params.get("TagKeyValues") is not None:
            self.TagKeyValues = []
            for item in params.get("TagKeyValues"):
                obj = Tag()
                obj._deserialize(item)
                self.TagKeyValues.append(obj)


class ResourceTag(AbstractModel):
    """资源标签

    """

    def __init__(self):
        """
        :param ResourceRegion: 资源所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        :param ServiceType: 业务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param ResourcePrefix: 资源前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourcePrefix: str
        :param ResourceId: 资源唯一标记
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param Tags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self.ResourceRegion = None
        self.ServiceType = None
        self.ResourcePrefix = None
        self.ResourceId = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceRegion = params.get("ResourceRegion")
        self.ServiceType = params.get("ServiceType")
        self.ResourcePrefix = params.get("ResourcePrefix")
        self.ResourceId = params.get("ResourceId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)


class Tag(AbstractModel):
    """表示一个标签键值对

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TagFilter(AbstractModel):
    """tag过滤数组多个是与的关系

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值数组 多个值的话是或的关系
        :type TagValue: list of str
        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")


class TagKeyObject(AbstractModel):
    """标签键对象

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        """
        self.TagKey = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")


class TagResource(AbstractModel):
    """标签键值对以及资源ID

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        :param ResourceId: 资源ID
        :type ResourceId: str
        :param TagKeyMd5: 标签键MD5值
        :type TagKeyMd5: str
        :param TagValueMd5: 标签值MD5值
        :type TagValueMd5: str
        :param ServiceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        """
        self.TagKey = None
        self.TagValue = None
        self.ResourceId = None
        self.TagKeyMd5 = None
        self.TagValueMd5 = None
        self.ServiceType = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceId = params.get("ResourceId")
        self.TagKeyMd5 = params.get("TagKeyMd5")
        self.TagValueMd5 = params.get("TagValueMd5")
        self.ServiceType = params.get("ServiceType")


class TagWithDelete(AbstractModel):
    """表示一个标签键值对以及是否允许删除

    """

    def __init__(self):
        """
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        :param CanDelete: 是否可以删除
        :type CanDelete: int
        """
        self.TagKey = None
        self.TagValue = None
        self.CanDelete = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.CanDelete = params.get("CanDelete")


class UpdateResourceTagValueRequest(AbstractModel):
    """UpdateResourceTagValue请求参数结构体

    """

    def __init__(self):
        """
        :param TagKey: 资源关联的标签键
        :type TagKey: str
        :param TagValue: 修改后的标签值
        :type TagValue: str
        :param Resource: [ 资源六段式描述 ](https://cloud.tencent.com/document/product/598/10606)
        :type Resource: str
        """
        self.TagKey = None
        self.TagValue = None
        self.Resource = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.Resource = params.get("Resource")


class UpdateResourceTagValueResponse(AbstractModel):
    """UpdateResourceTagValue返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")