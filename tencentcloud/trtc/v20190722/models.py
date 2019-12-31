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

from tencentcloud.common.abstract_model import AbstractModel


class DismissRoomRequest(AbstractModel):
    """DismissRoom请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        """
        self.SdkAppId = None
        self.RoomId = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")


class DismissRoomResponse(AbstractModel):
    """DismissRoom返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveUserRequest(AbstractModel):
    """RemoveUser请求参数结构体

    """

    def __init__(self):
        """
        :param SdkAppId: TRTC的SDKAppId。
        :type SdkAppId: int
        :param RoomId: 房间号。
        :type RoomId: int
        :param UserIds: 要移出的用户列表，最多10个。
        :type UserIds: list of str
        """
        self.SdkAppId = None
        self.RoomId = None
        self.UserIds = None


    def _deserialize(self, params):
        self.SdkAppId = params.get("SdkAppId")
        self.RoomId = params.get("RoomId")
        self.UserIds = params.get("UserIds")


class RemoveUserResponse(AbstractModel):
    """RemoveUser返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")