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
from tencentcloud.mgobe.v20201014 import models


class MgobeClient(AbstractClient):
    _apiVersion = '2020-10-14'
    _endpoint = 'mgobe.tencentcloudapi.com'
    _service = 'mgobe'


    def ChangeRoomPlayerProfile(self, request):
        """此接口无法使用，游戏联机对战引擎MGOBE已于6.1正式下架，感谢您的支持

        修改房间玩家自定义属性

        :param request: Request instance for ChangeRoomPlayerProfile.
        :type request: :class:`tencentcloud.mgobe.v20201014.models.ChangeRoomPlayerProfileRequest`
        :rtype: :class:`tencentcloud.mgobe.v20201014.models.ChangeRoomPlayerProfileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeRoomPlayerProfile", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChangeRoomPlayerProfileResponse()
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


    def ChangeRoomPlayerStatus(self, request):
        """此接口无法使用，游戏联机对战引擎MGOBE已于6.1正式下架，感谢您的支持

        修改玩家自定义状态

        :param request: Request instance for ChangeRoomPlayerStatus.
        :type request: :class:`tencentcloud.mgobe.v20201014.models.ChangeRoomPlayerStatusRequest`
        :rtype: :class:`tencentcloud.mgobe.v20201014.models.ChangeRoomPlayerStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChangeRoomPlayerStatus", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChangeRoomPlayerStatusResponse()
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


    def DescribePlayer(self, request):
        """此接口无法使用，游戏联机对战引擎MGOBE已于6.1正式下架，感谢您的支持

        该接口用于查询玩家信息。支持两种用法，当OpenId不传的时候，PlayerId必传，传入PlayerId可以查询当前PlayerId的玩家信息，当OpenId传入的时候，PlayerId可不传，按照OpenId查询玩家信息。

        :param request: Request instance for DescribePlayer.
        :type request: :class:`tencentcloud.mgobe.v20201014.models.DescribePlayerRequest`
        :rtype: :class:`tencentcloud.mgobe.v20201014.models.DescribePlayerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePlayer", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePlayerResponse()
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
        """此接口无法使用，游戏联机对战引擎MGOBE已于6.1正式下架，感谢您的支持

        该接口用于查询房间信息。支持两种用法，当房间Id不传的时候，玩家Id必传，传入玩家Id可以查询当前玩家所在的房间信息，当房间Id传入的时候，玩家Id可不传，按照房间Id查询房间信息。

        :param request: Request instance for DescribeRoom.
        :type request: :class:`tencentcloud.mgobe.v20201014.models.DescribeRoomRequest`
        :rtype: :class:`tencentcloud.mgobe.v20201014.models.DescribeRoomResponse`

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


    def DismissRoom(self, request):
        """此接口无法使用，游戏联机对战引擎MGOBE已于6.1正式下架，感谢您的支持

        通过game_id、room_id解散房间

        :param request: Request instance for DismissRoom.
        :type request: :class:`tencentcloud.mgobe.v20201014.models.DismissRoomRequest`
        :rtype: :class:`tencentcloud.mgobe.v20201014.models.DismissRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismissRoom", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DismissRoomResponse()
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


    def ModifyRoom(self, request):
        """此接口无法使用，游戏联机对战引擎MGOBE已于6.1正式下架，感谢您的支持

        修改房间

        :param request: Request instance for ModifyRoom.
        :type request: :class:`tencentcloud.mgobe.v20201014.models.ModifyRoomRequest`
        :rtype: :class:`tencentcloud.mgobe.v20201014.models.ModifyRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRoom", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRoomResponse()
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


    def RemoveRoomPlayer(self, request):
        """此接口无法使用，游戏联机对战引擎MGOBE已于6.1正式下架，感谢您的支持

        踢出房间玩家

        :param request: Request instance for RemoveRoomPlayer.
        :type request: :class:`tencentcloud.mgobe.v20201014.models.RemoveRoomPlayerRequest`
        :rtype: :class:`tencentcloud.mgobe.v20201014.models.RemoveRoomPlayerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveRoomPlayer", params, headers=headers)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveRoomPlayerResponse()
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