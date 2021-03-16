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
from tencentcloud.chdfs.v20190718 import models


class ChdfsClient(AbstractClient):
    _apiVersion = '2019-07-18'
    _endpoint = 'chdfs.tencentcloudapi.com'
    _service = 'chdfs'


    def CreateAccessGroup(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        创建权限组。

        :param request: Request instance for CreateAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateAccessGroupResponse`

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


    def CreateAccessRules(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量创建权限规则，权限规则ID和创建时间无需填写。

        :param request: Request instance for CreateAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccessRulesResponse()
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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        创建文件系统（异步）。

        :param request: Request instance for CreateFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateFileSystemResponse`

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


    def CreateLifeCycleRules(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量创建生命周期规则，生命周期规则ID和创建时间无需填写。

        :param request: Request instance for CreateLifeCycleRules.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateLifeCycleRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateLifeCycleRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLifeCycleRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLifeCycleRulesResponse()
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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        创建文件系统挂载点，仅限于创建成功的文件系统。

        :param request: Request instance for CreateMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateMountPointResponse`

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


    def CreateRestoreTasks(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量创建回热任务，回热任务ID、状态和创建时间无需填写。

        :param request: Request instance for CreateRestoreTasks.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.CreateRestoreTasksRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.CreateRestoreTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRestoreTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRestoreTasksResponse()
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


    def DeleteAccessGroup(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        删除权限组。

        :param request: Request instance for DeleteAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteAccessGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccessGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccessGroupResponse()
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


    def DeleteAccessRules(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量删除权限规则。

        :param request: Request instance for DeleteAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccessRulesResponse()
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


    def DeleteFileSystem(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        删除文件系统，不允许删除非空文件系统。

        :param request: Request instance for DeleteFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteFileSystemResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFileSystem", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFileSystemResponse()
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


    def DeleteLifeCycleRules(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量删除生命周期规则。

        :param request: Request instance for DeleteLifeCycleRules.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteLifeCycleRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteLifeCycleRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLifeCycleRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLifeCycleRulesResponse()
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


    def DeleteMountPoint(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        删除挂载点。

        :param request: Request instance for DeleteMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DeleteMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DeleteMountPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMountPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMountPointResponse()
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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        查看权限组列表。

        :param request: Request instance for DescribeAccessGroups.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeAccessGroupsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeAccessGroupsResponse`

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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过权限组ID查看权限规则列表。

        :param request: Request instance for DescribeAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeAccessRulesResponse`

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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        查看文件系统详细信息。

        :param request: Request instance for DescribeFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeFileSystemResponse`

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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        查看文件系统列表。

        :param request: Request instance for DescribeFileSystems.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeFileSystemsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeFileSystemsResponse`

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


    def DescribeLifeCycleRules(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过文件系统ID查看生命周期规则列表。

        :param request: Request instance for DescribeLifeCycleRules.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeLifeCycleRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeLifeCycleRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLifeCycleRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLifeCycleRulesResponse()
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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        查看挂载点详细信息。

        :param request: Request instance for DescribeMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeMountPointResponse`

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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过文件系统ID或者权限组ID查看挂载点列表。

        :param request: Request instance for DescribeMountPoints.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeMountPointsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeMountPointsResponse`

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


    def DescribeResourceTags(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过文件系统ID查看资源标签列表。

        :param request: Request instance for DescribeResourceTags.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeResourceTagsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeResourceTagsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeResourceTags", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeResourceTagsResponse()
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


    def DescribeRestoreTasks(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        通过文件系统ID查看回热任务列表。

        :param request: Request instance for DescribeRestoreTasks.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.DescribeRestoreTasksRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.DescribeRestoreTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRestoreTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRestoreTasksResponse()
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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        修改权限组属性。

        :param request: Request instance for ModifyAccessGroup.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyAccessGroupRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyAccessGroupResponse`

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


    def ModifyAccessRules(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量修改权限规则属性，需要指定权限规则ID，支持修改权限规则地址、访问模式和优先级。

        :param request: Request instance for ModifyAccessRules.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyAccessRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyAccessRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccessRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccessRulesResponse()
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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        修改文件系统属性，仅限于创建成功的文件系统。

        :param request: Request instance for ModifyFileSystem.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyFileSystemRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyFileSystemResponse`

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


    def ModifyLifeCycleRules(self, request):
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        批量修改生命周期规则属性，需要指定生命周期规则ID，支持修改生命周期规则名称、路径、转换列表和状态。

        :param request: Request instance for ModifyLifeCycleRules.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyLifeCycleRulesRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyLifeCycleRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLifeCycleRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLifeCycleRulesResponse()
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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        修改挂载点属性。

        :param request: Request instance for ModifyMountPoint.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyMountPointRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyMountPointResponse`

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
        """云API旧版本2019-07-18预下线，所有功能由新版本2020-11-12替代，目前云API主要用作控制台使用。

        修改资源标签列表，全量覆盖。

        :param request: Request instance for ModifyResourceTags.
        :type request: :class:`tencentcloud.chdfs.v20190718.models.ModifyResourceTagsRequest`
        :rtype: :class:`tencentcloud.chdfs.v20190718.models.ModifyResourceTagsResponse`

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