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
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _Info: 项目描述
        :type Info: str
        """
        self._ProjectName = None
        self._Info = None

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddProjectResponse(AbstractModel):
    """AddProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目Id
        :type ProjectId: int
        :param _IsNew: 是否为新项目，1是新项目，0不是新项目
        :type IsNew: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ProjectId = None
        self._IsNew = None
        self._RequestId = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IsNew(self):
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._IsNew = params.get("IsNew")
        self._RequestId = params.get("RequestId")


class AddResourceTagRequest(AbstractModel):
    """AddResourceTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 需要绑定的标签键，取值规范参考：https://cloud.tencent.com/document/product/651/13354
        :type TagKey: str
        :param _TagValue: 需要绑定的标签值，取值规范参考：https://cloud.tencent.com/document/product/651/13354
        :type TagValue: str
        :param _Resource: 待关联的资源，用标准的资源六段式表示。正确的资源六段式请参考：https://cloud.tencent.com/document/product/651/89122
        :type Resource: str
        """
        self._TagKey = None
        self._TagValue = None
        self._Resource = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddResourceTagResponse(AbstractModel):
    """AddResourceTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AttachResourcesTagRequest(AbstractModel):
    """AttachResourcesTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 业务的英文简称，即资源六段式第三段。资源六段式的描述方式参考：https://cloud.tencent.com/document/product/651/89122
        :type ServiceType: str
        :param _ResourceIds: 资源ID数组，资源个数最多为50
        :type ResourceIds: list of str
        :param _TagKey: 需要绑定的标签键，取值规范参考：https://cloud.tencent.com/document/product/651/13354
        :type TagKey: str
        :param _TagValue: 需要绑定的标签值，取值规范参考：https://cloud.tencent.com/document/product/651/13354
        :type TagValue: str
        :param _ResourceRegion: 资源所在地域，不区分地域的资源则不必填。区分地域的资源则必填，且必填时必须是参数ResourceIds.N资源所对应的地域，且如果ResourceIds.N为批量时，这些资源也必须是同一个地域的。例如示例值：ap-beijing，则参数ResourceIds.N中都应该填写该地域的资源。
        :type ResourceRegion: str
        :param _ResourcePrefix: 资源前缀（资源六段式中最后一段"/"前面的部分），cos存储桶不需要传入该字段，其他云资源必填
        :type ResourcePrefix: str
        """
        self._ServiceType = None
        self._ResourceIds = None
        self._TagKey = None
        self._TagValue = None
        self._ResourceRegion = None
        self._ResourcePrefix = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourceIds = params.get("ResourceIds")
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachResourcesTagResponse(AbstractModel):
    """AttachResourcesTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateTagRequest(AbstractModel):
    """CreateTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class CreateTagResponse(AbstractModel):
    """CreateTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateTagsRequest(AbstractModel):
    """CreateTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tags: 标签列表。
N取值范围：0~9
        :type Tags: list of Tag
        """
        self._Tags = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
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
        


