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
from tencentcloud.cms.v20190321 import models


class CmsClient(AbstractClient):
    _apiVersion = '2019-03-21'
    _endpoint = 'cms.tencentcloudapi.com'
    _service = 'cms'


    def CreateKeywordsSamples(self, request):
        """创建关键词接口

        :param request: Request instance for CreateKeywordsSamples.
        :type request: :class:`tencentcloud.cms.v20190321.models.CreateKeywordsSamplesRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.CreateKeywordsSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateKeywordsSamples", params, headers=headers)
            response = json.loads(body)
            model = models.CreateKeywordsSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLibSamples(self, request):
        """删除关键词接口

        :param request: Request instance for DeleteLibSamples.
        :type request: :class:`tencentcloud.cms.v20190321.models.DeleteLibSamplesRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.DeleteLibSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLibSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLibSamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeKeywordsLibs(self, request):
        """获取用户词库列表

        :param request: Request instance for DescribeKeywordsLibs.
        :type request: :class:`tencentcloud.cms.v20190321.models.DescribeKeywordsLibsRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.DescribeKeywordsLibsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeKeywordsLibs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeKeywordsLibsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLibSamples(self, request):
        """获取关键词接口

        :param request: Request instance for DescribeLibSamples.
        :type request: :class:`tencentcloud.cms.v20190321.models.DescribeLibSamplesRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.DescribeLibSamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLibSamples", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLibSamplesResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("ImageModeration", params, headers=headers)
            response = json.loads(body)
            model = models.ImageModerationResponse()
            model._deserialize(response["Response"])
            return model
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
            headers = request.headers
            body = self.call("TextModeration", params, headers=headers)
            response = json.loads(body)
            model = models.TextModerationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)