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


    def AudioModeration(self, request):
        """音频内容检测（Audio Moderation, AM）服务使用了波形分析、声纹分析等技术，能识别涉黄、涉政、涉恐等违规音频，同时支持用户配置音频黑库，打击自定义的违规内容。

        通过API直接上传音频即可进行检测，对于高危部分直接屏蔽，可疑部分人工复审，从而节省审核人力，释放业务风险。

        :param request: 调用AudioModeration所需参数的结构体。
        :type request: :class:`tencentcloud.cms.v20190321.models.AudioModerationRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.AudioModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AudioModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AudioModerationResponse()
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


    def DescribeModerationOverview(self, request):
        """根据日期，渠道和服务类型查询识别结果概览数据

        :param request: 调用DescribeModerationOverview所需参数的结构体。
        :type request: :class:`tencentcloud.cms.v20190321.models.DescribeModerationOverviewRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.DescribeModerationOverviewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeModerationOverview", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeModerationOverviewResponse()
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
        通过API获取检测的标签及置信度，可直接采信高置信度的结果，人工复审低置信度的结果，从而降低人工成本，提高审核效率。

        :param request: 调用ImageModeration所需参数的结构体。
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


    def TextModeration(self, request):
        """文本内容检测（Text Moderation）服务使用了深度学习技术，识别涉黄、涉政、涉恐等有害内容，同时支持用户配置词库，打击自定义的违规文本。
        通过API接口，能检测内容的危险等级，对于高危部分直接过滤，可疑部分人工复审，从而节省审核人力，释放业务风险。

        :param request: 调用TextModeration所需参数的结构体。
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


    def VideoModeration(self, request):
        """视频内容检测（Video Moderation, VM）服务能识别涉黄、涉政、涉恐等违规视频，同时支持用户配置视频黑库，打击自定义的违规内容。
        通过API直接上传视频即可进行检测，对于高危部分直接过滤，可疑部分人工复审，从而节省审核人力，释放业务风险。

        :param request: 调用VideoModeration所需参数的结构体。
        :type request: :class:`tencentcloud.cms.v20190321.models.VideoModerationRequest`
        :rtype: :class:`tencentcloud.cms.v20190321.models.VideoModerationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("VideoModeration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.VideoModerationResponse()
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