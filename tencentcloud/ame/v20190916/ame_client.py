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
    _service = 'ame'


    def DescribeAuthInfo(self, request):
        """获取授权项目信息列表

        :param request: Request instance for DescribeAuthInfo.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeAuthInfoRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeAuthInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAuthInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAuthInfoResponse()
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


    def DescribeCloudMusic(self, request):
        """获取云音乐播放信息接口

        :param request: Request instance for DescribeCloudMusic.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeCloudMusicRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeCloudMusicResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCloudMusic", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudMusicResponse()
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


    def DescribeCloudMusicPurchased(self, request):
        """获取授权项目下已购云音乐列表

        :param request: Request instance for DescribeCloudMusicPurchased.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeCloudMusicPurchasedRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeCloudMusicPurchasedResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCloudMusicPurchased", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCloudMusicPurchasedResponse()
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


    def DescribeItemById(self, request):
        """根据歌曲ID查询歌曲信息

        :param request: Request instance for DescribeItemById.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeItemByIdRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeItemByIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeItemById", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeItemByIdResponse()
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


    def DescribeItems(self, request):
        """该服务后续会停用，不再建议使用

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


    def DescribeKTVMusicDetail(self, request):
        """根据 Id 查询歌曲的详细信息，包含基础信息及播放信息。

        :param request: Request instance for DescribeKTVMusicDetail.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribeKTVMusicDetailRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribeKTVMusicDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeKTVMusicDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeKTVMusicDetailResponse()
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
        """获取曲库包歌曲播放信息接口

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


    def DescribePackageItems(self, request):
        """获取曲库包下已核销歌曲列表接口

        :param request: Request instance for DescribePackageItems.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribePackageItemsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribePackageItemsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePackageItems", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePackageItemsResponse()
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


    def DescribePackages(self, request):
        """获取已购曲库包列表接口

        :param request: Request instance for DescribePackages.
        :type request: :class:`tencentcloud.ame.v20190916.models.DescribePackagesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.DescribePackagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePackages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePackagesResponse()
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
        """该服务后续会停用，不再建议使用

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


    def ModifyMusicOnShelves(self, request):
        """根据资源方，需要变更的参数，请求该接口进行变更，为空的参数默认为无变更

        :param request: Request instance for ModifyMusicOnShelves.
        :type request: :class:`tencentcloud.ame.v20190916.models.ModifyMusicOnShelvesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.ModifyMusicOnShelvesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMusicOnShelves", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMusicOnShelvesResponse()
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


    def PutMusicOnTheShelves(self, request):
        """根据资源方所传歌曲信息，进行歌曲上架，多个歌曲同时请求时，需构造复合结构进行请求

        :param request: Request instance for PutMusicOnTheShelves.
        :type request: :class:`tencentcloud.ame.v20190916.models.PutMusicOnTheShelvesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.PutMusicOnTheShelvesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("PutMusicOnTheShelves", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.PutMusicOnTheShelvesResponse()
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
        """客户上报用户数据功能，为了更好地为用户提供优质服务

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


    def SearchKTVMusics(self, request):
        """根据搜索条件，返回匹配的歌曲列表。

        :param request: Request instance for SearchKTVMusics.
        :type request: :class:`tencentcloud.ame.v20190916.models.SearchKTVMusicsRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.SearchKTVMusicsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SearchKTVMusics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SearchKTVMusicsResponse()
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


    def TakeMusicOffShelves(self, request):
        """根据资源方所传MusicId进行将歌曲进行下架，多个MusicId使用逗号隔开

        :param request: Request instance for TakeMusicOffShelves.
        :type request: :class:`tencentcloud.ame.v20190916.models.TakeMusicOffShelvesRequest`
        :rtype: :class:`tencentcloud.ame.v20190916.models.TakeMusicOffShelvesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TakeMusicOffShelves", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TakeMusicOffShelvesResponse()
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