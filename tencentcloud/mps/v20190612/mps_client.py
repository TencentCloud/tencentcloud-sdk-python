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
from tencentcloud.mps.v20190612 import models


class MpsClient(AbstractClient):
    _apiVersion = '2019-06-12'
    _endpoint = 'mps.tencentcloudapi.com'
    _service = 'mps'


    def CreateAIAnalysisTemplate(self, request):
        """创建用户自定义内容分析模板，数量上限：50。

        :param request: Request instance for CreateAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAIAnalysisTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAIAnalysisTemplateResponse()
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


    def CreateAIRecognitionTemplate(self, request):
        """创建用户自定义内容识别模板，数量上限：50。

        :param request: Request instance for CreateAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAIRecognitionTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAIRecognitionTemplateResponse()
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


    def CreateAdaptiveDynamicStreamingTemplate(self, request):
        """创建转自适应码流模板，数量上限：100。

        :param request: Request instance for CreateAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAdaptiveDynamicStreamingTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAdaptiveDynamicStreamingTemplateResponse()
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


    def CreateAnimatedGraphicsTemplate(self, request):
        """创建用户自定义转动图模板，数量上限：16。

        :param request: Request instance for CreateAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAnimatedGraphicsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAnimatedGraphicsTemplateResponse()
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


    def CreateContentReviewTemplate(self, request):
        """创建用户自定义内容智能识别模板，数量上限：50。

        :param request: Request instance for CreateContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateContentReviewTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateContentReviewTemplateResponse()
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


    def CreateImageSpriteTemplate(self, request):
        """创建用户自定义雪碧图模板，数量上限：16。

        :param request: Request instance for CreateImageSpriteTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateImageSpriteTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateImageSpriteTemplateResponse()
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


    def CreatePersonSample(self, request):
        """该接口用于创建素材样本，用于通过五官定位等技术，进行内容识别、内容不适宜等视频处理。

        :param request: Request instance for CreatePersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreatePersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreatePersonSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePersonSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePersonSampleResponse()
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


    def CreateSampleSnapshotTemplate(self, request):
        """创建用户自定义采样截图模板，数量上限：16。

        :param request: Request instance for CreateSampleSnapshotTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateSampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSampleSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSampleSnapshotTemplateResponse()
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


    def CreateSnapshotByTimeOffsetTemplate(self, request):
        """创建用户自定义指定时间点截图模板，数量上限：16。

        :param request: Request instance for CreateSnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateSnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSnapshotByTimeOffsetTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSnapshotByTimeOffsetTemplateResponse()
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


    def CreateTranscodeTemplate(self, request):
        """创建用户自定义转码模板，数量上限：1000。

        :param request: Request instance for CreateTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTranscodeTemplateResponse()
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


    def CreateWatermarkTemplate(self, request):
        """创建用户自定义水印模板，数量上限：1000。

        :param request: Request instance for CreateWatermarkTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWatermarkTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWatermarkTemplateResponse()
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


    def CreateWordSamples(self, request):
        """该接口用于批量创建关键词样本，样本用于通过OCR、ASR技术，进行不适宜内容识别、内容识别等视频处理。

        :param request: Request instance for CreateWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWordSamplesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWordSamples", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWordSamplesResponse()
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


    def CreateWorkflow(self, request):
        """对 COS 中指定 Bucket 的目录下上传的媒体文件，设置处理规则，包括：
        1. 视频转码（带水印）；
        2. 视频转动图；
        3. 对视频按指定时间点截图；
        4. 对视频采样截图；
        5. 对视频截图雪碧图；
        6. 对视频转自适应码流；
        7. 智能内容审核（鉴黄、鉴恐、鉴政）；
        8. 智能内容分析（标签、分类、封面、按帧标签）；
        9. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词）。

        注意：创建工作流成功后是禁用状态，需要手动启用。

        :param request: Request instance for CreateWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.CreateWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.CreateWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateWorkflowResponse()
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


    def DeleteAIAnalysisTemplate(self, request):
        """删除用户自定义内容分析模板。

        注意：模板 ID 为 10000 以下的为系统预置模板，不允许删除。

        :param request: Request instance for DeleteAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAIAnalysisTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAIAnalysisTemplateResponse()
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


    def DeleteAIRecognitionTemplate(self, request):
        """删除用户自定义内容识别模板。

        :param request: Request instance for DeleteAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAIRecognitionTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAIRecognitionTemplateResponse()
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


    def DeleteAdaptiveDynamicStreamingTemplate(self, request):
        """删除转自适应码流模板

        :param request: Request instance for DeleteAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAdaptiveDynamicStreamingTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAdaptiveDynamicStreamingTemplateResponse()
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


    def DeleteAnimatedGraphicsTemplate(self, request):
        """删除用户自定义转动图模板。

        :param request: Request instance for DeleteAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAnimatedGraphicsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAnimatedGraphicsTemplateResponse()
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


    def DeleteContentReviewTemplate(self, request):
        """删除用户自定义内容智能识别模板。

        :param request: Request instance for DeleteContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteContentReviewTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteContentReviewTemplateResponse()
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


    def DeleteImageSpriteTemplate(self, request):
        """删除雪碧图模板。

        :param request: Request instance for DeleteImageSpriteTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteImageSpriteTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteImageSpriteTemplateResponse()
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


    def DeletePersonSample(self, request):
        """该接口用于根据素材 ID，删除素材样本。

        :param request: Request instance for DeletePersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeletePersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeletePersonSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePersonSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePersonSampleResponse()
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


    def DeleteSampleSnapshotTemplate(self, request):
        """删除用户自定义采样截图模板。

        :param request: Request instance for DeleteSampleSnapshotTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteSampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteSampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSampleSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSampleSnapshotTemplateResponse()
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


    def DeleteSnapshotByTimeOffsetTemplate(self, request):
        """删除用户自定义指定时间点截图模板。

        :param request: Request instance for DeleteSnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteSnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteSnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSnapshotByTimeOffsetTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSnapshotByTimeOffsetTemplateResponse()
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


    def DeleteTranscodeTemplate(self, request):
        """删除用户自定义转码模板。

        :param request: Request instance for DeleteTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTranscodeTemplateResponse()
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


    def DeleteWatermarkTemplate(self, request):
        """删除用户自定义水印模板。

        :param request: Request instance for DeleteWatermarkTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWatermarkTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWatermarkTemplateResponse()
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


    def DeleteWordSamples(self, request):
        """该接口用于批量删除关键词样本。

        :param request: Request instance for DeleteWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWordSamplesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWordSamples", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWordSamplesResponse()
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


    def DeleteWorkflow(self, request):
        """删除工作流。对于已启用的工作流，需要禁用后才能删除。

        :param request: Request instance for DeleteWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.DeleteWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DeleteWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteWorkflowResponse()
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


    def DescribeAIAnalysisTemplates(self, request):
        """根据内容分析模板唯一标识，获取内容分析模板详情列表。返回结果包含符合条件的所有用户自定义内容分析模板及系统预置视频内容分析模板

        :param request: Request instance for DescribeAIAnalysisTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAIAnalysisTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAIAnalysisTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAIAnalysisTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAIAnalysisTemplatesResponse()
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


    def DescribeAIRecognitionTemplates(self, request):
        """根据内容识别模板唯一标识，获取内容识别模板详情列表。返回结果包含符合条件的所有用户自定义内容识别模板及系统预置视频内容识别模板

        :param request: Request instance for DescribeAIRecognitionTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAIRecognitionTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAIRecognitionTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAIRecognitionTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAIRecognitionTemplatesResponse()
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


    def DescribeAdaptiveDynamicStreamingTemplates(self, request):
        """查询转自适应码流模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeAdaptiveDynamicStreamingTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAdaptiveDynamicStreamingTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAdaptiveDynamicStreamingTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAdaptiveDynamicStreamingTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAdaptiveDynamicStreamingTemplatesResponse()
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


    def DescribeAnimatedGraphicsTemplates(self, request):
        """查询转动图模板列表，支持根据条件，分页查询。

        :param request: Request instance for DescribeAnimatedGraphicsTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeAnimatedGraphicsTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeAnimatedGraphicsTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAnimatedGraphicsTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAnimatedGraphicsTemplatesResponse()
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


    def DescribeContentReviewTemplates(self, request):
        """根据内容智能识别模板唯一标识，获取内容智能识别模板详情列表。返回结果包含符合条件的所有用户自定义模板及系统预置内容智能识别模板。

        :param request: Request instance for DescribeContentReviewTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeContentReviewTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeContentReviewTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeContentReviewTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeContentReviewTemplatesResponse()
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


    def DescribeImageSpriteTemplates(self, request):
        """查询雪碧图模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeImageSpriteTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeImageSpriteTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeImageSpriteTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeImageSpriteTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeImageSpriteTemplatesResponse()
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


    def DescribeMediaMetaData(self, request):
        """获取媒体的元信息，包括视频画面宽、高、编码格式、时长、帧率等。

        :param request: Request instance for DescribeMediaMetaData.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeMediaMetaDataRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeMediaMetaDataResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMediaMetaData", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMediaMetaDataResponse()
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


    def DescribePersonSamples(self, request):
        """该接口用于查询素材样本信息，支持根据素材 ID、名称、标签，分页查询。

        :param request: Request instance for DescribePersonSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribePersonSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribePersonSamplesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePersonSamples", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePersonSamplesResponse()
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


    def DescribeSampleSnapshotTemplates(self, request):
        """查询采样截图模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeSampleSnapshotTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeSampleSnapshotTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeSampleSnapshotTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSampleSnapshotTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSampleSnapshotTemplatesResponse()
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


    def DescribeSnapshotByTimeOffsetTemplates(self, request):
        """查询指定时间点截图模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeSnapshotByTimeOffsetTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeSnapshotByTimeOffsetTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeSnapshotByTimeOffsetTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSnapshotByTimeOffsetTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSnapshotByTimeOffsetTemplatesResponse()
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


    def DescribeTaskDetail(self, request):
        """通过任务 ID 查询任务的执行状态和结果的详细信息（最多可以查询3天之内提交的任务）。

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskDetailResponse()
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


    def DescribeTasks(self, request):
        """* 该接口用于查询任务列表；
        * 当列表数据比较多时，单次接口调用无法拉取整个列表，可通过 ScrollToken 参数，分批拉取；
        * 只能查询到最近三天（72 小时）内的任务。

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTasks", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTasksResponse()
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


    def DescribeTranscodeTemplates(self, request):
        """根据转码模板唯一标识，获取转码模板详情列表。返回结果包含符合条件的所有用户自定义模板及[系统预置转码模板](https://cloud.tencent.com/document/product/266/33476#.E9.A2.84.E7.BD.AE.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)。

        :param request: Request instance for DescribeTranscodeTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeTranscodeTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeTranscodeTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTranscodeTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTranscodeTemplatesResponse()
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


    def DescribeWatermarkTemplates(self, request):
        """查询用户自定义水印模板，支持根据条件，分页查询。

        :param request: Request instance for DescribeWatermarkTemplates.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWatermarkTemplatesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWatermarkTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWatermarkTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWatermarkTemplatesResponse()
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


    def DescribeWordSamples(self, request):
        """该接口用于根据应用场景、关键词、标签，分页查询关键词样本信息。

        :param request: Request instance for DescribeWordSamples.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWordSamplesRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWordSamplesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWordSamples", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWordSamplesResponse()
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


    def DescribeWorkflows(self, request):
        """根据工作流 ID，获取工作流详情列表。

        :param request: Request instance for DescribeWorkflows.
        :type request: :class:`tencentcloud.mps.v20190612.models.DescribeWorkflowsRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DescribeWorkflowsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeWorkflows", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeWorkflowsResponse()
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


    def DisableWorkflow(self, request):
        """禁用工作流。

        :param request: Request instance for DisableWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.DisableWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.DisableWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableWorkflowResponse()
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


    def EditMedia(self, request):
        """对视频进行编辑（剪辑、拼接等），生成一个新的点播视频。编辑的功能包括：

        1. 对一个文件进行剪辑，生成一个新的视频；
        2. 对多个文件进行拼接，生成一个新的视频；
        3. 对多个文件进行剪辑，然后再拼接，生成一个新的视频。

        :param request: Request instance for EditMedia.
        :type request: :class:`tencentcloud.mps.v20190612.models.EditMediaRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.EditMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EditMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EditMediaResponse()
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


    def EnableWorkflow(self, request):
        """启用工作流。

        :param request: Request instance for EnableWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.EnableWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.EnableWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableWorkflowResponse()
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


    def ExecuteFunction(self, request):
        """本接口仅用于定制开发的特殊场景，除非云视频处理客服人员主动告知您需要使用本接口，其它情况请勿调用。

        :param request: Request instance for ExecuteFunction.
        :type request: :class:`tencentcloud.mps.v20190612.models.ExecuteFunctionRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ExecuteFunctionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ExecuteFunction", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ExecuteFunctionResponse()
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


    def ManageTask(self, request):
        """对已发起的任务进行管理。

        :param request: Request instance for ManageTask.
        :type request: :class:`tencentcloud.mps.v20190612.models.ManageTaskRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ManageTaskResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ManageTask", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ManageTaskResponse()
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


    def ModifyAIAnalysisTemplate(self, request):
        """修改用户自定义内容分析模板。

        注意：模板 ID 10000 以下的为系统预置模板，不允许修改。

        :param request: Request instance for ModifyAIAnalysisTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAIAnalysisTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAIAnalysisTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAIAnalysisTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAIAnalysisTemplateResponse()
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


    def ModifyAIRecognitionTemplate(self, request):
        """修改用户自定义内容识别模板。

        :param request: Request instance for ModifyAIRecognitionTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAIRecognitionTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAIRecognitionTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAIRecognitionTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAIRecognitionTemplateResponse()
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


    def ModifyAdaptiveDynamicStreamingTemplate(self, request):
        """修改转自适应码流模板

        :param request: Request instance for ModifyAdaptiveDynamicStreamingTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAdaptiveDynamicStreamingTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAdaptiveDynamicStreamingTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAdaptiveDynamicStreamingTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAdaptiveDynamicStreamingTemplateResponse()
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


    def ModifyAnimatedGraphicsTemplate(self, request):
        """修改用户自定义转动图模板。

        :param request: Request instance for ModifyAnimatedGraphicsTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyAnimatedGraphicsTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyAnimatedGraphicsTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAnimatedGraphicsTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAnimatedGraphicsTemplateResponse()
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


    def ModifyContentReviewTemplate(self, request):
        """修改用户自定义内容智能识别模板。

        :param request: Request instance for ModifyContentReviewTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyContentReviewTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyContentReviewTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyContentReviewTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyContentReviewTemplateResponse()
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


    def ModifyImageSpriteTemplate(self, request):
        """修改用户自定义雪碧图模板。

        :param request: Request instance for ModifyImageSpriteTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyImageSpriteTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyImageSpriteTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyImageSpriteTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyImageSpriteTemplateResponse()
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


    def ModifyPersonSample(self, request):
        """该接口用于根据素材 ID，修改素材样本信息，包括名称、描述的修改，以及五官、标签的添加、删除、重置操作。五官删除操作需保证至少剩余 1 张图片，否则，请使用重置操作。

        :param request: Request instance for ModifyPersonSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyPersonSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyPersonSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPersonSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPersonSampleResponse()
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


    def ModifySampleSnapshotTemplate(self, request):
        """修改用户自定义采样截图模板。

        :param request: Request instance for ModifySampleSnapshotTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifySampleSnapshotTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifySampleSnapshotTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySampleSnapshotTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySampleSnapshotTemplateResponse()
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


    def ModifySnapshotByTimeOffsetTemplate(self, request):
        """修改用户自定义指定时间点截图模板。

        :param request: Request instance for ModifySnapshotByTimeOffsetTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifySnapshotByTimeOffsetTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifySnapshotByTimeOffsetTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySnapshotByTimeOffsetTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySnapshotByTimeOffsetTemplateResponse()
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


    def ModifyTranscodeTemplate(self, request):
        """修改用户自定义转码模板信息。

        :param request: Request instance for ModifyTranscodeTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyTranscodeTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyTranscodeTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTranscodeTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTranscodeTemplateResponse()
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


    def ModifyWatermarkTemplate(self, request):
        """修改用户自定义水印模板，水印类型不允许修改。

        :param request: Request instance for ModifyWatermarkTemplate.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyWatermarkTemplateRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyWatermarkTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWatermarkTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWatermarkTemplateResponse()
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


    def ModifyWordSample(self, request):
        """该接口用于修改关键词的应用场景、标签，关键词本身不可修改，如需修改，可删除重建。

        :param request: Request instance for ModifyWordSample.
        :type request: :class:`tencentcloud.mps.v20190612.models.ModifyWordSampleRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ModifyWordSampleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyWordSample", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyWordSampleResponse()
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


    def ParseLiveStreamProcessNotification(self, request):
        """从 CMQ 获取到消息后，从消息的 msgBody 字段中解析出 MPS 直播流处理事件通知的内容。
        该接口不用于发起网络调用，而是用来帮助生成各个语言平台的 SDK，您可以参考 SDK 的中解析函数的实现事件通知的解析。

        :param request: Request instance for ParseLiveStreamProcessNotification.
        :type request: :class:`tencentcloud.mps.v20190612.models.ParseLiveStreamProcessNotificationRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ParseLiveStreamProcessNotificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ParseLiveStreamProcessNotification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ParseLiveStreamProcessNotificationResponse()
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


    def ParseNotification(self, request):
        """从 CMQ 获取到消息后，从消息的 msgBody 字段中解析出 MPS 事件通知的内容。
        该接口不用于发起网络调用，而是用来帮助生成各个语言平台的 SDK，您可以参考 SDK 的中解析函数的实现事件通知的解析。

        :param request: Request instance for ParseNotification.
        :type request: :class:`tencentcloud.mps.v20190612.models.ParseNotificationRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ParseNotificationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ParseNotification", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ParseNotificationResponse()
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


    def ProcessLiveStream(self, request):
        """对直播流媒体发起处理任务，功能包括：

        * 智能内容审核（画面鉴黄、鉴政、鉴暴、声音鉴黄）；
        * 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词）。

        直播流处理事件通知实时写入用户指定的消息队列 CMQ 中，用户需要从消息队列 CMQ 中获取事件通知结果，同时处理过程中存在输出文件的，会写入用户指定的输出文件的目标存储中。

        :param request: Request instance for ProcessLiveStream.
        :type request: :class:`tencentcloud.mps.v20190612.models.ProcessLiveStreamRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ProcessLiveStreamResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ProcessLiveStream", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ProcessLiveStreamResponse()
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


    def ProcessMedia(self, request):
        """对 COS 中的媒体文件发起处理任务，功能包括：
        1. 视频转码（带水印）；
        2. 视频转动图；
        3. 对视频按指定时间点截图；
        4. 对视频采样截图；
        5. 对视频截图雪碧图；
        6. 对视频转自适应码流；
        7. 智能内容审核（鉴黄、鉴恐、鉴政）；
        8. 智能内容分析（标签、分类、封面、按帧标签）；
        9. 智能内容识别（人脸、文本全文、文本关键词、语音全文、语音关键词）。

        :param request: Request instance for ProcessMedia.
        :type request: :class:`tencentcloud.mps.v20190612.models.ProcessMediaRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ProcessMediaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ProcessMedia", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ProcessMediaResponse()
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


    def RecognizeMediaForZhiXue(self, request):
        """智能媒体识别，包含表情和动作识别。仅用于智学，其他调用无效。

        :param request: Request instance for RecognizeMediaForZhiXue.
        :type request: :class:`tencentcloud.mps.v20190612.models.RecognizeMediaForZhiXueRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.RecognizeMediaForZhiXueResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecognizeMediaForZhiXue", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecognizeMediaForZhiXueResponse()
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


    def ResetWorkflow(self, request):
        """重新设置一个已经存在且处于禁用状态的工作流。

        :param request: Request instance for ResetWorkflow.
        :type request: :class:`tencentcloud.mps.v20190612.models.ResetWorkflowRequest`
        :rtype: :class:`tencentcloud.mps.v20190612.models.ResetWorkflowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetWorkflow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetWorkflowResponse()
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