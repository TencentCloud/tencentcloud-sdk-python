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
from tencentcloud.aai.v20180522 import models


class AaiClient(AbstractClient):
    _apiVersion = '2018-05-22'
    _endpoint = 'aai.tencentcloudapi.com'


    def Chat(self, request):
        """提供基于文本的基础聊天能力，可以让您的应用快速拥有具备深度语义理解的机器聊天功能。

        :param request: 调用Chat所需参数的结构体。
        :type request: :class:`tencentcloud.aai.v20180522.models.ChatRequest`
        :rtype: :class:`tencentcloud.aai.v20180522.models.ChatResponse`

        """
        try:
            params = request._serialize()
            body = self.call("Chat", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ChatResponse()
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


    def SentenceRecognition(self, request):
        """识别60s内的短语音，当音频放在请求body中传输时整个请求大小不能超过600KB，当音频以url方式传输时，音频时长不可超过60s。所有请求参数放在post的body中采用x-www-form-urlencoded（数据转换成一个字符串（name1=value1&name2=value2…）进行urlencode后）编码传输。现暂只支持中文普通话识别，支持识别8k(16k)的16bit的mp3或者wav音频。

        :param request: 调用SentenceRecognition所需参数的结构体。
        :type request: :class:`tencentcloud.aai.v20180522.models.SentenceRecognitionRequest`
        :rtype: :class:`tencentcloud.aai.v20180522.models.SentenceRecognitionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SentenceRecognition", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SentenceRecognitionResponse()
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


    def SimultaneousInterpreting(self, request):
        """该接口是实时流式识别，可同时返回语音识别文本及翻译文本，当前仅支持中文和英文。该接口可配合同传windows客户端，提供会议现场同传服务。

        :param request: 调用SimultaneousInterpreting所需参数的结构体。
        :type request: :class:`tencentcloud.aai.v20180522.models.SimultaneousInterpretingRequest`
        :rtype: :class:`tencentcloud.aai.v20180522.models.SimultaneousInterpretingResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SimultaneousInterpreting", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SimultaneousInterpretingResponse()
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


    def TextToVoice(self, request):
        """腾讯云语音合成技术（TTS）可以将任意文本转化为语音，实现让机器和应用张口说话。
        腾讯TTS技术可以应用到很多场景，比如，移动APP语音播报新闻；智能设备语音提醒；依靠网上现有节目或少量录音，快速合成明星语音，降低邀约成本；支持车载导航语音合成的个性化语音播报。
        内测期间免费使用。

        :param request: 调用TextToVoice所需参数的结构体。
        :type request: :class:`tencentcloud.aai.v20180522.models.TextToVoiceRequest`
        :rtype: :class:`tencentcloud.aai.v20180522.models.TextToVoiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextToVoice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextToVoiceResponse()
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