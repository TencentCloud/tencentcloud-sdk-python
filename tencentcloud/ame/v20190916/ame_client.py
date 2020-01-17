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
from tencentcloud.ame.v20190916 import models


class AmeClient(AbstractClient):
    _apiVersion = '2019-09-16'
    _endpoint = 'ame.tencentcloudapi.com'


    def DescribeItems(self, request):
        """分类内容下歌曲列表获取，根据CategoryID或CategoryCode

        :param request: Request instance for DescribeItems.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeItemsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeItemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeItems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeItemsResponse()
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


    def DescribeLyric(self, request):
        """根据接口的模式及歌曲ID来取得歌词信息。

        :param request: Request instance for DescribeLyric.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeLyricRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeLyricResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLyric", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLyricResponse()
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


    def DescribeMusic(self, request):
        """根据接口的模式及歌曲ID来取得对应权限的歌曲播放地址等信息。

        :param request: Request instance for DescribeMusic.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeMusicRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeMusicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMusic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMusicResponse()
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


    def DescribeStations(self, request):
        """获取素材库列表时使用

        :param request: Request instance for DescribeStations.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeStationsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeStationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeStations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeStationsResponse()
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


    def ReportData(self, request):
        """客户上报用户数据功能，为了更好的为用户提供优质服务

        :param request: Request instance for ReportData.
        :type request: :class:`tencentcloud.ame.v20190916.models.ReportDataRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.ReportDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReportData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReportDataResponse()
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