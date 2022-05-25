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
from tencentcloud.dasb.v20191018 import models


class DasbClient(AbstractClient):
    _apiVersion = '2019-10-18'
    _endpoint = 'dasb.tencentcloudapi.com'
    _service = 'dasb'


    def CreateAcl(self, request):
        """新建访问权限

        :param request: Request instance for CreateAcl.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateAclRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAcl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAclResponse()
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


    def CreateUser(self, request):
        """新建用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.dasb.v20191018.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateUserResponse()
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


    def DeleteAcls(self, request):
        """删除访问权限

        :param request: Request instance for DeleteAcls.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteAclsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAcls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAclsResponse()
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


    def DeleteUsers(self, request):
        """删除用户

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DeleteUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteUsersResponse()
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


    def DescribeAcls(self, request):
        """查询访问权限列表

        :param request: Request instance for DescribeAcls.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeAclsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAcls", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAclsResponse()
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


    def DescribeDasbImageIds(self, request):
        """获取镜像列表

        :param request: Request instance for DescribeDasbImageIds.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeDasbImageIdsRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeDasbImageIdsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDasbImageIds", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDasbImageIdsResponse()
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


    def DescribeDevices(self, request):
        """查询资产列表

        :param request: Request instance for DescribeDevices.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeDevicesRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeDevicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDevices", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDevicesResponse()
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


    def DescribeUsers(self, request):
        """查询用户列表

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.dasb.v20191018.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.DescribeUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsers", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUsersResponse()
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


    def ModifyAcl(self, request):
        """修改访问权限

        :param request: Request instance for ModifyAcl.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyAclRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAcl", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAclResponse()
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


    def ModifyUser(self, request):
        """修改用户信息

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.dasb.v20191018.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.dasb.v20191018.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyUserResponse()
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