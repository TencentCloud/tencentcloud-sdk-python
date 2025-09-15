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
from tencentcloud.mrs.v20200910 import models


class MrsClient(AbstractClient):
    _apiVersion = '2020-09-10'
    _endpoint = 'mrs.tencentcloudapi.com'
    _service = 'mrs'


    def DrugInstructionObject(self, request):
        r"""药品说明书PDF文件结构化

        :param request: Request instance for DrugInstructionObject.
        :type request: :class:`tencentcloud.mrs.v20200910.models.DrugInstructionObjectRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.DrugInstructionObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DrugInstructionObject", params, headers=headers)
            response = json.loads(body)
            model = models.DrugInstructionObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageMask(self, request):
        r"""医疗报告图片脱敏接口

        :param request: Request instance for ImageMask.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageMaskRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageMaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageMask", params, headers=headers)
            response = json.loads(body)
            model = models.ImageMaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageMaskAsync(self, request):
        r"""图片脱敏-异步接口
        短时间大批量调用（例如>100上传/10分钟），如果遇到错误码“FalledOperation.AsyncQueueFullError”，请于数分钟后再次尝试提交。

        :param request: Request instance for ImageMaskAsync.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageMaskAsyncRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageMaskAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageMaskAsync", params, headers=headers)
            response = json.loads(body)
            model = models.ImageMaskAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageMaskAsyncGetResult(self, request):
        r"""图片脱敏-异步获取结果接口
        请于上传请求后24小时内获取结果。

        :param request: Request instance for ImageMaskAsyncGetResult.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageMaskAsyncGetResultRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageMaskAsyncGetResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageMaskAsyncGetResult", params, headers=headers)
            response = json.loads(body)
            model = models.ImageMaskAsyncGetResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageToClass(self, request):
        r"""图片分类

        :param request: Request instance for ImageToClass.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageToClassRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageToClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageToClass", params, headers=headers)
            response = json.loads(body)
            model = models.ImageToClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageToObject(self, request):
        r"""图片转结构化对象

        :param request: Request instance for ImageToObject.
        :type request: :class:`tencentcloud.mrs.v20200910.models.ImageToObjectRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.ImageToObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageToObject", params, headers=headers)
            response = json.loads(body)
            model = models.ImageToObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextToClass(self, request):
        r"""文本分类

        适用场景：经过腾讯医疗专用 OCR 从图片识别之后的文本，并且需要加上每个字符的坐标信息，才可以调用此接口。通过其它 OCR 识别的文本可能不适配。医院的 XML 格式文本也不适配，XML 文件需要经过特殊转换才能直接调用此接口。单次调用传入的文本不宜超过 2000 字。如有需要调用此接口，建议先咨询产品团队。

        :param request: Request instance for TextToClass.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TextToClassRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TextToClassResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToClass", params, headers=headers)
            response = json.loads(body)
            model = models.TextToClassResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextToObject(self, request):
        r"""文本转结构化对象。

        适用场景：经过腾讯医疗专用 OCR 从图片识别之后的文本，可以调用此接口。通过其它 OCR 识别的文本可能不适配。医院的 XML 格式文本也不适配，XML 文件需要经过特殊转换才能直接调用此接口。单次调用传入的文本不宜超过 2000 字。

        :param request: Request instance for TextToObject.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TextToObjectRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TextToObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToObject", params, headers=headers)
            response = json.loads(body)
            model = models.TextToObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TurnPDFToObject(self, request):
        r"""将PDF格式的体检报告文件结构化，解析关键信息。
        注意：该接口是按照体检报告 PDF 页面数量统计次数，不是按照 PDF 文件数量统计次数。通过该接口传入的报告必须是体检报告，非体检报告可能无法正确解析。

        :param request: Request instance for TurnPDFToObject.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TurnPDFToObjectRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TurnPDFToObjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TurnPDFToObject", params, headers=headers)
            response = json.loads(body)
            model = models.TurnPDFToObjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TurnPDFToObjectAsync(self, request):
        r"""体检报告PDF文件结构化-异步接口

        :param request: Request instance for TurnPDFToObjectAsync.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TurnPDFToObjectAsyncRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TurnPDFToObjectAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TurnPDFToObjectAsync", params, headers=headers)
            response = json.loads(body)
            model = models.TurnPDFToObjectAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TurnPDFToObjectAsyncGetResult(self, request):
        r"""体检报告PDF文件结构化异步获取结果接口

        :param request: Request instance for TurnPDFToObjectAsyncGetResult.
        :type request: :class:`tencentcloud.mrs.v20200910.models.TurnPDFToObjectAsyncGetResultRequest`
        :rtype: :class:`tencentcloud.mrs.v20200910.models.TurnPDFToObjectAsyncGetResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TurnPDFToObjectAsyncGetResult", params, headers=headers)
            response = json.loads(body)
            model = models.TurnPDFToObjectAsyncGetResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))