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

        <br>
        接口返回值说明：调用本接口有两个返回值，一个是同步返回值，一个是识别完成后的异步回调返回值。

        音频识别结果存在于异步回调返回值中，异步回调返回值明细：

        参数名 | 类型 | 描述
        -|-|-
        SeqID | String | 请求seqId唯一标识
        EvilFlag | Integer | 是否恶意：0正常，1可疑（Homology模块下：0未匹配到，1恶意，2白样本）
        EvilType | Integer | 恶意类型：100正常，20001政治，20002色情，20007谩骂
        Duration | Integer | 音频时长（单位：毫秒）
        PornDetect | [AudioDetectData](#ADD) | 音频智能鉴黄
        PolityDetect | [AudioDetectData](#ADD)| 音频涉政识别
        CurseDetect | [AudioDetectData](#ADD) | 音频谩骂识别
        CustomizedDetect | [AudioDetectData](#ADD) | 自定义识别
        Homology | [AudioDetectData](#ADD) | 相似度识别


        <span id="ADD"> AudioDetectData </span>

        参数名 | 类型 | 描述
        -|-|-
        HitFlag | Integer | 0正常，1可疑
        Score | Integer | 判断分值
        EvilType | Integer | 恶意类型：100正常，20001政治，20002色情，20007谩骂
        Keywords | Array of String | 关键词明细
        StartTime | Array of String | 恶意开始时间（Homology、CustomizedDetect无此字段）
        EndTime | Array of String | 恶意结束时间（Homology、CustomizedDetect无此字段）
        SeedUrl | String | 命中的种子URL

        :param request: Request instance for AudioModeration.
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


    def CreateFileSample(self, request):
        """通过该接口可以将文件新增到样本库

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
        """新增文本类型样本库

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
        """删除文件样本库，支持批量删除，一次提交不超过20个

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
        """删除文字样本库，暂时只支持单个删除

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
        """查询文件样本库，支持批量查询

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


    def DescribeModerationOverview(self, request):
        """根据日期，渠道和服务类型查询识别结果概览数据

        :param request: Request instance for DescribeModerationOverview.
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


    def DescribeTextSample(self, request):
        """支持批量查询文字样本库

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


    def VideoModeration(self, request):
        """视频内容检测（Video Moderation, VM）服务能识别涉黄、涉政、涉恐等违规视频，同时支持用户配置视频黑库，打击自定义的违规内容。

        <br>
        接口返回值说明：调用本接口有两个返回值，一个是同步返回值，一个是识别完成后的异步回调返回值。

        视频识别结果存在于异步回调返回值中，异步回调返回值明细：

        参数名 | 类型 | 描述
        -|-|-
        SeqID | String | 请求seqId唯一标识
        EvilFlag | Integer | 是否恶意：0正常，1可疑（Homology模块下：0未匹配到，1恶意，2白样本）
        EvilType | Integer | 恶意类型：100正常，20001政治，20002色情
        Duration | Integer | 视频时长（单位：秒）
        PornDetect | [VideoDetectData](#VDD) | 视频智能鉴黄
        PolityDetect | [VideoDetectData](#VDD) | 视频涉政识别
        Homology | [VideoDetectData](#VDD) | 相似度识别


        <span id="VDD">VideoDetectData</span>

        参数名 | 类型 | 描述
        -|-|-
        HitFlag | Integer  | 0正常，1可疑
        Score | Integer | 判断分值
        EvilType | Integer | 恶意类型：100正常，20001政治，20002色情
        Keywords | Array of String | 关键词明细
        SeedUrl | String | 命中的种子URL

        :param request: Request instance for VideoModeration.
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