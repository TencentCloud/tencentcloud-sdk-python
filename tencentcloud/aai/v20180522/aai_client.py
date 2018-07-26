# -*- coding: utf8 -*-
# Copyright 1999-2017 Tencent Ltd.
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


    def SentenceRecognition(self, request):
        """识别60s内的短语音，当音频放在请求body中传输时整个请求大小不能超过1M，当音频以url方式传输时，音频时长不可超过60s。所有请求参数放在post的body中采用x-www-form-urlencoded（数据转换成一个字串（name1=value1&name2=value2…）进行urlencode后传输）编码传输。

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
                raise e
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
                raise e
            else:
                raise TencentCloudSDKException(e.message, e.message)