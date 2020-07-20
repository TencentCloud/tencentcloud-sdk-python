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
from tencentcloud.tts.v20190823 import models


class TtsClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tts.tencentcloudapi.com'


    def TextToVoice(self, request):
        """腾讯云语音合成技术（TTS）可以将任意文本转化为语音，实现让机器和应用张口说话。
        腾讯TTS技术可以应用到很多场景，比如，移动APP语音播报新闻；智能设备语音提醒；依靠网上现有节目或少量录音，快速合成明星语音，降低邀约成本；支持车载导航语音合成的个性化语音播报。
        内测期间免费使用。

        :param request: Request instance for TextToVoice.
        :type request: :class:`tencentcloud.tts.v20190823.models.TextToVoiceRequest`
        :rtype: :class:`tencentcloud.tts.v20190823.models.TextToVoiceResponse`

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