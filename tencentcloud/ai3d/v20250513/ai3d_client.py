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
from tencentcloud.ai3d.v20250513 import models


class Ai3dClient(AbstractClient):
    _apiVersion = '2025-05-13'
    _endpoint = 'ai3d.tencentcloudapi.com'
    _service = 'ai3d'


    def Convert3DFormat(self, request):
        r"""输入3D模型文件后，可进行3D模型文件格式转换。

        :param request: Request instance for Convert3DFormat.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.Convert3DFormatRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.Convert3DFormatResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Convert3DFormat", params, headers=headers)
            response = json.loads(body)
            model = models.Convert3DFormatResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHunyuanTo3DUVJob(self, request):
        r"""查询组件拆分任务。

        :param request: Request instance for DescribeHunyuanTo3DUVJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.DescribeHunyuanTo3DUVJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.DescribeHunyuanTo3DUVJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHunyuanTo3DUVJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHunyuanTo3DUVJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReduceFaceJob(self, request):
        r"""混元生3D接口，采用 Polygon 1.5模型，输入3D 高模后，可生成布线规整，较低面数的3D 模型。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for DescribeReduceFaceJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.DescribeReduceFaceJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.DescribeReduceFaceJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReduceFaceJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReduceFaceJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTextureTo3DJob(self, request):
        r"""混元生3D接口，输入单几何模型和参考图或文字描述后，可生成对应的纹理贴图。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for DescribeTextureTo3DJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.DescribeTextureTo3DJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.DescribeTextureTo3DJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTextureTo3DJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTextureTo3DJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuan3DPartJob(self, request):
        r"""查询组件生成任务。

        :param request: Request instance for QueryHunyuan3DPartJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuan3DPartJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuan3DPartJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuan3DPartJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuan3DPartJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuanTo3DProJob(self, request):
        r"""混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供3个并发，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for QueryHunyuanTo3DProJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuanTo3DProJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuanTo3DProJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanTo3DProJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanTo3DProJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuanTo3DRapidJob(self, request):
        r"""混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for QueryHunyuanTo3DRapidJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuanTo3DRapidJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuanTo3DRapidJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanTo3DRapidJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanTo3DRapidJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuan3DPartJob(self, request):
        r"""输入3D模型文件后，根据模型结构自动进行组件识别生成。

        :param request: Request instance for SubmitHunyuan3DPartJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuan3DPartJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuan3DPartJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuan3DPartJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuan3DPartJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanTo3DProJob(self, request):
        r"""混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供3个并发，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for SubmitHunyuanTo3DProJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DProJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DProJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanTo3DProJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanTo3DProJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanTo3DRapidJob(self, request):
        r"""混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for SubmitHunyuanTo3DRapidJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DRapidJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DRapidJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanTo3DRapidJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanTo3DRapidJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanTo3DUVJob(self, request):
        r"""输入模型后，可根据模型纹理进行UV展开，输出对应UV贴图。

        :param request: Request instance for SubmitHunyuanTo3DUVJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DUVJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DUVJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanTo3DUVJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanTo3DUVJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitReduceFaceJob(self, request):
        r"""混元生3D接口，采用 Polygon 1.5模型，输入3D 高模后，可生成布线规整，较低面数的3D 模型。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for SubmitReduceFaceJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.SubmitReduceFaceJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.SubmitReduceFaceJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitReduceFaceJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitReduceFaceJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTextureTo3DJob(self, request):
        r"""混元生3D接口，输入单几何模型和参考图或文字描述后，可生成对应的纹理贴图。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for SubmitTextureTo3DJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.SubmitTextureTo3DJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.SubmitTextureTo3DJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTextureTo3DJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTextureTo3DJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))