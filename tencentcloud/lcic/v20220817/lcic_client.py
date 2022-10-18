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
from tencentcloud.lcic.v20220817 import models


class LcicClient(AbstractClient):
    _apiVersion = '2022-08-17'
    _endpoint = 'lcic.tencentcloudapi.com'
    _service = 'lcic'


    def BindDocumentToRoom(self, request):
        """绑定文档到房间

        :param request: Request instance for BindDocumentToRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.BindDocumentToRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.BindDocumentToRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindDocumentToRoom", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.BindDocumentToRoomResponse()
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


    def CreateDocument(self, request):
        """创建房间内可以使用的文档。

        :param request: Request instance for CreateDocument.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateDocumentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDocument", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDocumentResponse()
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


    def CreateRoom(self, request):
        """创建房间

        :param request: Request instance for CreateRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoom", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoomResponse()
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


    def CreateSupervisor(self, request):
        """创建巡课

        :param request: Request instance for CreateSupervisor.
        :type request: :class:`tencentcloud.lcic.v20220817.models.CreateSupervisorRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.CreateSupervisorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSupervisor", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSupervisorResponse()
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


    def DeleteRoom(self, request):
        """删除房间

        :param request: Request instance for DeleteRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DeleteRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DeleteRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoom", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRoomResponse()
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


    def DescribeRoom(self, request):
        """获取房间信息

        :param request: Request instance for DescribeRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoom", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoomResponse()
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


    def DescribeRoomStatistics(self, request):
        """获取房间统计信息，仅可在房间结束后调用。

        :param request: Request instance for DescribeRoomStatistics.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomStatisticsRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeRoomStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoomStatistics", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRoomStatisticsResponse()
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


    def DescribeUser(self, request):
        """获取用户信息

        :param request: Request instance for DescribeUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.DescribeUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.DescribeUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserResponse()
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


    def LoginOriginId(self, request):
        """使用源账号登录，源账号为注册时填入的originId

        :param request: Request instance for LoginOriginId.
        :type request: :class:`tencentcloud.lcic.v20220817.models.LoginOriginIdRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.LoginOriginIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LoginOriginId", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LoginOriginIdResponse()
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


    def LoginUser(self, request):
        """登录

        :param request: Request instance for LoginUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.LoginUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.LoginUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LoginUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LoginUserResponse()
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


    def ModifyApp(self, request):
        """修改应用

        :param request: Request instance for ModifyApp.
        :type request: :class:`tencentcloud.lcic.v20220817.models.ModifyAppRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.ModifyAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyApp", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAppResponse()
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


    def RegisterUser(self, request):
        """注册用户

        :param request: Request instance for RegisterUser.
        :type request: :class:`tencentcloud.lcic.v20220817.models.RegisterUserRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.RegisterUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterUser", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RegisterUserResponse()
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


    def SetAppCustomContent(self, request):
        """设置应用的自定义内容，包括应用图标，自定义的代码等。如果已存在，则为更新。更新js、css内容后，要生效也需要调用该接口

        :param request: Request instance for SetAppCustomContent.
        :type request: :class:`tencentcloud.lcic.v20220817.models.SetAppCustomContentRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.SetAppCustomContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAppCustomContent", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetAppCustomContentResponse()
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


    def UnbindDocumentFromRoom(self, request):
        """文档从房间解绑

        :param request: Request instance for UnbindDocumentFromRoom.
        :type request: :class:`tencentcloud.lcic.v20220817.models.UnbindDocumentFromRoomRequest`
        :rtype: :class:`tencentcloud.lcic.v20220817.models.UnbindDocumentFromRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindDocumentFromRoom", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnbindDocumentFromRoomResponse()
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