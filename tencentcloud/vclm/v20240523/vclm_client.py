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
from tencentcloud.vclm.v20240523 import models


class VclmClient(AbstractClient):
    _apiVersion = '2024-05-23'
    _endpoint = 'vclm.tencentcloudapi.com'
    _service = 'vclm'


    def ConfirmVideoTranslateJob(self, request):
        """确认视频转译结果

        :param request: Request instance for ConfirmVideoTranslateJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.ConfirmVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.ConfirmVideoTranslateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmVideoTranslateJob", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmVideoTranslateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeImageAnimateJob(self, request):
        """用于查询图片跳舞任务。图片跳舞能力支持舞蹈动作结合图片生成跳舞视频，满足社交娱乐、互动营销等场景的需求。

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


    def DescribePortraitSingJob(self, request):
        """用于查询图片唱演任务。
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


    def DescribeVideoStylizationJob(self, request):
        """用于查询视频风格化任务。视频风格化支持将输入视频生成特定风格的视频。生成后的视频画面风格多样、流畅自然，能够满足社交娱乐、互动营销、视频素材制作等场景的需求。

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


    def DescribeVideoTranslateJob(self, request):
        """查询视频翻译任务

        :param request: Request instance for DescribeVideoTranslateJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.DescribeVideoTranslateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoTranslateJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoTranslateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitImageAnimateJob(self, request):
        """用于提交图片跳舞任务。图片跳舞能力支持舞蹈动作结合图片生成跳舞视频，满足社交娱乐、互动营销等场景的需求。

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


    def SubmitPortraitSingJob(self, request):
        """用于提交图片唱演任务。
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


    def SubmitVideoStylizationJob(self, request):
        """用于提交视频风格化任务。支持将输入视频生成特定风格的视频。生成后的视频画面风格多样、流畅自然，能够满足社交娱乐、互动营销、视频素材制作等场景的需求。

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


    def SubmitVideoTranslateJob(self, request):
        """###### 支持音色种别列表
        | 音色名称                 | 性别 | 目标语言         | 音色ID |
        | ------------------------ | ---- | ---------------- | ------ |
        | Florian Multilingual     | 男 | 德语(德国)       | 701001 |
        | Seraphina                | 女  | 德语(德国)       | 701002 |
        | Ada Multilingual         | 女 | 英语(英国)       | 701003 |
        | Ollie Multilingual       | 男  | 英语(英国)       | 701004 |
        | Ava Multilingual         | 女 | 英语(美国)       | 701005 |
        | Andrew Multilingual      | 男  | 英语(美国)       | 701006 |
        | Emma Multilingual        | 女  | 英语(美国)       | 701007 |
        | Brian Multilingual       | 男  | 英语(美国)       | 701008 |
        | Jenny Multilingual       | 女  | 英语(美国)       | 701009 |
        | Ryan Multilingual        | 男  | 英语(美国)       | 701010 |
        | Adam Multilingual        | 男  | 英语(美国)       | 701011 |
        | AlloyTurbo Multilingual  | 男  | 英语(美国)       | 701012 |
        | Amanda Multilingual      | 女  | 英语(美国)       | 701013 |
        | Brandon Multilingual     | 男  | 英语(美国)       | 701014 |
        | Christopher Multilingual | 男  | 英语(美国)       | 701015 |
        | Cora Multilingual        | 女  | 英语(美国)       | 701016 |
        | Davis Multilingual       | 男  | 英语(美国)       | 701017 |
        | Derek Multilingual       | 男  | 英语(美国)       | 701018 |
        | Dustin Multilingual      | 男  | 英语(美国)       | 701019 |
        | Evelyn Multilingual      | 女  | 英语(美国)       | 701020 |
        | Lewis Multilingual       | 男  | 英语(美国)       | 701021 |
        | Lola Multilingual        | 女  | 英语(美国)       | 701022 |
        | Nancy Multilingual       | 女  | 英语(美国)       | 701023 |
        | NovaTurbo Multilingual   | 女   | 英语(美国)       | 701024 |
        | Phoebe Multilingual      | 女  | 英语(美国)       | 701025 |
        | Samuel Multilingual      | 男  | 英语(美国)       | 701026 |
        | Serena Multilingual      | 女  | 英语(美国)       | 701027 |
        | Steffan Multilingual     | 男  | 英语(美国)       | 701028 |
        | Arabella Multilingual    | 女  | 西班牙语(西班牙) | 701029 |
        | Isidora Multilingual     | 女  | 西班牙语(西班牙) | 701030 |
        | Tristan Multilingual     | 男  | 西班牙语(西班牙) | 701031 |
        | Ximena Multilingual      | 女  | 西班牙语(西班牙) | 701032 |
        | Remy Multilingual        | 男  | 法语(法国)       | 701033 |
        | Vivienne Multilingual    | 女  | 法语(法国)       | 701034 |
        | Lucien Multilingual      | 男  | 法语(法国)       | 701035 |
        | Alessio Multilingual     | 男  | 意大利语(意大利) | 701036 |
        | Giuseppe Multilingual    | 男  | 意大利语(意大利) | 701037 |
        | Isabella Multilingual    | 女  | 意大利语(意大利) | 701038 |
        | Marcello Multilingual    | 男  | 意大利语(意大利) | 701039 |
        | Masaru Multilingual      | 男  | 日语(日本)       | 701040 |
        | Hyunsu Multilingual      | 男  | 韩语(韩国)       | 701041 |
        | Macerio Multilingual     | 男  | 葡萄牙语(巴西)   | 701042 |
        | Thalita Multilingual     | 女  | 葡萄牙语(巴西)   | 701043 |
        | 晓辰 多语言              | 女  | 中文(普通话)     | 701044 |
        | 晓晓 多语言              | 女  | 中文(普通话)     | 701045 |
        | 晓宇 多语言              | 女  | 中文(普通话)     | 701046 |
        | 云逸 多语言              | 男 | 中文(普通话)     | 701047 |
        | Yunfan Multilingual      | 男  | 中文(普通话)     | 701048 |
        | Yunxiao Multilingual     | 男  | 中文(普通话)     | 701049 |
        | 晓晓 方言                | 女  | 中文(普通话)     | 701050 |

        :param request: Request instance for SubmitVideoTranslateJob.
        :type request: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vclm.v20240523.models.SubmitVideoTranslateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitVideoTranslateJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitVideoTranslateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))