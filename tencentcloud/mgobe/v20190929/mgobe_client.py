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
from tencentcloud.mgobe.v20190929 import models


class MgobeClient(AbstractClient):
    _apiVersion = '2019-09-29'
    _endpoint = 'mgobe.tencentcloudapi.com'
    _service = 'mgobe'


    def DismissRoom(self, request):
        """通过game_id、room_id解散房间

        :param request: Request instance for DismissRoom.
        :type request: :class:`tencentcloud.mgobe.v20190929.models.DismissRoomRequest`
        :rtype: :class:`tencentcloud.mgobe.v20190929.models.DismissRoomResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DismissRoom", params, headers=headers)
            response = json.loads(body)
            model = models.DismissRoomResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)