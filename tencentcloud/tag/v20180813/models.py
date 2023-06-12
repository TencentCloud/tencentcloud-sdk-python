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


class AddProjectRequest(AbstractModel):
    """AddProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param Info: 项目描述
        :type Info: str
        """
        self.ProjectName = None
        self.Info = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddProjectResponse(AbstractModel):
    """AddProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目Id
        :type ProjectId: int
        :param IsNew: 是否为新项目
        :type IsNew: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProjectId = None
        self.IsNew = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.IsNew = params.get("IsNew")
        self.RequestId = params.get("RequestId")


class AddResourceTagRequest(AbstractModel):
    """AddResourceTag请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddResourceTagResponse(AbstractModel):
    """AddResourceTag返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachResourcesTagResponse(AbstractModel):
    """AttachResourcesTag返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagResponse(AbstractModel):
    """CreateTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTagsRequest(AbstractModel):
    """CreateTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param Tags: 标签列表。
N取值范围：0~9
        :type Tags: list of Tag
        """
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTagsResponse(AbstractModel):
    """CreateTags返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceTagResponse(AbstractModel):
    """DeleteResourceTag返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagResponse(AbstractModel):
    """DeleteTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTagsRequest(AbstractModel):
    """DeleteTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param Tags: 标签列表。
N取值范围：0~9
        :type Tags: list of Tag
        """
        self.Tags = None


    def _deserialize(self, params):
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTagsResponse(AbstractModel):
    """DeleteTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param AllList: 传1拉取所有项目（包括隐藏项目），传0拉取显示项目
        :type AllList: int
        :param Limit: 分页条数，固定值1000。
        :type Limit: int
        :param Offset: 分页偏移量。
        :type Offset: int
        """
        self.AllList = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.AllList = params.get("AllList")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 数据总条数
        :type Total: int
        :param Projects: 项目列表
        :type Projects: list of Project
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Projects = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("Projects") is not None:
            self.Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self.Projects.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsRequest(AbstractModel):
    """DescribeResourceTagsByResourceIds请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByResourceIdsResponse(AbstractModel):
    """DescribeResourceTagsByResourceIds返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByResourceIdsSeqResponse(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param ServiceType: 业务类型
        :type ServiceType: str
        :param ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param ResourceIds: 资源唯一标识ID的列表，列表容量不超过20
        :type ResourceIds: list of str
        :param TagKeys: 资源标签键列表，列表容量不超过20
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByTagKeysResponse(AbstractModel):
    """DescribeResourceTagsByTagKeys返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagsResponse(AbstractModel):
    """DescribeResourcesByTags返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagsUnionResponse(AbstractModel):
    """DescribeResourcesByTagsUnion返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagKeysResponse(AbstractModel):
    """DescribeTagKeys返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesResponse(AbstractModel):
    """DescribeTagValues返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesSeqResponse(AbstractModel):
    """DescribeTagValuesSeq返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsSeqResponse(AbstractModel):
    """DescribeTagsSeq返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachResourcesTagResponse(AbstractModel):
    """DetachResourcesTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class FailedResource(AbstractModel):
    """失败资源信息。
    绑定或解绑资源标签时失败返回

    """

    def __init__(self):
        r"""
        :param Resource: 失败的资源六段式
        :type Resource: str
        :param Code: 错误码
        :type Code: str
        :param Message: 错误信息
        :type Message: str
        """
        self.Resource = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourcesRequest(AbstractModel):
    """GetResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceList: 资源六段式列表。腾讯云使用资源六段式描述一个资源。
例如：ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}。
如果传入了此参数会返回所有匹配的资源列表，指定的MaxResults会失效。
N取值范围：0~9
        :type ResourceList: list of str
        :param TagFilters: 标签键和标签值。
指定多个标签，会查询同时绑定了该多个标签的资源。
N取值范围：0~5。
每个TagFilters中的TagValue最多支持10个
        :type TagFilters: list of TagFilter
        :param PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param MaxResults: 每一页返回的数据最大条数，最大200。
缺省值：50。
        :type MaxResults: int
        """
        self.ResourceList = None
        self.TagFilters = None
        self.PaginationToken = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.ResourceList = params.get("ResourceList")
        if params.get("TagFilters") is not None:
            self.TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self.TagFilters.append(obj)
        self.PaginationToken = params.get("PaginationToken")
        self.MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourcesResponse(AbstractModel):
    """GetResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param PaginationToken: 获取的下一页的Token值
        :type PaginationToken: str
        :param ResourceTagMappingList: 资源及关联的标签(键和值)列表
        :type ResourceTagMappingList: list of ResourceTagMapping
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PaginationToken = None
        self.ResourceTagMappingList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        if params.get("ResourceTagMappingList") is not None:
            self.ResourceTagMappingList = []
            for item in params.get("ResourceTagMappingList"):
                obj = ResourceTagMapping()
                obj._deserialize(item)
                self.ResourceTagMappingList.append(obj)
        self.RequestId = params.get("RequestId")


class GetTagKeysRequest(AbstractModel):
    """GetTagKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param MaxResults: 每一页返回的数据最大条数，最大1000。
缺省值：50。
        :type MaxResults: int
        """
        self.PaginationToken = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        self.MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagKeysResponse(AbstractModel):
    """GetTagKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param PaginationToken: 获取的下一页的Token值
        :type PaginationToken: str
        :param TagKeys: 标签键信息。
        :type TagKeys: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PaginationToken = None
        self.TagKeys = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        self.TagKeys = params.get("TagKeys")
        self.RequestId = params.get("RequestId")


class GetTagValuesRequest(AbstractModel):
    """GetTagValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param TagKeys: 标签键。
返回所有标签键列表对应的标签值。
最大长度：20
        :type TagKeys: list of str
        :param PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param MaxResults: 每一页返回的数据最大条数，最大1000。
缺省值：50。
        :type MaxResults: int
        """
        self.TagKeys = None
        self.PaginationToken = None
        self.MaxResults = None


    def _deserialize(self, params):
        self.TagKeys = params.get("TagKeys")
        self.PaginationToken = params.get("PaginationToken")
        self.MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagValuesResponse(AbstractModel):
    """GetTagValues返回参数结构体

    """

    def __init__(self):
        r"""
        :param PaginationToken: 获取的下一页的Token值
        :type PaginationToken: str
        :param Tags: 标签列表。
        :type Tags: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PaginationToken = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class GetTagsRequest(AbstractModel):
    """GetTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param MaxResults: 每一页返回的数据最大条数，最大1000。
缺省值：50。
        :type MaxResults: int
        :param TagKeys: 标签键。
返回所有标签键列表对应的标签。
最大长度：20
        :type TagKeys: list of str
        """
        self.PaginationToken = None
        self.MaxResults = None
        self.TagKeys = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        self.MaxResults = params.get("MaxResults")
        self.TagKeys = params.get("TagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagsResponse(AbstractModel):
    """GetTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param PaginationToken: 获取的下一页的Token值
        :type PaginationToken: str
        :param Tags: 标签列表。
        :type Tags: list of Tag
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PaginationToken = None
        self.Tags = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PaginationToken = params.get("PaginationToken")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcesTagValueResponse(AbstractModel):
    """ModifyResourcesTagValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Project(AbstractModel):
    """项目信息

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param CreatorUin: 创建人uin
        :type CreatorUin: int
        :param ProjectInfo: 项目描述
        :type ProjectInfo: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.CreatorUin = None
        self.ProjectInfo = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.CreatorUin = params.get("CreatorUin")
        self.ProjectInfo = params.get("ProjectInfo")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIdTag(AbstractModel):
    """资源标签键值

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTag(AbstractModel):
    """资源标签

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTagMapping(AbstractModel):
    """资源及关联的标签(键和值)。

    """

    def __init__(self):
        r"""
        :param Resource: 资源六段式。腾讯云使用资源六段式描述一个资源。
例如：ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}。
        :type Resource: str
        :param Tags: 资源关联的标签列表
        :type Tags: list of Tag
        """
        self.Resource = None
        self.Tags = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """表示一个标签键值对

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """tag过滤数组多个是与的关系

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagKeyObject(AbstractModel):
    """标签键对象

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        """
        self.TagKey = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResource(AbstractModel):
    """标签键值对以及资源ID

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResourcesRequest(AbstractModel):
    """TagResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceList: 资源六段式列表。腾讯云使用资源六段式描述一个资源。可参考[访问管理](https://cloud.tencent.com/document/product/598/67350)-概览-接口列表-资源六段式信息
例如：ResourceList.1 = qcs::${ServiceType}:${Region}:uin/${Account}:${ResourcePrefix}/${ResourceId}。
N取值范围：0~9
        :type ResourceList: list of str
        :param Tags: 标签键和标签值。
如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。
同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。
如果标签不存在会为您自动创建标签。
N取值范围：0~9
        :type Tags: list of Tag
        """
        self.ResourceList = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceList = params.get("ResourceList")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResourcesResponse(AbstractModel):
    """TagResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param FailedResources: 失败资源信息。
创建并绑定标签成功时，返回的FailedResources为空。
创建并绑定标签失败或部分失败时，返回的FailedResources会显示失败资源的详细信息。
        :type FailedResources: list of FailedResource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedResources = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FailedResources") is not None:
            self.FailedResources = []
            for item in params.get("FailedResources"):
                obj = FailedResource()
                obj._deserialize(item)
                self.FailedResources.append(obj)
        self.RequestId = params.get("RequestId")


class TagWithDelete(AbstractModel):
    """表示一个标签键值对以及是否允许删除

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnTagResourcesRequest(AbstractModel):
    """UnTagResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param ResourceList: 资源六段式列表。腾讯云使用资源六段式描述一个资源。可参考[访问管理](https://cloud.tencent.com/document/product/598/67350)-概览-接口列表-资源六段式信息
例如：ResourceList.1 = qcs::${ServiceType}:${Region}:uin/${Account}:${ResourcePrefix}/${ResourceId}。
N取值范围：0~9
        :type ResourceList: list of str
        :param TagKeys: 标签键。
取值范围：0~9
        :type TagKeys: list of str
        """
        self.ResourceList = None
        self.TagKeys = None


    def _deserialize(self, params):
        self.ResourceList = params.get("ResourceList")
        self.TagKeys = params.get("TagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnTagResourcesResponse(AbstractModel):
    """UnTagResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param FailedResources: 失败资源信息。
解绑标签成功时，返回的FailedResources为空。
解绑标签失败或部分失败时，返回的FailedResources会显示失败资源的详细信息。
        :type FailedResources: list of FailedResource
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FailedResources = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FailedResources") is not None:
            self.FailedResources = []
            for item in params.get("FailedResources"):
                obj = FailedResource()
                obj._deserialize(item)
                self.FailedResources.append(obj)
        self.RequestId = params.get("RequestId")


class UpdateProjectRequest(AbstractModel):
    """UpdateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param ProjectName: 项目名称
        :type ProjectName: str
        :param Disable: 禁用项目，1，禁用，0，启用
        :type Disable: int
        :param Info: 备注
        :type Info: str
        """
        self.ProjectId = None
        self.ProjectName = None
        self.Disable = None
        self.Info = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProjectName = params.get("ProjectName")
        self.Disable = params.get("Disable")
        self.Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProjectResponse(AbstractModel):
    """UpdateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateResourceTagValueRequest(AbstractModel):
    """UpdateResourceTagValue请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateResourceTagValueResponse(AbstractModel):
    """UpdateResourceTagValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")