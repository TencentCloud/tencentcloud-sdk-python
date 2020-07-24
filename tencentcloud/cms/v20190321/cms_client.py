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
from tencentcloud.cms.v20190321 import models


class CmsClient(AbstractClient):
    _apiVersion = '2019-03-21'
    _endpoint = 'cms.tencentcloudapi.com'


    def CreateFileSample(self, request):
        """本文档适用于图片内容安全、视频内容安全自定义识别库的管理。
        <br>
        通过该接口可以将图片新增到样本库。

        :param request: Request instance for CreateFileSample.
        :type request: :class:`tencentcloud.cms.v20190321.models.CreateFileSampleRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.CreateFileSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFileSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFileSampleResponse()
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


    def CreateTextSample(self, request):
        """本文档适用于文本内容安全、音频内容安全自定义识别库的管理。
        <br>
        通过该接口可以将文本新增到样本库。

        :param request: Request instance for CreateTextSample.
        :type request: :class:`tencentcloud.cms.v20190321.models.CreateTextSampleRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.CreateTextSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTextSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTextSampleResponse()
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


    def DeleteFileSample(self, request):
        """本文档适用于图片内容安全、视频内容安全自定义识别库的管理。
        <br>
        删除图片样本库，支持批量删除，一次提交不超过20个。

        :param request: Request instance for DeleteFileSample.
        :type request: :class:`tencentcloud.cms.v20190321.models.DeleteFileSampleRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.DeleteFileSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFileSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFileSampleResponse()
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


    def DeleteTextSample(self, request):
        """本文档适用于文本内容安全、音频内容安全自定义识别库的管理。
        <br>
        删除文本样本库，暂时只支持单个删除。

        :param request: Request instance for DeleteTextSample.
        :type request: :class:`tencentcloud.cms.v20190321.models.DeleteTextSampleRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.DeleteTextSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTextSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTextSampleResponse()
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


    def DescribeFileSample(self, request):
        """本文档适用于图片内容安全、视频内容安全自定义识别库的管理。
        <br>
        查询图片样本库，支持批量查询。

        :param request: Request instance for DescribeFileSample.
        :type request: :class:`tencentcloud.cms.v20190321.models.DescribeFileSampleRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.DescribeFileSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFileSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFileSampleResponse()
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


    def DescribeTextSample(self, request):
        """本文档适用于文本内容安全、音频内容安全自定义识别库的管理。
        <br>
        支持批量查询文本样本库。

        :param request: Request instance for DescribeTextSample.
        :type request: :class:`tencentcloud.cms.v20190321.models.DescribeTextSampleRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.DescribeTextSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTextSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTextSampleResponse()
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


    def ImageModeration(self, request):
        """图片内容检测服务（Image Moderation, IM）能自动扫描图片，识别涉黄、涉恐、涉政、涉毒等有害内容，同时支持用户配置图片黑名单，打击自定义的违规图片。

        :param request: Request instance for ImageModeration.
        :type request: :class:`tencentcloud.cms.v20190321.models.ImageModerationRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.ImageModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageModerationResponse()
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


    def ManualReview(self, request):
        """人工审核对外接口

        :param request: Request instance for ManualReview.
        :type request: :class:`tencentcloud.cms.v20190321.models.ManualReviewRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.ManualReviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManualReview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManualReviewResponse()
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


    def TextModeration(self, request):
        """文本内容检测（Text Moderation）服务使用了深度学习技术，识别涉黄、涉政、涉恐等有害内容，同时支持用户配置词库，打击自定义的违规文本。

        :param request: Request instance for TextModeration.
        :type request: :class:`tencentcloud.cms.v20190321.models.TextModerationRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.TextModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextModerationResponse()
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