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
from tencentcloud.chdfs.v20201112 import models


class ChdfsClient(AbstractClient):
    _apiVersion = '2020-11-12'
    _endpoint = 'chdfs.tencentcloudapi.com'
    _service = 'chdfs'


    def AssociateAccessGroups(self, request):
        """给挂载点绑定多个权限组。

        :param request: Request instance for AssociateAccessGroups.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.AssociateAccessGroupsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.AssociateAccessGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateAccessGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateAccessGroupsResponse()
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


    def CreateAccessGroup(self, request):
        """创建权限组。

        :param request: Request instance for CreateAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccessGroupResponse()
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


    def CreateFileSystem(self, request):
        """创建文件系统（异步）。

        :param request: Request instance for CreateFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFileSystemResponse()
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


    def CreateMountPoint(self, request):
        """创建文件系统挂载点，仅限于创建成功的文件系统。

        :param request: Request instance for CreateMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.CreateMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.CreateMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMountPointResponse()
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


    def DescribeAccessGroup(self, request):
        """查看权限组详细信息。

        :param request: Request instance for DescribeAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessGroupResponse()
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


    def DescribeAccessGroups(self, request):
        """查看权限组列表。

        :param request: Request instance for DescribeAccessGroups.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessGroupsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessGroupsResponse()
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


    def DescribeAccessRules(self, request):
        """通过权限组ID查看权限规则列表。

        :param request: Request instance for DescribeAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccessRulesResponse()
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


    def DescribeFileSystem(self, request):
        """查看文件系统详细信息。

        :param request: Request instance for DescribeFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileSystemResponse()
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


    def DescribeFileSystems(self, request):
        """查看文件系统列表。

        :param request: Request instance for DescribeFileSystems.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeFileSystemsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeFileSystemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileSystems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileSystemsResponse()
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


    def DescribeMountPoint(self, request):
        """查看挂载点详细信息。

        :param request: Request instance for DescribeMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountPointResponse()
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


    def DescribeMountPoints(self, request):
        """查看挂载点列表。

        :param request: Request instance for DescribeMountPoints.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DescribeMountPointsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DescribeMountPointsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMountPoints", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMountPointsResponse()
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


    def DisassociateAccessGroups(self, request):
        """给挂载点解绑多个权限组。

        :param request: Request instance for DisassociateAccessGroups.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.DisassociateAccessGroupsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.DisassociateAccessGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateAccessGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateAccessGroupsResponse()
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


    def ModifyAccessGroup(self, request):
        """修改权限组属性。

        :param request: Request instance for ModifyAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessGroupResponse()
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


    def ModifyFileSystem(self, request):
        """修改文件系统属性，仅限于创建成功的文件系统。

        :param request: Request instance for ModifyFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyFileSystemResponse()
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


    def ModifyMountPoint(self, request):
        """修改挂载点属性。

        :param request: Request instance for ModifyMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMountPointResponse()
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
        """修改资源标签列表，全量覆盖。

        :param request: Request instance for ModifyResourceTags.
        :type request: :class:`tencentcloud.chdfs.v20201112.models.ModifyResourceTagsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20201112.models.ModifyResourceTagsResponse`

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