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
from tencentcloud.asr.v20190614 import models


class AsrClient(AbstractClient):
    _apiVersion = '2019-06-14'
    _endpoint = 'asr.tencentcloudapi.com'
    _service = 'asr'


    def CloseAsyncRecognitionTask(self, request):
        """本接口用于关闭语音流异步识别任务。

        :param request: Request instance for CloseAsyncRecognitionTask.
        :type request: :class:`tencentcloud.asr.v20190614.models.CloseAsyncRecognitionTaskRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.CloseAsyncRecognitionTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseAsyncRecognitionTask", params, headers=headers)
            response = json.loads(body)
            model = models.CloseAsyncRecognitionTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAsrKeyWordLib(self, request):
        """用户通过本接口进行关键字词表的创建。
        <br>•   默认每个用户最多可创建30个关键字词表。
        <br>•   每个关键词词表最多可添加100个词，每个词最多5个汉字或15个字符。
        <br>•   词表通过本地文件形式上传。
        <br>•   本地文件必须为UTF-8编码格式，每行仅添加一个词且不能包含标点和特殊字符。

        :param request: Request instance for CreateAsrKeyWordLib.
        :type request: :class:`tencentcloud.asr.v20190614.models.CreateAsrKeyWordLibRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.CreateAsrKeyWordLibResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAsrKeyWordLib", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAsrKeyWordLibResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAsrVocab(self, request):
        """用户通过本接口进行热词表的创建。
        <br>•   默认最多可创建30个热词表。
        <br>•   每个热词表最多可添加1000个词，每个词最长10个汉字或30个英文字符，不能超出限制。
        <br>•   热词表可以通过数组或者本地文件形式上传。
        <br>•   本地文件必须为UTF-8编码格式，每行仅添加一个热词且不能包含标点和特殊字符。
        <br>•   热词权重取值范围为[1,11]之间的整数或者100，权重越大代表该词被识别出来的概率越大。
        <br>• 注意:  热词权重设置为11时，当前热词将升级为超级热词，建议仅将重要且必须生效的热词设置到11，设置过多权重为11的热词将影响整体字准率。

        :param request: Request instance for CreateAsrVocab.
        :type request: :class:`tencentcloud.asr.v20190614.models.CreateAsrVocabRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.CreateAsrVocabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAsrVocab", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAsrVocabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAsyncRecognitionTask(self, request):
        """本接口用于对语音流进行准实时识别，通过异步回调来返回识别结果。适用于直播审核等场景。
        <br>• 支持rtmp、rtsp等流媒体协议，以及各类基于http协议的直播流(不支持hls)
        <br>• 音频流时长无限制，服务会自动拉取音频流数据，若连续10分钟拉不到流数据时，服务会终止识别任务
        <br>• 服务通过回调的方式来提供识别结果，用户需要提供CallbackUrl。回调时机为一小段话(最长15秒)回调一次。
        <br>• 签名方法参考 [公共参数](https://cloud.tencent.com/document/api/1093/35640) 中签名方法v3。
        <br>• 默认单账号限制并发数为20路，如您有提高并发限制的需求，请提[工单](https://console.cloud.tencent.com/workorder/category)进行咨询。

        :param request: Request instance for CreateAsyncRecognitionTask.
        :type request: :class:`tencentcloud.asr.v20190614.models.CreateAsyncRecognitionTaskRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.CreateAsyncRecognitionTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAsyncRecognitionTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAsyncRecognitionTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomization(self, request):
        """用户使用该接口可以创建自学习模型，以供识别调用。

        注意：调用该接口后，模型会自动训练。新建模型成功后，调用ModifyCustomizationState接口修改为上线状态，即可在识别请求中使用对应模型ID。

        :param request: Request instance for CreateCustomization.
        :type request: :class:`tencentcloud.asr.v20190614.models.CreateCustomizationRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.CreateCustomizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomization", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRecTask(self, request):
        """本接口可对较长的录音文件进行识别。如希望直接使用带界面的语音识别产品，请访问[产品体验中心](https://console.cloud.tencent.com/asr/demonstrate)。产品计费标准请查阅 [计费概述（在线版）](https://cloud.tencent.com/document/product/1093/35686)
        • 接口默认限频：20次/秒。此处仅限制任务提交频次，与识别结果返回时效无关
        • 返回时效：异步回调，非实时返回。最长3小时返回识别结果，**大多数情况下，1小时的音频1-3分钟即可完成识别**。请注意：上述返回时长不含音频下载时延，且30分钟内发送超过1000小时录音或2万条任务的情况除外
        • 音频格式：wav、mp3、m4a、flv、mp4、wma、3gp、amr、aac、ogg-opus、flac
        • 支持语言：在本页面上搜索 **EngineModelType**，或前往 [产品功能](https://cloud.tencent.com/document/product/1093/35682) 查看
        • 音频提交方式：本接口支持**音频 URL 、本地音频文件**两种请求方式。推荐使用 [腾讯云COS](https://cloud.tencent.com/document/product/436/38484) 来存储、生成URL并提交任务，此种方式将不产生外网和流量下行费用，可节约成本、提升任务速度（可参考COS预签名指南：[使用预签名 URL 访问 COS](https://cloud.tencent.com/document/product/436/68284) ，获取COS预签名url）
        • 音频限制：音频 URL 时长不能大于5小时，文件大小不超过1GB；本地音频文件不能大于5MB
        • 如何获取识别结果：支持**回调或轮询**的方式获取结果，具体请参考 [录音文件识别结果查询](https://cloud.tencent.com/document/product/1093/37822)
        • 识别结果有效时间：识别结果在服务端保存24小时
        • 签名方法参考 [公共参数](https://cloud.tencent.com/document/api/1093/35640) 中签名方法 v3

        :param request: Request instance for CreateRecTask.
        :type request: :class:`tencentcloud.asr.v20190614.models.CreateRecTaskRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.CreateRecTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRecTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRecTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAsrKeyWordLib(self, request):
        """用户通过本接口进行关键词表的删除。

        :param request: Request instance for DeleteAsrKeyWordLib.
        :type request: :class:`tencentcloud.asr.v20190614.models.DeleteAsrKeyWordLibRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.DeleteAsrKeyWordLibResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAsrKeyWordLib", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAsrKeyWordLibResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAsrVocab(self, request):
        """用户通过本接口进行热词表的删除。

        :param request: Request instance for DeleteAsrVocab.
        :type request: :class:`tencentcloud.asr.v20190614.models.DeleteAsrVocabRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.DeleteAsrVocabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAsrVocab", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAsrVocabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomization(self, request):
        """用户通过该接口可以删除自学习模型

        :param request: Request instance for DeleteCustomization.
        :type request: :class:`tencentcloud.asr.v20190614.models.DeleteCustomizationRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.DeleteCustomizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomization", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAsyncRecognitionTasks(self, request):
        """本接口用于查询当前在运行的语音流异步识别任务列表。
        <br>•   签名方法参考 [公共参数](https://cloud.tencent.com/document/api/1093/35640) 中签名方法v3。

        :param request: Request instance for DescribeAsyncRecognitionTasks.
        :type request: :class:`tencentcloud.asr.v20190614.models.DescribeAsyncRecognitionTasksRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.DescribeAsyncRecognitionTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAsyncRecognitionTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAsyncRecognitionTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskStatus(self, request):
        """调用录音文件识别请求接口后，有回调和轮询两种方式获取识别结果。
        • **注意任务有效期为24小时，超过24小时的任务请不要再查询，且不要依赖TaskId作为业务唯一ID，不同日期可能出现重复TaskId。**
        • 当采用回调方式时，识别完成后会将结果通过 POST 请求的形式通知到用户在请求时填写的回调 URL，具体请参见[ 录音识别结果回调 ](https://cloud.tencent.com/document/product/1093/52632)。
        • 当采用轮询方式时，需要主动提交任务ID来轮询识别结果，共有任务成功、等待、执行中和失败四种结果，具体信息请参见下文说明。
        •   请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        •   签名方法参考 [公共参数](https://cloud.tencent.com/document/api/1093/35640) 中签名方法v3。
        •   默认接口请求频率限制：50次/秒，如您有提高请求频率限制的需求，请提[工单](https://console.cloud.tencent.com/workorder/category)进行咨询。

        :param request: Request instance for DescribeTaskStatus.
        :type request: :class:`tencentcloud.asr.v20190614.models.DescribeTaskStatusRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.DescribeTaskStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadAsrVocab(self, request):
        """用户通过本接口进行热词表的下载，获得词表权重文件形式的 base64 值，文件形式为通过 “|” 分割的词和权重，即 word|weight 的形式。

        :param request: Request instance for DownloadAsrVocab.
        :type request: :class:`tencentcloud.asr.v20190614.models.DownloadAsrVocabRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.DownloadAsrVocabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadAsrVocab", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadAsrVocabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadCustomization(self, request):
        """用户通过该接口可以下载自学习模型的语料

        :param request: Request instance for DownloadCustomization.
        :type request: :class:`tencentcloud.asr.v20190614.models.DownloadCustomizationRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.DownloadCustomizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadCustomization", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadCustomizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAsrKeyWordLibList(self, request):
        """用户通过该接口，可获得所有的关键词表及其信息。

        :param request: Request instance for GetAsrKeyWordLibList.
        :type request: :class:`tencentcloud.asr.v20190614.models.GetAsrKeyWordLibListRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.GetAsrKeyWordLibListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAsrKeyWordLibList", params, headers=headers)
            response = json.loads(body)
            model = models.GetAsrKeyWordLibListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAsrVocab(self, request):
        """用户根据词表的ID可以获取对应的热词表信息

        :param request: Request instance for GetAsrVocab.
        :type request: :class:`tencentcloud.asr.v20190614.models.GetAsrVocabRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.GetAsrVocabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAsrVocab", params, headers=headers)
            response = json.loads(body)
            model = models.GetAsrVocabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetAsrVocabList(self, request):
        """用户通过该接口，可获得所有的热词表及其信息。

        :param request: Request instance for GetAsrVocabList.
        :type request: :class:`tencentcloud.asr.v20190614.models.GetAsrVocabListRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.GetAsrVocabListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetAsrVocabList", params, headers=headers)
            response = json.loads(body)
            model = models.GetAsrVocabListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCustomizationList(self, request):
        """查询自学习模型列表

        :param request: Request instance for GetCustomizationList.
        :type request: :class:`tencentcloud.asr.v20190614.models.GetCustomizationListRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.GetCustomizationListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCustomizationList", params, headers=headers)
            response = json.loads(body)
            model = models.GetCustomizationListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetModelInfo(self, request):
        """通过自学习模型id获取自学习模型详细信息

        :param request: Request instance for GetModelInfo.
        :type request: :class:`tencentcloud.asr.v20190614.models.GetModelInfoRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.GetModelInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetModelInfo", params, headers=headers)
            response = json.loads(body)
            model = models.GetModelInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetUsageByDate(self, request):
        """查询用户用量

        :param request: Request instance for GetUsageByDate.
        :type request: :class:`tencentcloud.asr.v20190614.models.GetUsageByDateRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.GetUsageByDateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetUsageByDate", params, headers=headers)
            response = json.loads(body)
            model = models.GetUsageByDateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomization(self, request):
        """用户通过该接口可以更新自学习模型，如模型名称、模型类型、模型语料。

        :param request: Request instance for ModifyCustomization.
        :type request: :class:`tencentcloud.asr.v20190614.models.ModifyCustomizationRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.ModifyCustomizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomization", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomizationState(self, request):
        """通过该接口，用户可以修改自学习模型状态，上下线自学习模型

        :param request: Request instance for ModifyCustomizationState.
        :type request: :class:`tencentcloud.asr.v20190614.models.ModifyCustomizationStateRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.ModifyCustomizationStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomizationState", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomizationStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SentenceRecognition(self, request):
        """本接口用于对60秒之内的短音频文件进行识别。
        •   支持中文普通话、英语、粤语、日语、越南语、马来语、印度尼西亚语、菲律宾语、泰语、葡萄牙语、土耳其语、阿拉伯语、印地语、法语、德语、上海话、四川话、武汉话、贵阳话、昆明话、西安话、郑州话、太原话、兰州话、银川话、西宁话、南京话、合肥话、南昌话、长沙话、苏州话、杭州话、济南话、天津话、石家庄话、黑龙江话、吉林话、辽宁话。
        •   支持本地语音文件上传和语音URL上传两种请求方式，音频时长不能超过60s，音频文件大小不能超过3MB。推荐使用 [腾讯云COS](https://cloud.tencent.com/document/product/436/38484) 来存储音频、生成URL并提交请求，此种方式会走内网下载音频，极大降低整体请求时延；并且不会产生外网和流量下行费用，可节约成本（可参考COS预签名指南：[使用预签名 URL 访问 COS](https://cloud.tencent.com/document/product/436/68284) ，获取COS预签名url）
        •   音频格式支持wav、pcm、ogg-opus、speex、silk、mp3、m4a、aac、 amr。
        •   请求方法为 HTTP POST , Content-Type为"application/json; charset=utf-8"
        •   签名方法参考 [公共参数](https://cloud.tencent.com/document/api/1093/35640) 中签名方法v3。
        •   默认接口请求频率限制：30次/秒，如您有提高请求频率限制的需求，请[前往购买](https://buy.cloud.tencent.com/asr)。

        :param request: Request instance for SentenceRecognition.
        :type request: :class:`tencentcloud.asr.v20190614.models.SentenceRecognitionRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.SentenceRecognitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SentenceRecognition", params, headers=headers)
            response = json.loads(body)
            model = models.SentenceRecognitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVocabState(self, request):
        """用户通过该接口可以设置热词表的默认状态。初始状态为0，用户可设置状态为1，即为默认状态。默认状态表示用户在请求识别时，如不设置热词表ID，则默认使用状态为1的热词表。

        :param request: Request instance for SetVocabState.
        :type request: :class:`tencentcloud.asr.v20190614.models.SetVocabStateRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.SetVocabStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVocabState", params, headers=headers)
            response = json.loads(body)
            model = models.SetVocabStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAsrKeyWordLib(self, request):
        """用户通过本接口进行对应的关键词表信息更新。

        :param request: Request instance for UpdateAsrKeyWordLib.
        :type request: :class:`tencentcloud.asr.v20190614.models.UpdateAsrKeyWordLibRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.UpdateAsrKeyWordLibResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAsrKeyWordLib", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAsrKeyWordLibResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateAsrVocab(self, request):
        """用户通过本接口进行对应的词表信息更新。

        :param request: Request instance for UpdateAsrVocab.
        :type request: :class:`tencentcloud.asr.v20190614.models.UpdateAsrVocabRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.UpdateAsrVocabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateAsrVocab", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateAsrVocabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VoicePrintCompare(self, request):
        """通过比对两段音频内说话人的声纹，得到一个打分，可通过打分判断两段音频声纹相似度,  打分区间[0 - 100]。 音频要求：16k采样率， 16bit位深，pcm或者wav格式， 单声道，总时长不超过30秒的音频，base64编码数据大小不超过2M，音频内容只有一个说话人声音，并且尽可能清晰，这样结果更加准确。

        :param request: Request instance for VoicePrintCompare.
        :type request: :class:`tencentcloud.asr.v20190614.models.VoicePrintCompareRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintCompareResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VoicePrintCompare", params, headers=headers)
            response = json.loads(body)
            model = models.VoicePrintCompareResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VoicePrintCount(self, request):
        """统计并返回注册的说话人id总数

        :param request: Request instance for VoicePrintCount.
        :type request: :class:`tencentcloud.asr.v20190614.models.VoicePrintCountRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VoicePrintCount", params, headers=headers)
            response = json.loads(body)
            model = models.VoicePrintCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VoicePrintDelete(self, request):
        """本接口用于以删除已经注册的说话人信息（删除之后，原有的说话人ID和说话人音频数据都会失效）

        :param request: Request instance for VoicePrintDelete.
        :type request: :class:`tencentcloud.asr.v20190614.models.VoicePrintDeleteRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintDeleteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VoicePrintDelete", params, headers=headers)
            response = json.loads(body)
            model = models.VoicePrintDeleteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VoicePrintEnroll(self, request):
        """说话人注册接口用于注册一个指定音频，生成一个唯一的说话人id，后续可通过说话人验证接口验证其它音频和已有的说话人ID匹配度，注册时可指定说话人昵称，方便标识说话人ID，  说话人昵称可重复配置。
        （注: 一个appid最多可以注册1000个说话人ID，一个说话人ID仅支持一条音频注册，后续可通过更新接口进行更新）

        使用须知
        支持的输入格式：编码文件(PCM, WAV)、16 bit采样位数、单声道（mono）。

        支持的音频采样率：16000 Hz。

        :param request: Request instance for VoicePrintEnroll.
        :type request: :class:`tencentcloud.asr.v20190614.models.VoicePrintEnrollRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintEnrollResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VoicePrintEnroll", params, headers=headers)
            response = json.loads(body)
            model = models.VoicePrintEnrollResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VoicePrintGroupVerify(self, request):
        """说话人验证1:N接口，可以通过传入一段说话人音频，并且指定已存在的groupId, 和返回topN,  接口返回groupId内所有声纹和传入音频声纹比对打分TopN的结果。

        :param request: Request instance for VoicePrintGroupVerify.
        :type request: :class:`tencentcloud.asr.v20190614.models.VoicePrintGroupVerifyRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintGroupVerifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VoicePrintGroupVerify", params, headers=headers)
            response = json.loads(body)
            model = models.VoicePrintGroupVerifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VoicePrintUpdate(self, request):
        """本接口用于更新和覆盖已注册的音频数据和说话人昵称，更新后原有的音频数据将失效。

        :param request: Request instance for VoicePrintUpdate.
        :type request: :class:`tencentcloud.asr.v20190614.models.VoicePrintUpdateRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintUpdateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VoicePrintUpdate", params, headers=headers)
            response = json.loads(body)
            model = models.VoicePrintUpdateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VoicePrintVerify(self, request):
        """本接口用于校验传入音频与已注册音频的匹配程度，通过指定说话人ID（VoicePrintId）和一段音频进行音频和说话人的匹配度判断

        :param request: Request instance for VoicePrintVerify.
        :type request: :class:`tencentcloud.asr.v20190614.models.VoicePrintVerifyRequest`
        :rtype: :class:`tencentcloud.asr.v20190614.models.VoicePrintVerifyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VoicePrintVerify", params, headers=headers)
            response = json.loads(body)
            model = models.VoicePrintVerifyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))