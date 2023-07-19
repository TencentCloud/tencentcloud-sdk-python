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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tag.v20180813 import models


class TagClient(AbstractClient):
    _apiVersion = '2018-08-13'
    _endpoint = 'tag.tencentcloudapi.com'
    _service = 'tag'


    def AddProject(self, request):
        """创建项目

        :param request: Request instance for AddProject.
        :type request: :class:`tencentcloud.tag.v20180813.models.AddProjectRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.AddProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddProject", params, headers=headers)
            response = json.loads(body)
            model = models.AddProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddResourceTag(self, request):
        """本接口用于给标签关联资源

        :param request: Request instance for AddResourceTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.AddResourceTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.AddResourceTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddResourceTag", params, headers=headers)
            response = json.loads(body)
            model = models.AddResourceTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachResourcesTag(self, request):
        """给多个资源关联某个标签

        :param request: Request instance for AttachResourcesTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.AttachResourcesTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.AttachResourcesTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachResourcesTag", params, headers=headers)
            response = json.loads(body)
            model = models.AttachResourcesTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTag(self, request):
        """本接口用于创建一对标签键和标签值

        :param request: Request instance for CreateTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.CreateTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.CreateTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTag", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTags(self, request):
        """本接口用于创建多对标签键和标签值

        :param request: Request instance for CreateTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.CreateTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.CreateTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTags", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceTag(self, request):
        """本接口用于解除标签和资源的关联关系

        :param request: Request instance for DeleteResourceTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.DeleteResourceTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DeleteResourceTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTag(self, request):
        """本接口用于删除一对标签键和标签值

        :param request: Request instance for DeleteTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.DeleteTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DeleteTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTag", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTags(self, request):
        """本接口用于批量删除标签键和标签值。

        :param request: Request instance for DeleteTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.DeleteTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DeleteTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTags", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjects(self, request):
        """获取项目列表

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceTags(self, request):
        """查询资源关联标签

        :param request: Request instance for DescribeResourceTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceTagsByResourceIds(self, request):
        """用于批量查询已有资源关联的标签键值对

        :param request: Request instance for DescribeResourceTagsByResourceIds.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceTagsByResourceIds", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceTagsByResourceIdsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceTagsByResourceIdsSeq(self, request):
        """按顺序查看资源关联的标签

        :param request: Request instance for DescribeResourceTagsByResourceIdsSeq.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsSeqRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsSeqResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceTagsByResourceIdsSeq", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceTagsByResourceIdsSeqResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceTagsByTagKeys(self, request):
        """根据标签键获取资源标签

        :param request: Request instance for DescribeResourceTagsByTagKeys.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByTagKeysRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByTagKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceTagsByTagKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceTagsByTagKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcesByTags(self, request):
        """通过标签查询资源列表

        :param request: Request instance for DescribeResourcesByTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourcesByTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourcesByTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcesByTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesByTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourcesByTagsUnion(self, request):
        """通过标签查询资源列表并集

        :param request: Request instance for DescribeResourcesByTagsUnion.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourcesByTagsUnionRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourcesByTagsUnionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourcesByTagsUnion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourcesByTagsUnionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagKeys(self, request):
        """用于查询已建立的标签列表中的标签键。

        :param request: Request instance for DescribeTagKeys.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagKeysRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagValues(self, request):
        """用于查询已建立的标签列表中的标签值。

        :param request: Request instance for DescribeTagValues.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagValues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagValuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagValuesSeq(self, request):
        """用于查询已建立的标签列表中的标签值。

        :param request: Request instance for DescribeTagValuesSeq.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesSeqRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesSeqResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagValuesSeq", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagValuesSeqResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTags(self, request):
        """用于查询已建立的标签列表。

        :param request: Request instance for DescribeTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTags", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTagsSeq(self, request):
        """用于查询已建立的标签列表。

        :param request: Request instance for DescribeTagsSeq.
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagsSeqRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagsSeqResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTagsSeq", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTagsSeqResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachResourcesTag(self, request):
        """解绑多个资源关联的某个标签

        :param request: Request instance for DetachResourcesTag.
        :type request: :class:`tencentcloud.tag.v20180813.models.DetachResourcesTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DetachResourcesTagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachResourcesTag", params, headers=headers)
            response = json.loads(body)
            model = models.DetachResourcesTagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResources(self, request):
        """查询绑定了标签的资源列表。

        :param request: Request instance for GetResources.
        :type request: :class:`tencentcloud.tag.v20180813.models.GetResourcesRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.GetResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResources", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTagKeys(self, request):
        """查询标签键列表。

        :param request: Request instance for GetTagKeys.
        :type request: :class:`tencentcloud.tag.v20180813.models.GetTagKeysRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.GetTagKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTagKeys", params, headers=headers)
            response = json.loads(body)
            model = models.GetTagKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTagValues(self, request):
        """用于查询已建立的标签列表中的标签值。

        :param request: Request instance for GetTagValues.
        :type request: :class:`tencentcloud.tag.v20180813.models.GetTagValuesRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.GetTagValuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTagValues", params, headers=headers)
            response = json.loads(body)
            model = models.GetTagValuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTags(self, request):
        """用于获取已建立的标签列表。

        :param request: Request instance for GetTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.GetTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.GetTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTags", params, headers=headers)
            response = json.loads(body)
            model = models.GetTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourceTags(self, request):
        """本接口用于修改资源关联的所有标签

        :param request: Request instance for ModifyResourceTags.
        :type request: :class:`tencentcloud.tag.v20180813.models.ModifyResourceTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.ModifyResourceTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourceTags", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourceTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyResourcesTagValue(self, request):
        """修改多个资源关联的某个标签键对应的标签值

        :param request: Request instance for ModifyResourcesTagValue.
        :type request: :class:`tencentcloud.tag.v20180813.models.ModifyResourcesTagValueRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.ModifyResourcesTagValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyResourcesTagValue", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyResourcesTagValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TagResources(self, request):
        """为指定的多个云产品的多个云资源统一创建并绑定标签。

        :param request: Request instance for TagResources.
        :type request: :class:`tencentcloud.tag.v20180813.models.TagResourcesRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.TagResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TagResources", params, headers=headers)
            response = json.loads(body)
            model = models.TagResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnTagResources(self, request):
        """指定的多个云产品的多个云资源统一解绑标签。

        :param request: Request instance for UnTagResources.
        :type request: :class:`tencentcloud.tag.v20180813.models.UnTagResourcesRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.UnTagResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnTagResources", params, headers=headers)
            response = json.loads(body)
            model = models.UnTagResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateProject(self, request):
        """修改项目

        :param request: Request instance for UpdateProject.
        :type request: :class:`tencentcloud.tag.v20180813.models.UpdateProjectRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.UpdateProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateProject", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateResourceTagValue(self, request):
        """本接口用于修改资源已关联的标签值（标签键不变）

        :param request: Request instance for UpdateResourceTagValue.
        :type request: :class:`tencentcloud.tag.v20180813.models.UpdateResourceTagValueRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.UpdateResourceTagValueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateResourceTagValue", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateResourceTagValueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))