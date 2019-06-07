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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.tag.v20180813 import models


class TagClient(AbstractClient):
    _apiVersion = '2018-08-13'
    _endpoint = 'tag.tencentcloudapi.com'


    def AddResourceTag(self, request):
        """本接口用于给标签关联资源

        :param request: 调用AddResourceTag所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.AddResourceTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.AddResourceTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddResourceTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddResourceTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTag(self, request):
        """本接口用于创建一对标签键和标签值

        :param request: 调用CreateTag所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.CreateTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.CreateTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteResourceTag(self, request):
        """本接口用于解除标签和资源的关联关系

        :param request: 调用DeleteResourceTag所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.DeleteResourceTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DeleteResourceTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteResourceTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteResourceTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTag(self, request):
        """本接口用于删除一对标签键和标签值

        :param request: 调用DeleteTag所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.DeleteTagRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DeleteTagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResourceTagsByResourceIds(self, request):
        """用于查询已有资源标签键值对

        :param request: 调用DescribeResourceTagsByResourceIds所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeResourceTagsByResourceIdsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTagsByResourceIds", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsByResourceIdsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagKeys(self, request):
        """用于查询已建立的标签列表中的标签键。

        :param request: 调用DescribeTagKeys所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagKeysRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagKeysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagKeys", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagKeysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTagValues(self, request):
        """用于查询已建立的标签列表中的标签值。

        :param request: 调用DescribeTagValues所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagValuesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTagValues", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagValuesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTags(self, request):
        """用于查询已建立的标签列表。

        :param request: 调用DescribeTags所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.DescribeTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.DescribeTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyResourceTags(self, request):
        """本接口用于修改资源关联的所有标签

        :param request: 调用ModifyResourceTags所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.ModifyResourceTagsRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.ModifyResourceTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyResourceTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyResourceTagsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateResourceTagValue(self, request):
        """本接口用于修改资源已关联的标签值（标签键不变）

        :param request: 调用UpdateResourceTagValue所需参数的结构体。
        :type request: :class:`tencentcloud.tag.v20180813.models.UpdateResourceTagValueRequest`
        :rtype: :class:`tencentcloud.tag.v20180813.models.UpdateResourceTagValueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpdateResourceTagValue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpdateResourceTagValueResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)