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
from tencentcloud.ft.v20200304 import models


class FtClient(AbstractClient):
    _apiVersion = '2020-03-04'
    _endpoint = 'ft.tencentcloudapi.com'


    def ChangeAgePic(self, request):
        """用户上传一张人脸图片，基于人脸编辑与生成算法，输出一张人脸变老或变年轻的图片，支持实现人脸不同年龄的变化。（目前暂只支持10岁，后续放开再通知）

        :param request: Request instance for ChangeAgePic.
        :type request: :class:`tencentcloud.ft.v20200304.models.ChangeAgePicRequest`
        :rtype: :class:`tencentcloud.ft.v20200304.models.ChangeAgePicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ChangeAgePic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChangeAgePicResponse()
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


    def SwapGenderPic(self, request):
        """用户上传一张人脸图片，基于人脸编辑与生成算法，输出一张人脸性别转换的图片。男变女可实现美颜、淡妆、加刘海和长发的效果；女变男可实现加胡须、变短发的效果。

        :param request: Request instance for SwapGenderPic.
        :type request: :class:`tencentcloud.ft.v20200304.models.SwapGenderPicRequest`
        :rtype: :class:`tencentcloud.ft.v20200304.models.SwapGenderPicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SwapGenderPic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SwapGenderPicResponse()
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