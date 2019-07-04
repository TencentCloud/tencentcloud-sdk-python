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
from tencentcloud.gme.v20180711 import models


class GmeClient(AbstractClient):
    _apiVersion = '2018-07-11'
    _endpoint = 'gme.tencentcloudapi.com'


    def DescribeFilterResultList(self, request):
        """根据日期查询识别结果列表

        :param request: 调用DescribeFilterResultList所需参数的结构体。
        :type request: :class:`tencentcloud.gme.v20180711.models.DescribeFilterResultListRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.DescribeFilterResultListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFilterResultList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFilterResultListResponse()
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


    def VoiceFilter(self, request):
        """本接口用于识别涉黄、涉政等违规音频，成功会回调配置在应用的回调地址。回调示例如下：
        {"BizId":0,"FileId":"test_file_id","FileName":"test_file_name","FileUrl":"test_file_url","OpenId":"test_open_id","TimeStamp":"0000-00-00 00:00:00","Data":[{"Type":1,"Word":"xx"}]}
        Type表示过滤类型，1：政治，2：色情

        :param request: 调用VoiceFilter所需参数的结构体。
        :type request: :class:`tencentcloud.gme.v20180711.models.VoiceFilterRequest`
        :rtype: :class:`tencentcloud.gme.v20180711.models.VoiceFilterResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VoiceFilter", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VoiceFilterResponse()
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