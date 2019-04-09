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
from tencentcloud.tbm.v20180129 import models


class TbmClient(AbstractClient):
    _apiVersion = '2018-01-29'
    _endpoint = 'tbm.tencentcloudapi.com'


    def DescribeBrandCommentCount(self, request):
        """通过分析用户在评价品牌时用词的正负面情绪评分，返回品牌好评与差评评价条数，按天输出结果。

        :param request: 调用DescribeBrandCommentCount所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandCommentCountRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandCommentCountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandCommentCount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandCommentCountResponse()
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


    def DescribeBrandExposure(self, request):
        """监测品牌关键词命中文章标题或全文的文章篇数，按天输出数据。

        :param request: 调用DescribeBrandExposure所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandExposureRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandExposureResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandExposure", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandExposureResponse()
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


    def DescribeBrandMediaReport(self, request):
        """监测品牌关键词出现在媒体网站（新闻媒体、网络门户、政府网站、微信公众号、天天快报等）发布资讯标题和正文中的报道数。按天输出结果。

        :param request: 调用DescribeBrandMediaReport所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandMediaReportRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandMediaReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandMediaReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandMediaReportResponse()
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


    def DescribeBrandNegComments(self, request):
        """通过分析用户在评价品牌时用词的正负面情绪评分，返回品牌热门差评观点列表。

        :param request: 调用DescribeBrandNegComments所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandNegCommentsRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandNegCommentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandNegComments", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandNegCommentsResponse()
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


    def DescribeBrandPosComments(self, request):
        """通过分析用户在评价品牌时用词的正负面情绪评分，返回品牌热门好评观点列表。

        :param request: 调用DescribeBrandPosComments所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandPosCommentsRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandPosCommentsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandPosComments", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandPosCommentsResponse()
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


    def DescribeBrandSocialOpinion(self, request):
        """检测品牌关键词出现在微博、QQ兴趣部落、论坛、博客等个人公开贡献资讯中的内容，每天聚合近30天热度最高的观点列表。

        :param request: 调用DescribeBrandSocialOpinion所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandSocialOpinionRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandSocialOpinionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandSocialOpinion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandSocialOpinionResponse()
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


    def DescribeBrandSocialReport(self, request):
        """监测品牌关键词出现在微博、QQ兴趣部落、论坛、博客等个人公开贡献资讯中的条数。按天输出数据结果。

        :param request: 调用DescribeBrandSocialReport所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandSocialReportRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeBrandSocialReportResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBrandSocialReport", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBrandSocialReportResponse()
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


    def DescribeIndustryNews(self, request):
        """根据客户定制的行业关键词，监测关键词出现在媒体网站（新闻媒体、网络门户、政府网站、微信公众号、天天快报等）发布资讯标题和正文中的报道数，以及文章列表、来源渠道、作者、发布时间等。

        :param request: 调用DescribeIndustryNews所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeIndustryNewsRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeIndustryNewsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIndustryNews", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIndustryNewsResponse()
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


    def DescribeUserPortrait(self, request):
        """通过分析洞察参与过品牌媒体互动的用户，比如公开发表品牌的新闻评论、在公开社交渠道发表过对品牌的评价观点等用户，返回用户的画像属性分布，例如性别、年龄、地域、喜爱的明星、喜爱的影视。

        :param request: 调用DescribeUserPortrait所需参数的结构体。
        :type request: :class:`tencentcloud.tbm.v20180129.models.DescribeUserPortraitRequest`
        :rtype: :class:`tencentcloud.tbm.v20180129.models.DescribeUserPortraitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUserPortrait", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUserPortraitResponse()
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