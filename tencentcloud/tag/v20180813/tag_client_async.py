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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.tag.v20180813 import models
from typing import Dict


class TagClient(AbstractClient):
    _apiVersion = '2018-08-13'
    _endpoint = 'tag.tencentcloudapi.com'
    _service = 'tag'

    async def AddProject(
            self,
            request: models.AddProjectRequest,
            opts: Dict = None,
    ) -> models.AddProjectResponse:
        """
        创建项目
        """
        
        kwargs = {}
        kwargs["action"] = "AddProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddResourceTag(
            self,
            request: models.AddResourceTagRequest,
            opts: Dict = None,
    ) -> models.AddResourceTagResponse:
        """
        本接口用于给标签关联资源
        """
        
        kwargs = {}
        kwargs["action"] = "AddResourceTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddResourceTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachResourcesTag(
            self,
            request: models.AttachResourcesTagRequest,
            opts: Dict = None,
    ) -> models.AttachResourcesTagResponse:
        """
        给多个资源关联某个标签
        """
        
        kwargs = {}
        kwargs["action"] = "AttachResourcesTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachResourcesTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTag(
            self,
            request: models.CreateTagRequest,
            opts: Dict = None,
    ) -> models.CreateTagResponse:
        """
        本接口用于创建一对标签键和标签值
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTags(
            self,
            request: models.CreateTagsRequest,
            opts: Dict = None,
    ) -> models.CreateTagsResponse:
        """
        本接口用于创建多对标签键和标签值
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceTag(
            self,
            request: models.DeleteResourceTagRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceTagResponse:
        """
        本接口用于解除标签和资源的关联关系
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTag(
            self,
            request: models.DeleteTagRequest,
            opts: Dict = None,
    ) -> models.DeleteTagResponse:
        """
        本接口用于删除一对标签键和标签值
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTags(
            self,
            request: models.DeleteTagsRequest,
            opts: Dict = None,
    ) -> models.DeleteTagsResponse:
        """
        本接口用于批量删除标签键和标签值。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjects(
            self,
            request: models.DescribeProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectsResponse:
        """
        获取项目列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTags(
            self,
            request: models.DescribeResourceTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsResponse:
        """
        查询资源关联标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTagsByResourceIds(
            self,
            request: models.DescribeResourceTagsByResourceIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsByResourceIdsResponse:
        """
        用于批量查询已有资源关联的标签键值对
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTagsByResourceIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsByResourceIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTagsByResourceIdsSeq(
            self,
            request: models.DescribeResourceTagsByResourceIdsSeqRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsByResourceIdsSeqResponse:
        """
        按顺序查看资源关联的标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTagsByResourceIdsSeq"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsByResourceIdsSeqResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceTagsByTagKeys(
            self,
            request: models.DescribeResourceTagsByTagKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceTagsByTagKeysResponse:
        """
        根据标签键获取资源标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceTagsByTagKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceTagsByTagKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByTags(
            self,
            request: models.DescribeResourcesByTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByTagsResponse:
        """
        通过标签查询资源列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByTagsUnion(
            self,
            request: models.DescribeResourcesByTagsUnionRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByTagsUnionResponse:
        """
        通过标签查询资源列表并集
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByTagsUnion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByTagsUnionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagKeys(
            self,
            request: models.DescribeTagKeysRequest,
            opts: Dict = None,
    ) -> models.DescribeTagKeysResponse:
        """
        用于查询已建立的标签列表中的标签键。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagValues(
            self,
            request: models.DescribeTagValuesRequest,
            opts: Dict = None,
    ) -> models.DescribeTagValuesResponse:
        """
        用于查询已建立的标签列表中的标签值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagValuesSeq(
            self,
            request: models.DescribeTagValuesSeqRequest,
            opts: Dict = None,
    ) -> models.DescribeTagValuesSeqResponse:
        """
        用于查询已建立的标签列表中的标签值。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagValuesSeq"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagValuesSeqResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTags(
            self,
            request: models.DescribeTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsResponse:
        """
        用于查询已建立的标签列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTagsSeq(
            self,
            request: models.DescribeTagsSeqRequest,
            opts: Dict = None,
    ) -> models.DescribeTagsSeqResponse:
        """
        用于查询已建立的标签列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTagsSeq"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTagsSeqResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachResourcesTag(
            self,
            request: models.DetachResourcesTagRequest,
            opts: Dict = None,
    ) -> models.DetachResourcesTagResponse:
        """
        解绑多个资源关联的某个标签
        """
        
        kwargs = {}
        kwargs["action"] = "DetachResourcesTag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachResourcesTagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetResources(
            self,
            request: models.GetResourcesRequest,
            opts: Dict = None,
    ) -> models.GetResourcesResponse:
        """
        查询绑定了标签的资源列表。
        """
        
        kwargs = {}
        kwargs["action"] = "GetResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTagKeys(
            self,
            request: models.GetTagKeysRequest,
            opts: Dict = None,
    ) -> models.GetTagKeysResponse:
        """
        查询标签键列表。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTagKeys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTagKeysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTagValues(
            self,
            request: models.GetTagValuesRequest,
            opts: Dict = None,
    ) -> models.GetTagValuesResponse:
        """
        用于查询已建立的标签列表中的标签值。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTagValues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTagValuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTags(
            self,
            request: models.GetTagsRequest,
            opts: Dict = None,
    ) -> models.GetTagsResponse:
        """
        用于获取已建立的标签列表。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceTags(
            self,
            request: models.ModifyResourceTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceTagsResponse:
        """
        本接口用于修改资源关联的所有标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcesTagValue(
            self,
            request: models.ModifyResourcesTagValueRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcesTagValueResponse:
        """
        修改多个资源关联的某个标签键对应的标签值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcesTagValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcesTagValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TagResources(
            self,
            request: models.TagResourcesRequest,
            opts: Dict = None,
    ) -> models.TagResourcesResponse:
        """
        为指定的多个云产品的多个云资源统一创建并绑定标签。
        """
        
        kwargs = {}
        kwargs["action"] = "TagResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TagResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnTagResources(
            self,
            request: models.UnTagResourcesRequest,
            opts: Dict = None,
    ) -> models.UnTagResourcesResponse:
        """
        指定的多个云产品的多个云资源统一解绑标签。
        """
        
        kwargs = {}
        kwargs["action"] = "UnTagResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnTagResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProject(
            self,
            request: models.UpdateProjectRequest,
            opts: Dict = None,
    ) -> models.UpdateProjectResponse:
        """
        修改项目
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateResourceTagValue(
            self,
            request: models.UpdateResourceTagValueRequest,
            opts: Dict = None,
    ) -> models.UpdateResourceTagValueResponse:
        """
        本接口用于修改资源已关联的标签值（标签键不变）
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceTagValue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceTagValueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)