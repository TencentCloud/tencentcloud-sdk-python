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
from tencentcloud.tsi.v20210325 import models


class TsiClient(AbstractClient):
    _apiVersion = '2021-03-25'
    _endpoint = 'tsi.tencentcloudapi.com'
    _service = 'tsi'


    def TongChuanDisplay(self, request):
        """获取同传结果。

        :param request: Request instance for TongChuanDisplay.
        :type request: :class:`tencentcloud.tsi.v20210325.models.TongChuanDisplayRequest`
        :rtype: :class:`tencentcloud.tsi.v20210325.models.TongChuanDisplayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TongChuanDisplay", params, headers=headers)
            response = json.loads(body)
            model = models.TongChuanDisplayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TongChuanRecognize(self, request):
        """本接口提供上传音频，将音频进行语音识别并翻译成文本的服务。
        该接口需要配合[同传查询结果](https://cloud.tencent.com/document/product/1399/107636)接口使用，建议一个线程进行音频数据上传同时另外一个线程拉取同传结果。
        如果需要同步接口，既上传音频的同时拉取同传结果，可以使用[同传上传音频并查询结果](https://cloud.tencent.com/document/product/1399/107634)接口。

        -----------
        ### 接口要求
        集成该API时，需按照以下要求：

        | 内容| 格式 |
        | -------- | ------- |
        | 音频格式  | pcm    |
        | 音频属性 | <ul><li>采样率：16000Hz</li><li>采样精度：16bits</li><li>声道：单声道（mono）</li></ul> |
        | 响应格式    | 统一采用 JSON 格式   |
        | 数据发送    | 建议每200ms 发送200ms 时长的数据包，即1:1实时率，对应大小为6400字节。<br/><ol><li>音频发送速率过快超过1:1实时率或者音频数据包之间发送间隔超过6秒，可能导致引擎出错，后台将返回错误；</li><li>每次发送数据的大小不得小于 200ms时长 的数据包，且不得大于 500ms时长 的数据包；小于 200ms时长 的数据包会被丢弃，大于 500ms时长 的数据包会影响引擎的数据处理；</li><li>若最后一个音频数据包不足 200ms，需要使用空数据进行补齐；</li></ol> |

        :param request: Request instance for TongChuanRecognize.
        :type request: :class:`tencentcloud.tsi.v20210325.models.TongChuanRecognizeRequest`
        :rtype: :class:`tencentcloud.tsi.v20210325.models.TongChuanRecognizeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TongChuanRecognize", params, headers=headers)
            response = json.loads(body)
            model = models.TongChuanRecognizeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TongChuanSync(self, request):
        """本接口提供上传音频，将音频进行语音识别并翻译成文本的服务，目前开放中英互译的同传服务。 待识别和翻译的音频文件格式是 pcm，pcm采样率要求16kHz、位深16bit、单声道、每个分片时长200ms~500ms，音频内语音清晰。

        :param request: Request instance for TongChuanSync.
        :type request: :class:`tencentcloud.tsi.v20210325.models.TongChuanSyncRequest`
        :rtype: :class:`tencentcloud.tsi.v20210325.models.TongChuanSyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TongChuanSync", params, headers=headers)
            response = json.loads(body)
            model = models.TongChuanSyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))