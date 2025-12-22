# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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
from tencentcloud.vclm.v20240523 import models


class VclmClient(AbstractClient):
    _apiVersion = '2024-05-23'
    _endpoint = 'vclm.tencentcloudapi.com'
    _service = 'vclm'


    def CheckAnimateImageJob(self, request):
        r"""检查图片跳舞输入图

        :param request: Request instance for CheckAnimateImageJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.CheckAnimateImageJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.CheckAnimateImageJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAnimateImageJob", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAnimateImageJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHumanActorJob(self, request):
        r"""通过JobId提交请求，获取人像驱动任务的结果信息。

        :param request: Request instance for DescribeHumanActorJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeHumanActorJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeHumanActorJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHumanActorJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHumanActorJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHunyuanToVideoJob(self, request):
        r"""查询混元生视频任务

        :param request: Request instance for DescribeHunyuanToVideoJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeHunyuanToVideoJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeHunyuanToVideoJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHunyuanToVideoJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHunyuanToVideoJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAnimateJob(self, request):
        r"""用于查询图片跳舞任务。图片跳舞能力支持舞蹈动作结合图片生成跳舞视频，满足社交娱乐、互动营销等场景的需求。

        :param request: Request instance for DescribeImageAnimateJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeImageAnimateJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeImageAnimateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageAnimateJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageAnimateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageToVideoGeneralJob(self, request):
        r"""查询图生视频通用能力任务接口

        :param request: Request instance for DescribeImageToVideoGeneralJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeImageToVideoGeneralJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeImageToVideoGeneralJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeImageToVideoGeneralJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeImageToVideoGeneralJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePortraitSingJob(self, request):
        r"""用于查询图片唱演任务。
        支持提交音频和图片生成唱演视频，满足社交娱乐、互动营销等场景的需求。

        :param request: Request instance for DescribePortraitSingJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribePortraitSingJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribePortraitSingJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePortraitSingJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePortraitSingJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplateToVideoJob(self, request):
        r"""用于查询视频特效任务。

        :param request: Request instance for DescribeTemplateToVideoJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeTemplateToVideoJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeTemplateToVideoJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateToVideoJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateToVideoJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoEditJob(self, request):
        r"""用于提交视频编辑任务，支持上传视频、文本及图片素材开展编辑操作，涵盖风格迁移、元素替换、内容增减等核心能力。

        :param request: Request instance for DescribeVideoEditJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoEditJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoEditJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoEditJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoEditJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoFaceFusionJob(self, request):
        r"""查询视频人脸融合任务

        :param request: Request instance for DescribeVideoFaceFusionJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoFaceFusionJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoFaceFusionJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoFaceFusionJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoFaceFusionJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoStylizationJob(self, request):
        r"""用于查询视频风格化任务。视频风格化支持将输入视频生成特定风格的视频。生成后的视频画面风格多样、流畅自然，能够满足社交娱乐、互动营销、视频素材制作等场景的需求。

        :param request: Request instance for DescribeVideoStylizationJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoStylizationJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoStylizationJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoStylizationJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoStylizationJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoVoiceJob(self, request):
        r"""通过JobId提交请求，获取视频配音频任务的结果信息。

        :param request: Request instance for DescribeVideoVoiceJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoVoiceJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoVoiceJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoVoiceJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoVoiceJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHumanActorJob(self, request):
        r"""用于提交人像驱动任务
        支持提交音频和图文来生成对应视频，满足动态交互、内容生产等场景需求。

        :param request: Request instance for SubmitHumanActorJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitHumanActorJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitHumanActorJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHumanActorJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHumanActorJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanToVideoJob(self, request):
        r"""●混元生视频接口，基于混元大模型，根据输入的文本或图片智能生成视频。

        ●默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for SubmitHunyuanToVideoJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitHunyuanToVideoJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitHunyuanToVideoJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanToVideoJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanToVideoJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitImageAnimateJob(self, request):
        r"""用于提交图片跳舞任务。图片跳舞能力支持舞蹈动作结合图片生成跳舞视频，满足社交娱乐、互动营销等场景的需求。

        :param request: Request instance for SubmitImageAnimateJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitImageAnimateJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitImageAnimateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitImageAnimateJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitImageAnimateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitImageToVideoGeneralJob(self, request):
        r"""图生视频通用能力接口

        :param request: Request instance for SubmitImageToVideoGeneralJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitImageToVideoGeneralJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitImageToVideoGeneralJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitImageToVideoGeneralJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitImageToVideoGeneralJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitPortraitSingJob(self, request):
        r"""用于提交图片唱演任务。
        支持提交音频和图片生成唱演视频，满足社交娱乐、互动营销等场景的需求。

        :param request: Request instance for SubmitPortraitSingJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitPortraitSingJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitPortraitSingJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitPortraitSingJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitPortraitSingJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTemplateToVideoJob(self, request):
        r"""提交视频特效任务接口

        :param request: Request instance for SubmitTemplateToVideoJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitTemplateToVideoJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitTemplateToVideoJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTemplateToVideoJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTemplateToVideoJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitVideoEditJob(self, request):
        r"""用于提交视频编辑任务，支持上传视频、文本及图片素材开展编辑操作，涵盖风格迁移、元素替换、内容增减等核心能力。

        :param request: Request instance for SubmitVideoEditJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoEditJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoEditJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitVideoEditJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitVideoEditJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitVideoFaceFusionJob(self, request):
        r"""提交视频人脸融合任务

        :param request: Request instance for SubmitVideoFaceFusionJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoFaceFusionJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoFaceFusionJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitVideoFaceFusionJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitVideoFaceFusionJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitVideoStylizationJob(self, request):
        r"""用于提交视频风格化任务。支持将输入视频生成特定风格的视频。生成后的视频画面风格多样、流畅自然，能够满足社交娱乐、互动营销、视频素材制作等场景的需求。

        :param request: Request instance for SubmitVideoStylizationJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoStylizationJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoStylizationJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitVideoStylizationJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitVideoStylizationJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitVideoVoiceJob(self, request):
        r"""提交视频配音效任务，输入视频后提交请求，会返回一个JobId，用于查询视频配音效的处理进度。

        :param request: Request instance for SubmitVideoVoiceJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoVoiceJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoVoiceJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitVideoVoiceJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitVideoVoiceJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))