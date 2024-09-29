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
from tencentcloud.vtc.v20240223 import models


class VtcClient(AbstractClient):
    _apiVersion = '2024-02-23'
    _endpoint = 'vtc.tencentcloudapi.com'
    _service = 'vtc'


    def ConfirmVideoTranslateJob(self, request):
        """确认视频翻译结果

        :param request: Request instance for ConfirmVideoTranslateJob.
        :type request: :class:`tencentcloud.vtc.v20240223.models.ConfirmVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vtc.v20240223.models.ConfirmVideoTranslateJobResponse`

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


    def DescribeVideoTranslateJob(self, request):
        """查询视频翻译任务

        :param request: Request instance for DescribeVideoTranslateJob.
        :type request: :class:`tencentcloud.vtc.v20240223.models.DescribeVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vtc.v20240223.models.DescribeVideoTranslateJobResponse`

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
        :type request: :class:`tencentcloud.vtc.v20240223.models.SubmitVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vtc.v20240223.models.SubmitVideoTranslateJobResponse`

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