class CreateTagsResponse(AbstractModel):
    """CreateTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteResourceTagRequest(AbstractModel):
    """DeleteResourceTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _Resource: [ 资源六段式描述 ](https://cloud.tencent.com/document/product/598/10606)
        :type Resource: str
        """
        self._TagKey = None
        self._Resource = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteResourceTagResponse(AbstractModel):
    """DeleteResourceTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTagRequest(AbstractModel):
    """DeleteTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 需要删除的标签键
        :type TagKey: str
        :param _TagValue: 需要删除的标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class DeleteTagResponse(AbstractModel):
    """DeleteTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteTagsRequest(AbstractModel):
    """DeleteTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Tags: 标签列表。
N取值范围：0~9
        :type Tags: list of Tag
        """
        self._Tags = None

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
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
        


class DeleteTagsResponse(AbstractModel):
    """DeleteTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeProjectsRequest(AbstractModel):
    """DescribeProjects请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AllList: 传1拉取所有项目（包括隐藏项目），传0拉取显示项目
        :type AllList: int
        :param _Limit: 分页条数，固定值1000。
        :type Limit: int
        :param _Offset: 分页偏移量。
        :type Offset: int
        :param _ProjectId: 按项目ID筛选，大于0
        :type ProjectId: int
        :param _ProjectName: 按项目名称筛选
        :type ProjectName: str
        """
        self._AllList = None
        self._Limit = None
        self._Offset = None
        self._ProjectId = None
        self._ProjectName = None

    @property
    def AllList(self):
        return self._AllList

    @AllList.setter
    def AllList(self, AllList):
        self._AllList = AllList

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName


    def _deserialize(self, params):
        self._AllList = params.get("AllList")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProjectsResponse(AbstractModel):
    """DescribeProjects返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 数据总条数
        :type Total: int
        :param _Projects: 项目列表
        :type Projects: list of Project
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Projects = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Projects(self):
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Projects") is not None:
            self._Projects = []
            for item in params.get("Projects"):
                obj = Project()
                obj._deserialize(item)
                self._Projects.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsRequest(AbstractModel):
    """DescribeResourceTagsByResourceIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 业务类型
        :type ServiceType: str
        :param _ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param _ResourceIds: 资源ID数组，大小不超过50
        :type ResourceIds: list of str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。 All：全部标签。 默认值：All。
        :type Category: str
        """
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceIds = None
        self._ResourceRegion = None
        self._Offset = None
        self._Limit = None
        self._Category = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceIds = params.get("ResourceIds")
        self._ResourceRegion = params.get("ResourceRegion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByResourceIdsResponse(AbstractModel):
    """DescribeResourceTagsByResourceIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Tags: 标签列表
        :type Tags: list of TagResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsByResourceIdsSeqRequest(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 业务类型
        :type ServiceType: str
        :param _ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param _ResourceIds: 资源唯一标记
        :type ResourceIds: list of str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        """
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceIds = None
        self._ResourceRegion = None
        self._Offset = None
        self._Limit = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceIds = params.get("ResourceIds")
        self._ResourceRegion = params.get("ResourceRegion")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByResourceIdsSeqResponse(AbstractModel):
    """DescribeResourceTagsByResourceIdsSeq返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Tags: 标签列表
        :type Tags: list of TagResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagResource()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsByTagKeysRequest(AbstractModel):
    """DescribeResourceTagsByTagKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 业务类型
        :type ServiceType: str
        :param _ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param _ResourceRegion: 资源地域
        :type ResourceRegion: str
        :param _ResourceIds: 资源唯一标识ID的列表，列表容量不超过20
        :type ResourceIds: list of str
        :param _TagKeys: 资源标签键列表，列表容量不超过20
        :type TagKeys: list of str
        :param _Limit: 每页大小，默认为 400
        :type Limit: int
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        """
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceRegion = None
        self._ResourceIds = None
        self._TagKeys = None
        self._Limit = None
        self._Offset = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourceIds = params.get("ResourceIds")
        self._TagKeys = params.get("TagKeys")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsByTagKeysResponse(AbstractModel):
    """DescribeResourceTagsByTagKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Rows: 资源标签
        :type Rows: list of ResourceIdTag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = ResourceIdTag()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourceTagsRequest(AbstractModel):
    """DescribeResourceTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CreateUin: 创建者uin
        :type CreateUin: int
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _ServiceType: 业务类型
        :type ServiceType: str
        :param _ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param _ResourceId: 资源唯一标识。只输入ResourceId进行查询可能会查询较慢，或者无法匹配到结果，建议在输入ResourceId的同时也输入ServiceType、ResourcePrefix和ResourceRegion（不区分地域的资源可忽略该参数）
        :type ResourceId: str
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        :param _CosResourceId: 是否是cos的资源（0或者1），输入的ResourceId为cos资源时必填
        :type CosResourceId: int
        """
        self._CreateUin = None
        self._ResourceRegion = None
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceId = None
        self._Offset = None
        self._Limit = None
        self._CosResourceId = None

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CosResourceId(self):
        return self._CosResourceId

    @CosResourceId.setter
    def CosResourceId(self, CosResourceId):
        self._CosResourceId = CosResourceId


    def _deserialize(self, params):
        self._CreateUin = params.get("CreateUin")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceId = params.get("ResourceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CosResourceId = params.get("CosResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourceTagsResponse(AbstractModel):
    """DescribeResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param _Rows: 资源标签
        :type Rows: list of TagResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = TagResource()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesByTagsRequest(AbstractModel):
    """DescribeResourcesByTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagFilters: 标签过滤数组
        :type TagFilters: list of TagFilter
        :param _CreateUin: 创建标签者uin
        :type CreateUin: int
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        :param _ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param _ResourceId: 资源唯一标记
        :type ResourceId: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _ServiceType: 业务类型
        :type ServiceType: str
        """
        self._TagFilters = None
        self._CreateUin = None
        self._Offset = None
        self._Limit = None
        self._ResourcePrefix = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._ServiceType = None

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagsResponse(AbstractModel):
    """DescribeResourcesByTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
注意：此字段可能返回 null，表示取不到有效值。
        :type Limit: int
        :param _Rows: 资源标签
        :type Rows: list of ResourceTag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeResourcesByTagsUnionRequest(AbstractModel):
    """DescribeResourcesByTagsUnion请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagFilters: 标签过滤数组
        :type TagFilters: list of TagFilter
        :param _CreateUin: 创建标签者uin
        :type CreateUin: int
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        :param _ResourcePrefix: 资源前缀
        :type ResourcePrefix: str
        :param _ResourceId: 资源唯一标记
        :type ResourceId: str
        :param _ResourceRegion: 资源所在地域
        :type ResourceRegion: str
        :param _ServiceType: 业务类型
        :type ServiceType: str
        """
        self._TagFilters = None
        self._CreateUin = None
        self._Offset = None
        self._Limit = None
        self._ResourcePrefix = None
        self._ResourceId = None
        self._ResourceRegion = None
        self._ServiceType = None

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType


    def _deserialize(self, params):
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceId = params.get("ResourceId")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagsUnionResponse(AbstractModel):
    """DescribeResourcesByTagsUnion返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Rows: 资源标签
        :type Rows: list of ResourceTag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Rows = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Rows(self):
        return self._Rows

    @Rows.setter
    def Rows(self, Rows):
        self._Rows = Rows

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Rows") is not None:
            self._Rows = []
            for item in params.get("Rows"):
                obj = ResourceTag()
                obj._deserialize(item)
                self._Rows.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagKeysRequest(AbstractModel):
    """DescribeTagKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15，最大1000
        :type Limit: int
        :param _ShowProject: 是否展现项目
        :type ShowProject: int
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。 All：全部标签。 默认值：All。
        :type Category: str
        """
        self._CreateUin = None
        self._Offset = None
        self._Limit = None
        self._ShowProject = None
        self._Category = None

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def ShowProject(self):
        return self._ShowProject

    @ShowProject.setter
    def ShowProject(self, ShowProject):
        self._ShowProject = ShowProject

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ShowProject = params.get("ShowProject")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagKeysResponse(AbstractModel):
    """DescribeTagKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Tags: 标签列表
        :type Tags: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Tags = params.get("Tags")
        self._RequestId = params.get("RequestId")


class DescribeTagValuesRequest(AbstractModel):
    """DescribeTagValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKeys: 标签键列表
        :type TagKeys: list of str
        :param _CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。 All：全部标签。 默认值：All。
        :type Category: str
        """
        self._TagKeys = None
        self._CreateUin = None
        self._Offset = None
        self._Limit = None
        self._Category = None

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKeys = params.get("TagKeys")
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesResponse(AbstractModel):
    """DescribeTagValues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagValuesSeqRequest(AbstractModel):
    """DescribeTagValuesSeq请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKeys: 标签键列表
        :type TagKeys: list of str
        :param _CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        """
        self._TagKeys = None
        self._CreateUin = None
        self._Offset = None
        self._Limit = None

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TagKeys = params.get("TagKeys")
        self._CreateUin = params.get("CreateUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagValuesSeqResponse(AbstractModel):
    """DescribeTagValuesSeq返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Tags: 标签列表
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagsRequest(AbstractModel):
    """DescribeTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签
        :type TagKey: str
        :param _TagValue: 标签值,与标签键同时存在或同时不存在，不存在时表示查询该用户所有标签
        :type TagValue: str
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        :param _CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param _TagKeys: 标签键数组,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签,当与TagKey同时传递时只取本值
        :type TagKeys: list of str
        :param _ShowProject: 是否展现项目标签
        :type ShowProject: int
        """
        self._TagKey = None
        self._TagValue = None
        self._Offset = None
        self._Limit = None
        self._CreateUin = None
        self._TagKeys = None
        self._ShowProject = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def ShowProject(self):
        return self._ShowProject

    @ShowProject.setter
    def ShowProject(self, ShowProject):
        self._ShowProject = ShowProject


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreateUin = params.get("CreateUin")
        self._TagKeys = params.get("TagKeys")
        self._ShowProject = params.get("ShowProject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsResponse(AbstractModel):
    """DescribeTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Tags: 标签列表
        :type Tags: list of TagWithDelete
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTagsSeqRequest(AbstractModel):
    """DescribeTagsSeq请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签
        :type TagKey: str
        :param _TagValue: 标签值,与标签键同时存在或同时不存在，不存在时表示查询该用户所有标签
        :type TagValue: str
        :param _Offset: 数据偏移量，默认为 0, 必须为Limit参数的整数倍
        :type Offset: int
        :param _Limit: 每页大小，默认为 15
        :type Limit: int
        :param _CreateUin: 创建者用户 Uin，不传或为空只将 Uin 作为条件查询
        :type CreateUin: int
        :param _TagKeys: 标签键数组,与标签值同时存在或同时不存在，不存在时表示查询该用户所有标签,当与TagKey同时传递时只取本值
        :type TagKeys: list of str
        :param _ShowProject: 是否展现项目标签
        :type ShowProject: int
        """
        self._TagKey = None
        self._TagValue = None
        self._Offset = None
        self._Limit = None
        self._CreateUin = None
        self._TagKeys = None
        self._ShowProject = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def CreateUin(self):
        return self._CreateUin

    @CreateUin.setter
    def CreateUin(self, CreateUin):
        self._CreateUin = CreateUin

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def ShowProject(self):
        return self._ShowProject

    @ShowProject.setter
    def ShowProject(self, ShowProject):
        self._ShowProject = ShowProject


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CreateUin = params.get("CreateUin")
        self._TagKeys = params.get("TagKeys")
        self._ShowProject = params.get("ShowProject")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTagsSeqResponse(AbstractModel):
    """DescribeTagsSeq返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 结果总数
        :type TotalCount: int
        :param _Offset: 数据位移偏量
        :type Offset: int
        :param _Limit: 每页大小
        :type Limit: int
        :param _Tags: 标签列表
        :type Tags: list of TagWithDelete
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Offset = None
        self._Limit = None
        self._Tags = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagWithDelete()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class DetachResourcesTagRequest(AbstractModel):
    """DetachResourcesTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 资源所属业务名称（资源六段式中的第三段）
        :type ServiceType: str
        :param _ResourceIds: 资源ID数组，资源个数最多为50
        :type ResourceIds: list of str
        :param _TagKey: 需要解绑的标签键
        :type TagKey: str
        :param _ResourceRegion: 资源所在地域，不区分地域的资源不需要传入该字段，区分地域的资源必填
        :type ResourceRegion: str
        :param _ResourcePrefix: 资源前缀（资源六段式中最后一段"/"前面的部分），cos存储桶不需要传入该字段，其他云资源必填
        :type ResourcePrefix: str
        """
        self._ServiceType = None
        self._ResourceIds = None
        self._TagKey = None
        self._ResourceRegion = None
        self._ResourcePrefix = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourceIds = params.get("ResourceIds")
        self._TagKey = params.get("TagKey")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachResourcesTagResponse(AbstractModel):
    """DetachResourcesTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class FailedResource(AbstractModel):
    """失败资源信息。
    绑定或解绑资源标签时失败返回

    """

    def __init__(self):
        r"""
        :param _Resource: 失败的资源六段式
        :type Resource: str
        :param _Code: 错误码
        :type Code: str
        :param _Message: 错误信息
        :type Message: str
        """
        self._Resource = None
        self._Code = None
        self._Message = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Code = params.get("Code")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourcesRequest(AbstractModel):
    """GetResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceList: 资源六段式列表。腾讯云使用资源六段式描述一个资源。
例如：ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}。
如果传入了此参数会返回所有匹配的资源列表，指定的MaxResults会失效。
N取值范围：0~9
        :type ResourceList: list of str
        :param _TagFilters: 标签键和标签值。
指定多个标签，会查询同时绑定了该多个标签的资源。
N取值范围：0~5。
每个TagFilters中的TagValue最多支持10个
        :type TagFilters: list of TagFilter
        :param _PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param _MaxResults: 每一页返回的数据最大条数，最大200。
缺省值：50。
        :type MaxResults: int
        """
        self._ResourceList = None
        self._TagFilters = None
        self._PaginationToken = None
        self._MaxResults = None

    @property
    def ResourceList(self):
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList

    @property
    def TagFilters(self):
        return self._TagFilters

    @TagFilters.setter
    def TagFilters(self, TagFilters):
        self._TagFilters = TagFilters

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults


    def _deserialize(self, params):
        self._ResourceList = params.get("ResourceList")
        if params.get("TagFilters") is not None:
            self._TagFilters = []
            for item in params.get("TagFilters"):
                obj = TagFilter()
                obj._deserialize(item)
                self._TagFilters.append(obj)
        self._PaginationToken = params.get("PaginationToken")
        self._MaxResults = params.get("MaxResults")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetResourcesResponse(AbstractModel):
    """GetResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PaginationToken: 获取的下一页的Token值
        :type PaginationToken: str
        :param _ResourceTagMappingList: 资源及关联的标签(键和值)列表
        :type ResourceTagMappingList: list of ResourceTagMapping
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PaginationToken = None
        self._ResourceTagMappingList = None
        self._RequestId = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def ResourceTagMappingList(self):
        return self._ResourceTagMappingList

    @ResourceTagMappingList.setter
    def ResourceTagMappingList(self, ResourceTagMappingList):
        self._ResourceTagMappingList = ResourceTagMappingList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        if params.get("ResourceTagMappingList") is not None:
            self._ResourceTagMappingList = []
            for item in params.get("ResourceTagMappingList"):
                obj = ResourceTagMapping()
                obj._deserialize(item)
                self._ResourceTagMappingList.append(obj)
        self._RequestId = params.get("RequestId")


class GetTagKeysRequest(AbstractModel):
    """GetTagKeys请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param _MaxResults: 每一页返回的数据最大条数，最大1000。
缺省值：50。
        :type MaxResults: int
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。 All：全部标签。 默认值：All。
        :type Category: str
        """
        self._PaginationToken = None
        self._MaxResults = None
        self._Category = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        self._MaxResults = params.get("MaxResults")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagKeysResponse(AbstractModel):
    """GetTagKeys返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PaginationToken: 获取的下一页的Token值，如果当前是最后一页，返回为空
        :type PaginationToken: str
        :param _TagKeys: 标签键信息。
        :type TagKeys: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PaginationToken = None
        self._TagKeys = None
        self._RequestId = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        self._TagKeys = params.get("TagKeys")
        self._RequestId = params.get("RequestId")


class GetTagValuesRequest(AbstractModel):
    """GetTagValues请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKeys: 标签键。
返回所有标签键列表对应的标签值。
最大长度：20
        :type TagKeys: list of str
        :param _PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param _MaxResults: 每一页返回的数据最大条数，最大1000。
缺省值：50。
        :type MaxResults: int
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。 All：全部标签。 默认值：All。
        :type Category: str
        """
        self._TagKeys = None
        self._PaginationToken = None
        self._MaxResults = None
        self._Category = None

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKeys = params.get("TagKeys")
        self._PaginationToken = params.get("PaginationToken")
        self._MaxResults = params.get("MaxResults")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagValuesResponse(AbstractModel):
    """GetTagValues返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PaginationToken: 获取的下一页的Token值，如果当前是最后一页，返回为空
        :type PaginationToken: str
        :param _Tags: 标签列表。
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PaginationToken = None
        self._Tags = None
        self._RequestId = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class GetTagsRequest(AbstractModel):
    """GetTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PaginationToken: 从上一页的响应中获取的下一页的Token值。
如果是第一次请求，设置为空。
        :type PaginationToken: str
        :param _MaxResults: 每一页返回的数据最大条数，最大1000。
缺省值：50。
        :type MaxResults: int
        :param _TagKeys: 标签键。
返回所有标签键列表对应的标签。
最大长度：20
        :type TagKeys: list of str
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。 All：全部标签。 默认值：All。
        :type Category: str
        """
        self._PaginationToken = None
        self._MaxResults = None
        self._TagKeys = None
        self._Category = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def MaxResults(self):
        return self._MaxResults

    @MaxResults.setter
    def MaxResults(self, MaxResults):
        self._MaxResults = MaxResults

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        self._MaxResults = params.get("MaxResults")
        self._TagKeys = params.get("TagKeys")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTagsResponse(AbstractModel):
    """GetTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PaginationToken: 获取的下一页的Token值，如果当前是最后一页，返回为空
        :type PaginationToken: str
        :param _Tags: 标签列表。
        :type Tags: list of Tag
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PaginationToken = None
        self._Tags = None
        self._RequestId = None

    @property
    def PaginationToken(self):
        return self._PaginationToken

    @PaginationToken.setter
    def PaginationToken(self, PaginationToken):
        self._PaginationToken = PaginationToken

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PaginationToken = params.get("PaginationToken")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyResourceTagsRequest(AbstractModel):
    """ModifyResourceTags请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Resource: [ 资源六段式描述 ](https://cloud.tencent.com/document/product/598/10606)
        :type Resource: str
        :param _ReplaceTags: 需要增加或修改的标签集合。如果Resource描述的资源未关联输入的标签键，则增加关联；若已关联，则将该资源关联的键对应的标签值修改为输入值。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键。可以不传该参数，但不能是空数组。
        :type ReplaceTags: list of Tag
        :param _DeleteTags: 需要解关联的标签集合。本接口中ReplaceTags和DeleteTags二者必须存在其一，且二者不能包含相同的标签键。可以不传该参数，但不能是空数组。
        :type DeleteTags: list of TagKeyObject
        """
        self._Resource = None
        self._ReplaceTags = None
        self._DeleteTags = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def ReplaceTags(self):
        return self._ReplaceTags

    @ReplaceTags.setter
    def ReplaceTags(self, ReplaceTags):
        self._ReplaceTags = ReplaceTags

    @property
    def DeleteTags(self):
        return self._DeleteTags

    @DeleteTags.setter
    def DeleteTags(self, DeleteTags):
        self._DeleteTags = DeleteTags


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("ReplaceTags") is not None:
            self._ReplaceTags = []
            for item in params.get("ReplaceTags"):
                obj = Tag()
                obj._deserialize(item)
                self._ReplaceTags.append(obj)
        if params.get("DeleteTags") is not None:
            self._DeleteTags = []
            for item in params.get("DeleteTags"):
                obj = TagKeyObject()
                obj._deserialize(item)
                self._DeleteTags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourceTagsResponse(AbstractModel):
    """ModifyResourceTags返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyResourcesTagValueRequest(AbstractModel):
    """ModifyResourcesTagValue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceType: 资源所属业务名称（资源六段式中的第三段）
        :type ServiceType: str
        :param _ResourceIds: 资源ID数组，资源个数最多为50
        :type ResourceIds: list of str
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        :param _ResourceRegion: 资源所在地域，不区分地域的资源不需要传入该字段，区分地域的资源必填
        :type ResourceRegion: str
        :param _ResourcePrefix: 资源前缀（资源六段式中最后一段"/"前面的部分），cos存储桶不需要传入该字段，其他云资源必填
        :type ResourcePrefix: str
        """
        self._ServiceType = None
        self._ResourceIds = None
        self._TagKey = None
        self._TagValue = None
        self._ResourceRegion = None
        self._ResourcePrefix = None

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix


    def _deserialize(self, params):
        self._ServiceType = params.get("ServiceType")
        self._ResourceIds = params.get("ResourceIds")
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._ResourceRegion = params.get("ResourceRegion")
        self._ResourcePrefix = params.get("ResourcePrefix")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyResourcesTagValueResponse(AbstractModel):
    """ModifyResourcesTagValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class Project(AbstractModel):
    """项目信息

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _CreatorUin: 创建人uin
        :type CreatorUin: int
        :param _ProjectInfo: 项目描述
        :type ProjectInfo: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._CreatorUin = None
        self._ProjectInfo = None
        self._CreateTime = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def CreatorUin(self):
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def ProjectInfo(self):
        return self._ProjectInfo

    @ProjectInfo.setter
    def ProjectInfo(self, ProjectInfo):
        self._ProjectInfo = ProjectInfo

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._CreatorUin = params.get("CreatorUin")
        self._ProjectInfo = params.get("ProjectInfo")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceIdTag(AbstractModel):
    """资源标签键值

    """

    def __init__(self):
        r"""
        :param _ResourceId: 资源唯一标识
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _TagKeyValues: 标签键值对
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKeyValues: list of Tag
        """
        self._ResourceId = None
        self._TagKeyValues = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def TagKeyValues(self):
        return self._TagKeyValues

    @TagKeyValues.setter
    def TagKeyValues(self, TagKeyValues):
        self._TagKeyValues = TagKeyValues


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        if params.get("TagKeyValues") is not None:
            self._TagKeyValues = []
            for item in params.get("TagKeyValues"):
                obj = Tag()
                obj._deserialize(item)
                self._TagKeyValues.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceTag(AbstractModel):
    """资源标签

    """

    def __init__(self):
        r"""
        :param _ResourceRegion: 资源所在地域
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceRegion: str
        :param _ServiceType: 业务类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _ResourcePrefix: 资源前缀
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourcePrefix: str
        :param _ResourceId: 资源唯一标记
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceId: str
        :param _Tags: 资源标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tag
        """
        self._ResourceRegion = None
        self._ServiceType = None
        self._ResourcePrefix = None
        self._ResourceId = None
        self._Tags = None

    @property
    def ResourceRegion(self):
        return self._ResourceRegion

    @ResourceRegion.setter
    def ResourceRegion(self, ResourceRegion):
        self._ResourceRegion = ResourceRegion

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def ResourcePrefix(self):
        return self._ResourcePrefix

    @ResourcePrefix.setter
    def ResourcePrefix(self, ResourcePrefix):
        self._ResourcePrefix = ResourcePrefix

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceRegion = params.get("ResourceRegion")
        self._ServiceType = params.get("ServiceType")
        self._ResourcePrefix = params.get("ResourcePrefix")
        self._ResourceId = params.get("ResourceId")
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
        


class ResourceTagMapping(AbstractModel):
    """资源及关联的标签(键和值)。

    """

    def __init__(self):
        r"""
        :param _Resource: 资源六段式。腾讯云使用资源六段式描述一个资源。
例如：ResourceList.1 = qcs::${ServiceType}:${Region}:${Account}:${ResourcePreifx}/${ResourceId}。
        :type Resource: str
        :param _Tags: 资源关联的标签列表
        :type Tags: list of Tag
        """
        self._Resource = None
        self._Tags = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
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
        


class Tag(AbstractModel):
    """表示一个标签键值对

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。 All：全部标签。 默认值：All。
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        """
        self._TagKey = None
        self._TagValue = None
        self._Category = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagFilter(AbstractModel):
    """tag过滤数组多个是与的关系

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值数组 多个值的话是或的关系
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class TagKeyObject(AbstractModel):
    """标签键对象

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        """
        self._TagKey = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResource(AbstractModel):
    """标签键值对以及资源ID

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        :param _ResourceId: 资源ID
        :type ResourceId: str
        :param _TagKeyMd5: 标签键MD5值
        :type TagKeyMd5: str
        :param _TagValueMd5: 标签值MD5值
        :type TagValueMd5: str
        :param _ServiceType: 资源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        """
        self._TagKey = None
        self._TagValue = None
        self._ResourceId = None
        self._TagKeyMd5 = None
        self._TagValueMd5 = None
        self._ServiceType = None
        self._Category = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def TagKeyMd5(self):
        return self._TagKeyMd5

    @TagKeyMd5.setter
    def TagKeyMd5(self, TagKeyMd5):
        self._TagKeyMd5 = TagKeyMd5

    @property
    def TagValueMd5(self):
        return self._TagValueMd5

    @TagValueMd5.setter
    def TagValueMd5(self, TagValueMd5):
        self._TagValueMd5 = TagValueMd5

    @property
    def ServiceType(self):
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._ResourceId = params.get("ResourceId")
        self._TagKeyMd5 = params.get("TagKeyMd5")
        self._TagValueMd5 = params.get("TagValueMd5")
        self._ServiceType = params.get("ServiceType")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResourcesRequest(AbstractModel):
    """TagResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceList: 待绑定的云资源，用标准的资源六段式表示。正确的资源六段式请参考：[标准的资源六段式](https://cloud.tencent.com/document/product/598/10606)和[支持标签的云产品及资源描述方式](https://cloud.tencent.com/document/product/651/89122)。
N取值范围：0~9
        :type ResourceList: list of str
        :param _Tags: 标签键和标签值。
如果指定多个标签，则会为指定资源同时创建并绑定该多个标签。
同一个资源上的同一个标签键只能对应一个标签值。如果您尝试添加已有标签键，则对应的标签值会更新为新值。
如果标签不存在会为您自动创建标签。
N取值范围：0~9
        :type Tags: list of Tag
        """
        self._ResourceList = None
        self._Tags = None

    @property
    def ResourceList(self):
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags


    def _deserialize(self, params):
        self._ResourceList = params.get("ResourceList")
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
        


class TagResourcesResponse(AbstractModel):
    """TagResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedResources: 失败资源信息。
创建并绑定标签成功时，返回的FailedResources为空。
创建并绑定标签失败或部分失败时，返回的FailedResources会显示失败资源的详细信息。
        :type FailedResources: list of FailedResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedResources = None
        self._RequestId = None

    @property
    def FailedResources(self):
        return self._FailedResources

    @FailedResources.setter
    def FailedResources(self, FailedResources):
        self._FailedResources = FailedResources

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FailedResources") is not None:
            self._FailedResources = []
            for item in params.get("FailedResources"):
                obj = FailedResource()
                obj._deserialize(item)
                self._FailedResources.append(obj)
        self._RequestId = params.get("RequestId")


class TagWithDelete(AbstractModel):
    """表示一个标签键值对以及是否允许删除

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        :param _CanDelete: 是否可以删除
        :type CanDelete: int
        :param _Category: 标签类型。取值： Custom：自定义标签。 System：系统标签。 All：全部标签。 默认值：All。
注意：此字段可能返回 null，表示取不到有效值。
        :type Category: str
        """
        self._TagKey = None
        self._TagValue = None
        self._CanDelete = None
        self._Category = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def CanDelete(self):
        return self._CanDelete

    @CanDelete.setter
    def CanDelete(self, CanDelete):
        self._CanDelete = CanDelete

    @property
    def Category(self):
        return self._Category

    @Category.setter
    def Category(self, Category):
        self._Category = Category


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._CanDelete = params.get("CanDelete")
        self._Category = params.get("Category")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnTagResourcesRequest(AbstractModel):
    """UnTagResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ResourceList: 资源六段式列表。腾讯云使用资源六段式描述一个资源。可参考[访问管理](https://cloud.tencent.com/document/product/598/67350)-概览-接口列表-资源六段式信息
例如：ResourceList.1 = qcs::${ServiceType}:${Region}:uin/${Account}:${ResourcePrefix}/${ResourceId}。
N取值范围：0~9
        :type ResourceList: list of str
        :param _TagKeys: 标签键。
取值范围：0~9
        :type TagKeys: list of str
        """
        self._ResourceList = None
        self._TagKeys = None

    @property
    def ResourceList(self):
        return self._ResourceList

    @ResourceList.setter
    def ResourceList(self, ResourceList):
        self._ResourceList = ResourceList

    @property
    def TagKeys(self):
        return self._TagKeys

    @TagKeys.setter
    def TagKeys(self, TagKeys):
        self._TagKeys = TagKeys


    def _deserialize(self, params):
        self._ResourceList = params.get("ResourceList")
        self._TagKeys = params.get("TagKeys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnTagResourcesResponse(AbstractModel):
    """UnTagResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FailedResources: 失败资源信息。
解绑标签成功时，返回的FailedResources为空。
解绑标签失败或部分失败时，返回的FailedResources会显示失败资源的详细信息。
        :type FailedResources: list of FailedResource
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FailedResources = None
        self._RequestId = None

    @property
    def FailedResources(self):
        return self._FailedResources

    @FailedResources.setter
    def FailedResources(self, FailedResources):
        self._FailedResources = FailedResources

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FailedResources") is not None:
            self._FailedResources = []
            for item in params.get("FailedResources"):
                obj = FailedResource()
                obj._deserialize(item)
                self._FailedResources.append(obj)
        self._RequestId = params.get("RequestId")


class UpdateProjectRequest(AbstractModel):
    """UpdateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
        :type ProjectId: int
        :param _ProjectName: 项目名称
        :type ProjectName: str
        :param _Disable: 禁用项目，1，禁用，0，启用
        :type Disable: int
        :param _Info: 备注
        :type Info: str
        """
        self._ProjectId = None
        self._ProjectName = None
        self._Disable = None
        self._Info = None

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def Info(self):
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._ProjectName = params.get("ProjectName")
        self._Disable = params.get("Disable")
        self._Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProjectResponse(AbstractModel):
    """UpdateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateResourceTagValueRequest(AbstractModel):
    """UpdateResourceTagValue请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TagKey: 资源关联的标签键
        :type TagKey: str
        :param _TagValue: 修改后的标签值
        :type TagValue: str
        :param _Resource: [ 资源六段式描述 ](https://cloud.tencent.com/document/product/598/10606)
        :type Resource: str
        """
        self._TagKey = None
        self._TagValue = None
        self._Resource = None

    @property
    def TagKey(self):
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        self._Resource = params.get("Resource")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateResourceTagValueResponse(AbstractModel):
    """UpdateResourceTagValue返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")