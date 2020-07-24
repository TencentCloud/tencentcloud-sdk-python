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
from tencentcloud.tmt.v20180321 import models


class TmtClient(AbstractClient):
    _apiVersion = '2018-03-21'
    _endpoint = 'tmt.tencentcloudapi.com'


    def ImageTranslate(self, request):
        """提供13种语言的图片翻译服务，可自动识别图片中的文本内容并翻译成目标语言，识别后的文本按行翻译，后续会提供可按段落翻译的版本。<br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。

        :param request: Request instance for ImageTranslate.
        :type request: :class:`tencentcloud.tmt.v20180321.models.ImageTranslateRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.ImageTranslateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ImageTranslate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ImageTranslateResponse()
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


    def LanguageDetect(self, request):
        """可自动识别文本内容的语言种类，轻量高效，无需额外实现判断方式，使面向客户的服务体验更佳。 <br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。

        :param request: Request instance for LanguageDetect.
        :type request: :class:`tencentcloud.tmt.v20180321.models.LanguageDetectRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.LanguageDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("LanguageDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.LanguageDetectResponse()
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


    def SpeechTranslate(self, request):
        """本接口提供上传音频，将音频进行语音识别并翻译成文本的服务，目前开放中英互译的语音翻译服务。
        待识别和翻译的音频文件可以是 pcm、mp3和speex 格式，pcm采样率要求16kHz、位深16bit、单声道，音频内语音清晰。<br/>
        如果采用流式传输的方式，要求每个分片时长200ms~500ms；如果采用非流式的传输方式，要求音频时长不超过8s。注意最后一个分片的IsEnd参数设置为1。<br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源部分。

        :param request: Request instance for SpeechTranslate.
        :type request: :class:`tencentcloud.tmt.v20180321.models.SpeechTranslateRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.SpeechTranslateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SpeechTranslate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SpeechTranslateResponse()
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


    def TextTranslate(self, request):
        """提供中文到英文、英文到中文的等多种语言的文本内容翻译服务， 经过大数据语料库、多种解码算法、翻译引擎深度优化，在新闻文章、生活口语等不同语言场景中都有深厚积累，翻译结果专业评价处于行业领先水平。<br />
        提示：对于一般开发者，我们建议优先使用SDK接入简化开发。SDK使用介绍请直接查看 5. 开发者资源 部分。

        :param request: Request instance for TextTranslate.
        :type request: :class:`tencentcloud.tmt.v20180321.models.TextTranslateRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.TextTranslateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextTranslate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextTranslateResponse()
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


    def TextTranslateBatch(self, request):
        """文本翻译的批量接口

        :param request: Request instance for TextTranslateBatch.
        :type request: :class:`tencentcloud.tmt.v20180321.models.TextTranslateBatchRequest`
        :rtype: :class:`tencentcloud.tmt.v20180321.models.TextTranslateBatchResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TextTranslateBatch", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TextTranslateBatchResponse()
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